# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import BoolPolicy
from pyVmomi.vim import DistributedVirtualSwitch
from pyVmomi.vim import InheritablePolicy
from pyVmomi.vim import IntPolicy
from pyVmomi.vim import NumericRange
from pyVmomi.vim import StringPolicy
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.dvs import DistributedVirtualPort
from pyVmomi.vim.dvs import DistributedVirtualPortgroup
from pyVmomi.vim.dvs import HostMember

from pyVmomi.vim.host import LinkDiscoveryProtocolConfig

class VmwareDistributedVirtualSwitch(DistributedVirtualSwitch):
   class FeatureCapability(DistributedVirtualSwitch.FeatureCapability):
      vspanSupported: Optional[bool] = None
      lldpSupported: Optional[bool] = None
      ipfixSupported: Optional[bool] = None
      ipfixCapability: Optional[IpfixFeatureCapability] = None
      multicastSnoopingSupported: Optional[bool] = None
      vspanCapability: Optional[VspanFeatureCapability] = None
      lacpCapability: Optional[LacpFeatureCapability] = None
      dpuCapability: Optional[DpuFeatureCapability] = None
      nsxSupported: Optional[bool] = None
      mtuCapability: Optional[MtuCapability] = None

   class IpfixFeatureCapability(DynamicData):
      ipfixSupported: Optional[bool] = None
      ipv6ForIpfixSupported: Optional[bool] = None
      observationDomainIdSupported: Optional[bool] = None

   class LacpFeatureCapability(DynamicData):
      lacpSupported: Optional[bool] = None
      multiLacpGroupSupported: Optional[bool] = None
      lacpFastModeSupported: Optional[bool] = None

   class DpuFeatureCapability(DynamicData):
      networkOffloadSupported: Optional[bool] = None
      activeStandbyModeSupported: Optional[bool] = None

   class VmwareHealthCheckFeatureCapability(DistributedVirtualSwitch.HealthCheckFeatureCapability):
      vlanMtuSupported: bool
      teamingSupported: bool

   class VspanFeatureCapability(DynamicData):
      mixedDestSupported: bool
      dvportSupported: bool
      remoteSourceSupported: bool
      remoteDestSupported: bool
      encapRemoteSourceSupported: bool
      erspanProtocolSupported: Optional[bool] = None
      mirrorNetstackSupported: Optional[bool] = None

   class MtuCapability(DynamicData):
      minMtuSupported: int
      maxMtuSupported: int

   class VspanPorts(DynamicData):
      portKey: list[str] = []
      uplinkPortName: list[str] = []
      wildcardPortConnecteeType: list[str] = []
      vlans: list[int] = []
      ipAddress: list[str] = []

   class VspanSession(DynamicData):
      key: Optional[str] = None
      name: Optional[str] = None
      description: Optional[str] = None
      enabled: bool
      sourcePortTransmitted: Optional[VspanPorts] = None
      sourcePortReceived: Optional[VspanPorts] = None
      destinationPort: Optional[VspanPorts] = None
      encapsulationVlanId: Optional[int] = None
      stripOriginalVlan: bool
      mirroredPacketLength: Optional[int] = None
      normalTrafficAllowed: bool
      sessionType: Optional[str] = None
      samplingRate: Optional[int] = None
      encapType: Optional[str] = None
      erspanId: Optional[int] = None
      erspanCOS: Optional[int] = None
      erspanGraNanosec: Optional[bool] = None
      netstack: Optional[str] = None

   class IpfixConfig(DynamicData):
      collectorIpAddress: Optional[str] = None
      collectorPort: Optional[int] = None
      observationDomainId: Optional[long] = None
      activeFlowTimeout: int
      idleFlowTimeout: int
      samplingRate: int
      internalFlowsOnly: bool

   class DpuFailoverPolicy(DynamicData):
      activeUplink: list[str] = []
      standbyUplink: list[str] = []

   class NetworkOffloadConfig(DynamicData):
      dpuFailoverPolicy: Optional[DpuFailoverPolicy] = None

   class ConfigInfo(DistributedVirtualSwitch.ConfigInfo):
      vspanSession: list[VspanSession] = []
      pvlanConfig: list[PvlanMapEntry] = []
      maxMtu: int
      linkDiscoveryProtocolConfig: Optional[LinkDiscoveryProtocolConfig] = None
      ipfixConfig: Optional[IpfixConfig] = None
      lacpGroupConfig: list[LacpGroupConfig] = []
      lacpApiVersion: Optional[str] = None
      multicastFilteringMode: Optional[str] = None
      networkOffloadSpecId: Optional[str] = None
      networkOffloadConfig: Optional[NetworkOffloadConfig] = None

   class ConfigSpec(DistributedVirtualSwitch.ConfigSpec):
      pvlanConfigSpec: list[PvlanConfigSpec] = []
      vspanConfigSpec: list[VspanConfigSpec] = []
      maxMtu: Optional[int] = None
      linkDiscoveryProtocolConfig: Optional[LinkDiscoveryProtocolConfig] = None
      ipfixConfig: Optional[IpfixConfig] = None
      lacpApiVersion: Optional[str] = None
      multicastFilteringMode: Optional[str] = None
      networkOffloadSpecId: Optional[str] = None
      networkOffloadConfig: Optional[NetworkOffloadConfig] = None

   class UplinkPortOrderPolicy(InheritablePolicy):
      activeUplinkPort: list[str] = []
      standbyUplinkPort: list[str] = []

   class FailureCriteria(InheritablePolicy):
      checkSpeed: Optional[StringPolicy] = None
      speed: Optional[IntPolicy] = None
      checkDuplex: Optional[BoolPolicy] = None
      fullDuplex: Optional[BoolPolicy] = None
      checkErrorPercent: Optional[BoolPolicy] = None
      percentage: Optional[IntPolicy] = None
      checkBeacon: Optional[BoolPolicy] = None

   class UplinkPortTeamingPolicy(InheritablePolicy):
      policy: Optional[StringPolicy] = None
      reversePolicy: Optional[BoolPolicy] = None
      notifySwitches: Optional[BoolPolicy] = None
      rollingOrder: Optional[BoolPolicy] = None
      failureCriteria: Optional[FailureCriteria] = None
      uplinkPortOrder: Optional[UplinkPortOrderPolicy] = None

   class VlanSpec(InheritablePolicy):
      pass

   class PvlanSpec(VlanSpec):
      pvlanId: int

   class VlanIdSpec(VlanSpec):
      vlanId: int

   class TrunkVlanSpec(VlanSpec):
      vlanId: list[NumericRange] = []

   class SecurityPolicy(InheritablePolicy):
      allowPromiscuous: Optional[BoolPolicy] = None
      macChanges: Optional[BoolPolicy] = None
      forgedTransmits: Optional[BoolPolicy] = None

   class MacLimitPolicyType(Enum):
      allow: ClassVar['MacLimitPolicyType'] = 'allow'
      drop: ClassVar['MacLimitPolicyType'] = 'drop'

   class MacLearningPolicy(InheritablePolicy):
      enabled: bool
      allowUnicastFlooding: Optional[bool] = None
      limit: Optional[int] = None
      limitPolicy: Optional[str] = None

   class MacManagementPolicy(InheritablePolicy):
      allowPromiscuous: Optional[bool] = None
      macChanges: Optional[bool] = None
      forgedTransmits: Optional[bool] = None
      macLearningPolicy: Optional[MacLearningPolicy] = None

   class VmwarePortConfigPolicy(DistributedVirtualPort.Setting):
      vlan: Optional[VlanSpec] = None
      qosTag: Optional[IntPolicy] = None
      uplinkTeamingPolicy: Optional[UplinkPortTeamingPolicy] = None
      securityPolicy: Optional[SecurityPolicy] = None
      ipfixEnabled: Optional[BoolPolicy] = None
      txUplink: Optional[BoolPolicy] = None
      lacpPolicy: Optional[UplinkLacpPolicy] = None
      macManagementPolicy: Optional[MacManagementPolicy] = None
      VNI: Optional[IntPolicy] = None

   class VMwarePortgroupPolicy(DistributedVirtualPortgroup.PortgroupPolicy):
      vlanOverrideAllowed: bool
      uplinkTeamingOverrideAllowed: bool
      securityPolicyOverrideAllowed: bool
      ipfixOverrideAllowed: Optional[bool] = None
      macManagementOverrideAllowed: Optional[bool] = None

   class PvlanPortType(Enum):
      promiscuous: ClassVar['PvlanPortType'] = 'promiscuous'
      isolated: ClassVar['PvlanPortType'] = 'isolated'
      community: ClassVar['PvlanPortType'] = 'community'

   class PvlanConfigSpec(DynamicData):
      pvlanEntry: PvlanMapEntry
      operation: str

   class PvlanMapEntry(DynamicData):
      primaryVlanId: int
      secondaryVlanId: int
      pvlanType: str

   class VspanConfigSpec(DynamicData):
      vspanSession: VspanSession
      operation: str

   class VspanSessionEncapType(Enum):
      gre: ClassVar['VspanSessionEncapType'] = 'gre'
      erspan2: ClassVar['VspanSessionEncapType'] = 'erspan2'
      erspan3: ClassVar['VspanSessionEncapType'] = 'erspan3'

   class VspanSessionType(Enum):
      mixedDestMirror: ClassVar['VspanSessionType'] = 'mixedDestMirror'
      dvPortMirror: ClassVar['VspanSessionType'] = 'dvPortMirror'
      remoteMirrorSource: ClassVar['VspanSessionType'] = 'remoteMirrorSource'
      remoteMirrorDest: ClassVar['VspanSessionType'] = 'remoteMirrorDest'
      encapsulatedRemoteMirrorSource: ClassVar['VspanSessionType'] = 'encapsulatedRemoteMirrorSource'

   class VmwareHealthCheckConfig(DistributedVirtualSwitch.HealthCheckConfig):
      pass

   class VlanMtuHealthCheckConfig(VmwareHealthCheckConfig):
      pass

   class TeamingHealthCheckConfig(VmwareHealthCheckConfig):
      pass

   class VlanHealthCheckResult(HostMember.UplinkHealthCheckResult):
      trunkedVlan: list[NumericRange] = []
      untrunkedVlan: list[NumericRange] = []

   class MtuHealthCheckResult(HostMember.UplinkHealthCheckResult):
      mtuMismatch: bool
      vlanSupportSwitchMtu: list[NumericRange] = []
      vlanNotSupportSwitchMtu: list[NumericRange] = []

   class TeamingMatchStatus(Enum):
      iphashMatch: ClassVar['TeamingMatchStatus'] = 'iphashMatch'
      nonIphashMatch: ClassVar['TeamingMatchStatus'] = 'nonIphashMatch'
      iphashMismatch: ClassVar['TeamingMatchStatus'] = 'iphashMismatch'
      nonIphashMismatch: ClassVar['TeamingMatchStatus'] = 'nonIphashMismatch'

   class TeamingHealthCheckResult(HostMember.HealthCheckResult):
      teamingStatus: str

   class UplinkLacpPolicy(InheritablePolicy):
      enable: Optional[BoolPolicy] = None
      mode: Optional[StringPolicy] = None

   class LacpGroupConfig(DynamicData):
      key: Optional[str] = None
      name: Optional[str] = None
      mode: Optional[str] = None
      uplinkNum: Optional[int] = None
      loadbalanceAlgorithm: Optional[str] = None
      vlan: Optional[LagVlanConfig] = None
      ipfix: Optional[LagIpfixConfig] = None
      uplinkName: list[str] = []
      uplinkPortKey: list[str] = []
      timeoutMode: Optional[str] = None

   class LagVlanConfig(DynamicData):
      vlanId: list[NumericRange] = []

   class LagIpfixConfig(DynamicData):
      ipfixEnabled: Optional[bool] = None

   class UplinkLacpMode(Enum):
      active: ClassVar['UplinkLacpMode'] = 'active'
      passive: ClassVar['UplinkLacpMode'] = 'passive'

   class UplinkLacpTimeoutMode(Enum):
      fast: ClassVar['UplinkLacpTimeoutMode'] = 'fast'
      slow: ClassVar['UplinkLacpTimeoutMode'] = 'slow'

   class LacpGroupSpec(DynamicData):
      lacpGroupConfig: LacpGroupConfig
      operation: str

   class LacpLoadBalanceAlgorithm(Enum):
      srcMac: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcMac'
      destMac: ClassVar['LacpLoadBalanceAlgorithm'] = 'destMac'
      srcDestMac: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestMac'
      destIpVlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'destIpVlan'
      srcIpVlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcIpVlan'
      srcDestIpVlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestIpVlan'
      destTcpUdpPort: ClassVar['LacpLoadBalanceAlgorithm'] = 'destTcpUdpPort'
      srcTcpUdpPort: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcTcpUdpPort'
      srcDestTcpUdpPort: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestTcpUdpPort'
      destIpTcpUdpPort: ClassVar['LacpLoadBalanceAlgorithm'] = 'destIpTcpUdpPort'
      srcIpTcpUdpPort: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcIpTcpUdpPort'
      srcDestIpTcpUdpPort: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestIpTcpUdpPort'
      destIpTcpUdpPortVlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'destIpTcpUdpPortVlan'
      srcIpTcpUdpPortVlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcIpTcpUdpPortVlan'
      srcDestIpTcpUdpPortVlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestIpTcpUdpPortVlan'
      destIp: ClassVar['LacpLoadBalanceAlgorithm'] = 'destIp'
      srcIp: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcIp'
      srcDestIp: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcDestIp'
      vlan: ClassVar['LacpLoadBalanceAlgorithm'] = 'vlan'
      srcPortId: ClassVar['LacpLoadBalanceAlgorithm'] = 'srcPortId'

   class LacpApiVersion(Enum):
      singleLag: ClassVar['LacpApiVersion'] = 'singleLag'
      multipleLag: ClassVar['LacpApiVersion'] = 'multipleLag'

   class MulticastFilteringMode(Enum):
      legacyFiltering: ClassVar['MulticastFilteringMode'] = 'legacyFiltering'
      snooping: ClassVar['MulticastFilteringMode'] = 'snooping'

   def UpdateLacpGroupConfig(self, lacpGroupSpec: list[LacpGroupSpec]) -> Task: ...
