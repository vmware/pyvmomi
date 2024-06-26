# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import HostSystem
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import SharesInfo
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.dvs import DistributedVirtualPort
from pyVmomi.vim.dvs import DistributedVirtualPortgroup
from pyVmomi.vim.dvs import EntityBackup
from pyVmomi.vim.dvs import HostMember
from pyVmomi.vim.dvs import HostProductSpec
from pyVmomi.vim.dvs import KeyedOpaqueBlob
from pyVmomi.vim.dvs import NetworkResourcePool
from pyVmomi.vim.dvs import PortCriteria
from pyVmomi.vim.dvs import ProductSpec
from pyVmomi.vim.dvs import VmVnicNetworkResourcePool

class DistributedVirtualSwitch(ManagedEntity):
   class ProductSpecOperationType(Enum):
      preInstall: ClassVar['ProductSpecOperationType'] = 'preInstall'
      upgrade: ClassVar['ProductSpecOperationType'] = 'upgrade'
      notifyAvailableUpgrade: ClassVar['ProductSpecOperationType'] = 'notifyAvailableUpgrade'
      proceedWithUpgrade: ClassVar['ProductSpecOperationType'] = 'proceedWithUpgrade'
      updateBundleInfo: ClassVar['ProductSpecOperationType'] = 'updateBundleInfo'

   class ContactInfo(DynamicData):
      name: Optional[str] = None
      contact: Optional[str] = None

   class NicTeamingPolicyMode(Enum):
      loadbalance_ip: ClassVar['NicTeamingPolicyMode'] = 'loadbalance_ip'
      loadbalance_srcmac: ClassVar['NicTeamingPolicyMode'] = 'loadbalance_srcmac'
      loadbalance_srcid: ClassVar['NicTeamingPolicyMode'] = 'loadbalance_srcid'
      failover_explicit: ClassVar['NicTeamingPolicyMode'] = 'failover_explicit'
      loadbalance_loadbased: ClassVar['NicTeamingPolicyMode'] = 'loadbalance_loadbased'

   class NetworkResourceManagementCapability(DynamicData):
      networkResourceManagementSupported: bool
      networkResourcePoolHighShareValue: int
      qosSupported: bool
      userDefinedNetworkResourcePoolsSupported: bool
      networkResourceControlVersion3Supported: Optional[bool] = None
      userDefinedInfraTrafficPoolSupported: Optional[bool] = None

   class RollbackCapability(DynamicData):
      rollbackSupported: bool

   class BackupRestoreCapability(DynamicData):
      backupRestoreSupported: bool

   class FeatureCapability(DynamicData):
      networkResourceManagementSupported: bool
      vmDirectPathGen2Supported: Optional[bool] = None
      nicTeamingPolicy: list[str] = []
      networkResourcePoolHighShareValue: Optional[int] = None
      networkResourceManagementCapability: Optional[NetworkResourceManagementCapability] = None
      healthCheckCapability: Optional[HealthCheckFeatureCapability] = None
      rollbackCapability: Optional[RollbackCapability] = None
      backupRestoreCapability: Optional[BackupRestoreCapability] = None
      networkFilterSupported: Optional[bool] = None
      macLearningSupported: Optional[bool] = None

   class HealthCheckFeatureCapability(DynamicData):
      pass

   class Capability(DynamicData):
      dvsOperationSupported: Optional[bool] = None
      dvPortGroupOperationSupported: Optional[bool] = None
      dvPortOperationSupported: Optional[bool] = None
      compatibleHostComponentProductInfo: list[HostProductSpec] = []
      featuresSupported: Optional[FeatureCapability] = None

   class Summary(DynamicData):
      name: str
      uuid: str
      numPorts: int
      productInfo: Optional[ProductSpec] = None
      hostMember: list[HostSystem] = []
      vm: list[VirtualMachine] = []
      host: list[HostSystem] = []
      portgroupName: list[str] = []
      description: Optional[str] = None
      contact: Optional[ContactInfo] = None
      numHosts: Optional[int] = None

   class SwitchPolicy(DynamicData):
      autoPreInstallAllowed: Optional[bool] = None
      autoUpgradeAllowed: Optional[bool] = None
      partialUpgradeAllowed: Optional[bool] = None

   class UplinkPortPolicy(DynamicData):
      pass

   class NameArrayUplinkPortPolicy(UplinkPortPolicy):
      uplinkPortName: list[str] = []

   class ConfigSpec(DynamicData):
      configVersion: Optional[str] = None
      name: Optional[str] = None
      numStandalonePorts: Optional[int] = None
      maxPorts: Optional[int] = None
      uplinkPortPolicy: Optional[UplinkPortPolicy] = None
      uplinkPortgroup: list[DistributedVirtualPortgroup] = []
      defaultPortConfig: Optional[DistributedVirtualPort.Setting] = None
      host: list[HostMember.ConfigSpec] = []
      extensionKey: Optional[str] = None
      description: Optional[str] = None
      policy: Optional[SwitchPolicy] = None
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      contact: Optional[ContactInfo] = None
      switchIpAddress: Optional[str] = None
      defaultProxySwitchMaxNumPorts: Optional[int] = None
      infrastructureTrafficResourceConfig: list[HostInfrastructureTrafficResource] = []
      netResourcePoolTrafficResourceConfig: list[HostInfrastructureTrafficResource] = []
      networkResourceControlVersion: Optional[str] = None

   class CreateSpec(DynamicData):
      configSpec: ConfigSpec
      productInfo: Optional[ProductSpec] = None
      capability: Optional[Capability] = None

   class ConfigInfo(DynamicData):
      uuid: str
      name: str
      numStandalonePorts: int
      numPorts: int
      maxPorts: int
      uplinkPortPolicy: UplinkPortPolicy
      uplinkPortgroup: list[DistributedVirtualPortgroup] = []
      defaultPortConfig: DistributedVirtualPort.Setting
      host: list[HostMember] = []
      productInfo: ProductSpec
      targetInfo: Optional[ProductSpec] = None
      extensionKey: Optional[str] = None
      vendorSpecificConfig: list[KeyedOpaqueBlob] = []
      policy: Optional[SwitchPolicy] = None
      description: Optional[str] = None
      configVersion: str
      contact: ContactInfo
      switchIpAddress: Optional[str] = None
      createTime: datetime
      networkResourceManagementEnabled: bool
      defaultProxySwitchMaxNumPorts: Optional[int] = None
      healthCheckConfig: list[HealthCheckConfig] = []
      infrastructureTrafficResourceConfig: list[HostInfrastructureTrafficResource] = []
      netResourcePoolTrafficResourceConfig: list[HostInfrastructureTrafficResource] = []
      networkResourceControlVersion: Optional[str] = None
      vmVnicNetworkResourcePool: list[VmVnicNetworkResourcePool] = []
      pnicCapacityRatioForReservation: Optional[int] = None

   class NetworkResourceControlVersion(Enum):
      version2: ClassVar['NetworkResourceControlVersion'] = 'version2'
      version3: ClassVar['NetworkResourceControlVersion'] = 'version3'

   class HostInfrastructureTrafficClass(Enum):
      management: ClassVar['HostInfrastructureTrafficClass'] = 'management'
      faultTolerance: ClassVar['HostInfrastructureTrafficClass'] = 'faultTolerance'
      vmotion: ClassVar['HostInfrastructureTrafficClass'] = 'vmotion'
      virtualMachine: ClassVar['HostInfrastructureTrafficClass'] = 'virtualMachine'
      iSCSI: ClassVar['HostInfrastructureTrafficClass'] = 'iSCSI'
      nfs: ClassVar['HostInfrastructureTrafficClass'] = 'nfs'
      hbr: ClassVar['HostInfrastructureTrafficClass'] = 'hbr'
      vsan: ClassVar['HostInfrastructureTrafficClass'] = 'vsan'
      vdp: ClassVar['HostInfrastructureTrafficClass'] = 'vdp'
      backupNfc: ClassVar['HostInfrastructureTrafficClass'] = 'backupNfc'
      nvmetcp: ClassVar['HostInfrastructureTrafficClass'] = 'nvmetcp'
      provisioning: ClassVar['HostInfrastructureTrafficClass'] = 'provisioning'

   class HostInfrastructureTrafficResource(DynamicData):
      class ResourceAllocation(DynamicData):
         limit: Optional[long] = None
         shares: Optional[SharesInfo] = None
         reservation: Optional[long] = None

      key: str
      description: Optional[str] = None
      allocationInfo: ResourceAllocation

   class HealthCheckConfig(DynamicData):
      enable: Optional[bool] = None
      interval: Optional[int] = None

   class ResourceRuntimeInfo(DynamicData):
      capacity: Optional[int] = None
      usage: Optional[int] = None
      available: Optional[int] = None
      allocatedResource: list[VmVnicNetworkResourcePool.VnicAllocatedResource] = []
      vmVnicNetworkResourcePoolRuntime: list[VmVnicNetworkResourcePool.RuntimeInfo] = []

   class RuntimeInfo(DynamicData):
      hostMemberRuntime: list[HostMember.RuntimeInfo] = []
      resourceRuntimeInfo: Optional[ResourceRuntimeInfo] = None

   @property
   def uuid(self) -> str: ...
   @property
   def capability(self) -> Capability: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def config(self) -> ConfigInfo: ...
   @property
   def networkResourcePool(self) -> list[NetworkResourcePool]: ...
   @property
   def portgroup(self) -> list[DistributedVirtualPortgroup]: ...
   @property
   def runtime(self) -> Optional[RuntimeInfo]: ...

   def FetchPortKeys(self, criteria: Optional[PortCriteria]) -> list[str]: ...
   def FetchPorts(self, criteria: Optional[PortCriteria]) -> list[DistributedVirtualPort]: ...
   def QueryUsedVlanId(self) -> list[int]: ...
   def Reconfigure(self, spec: ConfigSpec) -> Task: ...
   def PerformProductSpecOperation(self, operation: str, productSpec: Optional[ProductSpec]) -> Task: ...
   def Merge(self, dvs: DistributedVirtualSwitch) -> Task: ...
   def AddPortgroups(self, spec: list[DistributedVirtualPortgroup.ConfigSpec]) -> Task: ...
   def MovePort(self, portKey: list[str], destinationPortgroupKey: Optional[str]) -> Task: ...
   def UpdateCapability(self, capability: Capability) -> NoReturn: ...
   def ReconfigurePort(self, port: list[DistributedVirtualPort.ConfigSpec]) -> Task: ...
   def RefreshPortState(self, portKeys: list[str]) -> NoReturn: ...
   def RectifyHost(self, hosts: list[HostSystem]) -> Task: ...
   def UpdateNetworkResourcePool(self, configSpec: list[NetworkResourcePool.ConfigSpec]) -> NoReturn: ...
   def AddNetworkResourcePool(self, configSpec: list[NetworkResourcePool.ConfigSpec]) -> NoReturn: ...
   def RemoveNetworkResourcePool(self, key: list[str]) -> NoReturn: ...
   def ReconfigureVmVnicNetworkResourcePool(self, configSpec: list[VmVnicNetworkResourcePool.ConfigSpec]) -> Task: ...
   def EnableNetworkResourceManagement(self, enable: bool) -> NoReturn: ...
   def Rollback(self, entityBackup: Optional[EntityBackup.Config]) -> Task: ...
   def AddPortgroup(self, spec: DistributedVirtualPortgroup.ConfigSpec) -> Task: ...
   def UpdateHealthCheckConfig(self, healthCheckConfig: list[HealthCheckConfig]) -> Task: ...
   def LookupPortgroup(self, portgroupKey: str) -> Optional[DistributedVirtualPortgroup]: ...
