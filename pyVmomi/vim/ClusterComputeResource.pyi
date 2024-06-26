# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ComputeResource
from pyVmomi.vim import Datastore
from pyVmomi.vim import DistributedVirtualSwitch
from pyVmomi.vim import Folder
from pyVmomi.vim import HostSystem
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import SDDCBase
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage

from pyVmomi.vim.cluster import ActionHistory
from pyVmomi.vim.cluster import ConfigInfo
from pyVmomi.vim.cluster import ConfigSpec
from pyVmomi.vim.cluster import ConfigSpecEx
from pyVmomi.vim.cluster import DasAdmissionControlInfo
from pyVmomi.vim.cluster import DasAdvancedRuntimeInfo
from pyVmomi.vim.cluster import DasData
from pyVmomi.vim.cluster import DrsFaults
from pyVmomi.vim.cluster import DrsMigration
from pyVmomi.vim.cluster import DrsRecommendation
from pyVmomi.vim.cluster import EVCManager
from pyVmomi.vim.cluster import EnterMaintenanceResult
from pyVmomi.vim.cluster import HostRecommendation
from pyVmomi.vim.cluster import PlacementResult
from pyVmomi.vim.cluster import PlacementSpec
from pyVmomi.vim.cluster import Recommendation
from pyVmomi.vim.cluster import ResourceUsageSummary
from pyVmomi.vim.cluster import RuleInfo
from pyVmomi.vim.cluster import UsageSummary

from pyVmomi.vim.dvs import DistributedVirtualPortgroup

from pyVmomi.vim.encryption import CryptoKeyId
from pyVmomi.vim.encryption import KeyProviderId

from pyVmomi.vim.host import ConnectSpec
from pyVmomi.vim.host import DateTimeConfig
from pyVmomi.vim.host import HostAccessManager
from pyVmomi.vim.host import VirtualNic

from pyVmomi.vim.option import OptionValue

class ClusterComputeResource(ComputeResource):
   class Summary(ComputeResource.Summary):
      currentFailoverLevel: int
      admissionControlInfo: Optional[DasAdmissionControlInfo] = None
      numVmotions: int
      targetBalance: Optional[int] = None
      currentBalance: Optional[int] = None
      drsScore: Optional[int] = None
      numVmsPerDrsScoreBucket: list[int] = []
      usageSummary: Optional[UsageSummary] = None
      currentEVCModeKey: Optional[str] = None
      currentEVCGraphicsModeKey: Optional[str] = None
      dasData: Optional[DasData] = None
      clusterMaintenanceModeStatus: Optional[str] = None
      vcsHealthStatus: Optional[str] = None
      vcsSlots: list[VcsSlots] = []

   class DVSSetting(DynamicData):
      class DVPortgroupToServiceMapping(DynamicData):
         dvPortgroup: DistributedVirtualPortgroup
         service: str

      dvSwitch: DistributedVirtualSwitch
      pnicDevices: list[str] = []
      dvPortgroupSetting: list[DVPortgroupToServiceMapping] = []

   class HCIWorkflowState(Enum):
      in_progress: ClassVar['HCIWorkflowState'] = 'in_progress'
      done: ClassVar['HCIWorkflowState'] = 'done'
      invalid: ClassVar['HCIWorkflowState'] = 'invalid'

   class HostConfigurationProfile(DynamicData):
      dateTimeConfig: Optional[DateTimeConfig] = None
      lockdownMode: Optional[HostAccessManager.LockdownMode] = None

   class HCIConfigInfo(DynamicData):
      workflowState: str
      dvsSetting: list[DVSSetting] = []
      configuredHosts: list[HostSystem] = []
      hostConfigProfile: Optional[HostConfigurationProfile] = None

   class ClusterConfigResult(DynamicData):
      failedHosts: list[Folder.FailedHostResult] = []
      configuredHosts: list[HostSystem] = []

   class DvsProfile(DynamicData):
      class DVPortgroupSpecToServiceMapping(DynamicData):
         dvPortgroupSpec: Optional[DistributedVirtualPortgroup.ConfigSpec] = None
         dvPortgroup: Optional[DistributedVirtualPortgroup] = None
         service: str

      dvsName: Optional[str] = None
      dvSwitch: Optional[DistributedVirtualSwitch] = None
      pnicDevices: list[str] = []
      dvPortgroupMapping: list[DVPortgroupSpecToServiceMapping] = []

   class VCProfile(DynamicData):
      clusterSpec: Optional[ConfigSpecEx] = None
      evcModeKey: Optional[str] = None
      evcGraphicsModeKey: Optional[str] = None

   class HCIConfigSpec(DynamicData):
      dvsProf: list[DvsProfile] = []
      hostConfigProfile: Optional[HostConfigurationProfile] = None
      vSanConfigSpec: Optional[SDDCBase] = None
      vcProf: Optional[VCProfile] = None

   class HostVmkNicInfo(DynamicData):
      nicSpec: VirtualNic.Specification
      service: str

   class HostConfigurationInput(DynamicData):
      host: HostSystem
      hostVmkNics: list[HostVmkNicInfo] = []
      allowedInNonMaintenanceMode: Optional[bool] = None

   class ValidationResultBase(DynamicData):
      info: list[LocalizableMessage] = []

   class HostConfigurationValidation(ValidationResultBase):
      host: HostSystem
      isDvsSettingValid: Optional[bool] = None
      isVmknicSettingValid: Optional[bool] = None
      isNtpSettingValid: Optional[bool] = None
      isLockdownModeValid: Optional[bool] = None

   class DVSConfigurationValidation(ValidationResultBase):
      isDvsValid: bool
      isDvpgValid: bool

   class HostEvacuationInfo(DynamicData):
      host: HostSystem
      action: list[OptionValue] = []

   class MaintenanceInfo(DynamicData):
      partialMMId: Optional[str] = None
      hostEvacInfo: list[HostEvacuationInfo] = []

   class CryptoModePolicy(DynamicData):
      keyId: Optional[CryptoKeyId] = None
      providerId: Optional[KeyProviderId] = None

   class VcsHealthStatus(Enum):
      healthy: ClassVar['VcsHealthStatus'] = 'healthy'
      degraded: ClassVar['VcsHealthStatus'] = 'degraded'
      nonhealthy: ClassVar['VcsHealthStatus'] = 'nonhealthy'

   class VcsSlots(DynamicData):
      systemId: Optional[str] = None
      host: HostSystem
      datastore: list[Datastore] = []
      totalSlots: int

   @property
   def configuration(self) -> ConfigInfo: ...
   @property
   def recommendation(self) -> list[Recommendation]: ...
   @property
   def drsRecommendation(self) -> list[DrsRecommendation]: ...
   @property
   def summaryEx(self) -> Summary: ...
   @property
   def hciConfig(self) -> Optional[HCIConfigInfo]: ...
   @property
   def migrationHistory(self) -> list[DrsMigration]: ...
   @property
   def actionHistory(self) -> list[ActionHistory]: ...
   @property
   def drsFault(self) -> list[DrsFaults]: ...

   def ConfigureHCI(self, clusterSpec: HCIConfigSpec, hostInputs: list[HostConfigurationInput]) -> Task: ...
   def ExtendHCI(self, hostInputs: list[HostConfigurationInput], vSanConfigSpec: Optional[SDDCBase]) -> Task: ...
   def AbandonHciWorkflow(self) -> NoReturn: ...
   def ValidateHCIConfiguration(self, hciConfigSpec: Optional[HCIConfigSpec], hosts: list[HostSystem]) -> list[ValidationResultBase]: ...
   def Reconfigure(self, spec: ConfigSpec, modify: bool) -> Task: ...
   def ApplyRecommendation(self, key: str) -> NoReturn: ...
   def CancelRecommendation(self, key: str) -> NoReturn: ...
   def RecommendHostsForVm(self, vm: VirtualMachine, pool: Optional[ResourcePool]) -> list[HostRecommendation]: ...
   def AddHost(self, spec: ConnectSpec, asConnected: bool, resourcePool: Optional[ResourcePool], license: Optional[str]) -> Task: ...
   def MoveInto(self, host: list[HostSystem]) -> Task: ...
   def MoveHostInto(self, host: HostSystem, resourcePool: Optional[ResourcePool]) -> Task: ...
   def RefreshRecommendation(self) -> NoReturn: ...
   def EvcManager(self) -> Optional[EVCManager]: ...
   def RetrieveDasAdvancedRuntimeInfo(self) -> Optional[DasAdvancedRuntimeInfo]: ...
   def EnterMaintenanceMode(self, host: list[HostSystem], option: list[OptionValue], info: Optional[MaintenanceInfo]) -> EnterMaintenanceResult: ...
   def PlaceVm(self, placementSpec: PlacementSpec) -> PlacementResult: ...
   def FindRulesForVm(self, vm: VirtualMachine) -> list[RuleInfo]: ...
   def StampAllRulesWithUuid(self) -> Task: ...
   def GetResourceUsage(self) -> ResourceUsageSummary: ...
   def SetCryptoMode(self, cryptoMode: str, policy: Optional[CryptoModePolicy]) -> NoReturn: ...
   def GetSystemVMsRestrictedDatastores(self) -> list[Datastore]: ...
