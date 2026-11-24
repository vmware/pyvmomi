# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.fault
import pyVmomi.vim.host



class DistributedVirtualPort(pyVmomi.vmodl.DynamicData):
   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      operation: str
      key: _typing.Optional[str] = None
      name: _typing.Optional[str] = None
      scope: list[pyVmomi.vim.ManagedEntity] = []
      description: _typing.Optional[str] = None
      setting: _typing.Optional[Setting] = None
      configVersion: _typing.Optional[str] = None

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      name: _typing.Optional[str] = None
      scope: list[pyVmomi.vim.ManagedEntity] = []
      description: _typing.Optional[str] = None
      setting: _typing.Optional[Setting] = None
      configVersion: str

   class TrafficShapingPolicy(pyVmomi.vim.InheritablePolicy):
      enabled: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      averageBandwidth: _typing.Optional[pyVmomi.vim.LongPolicy] = None
      peakBandwidth: _typing.Optional[pyVmomi.vim.LongPolicy] = None
      burstSize: _typing.Optional[pyVmomi.vim.LongPolicy] = None

   class HostLocalPortInfo(pyVmomi.vmodl.DynamicData):
      switchUuid: str
      portKey: str
      setting: Setting
      vnic: str

   class VendorSpecificConfig(pyVmomi.vim.InheritablePolicy):
      keyValue: list[KeyedOpaqueBlob] = []

   class FilterParameter(pyVmomi.vmodl.DynamicData):
      parameters: list[str] = []

   class FilterOnFailure(pyVmomi.VmomiSupport.Enum):
      failOpen: _typing.ClassVar['FilterOnFailure'] = 'failOpen'
      failClosed: _typing.ClassVar['FilterOnFailure'] = 'failClosed'

   class FilterConfig(pyVmomi.vim.InheritablePolicy):
      key: _typing.Optional[str] = None
      agentName: _typing.Optional[str] = None
      slotNumber: _typing.Optional[str] = None
      parameters: _typing.Optional[FilterParameter] = None
      onFailure: _typing.Optional[str] = None

   class TrafficFilterConfig(FilterConfig):
      trafficRuleset: _typing.Optional[TrafficRuleset] = None

   class FilterConfigSpec(FilterConfig):
      operation: str

   class TrafficFilterConfigSpec(TrafficFilterConfig):
      operation: str

   class FilterPolicy(pyVmomi.vim.InheritablePolicy):
      filterConfig: list[FilterConfig] = []

   class Setting(pyVmomi.vmodl.DynamicData):
      blocked: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      vmDirectPathGen2Allowed: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      inShapingPolicy: _typing.Optional[TrafficShapingPolicy] = None
      outShapingPolicy: _typing.Optional[TrafficShapingPolicy] = None
      vendorSpecificConfig: _typing.Optional[VendorSpecificConfig] = None
      networkResourcePoolKey: _typing.Optional[pyVmomi.vim.StringPolicy] = None
      filterPolicy: _typing.Optional[FilterPolicy] = None

   class RuntimeInfo(pyVmomi.vmodl.DynamicData):
      class VmDirectPathGen2InactiveReasonNetwork(pyVmomi.VmomiSupport.Enum):
         portNptIncompatibleDvs: _typing.ClassVar['VmDirectPathGen2InactiveReasonNetwork'] = 'portNptIncompatibleDvs'
         portNptNoCompatibleNics: _typing.ClassVar['VmDirectPathGen2InactiveReasonNetwork'] = 'portNptNoCompatibleNics'
         portNptNoVirtualFunctionsAvailable: _typing.ClassVar['VmDirectPathGen2InactiveReasonNetwork'] = 'portNptNoVirtualFunctionsAvailable'
         portNptDisabledForPort: _typing.ClassVar['VmDirectPathGen2InactiveReasonNetwork'] = 'portNptDisabledForPort'

      class VmDirectPathGen2InactiveReasonOther(pyVmomi.VmomiSupport.Enum):
         portNptIncompatibleHost: _typing.ClassVar['VmDirectPathGen2InactiveReasonOther'] = 'portNptIncompatibleHost'
         portNptIncompatibleConnectee: _typing.ClassVar['VmDirectPathGen2InactiveReasonOther'] = 'portNptIncompatibleConnectee'

      linkUp: bool
      blocked: bool
      vlanIds: list[pyVmomi.vim.NumericRange] = []
      trunkingMode: _typing.Optional[bool] = None
      mtu: _typing.Optional[int] = None
      linkPeer: _typing.Optional[str] = None
      macAddress: _typing.Optional[str] = None
      statusDetail: _typing.Optional[str] = None
      vmDirectPathGen2Active: _typing.Optional[bool] = None
      vmDirectPathGen2InactiveReasonNetwork: list[str] = []
      vmDirectPathGen2InactiveReasonOther: list[str] = []
      vmDirectPathGen2InactiveReasonExtended: _typing.Optional[str] = None

   class State(pyVmomi.vmodl.DynamicData):
      runtimeInfo: _typing.Optional[RuntimeInfo] = None
      stats: PortStatistics
      vendorSpecificState: list[KeyedOpaqueBlob] = []

   key: str
   config: ConfigInfo
   dvsUuid: str
   portgroupKey: _typing.Optional[str] = None
   proxyHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
   connectee: _typing.Optional[PortConnectee] = None
   conflict: bool
   conflictPortKey: _typing.Optional[str] = None
   state: _typing.Optional[State] = None
   connectionCookie: _typing.Optional[int] = None
   lastStatusChange: _datetime.datetime
   hostLocalPort: _typing.Optional[bool] = None
   externalId: _typing.Optional[str] = None
   segmentPortId: _typing.Optional[str] = None


class DistributedVirtualPortgroup(pyVmomi.vim.Network):
   class PortgroupType(pyVmomi.VmomiSupport.Enum):
      earlyBinding: _typing.ClassVar['PortgroupType'] = 'earlyBinding'
      lateBinding: _typing.ClassVar['PortgroupType'] = 'lateBinding'
      ephemeral: _typing.ClassVar['PortgroupType'] = 'ephemeral'

   class BackingType(pyVmomi.VmomiSupport.Enum):
      standard: _typing.ClassVar['BackingType'] = 'standard'
      nsx: _typing.ClassVar['BackingType'] = 'nsx'

   class PortgroupPolicy(pyVmomi.vmodl.DynamicData):
      blockOverrideAllowed: bool
      shapingOverrideAllowed: bool
      vendorConfigOverrideAllowed: bool
      livePortMovingAllowed: bool
      portConfigResetAtDisconnect: bool
      networkResourcePoolOverrideAllowed: _typing.Optional[bool] = None
      trafficFilterOverrideAllowed: _typing.Optional[bool] = None

   class MetaTagName(pyVmomi.VmomiSupport.Enum):
      dvsName: _typing.ClassVar['MetaTagName'] = 'dvsName'
      portgroupName: _typing.ClassVar['MetaTagName'] = 'portgroupName'
      portIndex: _typing.ClassVar['MetaTagName'] = 'portIndex'

   class SubnetAddressInfo(pyVmomi.vmodl.DynamicData):
      cidr: list[str] = []

   class NsxConfig(pyVmomi.vmodl.DynamicData):
      vlanIdExtended: _typing.Optional[int] = None
      subnetAddresses: _typing.Optional[SubnetAddressInfo] = None
      spanIds: list[str] = []

   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      configVersion: _typing.Optional[str] = None
      name: _typing.Optional[str] = None
      numPorts: _typing.Optional[int] = None
      portNameFormat: _typing.Optional[str] = None
      defaultPortConfig: _typing.Optional[DistributedVirtualPort.Setting] = None
      description: _typing.Optional[str] = None
      type: _typing.Optional[str] = None
      backingType: _typing.Optional[str] = None
      scope: list[pyVmomi.vim.ManagedEntity] = []
      policy: _typing.Optional[PortgroupPolicy] = None
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      autoExpand: _typing.Optional[bool] = None
      vmVnicNetworkResourcePoolKey: _typing.Optional[str] = None
      transportZoneUuid: _typing.Optional[str] = None
      transportZoneName: _typing.Optional[str] = None
      logicalSwitchUuid: _typing.Optional[str] = None
      segmentId: _typing.Optional[str] = None
      subnetId: _typing.Optional[str] = None
      nsxConfig: _typing.Optional[NsxConfig] = None

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      key: str
      name: str
      numPorts: int
      distributedVirtualSwitch: _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch] = None
      defaultPortConfig: _typing.Optional[DistributedVirtualPort.Setting] = None
      description: _typing.Optional[str] = None
      type: str
      backingType: _typing.Optional[str] = None
      policy: PortgroupPolicy
      portNameFormat: _typing.Optional[str] = None
      scope: list[pyVmomi.vim.ManagedEntity] = []
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      configVersion: _typing.Optional[str] = None
      autoExpand: _typing.Optional[bool] = None
      vmVnicNetworkResourcePoolKey: _typing.Optional[str] = None
      uplink: _typing.Optional[bool] = None
      transportZoneUuid: _typing.Optional[str] = None
      transportZoneName: _typing.Optional[str] = None
      logicalSwitchUuid: _typing.Optional[str] = None
      segmentId: _typing.Optional[str] = None
      subnetId: _typing.Optional[str] = None
      nsxConfig: _typing.Optional[NsxConfig] = None

   class Problem(pyVmomi.vmodl.DynamicData):
      logicalSwitchUuid: str
      fault: pyVmomi.vmodl.MethodFault

   class NsxPortgroupOperationResult(pyVmomi.vmodl.DynamicData):
      portgroups: list[DistributedVirtualPortgroup] = []
      problems: list[Problem] = []

   @property
   def key(self) -> str: ...
   @property
   def config(self) -> ConfigInfo: ...
   @property
   def portKeys(self) -> list[str]: ...

   def Reconfigure(self, spec: ConfigSpec) -> pyVmomi.vim.Task: ...
   def Rollback(self, entityBackup: _typing.Optional[EntityBackup.Config]) -> pyVmomi.vim.Task: ...


class DistributedVirtualPortgroupInfo(pyVmomi.vmodl.DynamicData):
   switchName: str
   switchUuid: str
   portgroupName: str
   portgroupKey: str
   portgroupType: str
   uplinkPortgroup: bool
   portgroup: DistributedVirtualPortgroup
   networkReservationSupported: _typing.Optional[bool] = None
   backingType: _typing.Optional[str] = None
   logicalSwitchUuid: _typing.Optional[str] = None
   segmentId: _typing.Optional[str] = None
   subnetId: _typing.Optional[str] = None


class DistributedVirtualPortgroupSelection(pyVmomi.vim.SelectionSet):
   dvsUuid: str
   portgroupKey: list[str] = []


class DistributedVirtualSwitchInfo(pyVmomi.vmodl.DynamicData):
   switchName: str
   switchUuid: str
   distributedVirtualSwitch: pyVmomi.vim.DistributedVirtualSwitch
   networkReservationSupported: _typing.Optional[bool] = None


class DistributedVirtualSwitchManager(pyVmomi.VmomiSupport.ManagedObject):
   class PhysicalNicsList(pyVmomi.vmodl.DynamicData):
      host: pyVmomi.vim.HostSystem
      physicalNics: list[pyVmomi.vim.host.PhysicalNic] = []

   class DvsConfigTarget(pyVmomi.vmodl.DynamicData):
      distributedVirtualPortgroup: list[DistributedVirtualPortgroupInfo] = []
      distributedVirtualSwitch: list[DistributedVirtualSwitchInfo] = []

   class CompatibilityResult(pyVmomi.vmodl.DynamicData):
      host: pyVmomi.vim.HostSystem
      error: list[pyVmomi.vmodl.MethodFault] = []

   class HostContainer(pyVmomi.vmodl.DynamicData):
      container: pyVmomi.vim.ManagedEntity
      recursive: bool

   class HostDvsFilterSpec(pyVmomi.vmodl.DynamicData):
      inclusive: bool

   class HostArrayFilter(HostDvsFilterSpec):
      host: list[pyVmomi.vim.HostSystem] = []

   class HostContainerFilter(HostDvsFilterSpec):
      hostContainer: HostContainer

   class HostDvsMembershipFilter(HostDvsFilterSpec):
      distributedVirtualSwitch: pyVmomi.vim.DistributedVirtualSwitch

   class DvsProductSpec(pyVmomi.vmodl.DynamicData):
      newSwitchProductSpec: _typing.Optional[ProductSpec] = None
      distributedVirtualSwitch: _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch] = None

   class ImportResult(pyVmomi.vmodl.DynamicData):
      distributedVirtualSwitch: list[pyVmomi.vim.DistributedVirtualSwitch] = []
      distributedVirtualPortgroup: list[DistributedVirtualPortgroup] = []
      importFault: list[pyVmomi.vim.fault.ImportOperationBulkFault.FaultOnImport] = []

   class SpanInfo(pyVmomi.vmodl.DynamicData):
      ID: str
      clusters: list[pyVmomi.vim.ClusterComputeResource] = []
      exclusive: _typing.Optional[bool] = None

   def QuerySupportedSwitchSpec(self, recommended: _typing.Optional[bool]) -> list[ProductSpec]: ...
   def QuerySupportedNetworkOffloadSpec(self, switchProductSpec: ProductSpec) -> list[NetworkOffloadSpec]: ...
   def QueryCompatibleVmnicsFromHosts(self, hosts: list[pyVmomi.vim.HostSystem], dvs: pyVmomi.vim.DistributedVirtualSwitch) -> list[PhysicalNicsList]: ...
   def QueryCompatibleHostForNewDvs(self, container: pyVmomi.vim.ManagedEntity, recursive: bool, switchProductSpec: _typing.Optional[ProductSpec]) -> list[pyVmomi.vim.HostSystem]: ...
   def QueryCompatibleHostForExistingDvs(self, container: pyVmomi.vim.ManagedEntity, recursive: bool, dvs: pyVmomi.vim.DistributedVirtualSwitch) -> list[pyVmomi.vim.HostSystem]: ...
   def QueryCompatibleHostSpec(self, switchProductSpec: _typing.Optional[ProductSpec]) -> list[HostProductSpec]: ...
   def QueryFeatureCapability(self, switchProductSpec: _typing.Optional[ProductSpec]) -> _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch.FeatureCapability]: ...
   def QuerySwitchByUuid(self, uuid: str) -> _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch]: ...
   def QueryDvsConfigTarget(self, host: _typing.Optional[pyVmomi.vim.HostSystem], dvs: _typing.Optional[pyVmomi.vim.DistributedVirtualSwitch]) -> DvsConfigTarget: ...
   def CheckCompatibility(self, hostContainer: HostContainer, dvsProductSpec: _typing.Optional[DvsProductSpec], hostFilterSpec: list[HostDvsFilterSpec]) -> list[CompatibilityResult]: ...
   def RectifyHost(self, hosts: list[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task: ...
   def ExportEntity(self, selectionSet: list[pyVmomi.vim.SelectionSet]) -> pyVmomi.vim.Task: ...
   def ImportEntity(self, entityBackup: list[EntityBackup.Config], importType: str) -> pyVmomi.vim.Task: ...
   def LookupPortgroup(self, switchUuid: str, portgroupKey: str) -> _typing.Optional[DistributedVirtualPortgroup]: ...
   def GetVpcNetworkSpan(self, spanId: _typing.Optional[str]) -> list[SpanInfo]: ...


class DistributedVirtualSwitchSelection(pyVmomi.vim.SelectionSet):
   dvsUuid: str


class EntityBackup(pyVmomi.vmodl.DynamicData):
   class Config(pyVmomi.vmodl.DynamicData):
      entityType: str
      configBlob: pyVmomi.VmomiSupport.binary
      key: _typing.Optional[str] = None
      name: _typing.Optional[str] = None
      container: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
      configVersion: _typing.Optional[str] = None

   class EntityType(pyVmomi.VmomiSupport.Enum):
      distributedVirtualSwitch: _typing.ClassVar['EntityType'] = 'distributedVirtualSwitch'
      distributedVirtualPortgroup: _typing.ClassVar['EntityType'] = 'distributedVirtualPortgroup'

   class ImportType(pyVmomi.VmomiSupport.Enum):
      createEntityWithNewIdentifier: _typing.ClassVar['ImportType'] = 'createEntityWithNewIdentifier'
      createEntityWithOriginalIdentifier: _typing.ClassVar['ImportType'] = 'createEntityWithOriginalIdentifier'
      applyToEntitySpecified: _typing.ClassVar['ImportType'] = 'applyToEntitySpecified'


class HostMember(pyVmomi.vmodl.DynamicData):
   class HostComponentState(pyVmomi.VmomiSupport.Enum):
      up: _typing.ClassVar['HostComponentState'] = 'up'
      pending: _typing.ClassVar['HostComponentState'] = 'pending'
      outOfSync: _typing.ClassVar['HostComponentState'] = 'outOfSync'
      warning: _typing.ClassVar['HostComponentState'] = 'warning'
      disconnected: _typing.ClassVar['HostComponentState'] = 'disconnected'
      down: _typing.ClassVar['HostComponentState'] = 'down'

   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      operation: str
      host: pyVmomi.vim.HostSystem
      backing: _typing.Optional[Backing] = None
      maxProxySwitchPorts: _typing.Optional[int] = None
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []

   class PnicSpec(pyVmomi.vmodl.DynamicData):
      pnicDevice: str
      uplinkPortKey: _typing.Optional[str] = None
      uplinkPortgroupKey: _typing.Optional[str] = None
      connectionCookie: _typing.Optional[int] = None

   class Backing(pyVmomi.vmodl.DynamicData):
      pass

   class PnicBacking(Backing):
      pnicSpec: list[PnicSpec] = []

   class RuntimeState(pyVmomi.vmodl.DynamicData):
      currentMaxProxySwitchPorts: int

   class TransportZoneType(pyVmomi.VmomiSupport.Enum):
      vlan: _typing.ClassVar['TransportZoneType'] = 'vlan'
      overlay: _typing.ClassVar['TransportZoneType'] = 'overlay'

   class TransportZoneInfo(pyVmomi.vmodl.DynamicData):
      uuid: str
      type: str

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      host: _typing.Optional[pyVmomi.vim.HostSystem] = None
      maxProxySwitchPorts: int
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      backing: Backing
      nsxSwitch: _typing.Optional[bool] = None
      ensEnabled: _typing.Optional[bool] = None
      ensInterruptEnabled: _typing.Optional[bool] = None
      transportZones: list[TransportZoneInfo] = []
      nsxtUsedUplinkNames: list[str] = []
      networkOffloadingEnabled: _typing.Optional[bool] = None
      teplessMode: _typing.Optional[bool] = None

   class HostUplinkState(pyVmomi.vmodl.DynamicData):
      class State(pyVmomi.VmomiSupport.Enum):
         active: _typing.ClassVar['State'] = 'active'
         standby: _typing.ClassVar['State'] = 'standby'

      uplinkName: str
      state: str

   class HostPerfNicOffloadState(pyVmomi.vmodl.DynamicData):
      class Status(pyVmomi.VmomiSupport.Enum):
         SUCCEEDED: _typing.ClassVar['Status'] = 'SUCCEEDED'
         IN_PROGRESS: _typing.ClassVar['Status'] = 'IN_PROGRESS'
         FAILED: _typing.ClassVar['Status'] = 'FAILED'

      enabled: bool
      runtimeStatus: _typing.Optional[str] = None
      statusDescription: _typing.Optional[str] = None

   class RuntimeInfo(pyVmomi.vmodl.DynamicData):
      host: pyVmomi.vim.HostSystem
      status: _typing.Optional[str] = None
      statusDetail: _typing.Optional[str] = None
      nsxtStatus: _typing.Optional[str] = None
      nsxtStatusDetail: _typing.Optional[str] = None
      healthCheckResult: list[HealthCheckResult] = []
      hostUplinkState: list[HostUplinkState] = []
      hostPerfNicOffloadState: _typing.Optional[HostPerfNicOffloadState] = None

   class HealthCheckResult(pyVmomi.vmodl.DynamicData):
      summary: _typing.Optional[str] = None

   class UplinkHealthCheckResult(HealthCheckResult):
      uplinkPortKey: str

   runtimeState: _typing.Optional[RuntimeState] = None
   config: ConfigInfo
   productInfo: _typing.Optional[ProductSpec] = None
   uplinkPortKey: list[str] = []
   status: str
   statusDetail: _typing.Optional[str] = None


class HostProductSpec(pyVmomi.vmodl.DynamicData):
   productLineId: _typing.Optional[str] = None
   version: _typing.Optional[str] = None


class KeyedOpaqueBlob(pyVmomi.vmodl.DynamicData):
   key: str
   opaqueData: str


class NetworkOffloadSpec(pyVmomi.vmodl.DynamicData):
   id: str
   name: _typing.Optional[str] = None
   types: list[str] = []
   dpuCapability: _typing.Optional[VmwareDistributedVirtualSwitch.DpuFeatureCapability] = None


class NetworkResourcePool(pyVmomi.vmodl.DynamicData):
   class AllocationInfo(pyVmomi.vmodl.DynamicData):
      limit: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      shares: _typing.Optional[pyVmomi.vim.SharesInfo] = None
      priorityTag: _typing.Optional[int] = None

   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      key: str
      configVersion: _typing.Optional[str] = None
      allocationInfo: _typing.Optional[AllocationInfo] = None
      name: _typing.Optional[str] = None
      description: _typing.Optional[str] = None

   key: str
   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   configVersion: str
   allocationInfo: AllocationInfo


class PortConnectee(pyVmomi.vmodl.DynamicData):
   class ConnecteeType(pyVmomi.VmomiSupport.Enum):
      pnic: _typing.ClassVar['ConnecteeType'] = 'pnic'
      vmVnic: _typing.ClassVar['ConnecteeType'] = 'vmVnic'
      hostConsoleVnic: _typing.ClassVar['ConnecteeType'] = 'hostConsoleVnic'
      hostVmkVnic: _typing.ClassVar['ConnecteeType'] = 'hostVmkVnic'
      systemCrxVnic: _typing.ClassVar['ConnecteeType'] = 'systemCrxVnic'

   connectedEntity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   nicKey: _typing.Optional[str] = None
   type: _typing.Optional[str] = None
   addressHint: _typing.Optional[str] = None


class PortConnection(pyVmomi.vmodl.DynamicData):
   switchUuid: str
   portgroupKey: _typing.Optional[str] = None
   portKey: _typing.Optional[str] = None
   connectionCookie: _typing.Optional[int] = None


class PortCriteria(pyVmomi.vmodl.DynamicData):
   connected: _typing.Optional[bool] = None
   active: _typing.Optional[bool] = None
   uplinkPort: _typing.Optional[bool] = None
   nsxPort: _typing.Optional[bool] = None
   scope: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   portgroupKey: list[str] = []
   inside: _typing.Optional[bool] = None
   portKey: list[str] = []
   host: list[pyVmomi.vim.HostSystem] = []


class PortStatistics(pyVmomi.vmodl.DynamicData):
   packetsInMulticast: pyVmomi.VmomiSupport.long
   packetsOutMulticast: pyVmomi.VmomiSupport.long
   bytesInMulticast: pyVmomi.VmomiSupport.long
   bytesOutMulticast: pyVmomi.VmomiSupport.long
   packetsInUnicast: pyVmomi.VmomiSupport.long
   packetsOutUnicast: pyVmomi.VmomiSupport.long
   bytesInUnicast: pyVmomi.VmomiSupport.long
   bytesOutUnicast: pyVmomi.VmomiSupport.long
   packetsInBroadcast: pyVmomi.VmomiSupport.long
   packetsOutBroadcast: pyVmomi.VmomiSupport.long
   bytesInBroadcast: pyVmomi.VmomiSupport.long
   bytesOutBroadcast: pyVmomi.VmomiSupport.long
   packetsInDropped: pyVmomi.VmomiSupport.long
   packetsOutDropped: pyVmomi.VmomiSupport.long
   packetsInException: pyVmomi.VmomiSupport.long
   packetsOutException: pyVmomi.VmomiSupport.long
   bytesInFromPnic: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   bytesOutToPnic: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class ProductSpec(pyVmomi.vmodl.DynamicData):
   name: _typing.Optional[str] = None
   vendor: _typing.Optional[str] = None
   version: _typing.Optional[str] = None
   build: _typing.Optional[str] = None
   forwardingClass: _typing.Optional[str] = None
   bundleId: _typing.Optional[str] = None
   bundleUrl: _typing.Optional[str] = None


class TrafficRule(pyVmomi.vmodl.DynamicData):
   class Qualifier(pyVmomi.vmodl.DynamicData):
      key: _typing.Optional[str] = None

   class Action(pyVmomi.vmodl.DynamicData):
      pass

   class RuleDirectionType(pyVmomi.VmomiSupport.Enum):
      incomingPackets: _typing.ClassVar['RuleDirectionType'] = 'incomingPackets'
      outgoingPackets: _typing.ClassVar['RuleDirectionType'] = 'outgoingPackets'
      both: _typing.ClassVar['RuleDirectionType'] = 'both'

   class IpQualifier(Qualifier):
      sourceAddress: _typing.Optional[pyVmomi.vim.IpAddress] = None
      destinationAddress: _typing.Optional[pyVmomi.vim.IpAddress] = None
      protocol: _typing.Optional[pyVmomi.vim.IntExpression] = None
      sourceIpPort: _typing.Optional[IpPort] = None
      destinationIpPort: _typing.Optional[IpPort] = None
      tcpFlags: _typing.Optional[pyVmomi.vim.IntExpression] = None

   class IpPort(pyVmomi.vim.NegatableExpression):
      pass

   class SingleIpPort(IpPort):
      portNumber: int

   class IpPortRange(IpPort):
      startPortNumber: int
      endPortNumber: int

   class MacQualifier(Qualifier):
      sourceAddress: _typing.Optional[pyVmomi.vim.MacAddress] = None
      destinationAddress: _typing.Optional[pyVmomi.vim.MacAddress] = None
      protocol: _typing.Optional[pyVmomi.vim.IntExpression] = None
      vlanId: _typing.Optional[pyVmomi.vim.IntExpression] = None

   class SystemTrafficQualifier(Qualifier):
      typeOfSystemTraffic: _typing.Optional[pyVmomi.vim.StringExpression] = None

   class DropAction(Action):
      pass

   class AcceptAction(Action):
      pass

   class UpdateTagAction(Action):
      qosTag: _typing.Optional[int] = None
      dscpTag: _typing.Optional[int] = None

   class RateLimitAction(Action):
      packetsPerSecond: int

   class LogAction(Action):
      pass

   class GreAction(Action):
      encapsulationIp: pyVmomi.vim.SingleIp

   class MacRewriteAction(Action):
      rewriteMac: str

   class PuntAction(Action):
      pass

   class CopyAction(Action):
      pass

   key: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   sequence: _typing.Optional[int] = None
   qualifier: list[Qualifier] = []
   action: _typing.Optional[Action] = None
   direction: _typing.Optional[str] = None


class TrafficRuleset(pyVmomi.vmodl.DynamicData):
   key: _typing.Optional[str] = None
   enabled: _typing.Optional[bool] = None
   precedence: _typing.Optional[int] = None
   rules: list[TrafficRule] = []


class VmVnicNetworkResourcePool(pyVmomi.vmodl.DynamicData):
   class ResourceAllocation(pyVmomi.vmodl.DynamicData):
      reservationQuota: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      operation: str
      key: _typing.Optional[str] = None
      configVersion: _typing.Optional[str] = None
      allocationInfo: _typing.Optional[ResourceAllocation] = None
      name: _typing.Optional[str] = None
      description: _typing.Optional[str] = None

   class VnicAllocatedResource(pyVmomi.vmodl.DynamicData):
      vm: pyVmomi.vim.VirtualMachine
      vnicKey: str
      reservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class RuntimeInfo(pyVmomi.vmodl.DynamicData):
      key: str
      name: _typing.Optional[str] = None
      capacity: _typing.Optional[int] = None
      usage: _typing.Optional[int] = None
      available: _typing.Optional[int] = None
      status: str
      allocatedResource: list[VnicAllocatedResource] = []

   key: str
   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   configVersion: str
   allocationInfo: _typing.Optional[ResourceAllocation] = None


class VmwareDistributedVirtualSwitch(pyVmomi.vim.DistributedVirtualSwitch):
   class FeatureCapability(pyVmomi.vim.DistributedVirtualSwitch.FeatureCapability):
      vspanSupported: _typing.Optional[bool] = None
      lldpSupported: _typing.Optional[bool] = None
      ipfixSupported: _typing.Optional[bool] = None
      ipfixCapability: _typing.Optional[IpfixFeatureCapability] = None
      multicastSnoopingSupported: _typing.Optional[bool] = None
      vspanCapability: _typing.Optional[VspanFeatureCapability] = None
      lacpCapability: _typing.Optional[LacpFeatureCapability] = None
      dpuCapability: _typing.Optional[DpuFeatureCapability] = None
      nsxSupported: _typing.Optional[bool] = None
      mtuCapability: _typing.Optional[MtuCapability] = None
      realTimeConfigSupported: _typing.Optional[bool] = None
      perfNicOffloadCapability: _typing.Optional[PerfNicOffloadFeatureCapability] = None
      systemTrafficCapabilities: _typing.Optional[SystemTrafficCapabilities] = None

   class IpfixFeatureCapability(pyVmomi.vmodl.DynamicData):
      ipfixSupported: _typing.Optional[bool] = None
      ipv6ForIpfixSupported: _typing.Optional[bool] = None
      observationDomainIdSupported: _typing.Optional[bool] = None

   class LacpFeatureCapability(pyVmomi.vmodl.DynamicData):
      lacpSupported: _typing.Optional[bool] = None
      multiLacpGroupSupported: _typing.Optional[bool] = None
      lacpFastModeSupported: _typing.Optional[bool] = None

   class DpuFeatureCapability(pyVmomi.vmodl.DynamicData):
      networkOffloadSupported: _typing.Optional[bool] = None
      activeStandbyModeSupported: _typing.Optional[bool] = None

   class PerfNicOffloadFeatureCapability(pyVmomi.vmodl.DynamicData):
      supported: _typing.Optional[bool] = None

   class SystemTrafficCapabilities(pyVmomi.vmodl.DynamicData):
      systemTrafficQualifiers: list[str] = []

   class VmwareHealthCheckFeatureCapability(pyVmomi.vim.DistributedVirtualSwitch.HealthCheckFeatureCapability):
      vlanMtuSupported: bool
      teamingSupported: bool

   class VspanFeatureCapability(pyVmomi.vmodl.DynamicData):
      mixedDestSupported: bool
      dvportSupported: bool
      remoteSourceSupported: bool
      remoteDestSupported: bool
      encapRemoteSourceSupported: bool
      erspanProtocolSupported: _typing.Optional[bool] = None
      mirrorNetstackSupported: _typing.Optional[bool] = None

   class MtuCapability(pyVmomi.vmodl.DynamicData):
      minMtuSupported: int
      maxMtuSupported: int

   class VspanPorts(pyVmomi.vmodl.DynamicData):
      portKey: list[str] = []
      uplinkPortName: list[str] = []
      wildcardPortConnecteeType: list[str] = []
      vlans: list[int] = []
      ipAddress: list[str] = []

   class VspanSession(pyVmomi.vmodl.DynamicData):
      key: _typing.Optional[str] = None
      name: _typing.Optional[str] = None
      description: _typing.Optional[str] = None
      enabled: bool
      sourcePortTransmitted: _typing.Optional[VspanPorts] = None
      sourcePortReceived: _typing.Optional[VspanPorts] = None
      destinationPort: _typing.Optional[VspanPorts] = None
      encapsulationVlanId: _typing.Optional[int] = None
      stripOriginalVlan: bool
      mirroredPacketLength: _typing.Optional[int] = None
      normalTrafficAllowed: bool
      sessionType: _typing.Optional[str] = None
      samplingRate: _typing.Optional[int] = None
      encapType: _typing.Optional[str] = None
      erspanId: _typing.Optional[int] = None
      erspanCOS: _typing.Optional[int] = None
      erspanGraNanosec: _typing.Optional[bool] = None
      netstack: _typing.Optional[str] = None

   class IpfixConfig(pyVmomi.vmodl.DynamicData):
      collectorIpAddress: _typing.Optional[str] = None
      collectorPort: _typing.Optional[int] = None
      observationDomainId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      activeFlowTimeout: int
      idleFlowTimeout: _typing.Optional[int] = None
      samplingRate: int
      internalFlowsOnly: bool

   class DpuFailoverPolicy(pyVmomi.vmodl.DynamicData):
      activeUplink: list[str] = []
      standbyUplink: list[str] = []

   class NetworkOffloadConfig(pyVmomi.vmodl.DynamicData):
      dpuFailoverPolicy: _typing.Optional[DpuFailoverPolicy] = None

   class RealTimeLanAnnotation(pyVmomi.vmodl.DynamicData):
      lanAUplink: list[str] = []
      lanBUplink: list[str] = []

   class RealTimeConfig(pyVmomi.vmodl.DynamicData):
      allowed: _typing.Optional[bool] = None
      lanAnnotation: _typing.Optional[RealTimeLanAnnotation] = None

   class ConfigInfo(pyVmomi.vim.DistributedVirtualSwitch.ConfigInfo):
      vspanSession: list[VspanSession] = []
      pvlanConfig: list[PvlanMapEntry] = []
      maxMtu: int
      linkDiscoveryProtocolConfig: _typing.Optional[pyVmomi.vim.host.LinkDiscoveryProtocolConfig] = None
      ipfixConfig: _typing.Optional[IpfixConfig] = None
      lacpGroupConfig: list[LacpGroupConfig] = []
      lacpApiVersion: _typing.Optional[str] = None
      multicastFilteringMode: _typing.Optional[str] = None
      networkOffloadSpecId: _typing.Optional[str] = None
      networkOffloadConfig: _typing.Optional[NetworkOffloadConfig] = None
      realTimeConfig: _typing.Optional[RealTimeConfig] = None

   class ConfigSpec(pyVmomi.vim.DistributedVirtualSwitch.ConfigSpec):
      pvlanConfigSpec: list[PvlanConfigSpec] = []
      vspanConfigSpec: list[VspanConfigSpec] = []
      maxMtu: _typing.Optional[int] = None
      linkDiscoveryProtocolConfig: _typing.Optional[pyVmomi.vim.host.LinkDiscoveryProtocolConfig] = None
      ipfixConfig: _typing.Optional[IpfixConfig] = None
      lacpApiVersion: _typing.Optional[str] = None
      multicastFilteringMode: _typing.Optional[str] = None
      networkOffloadSpecId: _typing.Optional[str] = None
      networkOffloadConfig: _typing.Optional[NetworkOffloadConfig] = None
      realTimeConfig: _typing.Optional[RealTimeConfig] = None

   class UplinkPortOrderPolicy(pyVmomi.vim.InheritablePolicy):
      activeUplinkPort: list[str] = []
      standbyUplinkPort: list[str] = []

   class FailureCriteria(pyVmomi.vim.InheritablePolicy):
      checkSpeed: _typing.Optional[pyVmomi.vim.StringPolicy] = None
      speed: _typing.Optional[pyVmomi.vim.IntPolicy] = None
      checkDuplex: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      fullDuplex: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      checkErrorPercent: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      percentage: _typing.Optional[pyVmomi.vim.IntPolicy] = None
      checkBeacon: _typing.Optional[pyVmomi.vim.BoolPolicy] = None

   class UplinkPortTeamingPolicy(pyVmomi.vim.InheritablePolicy):
      policy: _typing.Optional[pyVmomi.vim.StringPolicy] = None
      reversePolicy: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      notifySwitches: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      rollingOrder: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      failureCriteria: _typing.Optional[FailureCriteria] = None
      uplinkPortOrder: _typing.Optional[UplinkPortOrderPolicy] = None

   class VlanSpec(pyVmomi.vim.InheritablePolicy):
      pass

   class PvlanSpec(VlanSpec):
      pvlanId: int

   class VlanIdSpec(VlanSpec):
      vlanId: int

   class TrunkVlanSpec(VlanSpec):
      vlanId: list[pyVmomi.vim.NumericRange] = []

   class SecurityPolicy(pyVmomi.vim.InheritablePolicy):
      allowPromiscuous: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      macChanges: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      forgedTransmits: _typing.Optional[pyVmomi.vim.BoolPolicy] = None

   class MacLimitPolicyType(pyVmomi.VmomiSupport.Enum):
      allow: _typing.ClassVar['MacLimitPolicyType'] = 'allow'
      drop: _typing.ClassVar['MacLimitPolicyType'] = 'drop'

   class MacLearningPolicy(pyVmomi.vim.InheritablePolicy):
      enabled: bool
      allowUnicastFlooding: _typing.Optional[bool] = None
      limit: _typing.Optional[int] = None
      limitPolicy: _typing.Optional[str] = None

   class MacManagementPolicy(pyVmomi.vim.InheritablePolicy):
      allowPromiscuous: _typing.Optional[bool] = None
      macChanges: _typing.Optional[bool] = None
      forgedTransmits: _typing.Optional[bool] = None
      macLearningPolicy: _typing.Optional[MacLearningPolicy] = None

   class VmwarePortConfigPolicy(DistributedVirtualPort.Setting):
      vlan: _typing.Optional[VlanSpec] = None
      qosTag: _typing.Optional[pyVmomi.vim.IntPolicy] = None
      uplinkTeamingPolicy: _typing.Optional[UplinkPortTeamingPolicy] = None
      securityPolicy: _typing.Optional[SecurityPolicy] = None
      ipfixEnabled: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      txUplink: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      lacpPolicy: _typing.Optional[UplinkLacpPolicy] = None
      macManagementPolicy: _typing.Optional[MacManagementPolicy] = None
      VNI: _typing.Optional[pyVmomi.vim.IntPolicy] = None

   class VMwarePortgroupPolicy(DistributedVirtualPortgroup.PortgroupPolicy):
      vlanOverrideAllowed: bool
      uplinkTeamingOverrideAllowed: bool
      securityPolicyOverrideAllowed: bool
      ipfixOverrideAllowed: _typing.Optional[bool] = None
      macManagementOverrideAllowed: _typing.Optional[bool] = None

   class PvlanPortType(pyVmomi.VmomiSupport.Enum):
      promiscuous: _typing.ClassVar['PvlanPortType'] = 'promiscuous'
      isolated: _typing.ClassVar['PvlanPortType'] = 'isolated'
      community: _typing.ClassVar['PvlanPortType'] = 'community'

   class PvlanConfigSpec(pyVmomi.vmodl.DynamicData):
      pvlanEntry: PvlanMapEntry
      operation: str

   class PvlanMapEntry(pyVmomi.vmodl.DynamicData):
      primaryVlanId: int
      secondaryVlanId: int
      pvlanType: str

   class VspanConfigSpec(pyVmomi.vmodl.DynamicData):
      vspanSession: VspanSession
      operation: str

   class VspanSessionEncapType(pyVmomi.VmomiSupport.Enum):
      gre: _typing.ClassVar['VspanSessionEncapType'] = 'gre'
      erspan2: _typing.ClassVar['VspanSessionEncapType'] = 'erspan2'
      erspan3: _typing.ClassVar['VspanSessionEncapType'] = 'erspan3'

   class VspanSessionType(pyVmomi.VmomiSupport.Enum):
      mixedDestMirror: _typing.ClassVar['VspanSessionType'] = 'mixedDestMirror'
      dvPortMirror: _typing.ClassVar['VspanSessionType'] = 'dvPortMirror'
      remoteMirrorSource: _typing.ClassVar['VspanSessionType'] = 'remoteMirrorSource'
      remoteMirrorDest: _typing.ClassVar['VspanSessionType'] = 'remoteMirrorDest'
      encapsulatedRemoteMirrorSource: _typing.ClassVar['VspanSessionType'] = 'encapsulatedRemoteMirrorSource'

   class VmwareHealthCheckConfig(pyVmomi.vim.DistributedVirtualSwitch.HealthCheckConfig):
      pass

   class VlanMtuHealthCheckConfig(VmwareHealthCheckConfig):
      pass

   class TeamingHealthCheckConfig(VmwareHealthCheckConfig):
      pass

   class VlanHealthCheckResult(HostMember.UplinkHealthCheckResult):
      trunkedVlan: list[pyVmomi.vim.NumericRange] = []
      untrunkedVlan: list[pyVmomi.vim.NumericRange] = []

   class MtuHealthCheckResult(HostMember.UplinkHealthCheckResult):
      mtuMismatch: bool
      vlanSupportSwitchMtu: list[pyVmomi.vim.NumericRange] = []
      vlanNotSupportSwitchMtu: list[pyVmomi.vim.NumericRange] = []

   class TeamingMatchStatus(pyVmomi.VmomiSupport.Enum):
      iphashMatch: _typing.ClassVar['TeamingMatchStatus'] = 'iphashMatch'
      nonIphashMatch: _typing.ClassVar['TeamingMatchStatus'] = 'nonIphashMatch'
      iphashMismatch: _typing.ClassVar['TeamingMatchStatus'] = 'iphashMismatch'
      nonIphashMismatch: _typing.ClassVar['TeamingMatchStatus'] = 'nonIphashMismatch'

   class TeamingHealthCheckResult(HostMember.HealthCheckResult):
      teamingStatus: str

   class UplinkLacpPolicy(pyVmomi.vim.InheritablePolicy):
      enable: _typing.Optional[pyVmomi.vim.BoolPolicy] = None
      mode: _typing.Optional[pyVmomi.vim.StringPolicy] = None

   class LacpGroupConfig(pyVmomi.vmodl.DynamicData):
      key: _typing.Optional[str] = None
      name: _typing.Optional[str] = None
      mode: _typing.Optional[str] = None
      uplinkNum: _typing.Optional[int] = None
      loadbalanceAlgorithm: _typing.Optional[str] = None
      vlan: _typing.Optional[LagVlanConfig] = None
      ipfix: _typing.Optional[LagIpfixConfig] = None
      uplinkName: list[str] = []
      uplinkPortKey: list[str] = []
      timeoutMode: _typing.Optional[str] = None

   class LagVlanConfig(pyVmomi.vmodl.DynamicData):
      vlanId: list[pyVmomi.vim.NumericRange] = []

   class LagIpfixConfig(pyVmomi.vmodl.DynamicData):
      ipfixEnabled: _typing.Optional[bool] = None

   class UplinkLacpMode(pyVmomi.VmomiSupport.Enum):
      active: _typing.ClassVar['UplinkLacpMode'] = 'active'
      passive: _typing.ClassVar['UplinkLacpMode'] = 'passive'

   class UplinkLacpTimeoutMode(pyVmomi.VmomiSupport.Enum):
      fast: _typing.ClassVar['UplinkLacpTimeoutMode'] = 'fast'
      slow: _typing.ClassVar['UplinkLacpTimeoutMode'] = 'slow'

   class LacpGroupSpec(pyVmomi.vmodl.DynamicData):
      lacpGroupConfig: LacpGroupConfig
      operation: str

   class LacpLoadBalanceAlgorithm(pyVmomi.VmomiSupport.Enum):
      srcMac: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcMac'
      destMac: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'destMac'
      srcDestMac: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestMac'
      destIpVlan: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'destIpVlan'
      srcIpVlan: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcIpVlan'
      srcDestIpVlan: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestIpVlan'
      destTcpUdpPort: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'destTcpUdpPort'
      srcTcpUdpPort: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcTcpUdpPort'
      srcDestTcpUdpPort: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestTcpUdpPort'
      destIpTcpUdpPort: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'destIpTcpUdpPort'
      srcIpTcpUdpPort: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcIpTcpUdpPort'
      srcDestIpTcpUdpPort: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestIpTcpUdpPort'
      destIpTcpUdpPortVlan: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'destIpTcpUdpPortVlan'
      srcIpTcpUdpPortVlan: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcIpTcpUdpPortVlan'
      srcDestIpTcpUdpPortVlan: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestIpTcpUdpPortVlan'
      destIp: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'destIp'
      srcIp: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcIp'
      srcDestIp: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestIp'
      vlan: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'vlan'
      srcPortId: _typing.ClassVar['LacpLoadBalanceAlgorithm'] = 'srcPortId'

   class LacpApiVersion(pyVmomi.VmomiSupport.Enum):
      singleLag: _typing.ClassVar['LacpApiVersion'] = 'singleLag'
      multipleLag: _typing.ClassVar['LacpApiVersion'] = 'multipleLag'

   class MulticastFilteringMode(pyVmomi.VmomiSupport.Enum):
      legacyFiltering: _typing.ClassVar['MulticastFilteringMode'] = 'legacyFiltering'
      snooping: _typing.ClassVar['MulticastFilteringMode'] = 'snooping'

   def UpdateLacpGroupConfig(self, lacpGroupSpec: list[LacpGroupSpec]) -> pyVmomi.vim.Task: ...
