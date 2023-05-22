from pyVmomi import vmodl


class DeviceGroupId(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value


class FaultDomainId(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value


class ReplicationGroupId(vmodl.DynamicData):
    @property
    def faultDomainId(self) -> FaultDomainId: ...
    @faultDomainId.setter
    def faultDomainId(self, value: FaultDomainId):
        self._faultDomainId = value
    @property
    def deviceGroupId(self) -> DeviceGroupId: ...
    @deviceGroupId.setter
    def deviceGroupId(self, value: DeviceGroupId):
        self._deviceGroupId = value


class ReplicationSpec(vmodl.DynamicData):
    @property
    def replicationGroupId(self) -> ReplicationGroupId: ...
    @replicationGroupId.setter
    def replicationGroupId(self, value: ReplicationGroupId):
        self._replicationGroupId = value