# Copyright (c) 2011-2024 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

from .VmomiSupport import GetVmodlType, ManagedObject, Object


# Used to replace few type definitions for emulating
# legacy behavior. Ref. VmomiSupport._wsdlTypeMap
_legacyTypes = {
    "type": "string",
    "ManagedMethod": "string",
    "PropertyPath": "string",
    "type[]": "string[]",
    "ManagedMethod[]": "string[]",
    "PropertyPath[]": "string[]"
}


class StubAdapterAccessorMixin(object):

    # Retrieve a managed property
    #
    # @param self The object pointer
    # @param mo managed object
    # @param info property info
    def InvokeAccessor(self, mo, info):
        prop = info.name
        param = Object(name="prop", type=str, version=self.version, flags=0)

        # Emulate legacy behavior for backward compatibility
        replacement = _legacyTypes.get(info.type.__name__, None)
        if replacement:
            info.type = GetVmodlType(replacement)

        # When the type is a list of instances of ManagedObject
        # the legacy behavior was to return the base class
        # e.g. The returned object type was ManagedObject[] for
        # vim.Datastore[] or vim.ManagedEntity[]
        if info.type.__name__.endswith("[]"):
            elementTypeName = info.type.__name__[:-2]
            try:
                elementType = GetVmodlType(elementTypeName)
                if issubclass(elementType, ManagedObject):
                    info.type = GetVmodlType('vmodl.ManagedObject[]')
            except KeyError:
                pass

        info = Object(name=info.name,
                      type=ManagedObject,
                      wsdlName="Fetch",
                      version=info.version,
                      params=(param, ),
                      isTask=False,
                      resultFlags=info.flags,
                      result=info.type,
                      methodResult=info.type)
        return self.InvokeMethod(mo, info, (prop, ))

    def SupportServerGUIDs(self):
        return False
