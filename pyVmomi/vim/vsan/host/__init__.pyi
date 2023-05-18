from typing import List
from enum import Enum
from pyVmomi import ScsiDisk, vim, vmodl
from datetime import datetime


class ClusterStatus(vmodl.DynamicData):
    @property
    def uuid(self) -> str: ...
    @property
    def nodeUuid(self) -> str: ...
    @property
    def health(self) -> str: ...
    @property
    def nodeState(self) -> ClusterStatus.State: ...
    @property
    def memberUuid(self) -> List[str]: ...


    class State(vmodl.DynamicData):
        @property
        def state(self) -> str: ...
        @property
        def completion(self) -> ClusterStatus.State.CompletionEstimate: ...


        class CompletionEstimate(vmodl.DynamicData):
            @property
            def completeTime(self) -> datetime: ...
            @property
            def percentComplete(self) -> int: ...


class ConfigInfo(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @property
    def hostSystem(self) -> vim.HostSystem: ...
    @property
    def clusterInfo(self) -> ConfigInfo.ClusterInfo: ...
    @property
    def storageInfo(self) -> ConfigInfo.StorageInfo: ...
    @property
    def networkInfo(self) -> ConfigInfo.NetworkInfo: ...
    @property
    def faultDomainInfo(self) -> ConfigInfo.FaultDomainInfo: ...
    @property
    def vsanEsaEnabled(self) -> bool: ...


    class ClusterInfo(vmodl.DynamicData):
        @property
        def uuid(self) -> str: ...
        @property
        def nodeUuid(self) -> str: ...


    class FaultDomainInfo(vmodl.DynamicData):
        @property
        def name(self) -> str: ...


    class NetworkInfo(vmodl.DynamicData):
        @property
        def port(self) -> List[ConfigInfo.NetworkInfo.PortConfig]: ...


        class PortConfig(vmodl.DynamicData):
            @property
            def ipConfig(self) -> IpConfig: ...
            @property
            def device(self) -> str: ...


    class StorageInfo(vmodl.DynamicData):
        @property
        def autoClaimStorage(self) -> bool: ...
        @property
        def diskMapping(self) -> List[DiskMapping]: ...
        @property
        def diskMapInfo(self) -> List[DiskMapInfo]: ...
        @property
        def checksumEnabled(self) -> bool: ...


class DecommissionMode(vmodl.DynamicData):
    @property
    def objectAction(self) -> str: ...


    class ObjectAction(Enum):
        noAction = "noAction"
        ensureObjectAccessibility = "ensureObjectAccessibility"
        evacuateAllData = "evacuateAllData"


class DiskMapInfo(vmodl.DynamicData):
    @property
    def mapping(self) -> DiskMapping: ...
    @property
    def mounted(self) -> bool: ...


class DiskMapResult(vmodl.DynamicData):
    @property
    def mapping(self) -> DiskMapping: ...
    @property
    def diskResult(self) -> List[DiskResult]: ...
    @property
    def error(self) -> vmodl.MethodFault: ...


class DiskMapping(vmodl.DynamicData):
    @property
    def ssd(self) -> ScsiDisk: ...
    @property
    def nonSsd(self) -> List[ScsiDisk]: ...


class DiskResult(vmodl.DynamicData):
    @property
    def disk(self) -> ScsiDisk: ...
    @property
    def state(self) -> str: ...
    @property
    def vsanUuid(self) -> str: ...
    @property
    def error(self) -> vmodl.MethodFault: ...
    @property
    def degraded(self) -> bool: ...


    class State(Enum):
        inUse = "inUse"
        eligible = "eligible"
        ineligible = "ineligible"


class IpConfig(vmodl.DynamicData):
    @property
    def upstreamIpAddress(self) -> str: ...
    @property
    def downstreamIpAddress(self) -> str: ...


class MembershipInfo(vmodl.DynamicData):
    @property
    def nodeUuid(self) -> str: ...
    @property
    def hostname(self) -> str: ...


class VsanDiskInfo(vmodl.DynamicData):
    @property
    def vsanUuid(self) -> str: ...
    @property
    def formatVersion(self) -> int: ...


class VsanRuntimeInfo(vmodl.DynamicData):
    @property
    def membershipList(self) -> List[MembershipInfo]: ...
    @property
    def diskIssues(self) -> List[VsanRuntimeInfo.DiskIssue]: ...
    @property
    def accessGenNo(self) -> int: ...


    class DiskIssue(vmodl.DynamicData):
        @property
        def diskId(self) -> str: ...
        @property
        def issue(self) -> str: ...


    class DiskIssueType(Enum):
        nonExist = "nonExist"
        stampMismatch = "stampMismatch"
        unknown = "unknown"