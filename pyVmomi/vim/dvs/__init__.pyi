from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, binary, long


class DistributedVirtualPortgroup(vim.Network):
    @property
    def key(self) -> str: ...
    @property
    def config(self) -> DistributedVirtualPortgroup.ConfigInfo: ...
    @property
    def portKeys(self) -> List[str]: ...
    def Reconfigure(self, spec: DistributedVirtualPortgroup.ConfigSpec) -> vim.Task: ...
    def Rollback(self, entityBackup: EntityBackup.Config) -> vim.Task: ...


    class ConfigInfo(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def numPorts(self) -> int: ...
        @numPorts.setter
        def numPorts(self, value: int):
            self._numPorts = value
        @property
        def distributedVirtualSwitch(self) -> vim.DistributedVirtualSwitch: ...
        @distributedVirtualSwitch.setter
        def distributedVirtualSwitch(self, value: vim.DistributedVirtualSwitch):
            self._distributedVirtualSwitch = value
        @property
        def defaultPortConfig(self) -> DistributedVirtualPort.Setting: ...
        @defaultPortConfig.setter
        def defaultPortConfig(self, value: DistributedVirtualPort.Setting):
            self._defaultPortConfig = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def backingType(self) -> str: ...
        @backingType.setter
        def backingType(self, value: str):
            self._backingType = value
        @property
        def policy(self) -> DistributedVirtualPortgroup.PortgroupPolicy: ...
        @policy.setter
        def policy(self, value: DistributedVirtualPortgroup.PortgroupPolicy):
            self._policy = value
        @property
        def portNameFormat(self) -> str: ...
        @portNameFormat.setter
        def portNameFormat(self, value: str):
            self._portNameFormat = value
        @property
        def scope(self) -> List[vim.ManagedEntity]: ...
        @scope.setter
        def scope(self, value: List[vim.ManagedEntity]):
            self._scope = value
        @property
        def vendorSpecificConfig(self) -> List[KeyedOpaqueBlob]: ...
        @vendorSpecificConfig.setter
        def vendorSpecificConfig(self, value: List[KeyedOpaqueBlob]):
            self._vendorSpecificConfig = value
        @property
        def configVersion(self) -> str: ...
        @configVersion.setter
        def configVersion(self, value: str):
            self._configVersion = value
        @property
        def autoExpand(self) -> bool: ...
        @autoExpand.setter
        def autoExpand(self, value: bool):
            self._autoExpand = value
        @property
        def vmVnicNetworkResourcePoolKey(self) -> str: ...
        @vmVnicNetworkResourcePoolKey.setter
        def vmVnicNetworkResourcePoolKey(self, value: str):
            self._vmVnicNetworkResourcePoolKey = value
        @property
        def uplink(self) -> bool: ...
        @uplink.setter
        def uplink(self, value: bool):
            self._uplink = value
        @property
        def transportZoneUuid(self) -> str: ...
        @transportZoneUuid.setter
        def transportZoneUuid(self, value: str):
            self._transportZoneUuid = value
        @property
        def transportZoneName(self) -> str: ...
        @transportZoneName.setter
        def transportZoneName(self, value: str):
            self._transportZoneName = value
        @property
        def logicalSwitchUuid(self) -> str: ...
        @logicalSwitchUuid.setter
        def logicalSwitchUuid(self, value: str):
            self._logicalSwitchUuid = value
        @property
        def segmentId(self) -> str: ...
        @segmentId.setter
        def segmentId(self, value: str):
            self._segmentId = value


    class ConfigSpec(vmodl.DynamicData):
        @property
        def configVersion(self) -> str: ...
        @configVersion.setter
        def configVersion(self, value: str):
            self._configVersion = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def numPorts(self) -> int: ...
        @numPorts.setter
        def numPorts(self, value: int):
            self._numPorts = value
        @property
        def portNameFormat(self) -> str: ...
        @portNameFormat.setter
        def portNameFormat(self, value: str):
            self._portNameFormat = value
        @property
        def defaultPortConfig(self) -> DistributedVirtualPort.Setting: ...
        @defaultPortConfig.setter
        def defaultPortConfig(self, value: DistributedVirtualPort.Setting):
            self._defaultPortConfig = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def backingType(self) -> str: ...
        @backingType.setter
        def backingType(self, value: str):
            self._backingType = value
        @property
        def scope(self) -> List[vim.ManagedEntity]: ...
        @scope.setter
        def scope(self, value: List[vim.ManagedEntity]):
            self._scope = value
        @property
        def policy(self) -> DistributedVirtualPortgroup.PortgroupPolicy: ...
        @policy.setter
        def policy(self, value: DistributedVirtualPortgroup.PortgroupPolicy):
            self._policy = value
        @property
        def vendorSpecificConfig(self) -> List[KeyedOpaqueBlob]: ...
        @vendorSpecificConfig.setter
        def vendorSpecificConfig(self, value: List[KeyedOpaqueBlob]):
            self._vendorSpecificConfig = value
        @property
        def autoExpand(self) -> bool: ...
        @autoExpand.setter
        def autoExpand(self, value: bool):
            self._autoExpand = value
        @property
        def vmVnicNetworkResourcePoolKey(self) -> str: ...
        @vmVnicNetworkResourcePoolKey.setter
        def vmVnicNetworkResourcePoolKey(self, value: str):
            self._vmVnicNetworkResourcePoolKey = value
        @property
        def transportZoneUuid(self) -> str: ...
        @transportZoneUuid.setter
        def transportZoneUuid(self, value: str):
            self._transportZoneUuid = value
        @property
        def transportZoneName(self) -> str: ...
        @transportZoneName.setter
        def transportZoneName(self, value: str):
            self._transportZoneName = value
        @property
        def logicalSwitchUuid(self) -> str: ...
        @logicalSwitchUuid.setter
        def logicalSwitchUuid(self, value: str):
            self._logicalSwitchUuid = value
        @property
        def segmentId(self) -> str: ...
        @segmentId.setter
        def segmentId(self, value: str):
            self._segmentId = value


    class NsxPortgroupOperationResult(vmodl.DynamicData):
        @property
        def portgroups(self) -> List[DistributedVirtualPortgroup]: ...
        @portgroups.setter
        def portgroups(self, value: List[DistributedVirtualPortgroup]):
            self._portgroups = value
        @property
        def problems(self) -> List[DistributedVirtualPortgroup.Problem]: ...
        @problems.setter
        def problems(self, value: List[DistributedVirtualPortgroup.Problem]):
            self._problems = value


    class PortgroupPolicy(vmodl.DynamicData):
        @property
        def blockOverrideAllowed(self) -> bool: ...
        @blockOverrideAllowed.setter
        def blockOverrideAllowed(self, value: bool):
            self._blockOverrideAllowed = value
        @property
        def shapingOverrideAllowed(self) -> bool: ...
        @shapingOverrideAllowed.setter
        def shapingOverrideAllowed(self, value: bool):
            self._shapingOverrideAllowed = value
        @property
        def vendorConfigOverrideAllowed(self) -> bool: ...
        @vendorConfigOverrideAllowed.setter
        def vendorConfigOverrideAllowed(self, value: bool):
            self._vendorConfigOverrideAllowed = value
        @property
        def livePortMovingAllowed(self) -> bool: ...
        @livePortMovingAllowed.setter
        def livePortMovingAllowed(self, value: bool):
            self._livePortMovingAllowed = value
        @property
        def portConfigResetAtDisconnect(self) -> bool: ...
        @portConfigResetAtDisconnect.setter
        def portConfigResetAtDisconnect(self, value: bool):
            self._portConfigResetAtDisconnect = value
        @property
        def networkResourcePoolOverrideAllowed(self) -> bool: ...
        @networkResourcePoolOverrideAllowed.setter
        def networkResourcePoolOverrideAllowed(self, value: bool):
            self._networkResourcePoolOverrideAllowed = value
        @property
        def trafficFilterOverrideAllowed(self) -> bool: ...
        @trafficFilterOverrideAllowed.setter
        def trafficFilterOverrideAllowed(self, value: bool):
            self._trafficFilterOverrideAllowed = value


    class Problem(vmodl.DynamicData):
        @property
        def logicalSwitchUuid(self) -> str: ...
        @logicalSwitchUuid.setter
        def logicalSwitchUuid(self, value: str):
            self._logicalSwitchUuid = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


    class BackingType(Enum):
        standard = "standard"
        nsx = "nsx"


    class MetaTagName(Enum):
        dvsName = "dvsName"
        portgroupName = "portgroupName"
        portIndex = "portIndex"


    class PortgroupType(Enum):
        earlyBinding = "earlyBinding"
        lateBinding = "lateBinding"
        ephemeral = "ephemeral"


class DistributedVirtualSwitchManager(ManagedObject):
    def QuerySupportedSwitchSpec(self, recommended: bool) -> List[ProductSpec]: ...
    def QuerySupportedNetworkOffloadSpec(self, switchProductSpec: ProductSpec) -> List[NetworkOffloadSpec]: ...
    def QueryCompatibleVmnicsFromHosts(self, hosts: List[vim.HostSystem], dvs: vim.DistributedVirtualSwitch) -> List[DistributedVirtualSwitchManager.PhysicalNicsList]: ...
    def QueryCompatibleHostForNewDvs(self, container: vim.ManagedEntity, recursive: bool, switchProductSpec: ProductSpec) -> List[vim.HostSystem]: ...
    def QueryCompatibleHostForExistingDvs(self, container: vim.ManagedEntity, recursive: bool, dvs: vim.DistributedVirtualSwitch) -> List[vim.HostSystem]: ...
    def QueryCompatibleHostSpec(self, switchProductSpec: ProductSpec) -> List[HostProductSpec]: ...
    def QueryFeatureCapability(self, switchProductSpec: ProductSpec) -> vim.DistributedVirtualSwitch.FeatureCapability: ...
    def QuerySwitchByUuid(self, uuid: str) -> vim.DistributedVirtualSwitch: ...
    def QueryDvsConfigTarget(self, host: vim.HostSystem, dvs: vim.DistributedVirtualSwitch) -> DistributedVirtualSwitchManager.DvsConfigTarget: ...
    def CheckCompatibility(self, hostContainer: DistributedVirtualSwitchManager.HostContainer, dvsProductSpec: DistributedVirtualSwitchManager.DvsProductSpec, hostFilterSpec: List[DistributedVirtualSwitchManager.HostDvsFilterSpec]) -> List[DistributedVirtualSwitchManager.CompatibilityResult]: ...
    def RectifyHost(self, hosts: List[vim.HostSystem]) -> vim.Task: ...
    def ExportEntity(self, selectionSet: List[vim.SelectionSet]) -> vim.Task: ...
    def ImportEntity(self, entityBackup: List[EntityBackup.Config], importType: str) -> vim.Task: ...
    def LookupPortgroup(self, switchUuid: str, portgroupKey: str) -> DistributedVirtualPortgroup: ...


    class CompatibilityResult(vmodl.DynamicData):
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def error(self) -> List[vmodl.MethodFault]: ...
        @error.setter
        def error(self, value: List[vmodl.MethodFault]):
            self._error = value


    class DvsConfigTarget(vmodl.DynamicData):
        @property
        def distributedVirtualPortgroup(self) -> List[DistributedVirtualPortgroupInfo]: ...
        @distributedVirtualPortgroup.setter
        def distributedVirtualPortgroup(self, value: List[DistributedVirtualPortgroupInfo]):
            self._distributedVirtualPortgroup = value
        @property
        def distributedVirtualSwitch(self) -> List[DistributedVirtualSwitchInfo]: ...
        @distributedVirtualSwitch.setter
        def distributedVirtualSwitch(self, value: List[DistributedVirtualSwitchInfo]):
            self._distributedVirtualSwitch = value


    class DvsProductSpec(vmodl.DynamicData):
        @property
        def newSwitchProductSpec(self) -> ProductSpec: ...
        @newSwitchProductSpec.setter
        def newSwitchProductSpec(self, value: ProductSpec):
            self._newSwitchProductSpec = value
        @property
        def distributedVirtualSwitch(self) -> vim.DistributedVirtualSwitch: ...
        @distributedVirtualSwitch.setter
        def distributedVirtualSwitch(self, value: vim.DistributedVirtualSwitch):
            self._distributedVirtualSwitch = value


    class HostArrayFilter(DistributedVirtualSwitchManager.HostDvsFilterSpec):
        @property
        def host(self) -> List[vim.HostSystem]: ...
        @host.setter
        def host(self, value: List[vim.HostSystem]):
            self._host = value


    class HostContainer(vmodl.DynamicData):
        @property
        def container(self) -> vim.ManagedEntity: ...
        @container.setter
        def container(self, value: vim.ManagedEntity):
            self._container = value
        @property
        def recursive(self) -> bool: ...
        @recursive.setter
        def recursive(self, value: bool):
            self._recursive = value


    class HostContainerFilter(DistributedVirtualSwitchManager.HostDvsFilterSpec):
        @property
        def hostContainer(self) -> DistributedVirtualSwitchManager.HostContainer: ...
        @hostContainer.setter
        def hostContainer(self, value: DistributedVirtualSwitchManager.HostContainer):
            self._hostContainer = value


    class HostDvsFilterSpec(vmodl.DynamicData):
        @property
        def inclusive(self) -> bool: ...
        @inclusive.setter
        def inclusive(self, value: bool):
            self._inclusive = value


    class HostDvsMembershipFilter(DistributedVirtualSwitchManager.HostDvsFilterSpec):
        @property
        def distributedVirtualSwitch(self) -> vim.DistributedVirtualSwitch: ...
        @distributedVirtualSwitch.setter
        def distributedVirtualSwitch(self, value: vim.DistributedVirtualSwitch):
            self._distributedVirtualSwitch = value


    class ImportResult(vmodl.DynamicData):
        @property
        def distributedVirtualSwitch(self) -> List[vim.DistributedVirtualSwitch]: ...
        @distributedVirtualSwitch.setter
        def distributedVirtualSwitch(self, value: List[vim.DistributedVirtualSwitch]):
            self._distributedVirtualSwitch = value
        @property
        def distributedVirtualPortgroup(self) -> List[DistributedVirtualPortgroup]: ...
        @distributedVirtualPortgroup.setter
        def distributedVirtualPortgroup(self, value: List[DistributedVirtualPortgroup]):
            self._distributedVirtualPortgroup = value
        @property
        def importFault(self) -> List[vim.fault.ImportOperationBulkFault.FaultOnImport]: ...
        @importFault.setter
        def importFault(self, value: List[vim.fault.ImportOperationBulkFault.FaultOnImport]):
            self._importFault = value


    class PhysicalNicsList(vmodl.DynamicData):
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def physicalNics(self) -> List[vim.host.PhysicalNic]: ...
        @physicalNics.setter
        def physicalNics(self, value: List[vim.host.PhysicalNic]):
            self._physicalNics = value


class VmwareDistributedVirtualSwitch(vim.DistributedVirtualSwitch):
    def UpdateLacpGroupConfig(self, lacpGroupSpec: List[VmwareDistributedVirtualSwitch.LacpGroupSpec]) -> vim.Task: ...


    class ConfigInfo(vim.DistributedVirtualSwitch.ConfigInfo):
        @property
        def vspanSession(self) -> List[VmwareDistributedVirtualSwitch.VspanSession]: ...
        @vspanSession.setter
        def vspanSession(self, value: List[VmwareDistributedVirtualSwitch.VspanSession]):
            self._vspanSession = value
        @property
        def pvlanConfig(self) -> List[VmwareDistributedVirtualSwitch.PvlanMapEntry]: ...
        @pvlanConfig.setter
        def pvlanConfig(self, value: List[VmwareDistributedVirtualSwitch.PvlanMapEntry]):
            self._pvlanConfig = value
        @property
        def maxMtu(self) -> int: ...
        @maxMtu.setter
        def maxMtu(self, value: int):
            self._maxMtu = value
        @property
        def linkDiscoveryProtocolConfig(self) -> vim.host.LinkDiscoveryProtocolConfig: ...
        @linkDiscoveryProtocolConfig.setter
        def linkDiscoveryProtocolConfig(self, value: vim.host.LinkDiscoveryProtocolConfig):
            self._linkDiscoveryProtocolConfig = value
        @property
        def ipfixConfig(self) -> VmwareDistributedVirtualSwitch.IpfixConfig: ...
        @ipfixConfig.setter
        def ipfixConfig(self, value: VmwareDistributedVirtualSwitch.IpfixConfig):
            self._ipfixConfig = value
        @property
        def lacpGroupConfig(self) -> List[VmwareDistributedVirtualSwitch.LacpGroupConfig]: ...
        @lacpGroupConfig.setter
        def lacpGroupConfig(self, value: List[VmwareDistributedVirtualSwitch.LacpGroupConfig]):
            self._lacpGroupConfig = value
        @property
        def lacpApiVersion(self) -> str: ...
        @lacpApiVersion.setter
        def lacpApiVersion(self, value: str):
            self._lacpApiVersion = value
        @property
        def multicastFilteringMode(self) -> str: ...
        @multicastFilteringMode.setter
        def multicastFilteringMode(self, value: str):
            self._multicastFilteringMode = value
        @property
        def networkOffloadSpecId(self) -> str: ...
        @networkOffloadSpecId.setter
        def networkOffloadSpecId(self, value: str):
            self._networkOffloadSpecId = value


    class ConfigSpec(vim.DistributedVirtualSwitch.ConfigSpec):
        @property
        def pvlanConfigSpec(self) -> List[VmwareDistributedVirtualSwitch.PvlanConfigSpec]: ...
        @pvlanConfigSpec.setter
        def pvlanConfigSpec(self, value: List[VmwareDistributedVirtualSwitch.PvlanConfigSpec]):
            self._pvlanConfigSpec = value
        @property
        def vspanConfigSpec(self) -> List[VmwareDistributedVirtualSwitch.VspanConfigSpec]: ...
        @vspanConfigSpec.setter
        def vspanConfigSpec(self, value: List[VmwareDistributedVirtualSwitch.VspanConfigSpec]):
            self._vspanConfigSpec = value
        @property
        def maxMtu(self) -> int: ...
        @maxMtu.setter
        def maxMtu(self, value: int):
            self._maxMtu = value
        @property
        def linkDiscoveryProtocolConfig(self) -> vim.host.LinkDiscoveryProtocolConfig: ...
        @linkDiscoveryProtocolConfig.setter
        def linkDiscoveryProtocolConfig(self, value: vim.host.LinkDiscoveryProtocolConfig):
            self._linkDiscoveryProtocolConfig = value
        @property
        def ipfixConfig(self) -> VmwareDistributedVirtualSwitch.IpfixConfig: ...
        @ipfixConfig.setter
        def ipfixConfig(self, value: VmwareDistributedVirtualSwitch.IpfixConfig):
            self._ipfixConfig = value
        @property
        def lacpApiVersion(self) -> str: ...
        @lacpApiVersion.setter
        def lacpApiVersion(self, value: str):
            self._lacpApiVersion = value
        @property
        def multicastFilteringMode(self) -> str: ...
        @multicastFilteringMode.setter
        def multicastFilteringMode(self, value: str):
            self._multicastFilteringMode = value
        @property
        def networkOffloadSpecId(self) -> str: ...
        @networkOffloadSpecId.setter
        def networkOffloadSpecId(self, value: str):
            self._networkOffloadSpecId = value


    class DpuFeatureCapability(vmodl.DynamicData):
        @property
        def networkOffloadSupported(self) -> bool: ...
        @networkOffloadSupported.setter
        def networkOffloadSupported(self, value: bool):
            self._networkOffloadSupported = value


    class FailureCriteria(vim.InheritablePolicy):
        @property
        def checkSpeed(self) -> vim.StringPolicy: ...
        @checkSpeed.setter
        def checkSpeed(self, value: vim.StringPolicy):
            self._checkSpeed = value
        @property
        def speed(self) -> vim.IntPolicy: ...
        @speed.setter
        def speed(self, value: vim.IntPolicy):
            self._speed = value
        @property
        def checkDuplex(self) -> vim.BoolPolicy: ...
        @checkDuplex.setter
        def checkDuplex(self, value: vim.BoolPolicy):
            self._checkDuplex = value
        @property
        def fullDuplex(self) -> vim.BoolPolicy: ...
        @fullDuplex.setter
        def fullDuplex(self, value: vim.BoolPolicy):
            self._fullDuplex = value
        @property
        def checkErrorPercent(self) -> vim.BoolPolicy: ...
        @checkErrorPercent.setter
        def checkErrorPercent(self, value: vim.BoolPolicy):
            self._checkErrorPercent = value
        @property
        def percentage(self) -> vim.IntPolicy: ...
        @percentage.setter
        def percentage(self, value: vim.IntPolicy):
            self._percentage = value
        @property
        def checkBeacon(self) -> vim.BoolPolicy: ...
        @checkBeacon.setter
        def checkBeacon(self, value: vim.BoolPolicy):
            self._checkBeacon = value


    class FeatureCapability(vim.DistributedVirtualSwitch.FeatureCapability):
        @property
        def vspanSupported(self) -> bool: ...
        @vspanSupported.setter
        def vspanSupported(self, value: bool):
            self._vspanSupported = value
        @property
        def lldpSupported(self) -> bool: ...
        @lldpSupported.setter
        def lldpSupported(self, value: bool):
            self._lldpSupported = value
        @property
        def ipfixSupported(self) -> bool: ...
        @ipfixSupported.setter
        def ipfixSupported(self, value: bool):
            self._ipfixSupported = value
        @property
        def ipfixCapability(self) -> VmwareDistributedVirtualSwitch.IpfixFeatureCapability: ...
        @ipfixCapability.setter
        def ipfixCapability(self, value: VmwareDistributedVirtualSwitch.IpfixFeatureCapability):
            self._ipfixCapability = value
        @property
        def multicastSnoopingSupported(self) -> bool: ...
        @multicastSnoopingSupported.setter
        def multicastSnoopingSupported(self, value: bool):
            self._multicastSnoopingSupported = value
        @property
        def vspanCapability(self) -> VmwareDistributedVirtualSwitch.VspanFeatureCapability: ...
        @vspanCapability.setter
        def vspanCapability(self, value: VmwareDistributedVirtualSwitch.VspanFeatureCapability):
            self._vspanCapability = value
        @property
        def lacpCapability(self) -> VmwareDistributedVirtualSwitch.LacpFeatureCapability: ...
        @lacpCapability.setter
        def lacpCapability(self, value: VmwareDistributedVirtualSwitch.LacpFeatureCapability):
            self._lacpCapability = value
        @property
        def dpuCapability(self) -> VmwareDistributedVirtualSwitch.DpuFeatureCapability: ...
        @dpuCapability.setter
        def dpuCapability(self, value: VmwareDistributedVirtualSwitch.DpuFeatureCapability):
            self._dpuCapability = value
        @property
        def nsxSupported(self) -> bool: ...
        @nsxSupported.setter
        def nsxSupported(self, value: bool):
            self._nsxSupported = value
        @property
        def mtuCapability(self) -> VmwareDistributedVirtualSwitch.MtuCapability: ...
        @mtuCapability.setter
        def mtuCapability(self, value: VmwareDistributedVirtualSwitch.MtuCapability):
            self._mtuCapability = value


    class IpfixConfig(vmodl.DynamicData):
        @property
        def collectorIpAddress(self) -> str: ...
        @collectorIpAddress.setter
        def collectorIpAddress(self, value: str):
            self._collectorIpAddress = value
        @property
        def collectorPort(self) -> int: ...
        @collectorPort.setter
        def collectorPort(self, value: int):
            self._collectorPort = value
        @property
        def observationDomainId(self) -> long: ...
        @observationDomainId.setter
        def observationDomainId(self, value: long):
            self._observationDomainId = value
        @property
        def activeFlowTimeout(self) -> int: ...
        @activeFlowTimeout.setter
        def activeFlowTimeout(self, value: int):
            self._activeFlowTimeout = value
        @property
        def idleFlowTimeout(self) -> int: ...
        @idleFlowTimeout.setter
        def idleFlowTimeout(self, value: int):
            self._idleFlowTimeout = value
        @property
        def samplingRate(self) -> int: ...
        @samplingRate.setter
        def samplingRate(self, value: int):
            self._samplingRate = value
        @property
        def internalFlowsOnly(self) -> bool: ...
        @internalFlowsOnly.setter
        def internalFlowsOnly(self, value: bool):
            self._internalFlowsOnly = value


    class IpfixFeatureCapability(vmodl.DynamicData):
        @property
        def ipfixSupported(self) -> bool: ...
        @ipfixSupported.setter
        def ipfixSupported(self, value: bool):
            self._ipfixSupported = value
        @property
        def ipv6ForIpfixSupported(self) -> bool: ...
        @ipv6ForIpfixSupported.setter
        def ipv6ForIpfixSupported(self, value: bool):
            self._ipv6ForIpfixSupported = value
        @property
        def observationDomainIdSupported(self) -> bool: ...
        @observationDomainIdSupported.setter
        def observationDomainIdSupported(self, value: bool):
            self._observationDomainIdSupported = value


    class LacpFeatureCapability(vmodl.DynamicData):
        @property
        def lacpSupported(self) -> bool: ...
        @lacpSupported.setter
        def lacpSupported(self, value: bool):
            self._lacpSupported = value
        @property
        def multiLacpGroupSupported(self) -> bool: ...
        @multiLacpGroupSupported.setter
        def multiLacpGroupSupported(self, value: bool):
            self._multiLacpGroupSupported = value
        @property
        def lacpFastModeSupported(self) -> bool: ...
        @lacpFastModeSupported.setter
        def lacpFastModeSupported(self, value: bool):
            self._lacpFastModeSupported = value


    class LacpGroupConfig(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def mode(self) -> str: ...
        @mode.setter
        def mode(self, value: str):
            self._mode = value
        @property
        def uplinkNum(self) -> int: ...
        @uplinkNum.setter
        def uplinkNum(self, value: int):
            self._uplinkNum = value
        @property
        def loadbalanceAlgorithm(self) -> str: ...
        @loadbalanceAlgorithm.setter
        def loadbalanceAlgorithm(self, value: str):
            self._loadbalanceAlgorithm = value
        @property
        def vlan(self) -> VmwareDistributedVirtualSwitch.LagVlanConfig: ...
        @vlan.setter
        def vlan(self, value: VmwareDistributedVirtualSwitch.LagVlanConfig):
            self._vlan = value
        @property
        def ipfix(self) -> VmwareDistributedVirtualSwitch.LagIpfixConfig: ...
        @ipfix.setter
        def ipfix(self, value: VmwareDistributedVirtualSwitch.LagIpfixConfig):
            self._ipfix = value
        @property
        def uplinkName(self) -> List[str]: ...
        @uplinkName.setter
        def uplinkName(self, value: List[str]):
            self._uplinkName = value
        @property
        def uplinkPortKey(self) -> List[str]: ...
        @uplinkPortKey.setter
        def uplinkPortKey(self, value: List[str]):
            self._uplinkPortKey = value
        @property
        def timeoutMode(self) -> str: ...
        @timeoutMode.setter
        def timeoutMode(self, value: str):
            self._timeoutMode = value


    class LacpGroupSpec(vmodl.DynamicData):
        @property
        def lacpGroupConfig(self) -> VmwareDistributedVirtualSwitch.LacpGroupConfig: ...
        @lacpGroupConfig.setter
        def lacpGroupConfig(self, value: VmwareDistributedVirtualSwitch.LacpGroupConfig):
            self._lacpGroupConfig = value
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value


    class LagIpfixConfig(vmodl.DynamicData):
        @property
        def ipfixEnabled(self) -> bool: ...
        @ipfixEnabled.setter
        def ipfixEnabled(self, value: bool):
            self._ipfixEnabled = value


    class LagVlanConfig(vmodl.DynamicData):
        @property
        def vlanId(self) -> List[vim.NumericRange]: ...
        @vlanId.setter
        def vlanId(self, value: List[vim.NumericRange]):
            self._vlanId = value


    class MacLearningPolicy(vim.InheritablePolicy):
        @property
        def enabled(self) -> bool: ...
        @enabled.setter
        def enabled(self, value: bool):
            self._enabled = value
        @property
        def allowUnicastFlooding(self) -> bool: ...
        @allowUnicastFlooding.setter
        def allowUnicastFlooding(self, value: bool):
            self._allowUnicastFlooding = value
        @property
        def limit(self) -> int: ...
        @limit.setter
        def limit(self, value: int):
            self._limit = value
        @property
        def limitPolicy(self) -> str: ...
        @limitPolicy.setter
        def limitPolicy(self, value: str):
            self._limitPolicy = value


    class MacManagementPolicy(vim.InheritablePolicy):
        @property
        def allowPromiscuous(self) -> bool: ...
        @allowPromiscuous.setter
        def allowPromiscuous(self, value: bool):
            self._allowPromiscuous = value
        @property
        def macChanges(self) -> bool: ...
        @macChanges.setter
        def macChanges(self, value: bool):
            self._macChanges = value
        @property
        def forgedTransmits(self) -> bool: ...
        @forgedTransmits.setter
        def forgedTransmits(self, value: bool):
            self._forgedTransmits = value
        @property
        def macLearningPolicy(self) -> VmwareDistributedVirtualSwitch.MacLearningPolicy: ...
        @macLearningPolicy.setter
        def macLearningPolicy(self, value: VmwareDistributedVirtualSwitch.MacLearningPolicy):
            self._macLearningPolicy = value


    class MtuCapability(vmodl.DynamicData):
        @property
        def minMtuSupported(self) -> int: ...
        @minMtuSupported.setter
        def minMtuSupported(self, value: int):
            self._minMtuSupported = value
        @property
        def maxMtuSupported(self) -> int: ...
        @maxMtuSupported.setter
        def maxMtuSupported(self, value: int):
            self._maxMtuSupported = value


    class MtuHealthCheckResult(HostMember.UplinkHealthCheckResult):
        @property
        def mtuMismatch(self) -> bool: ...
        @mtuMismatch.setter
        def mtuMismatch(self, value: bool):
            self._mtuMismatch = value
        @property
        def vlanSupportSwitchMtu(self) -> List[vim.NumericRange]: ...
        @vlanSupportSwitchMtu.setter
        def vlanSupportSwitchMtu(self, value: List[vim.NumericRange]):
            self._vlanSupportSwitchMtu = value
        @property
        def vlanNotSupportSwitchMtu(self) -> List[vim.NumericRange]: ...
        @vlanNotSupportSwitchMtu.setter
        def vlanNotSupportSwitchMtu(self, value: List[vim.NumericRange]):
            self._vlanNotSupportSwitchMtu = value


    class PvlanConfigSpec(vmodl.DynamicData):
        @property
        def pvlanEntry(self) -> VmwareDistributedVirtualSwitch.PvlanMapEntry: ...
        @pvlanEntry.setter
        def pvlanEntry(self, value: VmwareDistributedVirtualSwitch.PvlanMapEntry):
            self._pvlanEntry = value
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value


    class PvlanMapEntry(vmodl.DynamicData):
        @property
        def primaryVlanId(self) -> int: ...
        @primaryVlanId.setter
        def primaryVlanId(self, value: int):
            self._primaryVlanId = value
        @property
        def secondaryVlanId(self) -> int: ...
        @secondaryVlanId.setter
        def secondaryVlanId(self, value: int):
            self._secondaryVlanId = value
        @property
        def pvlanType(self) -> str: ...
        @pvlanType.setter
        def pvlanType(self, value: str):
            self._pvlanType = value


    class PvlanSpec(VmwareDistributedVirtualSwitch.VlanSpec):
        @property
        def pvlanId(self) -> int: ...
        @pvlanId.setter
        def pvlanId(self, value: int):
            self._pvlanId = value


    class SecurityPolicy(vim.InheritablePolicy):
        @property
        def allowPromiscuous(self) -> vim.BoolPolicy: ...
        @allowPromiscuous.setter
        def allowPromiscuous(self, value: vim.BoolPolicy):
            self._allowPromiscuous = value
        @property
        def macChanges(self) -> vim.BoolPolicy: ...
        @macChanges.setter
        def macChanges(self, value: vim.BoolPolicy):
            self._macChanges = value
        @property
        def forgedTransmits(self) -> vim.BoolPolicy: ...
        @forgedTransmits.setter
        def forgedTransmits(self, value: vim.BoolPolicy):
            self._forgedTransmits = value


    class TeamingHealthCheckConfig(VmwareDistributedVirtualSwitch.VmwareHealthCheckConfig): ...


    class TeamingHealthCheckResult(HostMember.HealthCheckResult):
        @property
        def teamingStatus(self) -> str: ...
        @teamingStatus.setter
        def teamingStatus(self, value: str):
            self._teamingStatus = value


    class TrunkVlanSpec(VmwareDistributedVirtualSwitch.VlanSpec):
        @property
        def vlanId(self) -> List[vim.NumericRange]: ...
        @vlanId.setter
        def vlanId(self, value: List[vim.NumericRange]):
            self._vlanId = value


    class UplinkLacpPolicy(vim.InheritablePolicy):
        @property
        def enable(self) -> vim.BoolPolicy: ...
        @enable.setter
        def enable(self, value: vim.BoolPolicy):
            self._enable = value
        @property
        def mode(self) -> vim.StringPolicy: ...
        @mode.setter
        def mode(self, value: vim.StringPolicy):
            self._mode = value


    class UplinkPortOrderPolicy(vim.InheritablePolicy):
        @property
        def activeUplinkPort(self) -> List[str]: ...
        @activeUplinkPort.setter
        def activeUplinkPort(self, value: List[str]):
            self._activeUplinkPort = value
        @property
        def standbyUplinkPort(self) -> List[str]: ...
        @standbyUplinkPort.setter
        def standbyUplinkPort(self, value: List[str]):
            self._standbyUplinkPort = value


    class UplinkPortTeamingPolicy(vim.InheritablePolicy):
        @property
        def policy(self) -> vim.StringPolicy: ...
        @policy.setter
        def policy(self, value: vim.StringPolicy):
            self._policy = value
        @property
        def reversePolicy(self) -> vim.BoolPolicy: ...
        @reversePolicy.setter
        def reversePolicy(self, value: vim.BoolPolicy):
            self._reversePolicy = value
        @property
        def notifySwitches(self) -> vim.BoolPolicy: ...
        @notifySwitches.setter
        def notifySwitches(self, value: vim.BoolPolicy):
            self._notifySwitches = value
        @property
        def rollingOrder(self) -> vim.BoolPolicy: ...
        @rollingOrder.setter
        def rollingOrder(self, value: vim.BoolPolicy):
            self._rollingOrder = value
        @property
        def failureCriteria(self) -> VmwareDistributedVirtualSwitch.FailureCriteria: ...
        @failureCriteria.setter
        def failureCriteria(self, value: VmwareDistributedVirtualSwitch.FailureCriteria):
            self._failureCriteria = value
        @property
        def uplinkPortOrder(self) -> VmwareDistributedVirtualSwitch.UplinkPortOrderPolicy: ...
        @uplinkPortOrder.setter
        def uplinkPortOrder(self, value: VmwareDistributedVirtualSwitch.UplinkPortOrderPolicy):
            self._uplinkPortOrder = value


    class VMwarePortgroupPolicy(DistributedVirtualPortgroup.PortgroupPolicy):
        @property
        def vlanOverrideAllowed(self) -> bool: ...
        @vlanOverrideAllowed.setter
        def vlanOverrideAllowed(self, value: bool):
            self._vlanOverrideAllowed = value
        @property
        def uplinkTeamingOverrideAllowed(self) -> bool: ...
        @uplinkTeamingOverrideAllowed.setter
        def uplinkTeamingOverrideAllowed(self, value: bool):
            self._uplinkTeamingOverrideAllowed = value
        @property
        def securityPolicyOverrideAllowed(self) -> bool: ...
        @securityPolicyOverrideAllowed.setter
        def securityPolicyOverrideAllowed(self, value: bool):
            self._securityPolicyOverrideAllowed = value
        @property
        def ipfixOverrideAllowed(self) -> bool: ...
        @ipfixOverrideAllowed.setter
        def ipfixOverrideAllowed(self, value: bool):
            self._ipfixOverrideAllowed = value
        @property
        def macManagementOverrideAllowed(self) -> bool: ...
        @macManagementOverrideAllowed.setter
        def macManagementOverrideAllowed(self, value: bool):
            self._macManagementOverrideAllowed = value


    class VlanHealthCheckResult(HostMember.UplinkHealthCheckResult):
        @property
        def trunkedVlan(self) -> List[vim.NumericRange]: ...
        @trunkedVlan.setter
        def trunkedVlan(self, value: List[vim.NumericRange]):
            self._trunkedVlan = value
        @property
        def untrunkedVlan(self) -> List[vim.NumericRange]: ...
        @untrunkedVlan.setter
        def untrunkedVlan(self, value: List[vim.NumericRange]):
            self._untrunkedVlan = value


    class VlanIdSpec(VmwareDistributedVirtualSwitch.VlanSpec):
        @property
        def vlanId(self) -> int: ...
        @vlanId.setter
        def vlanId(self, value: int):
            self._vlanId = value


    class VlanMtuHealthCheckConfig(VmwareDistributedVirtualSwitch.VmwareHealthCheckConfig): ...


    class VlanSpec(vim.InheritablePolicy): ...


    class VmwareHealthCheckConfig(vim.DistributedVirtualSwitch.HealthCheckConfig): ...


    class VmwareHealthCheckFeatureCapability(vim.DistributedVirtualSwitch.HealthCheckFeatureCapability):
        @property
        def vlanMtuSupported(self) -> bool: ...
        @vlanMtuSupported.setter
        def vlanMtuSupported(self, value: bool):
            self._vlanMtuSupported = value
        @property
        def teamingSupported(self) -> bool: ...
        @teamingSupported.setter
        def teamingSupported(self, value: bool):
            self._teamingSupported = value


    class VmwarePortConfigPolicy(DistributedVirtualPort.Setting):
        @property
        def vlan(self) -> VmwareDistributedVirtualSwitch.VlanSpec: ...
        @vlan.setter
        def vlan(self, value: VmwareDistributedVirtualSwitch.VlanSpec):
            self._vlan = value
        @property
        def qosTag(self) -> vim.IntPolicy: ...
        @qosTag.setter
        def qosTag(self, value: vim.IntPolicy):
            self._qosTag = value
        @property
        def uplinkTeamingPolicy(self) -> VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy: ...
        @uplinkTeamingPolicy.setter
        def uplinkTeamingPolicy(self, value: VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy):
            self._uplinkTeamingPolicy = value
        @property
        def securityPolicy(self) -> VmwareDistributedVirtualSwitch.SecurityPolicy: ...
        @securityPolicy.setter
        def securityPolicy(self, value: VmwareDistributedVirtualSwitch.SecurityPolicy):
            self._securityPolicy = value
        @property
        def ipfixEnabled(self) -> vim.BoolPolicy: ...
        @ipfixEnabled.setter
        def ipfixEnabled(self, value: vim.BoolPolicy):
            self._ipfixEnabled = value
        @property
        def txUplink(self) -> vim.BoolPolicy: ...
        @txUplink.setter
        def txUplink(self, value: vim.BoolPolicy):
            self._txUplink = value
        @property
        def lacpPolicy(self) -> VmwareDistributedVirtualSwitch.UplinkLacpPolicy: ...
        @lacpPolicy.setter
        def lacpPolicy(self, value: VmwareDistributedVirtualSwitch.UplinkLacpPolicy):
            self._lacpPolicy = value
        @property
        def macManagementPolicy(self) -> VmwareDistributedVirtualSwitch.MacManagementPolicy: ...
        @macManagementPolicy.setter
        def macManagementPolicy(self, value: VmwareDistributedVirtualSwitch.MacManagementPolicy):
            self._macManagementPolicy = value
        @property
        def VNI(self) -> vim.IntPolicy: ...
        @VNI.setter
        def VNI(self, value: vim.IntPolicy):
            self._VNI = value


    class VspanConfigSpec(vmodl.DynamicData):
        @property
        def vspanSession(self) -> VmwareDistributedVirtualSwitch.VspanSession: ...
        @vspanSession.setter
        def vspanSession(self, value: VmwareDistributedVirtualSwitch.VspanSession):
            self._vspanSession = value
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value


    class VspanFeatureCapability(vmodl.DynamicData):
        @property
        def mixedDestSupported(self) -> bool: ...
        @mixedDestSupported.setter
        def mixedDestSupported(self, value: bool):
            self._mixedDestSupported = value
        @property
        def dvportSupported(self) -> bool: ...
        @dvportSupported.setter
        def dvportSupported(self, value: bool):
            self._dvportSupported = value
        @property
        def remoteSourceSupported(self) -> bool: ...
        @remoteSourceSupported.setter
        def remoteSourceSupported(self, value: bool):
            self._remoteSourceSupported = value
        @property
        def remoteDestSupported(self) -> bool: ...
        @remoteDestSupported.setter
        def remoteDestSupported(self, value: bool):
            self._remoteDestSupported = value
        @property
        def encapRemoteSourceSupported(self) -> bool: ...
        @encapRemoteSourceSupported.setter
        def encapRemoteSourceSupported(self, value: bool):
            self._encapRemoteSourceSupported = value
        @property
        def erspanProtocolSupported(self) -> bool: ...
        @erspanProtocolSupported.setter
        def erspanProtocolSupported(self, value: bool):
            self._erspanProtocolSupported = value
        @property
        def mirrorNetstackSupported(self) -> bool: ...
        @mirrorNetstackSupported.setter
        def mirrorNetstackSupported(self, value: bool):
            self._mirrorNetstackSupported = value


    class VspanPorts(vmodl.DynamicData):
        @property
        def portKey(self) -> List[str]: ...
        @portKey.setter
        def portKey(self, value: List[str]):
            self._portKey = value
        @property
        def uplinkPortName(self) -> List[str]: ...
        @uplinkPortName.setter
        def uplinkPortName(self, value: List[str]):
            self._uplinkPortName = value
        @property
        def wildcardPortConnecteeType(self) -> List[str]: ...
        @wildcardPortConnecteeType.setter
        def wildcardPortConnecteeType(self, value: List[str]):
            self._wildcardPortConnecteeType = value
        @property
        def vlans(self) -> List[int]: ...
        @vlans.setter
        def vlans(self, value: List[int]):
            self._vlans = value
        @property
        def ipAddress(self) -> List[str]: ...
        @ipAddress.setter
        def ipAddress(self, value: List[str]):
            self._ipAddress = value


    class VspanSession(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
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
        def enabled(self) -> bool: ...
        @enabled.setter
        def enabled(self, value: bool):
            self._enabled = value
        @property
        def sourcePortTransmitted(self) -> VmwareDistributedVirtualSwitch.VspanPorts: ...
        @sourcePortTransmitted.setter
        def sourcePortTransmitted(self, value: VmwareDistributedVirtualSwitch.VspanPorts):
            self._sourcePortTransmitted = value
        @property
        def sourcePortReceived(self) -> VmwareDistributedVirtualSwitch.VspanPorts: ...
        @sourcePortReceived.setter
        def sourcePortReceived(self, value: VmwareDistributedVirtualSwitch.VspanPorts):
            self._sourcePortReceived = value
        @property
        def destinationPort(self) -> VmwareDistributedVirtualSwitch.VspanPorts: ...
        @destinationPort.setter
        def destinationPort(self, value: VmwareDistributedVirtualSwitch.VspanPorts):
            self._destinationPort = value
        @property
        def encapsulationVlanId(self) -> int: ...
        @encapsulationVlanId.setter
        def encapsulationVlanId(self, value: int):
            self._encapsulationVlanId = value
        @property
        def stripOriginalVlan(self) -> bool: ...
        @stripOriginalVlan.setter
        def stripOriginalVlan(self, value: bool):
            self._stripOriginalVlan = value
        @property
        def mirroredPacketLength(self) -> int: ...
        @mirroredPacketLength.setter
        def mirroredPacketLength(self, value: int):
            self._mirroredPacketLength = value
        @property
        def normalTrafficAllowed(self) -> bool: ...
        @normalTrafficAllowed.setter
        def normalTrafficAllowed(self, value: bool):
            self._normalTrafficAllowed = value
        @property
        def sessionType(self) -> str: ...
        @sessionType.setter
        def sessionType(self, value: str):
            self._sessionType = value
        @property
        def samplingRate(self) -> int: ...
        @samplingRate.setter
        def samplingRate(self, value: int):
            self._samplingRate = value
        @property
        def encapType(self) -> str: ...
        @encapType.setter
        def encapType(self, value: str):
            self._encapType = value
        @property
        def erspanId(self) -> int: ...
        @erspanId.setter
        def erspanId(self, value: int):
            self._erspanId = value
        @property
        def erspanCOS(self) -> int: ...
        @erspanCOS.setter
        def erspanCOS(self, value: int):
            self._erspanCOS = value
        @property
        def erspanGraNanosec(self) -> bool: ...
        @erspanGraNanosec.setter
        def erspanGraNanosec(self, value: bool):
            self._erspanGraNanosec = value
        @property
        def netstack(self) -> str: ...
        @netstack.setter
        def netstack(self, value: str):
            self._netstack = value


    class LacpApiVersion(Enum):
        singleLag = "singleLag"
        multipleLag = "multipleLag"


    class LacpLoadBalanceAlgorithm(Enum):
        srcMac = "srcMac"
        destMac = "destMac"
        srcDestMac = "srcDestMac"
        destIpVlan = "destIpVlan"
        srcIpVlan = "srcIpVlan"
        srcDestIpVlan = "srcDestIpVlan"
        destTcpUdpPort = "destTcpUdpPort"
        srcTcpUdpPort = "srcTcpUdpPort"
        srcDestTcpUdpPort = "srcDestTcpUdpPort"
        destIpTcpUdpPort = "destIpTcpUdpPort"
        srcIpTcpUdpPort = "srcIpTcpUdpPort"
        srcDestIpTcpUdpPort = "srcDestIpTcpUdpPort"
        destIpTcpUdpPortVlan = "destIpTcpUdpPortVlan"
        srcIpTcpUdpPortVlan = "srcIpTcpUdpPortVlan"
        srcDestIpTcpUdpPortVlan = "srcDestIpTcpUdpPortVlan"
        destIp = "destIp"
        srcIp = "srcIp"
        srcDestIp = "srcDestIp"
        vlan = "vlan"
        srcPortId = "srcPortId"


    class MacLimitPolicyType(Enum):
        allow = "allow"
        drop = "drop"


    class MulticastFilteringMode(Enum):
        legacyFiltering = "legacyFiltering"
        snooping = "snooping"


    class PvlanPortType(Enum):
        promiscuous = "promiscuous"
        isolated = "isolated"
        community = "community"


    class TeamingMatchStatus(Enum):
        iphashMatch = "iphashMatch"
        nonIphashMatch = "nonIphashMatch"
        iphashMismatch = "iphashMismatch"
        nonIphashMismatch = "nonIphashMismatch"


    class UplinkLacpMode(Enum):
        active = "active"
        passive = "passive"


    class UplinkLacpTimeoutMode(Enum):
        fast = "fast"
        slow = "slow"


    class VspanSessionEncapType(Enum):
        gre = "gre"
        erspan2 = "erspan2"
        erspan3 = "erspan3"


    class VspanSessionType(Enum):
        mixedDestMirror = "mixedDestMirror"
        dvPortMirror = "dvPortMirror"
        remoteMirrorSource = "remoteMirrorSource"
        remoteMirrorDest = "remoteMirrorDest"
        encapsulatedRemoteMirrorSource = "encapsulatedRemoteMirrorSource"


class DistributedVirtualPort(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def config(self) -> DistributedVirtualPort.ConfigInfo: ...
    @config.setter
    def config(self, value: DistributedVirtualPort.ConfigInfo):
        self._config = value
    @property
    def dvsUuid(self) -> str: ...
    @dvsUuid.setter
    def dvsUuid(self, value: str):
        self._dvsUuid = value
    @property
    def portgroupKey(self) -> str: ...
    @portgroupKey.setter
    def portgroupKey(self, value: str):
        self._portgroupKey = value
    @property
    def proxyHost(self) -> vim.HostSystem: ...
    @proxyHost.setter
    def proxyHost(self, value: vim.HostSystem):
        self._proxyHost = value
    @property
    def connectee(self) -> PortConnectee: ...
    @connectee.setter
    def connectee(self, value: PortConnectee):
        self._connectee = value
    @property
    def conflict(self) -> bool: ...
    @conflict.setter
    def conflict(self, value: bool):
        self._conflict = value
    @property
    def conflictPortKey(self) -> str: ...
    @conflictPortKey.setter
    def conflictPortKey(self, value: str):
        self._conflictPortKey = value
    @property
    def state(self) -> DistributedVirtualPort.State: ...
    @state.setter
    def state(self, value: DistributedVirtualPort.State):
        self._state = value
    @property
    def connectionCookie(self) -> int: ...
    @connectionCookie.setter
    def connectionCookie(self, value: int):
        self._connectionCookie = value
    @property
    def lastStatusChange(self) -> datetime: ...
    @lastStatusChange.setter
    def lastStatusChange(self, value: datetime):
        self._lastStatusChange = value
    @property
    def hostLocalPort(self) -> bool: ...
    @hostLocalPort.setter
    def hostLocalPort(self, value: bool):
        self._hostLocalPort = value
    @property
    def externalId(self) -> str: ...
    @externalId.setter
    def externalId(self, value: str):
        self._externalId = value
    @property
    def segmentPortId(self) -> str: ...
    @segmentPortId.setter
    def segmentPortId(self, value: str):
        self._segmentPortId = value


    class ConfigInfo(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def scope(self) -> List[vim.ManagedEntity]: ...
        @scope.setter
        def scope(self, value: List[vim.ManagedEntity]):
            self._scope = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value
        @property
        def setting(self) -> DistributedVirtualPort.Setting: ...
        @setting.setter
        def setting(self, value: DistributedVirtualPort.Setting):
            self._setting = value
        @property
        def configVersion(self) -> str: ...
        @configVersion.setter
        def configVersion(self, value: str):
            self._configVersion = value


    class ConfigSpec(vmodl.DynamicData):
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def scope(self) -> List[vim.ManagedEntity]: ...
        @scope.setter
        def scope(self, value: List[vim.ManagedEntity]):
            self._scope = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value
        @property
        def setting(self) -> DistributedVirtualPort.Setting: ...
        @setting.setter
        def setting(self, value: DistributedVirtualPort.Setting):
            self._setting = value
        @property
        def configVersion(self) -> str: ...
        @configVersion.setter
        def configVersion(self, value: str):
            self._configVersion = value


    class FilterConfig(vim.InheritablePolicy):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def agentName(self) -> str: ...
        @agentName.setter
        def agentName(self, value: str):
            self._agentName = value
        @property
        def slotNumber(self) -> str: ...
        @slotNumber.setter
        def slotNumber(self, value: str):
            self._slotNumber = value
        @property
        def parameters(self) -> DistributedVirtualPort.FilterParameter: ...
        @parameters.setter
        def parameters(self, value: DistributedVirtualPort.FilterParameter):
            self._parameters = value
        @property
        def onFailure(self) -> str: ...
        @onFailure.setter
        def onFailure(self, value: str):
            self._onFailure = value


    class FilterConfigSpec(DistributedVirtualPort.FilterConfig):
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value


    class FilterParameter(vmodl.DynamicData):
        @property
        def parameters(self) -> List[str]: ...
        @parameters.setter
        def parameters(self, value: List[str]):
            self._parameters = value


    class FilterPolicy(vim.InheritablePolicy):
        @property
        def filterConfig(self) -> List[DistributedVirtualPort.FilterConfig]: ...
        @filterConfig.setter
        def filterConfig(self, value: List[DistributedVirtualPort.FilterConfig]):
            self._filterConfig = value


    class HostLocalPortInfo(vmodl.DynamicData):
        @property
        def switchUuid(self) -> str: ...
        @switchUuid.setter
        def switchUuid(self, value: str):
            self._switchUuid = value
        @property
        def portKey(self) -> str: ...
        @portKey.setter
        def portKey(self, value: str):
            self._portKey = value
        @property
        def setting(self) -> DistributedVirtualPort.Setting: ...
        @setting.setter
        def setting(self, value: DistributedVirtualPort.Setting):
            self._setting = value
        @property
        def vnic(self) -> str: ...
        @vnic.setter
        def vnic(self, value: str):
            self._vnic = value


    class RuntimeInfo(vmodl.DynamicData):
        @property
        def linkUp(self) -> bool: ...
        @linkUp.setter
        def linkUp(self, value: bool):
            self._linkUp = value
        @property
        def blocked(self) -> bool: ...
        @blocked.setter
        def blocked(self, value: bool):
            self._blocked = value
        @property
        def vlanIds(self) -> List[vim.NumericRange]: ...
        @vlanIds.setter
        def vlanIds(self, value: List[vim.NumericRange]):
            self._vlanIds = value
        @property
        def trunkingMode(self) -> bool: ...
        @trunkingMode.setter
        def trunkingMode(self, value: bool):
            self._trunkingMode = value
        @property
        def mtu(self) -> int: ...
        @mtu.setter
        def mtu(self, value: int):
            self._mtu = value
        @property
        def linkPeer(self) -> str: ...
        @linkPeer.setter
        def linkPeer(self, value: str):
            self._linkPeer = value
        @property
        def macAddress(self) -> str: ...
        @macAddress.setter
        def macAddress(self, value: str):
            self._macAddress = value
        @property
        def statusDetail(self) -> str: ...
        @statusDetail.setter
        def statusDetail(self, value: str):
            self._statusDetail = value
        @property
        def vmDirectPathGen2Active(self) -> bool: ...
        @vmDirectPathGen2Active.setter
        def vmDirectPathGen2Active(self, value: bool):
            self._vmDirectPathGen2Active = value
        @property
        def vmDirectPathGen2InactiveReasonNetwork(self) -> List[str]: ...
        @vmDirectPathGen2InactiveReasonNetwork.setter
        def vmDirectPathGen2InactiveReasonNetwork(self, value: List[str]):
            self._vmDirectPathGen2InactiveReasonNetwork = value
        @property
        def vmDirectPathGen2InactiveReasonOther(self) -> List[str]: ...
        @vmDirectPathGen2InactiveReasonOther.setter
        def vmDirectPathGen2InactiveReasonOther(self, value: List[str]):
            self._vmDirectPathGen2InactiveReasonOther = value
        @property
        def vmDirectPathGen2InactiveReasonExtended(self) -> str: ...
        @vmDirectPathGen2InactiveReasonExtended.setter
        def vmDirectPathGen2InactiveReasonExtended(self, value: str):
            self._vmDirectPathGen2InactiveReasonExtended = value


        class VmDirectPathGen2InactiveReasonNetwork(Enum):
            portNptIncompatibleDvs = "portNptIncompatibleDvs"
            portNptNoCompatibleNics = "portNptNoCompatibleNics"
            portNptNoVirtualFunctionsAvailable = "portNptNoVirtualFunctionsAvailable"
            portNptDisabledForPort = "portNptDisabledForPort"


        class VmDirectPathGen2InactiveReasonOther(Enum):
            portNptIncompatibleHost = "portNptIncompatibleHost"
            portNptIncompatibleConnectee = "portNptIncompatibleConnectee"


    class Setting(vmodl.DynamicData):
        @property
        def blocked(self) -> vim.BoolPolicy: ...
        @blocked.setter
        def blocked(self, value: vim.BoolPolicy):
            self._blocked = value
        @property
        def vmDirectPathGen2Allowed(self) -> vim.BoolPolicy: ...
        @vmDirectPathGen2Allowed.setter
        def vmDirectPathGen2Allowed(self, value: vim.BoolPolicy):
            self._vmDirectPathGen2Allowed = value
        @property
        def inShapingPolicy(self) -> DistributedVirtualPort.TrafficShapingPolicy: ...
        @inShapingPolicy.setter
        def inShapingPolicy(self, value: DistributedVirtualPort.TrafficShapingPolicy):
            self._inShapingPolicy = value
        @property
        def outShapingPolicy(self) -> DistributedVirtualPort.TrafficShapingPolicy: ...
        @outShapingPolicy.setter
        def outShapingPolicy(self, value: DistributedVirtualPort.TrafficShapingPolicy):
            self._outShapingPolicy = value
        @property
        def vendorSpecificConfig(self) -> DistributedVirtualPort.VendorSpecificConfig: ...
        @vendorSpecificConfig.setter
        def vendorSpecificConfig(self, value: DistributedVirtualPort.VendorSpecificConfig):
            self._vendorSpecificConfig = value
        @property
        def networkResourcePoolKey(self) -> vim.StringPolicy: ...
        @networkResourcePoolKey.setter
        def networkResourcePoolKey(self, value: vim.StringPolicy):
            self._networkResourcePoolKey = value
        @property
        def filterPolicy(self) -> DistributedVirtualPort.FilterPolicy: ...
        @filterPolicy.setter
        def filterPolicy(self, value: DistributedVirtualPort.FilterPolicy):
            self._filterPolicy = value


    class State(vmodl.DynamicData):
        @property
        def runtimeInfo(self) -> DistributedVirtualPort.RuntimeInfo: ...
        @runtimeInfo.setter
        def runtimeInfo(self, value: DistributedVirtualPort.RuntimeInfo):
            self._runtimeInfo = value
        @property
        def stats(self) -> PortStatistics: ...
        @stats.setter
        def stats(self, value: PortStatistics):
            self._stats = value
        @property
        def vendorSpecificState(self) -> List[KeyedOpaqueBlob]: ...
        @vendorSpecificState.setter
        def vendorSpecificState(self, value: List[KeyedOpaqueBlob]):
            self._vendorSpecificState = value


    class TrafficFilterConfig(DistributedVirtualPort.FilterConfig):
        @property
        def trafficRuleset(self) -> TrafficRuleset: ...
        @trafficRuleset.setter
        def trafficRuleset(self, value: TrafficRuleset):
            self._trafficRuleset = value


    class TrafficFilterConfigSpec(DistributedVirtualPort.TrafficFilterConfig):
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value


    class TrafficShapingPolicy(vim.InheritablePolicy):
        @property
        def enabled(self) -> vim.BoolPolicy: ...
        @enabled.setter
        def enabled(self, value: vim.BoolPolicy):
            self._enabled = value
        @property
        def averageBandwidth(self) -> vim.LongPolicy: ...
        @averageBandwidth.setter
        def averageBandwidth(self, value: vim.LongPolicy):
            self._averageBandwidth = value
        @property
        def peakBandwidth(self) -> vim.LongPolicy: ...
        @peakBandwidth.setter
        def peakBandwidth(self, value: vim.LongPolicy):
            self._peakBandwidth = value
        @property
        def burstSize(self) -> vim.LongPolicy: ...
        @burstSize.setter
        def burstSize(self, value: vim.LongPolicy):
            self._burstSize = value


    class VendorSpecificConfig(vim.InheritablePolicy):
        @property
        def keyValue(self) -> List[KeyedOpaqueBlob]: ...
        @keyValue.setter
        def keyValue(self, value: List[KeyedOpaqueBlob]):
            self._keyValue = value


    class FilterOnFailure(Enum):
        failOpen = "failOpen"
        failClosed = "failClosed"


class DistributedVirtualPortgroupInfo(vmodl.DynamicData):
    @property
    def switchName(self) -> str: ...
    @switchName.setter
    def switchName(self, value: str):
        self._switchName = value
    @property
    def switchUuid(self) -> str: ...
    @switchUuid.setter
    def switchUuid(self, value: str):
        self._switchUuid = value
    @property
    def portgroupName(self) -> str: ...
    @portgroupName.setter
    def portgroupName(self, value: str):
        self._portgroupName = value
    @property
    def portgroupKey(self) -> str: ...
    @portgroupKey.setter
    def portgroupKey(self, value: str):
        self._portgroupKey = value
    @property
    def portgroupType(self) -> str: ...
    @portgroupType.setter
    def portgroupType(self, value: str):
        self._portgroupType = value
    @property
    def uplinkPortgroup(self) -> bool: ...
    @uplinkPortgroup.setter
    def uplinkPortgroup(self, value: bool):
        self._uplinkPortgroup = value
    @property
    def portgroup(self) -> DistributedVirtualPortgroup: ...
    @portgroup.setter
    def portgroup(self, value: DistributedVirtualPortgroup):
        self._portgroup = value
    @property
    def networkReservationSupported(self) -> bool: ...
    @networkReservationSupported.setter
    def networkReservationSupported(self, value: bool):
        self._networkReservationSupported = value
    @property
    def backingType(self) -> str: ...
    @backingType.setter
    def backingType(self, value: str):
        self._backingType = value
    @property
    def logicalSwitchUuid(self) -> str: ...
    @logicalSwitchUuid.setter
    def logicalSwitchUuid(self, value: str):
        self._logicalSwitchUuid = value
    @property
    def segmentId(self) -> str: ...
    @segmentId.setter
    def segmentId(self, value: str):
        self._segmentId = value


class DistributedVirtualPortgroupSelection(vim.SelectionSet):
    @property
    def dvsUuid(self) -> str: ...
    @dvsUuid.setter
    def dvsUuid(self, value: str):
        self._dvsUuid = value
    @property
    def portgroupKey(self) -> List[str]: ...
    @portgroupKey.setter
    def portgroupKey(self, value: List[str]):
        self._portgroupKey = value


class DistributedVirtualSwitchInfo(vmodl.DynamicData):
    @property
    def switchName(self) -> str: ...
    @switchName.setter
    def switchName(self, value: str):
        self._switchName = value
    @property
    def switchUuid(self) -> str: ...
    @switchUuid.setter
    def switchUuid(self, value: str):
        self._switchUuid = value
    @property
    def distributedVirtualSwitch(self) -> vim.DistributedVirtualSwitch: ...
    @distributedVirtualSwitch.setter
    def distributedVirtualSwitch(self, value: vim.DistributedVirtualSwitch):
        self._distributedVirtualSwitch = value
    @property
    def networkReservationSupported(self) -> bool: ...
    @networkReservationSupported.setter
    def networkReservationSupported(self, value: bool):
        self._networkReservationSupported = value


class DistributedVirtualSwitchSelection(vim.SelectionSet):
    @property
    def dvsUuid(self) -> str: ...
    @dvsUuid.setter
    def dvsUuid(self, value: str):
        self._dvsUuid = value


class EntityBackup(vmodl.DynamicData):


    class Config(vmodl.DynamicData):
        @property
        def entityType(self) -> str: ...
        @entityType.setter
        def entityType(self, value: str):
            self._entityType = value
        @property
        def configBlob(self) -> binary: ...
        @configBlob.setter
        def configBlob(self, value: binary):
            self._configBlob = value
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def container(self) -> vim.ManagedEntity: ...
        @container.setter
        def container(self, value: vim.ManagedEntity):
            self._container = value
        @property
        def configVersion(self) -> str: ...
        @configVersion.setter
        def configVersion(self, value: str):
            self._configVersion = value


    class EntityType(Enum):
        distributedVirtualSwitch = "distributedVirtualSwitch"
        distributedVirtualPortgroup = "distributedVirtualPortgroup"


    class ImportType(Enum):
        createEntityWithNewIdentifier = "createEntityWithNewIdentifier"
        createEntityWithOriginalIdentifier = "createEntityWithOriginalIdentifier"
        applyToEntitySpecified = "applyToEntitySpecified"


class HostMember(vmodl.DynamicData):
    @property
    def runtimeState(self) -> HostMember.RuntimeState: ...
    @runtimeState.setter
    def runtimeState(self, value: HostMember.RuntimeState):
        self._runtimeState = value
    @property
    def config(self) -> HostMember.ConfigInfo: ...
    @config.setter
    def config(self, value: HostMember.ConfigInfo):
        self._config = value
    @property
    def productInfo(self) -> ProductSpec: ...
    @productInfo.setter
    def productInfo(self, value: ProductSpec):
        self._productInfo = value
    @property
    def uplinkPortKey(self) -> List[str]: ...
    @uplinkPortKey.setter
    def uplinkPortKey(self, value: List[str]):
        self._uplinkPortKey = value
    @property
    def status(self) -> str: ...
    @status.setter
    def status(self, value: str):
        self._status = value
    @property
    def statusDetail(self) -> str: ...
    @statusDetail.setter
    def statusDetail(self, value: str):
        self._statusDetail = value


    class Backing(vmodl.DynamicData): ...


    class ConfigInfo(vmodl.DynamicData):
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def maxProxySwitchPorts(self) -> int: ...
        @maxProxySwitchPorts.setter
        def maxProxySwitchPorts(self, value: int):
            self._maxProxySwitchPorts = value
        @property
        def vendorSpecificConfig(self) -> List[KeyedOpaqueBlob]: ...
        @vendorSpecificConfig.setter
        def vendorSpecificConfig(self, value: List[KeyedOpaqueBlob]):
            self._vendorSpecificConfig = value
        @property
        def backing(self) -> HostMember.Backing: ...
        @backing.setter
        def backing(self, value: HostMember.Backing):
            self._backing = value
        @property
        def nsxSwitch(self) -> bool: ...
        @nsxSwitch.setter
        def nsxSwitch(self, value: bool):
            self._nsxSwitch = value
        @property
        def ensEnabled(self) -> bool: ...
        @ensEnabled.setter
        def ensEnabled(self, value: bool):
            self._ensEnabled = value
        @property
        def ensInterruptEnabled(self) -> bool: ...
        @ensInterruptEnabled.setter
        def ensInterruptEnabled(self, value: bool):
            self._ensInterruptEnabled = value
        @property
        def transportZones(self) -> List[HostMember.TransportZoneInfo]: ...
        @transportZones.setter
        def transportZones(self, value: List[HostMember.TransportZoneInfo]):
            self._transportZones = value
        @property
        def nsxtUsedUplinkNames(self) -> List[str]: ...
        @nsxtUsedUplinkNames.setter
        def nsxtUsedUplinkNames(self, value: List[str]):
            self._nsxtUsedUplinkNames = value
        @property
        def networkOffloadingEnabled(self) -> bool: ...
        @networkOffloadingEnabled.setter
        def networkOffloadingEnabled(self, value: bool):
            self._networkOffloadingEnabled = value


    class ConfigSpec(vmodl.DynamicData):
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def backing(self) -> HostMember.Backing: ...
        @backing.setter
        def backing(self, value: HostMember.Backing):
            self._backing = value
        @property
        def maxProxySwitchPorts(self) -> int: ...
        @maxProxySwitchPorts.setter
        def maxProxySwitchPorts(self, value: int):
            self._maxProxySwitchPorts = value
        @property
        def vendorSpecificConfig(self) -> List[KeyedOpaqueBlob]: ...
        @vendorSpecificConfig.setter
        def vendorSpecificConfig(self, value: List[KeyedOpaqueBlob]):
            self._vendorSpecificConfig = value


    class HealthCheckResult(vmodl.DynamicData):
        @property
        def summary(self) -> str: ...
        @summary.setter
        def summary(self, value: str):
            self._summary = value


    class PnicBacking(HostMember.Backing):
        @property
        def pnicSpec(self) -> List[HostMember.PnicSpec]: ...
        @pnicSpec.setter
        def pnicSpec(self, value: List[HostMember.PnicSpec]):
            self._pnicSpec = value


    class PnicSpec(vmodl.DynamicData):
        @property
        def pnicDevice(self) -> str: ...
        @pnicDevice.setter
        def pnicDevice(self, value: str):
            self._pnicDevice = value
        @property
        def uplinkPortKey(self) -> str: ...
        @uplinkPortKey.setter
        def uplinkPortKey(self, value: str):
            self._uplinkPortKey = value
        @property
        def uplinkPortgroupKey(self) -> str: ...
        @uplinkPortgroupKey.setter
        def uplinkPortgroupKey(self, value: str):
            self._uplinkPortgroupKey = value
        @property
        def connectionCookie(self) -> int: ...
        @connectionCookie.setter
        def connectionCookie(self, value: int):
            self._connectionCookie = value


    class RuntimeInfo(vmodl.DynamicData):
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def status(self) -> str: ...
        @status.setter
        def status(self, value: str):
            self._status = value
        @property
        def statusDetail(self) -> str: ...
        @statusDetail.setter
        def statusDetail(self, value: str):
            self._statusDetail = value
        @property
        def nsxtStatus(self) -> str: ...
        @nsxtStatus.setter
        def nsxtStatus(self, value: str):
            self._nsxtStatus = value
        @property
        def nsxtStatusDetail(self) -> str: ...
        @nsxtStatusDetail.setter
        def nsxtStatusDetail(self, value: str):
            self._nsxtStatusDetail = value
        @property
        def healthCheckResult(self) -> List[HostMember.HealthCheckResult]: ...
        @healthCheckResult.setter
        def healthCheckResult(self, value: List[HostMember.HealthCheckResult]):
            self._healthCheckResult = value


    class RuntimeState(vmodl.DynamicData):
        @property
        def currentMaxProxySwitchPorts(self) -> int: ...
        @currentMaxProxySwitchPorts.setter
        def currentMaxProxySwitchPorts(self, value: int):
            self._currentMaxProxySwitchPorts = value


    class TransportZoneInfo(vmodl.DynamicData):
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value


    class UplinkHealthCheckResult(HostMember.HealthCheckResult):
        @property
        def uplinkPortKey(self) -> str: ...
        @uplinkPortKey.setter
        def uplinkPortKey(self, value: str):
            self._uplinkPortKey = value


    class HostComponentState(Enum):
        up = "up"
        pending = "pending"
        outOfSync = "outOfSync"
        warning = "warning"
        disconnected = "disconnected"
        down = "down"


    class TransportZoneType(Enum):
        vlan = "vlan"
        overlay = "overlay"


class HostProductSpec(vmodl.DynamicData):
    @property
    def productLineId(self) -> str: ...
    @productLineId.setter
    def productLineId(self, value: str):
        self._productLineId = value
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value


class KeyedOpaqueBlob(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def opaqueData(self) -> str: ...
    @opaqueData.setter
    def opaqueData(self, value: str):
        self._opaqueData = value


class NetworkOffloadSpec(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def types(self) -> List[str]: ...
    @types.setter
    def types(self, value: List[str]):
        self._types = value


class NetworkResourcePool(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
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
    def configVersion(self) -> str: ...
    @configVersion.setter
    def configVersion(self, value: str):
        self._configVersion = value
    @property
    def allocationInfo(self) -> NetworkResourcePool.AllocationInfo: ...
    @allocationInfo.setter
    def allocationInfo(self, value: NetworkResourcePool.AllocationInfo):
        self._allocationInfo = value


    class AllocationInfo(vmodl.DynamicData):
        @property
        def limit(self) -> long: ...
        @limit.setter
        def limit(self, value: long):
            self._limit = value
        @property
        def shares(self) -> vim.SharesInfo: ...
        @shares.setter
        def shares(self, value: vim.SharesInfo):
            self._shares = value
        @property
        def priorityTag(self) -> int: ...
        @priorityTag.setter
        def priorityTag(self, value: int):
            self._priorityTag = value


    class ConfigSpec(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def configVersion(self) -> str: ...
        @configVersion.setter
        def configVersion(self, value: str):
            self._configVersion = value
        @property
        def allocationInfo(self) -> NetworkResourcePool.AllocationInfo: ...
        @allocationInfo.setter
        def allocationInfo(self, value: NetworkResourcePool.AllocationInfo):
            self._allocationInfo = value
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


class PortConnectee(vmodl.DynamicData):
    @property
    def connectedEntity(self) -> vim.ManagedEntity: ...
    @connectedEntity.setter
    def connectedEntity(self, value: vim.ManagedEntity):
        self._connectedEntity = value
    @property
    def nicKey(self) -> str: ...
    @nicKey.setter
    def nicKey(self, value: str):
        self._nicKey = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def addressHint(self) -> str: ...
    @addressHint.setter
    def addressHint(self, value: str):
        self._addressHint = value


    class ConnecteeType(Enum):
        pnic = "pnic"
        vmVnic = "vmVnic"
        hostConsoleVnic = "hostConsoleVnic"
        hostVmkVnic = "hostVmkVnic"
        systemCrxVnic = "systemCrxVnic"


class PortConnection(vmodl.DynamicData):
    @property
    def switchUuid(self) -> str: ...
    @switchUuid.setter
    def switchUuid(self, value: str):
        self._switchUuid = value
    @property
    def portgroupKey(self) -> str: ...
    @portgroupKey.setter
    def portgroupKey(self, value: str):
        self._portgroupKey = value
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value
    @property
    def connectionCookie(self) -> int: ...
    @connectionCookie.setter
    def connectionCookie(self, value: int):
        self._connectionCookie = value


class PortCriteria(vmodl.DynamicData):
    @property
    def connected(self) -> bool: ...
    @connected.setter
    def connected(self, value: bool):
        self._connected = value
    @property
    def active(self) -> bool: ...
    @active.setter
    def active(self, value: bool):
        self._active = value
    @property
    def uplinkPort(self) -> bool: ...
    @uplinkPort.setter
    def uplinkPort(self, value: bool):
        self._uplinkPort = value
    @property
    def nsxPort(self) -> bool: ...
    @nsxPort.setter
    def nsxPort(self, value: bool):
        self._nsxPort = value
    @property
    def scope(self) -> vim.ManagedEntity: ...
    @scope.setter
    def scope(self, value: vim.ManagedEntity):
        self._scope = value
    @property
    def portgroupKey(self) -> List[str]: ...
    @portgroupKey.setter
    def portgroupKey(self, value: List[str]):
        self._portgroupKey = value
    @property
    def inside(self) -> bool: ...
    @inside.setter
    def inside(self, value: bool):
        self._inside = value
    @property
    def portKey(self) -> List[str]: ...
    @portKey.setter
    def portKey(self, value: List[str]):
        self._portKey = value
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @host.setter
    def host(self, value: List[vim.HostSystem]):
        self._host = value


class PortStatistics(vmodl.DynamicData):
    @property
    def packetsInMulticast(self) -> long: ...
    @packetsInMulticast.setter
    def packetsInMulticast(self, value: long):
        self._packetsInMulticast = value
    @property
    def packetsOutMulticast(self) -> long: ...
    @packetsOutMulticast.setter
    def packetsOutMulticast(self, value: long):
        self._packetsOutMulticast = value
    @property
    def bytesInMulticast(self) -> long: ...
    @bytesInMulticast.setter
    def bytesInMulticast(self, value: long):
        self._bytesInMulticast = value
    @property
    def bytesOutMulticast(self) -> long: ...
    @bytesOutMulticast.setter
    def bytesOutMulticast(self, value: long):
        self._bytesOutMulticast = value
    @property
    def packetsInUnicast(self) -> long: ...
    @packetsInUnicast.setter
    def packetsInUnicast(self, value: long):
        self._packetsInUnicast = value
    @property
    def packetsOutUnicast(self) -> long: ...
    @packetsOutUnicast.setter
    def packetsOutUnicast(self, value: long):
        self._packetsOutUnicast = value
    @property
    def bytesInUnicast(self) -> long: ...
    @bytesInUnicast.setter
    def bytesInUnicast(self, value: long):
        self._bytesInUnicast = value
    @property
    def bytesOutUnicast(self) -> long: ...
    @bytesOutUnicast.setter
    def bytesOutUnicast(self, value: long):
        self._bytesOutUnicast = value
    @property
    def packetsInBroadcast(self) -> long: ...
    @packetsInBroadcast.setter
    def packetsInBroadcast(self, value: long):
        self._packetsInBroadcast = value
    @property
    def packetsOutBroadcast(self) -> long: ...
    @packetsOutBroadcast.setter
    def packetsOutBroadcast(self, value: long):
        self._packetsOutBroadcast = value
    @property
    def bytesInBroadcast(self) -> long: ...
    @bytesInBroadcast.setter
    def bytesInBroadcast(self, value: long):
        self._bytesInBroadcast = value
    @property
    def bytesOutBroadcast(self) -> long: ...
    @bytesOutBroadcast.setter
    def bytesOutBroadcast(self, value: long):
        self._bytesOutBroadcast = value
    @property
    def packetsInDropped(self) -> long: ...
    @packetsInDropped.setter
    def packetsInDropped(self, value: long):
        self._packetsInDropped = value
    @property
    def packetsOutDropped(self) -> long: ...
    @packetsOutDropped.setter
    def packetsOutDropped(self, value: long):
        self._packetsOutDropped = value
    @property
    def packetsInException(self) -> long: ...
    @packetsInException.setter
    def packetsInException(self, value: long):
        self._packetsInException = value
    @property
    def packetsOutException(self) -> long: ...
    @packetsOutException.setter
    def packetsOutException(self, value: long):
        self._packetsOutException = value
    @property
    def bytesInFromPnic(self) -> long: ...
    @bytesInFromPnic.setter
    def bytesInFromPnic(self, value: long):
        self._bytesInFromPnic = value
    @property
    def bytesOutToPnic(self) -> long: ...
    @bytesOutToPnic.setter
    def bytesOutToPnic(self, value: long):
        self._bytesOutToPnic = value


class ProductSpec(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def vendor(self) -> str: ...
    @vendor.setter
    def vendor(self, value: str):
        self._vendor = value
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value
    @property
    def build(self) -> str: ...
    @build.setter
    def build(self, value: str):
        self._build = value
    @property
    def forwardingClass(self) -> str: ...
    @forwardingClass.setter
    def forwardingClass(self, value: str):
        self._forwardingClass = value
    @property
    def bundleId(self) -> str: ...
    @bundleId.setter
    def bundleId(self, value: str):
        self._bundleId = value
    @property
    def bundleUrl(self) -> str: ...
    @bundleUrl.setter
    def bundleUrl(self, value: str):
        self._bundleUrl = value


class TrafficRule(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def sequence(self) -> int: ...
    @sequence.setter
    def sequence(self, value: int):
        self._sequence = value
    @property
    def qualifier(self) -> List[TrafficRule.Qualifier]: ...
    @qualifier.setter
    def qualifier(self, value: List[TrafficRule.Qualifier]):
        self._qualifier = value
    @property
    def action(self) -> TrafficRule.Action: ...
    @action.setter
    def action(self, value: TrafficRule.Action):
        self._action = value
    @property
    def direction(self) -> str: ...
    @direction.setter
    def direction(self, value: str):
        self._direction = value


    class AcceptAction(TrafficRule.Action): ...


    class Action(vmodl.DynamicData): ...


    class CopyAction(TrafficRule.Action): ...


    class DropAction(TrafficRule.Action): ...


    class GreAction(TrafficRule.Action):
        @property
        def encapsulationIp(self) -> vim.SingleIp: ...
        @encapsulationIp.setter
        def encapsulationIp(self, value: vim.SingleIp):
            self._encapsulationIp = value


    class IpPort(vim.NegatableExpression): ...


    class IpPortRange(TrafficRule.IpPort):
        @property
        def startPortNumber(self) -> int: ...
        @startPortNumber.setter
        def startPortNumber(self, value: int):
            self._startPortNumber = value
        @property
        def endPortNumber(self) -> int: ...
        @endPortNumber.setter
        def endPortNumber(self, value: int):
            self._endPortNumber = value


    class IpQualifier(TrafficRule.Qualifier):
        @property
        def sourceAddress(self) -> vim.IpAddress: ...
        @sourceAddress.setter
        def sourceAddress(self, value: vim.IpAddress):
            self._sourceAddress = value
        @property
        def destinationAddress(self) -> vim.IpAddress: ...
        @destinationAddress.setter
        def destinationAddress(self, value: vim.IpAddress):
            self._destinationAddress = value
        @property
        def protocol(self) -> vim.IntExpression: ...
        @protocol.setter
        def protocol(self, value: vim.IntExpression):
            self._protocol = value
        @property
        def sourceIpPort(self) -> TrafficRule.IpPort: ...
        @sourceIpPort.setter
        def sourceIpPort(self, value: TrafficRule.IpPort):
            self._sourceIpPort = value
        @property
        def destinationIpPort(self) -> TrafficRule.IpPort: ...
        @destinationIpPort.setter
        def destinationIpPort(self, value: TrafficRule.IpPort):
            self._destinationIpPort = value
        @property
        def tcpFlags(self) -> vim.IntExpression: ...
        @tcpFlags.setter
        def tcpFlags(self, value: vim.IntExpression):
            self._tcpFlags = value


    class LogAction(TrafficRule.Action): ...


    class MacQualifier(TrafficRule.Qualifier):
        @property
        def sourceAddress(self) -> vim.MacAddress: ...
        @sourceAddress.setter
        def sourceAddress(self, value: vim.MacAddress):
            self._sourceAddress = value
        @property
        def destinationAddress(self) -> vim.MacAddress: ...
        @destinationAddress.setter
        def destinationAddress(self, value: vim.MacAddress):
            self._destinationAddress = value
        @property
        def protocol(self) -> vim.IntExpression: ...
        @protocol.setter
        def protocol(self, value: vim.IntExpression):
            self._protocol = value
        @property
        def vlanId(self) -> vim.IntExpression: ...
        @vlanId.setter
        def vlanId(self, value: vim.IntExpression):
            self._vlanId = value


    class MacRewriteAction(TrafficRule.Action):
        @property
        def rewriteMac(self) -> str: ...
        @rewriteMac.setter
        def rewriteMac(self, value: str):
            self._rewriteMac = value


    class PuntAction(TrafficRule.Action): ...


    class Qualifier(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value


    class RateLimitAction(TrafficRule.Action):
        @property
        def packetsPerSecond(self) -> int: ...
        @packetsPerSecond.setter
        def packetsPerSecond(self, value: int):
            self._packetsPerSecond = value


    class SingleIpPort(TrafficRule.IpPort):
        @property
        def portNumber(self) -> int: ...
        @portNumber.setter
        def portNumber(self, value: int):
            self._portNumber = value


    class SystemTrafficQualifier(TrafficRule.Qualifier):
        @property
        def typeOfSystemTraffic(self) -> vim.StringExpression: ...
        @typeOfSystemTraffic.setter
        def typeOfSystemTraffic(self, value: vim.StringExpression):
            self._typeOfSystemTraffic = value


    class UpdateTagAction(TrafficRule.Action):
        @property
        def qosTag(self) -> int: ...
        @qosTag.setter
        def qosTag(self, value: int):
            self._qosTag = value
        @property
        def dscpTag(self) -> int: ...
        @dscpTag.setter
        def dscpTag(self, value: int):
            self._dscpTag = value


    class RuleDirectionType(Enum):
        incomingPackets = "incomingPackets"
        outgoingPackets = "outgoingPackets"
        both = "both"


class TrafficRuleset(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def precedence(self) -> int: ...
    @precedence.setter
    def precedence(self, value: int):
        self._precedence = value
    @property
    def rules(self) -> List[TrafficRule]: ...
    @rules.setter
    def rules(self, value: List[TrafficRule]):
        self._rules = value


class VmVnicNetworkResourcePool(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
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
    def configVersion(self) -> str: ...
    @configVersion.setter
    def configVersion(self, value: str):
        self._configVersion = value
    @property
    def allocationInfo(self) -> VmVnicNetworkResourcePool.ResourceAllocation: ...
    @allocationInfo.setter
    def allocationInfo(self, value: VmVnicNetworkResourcePool.ResourceAllocation):
        self._allocationInfo = value


    class ConfigSpec(vmodl.DynamicData):
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def configVersion(self) -> str: ...
        @configVersion.setter
        def configVersion(self, value: str):
            self._configVersion = value
        @property
        def allocationInfo(self) -> VmVnicNetworkResourcePool.ResourceAllocation: ...
        @allocationInfo.setter
        def allocationInfo(self, value: VmVnicNetworkResourcePool.ResourceAllocation):
            self._allocationInfo = value
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


    class ResourceAllocation(vmodl.DynamicData):
        @property
        def reservationQuota(self) -> long: ...
        @reservationQuota.setter
        def reservationQuota(self, value: long):
            self._reservationQuota = value


    class RuntimeInfo(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def capacity(self) -> int: ...
        @capacity.setter
        def capacity(self, value: int):
            self._capacity = value
        @property
        def usage(self) -> int: ...
        @usage.setter
        def usage(self, value: int):
            self._usage = value
        @property
        def available(self) -> int: ...
        @available.setter
        def available(self, value: int):
            self._available = value
        @property
        def status(self) -> str: ...
        @status.setter
        def status(self, value: str):
            self._status = value
        @property
        def allocatedResource(self) -> List[VmVnicNetworkResourcePool.VnicAllocatedResource]: ...
        @allocatedResource.setter
        def allocatedResource(self, value: List[VmVnicNetworkResourcePool.VnicAllocatedResource]):
            self._allocatedResource = value


    class VnicAllocatedResource(vmodl.DynamicData):
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @vm.setter
        def vm(self, value: vim.VirtualMachine):
            self._vm = value
        @property
        def vnicKey(self) -> str: ...
        @vnicKey.setter
        def vnicKey(self, value: str):
            self._vnicKey = value
        @property
        def reservation(self) -> long: ...
        @reservation.setter
        def reservation(self, value: long):
            self._reservation = value


class HostDistributedVirtualSwitchManager():


    class DVSConfigSpec():


        class SwitchMode(Enum):
            normal = "normal"
            mux = "mux"