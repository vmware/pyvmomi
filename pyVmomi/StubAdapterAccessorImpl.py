# **********************************************************
# Copyright (c) 2011-2022 VMware, Inc.
# **********************************************************

from .VmomiSupport import GetVmodlType, ManagedObject, Object


class StubAdapterAccessorMixin:

    # Retrieve a managed property
    #
    # @param self self
    # @param mo managed object
    # @param info property info
    def InvokeAccessor(self, mo, info):
        prop = info.name
        param = Object(name="prop", type=str, version=self.version, flags=0)
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
