from pyVmomi import vmodl


class DeviceGroupId(vmodl.DynamicData):
    @property
    def id(self) -> str: ...


class FaultDomainId(vmodl.DynamicData):
    @property
    def id(self) -> str: ...


class ReplicationGroupId(vmodl.DynamicData):
    @property
    def faultDomainId(self) -> FaultDomainId: ...
    @property
    def deviceGroupId(self) -> DeviceGroupId: ...


class ReplicationSpec(vmodl.DynamicData):
    @property
    def replicationGroupId(self) -> ReplicationGroupId: ...