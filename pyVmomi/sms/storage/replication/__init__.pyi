from typing import List
from pyVmomi import sms, vim, vmodl
from datetime import datetime


class DeviceId(vmodl.DynamicData): ...


class FailoverParam(vmodl.DynamicData):
    @property
    def isPlanned(self) -> bool: ...
    @isPlanned.setter
    def isPlanned(self, value: bool):
        self._isPlanned = value
    @property
    def checkOnly(self) -> bool: ...
    @checkOnly.setter
    def checkOnly(self, value: bool):
        self._checkOnly = value
    @property
    def replicationGroupsToFailover(self) -> List[FailoverParam.ReplicationGroupData]: ...
    @replicationGroupsToFailover.setter
    def replicationGroupsToFailover(self, value: List[FailoverParam.ReplicationGroupData]):
        self._replicationGroupsToFailover = value
    @property
    def policyAssociations(self) -> List[FailoverParam.PolicyAssociation]: ...
    @policyAssociations.setter
    def policyAssociations(self, value: List[FailoverParam.PolicyAssociation]):
        self._policyAssociations = value


    class PolicyAssociation(vmodl.DynamicData):
        @property
        def id(self) -> DeviceId: ...
        @id.setter
        def id(self, value: DeviceId):
            self._id = value
        @property
        def policyId(self) -> str: ...
        @policyId.setter
        def policyId(self, value: str):
            self._policyId = value
        @property
        def datastore(self) -> vim.Datastore: ...
        @datastore.setter
        def datastore(self, value: vim.Datastore):
            self._datastore = value


    class ReplicationGroupData(vmodl.DynamicData):
        @property
        def groupId(self) -> vim.vm.replication.ReplicationGroupId: ...
        @groupId.setter
        def groupId(self, value: vim.vm.replication.ReplicationGroupId):
            self._groupId = value
        @property
        def pitId(self) -> PointInTimeReplicaId: ...
        @pitId.setter
        def pitId(self, value: PointInTimeReplicaId):
            self._pitId = value


class FailoverSuccessResult(GroupOperationResult):
    @property
    def newState(self) -> str: ...
    @newState.setter
    def newState(self, value: str):
        self._newState = value
    @property
    def pitId(self) -> PointInTimeReplicaId: ...
    @pitId.setter
    def pitId(self, value: PointInTimeReplicaId):
        self._pitId = value
    @property
    def pitIdBeforeFailover(self) -> PointInTimeReplicaId: ...
    @pitIdBeforeFailover.setter
    def pitIdBeforeFailover(self, value: PointInTimeReplicaId):
        self._pitIdBeforeFailover = value
    @property
    def recoveredDeviceInfo(self) -> List[FailoverSuccessResult.RecoveredDevice]: ...
    @recoveredDeviceInfo.setter
    def recoveredDeviceInfo(self, value: List[FailoverSuccessResult.RecoveredDevice]):
        self._recoveredDeviceInfo = value
    @property
    def timeStamp(self) -> datetime: ...
    @timeStamp.setter
    def timeStamp(self, value: datetime):
        self._timeStamp = value


    class RecoveredDevice(vmodl.DynamicData):
        @property
        def targetDeviceId(self) -> ReplicaId: ...
        @targetDeviceId.setter
        def targetDeviceId(self, value: ReplicaId):
            self._targetDeviceId = value
        @property
        def recoveredDeviceId(self) -> DeviceId: ...
        @recoveredDeviceId.setter
        def recoveredDeviceId(self, value: DeviceId):
            self._recoveredDeviceId = value
        @property
        def sourceDeviceId(self) -> DeviceId: ...
        @sourceDeviceId.setter
        def sourceDeviceId(self, value: DeviceId):
            self._sourceDeviceId = value
        @property
        def info(self) -> List[str]: ...
        @info.setter
        def info(self, value: List[str]):
            self._info = value
        @property
        def datastore(self) -> vim.Datastore: ...
        @datastore.setter
        def datastore(self, value: vim.Datastore):
            self._datastore = value
        @property
        def recoveredDiskInfo(self) -> List[FailoverSuccessResult.RecoveredDiskInfo]: ...
        @recoveredDiskInfo.setter
        def recoveredDiskInfo(self, value: List[FailoverSuccessResult.RecoveredDiskInfo]):
            self._recoveredDiskInfo = value
        @property
        def error(self) -> vmodl.MethodFault: ...
        @error.setter
        def error(self, value: vmodl.MethodFault):
            self._error = value
        @property
        def warnings(self) -> List[vmodl.MethodFault]: ...
        @warnings.setter
        def warnings(self, value: List[vmodl.MethodFault]):
            self._warnings = value


    class RecoveredDiskInfo(vmodl.DynamicData):
        @property
        def deviceKey(self) -> int: ...
        @deviceKey.setter
        def deviceKey(self, value: int):
            self._deviceKey = value
        @property
        def dsUrl(self) -> str: ...
        @dsUrl.setter
        def dsUrl(self, value: str):
            self._dsUrl = value
        @property
        def diskPath(self) -> str: ...
        @diskPath.setter
        def diskPath(self, value: str):
            self._diskPath = value


class FaultDomainInfo(vim.vm.replication.FaultDomainId):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def storageArrayId(self) -> str: ...
    @storageArrayId.setter
    def storageArrayId(self, value: str):
        self._storageArrayId = value
    @property
    def children(self) -> List[vim.vm.replication.FaultDomainId]: ...
    @children.setter
    def children(self, value: List[vim.vm.replication.FaultDomainId]):
        self._children = value
    @property
    def provider(self) -> sms.provider.Provider: ...
    @provider.setter
    def provider(self, value: sms.provider.Provider):
        self._provider = value


class GroupErrorResult(GroupOperationResult):
    @property
    def error(self) -> List[vmodl.MethodFault]: ...
    @error.setter
    def error(self, value: List[vmodl.MethodFault]):
        self._error = value


class GroupInfo(vmodl.DynamicData):
    @property
    def groupId(self) -> vim.vm.replication.ReplicationGroupId: ...
    @groupId.setter
    def groupId(self, value: vim.vm.replication.ReplicationGroupId):
        self._groupId = value


class GroupOperationResult(vmodl.DynamicData):
    @property
    def groupId(self) -> vim.vm.replication.ReplicationGroupId: ...
    @groupId.setter
    def groupId(self, value: vim.vm.replication.ReplicationGroupId):
        self._groupId = value
    @property
    def warning(self) -> List[vmodl.MethodFault]: ...
    @warning.setter
    def warning(self, value: List[vmodl.MethodFault]):
        self._warning = value


class PointInTimeReplicaId(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value


class PromoteParam(vmodl.DynamicData):
    @property
    def isPlanned(self) -> bool: ...
    @isPlanned.setter
    def isPlanned(self, value: bool):
        self._isPlanned = value
    @property
    def replicationGroupsToPromote(self) -> List[vim.vm.replication.ReplicationGroupId]: ...
    @replicationGroupsToPromote.setter
    def replicationGroupsToPromote(self, value: List[vim.vm.replication.ReplicationGroupId]):
        self._replicationGroupsToPromote = value


class QueryPointInTimeReplicaParam(vmodl.DynamicData):
    @property
    def replicaTimeQueryParam(self) -> QueryPointInTimeReplicaParam.ReplicaQueryIntervalParam: ...
    @replicaTimeQueryParam.setter
    def replicaTimeQueryParam(self, value: QueryPointInTimeReplicaParam.ReplicaQueryIntervalParam):
        self._replicaTimeQueryParam = value
    @property
    def pitName(self) -> str: ...
    @pitName.setter
    def pitName(self, value: str):
        self._pitName = value
    @property
    def tags(self) -> List[str]: ...
    @tags.setter
    def tags(self, value: List[str]):
        self._tags = value
    @property
    def preferDetails(self) -> bool: ...
    @preferDetails.setter
    def preferDetails(self, value: bool):
        self._preferDetails = value


    class ReplicaQueryIntervalParam(vmodl.DynamicData):
        @property
        def fromDate(self) -> datetime: ...
        @fromDate.setter
        def fromDate(self, value: datetime):
            self._fromDate = value
        @property
        def toDate(self) -> datetime: ...
        @toDate.setter
        def toDate(self, value: datetime):
            self._toDate = value
        @property
        def number(self) -> int: ...
        @number.setter
        def number(self, value: int):
            self._number = value


class QueryPointInTimeReplicaSuccessResult(GroupOperationResult):
    @property
    def replicaInfo(self) -> List[QueryPointInTimeReplicaSuccessResult.PointInTimeReplicaInfo]: ...
    @replicaInfo.setter
    def replicaInfo(self, value: List[QueryPointInTimeReplicaSuccessResult.PointInTimeReplicaInfo]):
        self._replicaInfo = value


    class PointInTimeReplicaInfo(vmodl.DynamicData):
        @property
        def id(self) -> PointInTimeReplicaId: ...
        @id.setter
        def id(self, value: PointInTimeReplicaId):
            self._id = value
        @property
        def pitName(self) -> str: ...
        @pitName.setter
        def pitName(self, value: str):
            self._pitName = value
        @property
        def timeStamp(self) -> datetime: ...
        @timeStamp.setter
        def timeStamp(self, value: datetime):
            self._timeStamp = value
        @property
        def tags(self) -> List[str]: ...
        @tags.setter
        def tags(self, value: List[str]):
            self._tags = value


class QueryPointInTimeReplicaSummaryResult(GroupOperationResult):
    @property
    def intervalResults(self) -> List[QueryPointInTimeReplicaSummaryResult.ReplicaIntervalQueryResult]: ...
    @intervalResults.setter
    def intervalResults(self, value: List[QueryPointInTimeReplicaSummaryResult.ReplicaIntervalQueryResult]):
        self._intervalResults = value


    class ReplicaIntervalQueryResult(vmodl.DynamicData):
        @property
        def fromDate(self) -> datetime: ...
        @fromDate.setter
        def fromDate(self, value: datetime):
            self._fromDate = value
        @property
        def toDate(self) -> datetime: ...
        @toDate.setter
        def toDate(self, value: datetime):
            self._toDate = value
        @property
        def number(self) -> int: ...
        @number.setter
        def number(self, value: int):
            self._number = value


class QueryReplicationGroupSuccessResult(GroupOperationResult):
    @property
    def rgInfo(self) -> GroupInfo: ...
    @rgInfo.setter
    def rgInfo(self, value: GroupInfo):
        self._rgInfo = value


class QueryReplicationPeerResult(vmodl.DynamicData):
    @property
    def sourceDomain(self) -> vim.vm.replication.FaultDomainId: ...
    @sourceDomain.setter
    def sourceDomain(self, value: vim.vm.replication.FaultDomainId):
        self._sourceDomain = value
    @property
    def targetDomain(self) -> List[vim.vm.replication.FaultDomainId]: ...
    @targetDomain.setter
    def targetDomain(self, value: List[vim.vm.replication.FaultDomainId]):
        self._targetDomain = value
    @property
    def error(self) -> List[vmodl.MethodFault]: ...
    @error.setter
    def error(self, value: List[vmodl.MethodFault]):
        self._error = value
    @property
    def warning(self) -> List[vmodl.MethodFault]: ...
    @warning.setter
    def warning(self, value: List[vmodl.MethodFault]):
        self._warning = value


class RecoveredTargetGroupMemberInfo(TargetGroupMemberInfo):
    @property
    def recoveredDeviceId(self) -> DeviceId: ...
    @recoveredDeviceId.setter
    def recoveredDeviceId(self, value: DeviceId):
        self._recoveredDeviceId = value


class ReplicaId(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value


class ReverseReplicationSuccessResult(GroupOperationResult):
    @property
    def newGroupId(self) -> vim.vm.replication.DeviceGroupId: ...
    @newGroupId.setter
    def newGroupId(self, value: vim.vm.replication.DeviceGroupId):
        self._newGroupId = value


class SourceGroupInfo(GroupInfo):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def state(self) -> str: ...
    @state.setter
    def state(self, value: str):
        self._state = value
    @property
    def replica(self) -> List[SourceGroupInfo.ReplicationTargetInfo]: ...
    @replica.setter
    def replica(self, value: List[SourceGroupInfo.ReplicationTargetInfo]):
        self._replica = value
    @property
    def memberInfo(self) -> List[SourceGroupMemberInfo]: ...
    @memberInfo.setter
    def memberInfo(self, value: List[SourceGroupMemberInfo]):
        self._memberInfo = value


    class ReplicationTargetInfo(vmodl.DynamicData):
        @property
        def targetGroupId(self) -> vim.vm.replication.ReplicationGroupId: ...
        @targetGroupId.setter
        def targetGroupId(self, value: vim.vm.replication.ReplicationGroupId):
            self._targetGroupId = value
        @property
        def replicationAgreementDescription(self) -> str: ...
        @replicationAgreementDescription.setter
        def replicationAgreementDescription(self, value: str):
            self._replicationAgreementDescription = value


class SourceGroupMemberInfo(vmodl.DynamicData):
    @property
    def deviceId(self) -> DeviceId: ...
    @deviceId.setter
    def deviceId(self, value: DeviceId):
        self._deviceId = value
    @property
    def targetId(self) -> List[SourceGroupMemberInfo.TargetDeviceId]: ...
    @targetId.setter
    def targetId(self, value: List[SourceGroupMemberInfo.TargetDeviceId]):
        self._targetId = value


    class TargetDeviceId(vmodl.DynamicData):
        @property
        def domainId(self) -> vim.vm.replication.FaultDomainId: ...
        @domainId.setter
        def domainId(self, value: vim.vm.replication.FaultDomainId):
            self._domainId = value
        @property
        def deviceId(self) -> ReplicaId: ...
        @deviceId.setter
        def deviceId(self, value: ReplicaId):
            self._deviceId = value


class SyncReplicationGroupSuccessResult(GroupOperationResult):
    @property
    def timeStamp(self) -> datetime: ...
    @timeStamp.setter
    def timeStamp(self, value: datetime):
        self._timeStamp = value
    @property
    def pitId(self) -> PointInTimeReplicaId: ...
    @pitId.setter
    def pitId(self, value: PointInTimeReplicaId):
        self._pitId = value
    @property
    def pitName(self) -> str: ...
    @pitName.setter
    def pitName(self, value: str):
        self._pitName = value


class TargetGroupInfo(GroupInfo):
    @property
    def sourceInfo(self) -> TargetGroupInfo.TargetToSourceInfo: ...
    @sourceInfo.setter
    def sourceInfo(self, value: TargetGroupInfo.TargetToSourceInfo):
        self._sourceInfo = value
    @property
    def state(self) -> str: ...
    @state.setter
    def state(self, value: str):
        self._state = value
    @property
    def devices(self) -> List[TargetGroupMemberInfo]: ...
    @devices.setter
    def devices(self, value: List[TargetGroupMemberInfo]):
        self._devices = value
    @property
    def isPromoteCapable(self) -> bool: ...
    @isPromoteCapable.setter
    def isPromoteCapable(self, value: bool):
        self._isPromoteCapable = value


    class TargetToSourceInfo(vmodl.DynamicData):
        @property
        def sourceGroupId(self) -> vim.vm.replication.ReplicationGroupId: ...
        @sourceGroupId.setter
        def sourceGroupId(self, value: vim.vm.replication.ReplicationGroupId):
            self._sourceGroupId = value
        @property
        def replicationAgreementDescription(self) -> str: ...
        @replicationAgreementDescription.setter
        def replicationAgreementDescription(self, value: str):
            self._replicationAgreementDescription = value


class TargetGroupMemberInfo(vmodl.DynamicData):
    @property
    def replicaId(self) -> ReplicaId: ...
    @replicaId.setter
    def replicaId(self, value: ReplicaId):
        self._replicaId = value
    @property
    def sourceId(self) -> DeviceId: ...
    @sourceId.setter
    def sourceId(self, value: DeviceId):
        self._sourceId = value
    @property
    def targetDatastore(self) -> vim.Datastore: ...
    @targetDatastore.setter
    def targetDatastore(self, value: vim.Datastore):
        self._targetDatastore = value


class TestFailoverParam(FailoverParam): ...


class VVolId(DeviceId):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value


class VirtualDiskId(DeviceId):
    @property
    def diskId(self) -> str: ...
    @diskId.setter
    def diskId(self, value: str):
        self._diskId = value


class VirtualDiskKey(DeviceId):
    @property
    def vmInstanceUUID(self) -> str: ...
    @vmInstanceUUID.setter
    def vmInstanceUUID(self, value: str):
        self._vmInstanceUUID = value
    @property
    def deviceKey(self) -> int: ...
    @deviceKey.setter
    def deviceKey(self, value: int):
        self._deviceKey = value


class VirtualDiskMoId(DeviceId):
    @property
    def vcUuid(self) -> str: ...
    @vcUuid.setter
    def vcUuid(self, value: str):
        self._vcUuid = value
    @property
    def vmMoid(self) -> str: ...
    @vmMoid.setter
    def vmMoid(self, value: str):
        self._vmMoid = value
    @property
    def diskKey(self) -> str: ...
    @diskKey.setter
    def diskKey(self, value: str):
        self._diskKey = value


class VirtualMachineFilePath(VirtualMachineId):
    @property
    def vcUuid(self) -> str: ...
    @vcUuid.setter
    def vcUuid(self, value: str):
        self._vcUuid = value
    @property
    def dsUrl(self) -> str: ...
    @dsUrl.setter
    def dsUrl(self, value: str):
        self._dsUrl = value
    @property
    def vmxPath(self) -> str: ...
    @vmxPath.setter
    def vmxPath(self, value: str):
        self._vmxPath = value


class VirtualMachineId(DeviceId): ...


class VirtualMachineMoId(VirtualMachineId):
    @property
    def vcUuid(self) -> str: ...
    @vcUuid.setter
    def vcUuid(self, value: str):
        self._vcUuid = value
    @property
    def vmMoid(self) -> str: ...
    @vmMoid.setter
    def vmMoid(self, value: str):
        self._vmMoid = value


class VirtualMachineUUID(VirtualMachineId):
    @property
    def vmInstanceUUID(self) -> str: ...
    @vmInstanceUUID.setter
    def vmInstanceUUID(self, value: str):
        self._vmInstanceUUID = value