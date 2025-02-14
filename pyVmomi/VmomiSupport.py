# Copyright (c) 2005-2024 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# Support for VMOMI abstractions such as VMODL types, versions, etc.

import base64
import threading
from datetime import datetime
from functools import partial
from sys import version_info

from six import PY3, binary_type

from . import Iso8601
from . import _allowGetSet
from . import _allowCapitalizedNames
from . import _binaryIsBytearray

from functools import cmp_to_key
NoneType = type(None)

try:
    from six.moves import intern
except ImportError:
    # The old version of six package (< 1.8.0) doesn't have intern mapping so
    # we need to tolerate the import error here.
    def intern(s):
        return s

(F_LINK, F_LINKABLE, F_OPTIONAL, F_SECRET) = [1 << x for x in range(4)]

BASE_VERSION = 'vmodl.version.version0'
VERSION1 = 'vmodl.version.version1'

XMLNS_XSD = "http://www.w3.org/2001/XMLSchema"
XMLNS_XSI = "http://www.w3.org/2001/XMLSchema-instance"
XMLNS_VMODL_BASE = "urn:vim25"

# The lock ensures that we serialize the lazy loading. In particular, we need
# to guard against multiple threads loading the same types on the same kind
# of objects at the same time
# The lock is protecting the following variables:
# _topLevelNames, _*DefMap, and _dependencyMap
_lazyLock = threading.RLock()

# Also referenced in __init__.py
_topLevelNames = set()

# Maps to store parameters to create the type for each vmodlName
_managedDefMap = {}
_dataDefMap = {}
_enumDefMap = {}

# Map to store parameters to create the type for each wsdlName
_wsdlDefMap = {}

# Map that stores the nested classes for a given class
# if a.b.c and a.b.d are the nested classes of a.b,
# then _dependencyMap[a.b] = {c,d}
_dependencyMap = {}

# TODO Use a more holistic/data(typeinfo)-driven for all namespaces
# Populate the map in init phase or use the existing maps if possible
# Map top level names to xml namespaces
_urnMap = {"vim": XMLNS_VMODL_BASE, "sms": "urn:sms", "pbm": "urn:pbm"}


# Update the dependency map
# Note: Must be holding the _lazyLock
#
# @param names VmodlName of the type
def _AddToDependencyMap(names):
    """ Note: Must be holding the _lazyLock """
    curName = names[0]
    _topLevelNames.add(curName)
    for name in names[1:]:
        _dependencyMap.setdefault(curName, set()).add(name)
        curName = ".".join([curName, name])


# Check if a particular name is dependent on another
# Note: Must be holding the _lazyLock
#
# @param parent Parent Vmodl name
# @param name Vmodl name to be checked for dependency
# @return True, if name depends on parent, False otherwise
def _CheckForDependency(parent, name):
    """ Note: Must be holding the _lazyLock """
    if _allowCapitalizedNames:
        # If the flag is set, check for both capitalized and
        # uncapitalized form. This is a temporary fix for handling
        # vim.EsxCLI namespace.
        # Ex: If we add vim.EsxCLI.vdisk, then
        # _dependencyMap['vim.EsxCLI'] will have value ['vdisk'].
        # When we try to check dependency for vdisk, since the flag
        # is set, we will uncapitalize EsxCLI and this will result
        # in attribute error
        dependents = _dependencyMap.get(parent)
        if not dependents:
            uncapitalizedParent = UncapitalizeVmodlName(parent)
            dependents = _dependencyMap.get(uncapitalizedParent)

        if dependents:
            if name in dependents or Uncapitalize(name) in dependents:
                return True
    else:
        dependents = _dependencyMap.get(parent)
        if dependents:
            if name in dependents:
                return True
    return False


# Checks for the type definition in all the maps
# and loads it if it finds the definition
#
# @param name vmodl name of the type
# @return vmodl type
def _LoadVmodlType(name):
    isArray = name.endswith("[]")
    if isArray:
        name = name[:-2]
    if _allowCapitalizedNames:
        name = UncapitalizeVmodlName(name)

    with _lazyLock:
        for defMap, loadFn in [(_dataDefMap, LoadDataType),
                               (_managedDefMap, LoadManagedType),
                               (_enumDefMap, LoadEnumType)]:
            dic = defMap.get(name)
            if dic:
                typ = loadFn(*dic)
                return isArray and typ.Array or typ

        return None


# Simple class to store named attributes
class Object:
    # Constructor
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


# All properties and methods in vmodl types are created as LazyObject's
# in VmomiSupport. The attributes in these properties and methods that refer
# to vmodl types are "type", "result" and "methodResult". If a program tries
# to access any of these attributes, load the type. The vmodl name of the type
# can be retrieved by adding name to the attribute that is being accessed
# Creating a derived class of Object so that programs that want to use just
# Object are not affected
class LazyObject(Object):
    def __getattr__(self, attr):
        with _lazyLock:
            # Check if another thread already initialized this
            obj = self.__dict__.get(attr)
            if obj:
                return obj

            if attr == "type" or attr == "result" or attr == "methodResult":
                attrName = attr + "Name"
                vmodlName = getattr(self, attrName)
                vmodlType = GetVmodlType(vmodlName)
                setattr(self, attr, vmodlType)
                delattr(self, attrName)
                return vmodlType
            else:
                raise AttributeError(attr)


class Link(str):
    def __new__(cls, obj):
        if isinstance(obj, str):
            return str.__new__(cls, obj)
        elif isinstance(obj, DataObject):
            if obj.key:
                return str.__new__(cls, obj.key)
            raise AttributeError("DataObject does not have a key to link")
        else:
            raise ValueError


# LazyType to wrap around actual type
# This is used to intercept attribute accesses of a class
# and load the appropriate nested classes on-demand
class LazyType(type):
    def __getattr__(self, attr):
        if attr.endswith("[]"):
            searchName = attr[:-2]
        else:
            searchName = attr

        with _lazyLock:
            nestedClasses = _dependencyMap.get(self.__name__, [])
            if searchName in nestedClasses:
                return GetVmodlType(self.__name__ + "." + attr)
            else:
                return super(LazyType, self).__getattribute__(attr)


# LazyModule class
# Used as a placeholder until the actual type is loaded
# If someone wants to use the type, then it is loaded on-demand
class LazyModule(object):
    def __init__(self, name):
        # name is used to save the current context of the object
        # If it is created because of reference to a.b, name will
        # be a.b
        self.name = name

    def __getattr__(self, attr):
        # If someone tries to introspect the instance of this class
        # using inspect.isclass(), the function will check if the object
        # has __bases__ attr. So, throwing an AttributeError to make it work
        if attr == "__bases__":
            raise AttributeError

        with _lazyLock:
            # Check if we have already loaded the class or object
            # corresponding to this attribute
            obj = self.__dict__.get(attr)
            if obj:
                return obj

            name = ".".join([self.name, attr])
            # Get the actual vmodlName from the type dictionaries
            actualName = _GetActualName(name)
            if actualName:
                typeObj = GetVmodlType(actualName)
            else:
                if _CheckForDependency(self.name, attr):
                    typeObj = LazyModule(name)
                else:
                    urnNS = _urnMap.get(self.name)
                    if urnNS:
                        try:
                            typeObj = GetWsdlType(urnNS, attr)
                        except KeyError:
                            raise AttributeError(attr)
                        except:
                            import sys
                            import traceback
                            sys.exit(traceback.format_exc())
                    else:
                        raise AttributeError(attr)
            setattr(self, attr, typeObj)
            return typeObj

    # If the lazy module is representing a data object,
    # this will get triggered when some code tries to initialize it
    # Load the actual type and pass the arguments to it's init.
    def __call__(self, **kwargs):
        typ = _LoadVmodlType(self.name)
        if typ:
            return typ.__call__(**kwargs)
        else:
            raise AttributeError("'{0}' does not exist".format(self.name))


# Format a python VMOMI object
#
# @param val the object
# @param info the field
# @param indent the level of indentation
# @return the formatted string
def FormatObject(val, info=Object(name="", type=object, flags=0), indent=0):
    start = indent * "   " + (info.name and "{0} = ".format(info.name) or "")
    if val is None:
        result = "<unset>"
    elif isinstance(val, DataObject):
        if info.flags & F_LINK:
            result = "<{0}:{1}>".format(val.__class__.__name__, val.key)
        else:
            result = "({0}) {{\n{1}\n{2}}}".format(
                val.__class__.__name__, ',\n'.join([
                FormatObject(getattr(val, prop.name), prop, indent + 1)
                for prop in val._GetPropertyList()
            ]), indent * "   ")
    elif isinstance(val, ManagedObject):
        if val._serverGuid is None:
            result = "'{0}:{1}'".format(val.__class__.__name__, val._moId)
        else:
            result = "'{0}:{1}:{2}'".format(val.__class__.__name__,
                                            val._serverGuid, val._moId)
    elif isinstance(val, list):
        itemType = getattr(val, 'Item', getattr(info.type, 'Item', object))
        if val:
            item = Object(name="", type=itemType, flags=info.flags)
            vmomiObjects = ',\n'.join(
                [FormatObject(obj, item, indent + 1) for obj in val]
            )
            result = "({0}) [\n{1}\n{2}]".format(
                itemType.__name__, vmomiObjects, indent * "   ")
        else:
            result = "({0}) []".format(itemType.__name__)
    elif isinstance(val, type):
        result = val.__name__
    elif isinstance(val, UnknownManagedMethod):
        # TODO: reuse the base ManagedMethod
        result = val.name
    elif isinstance(val, ManagedMethod):
        result = '{0}.{1}'.format(val.info.type.__name__, val.info.name)
    elif isinstance(val, bool):
        result = val and "true" or "false"
    elif isinstance(val, datetime):
        result = Iso8601.ISO8601Format(val)
    elif isinstance(val, binary):
        result = base64.b64encode(val)
        if PY3:
            # In python3 the bytes result after the base64 encoding has a
            # leading 'b' which causes error when we use it to construct the
            # soap message. Workaround the issue by converting the result to
            # string. Since the result of base64 encoding contains only subset
            # of ASCII chars, converting to string will not change the value.
            result = str(result, 'utf-8')
    else:
        result = repr(val)
    return start + result


# Lookup a property for a given object type
#
# @param type the type
# @param name the name of the property
def GetPropertyInfo(type, name):
    try:
        while name not in type._propInfo:
            type = type.__bases__[0]
        else:
            return type._propInfo[name]
    except Exception:
        raise AttributeError(name)


# VMOMI Managed Object class
class ManagedObject(object):
    _wsdlName = "ManagedObject"
    _propInfo = {}
    _propList = []
    _methodInfo = {}
    _version = BASE_VERSION

    # Constructor
    #
    # @param[in] self self
    # @param[in] moId The ID of this managed object
    # @param[in] stub The stub adapter, if this is a client stub object
    def __init__(self, moId, stub=None, serverGuid=None):
        try:
            moId = intern(moId)
        except:
            pass
        object.__setattr__(self, "_moId", moId)
        object.__setattr__(self, "_stub", stub)
        object.__setattr__(self, "_serverGuid", serverGuid)

    # Invoke a managed method
    #
    # @param info method info
    # @param self The object pointer
    # @param ... arguments
    def _InvokeMethod(info, self, *posargs, **kwargs):
        if len(posargs) > len(info.params):
            s = "s" * (len(info.params) != 1)
            raise TypeError(
                "%s() takes at most %d argument%s (%d given)" %
                (Capitalize(info.name), len(info.params), s, len(posargs)))
        args = list(posargs) + [None] * (len(info.params) - len(posargs))
        if len(kwargs) > 0:
            paramNames = [param.name for param in info.params]
            for (k, v) in list(kwargs.items()):
                try:
                    idx = paramNames.index(k)
                except ValueError:
                    raise TypeError(
                        "%s() got an unexpected keyword argument '%s'" %
                        (Capitalize(info.name), k))
                if idx < len(posargs):
                    raise TypeError(
                        "%s() got multiple values for keyword argument '%s'" %
                        (Capitalize(info.name), k))
                args[idx] = v
        list(map(CheckField, info.params, args))
        return self._stub.InvokeMethod(self, info, args)

    _InvokeMethod = staticmethod(_InvokeMethod)

    # Invoke a managed property accessor
    #
    # @param info property info
    # @param self The object pointer
    def _InvokeAccessor(info, self):
        return self._stub.InvokeAccessor(self, info)

    _InvokeAccessor = staticmethod(_InvokeAccessor)

    # In contrast with the Python convention for "private" methods,
    # the ManagedObject and DataObject method names beginning with
    # an underscore denote public, officially supported system methods.
    # The execution of these methods does not involve a remote call.

    # Get the ID of a managed object
    # Public non-remote method. Officially supported.
    def _GetMoId(self):
        return self._moId

    # Get the serverGuid of a managed object
    # Public non-remote method. Officially supported.
    def _GetServerGuid(self):
        return self._serverGuid

    # Get the stub of a managed object
    # Public non-remote method. Officially supported.
    def _GetStub(self):
        return self._stub

    # Get a list of all properties of this type and base types
    # Public non-remote method. Officially supported.
    #
    # @param cls The managed object type
    @classmethod
    def _GetPropertyList(cls, includeBaseClassProps=True):
        if not includeBaseClassProps:
            return cls._propList
        prop = {}
        result = []
        while cls != ManagedObject:
            # Iterate through props, add info for prop not found in
            # derived class
            result = [
                info for info in cls._propList
                if prop.setdefault(info.name, cls) == cls
            ] + result
            cls = cls.__bases__[0]
        return result

    # Get a list of all methods of this type and base types
    # Public non-remote method. Officially supported.
    #
    # @param cls The managed object type
    @classmethod
    def _GetMethodList(cls):
        meth = {}
        result = []
        while cls != ManagedObject:
            # Iterate through methods, add info for method not found in
            # derived class
            result = [
                info for info in list(cls._methodInfo.values())
                if meth.setdefault(info.name, cls) == cls
            ] + result
            cls = cls.__bases__[0]
        return result

    # Lookup a method for a given managed object type
    # Public non-remote method. Officially supported.
    #
    # @param type the type
    # @param name the name of the property
    @classmethod
    def _GetMethodInfo(type, name):
        while hasattr(type, "_methodInfo"):
            try:
                return type._methodInfo[name]
            except KeyError:
                type = type.__bases__[0]
        raise AttributeError(name)

    def __setattr__(self, *args):
        if self._stub is not None:
            raise Exception("Managed object attributes are read-only")
        else:
            object.__setattr__(self, *args)

    __delattr__ = __setattr__

    if _allowGetSet:

        def __getattr__(self, name):
            if name.startswith("Get"):
                return lambda: getattr(self, name[3].lower() + name[4:])
            elif name.startswith("Set"):
                return lambda val: setattr(self, name[3].lower() + name[4:],
                                           val)
            raise AttributeError(name)

    # The equality test of ManagedObject is for client side only and might
    # not be appropriate for server side objects. The server side object has
    # to override this function if it has a different equality logic
    def __eq__(self, other):
        if other is None:
            return False
        else:
            return (self._moId == other._moId
                    and self.__class__ == other.__class__
                    and self._serverGuid == other._serverGuid)

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return str(self).__hash__()

    __str__ = __repr__ = FormatObject

    # shared with DataObject
    _GetPropertyInfo = classmethod(GetPropertyInfo)


# VMOMI Data Object class
class DataObject(object):
    _wsdlName = "DataObject"
    _propInfo = {}
    _propList = []
    _version = BASE_VERSION

    # Constructor
    #
    # @param info property info
    # @param ... keyword arguments indicate properties
    def __init__(self, **kwargs):
        for property in self._GetPropertyList():
            ptype = property.type
            if issubclass(ptype, list):
                value = ptype()
            elif property.flags & F_OPTIONAL:
                value = None
            elif ptype is bool:
                value = False
            elif issubclass(ptype, Enum):
                value = None
            elif issubclass(ptype, str):
                value = ""
            elif (ptype is long or issubclass(ptype, int)
                  or issubclass(ptype, float)):
                # Take care of byte, short, int, long, float and double
                value = ptype(0)
            else:
                value = None
            object.__setattr__(self, property.name, value)
        for (k, v) in list(kwargs.items()):
            setattr(self, k, v)

    # In contrast with the Python convention for "private" methods,
    # the ManagedObject and DataObject method names beginning with
    # an underscore denote public, officially supported system methods.
    # The execution of these methods does not involve a remote call.

    # Get a list of all properties of this type and base types
    # Public non-remote method. Officially supported.
    #
    # @param cls the data object type
    @classmethod
    def _GetPropertyList(cls, includeBaseClassProps=True):
        if not includeBaseClassProps:
            return cls._propList
        prop = {}
        result = []
        while cls != DataObject:
            # Iterate through props, add info for prop not found in
            # derived class
            result = [
                info for info in cls._propList
                if prop.setdefault(info.name, cls) == cls
            ] + result
            cls = cls.__bases__[0]
        return result

    def __setattr__(self, name, val):
        CheckField(self._GetPropertyInfo(name), val)
        object.__setattr__(self, name, val)

    __str__ = __repr__ = FormatObject

    # shared with ManagedObject
    _GetPropertyInfo = classmethod(GetPropertyInfo)


# Base class for enum types
class Enum(str):
    pass


# Base class for array types
class Array(list):
    __str__ = __repr__ = FormatObject


# Class for curried function objects
#
# Instances of this class are curried python function objects.
# If g = Curry(f, a1,...,an), then g(b1,...,bm) = f(a1,...,an, b1,...,bm)
class Curry(object):
    # Constructor
    #
    # @param self The object pointer
    # @param f the function object
    # @param args arguments to fix
    def __init__(self, f, *args):
        self.f = f
        self.args = args

    def __call__(self, *args, **kwargs):
        args = self.args + args
        return self.f(*args, **kwargs)

    def __get__(self, obj, type):
        if obj:
            # curried methods will receive 'self' *after* any fixed arguments
            return lambda *args, **kwargs: \
                self.f(*(self.args + (obj,) + args), **kwargs)
        return self


# Class for managed object methods
class ManagedMethod(Curry):
    # Constructor
    #
    # @param self The object pointer
    # @param info method info
    def __init__(self, info):
        Curry.__init__(self, ManagedObject._InvokeMethod, info)
        self.info = info


# __setattr__ implementation for MethodFault object.
#
# Exceptions in python3 have __traceback__ attribute that can be
# (and is - by unittest) modified by exception users.  So allow its
# modification although it is not a VMOMI property.  Note that
# __traceback__ cannot be deleted.
def _MethodFaultSetAttr(self, name, value):
    if name == '__traceback__':
        # Call MethodFault.__bases__[1].__setattr__
        Exception.__setattr__(self, name, value)
    else:
        # Call MethodFault.__bases__[0].__setattr__
        DataObject.__setattr__(self, name, value)


# Generic method representing unknown API methods returned by the server.
# Server may return unknown method name due to server defects or newer version.
class UnknownManagedMethod(ManagedMethod):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        raise Exception("Managed method {} is not available".format(self.name))


# Create the vmodl.MethodFault type
#
# This type must be generated dynamically because it inherits from
# vmodl.DynamicData, which is created dynamically by the emitted code.
#
# @return the new type
def CreateAndLoadMethodFaultType():
    with _lazyLock:
        props = [
            ["msg", "string", BASE_VERSION, F_OPTIONAL],
            [
                "faultCause", "vmodl.MethodFault",
                "vmodl.version.version1", F_OPTIONAL
            ],
            [
                "faultMessage", "vmodl.LocalizableMessage[]",
                "vmodl.version.version1", F_OPTIONAL
            ]
        ]
        propInfo = {}
        propList = [
            LazyObject(name=p[0], typeName=p[1], version=p[2], flags=p[3])
            for p in props
        ]
        dic = {
            "_wsdlName": "MethodFault",
            "_propInfo": propInfo,
            "_propList": propList,
            "_version": BASE_VERSION,
            "__setattr__": _MethodFaultSetAttr,
        }
        for info in propList:
            propInfo[info.name] = info
        name = "vmodl.MethodFault"
        CreateDataType("vmodl.MethodFault", "MethodFault", "vmodl.DynamicData",
                       BASE_VERSION, props)
        return _AddType(
            type(Exception)(
                name,
                (GetWsdlType(XMLNS_VMODL_BASE, "DynamicData"), Exception),
                dic))


# If the name of nested class of vmodl type is same as one of the nested
# classes of its parent, then we have to replace it. Else it won't be possible
# to intercept it with LazyType class
# @param vmodl type
# @param parent of the vmodl type
# @return vmodl type
def _CheckNestedClasses(typ, parent):
    with _lazyLock:
        vmodlName = typ.__name__
        nestedClasses = _dependencyMap.get(vmodlName, [])
        for nestedClass in nestedClasses:
            if hasattr(parent, nestedClass):
                setattr(typ, nestedClass,
                        GetVmodlType(vmodlName + "." + nestedClass))
        return typ


# A flag to control whether new type definitions will be frozen
_freezeDefintions = False

# Control whether new type definitions will be frozen. When True is passed,
# subsequent calls to CreateDataType, CreateManagedType and CreateEnumType will
# mark the new type definition as frozen. When False is passed, the usual
# mode will be restored.
def SetFreezeDefinitions(enabled):
    global _freezeDefintions
    _freezeDefintions = enabled

# The set of frozen names, specified as (namespace, name) pairs. This set is
# accessible only to the _TryFreezeName and _IsNameFrozen
# functions.
_frozenNames = set()

# If the _freezeDefinitions flag is True, adds the type to the set of frozen
# type definitions. Otherwise has no effect.
def _TryFreezeName(typeNs, name, frozenNames):
    if _freezeDefintions:
        frozenNames.add((typeNs, intern(name)))

_TryFreezeName = partial(_TryFreezeName, frozenNames = _frozenNames)

# Checks whether the specified type has been frozen
def _IsNameFrozen(typeNs, name, frozenNames):
    return (typeNs, intern(name)) in frozenNames

_IsNameFrozen = partial(_IsNameFrozen, frozenNames = _frozenNames)

# Make the frozen types set inaccessible outside the two functions which use it
del _frozenNames


# Create and Load a data object type at once
#
# @param vmodlName the VMODL name of the type
# @param wsdlName the WSDL name of the type
# @param parent the VMODL name of the parent type
# @param version the version of the type
# @param props properties of the type
# @return vmodl type
def CreateAndLoadDataType(vmodlName, wsdlName, parent, version, props):
    CreateDataType(vmodlName, wsdlName, parent, version, props)
    return LoadDataType(vmodlName, wsdlName, parent, version, props)


# Create a data object type
#
# @param vmodlName the VMODL name of the type
# @param wsdlName the WSDL name of the type
# @param parent the VMODL name of the parent type
# @param version the version of the type
# @param props properties of the type
def CreateDataType(vmodlName, wsdlName, parent, version, props):
    with _lazyLock:
        typeNs = GetInternedWsdlNamespace(version)
        if _IsNameFrozen(typeNs, wsdlName):
            return

        dic = [vmodlName, wsdlName, parent, version, props]
        names = vmodlName.split(".")
        if _allowCapitalizedNames:
            vmodlName = ".".join(name[0].lower() + name[1:] for name in names)
        _AddToDependencyMap(names)

        _dataDefMap[vmodlName] = dic
        _wsdlDefMap[(typeNs, wsdlName)] = dic
        _wsdlTypeMapNSs.add(typeNs)

        _TryFreezeName(typeNs, wsdlName)


# Load a data object type
# This function also loads the parent of the type if it's not loaded yet
#
# @param vmodlName the VMODL name of the type
# @param wsdlName the WSDL name of the type
# @param parent the VMODL name of the parent type
# @param version the version of the type
# @param props properties of the type
# @return the new data object type
def LoadDataType(vmodlName, wsdlName, parent, version, props):
    with _lazyLock:
        # Empty lists are saved as None in globals maps as it is much more
        # memory efficient. PythonStubEmitter files emit empty lists as None.
        if props is None:
            props = []
        propList = []
        for p in props:
            # DataObject Property does not contain the privilege for emitted
            # types. However, DynamicTypeConstructor from
            # DynamicTypeManagerHelper.py creates DataTypes with properties
            # containing privilege id.
            name, typeName, propVersion, flags = p[:4]
            if flags & F_LINK:
                if typeName.endswith("[]"):
                    linkType = "Link[]"
                else:
                    linkType = "Link"
                obj = LazyObject(name=name,
                                 typeName=linkType,
                                 version=propVersion,
                                 flags=flags,
                                 expectedType=typeName)
            else:
                obj = LazyObject(name=name,
                                 typeName=typeName,
                                 version=propVersion,
                                 flags=flags)
            propList.append(obj)
        propInfo = {}
        for info in propList:
            propInfo[info.name] = info
        dic = {
            "_wsdlName": wsdlName,
            "_propInfo": propInfo,
            "_propList": propList,
            "_version": version
        }

        if _allowGetSet:
            for property in propList:
                name = property.name
                suffix = name[0].upper() + name[1:]
                tGlobals = {}
                exec(
                    'def Get%s(self): return getattr(self, "%s")' %
                    (suffix, name) + '\n' +
                    'def Set%s(self, v): setattr(self, "%s", v)' %
                    (suffix, name), tGlobals, dic)

        vmodlParent = GetVmodlType(parent)
        result = _AddType(LazyType(vmodlName, (vmodlParent, ), dic))

        # MethodFault and RuntimeFault are builtin types, but MethodFault
        # extends DynamicData, which is (erroneously?) an emitted type, so we
        # can't create MethodFault and RuntimeFault until we have loaded
        # DynamicData
        if wsdlName == "DynamicData":
            CreateAndLoadMethodFaultType()
            CreateAndLoadDataType("vmodl.RuntimeFault", "RuntimeFault",
                                  "vmodl.MethodFault", BASE_VERSION, [])
            # Strictly speaking LocalizedMethodFault is not a data object type
            # (it can't be used in VMODL) But it can be treated as a data
            # object for (de)serialization purpose
            CreateAndLoadDataType(
                "vmodl.LocalizedMethodFault", "LocalizedMethodFault",
                "vmodl.MethodFault", BASE_VERSION, [
                    ("fault", "vmodl.MethodFault", BASE_VERSION, 0),
                    ("localizedMessage", "string", BASE_VERSION, F_OPTIONAL),
                ])

        return _CheckNestedClasses(result, vmodlParent)


# Create and Load a managed object type at once
#
# @param vmodlName the VMODL name of the type
# @param wsdlName the WSDL name of the type
# @param parent the VMODL name of the parent type
# @param version the version of the type
# @param props properties of the type
# @param methods methods of the type
# @return vmodl type
def CreateAndLoadManagedType(vmodlName, wsdlName, parent, version, props,
                             methods):
    CreateManagedType(vmodlName, wsdlName, parent, version, props, methods)
    return LoadManagedType(vmodlName, wsdlName, parent, version, props,
                           methods)


# Create a managed object type
#
# @param vmodlName the VMODL name of the type
# @param wsdlName the WSDL name of the type
# @param parent the VMODL name of the parent type
# @param version the version of the type
# @param props properties of the type
# @param methods methods of the type
def CreateManagedType(vmodlName, wsdlName, parent, version, props, methods):
    with _lazyLock:
        typeNs = GetInternedWsdlNamespace(version)
        if _IsNameFrozen(typeNs, wsdlName):
            return

        dic = [vmodlName, wsdlName, parent, version, props, methods]
        names = vmodlName.split(".")
        if _allowCapitalizedNames:
            vmodlName = ".".join(name[0].lower() + name[1:] for name in names)

        _AddToDependencyMap(names)

        if methods:
            for meth in methods:
                # We need to use method namespace to avoid duplicate wsdl
                # method issue when to find wsdl method from managed type
                # namespace for vSAN vmodls that can have different version
                # namespaces for managed methods and managed object type.
                methNs = GetInternedWsdlNamespace(meth[2])
                _SetWsdlMethod(methNs, meth[1], dic)

        _managedDefMap[vmodlName] = dic
        _wsdlDefMap[(typeNs, wsdlName)] = dic
        _wsdlTypeMapNSs.add(typeNs)

        _TryFreezeName(typeNs, wsdlName)


# Load a managed object type
# This function also loads the parent of the type if it's not loaded yet
#
# @param vmodlName the VMODL name of the type
# @param wsdlName the WSDL name of the type
# @param parent the VMODL name of the parent type
# @param version the version of the type
# @param props properties of the type
# @param methods methods of the type
# @return the new managed object type
def LoadManagedType(vmodlName, wsdlName, parent, version, props, methods):
    with _lazyLock:
        # Empty lists are saved as None in globals maps as it is much more
        # memory efficient. PythonStubEmitter files emit empty lists as None.
        if props is None:
            props = []
        if methods is None:
            methods = []
        parent = GetVmodlType(parent)
        propInfo = {}
        methodInfo = {}
        propList = [
            LazyObject(name=p[0],
                       typeName=p[1],
                       version=p[2],
                       flags=p[3],
                       privId=p[4]) for p in props
        ]
        dic = {
            "_wsdlName": wsdlName,
            "_propInfo": propInfo,
            "_propList": propList,
            "_methodInfo": methodInfo,
            "_version": version
        }
        for info in propList:
            propInfo[info.name] = info
            getter = Curry(ManagedObject._InvokeAccessor, info)
            dic[info.name] = property(getter)
        for (mVmodl, mWsdl, mVersion, mParams, mResult, mPrivilege,
             mFaults) in methods:
            if mFaults is None:
                mFaults = []
            mName = Capitalize(mVmodl)
            isTask = False
            if mWsdl.endswith("_Task"):
                isTask = True
            params = tuple([
                LazyObject(name=p[0],
                           typeName=p[1],
                           version=p[2],
                           flags=p[3],
                           privId=p[4]) for p in mParams
            ])
            info = LazyObject(name=mName,
                              typeName=vmodlName,
                              wsdlName=mWsdl,
                              version=mVersion,
                              params=params,
                              isTask=isTask,
                              resultFlags=mResult[0],
                              resultName=mResult[1],
                              methodResultName=mResult[2],
                              privId=mPrivilege,
                              faults=mFaults)
            methodInfo[mName] = info
            mm = ManagedMethod(info)
            ns = GetInternedWsdlNamespace(info.version)
            method = _SetWsdlMethod(ns, info.wsdlName, mm)
            if method != mm:
                raise RuntimeError("Duplicate wsdl method {0} {1} "
                                   "(new class {2} vs existing {3})".format(
                    ns, info.wsdlName, mm.info.type, method.info.type))
            dic[mWsdl] = mm
            dic[mName] = mm
        name = vmodlName
        result = _AddType(LazyType(name, (parent, ), dic))

        return _CheckNestedClasses(result, parent)


# Create an enum type
#
# @param vmodlName the VMODL name of the type
# @param wsdlName the WSDL name of the type
# @param version the version of the type
# @param values enum values
# @return vmodl type
def CreateAndLoadEnumType(vmodlName, wsdlName, version, values):
    CreateEnumType(vmodlName, wsdlName, version, values)
    return LoadEnumType(vmodlName, wsdlName, version, values)


# Create an enum type
#
# @param vmodlName the VMODL name of the type
# @param wsdlName the WSDL name of the type
# @param version the version of the type
# @param values enum values
def CreateEnumType(vmodlName, wsdlName, version, values):
    with _lazyLock:
        typeNs = GetInternedWsdlNamespace(version)
        if _IsNameFrozen(typeNs, wsdlName):
            return

        dic = [vmodlName, wsdlName, version, values]
        names = vmodlName.split(".")
        if _allowCapitalizedNames:
            vmodlName = ".".join(name[0].lower() + name[1:] for name in names)

        _AddToDependencyMap(names)

        _enumDefMap[vmodlName] = dic
        _wsdlDefMap[(typeNs, wsdlName)] = dic
        _wsdlTypeMapNSs.add(typeNs)

        _TryFreezeName(typeNs, wsdlName)


# Load an enum type
#
# @param vmodlName the VMODL name of the type
# @param wsdlName the WSDL name of the type
# @param version the version of the type
# @param values enum values
# @return the new enum type
def LoadEnumType(vmodlName, wsdlName, version, values):
    with _lazyLock:
        name = vmodlName
        # Enum type cannot have nested classes. So, creating normal type
        # instead of LazyType
        result = type(name, (Enum, ), {
            "_wsdlName": wsdlName,
            "_version": version
        })
        result.values = list(map(result, values))
        for value in result.values:
            setattr(result, value, value)
        return _AddType(result)


# Create an array type
#
# @param itemType the item type
# @return the new array type
def CreateArrayType(itemType):
    return type("{0}[]".format(itemType.__name__), (Array, ), {'Item': itemType})


# Add a new type to the type maps, create array constructors
# Note: Must be holding the _lazyLock, or in main init path
#
# @param type the type object
# @return type
def _AddType(type):
    """ Note: Must be holding the _lazyLock, or in main init path """
    type.Array = CreateArrayType(type)

    typeNS = GetInternedWsdlNamespace(type._version)
    newType = _SetWsdlType(typeNS, type._wsdlName, type)
    if newType != type:
        raise RuntimeError("Duplicate wsdl type %s (already in typemap)" %
                           (type._wsdlName))

    return type


def _areBasicTypes(info, valType):
    """Checks whether the provided type matches with the expected and both are
    basic types.

    @param info the expected type
    @param valType the type of the object to check
    """
    return (info is type and valType is type(Exception)
            or issubclass(info, int) and issubclass(valType, int)
            or issubclass(info, long) and (issubclass(valType, int)
                                           or issubclass(valType, long))
            or issubclass(info, float) and issubclass(valType, float)
            or issubclass(info, str) and issubclass(valType, str)
            or issubclass(info, bytes) and issubclass(valType, bytes))


# Check that a value matches a given type, and annotate if neccesary
#
# @param info object containing of expected type
# @param val object to check
# @throw TypeError if the value does not match the type
def CheckField(info, val):
    with _lazyLock:
        valType = Type(val)
        if val is None or (isinstance(val, list) and len(val) == 0):
            # If type of the property is an Any. We should allow this to have
            # unset items
            if not (info.flags & F_OPTIONAL) and info.type is not object:
                raise TypeError(
                    'Required field "%s" not provided (not @optional)' %
                    info.name)
            return
        elif info.type is object:
            try:
                GetQualifiedWsdlName(valType)
                return
            except KeyError:
                raise TypeError('Unknown type for {0}'.format(info.type.__name__))
        elif isinstance(val, info.type):
            return
        elif issubclass(info.type, list):
            # Checking the values of VMOMI array types is surprisingly
            # complicated....
            if isinstance(val, Array):
                # 1. We've got a PyVmomi Array object, which is effectively a
                # typed list;
                # verify that the type of the Array is a subclass of the
                # expected type.
                if issubclass(valType.Item, info.type.Item):
                    return
                elif info.flags & F_LINK:
                    # Allow objects of expected type to be assigned to links
                    if issubclass(valType, GetVmodlType(info.expectedType)):
                        return
                elif issubclass(info.type.Item, Enum) and issubclass(
                        valType.Item, str):
                    # Allow String array object to be assigned to enum array
                    return
            elif val:
                # 2. We've got a non-empty Python list object, which is
                # untyped;
                # walk the list and make sure that each element is a subclass
                # of the expected type.

                # Masking out F_OPTIONAL part of flags since we are checking
                # for each element of the list
                flags = info.flags & (F_LINKABLE | F_LINK)
                if flags & F_LINK:
                    if info.expectedType.endswith('[]'):
                        expectedType = info.expectedType[:-2]
                    else:
                        expectedType = info.expectedType
                    itemInfo = Object(type=info.type.Item,
                                      name=info.name,
                                      flags=flags,
                                      expectedType=expectedType)
                else:
                    itemInfo = Object(type=info.type.Item,
                                      name=info.name,
                                      flags=flags)
                for it in val:
                    CheckField(itemInfo, it)
                return
            else:
                # 3. We've got None or an empty Python list object;
                # no checking required since the result will be an empty array.
                return
        elif _areBasicTypes(info.type, valType):
            return
        elif issubclass(info.type, Link):
            # Allow object of expected type to be assigned to link
            if issubclass(valType, GetVmodlType(info.expectedType)):
                return
        raise TypeError('For "%s" expected type %s, but got %s' %
                        (info.name, info.type.__name__, valType.__name__))


# Finalize a created type
#
# @param type a created type
def FinalizeType(type):
    if issubclass(type, DataObject):
        for info in type._propList:
            info.type = GetVmodlType(info.type)
    elif issubclass(type, ManagedObject):
        for info in list(type._propInfo.values()):
            info.type = GetVmodlType(info.type)
        for info in list(type._methodInfo.values()):
            info.result = GetVmodlType(info.result)
            info.methodResult = GetVmodlType(info.methodResult)
            info.type = GetVmodlType(info.type)
            for param in info.params:
                param.type = GetVmodlType(param.type)


# Get the type of an object, for both new and old-style classes
def Type(obj):
    try:
        return obj.__class__
    except AttributeError:
        return type(obj)


# Set a WSDL type with wsdl namespace and wsdl name Internal to VmomiSupport
# Note: Must be holding the _lazyLock, or in main init path
def _SetWsdlType(ns, wsdlName, typ):
    """
    Set a WSDL type with wsdl namespace and wsdl name.
    Returns added type / existing type if (ns, wsdlName) already in the map

    Note: Must be holding the _lazyLock, or in main init path
    """
    return _wsdlTypeMap.setdefault((ns, wsdlName), typ)


# Lookup a WSDL type from wsdl namespace and wsdl name
#
# @param ns XML namespace
# @param name wsdl name
# @return type if found else throws KeyError
def GetWsdlType(ns, name):
    if ns is None or name is None:
        raise KeyError("{0} {1}".format(ns, name))

    with _lazyLock:
        # Check if the type is loaded in the map
        typ = _wsdlTypeMap.get((ns, name))
        if typ:
            return typ
        # It is an array type, get the actual type and return the array
        elif name.startswith("ArrayOf"):
            try:
                return GetWsdlType(ns, name[7:]).Array
            except KeyError:
                raise KeyError("{0} {1}".format(ns, name))
        else:
            # Type is not loaded yet, load it
            typ = _LoadVmodlType(_wsdlDefMap[(ns, name)][0])
            if typ:
                return typ

        raise KeyError("{0} {1}".format(ns, name))


# Guess the type from wsdlname with no ns
# WARNING! This should not be used in general, as there is no guarantee for
# the correctness of the guessing type
#
# @param name wsdl name
# @return type if found in any one of the name spaces else throws KeyError
def GuessWsdlType(name):
    with _lazyLock:
        # Some types may exist in multiple namespaces, and returning
        # the wrong one will cause a deserialization error (1656837).
        # Since in python3 the order of entries in set is not deterministic,
        # we will try to get the type from vim25 namespace first.
        try:
            return GetWsdlType(XMLNS_VMODL_BASE, name)
        except KeyError:
            pass

        for ns in _wsdlTypeMapNSs:
            try:
                return GetWsdlType(ns, name)
            except KeyError:
                pass
        raise KeyError(name)


# Return a map that contains all the wsdl types
# This function is rarely used
# By calling GetWsdlType on all wsdl names, we will make sure that the
# types are loaded before returning the iterator
#
# @return iterator to the wsdl type map
def GetWsdlTypes():
    with _lazyLock:
        for ns, name in _wsdlDefMap:
            GetWsdlType(ns, name)
        return _wsdlTypeMap.values()


# Get the qualified XML schema name (ns, name) of a type
def GetQualifiedWsdlName(type):
    with _lazyLock:
        wsdlNSAndName = _wsdlNameMap.get(type)
        if wsdlNSAndName:
            return wsdlNSAndName
        else:
            if issubclass(type, list):
                ns = GetWsdlNamespace(type.Item._version)
                return (ns, "ArrayOf" + Capitalize(type.Item._wsdlName))
            else:
                ns = GetWsdlNamespace(type._version)
                return (ns, type._wsdlName)


# Get the WSDL of a type
def GetWsdlName(type):
    return GetQualifiedWsdlName(type)[-1]


# Capitalize a string
def Capitalize(str):
    if str:
        return str[0].upper() + str[1:]
    return str


# Uncapitalize a string
def Uncapitalize(str):
    if str:
        return str[0].lower() + str[1:]
    return str


# To uncapitalize the entire vmodl name pyVmomi used to map Java package
# names to capitalized Python module names, but now maps the Java
# package names unchanged to Python module names.
# This function is needed to support the legacy name mapping.
def UncapitalizeVmodlName(str):
    if str:
        return ".".join(name[0].lower() + name[1:] for name in str.split("."))
    return str


# Add a parent version
def AddVersionParent(version, parent):
    parentMap[version].add(parent)


def CreateVersion(version, ns, versionId, isLegacy, serviceNs):
    """
    The primitive for creating and registering a version, used by
    AddVersion() implementations (Fling and proprietary).
    """
    if not ns:
        ns = serviceNs
    if version not in parentMap:
        nsMap[version] = ns
        if len(versionId) > 0:
            versionMap[ns + '/' + versionId] = version
        if isLegacy or ns == "":
            versionMap[ns] = version
        versionIdMap[version] = versionId
        if not serviceNs:
            serviceNs = ns
        serviceNsMap[version] = serviceNs
        parentMap[version] = set()


def GetVersionProps(version):
    """Get version properties

    This function is a fixed version of GetVersion().
    """

    ns = nsMap[version]
    versionId = versionIdMap[version]
    isLegacy = versionMap.get(ns) == version
    serviceNs = serviceNsMap[version]
    return ns, versionId, isLegacy, serviceNs


# Get version namespace from version
def GetVersionNamespace(version):
    """ Get version namespace from version """
    ns = nsMap[version]
    if not ns:
        ns = serviceNsMap[version]
    versionId = versionIdMap[version]
    if not versionId:
        namespace = ns
    else:
        namespace = '{0}/{1}'.format(ns, versionId)
    return namespace


# Get version from the version uri
def GetVersionFromVersionUri(version):
    return versionMap[version.rsplit(":", 1)[-1]]


# Get wsdl namespace from version
def GetWsdlNamespace(version):
    """ Get wsdl namespace from version """
    return "urn:" + serviceNsMap[version]


def GetInternedWsdlNamespace(version):
    """ Get interned wsdl namespace from version """
    return intern(GetWsdlNamespace(version))


# Get an iterable with all version parents
def GetVersionParents(version):
    return parentMap[version]


# Get all the versions for the service with specified namespace (partially)
# ordered by compatibility (i.e. any version in the list that is compatible
# with some version v in the list will preceed v)
#
# @param namespace XML namespace identifying a service
# @return returns all the versions for the service with specified
#                 namespace (partially) ordered by compatibility
#
# NOTE:
# For this function, we use 'namespace' as a representation of 'service'.
# While this works for most services, for compatibility reasons, the core and
# query services share the 'vim25' namespace with the vim service.
# Fortunately, this shouldn't be an issue in practice, as the implementations
# of the vim service (vpxd and hostd) don't currently advertise that they
# support any versions of the core or query services, and we don't expect that
# they ever will. This function assumes that all other namespaces identify a
# unique service.
def GetServiceVersions(namespace):
    """
    Get all the versions for the service with specified namespace (partially)
    ordered by compatibility (i.e. any version in the list that is compatible
    with some version v in the list will preceed v)
    """
    def compare(a, b):
        if a == b:
            return 0
        if b in parentMap[a]:
            return -1
        if a in parentMap[b]:
            return 1
        return (a > b) - (a < b)

    return sorted(
            [v for (v, n) in serviceNsMap.items() if n == namespace],
            key=cmp_to_key(compare))


# Set a WSDL method with wsdl namespace and wsdl name
#  Internal to VmomiSupport
#  Note: Must be holding the _lazyLock
#
# @param ns XML namespace
# @param wsdlName wsdl name
# @param inputMM managed method object or info to load it (it points to
#                list object that points to the type info which holds
#                this managed method's information)
# @return returns added method or exising method if (ns, wsdlName)
#                 is already in the map. It throws a runtime error if
#                 trying to set two type info list's to the same (ns, wsdlName)
def _SetWsdlMethod(ns, wsdlName, inputMM):
    """
    Set a WSDL method with wsdl namespace and wsdl name
    Returns added method / existing method if (ns, wsdlName) already in the map

    Note: Must be holding the _lazyLock
    """
    _wsdlMethodNSs.add(ns)
    curMM = _wsdlMethodMap.get((ns, wsdlName))
    # if inputMM is a list
    if isinstance(inputMM, list):
        if curMM is None:
            _wsdlMethodMap[(ns, wsdlName)] = inputMM
            return inputMM
        elif isinstance(curMM, list):
            raise RuntimeError(
                "Duplicate wsdl method %s %s (new class %s vs existing %s)" %
                (ns, wsdlName, inputMM[0], curMM[0]))
        else:
            return curMM
    # if inputMM is a ManagedMethod
    else:
        if curMM is None or isinstance(curMM, list):
            _wsdlMethodMap[(ns, wsdlName)] = inputMM
            return inputMM
        else:
            return curMM


# Get wsdl method from ns, wsdlName
#
# @param ns XML namespace
# @param wsdlName wsdl name
# @return managed method object or throws a KeyError
def GetWsdlMethod(ns, wsdlName):
    """ Get wsdl method from ns, wsdlName """
    with _lazyLock:
        method = _wsdlMethodMap[(ns, wsdlName)]
        if isinstance(method, ManagedMethod):
            # The type corresponding to the method is loaded,
            # just return the method object
            return method
        elif method:
            # The type is not loaded, the map contains the info
            # to load the type. Load the actual type and
            # return the method object
            LoadManagedType(*method)
            return _wsdlMethodMap[(ns, wsdlName)]
        else:
            raise KeyError("{0} {1}".format(ns, wsdlName))


# Guess the method from wsdlname with no ns
# WARNING! This should not be used in general, as there is no guarantee for
# the correctness of the guessing method
#
# @param name wsdl name
# @return managed method object if found in any namespace else throws KeyError
def GuessWsdlMethod(name):
    with _lazyLock:
        # Some methods may exist in multiple namespaces, and returning
        # the wrong one will cause a deserialization error (1656837).
        # Since in python3 the order of entries in set is not deterministic,
        # we will try to get the method from vim25 namespace first.
        try:
            return GetWsdlMethod(XMLNS_VMODL_BASE, name)
        except KeyError:
            pass

        for ns in _wsdlMethodNSs:
            try:
                return GetWsdlMethod(ns, name)
            except KeyError:
                pass
        raise KeyError(name)


# Widen a type to one supported in a given version
def GetCompatibleType(type, version):
    # Type can be widened if it has the attribute "_version" (which implies it
    # is either a DataObject or ManagedObject)
    if hasattr(type, "_version"):
        while not IsChildVersion(version, type._version):
            type = type.__bases__[0]
    return type


# Invert an injective mapping
def InverseMap(map):
    return dict([(v, k) for (k, v) in map.items()])


def GetVmodlNs(version):
    versionParts = version.split('.version.')
    assert len(versionParts) == 2, 'Unsupported version format: {0}'.format(version)
    return versionParts[0]


types = Object()

nsMap = {}  # e.g. 'vim.version.version12' -> 'vim25'
versionIdMap = {}  # e.g. 'vim.version.version12' -> '6.7'
versionMap = {}  # e.g. 'vim25/6.7' -> 'vim.version.version12'
# also 'vim25' -> 'vim.version.version3'

parentMap = {}  # e.g. 'vim.version.version12' -> set(
#          'vim.version.version11',
#          'vim.version.version10',
#          ...
#          'vmodl.version.version0'
#      )

serviceNsMap = {BASE_VERSION: XMLNS_VMODL_BASE.split(":")[-1]}


class _MaturitySet:
    """
    Registry for versions from all namespaces defining a given maturity.
    The registration is automatic (relevant code is generated by emitters),
    while for the query one may use either the VMODL namespace id (e.g. 'vim'),
    or the wire namespace id (e.g. 'vim25').
    """
    def __init__(self):
        self._verNameMap = {}  # e.g. 'vim'   -> 'vim.version.version12'
        self._verNameMapW = {}  # e.g. 'vim25' -> 'vim.version.version12'
        self._wireIdMap = {}  # e.g. 'vim'   -> 'vim25/6.7'
        self._wireIdMapW = {}  # e.g. 'vim25' -> 'vim25/6.7'

    def Add(self, version):
        """
        Register the version at corresponding maturity for a given VMODL
        namespace. The 'version' parameter is in the VMODL name format
        e.g. 'vim.version.version12'. This method is typically used by
        auto-generated code.
        """
        vmodlNs = GetVmodlNs(version)

        wireId = GetVersionNamespace(version)
        wireNs = wireId.split('/')[0]

        # We use the string representation of the instance as unique name
        if not _IsNameFrozen(wireNs, str(self)):
            self._verNameMap[vmodlNs] = version
            self._verNameMapW[wireNs] = version
            self._wireIdMap[vmodlNs] = wireId
            self._wireIdMapW[wireNs] = wireId
            _TryFreezeName(wireNs, str(self))


        return wireId, wireNs

    def GetName(self, vmodlNs):
        """
        VMODL namespace to registered version name mapping, e.g.
        'vim' -> 'vim.version.version12'
        """
        return self._verNameMap[vmodlNs]

    def GetNameW(self, wireNs):
        """
        Wire namespace to registered version name mapping, e.g.
        'vim25' -> 'vim.version.version12'
        """
        return self._verNameMapW[wireNs]

    def GetWireId(self, vmodlNs):
        """
        VMODL namespace to registered version wire-id mapping, e.g.
        'vim' -> 'vim25/6.7'
        """
        return self._wireIdMap[vmodlNs]

    def GetWireIdW(self, wireNs):
        """
        Wire namespace to registered version wire-id mapping, e.g.
        'vim25' -> 'vim25/6.7'
        """
        return self._wireIdMapW[wireNs]

    def EnumerateVmodlNs(self):
        """
        Returns an iterable with registered VMODL namespace, e.g.
        ['vim', 'vpx', ... ]
        """
        return self._verNameMap.keys()

    def EnumerateWireNs(self):
        """
        Returns an iterable with registered wire namespace, e.g.
        ['vim25', 'vpxd3', ... ]
        """
        return self._verNameMapW.keys()

    def EnumerateVersions(self):
        """
        Returns an iterable with registered VMODL versions, e.g.
        ['vim.version.version12', 'vpx.version.version12', ... ]
        """
        return self._verNameMap.values()

    def EnumerateWireIds(self):
        """
        Returns an iterable with registered versions wire-ids, e.g.
        e.g. ['vim25/6.7', 'vpxd3/6.7', ... ]
        """
        return self._wireIdMap.values()


# Backward compatibility aliases
_MaturitySet.Get = _MaturitySet.GetName
_MaturitySet.GetNamespace = _MaturitySet.GetWireId

from .Version import Init as _VersionInit  # noqa: E402
_VersionInit()

newestVersions = _MaturitySet()
ltsVersions = _MaturitySet()
oldestVersions = _MaturitySet()

# Deprecated
# Alias for backward compatibility. Required until VMC M11 is phased out.
publicVersions = ltsVersions
dottedVersions = ltsVersions

# AddVersion is not used in this module however it is imported from it in the
# generated bindings so removing it will break the world.
from .Version import AddVersion, IsChildVersion  # noqa: E402, F401

byte = type("byte", (int, ), {})
short = type("short", (int, ), {})
double = type("double", (float, ), {})
if PY3:
    long = type("long", (int, ), {})
URI = type("URI", (str, ), {})
if not PY3 and _binaryIsBytearray:
    # six defines binary_type in python2 as a string; this means the
    # JSON encoder sees checksum properties as strings and attempts
    # to perform utf-8 decoding on them because they contain high-bit
    # characters.
    binary = type("binary", (bytearray,), {})
else:
    binary = type("binary", (binary_type,), {})
PropertyPath = type("PropertyPath", (str, ), {})

# _wsdlTypeMapNSs store namespaces added to _wsdlTypeMap in _SetWsdlType
_wsdlTypeMapNSs = set()
_wsdlTypeMap = {
    # Note: xsd has no void type. This is a hack from before. Can be removed?
    (XMLNS_XSD, 'void'):
    NoneType,
    (XMLNS_XSD, 'anyType'):
    object,
    (XMLNS_XSD, 'boolean'):
    bool,
    (XMLNS_XSD, 'byte'):
    byte,
    (XMLNS_XSD, 'short'):
    short,
    (XMLNS_XSD, 'int'):
    int,
    (XMLNS_XSD, 'long'):
    long,
    (XMLNS_XSD, 'float'):
    float,
    (XMLNS_XSD, 'double'):
    double,
    (XMLNS_XSD, 'string'):
    str,
    (XMLNS_XSD, 'anyURI'):
    URI,
    (XMLNS_XSD, 'base64Binary'):
    binary,
    (XMLNS_XSD, 'dateTime'):
    datetime,
    (XMLNS_XSD, 'Link'):
    Link,
    (XMLNS_VMODL_BASE, 'TypeName'):
    type,
    (XMLNS_VMODL_BASE, 'MethodName'):
    ManagedMethod,
    (XMLNS_VMODL_BASE, 'PropertyPath'):
    PropertyPath
}
_wsdlNameMap = InverseMap(_wsdlTypeMap)

for ((ns, name), typ) in list(_wsdlTypeMap.items()):
    if typ is not NoneType:
        setattr(types, typ.__name__, typ)
        _wsdlTypeMapNSs.add(ns)
        arrayType = CreateArrayType(typ)
        setattr(types, Capitalize(typ.__name__) + "Array", arrayType)
        arrayName = "ArrayOf" + Capitalize(name)
        arrayNS = XMLNS_VMODL_BASE
        _SetWsdlType(arrayNS, arrayName, arrayType)
        _wsdlNameMap[arrayType] = (arrayNS, arrayName)
del name, typ

# unicode is mapped to wsdl name 'string' (Cannot put in wsdlTypeMap or name
# collision with non-unicode string)
_wsdlNameMap[str] = (XMLNS_XSD, 'string')
_wsdlNameMap[CreateArrayType(str)] = (XMLNS_VMODL_BASE,
                                                'ArrayOfString')

# _wsdlMethodNSs store namespaces added to _wsdlMethodMap in _SetWsdlMethod
_wsdlMethodNSs = set()
_wsdlMethodMap = {}

# Registering the classes defined in VmomiSupport in the definition maps
CreateManagedType(ManagedObject.__name__, ManagedObject._wsdlName, None,
                  ManagedObject._version, [], [])
_AddType(ManagedObject)
setattr(types, ManagedObject.__name__, ManagedObject)

CreateDataType(DataObject.__name__, DataObject._wsdlName, None,
               DataObject._version, [])
_AddType(DataObject)
setattr(types, DataObject.__name__, DataObject)

# Vmodl types
vmodlTypes = {
    # Note: xsd has no void type. This is a hack from before. Can be removed?
    "void": GetWsdlType(XMLNS_XSD, 'void'),
    "anyType": GetWsdlType(XMLNS_XSD, 'anyType'),
    "string": GetWsdlType(XMLNS_XSD, 'string'),
    "bool": GetWsdlType(XMLNS_XSD, 'boolean'),
    "boolean": GetWsdlType(XMLNS_XSD, 'boolean'),
    "byte": GetWsdlType(XMLNS_XSD, 'byte'),
    "short": GetWsdlType(XMLNS_XSD, 'short'),
    "int": GetWsdlType(XMLNS_XSD, 'int'),
    "long": GetWsdlType(XMLNS_XSD, 'long'),
    "float": GetWsdlType(XMLNS_XSD, 'float'),
    "double": GetWsdlType(XMLNS_XSD, 'double'),
    "Link": GetWsdlType(XMLNS_XSD, 'Link'),
    "vmodl.URI": GetWsdlType(XMLNS_XSD, 'anyURI'),
    "vmodl.Binary": GetWsdlType(XMLNS_XSD, 'base64Binary'),
    "vmodl.DateTime": GetWsdlType(XMLNS_XSD, 'dateTime'),
    "vmodl.TypeName": GetWsdlType(XMLNS_VMODL_BASE, 'TypeName'),
    "vmodl.MethodName": GetWsdlType(XMLNS_VMODL_BASE, 'MethodName'),
    "vmodl.DataObject": GetWsdlType(XMLNS_VMODL_BASE, 'DataObject'),
    "vmodl.ManagedObject": GetWsdlType(XMLNS_VMODL_BASE, 'ManagedObject'),
    "vmodl.PropertyPath": GetWsdlType(XMLNS_VMODL_BASE, 'PropertyPath'),
}
vmodlNames = {}


# Add array type into special names
for name, typ in vmodlTypes.copy().items():
    if typ is not NoneType:
        try:
            arrayType = typ.Array
        except AttributeError:
            wsdlName = GetWsdlName(typ)
            arrayNS = XMLNS_VMODL_BASE
            arrayType = GetWsdlType(arrayNS, "ArrayOf" + Capitalize(wsdlName))
        arrayName = name + "[]"
        vmodlTypes[arrayName] = arrayType

    # Set type to vmodl name map
    if name != "bool":
        vmodlNames[typ] = name
        vmodlNames[arrayType] = arrayName
del name, typ


# Get type from vmodl name
#
# @param name vmodl name
# @return vmodl type
def GetVmodlType(name):
    """ Get type from vmodl name """

    # If the input is already a type, just return
    if isinstance(name, type):
        return name

    # Try to get type from vmodl type names table
    typ = vmodlTypes.get(name)
    if typ:
        return typ

    # Else get the type from the _wsdlTypeMap
    isArray = name.endswith("[]")
    if isArray:
        name = name[:-2]
    ns, wsdlName = _GetWsdlInfo(name)
    try:
        typ = GetWsdlType(ns, wsdlName)
    except KeyError:
        raise KeyError(name)
    if typ:
        return isArray and typ.Array or typ
    else:
        raise KeyError(name)


# List the VMODL types in the specified definitions
#
# @param defs Specifies the definitions from which to extract the names
# @return a new list of the VMODL names in the specified dictionary
def _ListVmodlTypes(defs):
    with _lazyLock:
        return list(defs.keys())


# List all VMODL data types
#
# @return a new list of the VMODL names of all data types
def ListDataTypes():
    return _ListVmodlTypes(_dataDefMap)


# List all VMODL managed types
#
# @return a new list of the VMODL names of all managed types
def ListManagedTypes():
    return _ListVmodlTypes(_managedDefMap)


# List all VMODL enum types
#
# @return a new list of the VMODL names of all enum types
def ListEnumTypes():
    return _ListVmodlTypes(_enumDefMap)


# Get VMODL type name from type
#
# @param typ vmodl type
# @return vmodl name
def GetVmodlName(typ):
    """ Get vmodl type name from type """
    try:
        return vmodlNames[typ]
    except KeyError:
        return typ.__name__


# Get Wsdl type name from Python type name
#
# @param pythonTypeName Python type name
# @return wsdl type name
def GetWsdlTypeName(pythonTypeName):
    try:
        typ = GetVmodlType(pythonTypeName)
    except KeyError:
        raise NameError('No type found with name ' + pythonTypeName)
    return GetWsdlName(typ)


# Get Wsdl method name from Python method name
#
# @param pythonTypeName Python type name
# @param pythonMethodName Python method name
# @return wsdl method name
def GetWsdlMethodName(pythonTypeName, pythonMethodName):
    try:
        typ = GetVmodlType(pythonTypeName)
        _, _, _, _, _, methods = _wsdlDefMap[GetQualifiedWsdlName(typ)]
    except KeyError:
        raise NameError('No type found with name ' + pythonTypeName)
    uncapPythonMethodName = Uncapitalize(pythonMethodName)
    for method in methods:
        mVmodl, mWsdl, _, _, _, _, _ = method
        if mVmodl == uncapPythonMethodName or mVmodl == pythonMethodName:
            return mWsdl
    raise NameError('No method found with name ' + pythonMethodName)


# Get Python type name from Wsdl type name
#
# @param ns wsdl namespace
# @param wsdlTypeName wsdl type name
# @return python type name
def GetPythonTypeName(wsdlTypeName, ns):
    try:
        typ = GetWsdlType(ns, wsdlTypeName)
    except KeyError:
        raise NameError('No type found with namespace %s and name %s' %
                        (ns, wsdlTypeName))
    return GetVmodlName(typ)


# Get Python method name from Wsdl method name
#
# @param ns wsdl namespace
# @param wsdlTypeName wsdl type name
# @param wsdlMethodName wsdl method name
# @return python method name
def GetPythonMethodName(wsdlTypeName, ns, wsdlMethodName):
    try:
        _, _, _, _, _, methods = _wsdlDefMap[(ns, wsdlTypeName)]
    except KeyError:
        raise NameError('No type found with namespace %s and name %s' %
                        (ns, wsdlTypeName))
    for method in methods:
        mVmodl, mWsdl, _, _, _, _, _ = method
        if mWsdl == wsdlMethodName:
            return Capitalize(mVmodl)
    raise NameError('No method found with name ' + wsdlMethodName)


# String only dictionary: same as dict, except it only accept string as value
class StringDict(dict):
    """
    String only dictionary: same as dict, except it only accept string as value

    dict in python is kind of strange. U cannot just override __setitem__, as
    __init__, update, and setdefault all bypass __setitem__. When override,
    we have to override all three together
    """
    def __init__(self, *args, **kwargs):
        dict.__init__(self)
        self.update(*args, **kwargs)

    # Same as dict setdefault, except this will call through our __setitem__
    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).items():
            self[k] = v

    # Same as dict setdefault, except this will call through our __setitem__
    def setdefault(self, key, val=None):
        if key in self:
            return self[key]
        else:
            self[key] = val
            return val

    def __setitem__(self, key, val):
        """x.__setitem__(i, y) <==> x[i]=y, where y must be a string"""
        if not isinstance(val, str):
            raise TypeError("key %s has non-string value %s of %s" %
                            (key, val, type(val)))
        return dict.__setitem__(self, key, val)


# Retrieves the actual vmodl name from type dictionaries
# Note: Must be holding the _lazyLock
#
# @param name upcapitalized vmodl name
# @return vmodl name
def _GetActualName(name):
    """ Note: Must be holding the _lazyLock """
    if _allowCapitalizedNames:
        name = UncapitalizeVmodlName(name)
    for defMap in _dataDefMap, _managedDefMap, _enumDefMap:
        dic = defMap.get(name)
        if dic:
            return dic[0]
    return None


# Retrieves the actual wsdl name from type dictionaries
#
# @param name upcapitalized vmodl name
# @return (wsdl namespace, wsdl name)
def _GetWsdlInfo(name):
    if _allowCapitalizedNames:
        name = UncapitalizeVmodlName(name)

    with _lazyLock:
        # For data and managed objects, emitter puts version in field #3 and in
        # enum objects, it is in field #2. So, have to handle them differently
        for defMap in _dataDefMap, _managedDefMap:
            dic = defMap.get(name)
            if dic:
                return GetWsdlNamespace(dic[3]), dic[1]

        dic = _enumDefMap.get(name)
        if dic:
            return GetWsdlNamespace(dic[2]), dic[1]
        return None, None


# Checks if the definition exists for a vmodl name
#
# @param name vmodl name
# @return True if name exists, False otherwise
def TypeDefExists(name):
    # Check if is one of the primitive types
    typ = vmodlTypes.get(name)
    if typ:
        return True

    # Check if it's type definition is loaded in the dictionaries
    if name.endswith("[]"):
        name = name[:-2]

    with _lazyLock:
        actualName = _GetActualName(name)
    return actualName is not None


# Thread local for req context
_threadLocalContext = threading.local()
HOSTAPI_INVOKE_TIMEOUT_KEY = 'timeout'


# Get the RequestContext for the current thread
def GetRequestContext():
    """ Get the RequestContext for the current thread """
    global _threadLocalContext
    return _threadLocalContext.__dict__.setdefault('reqCtx', StringDict())


# Get the Http context for the current thread
def GetHttpContext():
    """ Get the Http context for the current thread """
    global _threadLocalContext
    return _threadLocalContext.__dict__.setdefault('httpCtx', dict())


# Class that resolves links
class LinkResolver:
    # Constructor
    #
    # @param self The object pointer
    # @param scope DataObject to be used against for resolving links
    def __init__(self, scope):
        self.linkables = {}
        self._VisitDataObject(scope)

    # Visit a DataObject and add it to linkable if it is one. Also
    # visit its properties that are DataObjects
    #
    # @param self The object pointer
    # @param obj DataObject to be visited
    def _VisitDataObject(self, obj):
        if isinstance(obj, DataObject):
            for prop in obj._GetPropertyList():
                if issubclass(prop.type, list):
                    for dataObj in getattr(obj, prop.name):
                        if (prop.flags & F_LINKABLE):
                            self._AddLinkable(dataObj)
                        self._VisitDataObject(dataObj)
                else:
                    dataObj = getattr(obj, prop.name)
                    if (prop.flags & F_LINKABLE):
                        self._AddLinkable(dataObj)
                    self._VisitDataObject(dataObj)
        elif isinstance(obj, list):
            for dataObj in obj:
                self._VisitDataObject(dataObj)

    # Adds a DataObject to linkable dictionary using its key
    #
    # @param self The object pointer
    # @param obj DataObject to be added to linkable
    def _AddLinkable(self, obj):
        key = getattr(obj, "key")
        if key and key != '':
            if key in self.linkables:
                # duplicate key present
                raise AttributeError(key)
            else:
                self.linkables[key] = obj
        else:
            # empty key
            raise AttributeError(key)

    # Resolves a key by looking up linkable dictionary
    #
    # @param self The object pointer
    # @param key Key to be resolved
    def ResolveLink(self, key):
        val = self.linkables[key]
        return val

    # Resolves a list of keys by resolving each key
    #
    # @param self The object pointer
    # @param keys keys to be resolved
    def ResolveLinks(self, keys):
        val = [self.linkables[k] for k in keys]
        return val


# Resolves a link key using the object provided as its scope by creating a
# link resolver object
#
# @param key Key to be resolved
# @param obj DataObject to be used against for resolving links
def ResolveLink(key, obj):
    if obj is None:
        return None
    linkResolver = LinkResolver(obj)
    return linkResolver.ResolveLink(key)


# Resolves a list of link keys using the object provided as its scope by
# creating a link resolver object
#
# @param keys keys to be resolved
# @param obj DataObject to be used against for resolving links
def ResolveLinks(keys, obj):
    if obj is None:
        return None
    linkResolver = LinkResolver(obj)
    return linkResolver.ResolveLinks(keys)


# Dictionary of type { 'branch' : { 'namespace' : count } }
# used by Vmodl Vcdb B2B code.

_breakingChanges = {}


def AddBreakingChangesInfo(branchName, vmodlNamespace, count):
    _breakingChanges.setdefault(branchName, {})[vmodlNamespace] = count


def GetBreakingChanges():
    return _breakingChanges
