# Copyright (c) 2022-2024 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

import base64
import json

from datetime import datetime

from . import Iso8601
from .VmomiSupport import ManagedObject, DataObject, ManagedMethod, \
    UnknownManagedMethod, GetWsdlType, XMLNS_VMODL_BASE, binary


class VmomiJSONEncoder(json.JSONEncoder):
    """
        Custom JSON encoder to encode vSphere objects.
        When a ManagedObject is encoded, it gains three properties:
            _vimid is the _moId (ex: 'vm-42')
            _vimref is the moRef (ex: 'vim.VirtualMachine:vm-42')
            _vimtype is the class name (ex: 'vim.VirtualMachine')
        When a DataObject is encoded, it gains one property:
            _vimtype is the class name (ex: 'vim.VirtualMachineQuestionInfo')
        If the dynamicProperty and dynamicType are empty, they are optionally
            omitted from the results of DataObjects and ManagedObjects
        @example "Explode only the object passed in"
            data = json.dumps(vm, cls=VmomiJSONEncoder)
        @example "Explode specific objects"
            data = json.dumps(vm, cls=VmomiJSONEncoder,
                              explode=[vm, vm.network[0]])
        @example "Explode all virtual machines in a list and their snapshots"
            data = json.dumps([vm1, vm2], cls=VmomiJSONEncoder,
                              explode=[templateOf('VirtualMachine'),
                                       templateOf('VirtualMachineSnapshot')])
    """
    def __init__(self, *args, **kwargs):
        """
        Consumer must specify what types to explode into full content
        and what types to leave as a ManagedObjectReference.  If the
        root object of the encoding is a ManagedObject, it will be
        added to the explode list automatically.
        A ManagedObject is only exploded once, the first time it is
        encountered.  All subsequent times it will be a moRef.
        @param explode (list) A list of objects and/or types to
            expand in the conversion process.  Directly add any
            objects to the list, or add the type of any object
            using type(templateOf('VirtualMachine')) for example.
        @param strip_dynamic (bool) Every object normally contains
            a dynamicProperty list and a dynamicType field even if
            the contents are [] and None respectively.  These fields
            clutter the output making it more difficult for a person
            to read and bloat the size of the result unnecessarily.
            This option removes them if they are the empty values above.
            The default is False.
        """
        self._done = set()
        self._first = True
        self._explode = kwargs.pop('explode', None)
        self._strip_dynamic = kwargs.pop('strip_dynamic', False)
        super(VmomiJSONEncoder, self).__init__(*args, **kwargs)

    def _remove_empty_dynamic_if(self, result):
        if self._strip_dynamic:
            if 'dynamicProperty' in result and len(result['dynamicProperty']) == 0:
                result.pop('dynamicProperty')
            if 'dynamicType' in result and not result['dynamicType']:
                result.pop('dynamicType')
        return result

    def default(self, obj):  # pylint: disable=method-hidden
        if self._first:
            self._first = False
            if not self._explode:
                self._explode = []
            if isinstance(obj, ManagedObject):
                self._explode.append(obj)
        if isinstance(obj, ManagedObject):
            if self.explode(obj):
                result = {}
                result['_vimid'] = obj._moId
                result['_vimref'] = '{}:{}'.format(obj.__class__.__name__,
                                                   obj._moId)
                result['_vimtype'] = obj.__class__.__name__
                for prop in obj._GetPropertyList():
                    result[prop.name] = getattr(obj, prop.name)
                return self._remove_empty_dynamic_if(result)
            return str(obj).strip("'")  # see VmomiSupport.FormatObject
        if isinstance(obj, DataObject):
            result = {k:v for k,v in obj.__dict__.items()}
            result['_vimtype'] = obj.__class__.__name__
            return self._remove_empty_dynamic_if(result)
        if isinstance(obj, binary):
            result = base64.b64encode(obj)
            # see VmomiSupport.FormatObject
            result = str(result, 'utf-8')
            return result
        if isinstance(obj, datetime):
            return Iso8601.ISO8601Format(obj)
        if isinstance(obj, UnknownManagedMethod):
            return obj.name
        if isinstance(obj, ManagedMethod):
            return str(obj)  # see VmomiSupport.FormatObject
        if isinstance(obj, type):
            return obj.__name__
        super(VmomiJSONEncoder, self).default(obj)

    def explode(self, obj):
        """ Determine if the object should be exploded. """
        if obj in self._done:
            return False
        result = False
        for item in self._explode:
            if hasattr(item, '_moId'):
                # If it has a _moId it is an instance
                if obj._moId == item._moId:
                    result = True
            else:
                # If it does not have a _moId it is a template
                if obj.__class__.__name__ == item.__name__:
                    result = True
        if result:
            self._done.add(obj)
        return result


def templateOf(typestr):
    """ Returns a class template. """
    return GetWsdlType(XMLNS_VMODL_BASE, typestr)
