from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime


class ClusterStatus(vmodl.DynamicData):
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def nodeUuid(self) -> str: ...
    @nodeUuid.setter
    def nodeUuid(self, value: str):
        self._nodeUuid = value
    @property
    def health(self) -> str: ...
    @health.setter
    def health(self, value: str):
        self._health = value
    @property
    def nodeState(self) -> ClusterStatus.State: ...
    @nodeState.setter
    def nodeState(self, value: ClusterStatus.State):
        self._nodeState = value
    @property
    def memberUuid(self) -> List[str]: ...
    @memberUuid.setter
    def memberUuid(self, value: List[str]):
        self._memberUuid = value


    class State(vmodl.DynamicData):
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value
        @property
        def completion(self) -> ClusterStatus.State.CompletionEstimate: ...
        @completion.setter
        def completion(self, value: ClusterStatus.State.CompletionEstimate):
            self._completion = value


        class CompletionEstimate(vmodl.DynamicData):
            @property
            def completeTime(self) -> datetime: ...
            @completeTime.setter
            def completeTime(self, value: datetime):
                self._completeTime = value
            @property
            def percentComplete(self) -> int: ...
            @percentComplete.setter
            def percentComplete(self, value: int):
                self._percentComplete = value


class ConfigInfo(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def hostSystem(self) -> vim.HostSystem: ...
    @hostSystem.setter
    def hostSystem(self, value: vim.HostSystem):
        self._hostSystem = value
    @property
    def clusterInfo(self) -> ConfigInfo.ClusterInfo: ...
    @clusterInfo.setter
    def clusterInfo(self, value: ConfigInfo.ClusterInfo):
        self._clusterInfo = value
    @property
    def storageInfo(self) -> ConfigInfo.StorageInfo: ...
    @storageInfo.setter
    def storageInfo(self, value: ConfigInfo.StorageInfo):
        self._storageInfo = value
    @property
    def networkInfo(self) -> ConfigInfo.NetworkInfo: ...
    @networkInfo.setter
    def networkInfo(self, value: ConfigInfo.NetworkInfo):
        self._networkInfo = value
    @property
    def faultDomainInfo(self) -> ConfigInfo.FaultDomainInfo: ...
    @faultDomainInfo.setter
    def faultDomainInfo(self, value: ConfigInfo.FaultDomainInfo):
        self._faultDomainInfo = value
    @property
    def vsanEsaEnabled(self) -> bool: ...
    @vsanEsaEnabled.setter
    def vsanEsaEnabled(self, value: bool):
        self._vsanEsaEnabled = value


    class ClusterInfo(vmodl.DynamicData):
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def nodeUuid(self) -> str: ...
        @nodeUuid.setter
        def nodeUuid(self, value: str):
            self._nodeUuid = value


    class FaultDomainInfo(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value


    class NetworkInfo(vmodl.DynamicData):
        @property
        def port(self) -> List[ConfigInfo.NetworkInfo.PortConfig]: ...
        @port.setter
        def port(self, value: List[ConfigInfo.NetworkInfo.PortConfig]):
            self._port = value


        class PortConfig(vmodl.DynamicData):
            @property
            def ipConfig(self) -> IpConfig: ...
            @ipConfig.setter
            def ipConfig(self, value: IpConfig):
                self._ipConfig = value
            @property
            def device(self) -> str: ...
            @device.setter
            def device(self, value: str):
                self._device = value


    class StorageInfo(vmodl.DynamicData):
        @property
        def autoClaimStorage(self) -> bool: ...
        @autoClaimStorage.setter
        def autoClaimStorage(self, value: bool):
            self._autoClaimStorage = value
        @property
        def diskMapping(self) -> List[DiskMapping]: ...
        @diskMapping.setter
        def diskMapping(self, value: List[DiskMapping]):
            self._diskMapping = value
        @property
        def diskMapInfo(self) -> List[DiskMapInfo]: ...
        @diskMapInfo.setter
        def diskMapInfo(self, value: List[DiskMapInfo]):
            self._diskMapInfo = value
        @property
        def checksumEnabled(self) -> bool: ...
        @checksumEnabled.setter
        def checksumEnabled(self, value: bool):
            self._checksumEnabled = value


class DecommissionMode(vmodl.DynamicData):
    @property
    def objectAction(self) -> str: ...
    @objectAction.setter
    def objectAction(self, value: str):
        self._objectAction = value


    class ObjectAction(Enum):
        noAction = "noAction"
        ensureObjectAccessibility = "ensureObjectAccessibility"
        evacuateAllData = "evacuateAllData"


class DiskMapInfo(vmodl.DynamicData):
    @property
    def mapping(self) -> DiskMapping: ...
    @mapping.setter
    def mapping(self, value: DiskMapping):
        self._mapping = value
    @property
    def mounted(self) -> bool: ...
    @mounted.setter
    def mounted(self, value: bool):
        self._mounted = value


class DiskMapResult(vmodl.DynamicData):
    @property
    def mapping(self) -> DiskMapping: ...
    @mapping.setter
    def mapping(self, value: DiskMapping):
        self._mapping = value
    @property
    def diskResult(self) -> List[DiskResult]: ...
    @diskResult.setter
    def diskResult(self, value: List[DiskResult]):
        self._diskResult = value
    @property
    def error(self) -> vmodl.MethodFault: ...
    @error.setter
    def error(self, value: vmodl.MethodFault):
        self._error = value


class DiskMapping(vmodl.DynamicData):
    @property
    def ssd(self) -> vim.host.ScsiDisk: ...
    @ssd.setter
    def ssd(self, value: vim.host.ScsiDisk):
        self._ssd = value
    @property
    def nonSsd(self) -> List[vim.host.ScsiDisk]: ...
    @nonSsd.setter
    def nonSsd(self, value: List[vim.host.ScsiDisk]):
        self._nonSsd = value


class DiskResult(vmodl.DynamicData):
    @property
    def disk(self) -> vim.host.ScsiDisk: ...
    @disk.setter
    def disk(self, value: vim.host.ScsiDisk):
        self._disk = value
    @property
    def state(self) -> str: ...
    @state.setter
    def state(self, value: str):
        self._state = value
    @property
    def vsanUuid(self) -> str: ...
    @vsanUuid.setter
    def vsanUuid(self, value: str):
        self._vsanUuid = value
    @property
    def error(self) -> vmodl.MethodFault: ...
    @error.setter
    def error(self, value: vmodl.MethodFault):
        self._error = value
    @property
    def degraded(self) -> bool: ...
    @degraded.setter
    def degraded(self, value: bool):
        self._degraded = value


    class State(Enum):
        inUse = "inUse"
        eligible = "eligible"
        ineligible = "ineligible"


class IpConfig(vmodl.DynamicData):
    @property
    def upstreamIpAddress(self) -> str: ...
    @upstreamIpAddress.setter
    def upstreamIpAddress(self, value: str):
        self._upstreamIpAddress = value
    @property
    def downstreamIpAddress(self) -> str: ...
    @downstreamIpAddress.setter
    def downstreamIpAddress(self, value: str):
        self._downstreamIpAddress = value


class MembershipInfo(vmodl.DynamicData):
    @property
    def nodeUuid(self) -> str: ...
    @nodeUuid.setter
    def nodeUuid(self, value: str):
        self._nodeUuid = value
    @property
    def hostname(self) -> str: ...
    @hostname.setter
    def hostname(self, value: str):
        self._hostname = value


class VsanDiskInfo(vmodl.DynamicData):
    @property
    def vsanUuid(self) -> str: ...
    @vsanUuid.setter
    def vsanUuid(self, value: str):
        self._vsanUuid = value
    @property
    def formatVersion(self) -> int: ...
    @formatVersion.setter
    def formatVersion(self, value: int):
        self._formatVersion = value


class VsanRuntimeInfo(vmodl.DynamicData):
    @property
    def membershipList(self) -> List[MembershipInfo]: ...
    @membershipList.setter
    def membershipList(self, value: List[MembershipInfo]):
        self._membershipList = value
    @property
    def diskIssues(self) -> List[VsanRuntimeInfo.DiskIssue]: ...
    @diskIssues.setter
    def diskIssues(self, value: List[VsanRuntimeInfo.DiskIssue]):
        self._diskIssues = value
    @property
    def accessGenNo(self) -> int: ...
    @accessGenNo.setter
    def accessGenNo(self, value: int):
        self._accessGenNo = value


    class DiskIssue(vmodl.DynamicData):
        @property
        def diskId(self) -> str: ...
        @diskId.setter
        def diskId(self, value: str):
            self._diskId = value
        @property
        def issue(self) -> str: ...
        @issue.setter
        def issue(self, value: str):
            self._issue = value


    class DiskIssueType(Enum):
        nonExist = "nonExist"
        stampMismatch = "stampMismatch"
        unknown = "unknown"