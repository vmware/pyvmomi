# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.host
import pyVmomi.vim.option
import pyVmomi.vim.vm
import pyVmomi.vim.vsan
import pyVmomi.vim.vm.device
import pyVmomi.vim.vsan.cluster
import pyVmomi.vim.vsan.host



class Action(pyVmomi.vmodl.DynamicData):
   class ActionType(pyVmomi.VmomiSupport.Enum):
      MigrationV1: _typing.ClassVar['ActionType'] = 'MigrationV1'
      VmPowerV1: _typing.ClassVar['ActionType'] = 'VmPowerV1'
      HostPowerV1: _typing.ClassVar['ActionType'] = 'HostPowerV1'
      IncreaseLimitV1: _typing.ClassVar['ActionType'] = 'IncreaseLimitV1'
      IncreaseSizeV1: _typing.ClassVar['ActionType'] = 'IncreaseSizeV1'
      IncreaseSharesV1: _typing.ClassVar['ActionType'] = 'IncreaseSharesV1'
      IncreaseReservationV1: _typing.ClassVar['ActionType'] = 'IncreaseReservationV1'
      DecreaseOthersReservationV1: _typing.ClassVar['ActionType'] = 'DecreaseOthersReservationV1'
      IncreaseClusterCapacityV1: _typing.ClassVar['ActionType'] = 'IncreaseClusterCapacityV1'
      DecreaseMigrationThresholdV1: _typing.ClassVar['ActionType'] = 'DecreaseMigrationThresholdV1'
      HostMaintenanceV1: _typing.ClassVar['ActionType'] = 'HostMaintenanceV1'
      StorageMigrationV1: _typing.ClassVar['ActionType'] = 'StorageMigrationV1'
      StoragePlacementV1: _typing.ClassVar['ActionType'] = 'StoragePlacementV1'
      PlacementV1: _typing.ClassVar['ActionType'] = 'PlacementV1'
      HostInfraUpdateHaV1: _typing.ClassVar['ActionType'] = 'HostInfraUpdateHaV1'

   type: str
   target: _typing.Optional[pyVmomi.VmomiSupport.ManagedObject] = None


class ActionHistory(pyVmomi.vmodl.DynamicData):
   action: Action
   time: _datetime.datetime


class AffinityRuleSpec(RuleInfo):
   vm: list[pyVmomi.vim.VirtualMachine] = []


class AntiAffinityRuleSpec(RuleInfo):
   vm: list[pyVmomi.vim.VirtualMachine] = []


class AttemptedVmInfo(pyVmomi.vmodl.DynamicData):
   vm: pyVmomi.vim.VirtualMachine
   task: _typing.Optional[pyVmomi.vim.Task] = None


class ClusterInitialPlacementAction(Action):
   targetHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
   pool: pyVmomi.vim.ResourcePool
   availableNetworks: list[pyVmomi.vim.Network] = []
   configSpec: _typing.Optional[pyVmomi.vim.vm.ConfigSpec] = None


class ClusterPowerContext(pyVmomi.vmodl.DynamicData):
   currentClusterPowerStatus: str
   orderedClusterPowerStatus: list[str] = []
   trackingTask: _typing.Optional[pyVmomi.vim.Task] = None
   lastErrorMessage: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None
   lastErrorMOs: list[pyVmomi.VmomiSupport.ManagedObject] = []

class ClusterPowerStatus:
   pass


class ConfigInfo(pyVmomi.vmodl.DynamicData):
   dasConfig: DasConfigInfo
   dasVmConfig: list[DasVmConfigInfo] = []
   drsConfig: DrsConfigInfo
   drsVmConfig: list[DrsVmConfigInfo] = []
   rule: list[RuleInfo] = []


class ConfigInfoEx(pyVmomi.vim.ComputeResource.ConfigInfo):
   systemVMsConfig: _typing.Optional[SystemVMsConfigInfo] = None
   dasConfig: DasConfigInfo
   dasVmConfig: list[DasVmConfigInfo] = []
   drsConfig: DrsConfigInfo
   drsVmConfig: list[DrsVmConfigInfo] = []
   rule: list[RuleInfo] = []
   orchestration: _typing.Optional[OrchestrationInfo] = None
   vmOrchestration: list[VmOrchestrationInfo] = []
   dpmConfigInfo: _typing.Optional[DpmConfigInfo] = None
   dpmHostConfig: list[DpmHostConfigInfo] = []
   vsanConfigInfo: _typing.Optional[pyVmomi.vim.vsan.cluster.ConfigInfo] = None
   vsanHostConfig: list[pyVmomi.vim.vsan.host.ConfigInfo] = []
   group: list[GroupInfo] = []
   infraUpdateHaConfig: _typing.Optional[InfraUpdateHaConfigInfo] = None
   proactiveDrsConfig: _typing.Optional[ProactiveDrsConfigInfo] = None
   cryptoConfig: _typing.Optional[CryptoConfigInfo] = None
   vsanCoreConfig: _typing.Optional[pyVmomi.vim.vsan.cluster.CoreConfigInfo] = None


class ConfigSpec(pyVmomi.vmodl.DynamicData):
   dasConfig: _typing.Optional[DasConfigInfo] = None
   dasVmConfigSpec: list[DasVmConfigSpec] = []
   drsConfig: _typing.Optional[DrsConfigInfo] = None
   drsVmConfigSpec: list[DrsVmConfigSpec] = []
   rulesSpec: list[RuleSpec] = []


class ConfigSpecEx(pyVmomi.vim.ComputeResource.ConfigSpec):
   systemVMsConfig: _typing.Optional[SystemVMsConfigSpec] = None
   dasConfig: _typing.Optional[DasConfigInfo] = None
   dasVmConfigSpec: list[DasVmConfigSpec] = []
   drsConfig: _typing.Optional[DrsConfigInfo] = None
   drsVmConfigSpec: list[DrsVmConfigSpec] = []
   rulesSpec: list[RuleSpec] = []
   orchestration: _typing.Optional[OrchestrationInfo] = None
   vmOrchestrationSpec: list[VmOrchestrationSpec] = []
   dpmConfig: _typing.Optional[DpmConfigInfo] = None
   dpmHostConfigSpec: list[DpmHostConfigSpec] = []
   vsanConfig: _typing.Optional[pyVmomi.vim.vsan.cluster.ConfigInfo] = None
   vsanHostConfigSpec: list[pyVmomi.vim.vsan.host.ConfigInfo] = []
   groupSpec: list[GroupSpec] = []
   infraUpdateHaConfig: _typing.Optional[InfraUpdateHaConfigInfo] = None
   proactiveDrsConfig: _typing.Optional[ProactiveDrsConfigInfo] = None
   inHciWorkflow: _typing.Optional[bool] = None
   cryptoConfig: _typing.Optional[CryptoConfigInfo] = None
   vsanCoreConfigSpec: _typing.Optional[pyVmomi.vim.vsan.cluster.CoreConfigSpec] = None


class CryptoConfigInfo(pyVmomi.vmodl.DynamicData):
   class CryptoMode(pyVmomi.VmomiSupport.Enum):
      onDemand: _typing.ClassVar['CryptoMode'] = 'onDemand'
      forceEnable: _typing.ClassVar['CryptoMode'] = 'forceEnable'

   cryptoMode: _typing.Optional[str] = None
   policy: _typing.Optional[pyVmomi.vim.ClusterComputeResource.CryptoModePolicy] = None


class DasAamHostInfo(DasHostInfo):
   hostDasState: list[DasAamNodeState] = []
   primaryHosts: list[str] = []


class DasAamNodeState(pyVmomi.vmodl.DynamicData):
   class DasState(pyVmomi.VmomiSupport.Enum):
      uninitialized: _typing.ClassVar['DasState'] = 'uninitialized'
      initialized: _typing.ClassVar['DasState'] = 'initialized'
      configuring: _typing.ClassVar['DasState'] = 'configuring'
      unconfiguring: _typing.ClassVar['DasState'] = 'unconfiguring'
      running: _typing.ClassVar['DasState'] = 'running'
      error: _typing.ClassVar['DasState'] = 'error'
      agentShutdown: _typing.ClassVar['DasState'] = 'agentShutdown'
      nodeFailed: _typing.ClassVar['DasState'] = 'nodeFailed'

   host: pyVmomi.vim.HostSystem
   name: str
   configState: str
   runtimeState: str


class DasAdmissionControlInfo(pyVmomi.vmodl.DynamicData):
   pass


class DasAdmissionControlPolicy(pyVmomi.vmodl.DynamicData):
   resourceReductionToToleratePercent: _typing.Optional[int] = None
   pMemAdmissionControlEnabled: _typing.Optional[bool] = None


class DasAdvancedRuntimeInfo(pyVmomi.vmodl.DynamicData):
   class VmcpCapabilityInfo(pyVmomi.vmodl.DynamicData):
      storageAPDSupported: bool
      storagePDLSupported: bool

   class HeartbeatDatastoreInfo(pyVmomi.vmodl.DynamicData):
      datastore: pyVmomi.vim.Datastore
      hosts: list[pyVmomi.vim.HostSystem] = []

   dasHostInfo: _typing.Optional[DasHostInfo] = None
   vmcpSupported: _typing.Optional[VmcpCapabilityInfo] = None
   heartbeatDatastoreInfo: list[HeartbeatDatastoreInfo] = []


class DasConfigInfo(pyVmomi.vmodl.DynamicData):
   class ServiceState(pyVmomi.VmomiSupport.Enum):
      disabled: _typing.ClassVar['ServiceState'] = 'disabled'
      enabled: _typing.ClassVar['ServiceState'] = 'enabled'

   class VmMonitoringState(pyVmomi.VmomiSupport.Enum):
      vmMonitoringDisabled: _typing.ClassVar['VmMonitoringState'] = 'vmMonitoringDisabled'
      vmMonitoringOnly: _typing.ClassVar['VmMonitoringState'] = 'vmMonitoringOnly'
      vmAndAppMonitoring: _typing.ClassVar['VmMonitoringState'] = 'vmAndAppMonitoring'

   class HBDatastoreCandidate(pyVmomi.VmomiSupport.Enum):
      userSelectedDs: _typing.ClassVar['HBDatastoreCandidate'] = 'userSelectedDs'
      allFeasibleDs: _typing.ClassVar['HBDatastoreCandidate'] = 'allFeasibleDs'
      allFeasibleDsWithUserPreference: _typing.ClassVar['HBDatastoreCandidate'] = 'allFeasibleDsWithUserPreference'

   enabled: _typing.Optional[bool] = None
   vmMonitoring: _typing.Optional[str] = None
   hostMonitoring: _typing.Optional[str] = None
   vmComponentProtecting: _typing.Optional[str] = None
   failoverLevel: _typing.Optional[int] = None
   admissionControlPolicy: _typing.Optional[DasAdmissionControlPolicy] = None
   admissionControlEnabled: _typing.Optional[bool] = None
   defaultVmSettings: _typing.Optional[DasVmSettings] = None
   option: list[pyVmomi.vim.option.OptionValue] = []
   heartbeatDatastore: list[pyVmomi.vim.Datastore] = []
   hBDatastoreCandidatePolicy: _typing.Optional[str] = None


class DasData(pyVmomi.vmodl.DynamicData):
   pass


class DasDataSummary(DasData):
   hostListVersion: pyVmomi.VmomiSupport.long
   clusterConfigVersion: pyVmomi.VmomiSupport.long
   compatListVersion: pyVmomi.VmomiSupport.long


class DasFailoverLevelAdvancedRuntimeInfo(DasAdvancedRuntimeInfo):
   class SlotInfo(pyVmomi.vmodl.DynamicData):
      numVcpus: int
      cpuMHz: int
      memoryMB: int

   class HostSlots(pyVmomi.vmodl.DynamicData):
      host: pyVmomi.vim.HostSystem
      slots: int

   class VmSlots(pyVmomi.vmodl.DynamicData):
      vm: pyVmomi.vim.VirtualMachine
      slots: int

   slotInfo: SlotInfo
   totalSlots: int
   usedSlots: int
   unreservedSlots: int
   totalVms: int
   totalHosts: int
   totalGoodHosts: int
   hostSlots: list[HostSlots] = []
   vmsRequiringMultipleSlots: list[VmSlots] = []

class DasFdmAvailabilityState:
   pass


class DasFdmHostState(pyVmomi.vmodl.DynamicData):
   state: str
   stateReporter: _typing.Optional[pyVmomi.vim.HostSystem] = None


class DasHostInfo(pyVmomi.vmodl.DynamicData):
   pass


class DasHostRecommendation(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   drsRating: _typing.Optional[int] = None


class DasVmConfigInfo(pyVmomi.vmodl.DynamicData):
   class Priority(pyVmomi.VmomiSupport.Enum):
      disabled: _typing.ClassVar['Priority'] = 'disabled'
      low: _typing.ClassVar['Priority'] = 'low'
      medium: _typing.ClassVar['Priority'] = 'medium'
      high: _typing.ClassVar['Priority'] = 'high'

   key: pyVmomi.vim.VirtualMachine
   restartPriority: _typing.Optional[Priority] = None
   powerOffOnIsolation: _typing.Optional[bool] = None
   dasSettings: _typing.Optional[DasVmSettings] = None


class DasVmConfigSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   info: _typing.Optional[DasVmConfigInfo] = None


class DasVmSettings(pyVmomi.vmodl.DynamicData):
   class RestartPriority(pyVmomi.VmomiSupport.Enum):
      disabled: _typing.ClassVar['RestartPriority'] = 'disabled'
      lowest: _typing.ClassVar['RestartPriority'] = 'lowest'
      low: _typing.ClassVar['RestartPriority'] = 'low'
      medium: _typing.ClassVar['RestartPriority'] = 'medium'
      high: _typing.ClassVar['RestartPriority'] = 'high'
      highest: _typing.ClassVar['RestartPriority'] = 'highest'
      clusterRestartPriority: _typing.ClassVar['RestartPriority'] = 'clusterRestartPriority'

   class IsolationResponse(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['IsolationResponse'] = 'none'
      powerOff: _typing.ClassVar['IsolationResponse'] = 'powerOff'
      shutdown: _typing.ClassVar['IsolationResponse'] = 'shutdown'
      clusterIsolationResponse: _typing.ClassVar['IsolationResponse'] = 'clusterIsolationResponse'

   restartPriority: _typing.Optional[str] = None
   restartPriorityTimeout: _typing.Optional[int] = None
   isolationResponse: _typing.Optional[str] = None
   vmToolsMonitoringSettings: _typing.Optional[VmToolsMonitoringSettings] = None
   vmComponentProtectionSettings: _typing.Optional[VmComponentProtectionSettings] = None


class DatastoreUpdateSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None

class DependencyRuleInfo(RuleInfo):
   vmGroup: str
   dependsOnVmGroup: str


class DpmConfigInfo(pyVmomi.vmodl.DynamicData):
   class DpmBehavior(pyVmomi.VmomiSupport.Enum):
      manual: _typing.ClassVar['DpmBehavior'] = 'manual'
      automated: _typing.ClassVar['DpmBehavior'] = 'automated'

   enabled: _typing.Optional[bool] = None
   defaultDpmBehavior: _typing.Optional[DpmBehavior] = None
   hostPowerActionRate: _typing.Optional[int] = None
   option: list[pyVmomi.vim.option.OptionValue] = []


class DpmHostConfigInfo(pyVmomi.vmodl.DynamicData):
   key: pyVmomi.vim.HostSystem
   enabled: _typing.Optional[bool] = None
   behavior: _typing.Optional[DpmConfigInfo.DpmBehavior] = None


class DpmHostConfigSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   info: _typing.Optional[DpmHostConfigInfo] = None


class DrsConfigInfo(pyVmomi.vmodl.DynamicData):
   class DrsBehavior(pyVmomi.VmomiSupport.Enum):
      manual: _typing.ClassVar['DrsBehavior'] = 'manual'
      partiallyAutomated: _typing.ClassVar['DrsBehavior'] = 'partiallyAutomated'
      fullyAutomated: _typing.ClassVar['DrsBehavior'] = 'fullyAutomated'

   enabled: _typing.Optional[bool] = None
   enableVmBehaviorOverrides: _typing.Optional[bool] = None
   defaultVmBehavior: _typing.Optional[DrsBehavior] = None
   vmotionRate: _typing.Optional[int] = None
   scaleDescendantsShares: _typing.Optional[str] = None
   option: list[pyVmomi.vim.option.OptionValue] = []


class DrsFaults(pyVmomi.vmodl.DynamicData):
   class FaultsByVm(pyVmomi.vmodl.DynamicData):
      vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
      fault: list[pyVmomi.vmodl.MethodFault] = []

   class FaultsByVirtualDisk(FaultsByVm):
      disk: _typing.Optional[pyVmomi.vim.vm.device.VirtualDiskId] = None

   reason: str
   faultsByVm: list[FaultsByVm] = []


class DrsMigration(pyVmomi.vmodl.DynamicData):
   key: str
   time: _datetime.datetime
   vm: pyVmomi.vim.VirtualMachine
   cpuLoad: _typing.Optional[int] = None
   memoryLoad: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   source: pyVmomi.vim.HostSystem
   sourceCpuLoad: _typing.Optional[int] = None
   sourceMemoryLoad: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   destination: pyVmomi.vim.HostSystem
   destinationCpuLoad: _typing.Optional[int] = None
   destinationMemoryLoad: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class DrsRecommendation(pyVmomi.vmodl.DynamicData):
   class ReasonCode(pyVmomi.VmomiSupport.Enum):
      fairnessCpuAvg: _typing.ClassVar['ReasonCode'] = 'fairnessCpuAvg'
      fairnessMemAvg: _typing.ClassVar['ReasonCode'] = 'fairnessMemAvg'
      jointAffin: _typing.ClassVar['ReasonCode'] = 'jointAffin'
      antiAffin: _typing.ClassVar['ReasonCode'] = 'antiAffin'
      hostMaint: _typing.ClassVar['ReasonCode'] = 'hostMaint'

   key: str
   rating: int
   reason: str
   reasonText: str
   migrationList: list[DrsMigration] = []


class DrsVmConfigInfo(pyVmomi.vmodl.DynamicData):
   key: pyVmomi.vim.VirtualMachine
   enabled: _typing.Optional[bool] = None
   behavior: _typing.Optional[DrsConfigInfo.DrsBehavior] = None


class DrsVmConfigSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   info: _typing.Optional[DrsVmConfigInfo] = None


class EVCManager(pyVmomi.vim.ExtensibleManagedObject):
   class EVCState(pyVmomi.vmodl.DynamicData):
      supportedEVCMode: list[pyVmomi.vim.EVCMode] = []
      currentEVCModeKey: _typing.Optional[str] = None
      guaranteedCPUFeatures: list[pyVmomi.vim.host.CpuIdInfo] = []
      featureCapability: list[pyVmomi.vim.host.FeatureCapability] = []
      featureMask: list[pyVmomi.vim.host.FeatureMask] = []
      featureRequirement: list[pyVmomi.vim.vm.FeatureRequirement] = []

   class CheckResult(pyVmomi.vmodl.DynamicData):
      evcModeKey: str
      error: pyVmomi.vmodl.MethodFault
      host: list[pyVmomi.vim.HostSystem] = []

   @property
   def managedCluster(self) -> pyVmomi.vim.ClusterComputeResource: ...
   @property
   def evcState(self) -> EVCState: ...

   def ConfigureEvc(self, evcModeKey: str, evcGraphicsModeKey: _typing.Optional[str]) -> pyVmomi.vim.Task: ...
   def DisableEvc(self) -> pyVmomi.vim.Task: ...
   def CheckConfigureEvc(self, evcModeKey: str, evcGraphicsModeKey: _typing.Optional[str]) -> pyVmomi.vim.Task: ...
   def CheckAddHostEvc(self, cnxSpec: pyVmomi.vim.host.ConnectSpec) -> pyVmomi.vim.Task: ...


class EnterMaintenanceResult(pyVmomi.vmodl.DynamicData):
   recommendations: list[Recommendation] = []
   fault: _typing.Optional[DrsFaults] = None


class FailoverHostAdmissionControlInfo(DasAdmissionControlInfo):
   class HostStatus(pyVmomi.vmodl.DynamicData):
      host: pyVmomi.vim.HostSystem
      status: pyVmomi.vim.ManagedEntity.Status

   hostStatus: list[HostStatus] = []


class FailoverHostAdmissionControlPolicy(DasAdmissionControlPolicy):
   failoverHosts: list[pyVmomi.vim.HostSystem] = []
   failoverLevel: _typing.Optional[int] = None

class FailoverLevelAdmissionControlInfo(DasAdmissionControlInfo):
   currentFailoverLevel: int


class FailoverLevelAdmissionControlPolicy(DasAdmissionControlPolicy):
   failoverLevel: int
   slotPolicy: _typing.Optional[SlotPolicy] = None


class FailoverResourcesAdmissionControlInfo(DasAdmissionControlInfo):
   currentCpuFailoverResourcesPercent: int
   currentMemoryFailoverResourcesPercent: int
   currentPMemFailoverResourcesPercent: _typing.Optional[int] = None


class FailoverResourcesAdmissionControlPolicy(DasAdmissionControlPolicy):
   cpuFailoverResourcesPercent: int
   memoryFailoverResourcesPercent: int
   failoverLevel: _typing.Optional[int] = None
   autoComputePercentages: _typing.Optional[bool] = None
   pMemFailoverResourcesPercent: _typing.Optional[int] = None
   autoComputePMemFailoverResourcesPercent: _typing.Optional[bool] = None

class FaultDomainDestroySpec(VsanFaultDomainSpec):
   pass

class FaultDomainUpdateSpec(VsanFaultDomainSpec):
   operation: str

class FixedSizeSlotPolicy(SlotPolicy):
   cpu: int
   memory: int


class FtVmHostRuleInfo(RuleInfo):
   vmGroupName: str
   hostGroupName: list[str] = []


class GroupInfo(pyVmomi.vmodl.DynamicData):
   name: str
   userCreated: _typing.Optional[bool] = None
   uniqueID: _typing.Optional[str] = None


class GroupSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   info: _typing.Optional[GroupInfo] = None


class HostGroup(GroupInfo):
   host: list[pyVmomi.vim.HostSystem] = []


class HostInfraUpdateHaModeAction(Action):
   class OperationType(pyVmomi.VmomiSupport.Enum):
      enterQuarantine: _typing.ClassVar['OperationType'] = 'enterQuarantine'
      exitQuarantine: _typing.ClassVar['OperationType'] = 'exitQuarantine'
      enterMaintenance: _typing.ClassVar['OperationType'] = 'enterMaintenance'

   operationType: str


class HostPowerAction(Action):
   class OperationType(pyVmomi.VmomiSupport.Enum):
      powerOn: _typing.ClassVar['OperationType'] = 'powerOn'
      powerOff: _typing.ClassVar['OperationType'] = 'powerOff'

   operationType: OperationType
   powerConsumptionWatt: _typing.Optional[int] = None
   cpuCapacityMHz: _typing.Optional[int] = None
   memCapacityMB: _typing.Optional[int] = None


class HostRecommendation(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   rating: int


class InfraUpdateHaConfigInfo(pyVmomi.vmodl.DynamicData):
   class BehaviorType(pyVmomi.VmomiSupport.Enum):
      Manual: _typing.ClassVar['BehaviorType'] = 'Manual'
      Automated: _typing.ClassVar['BehaviorType'] = 'Automated'

   class RemediationType(pyVmomi.VmomiSupport.Enum):
      QuarantineMode: _typing.ClassVar['RemediationType'] = 'QuarantineMode'
      MaintenanceMode: _typing.ClassVar['RemediationType'] = 'MaintenanceMode'

   enabled: _typing.Optional[bool] = None
   behavior: _typing.Optional[str] = None
   moderateRemediation: _typing.Optional[str] = None
   severeRemediation: _typing.Optional[str] = None
   providers: list[str] = []


class InitialPlacementAction(Action):
   targetHost: pyVmomi.vim.HostSystem
   pool: _typing.Optional[pyVmomi.vim.ResourcePool] = None


class MigrationAction(Action):
   drsMigration: _typing.Optional[DrsMigration] = None


class NotAttemptedVmInfo(pyVmomi.vmodl.DynamicData):
   vm: pyVmomi.vim.VirtualMachine
   fault: pyVmomi.vmodl.MethodFault


class OrchestrationInfo(pyVmomi.vmodl.DynamicData):
   defaultVmReadiness: _typing.Optional[VmReadiness] = None


class PerformClusterPowerActionSpec(pyVmomi.vmodl.DynamicData):
   targetPowerStatus: str
   isOrchestration: _typing.Optional[bool] = None
   initialPowerStatus: _typing.Optional[str] = None
   powerOffReason: _typing.Optional[str] = None
   infraVMs: list[pyVmomi.vim.VirtualMachine] = []
   infraVMUuids: list[str] = []


class PlacementAction(Action):
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   targetHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
   relocateSpec: _typing.Optional[pyVmomi.vim.vm.RelocateSpec] = None


class PlacementResult(pyVmomi.vmodl.DynamicData):
   recommendations: list[Recommendation] = []
   drsFault: _typing.Optional[DrsFaults] = None


class PlacementSpec(pyVmomi.vmodl.DynamicData):
   class PlacementType(pyVmomi.VmomiSupport.Enum):
      create: _typing.ClassVar['PlacementType'] = 'create'
      reconfigure: _typing.ClassVar['PlacementType'] = 'reconfigure'
      relocate: _typing.ClassVar['PlacementType'] = 'relocate'
      clone: _typing.ClassVar['PlacementType'] = 'clone'

   priority: _typing.Optional[pyVmomi.vim.VirtualMachine.MovePriority] = None
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   configSpec: _typing.Optional[pyVmomi.vim.vm.ConfigSpec] = None
   relocateSpec: _typing.Optional[pyVmomi.vim.vm.RelocateSpec] = None
   hosts: list[pyVmomi.vim.HostSystem] = []
   datastores: list[pyVmomi.vim.Datastore] = []
   storagePods: list[pyVmomi.vim.StoragePod] = []
   disallowPrerequisiteMoves: _typing.Optional[bool] = None
   rules: list[RuleInfo] = []
   key: _typing.Optional[str] = None
   placementType: _typing.Optional[str] = None
   cloneSpec: _typing.Optional[pyVmomi.vim.vm.CloneSpec] = None
   cloneName: _typing.Optional[str] = None

class PowerOnVmOption:
   pass


class PowerOnVmResult(pyVmomi.vmodl.DynamicData):
   attempted: list[AttemptedVmInfo] = []
   notAttempted: list[NotAttemptedVmInfo] = []
   recommendations: list[Recommendation] = []


class PreemptibleVmPairInfo(pyVmomi.vmodl.DynamicData):
   id: _typing.Optional[int] = None
   monitoredVm: pyVmomi.vim.VirtualMachine
   preemptibleVm: pyVmomi.vim.VirtualMachine


class PreemptibleVmPairSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   info: _typing.Optional[PreemptibleVmPairInfo] = None


class ProactiveDrsConfigInfo(pyVmomi.vmodl.DynamicData):
   enabled: _typing.Optional[bool] = None


class QueryVsanManagedStorageSpaceUsageSpec(pyVmomi.vmodl.DynamicData):
   datastoreTypes: list[str] = []


class Recommendation(pyVmomi.vmodl.DynamicData):
   class RecommendationType(pyVmomi.VmomiSupport.Enum):
      V1: _typing.ClassVar['RecommendationType'] = 'V1'

   class ReasonCode(pyVmomi.VmomiSupport.Enum):
      fairnessCpuAvg: _typing.ClassVar['ReasonCode'] = 'fairnessCpuAvg'
      fairnessMemAvg: _typing.ClassVar['ReasonCode'] = 'fairnessMemAvg'
      jointAffin: _typing.ClassVar['ReasonCode'] = 'jointAffin'
      antiAffin: _typing.ClassVar['ReasonCode'] = 'antiAffin'
      hostMaint: _typing.ClassVar['ReasonCode'] = 'hostMaint'
      enterStandby: _typing.ClassVar['ReasonCode'] = 'enterStandby'
      reservationCpu: _typing.ClassVar['ReasonCode'] = 'reservationCpu'
      reservationMem: _typing.ClassVar['ReasonCode'] = 'reservationMem'
      powerOnVm: _typing.ClassVar['ReasonCode'] = 'powerOnVm'
      powerSaving: _typing.ClassVar['ReasonCode'] = 'powerSaving'
      increaseCapacity: _typing.ClassVar['ReasonCode'] = 'increaseCapacity'
      checkResource: _typing.ClassVar['ReasonCode'] = 'checkResource'
      unreservedCapacity: _typing.ClassVar['ReasonCode'] = 'unreservedCapacity'
      colocateCommunicatingVM: _typing.ClassVar['ReasonCode'] = 'colocateCommunicatingVM'
      balanceNetworkBandwidthUsage: _typing.ClassVar['ReasonCode'] = 'balanceNetworkBandwidthUsage'
      vmHostHardAffinity: _typing.ClassVar['ReasonCode'] = 'vmHostHardAffinity'
      vmHostSoftAffinity: _typing.ClassVar['ReasonCode'] = 'vmHostSoftAffinity'
      increaseAllocation: _typing.ClassVar['ReasonCode'] = 'increaseAllocation'
      balanceDatastoreSpaceUsage: _typing.ClassVar['ReasonCode'] = 'balanceDatastoreSpaceUsage'
      balanceDatastoreIOLoad: _typing.ClassVar['ReasonCode'] = 'balanceDatastoreIOLoad'
      balanceDatastoreIOPSReservation: _typing.ClassVar['ReasonCode'] = 'balanceDatastoreIOPSReservation'
      datastoreMaint: _typing.ClassVar['ReasonCode'] = 'datastoreMaint'
      virtualDiskJointAffin: _typing.ClassVar['ReasonCode'] = 'virtualDiskJointAffin'
      virtualDiskAntiAffin: _typing.ClassVar['ReasonCode'] = 'virtualDiskAntiAffin'
      datastoreSpaceOutage: _typing.ClassVar['ReasonCode'] = 'datastoreSpaceOutage'
      storagePlacement: _typing.ClassVar['ReasonCode'] = 'storagePlacement'
      iolbDisabledInternal: _typing.ClassVar['ReasonCode'] = 'iolbDisabledInternal'
      xvmotionPlacement: _typing.ClassVar['ReasonCode'] = 'xvmotionPlacement'
      networkBandwidthReservation: _typing.ClassVar['ReasonCode'] = 'networkBandwidthReservation'
      hostInDegradation: _typing.ClassVar['ReasonCode'] = 'hostInDegradation'
      hostExitDegradation: _typing.ClassVar['ReasonCode'] = 'hostExitDegradation'
      maxVmsConstraint: _typing.ClassVar['ReasonCode'] = 'maxVmsConstraint'
      ftConstraints: _typing.ClassVar['ReasonCode'] = 'ftConstraints'
      vmHostAffinityPolicy: _typing.ClassVar['ReasonCode'] = 'vmHostAffinityPolicy'
      vmHostAntiAffinityPolicy: _typing.ClassVar['ReasonCode'] = 'vmHostAntiAffinityPolicy'
      vmAntiAffinityPolicy: _typing.ClassVar['ReasonCode'] = 'vmAntiAffinityPolicy'
      balanceVsanUsage: _typing.ClassVar['ReasonCode'] = 'balanceVsanUsage'
      ahPlacementOptimization: _typing.ClassVar['ReasonCode'] = 'ahPlacementOptimization'
      vmxUpgrade: _typing.ClassVar['ReasonCode'] = 'vmxUpgrade'

   key: str
   type: str
   time: _datetime.datetime
   rating: int
   reason: str
   reasonText: str
   warningText: _typing.Optional[str] = None
   warningDetails: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None
   prerequisite: list[str] = []
   action: list[Action] = []
   target: _typing.Optional[pyVmomi.VmomiSupport.ManagedObject] = None


class ResourceUsageSummary(pyVmomi.vmodl.DynamicData):
   cpuUsedMHz: int
   cpuCapacityMHz: int
   memUsedMB: int
   memCapacityMB: int
   pMemAvailableMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   pMemCapacityMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   storageUsedMB: pyVmomi.VmomiSupport.long
   storageCapacityMB: pyVmomi.VmomiSupport.long


class RuleInfo(pyVmomi.vmodl.DynamicData):
   key: _typing.Optional[int] = None
   status: _typing.Optional[pyVmomi.vim.ManagedEntity.Status] = None
   enabled: _typing.Optional[bool] = None
   name: _typing.Optional[str] = None
   mandatory: _typing.Optional[bool] = None
   userCreated: _typing.Optional[bool] = None
   inCompliance: _typing.Optional[bool] = None
   ruleUuid: _typing.Optional[str] = None


class RuleSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   info: _typing.Optional[RuleInfo] = None


class SiteFaultDomain(pyVmomi.vmodl.DynamicData):
   hosts: list[pyVmomi.vim.HostSystem] = []
   name: str


class SiteFaultDomainConfig(pyVmomi.vmodl.DynamicData):
   siteFaultDomains: list[SiteFaultDomain] = []


class SlotPolicy(pyVmomi.vmodl.DynamicData):
   pass


class StorageComplianceResult(pyVmomi.vmodl.DynamicData):
   class StorageComplianceStatus(pyVmomi.VmomiSupport.Enum):
      compliant: _typing.ClassVar['StorageComplianceStatus'] = 'compliant'
      nonCompliant: _typing.ClassVar['StorageComplianceStatus'] = 'nonCompliant'
      unknown: _typing.ClassVar['StorageComplianceStatus'] = 'unknown'
      notApplicable: _typing.ClassVar['StorageComplianceStatus'] = 'notApplicable'

   checkTime: _typing.Optional[_datetime.datetime] = None
   profile: _typing.Optional[str] = None
   objectUUID: _typing.Optional[str] = None
   complianceStatus: str
   mismatch: bool
   violatedPolicies: list[StoragePolicyStatus] = []
   operationalStatus: _typing.Optional[StorageOperationalStatus] = None
   objPolicyGenerationId: _typing.Optional[str] = None


class StorageOperationalStatus(pyVmomi.vmodl.DynamicData):
   healthy: _typing.Optional[bool] = None
   operationETA: _typing.Optional[_datetime.datetime] = None
   operationProgress: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   transitional: _typing.Optional[bool] = None


class StoragePolicyStatus(pyVmomi.vmodl.DynamicData):
   id: _typing.Optional[str] = None
   expectedValue: _typing.Optional[str] = None
   currentValue: _typing.Optional[str] = None


class SystemVMsConfigInfo(pyVmomi.vmodl.DynamicData):
   class DeploymentMode(pyVmomi.VmomiSupport.Enum):
      SYSTEM_MANAGED: _typing.ClassVar['DeploymentMode'] = 'SYSTEM_MANAGED'
      ABSENT: _typing.ClassVar['DeploymentMode'] = 'ABSENT'

   allowedDatastores: list[pyVmomi.vim.Datastore] = []
   notAllowedDatastores: list[pyVmomi.vim.Datastore] = []
   dsTagCategoriesToExclude: list[str] = []
   deploymentMode: _typing.Optional[str] = None


class SystemVMsConfigSpec(pyVmomi.vmodl.DynamicData):
   allowedDatastores: list[DatastoreUpdateSpec] = []
   notAllowedDatastores: list[DatastoreUpdateSpec] = []
   dsTagCategoriesToExclude: list[TagCategoryUpdateSpec] = []
   deploymentMode: _typing.Optional[str] = None


class TagCategoryUpdateSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   category: _typing.Optional[str] = None


class UsageSummary(pyVmomi.vmodl.DynamicData):
   totalCpuCapacityMhz: int
   totalMemCapacityMB: int
   cpuReservationMhz: int
   memReservationMB: int
   poweredOffCpuReservationMhz: _typing.Optional[int] = None
   poweredOffMemReservationMB: _typing.Optional[int] = None
   cpuDemandMhz: int
   memDemandMB: int
   statsGenNumber: pyVmomi.VmomiSupport.long
   cpuEntitledMhz: int
   memEntitledMB: int
   poweredOffVmCount: int
   totalVmCount: int
   tier0MemCapacityMB: _typing.Optional[int] = None
   reservedTier0MemMB: _typing.Optional[int] = None
   unreservedTier0MemMB: _typing.Optional[int] = None


class VSANPreferredFaultDomainInfo(pyVmomi.vmodl.DynamicData):
   preferredFaultDomainName: _typing.Optional[str] = None
   preferredFaultDomainId: _typing.Optional[str] = None


class VSANStretchedClusterCapability(pyVmomi.vmodl.DynamicData):
   hostMoId: str
   connStatus: _typing.Optional[str] = None
   isSupported: _typing.Optional[bool] = None
   hostCapability: _typing.Optional[pyVmomi.vim.host.VSANStretchedClusterHostCapability] = None


class VSANStretchedClusterFaultDomainConfig(pyVmomi.vmodl.DynamicData):
   firstFdName: str
   firstFdHosts: list[pyVmomi.vim.HostSystem] = []
   secondFdName: str
   secondFdHosts: list[pyVmomi.vim.HostSystem] = []


class VSANStretchedClusterHostVirtualApplianceStatus(pyVmomi.vmodl.DynamicData):
   vcCluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource] = None
   isVirtualApp: _typing.Optional[bool] = None
   vcClusters: list[pyVmomi.vim.ClusterComputeResource] = []
   isVirtualAppValid: _typing.Optional[bool] = None


class VSANWitnessHostInfo(pyVmomi.vmodl.DynamicData):
   nodeUuid: str
   faultDomainName: _typing.Optional[str] = None
   preferredFdName: _typing.Optional[str] = None
   preferredFdUuid: _typing.Optional[str] = None
   unicastAgentAddr: _typing.Optional[str] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   metadataMode: _typing.Optional[bool] = None


class VmComponentProtectionSettings(pyVmomi.vmodl.DynamicData):
   class StorageVmReaction(pyVmomi.VmomiSupport.Enum):
      disabled: _typing.ClassVar['StorageVmReaction'] = 'disabled'
      warning: _typing.ClassVar['StorageVmReaction'] = 'warning'
      restartConservative: _typing.ClassVar['StorageVmReaction'] = 'restartConservative'
      restartAggressive: _typing.ClassVar['StorageVmReaction'] = 'restartAggressive'
      clusterDefault: _typing.ClassVar['StorageVmReaction'] = 'clusterDefault'

   class VmReactionOnAPDCleared(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['VmReactionOnAPDCleared'] = 'none'
      reset: _typing.ClassVar['VmReactionOnAPDCleared'] = 'reset'
      useClusterDefault: _typing.ClassVar['VmReactionOnAPDCleared'] = 'useClusterDefault'

   vmStorageProtectionForAPD: _typing.Optional[str] = None
   enableAPDTimeoutForHosts: _typing.Optional[bool] = None
   vmTerminateDelayForAPDSec: _typing.Optional[int] = None
   vmReactionOnAPDCleared: _typing.Optional[str] = None
   vmStorageProtectionForPDL: _typing.Optional[str] = None


class VmGroup(GroupInfo):
   vm: list[pyVmomi.vim.VirtualMachine] = []


class VmHostRuleInfo(RuleInfo):
   vmGroupName: _typing.Optional[str] = None
   affineHostGroupName: _typing.Optional[str] = None
   antiAffineHostGroupName: _typing.Optional[str] = None


class VmOrchestrationInfo(pyVmomi.vmodl.DynamicData):
   vm: pyVmomi.vim.VirtualMachine
   vmReadiness: VmReadiness


class VmOrchestrationSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   info: _typing.Optional[VmOrchestrationInfo] = None


class VmReadiness(pyVmomi.vmodl.DynamicData):
   class ReadyCondition(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['ReadyCondition'] = 'none'
      poweredOn: _typing.ClassVar['ReadyCondition'] = 'poweredOn'
      guestHbStatusGreen: _typing.ClassVar['ReadyCondition'] = 'guestHbStatusGreen'
      appHbStatusGreen: _typing.ClassVar['ReadyCondition'] = 'appHbStatusGreen'
      useClusterDefault: _typing.ClassVar['ReadyCondition'] = 'useClusterDefault'

   readyCondition: _typing.Optional[str] = None
   postReadyDelay: _typing.Optional[int] = None


class VmToolsMonitoringSettings(pyVmomi.vmodl.DynamicData):
   enabled: _typing.Optional[bool] = None
   vmMonitoring: _typing.Optional[str] = None
   clusterSettings: _typing.Optional[bool] = None
   failureInterval: _typing.Optional[int] = None
   minUpTime: _typing.Optional[int] = None
   maxFailures: _typing.Optional[int] = None
   maxFailureWindow: _typing.Optional[int] = None


class VsanAttachToSrOperation(pyVmomi.vmodl.DynamicData):
   task: _typing.Optional[pyVmomi.vim.Task] = None
   success: _typing.Optional[bool] = None
   timestamp: _typing.Optional[_datetime.datetime] = None
   srNumber: str

class VsanBaselinePreferenceType:
   pass


class VsanCapability(pyVmomi.vmodl.DynamicData):
   target: _typing.Optional[pyVmomi.VmomiSupport.ManagedObject] = None
   capabilities: list[str] = []
   statuses: list[str] = []

class VsanCapabilityStatus:
   pass


class VsanCapabilitySystem(pyVmomi.VmomiSupport.ManagedObject):
   def GetCapabilities(self, targets: list[pyVmomi.VmomiSupport.ManagedObject]) -> list[VsanCapability]: ...

class VsanCapabilityType:
   pass

class VsanCapabilityType90:
   pass

class VsanCapabilityType91:
   pass


class VsanClientServerHciMeshDitEncryptionHealthSummary(pyVmomi.vmodl.DynamicData):
   clusterUuid: str
   clusterName: str
   ownerVc: _typing.Optional[str] = None
   isLocalOwnerVc: _typing.Optional[bool] = None
   health: str
   issues: list[str] = []


class VsanClusterAdvCfgSyncHostResult(pyVmomi.vmodl.DynamicData):
   hostname: str
   value: str
   isDefault: _typing.Optional[bool] = None


class VsanClusterAdvCfgSyncResult(pyVmomi.vmodl.DynamicData):
   inSync: bool
   name: str
   hostValues: list[VsanClusterAdvCfgSyncHostResult] = []


class VsanClusterBalancePerDiskInfo(pyVmomi.vmodl.DynamicData):
   uuid: _typing.Optional[str] = None
   fullness: pyVmomi.VmomiSupport.long
   variance: pyVmomi.VmomiSupport.long
   fullnessAboveThreshold: pyVmomi.VmomiSupport.long
   dataToMoveB: pyVmomi.VmomiSupport.long
   compFullness: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   compVariance: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanClusterBalanceSummary(pyVmomi.vmodl.DynamicData):
   varianceThreshold: pyVmomi.VmomiSupport.long
   disks: list[VsanClusterBalancePerDiskInfo] = []


class VsanClusterClomdLivenessResult(pyVmomi.vmodl.DynamicData):
   clomdLivenessResult: list[VsanHostClomdLivenessResult] = []
   issueFound: bool


class VsanClusterConfig(pyVmomi.vmodl.DynamicData):
   config: pyVmomi.vim.vsan.cluster.ConfigInfo
   name: str
   hosts: list[str] = []
   toBeDeleted: _typing.Optional[bool] = None


class VsanClusterCreateVmHealthTestResult(pyVmomi.vmodl.DynamicData):
   clusterResult: VsanClusterProactiveTestResult
   hostResults: list[VsanHostCreateVmHealthTestResult] = []


class VsanClusterDitEncryptionHealthSummary(pyVmomi.vmodl.DynamicData):
   overallHealth: str
   enabled: _typing.Optional[bool] = None
   hostResults: list[pyVmomi.vim.host.VsanDitEncryptionHealthSummary] = []


class VsanClusterEncryptionHealthSummary(pyVmomi.vmodl.DynamicData):
   overallHealth: _typing.Optional[str] = None
   configHealth: _typing.Optional[str] = None
   kmsHealth: _typing.Optional[str] = None
   vcKmsResult: _typing.Optional[VsanVcKmipServersHealth] = None
   hostResults: list[pyVmomi.vim.host.VsanEncryptionHealthSummary] = []
   aesniHealth: _typing.Optional[str] = None


class VsanClusterFileServiceHealthSummary(pyVmomi.vmodl.DynamicData):
   overallHealth: _typing.Optional[str] = None
   hostResults: list[pyVmomi.vim.host.VsanFileServiceHealthSummary] = []


class VsanClusterGlobalDedupHealthSummary(pyVmomi.vmodl.DynamicData):
   dedupConfigHealth: list[pyVmomi.vim.host.VsanHostGlobalDedupConfigHealthSummary] = []
   dedupStoreHealth: _typing.Optional[str] = None


class VsanClusterHciMeshDitEncryptionHealthSummary(pyVmomi.vmodl.DynamicData):
   overallHealth: str
   hostClientClusterSummary: list[pyVmomi.vim.host.VsanHostHciMeshDitEncryptionHealthSummary] = []
   hostServerClusterSummary: list[pyVmomi.vim.host.VsanHostHciMeshDitEncryptionHealthSummary] = []
   serverClusterSummary: list[VsanClientServerHciMeshDitEncryptionHealthSummary] = []


class VsanClusterHclInfo(pyVmomi.vmodl.DynamicData):
   hclDbLastUpdate: _typing.Optional[_datetime.datetime] = None
   hclDbAgeHealth: _typing.Optional[str] = None
   hostResults: list[pyVmomi.vim.host.VsanHostHclInfo] = []
   updateItems: list[pyVmomi.vim.vsan.VsanUpdateItem] = []
   hclDbAbsent: _typing.Optional[bool] = None


class VsanClusterHealthAction(pyVmomi.vmodl.DynamicData):
   class VsanClusterHealthActionIdEnum(pyVmomi.VmomiSupport.Enum):
      RepairClusterObjectsAction: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'RepairClusterObjectsAction'
      UploadHclDb: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'UploadHclDb'
      UpdateHclDbFromInternet: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'UpdateHclDbFromInternet'
      EnableHealthService: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'EnableHealthService'
      DiskBalance: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'DiskBalance'
      StopDiskBalance: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'StopDiskBalance'
      RemediateDedup: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateDedup'
      UpgradeVsanDiskFormat: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'UpgradeVsanDiskFormat'
      CreateDVS: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'CreateDVS'
      ConfigureHA: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'ConfigureHA'
      ConfigureDRS: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'ConfigureDRS'
      ConfigureVSAN: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'ConfigureVSAN'
      ClaimVSANDisks: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'ClaimVSANDisks'
      ClusterUpgrade: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'ClusterUpgrade'
      CreateVMKnic: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'CreateVMKnic'
      CreateVMKnicWithVMotion: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'CreateVMKnicWithVMotion'
      RunBurnInTest: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'RunBurnInTest'
      EnableIscsiTargetService: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'EnableIscsiTargetService'
      EnablePerformanceServiceAction: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'EnablePerformanceServiceAction'
      RemediateClusterConfig: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateClusterConfig'
      EnableCeip: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'EnableCeip'
      LoginVumIsoDepot: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'LoginVumIsoDepot'
      PurgeInaccessSwapObjs: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'PurgeInaccessSwapObjs'
      UploadReleaseCatalog: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'UploadReleaseCatalog'
      ConfigureAutomaticRebalance: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'ConfigureAutomaticRebalance'
      RemediateFileService: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateFileService'
      RelayoutVsanObjects: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'RelayoutVsanObjects'
      RemediateFileServiceImbalance: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateFileServiceImbalance'
      SelectNvme: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'SelectNvme'
      CreateFileServiceDomain: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'CreateFileServiceDomain'
      RemediateIscsiLunsRuntimeStatus: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'RemediateIscsiLunsRuntimeStatus'
      ShallowRekey: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'ShallowRekey'
      VsanClusterHealthActionIdEnum_Unknown: _typing.ClassVar['VsanClusterHealthActionIdEnum'] = 'VsanClusterHealthActionIdEnum_Unknown'

   actionId: str
   actionLabel: pyVmomi.vmodl.LocalizableMessage
   actionDescription: pyVmomi.vmodl.LocalizableMessage
   enabled: bool
   parameters: list[pyVmomi.vim.KeyValue] = []

class VsanClusterHealthCategoryEnum:
   pass


class VsanClusterHealthCheckInfo(pyVmomi.vmodl.DynamicData):
   testId: str
   testName: _typing.Optional[str] = None
   groupId: str
   groupName: _typing.Optional[str] = None


class VsanClusterHealthConfigs(pyVmomi.vmodl.DynamicData):
   enableVsanTelemetry: _typing.Optional[bool] = None
   vsanTelemetryInterval: _typing.Optional[int] = None
   vsanTelemetryProxy: _typing.Optional[VsanClusterTelemetryProxyConfig] = None
   configs: list[VsanClusterHealthResultKeyValuePair] = []


class VsanClusterHealthExternalLink(VsanClusterHealthLinkBase):
   url: str
   category: _typing.Optional[str] = None


class VsanClusterHealthGroup(pyVmomi.vmodl.DynamicData):
   groupId: str
   groupName: str
   groupHealth: str
   groupTests: list[VsanClusterHealthTest] = []
   groupDetails: list[VsanClusterHealthResultBase] = []
   inProgress: _typing.Optional[bool] = None


class VsanClusterHealthLinkBase(pyVmomi.vmodl.DynamicData):
   label: _typing.Optional[str] = None


class VsanClusterHealthQuerySpec(pyVmomi.vmodl.DynamicData):
   task: _typing.Optional[pyVmomi.vim.Task] = None
   diskNames: list[str] = []
   includeHealthRemediation: _typing.Optional[bool] = None
   excludeChecks: list[str] = []


class VsanClusterHealthResultBase(pyVmomi.vmodl.DynamicData):
   label: _typing.Optional[str] = None


class VsanClusterHealthResultColumnInfo(pyVmomi.vmodl.DynamicData):
   label: str
   type: str


class VsanClusterHealthResultKeyValuePair(pyVmomi.vmodl.DynamicData):
   key: _typing.Optional[str] = None
   value: _typing.Optional[str] = None


class VsanClusterHealthResultRow(pyVmomi.vmodl.DynamicData):
   values: list[str] = []
   nestedRows: list[VsanClusterHealthResultRow] = []
   actions: list[VsanHealthDataDrivenAction] = []


class VsanClusterHealthResultTable(VsanClusterHealthResultBase):
   columns: list[VsanClusterHealthResultColumnInfo] = []
   rows: list[VsanClusterHealthResultRow] = []


class VsanClusterHealthResultWithRemediation(VsanClusterHealthResultBase):
   issueDescription: _typing.Optional[str] = None
   issueDetail: list[VsanClusterHealthResultTable] = []
   troubleshooting: _typing.Optional[VsanHealthTroubleshooting] = None
   additionalResources: list[VsanClusterHealthExternalLink] = []


class VsanClusterHealthSummary(pyVmomi.vmodl.DynamicData):
   clusterStatus: _typing.Optional[VsanClusterHealthSystemStatusResult] = None
   timestamp: _typing.Optional[_datetime.datetime] = None
   clusterVersions: _typing.Optional[VsanClusterHealthSystemVersionResult] = None
   objectHealth: _typing.Optional[pyVmomi.vim.host.VsanObjectOverallHealth] = None
   vmHealth: _typing.Optional[VsanClusterVMsHealthOverallResult] = None
   networkHealth: _typing.Optional[VsanClusterNetworkHealthResult] = None
   limitHealth: _typing.Optional[VsanClusterLimitHealthResult] = None
   advCfgSync: list[VsanClusterAdvCfgSyncResult] = []
   createVmHealth: list[VsanHostCreateVmHealthTestResult] = []
   physicalDisksHealth: list[pyVmomi.vim.host.VsanPhysicalDiskHealthSummary] = []
   encryptionHealth: _typing.Optional[VsanClusterEncryptionHealthSummary] = None
   hclInfo: _typing.Optional[VsanClusterHclInfo] = None
   groups: list[VsanClusterHealthGroup] = []
   overallHealth: str
   overallHealthDescription: str
   clomdLiveness: _typing.Optional[VsanClusterClomdLivenessResult] = None
   diskBalance: _typing.Optional[VsanClusterBalanceSummary] = None
   genericCluster: _typing.Optional[pyVmomi.vim.vsan.VsanGenericClusterBestPracticeHealth] = None
   networkConfig: _typing.Optional[pyVmomi.vim.vsan.VsanNetworkConfigBestPracticeHealth] = None
   vsanConfig: _typing.Optional[pyVmomi.vim.vsan.VsanConfigCheckResult] = None
   burnInTest: _typing.Optional[pyVmomi.vim.vsan.VsanBurnInTestCheckResult] = None
   perfsvcHealth: _typing.Optional[pyVmomi.vim.vsan.VsanPerfsvcHealthResult] = None
   cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource] = None
   fileServiceHealth: _typing.Optional[VsanClusterFileServiceHealthSummary] = None
   ditEncryptionHealth: _typing.Optional[VsanClusterDitEncryptionHealthSummary] = None
   healthScore: _typing.Optional[int] = None
   globalDedupHealth: _typing.Optional[VsanClusterGlobalDedupHealthSummary] = None
   hciMeshDitEncryptionHealth: _typing.Optional[VsanClusterHciMeshDitEncryptionHealthSummary] = None
   healthStatusCounts: _typing.Optional[VsanHealthStatusCounts] = None


class VsanClusterHealthSystem(pyVmomi.VmomiSupport.ManagedObject):
   def QueryVerifyClusterNetworkSettings(self, hosts: list[str], esxRootPassword: str) -> VsanClusterNetworkHealthResult: ...
   def QueryCheckLimits(self, hosts: list[str], esxRootPassword: str) -> VsanClusterLimitHealthResult: ...
   def QueryPhysicalDiskHealthSummary(self, hosts: list[str], esxRootPassword: str) -> list[pyVmomi.vim.host.VsanPhysicalDiskHealthSummary]: ...
   def QueryAdvCfgSync(self, hosts: list[str], esxRootPassword: str, options: list[str]) -> list[VsanClusterAdvCfgSyncResult]: ...
   def QueryClusterCreateVmHealthTest(self, hosts: list[str], esxRootPassword: str, timeout: int) -> VsanClusterCreateVmHealthTestResult: ...
   def QueryClusterNetworkPerfTest(self, hosts: list[str], esxRootPassword: str, multicast: bool, durationSec: _typing.Optional[int]) -> VsanClusterNetworkLoadTestResult: ...
   def QueryCaptureVsanPcap(self, hosts: list[str], esxRootPassword: str, duration: int, vmknic: list[VsanClusterHostVmknicMapping], includeRawPcap: _typing.Optional[bool], includeIgmp: _typing.Optional[bool], cmmdsMsgTypeFilter: list[str], cmmdsPorts: list[int], clusterUuid: _typing.Optional[str]) -> VsanVsanClusterPcapResult: ...
   def QueryClusterHealthSystemVersions(self, hosts: list[str], esxRootPassword: str) -> VsanClusterHealthSystemVersionResult: ...
   def CheckClusterClomdLiveness(self, hosts: list[str], esxRootPassword: str) -> VsanClusterClomdLivenessResult: ...
   def RepairClusterImmediateObjects(self, hosts: list[str], esxRootPassword: str, uuids: list[str]) -> VsanClusterHealthSystemObjectsRepairResult: ...
   def GetClusterHclInfo(self, hosts: list[str], esxRootPassword: str) -> VsanClusterHclInfo: ...


class VsanClusterHealthSystemObjectsRepairResult(pyVmomi.vmodl.DynamicData):
   inRepairingQueueObjects: list[str] = []
   failedRepairObjects: list[pyVmomi.vim.host.VsanFailedRepairObjectResult] = []
   issueFound: bool


class VsanClusterHealthSystemStatusResult(pyVmomi.vmodl.DynamicData):
   status: str
   goalState: str
   untrackedHosts: list[str] = []
   trackedHostsStatus: list[pyVmomi.vim.host.VsanHostHealthSystemStatusResult] = []


class VsanClusterHealthSystemVersionResult(pyVmomi.vmodl.DynamicData):
   hostResults: list[VsanHostHealthSystemVersionResult] = []
   vcVersion: _typing.Optional[str] = None
   issueFound: bool
   upgradePossible: _typing.Optional[bool] = None
   vcBuild: _typing.Optional[str] = None


class VsanClusterHealthTest(pyVmomi.vmodl.DynamicData):
   testId: _typing.Optional[str] = None
   testName: _typing.Optional[str] = None
   testDescription: _typing.Optional[str] = None
   testShortDescription: _typing.Optional[str] = None
   testHealthyEntities: _typing.Optional[int] = None
   testAllEntities: _typing.Optional[int] = None
   testHealth: _typing.Optional[str] = None
   testDetails: list[VsanClusterHealthResultBase] = []
   testActions: list[VsanClusterHealthAction] = []
   historicalResults: list[VsanHistoricalHealthTest] = []
   testCorrelation: _typing.Optional[VsanHealthCorrelation] = None
   reducedScore: _typing.Optional[int] = None
   category: _typing.Optional[str] = None
   riskIfNotFix: _typing.Optional[str] = None
   lastStatusChangeTime: _typing.Optional[_datetime.datetime] = None


class VsanClusterHostVmknicMapping(pyVmomi.vmodl.DynamicData):
   host: str
   vmknic: str


class VsanClusterLimitHealthResult(pyVmomi.vmodl.DynamicData):
   issueFound: bool
   componentLimitHealth: str
   diskFreeSpaceHealth: str
   rcFreeReservationHealth: str
   hostResults: list[pyVmomi.vim.host.VsanLimitHealthResult] = []
   whatifHostFailures: list[VsanClusterWhatifHostFailuresResult] = []
   hostsCommFailure: list[str] = []


class VsanClusterMgmtInternalSystem(pyVmomi.VmomiSupport.ManagedObject):
   def RemediateVsanCluster(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task: ...
   def RemediateVsanHost(self, host: pyVmomi.vim.HostSystem) -> pyVmomi.vim.Task: ...


class VsanClusterNetworkHealthResult(pyVmomi.vmodl.DynamicData):
   hostResults: list[pyVmomi.vim.host.VsanNetworkHealthResult] = []
   issueFound: _typing.Optional[bool] = None
   vsanVmknicPresent: _typing.Optional[bool] = None
   matchingMulticastConfig: _typing.Optional[bool] = None
   matchingIpSubnets: _typing.Optional[bool] = None
   pingTestSuccess: _typing.Optional[bool] = None
   largePingTestSuccess: _typing.Optional[bool] = None
   hostLatencyCheckSuccess: _typing.Optional[bool] = None
   potentialMulticastIssue: _typing.Optional[bool] = None
   otherHostsInVsanCluster: list[str] = []
   partitions: list[VsanClusterNetworkPartitionInfo] = []
   hostsWithVsanDisabled: list[str] = []
   hostsDisconnected: list[str] = []
   hostsCommFailure: list[str] = []
   hostsInEsxMaintenanceMode: list[str] = []
   hostsInVsanMaintenanceMode: list[str] = []
   infoAboutUnexpectedHosts: list[pyVmomi.vim.host.VsanQueryResultHostInfo] = []
   clusterInUnicastMode: _typing.Optional[bool] = None
   clusterInRDMAMode: _typing.Optional[bool] = None


class VsanClusterNetworkLoadTestResult(pyVmomi.vmodl.DynamicData):
   clusterResult: VsanClusterProactiveTestResult
   hostResults: list[pyVmomi.vim.host.VsanNetworkLoadTestResult] = []


class VsanClusterNetworkPartitionInfo(pyVmomi.vmodl.DynamicData):
   hosts: list[str] = []
   partitionUnknown: _typing.Optional[bool] = None


class VsanClusterNetworkPerfTaskSpec(pyVmomi.vmodl.DynamicData):
   Cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource] = None
   DurationSec: _typing.Optional[int] = None
   ownerVc: _typing.Optional[str] = None


class VsanClusterPowerSystem(pyVmomi.VmomiSupport.ManagedObject):
   def PerformClusterPowerAction(self, cluster: pyVmomi.vim.ComputeResource, spec: PerformClusterPowerActionSpec) -> pyVmomi.vim.Task: ...
   def QueryClusterPowerContext(self, cluster: pyVmomi.vim.ComputeResource) -> ClusterPowerContext: ...
   def UpdateClusterPowerStatus(self, cluster: pyVmomi.vim.ComputeResource, status: str) -> bool: ...


class VsanClusterProactiveTestResult(pyVmomi.vmodl.DynamicData):
   overallStatus: str
   overallStatusDescription: str
   timestamp: _datetime.datetime
   healthTest: _typing.Optional[VsanClusterHealthTest] = None


class VsanClusterTelemetryProxyConfig(pyVmomi.vmodl.DynamicData):
   host: _typing.Optional[str] = None
   port: _typing.Optional[int] = None
   user: _typing.Optional[str] = None
   password: _typing.Optional[str] = None
   autoDiscovered: _typing.Optional[bool] = None


class VsanClusterVMsHealthOverallResult(pyVmomi.vmodl.DynamicData):
   healthStateList: list[VsanClusterVMsHealthSummaryResult] = []
   overallHealthState: _typing.Optional[str] = None


class VsanClusterVMsHealthSummaryResult(pyVmomi.vmodl.DynamicData):
   numVMs: int
   state: _typing.Optional[str] = None
   health: str
   vmInstanceUuids: list[str] = []


class VsanClusterVmdkLoadTestResult(pyVmomi.vmodl.DynamicData):
   task: _typing.Optional[pyVmomi.vim.Task] = None
   clusterResult: _typing.Optional[VsanClusterProactiveTestResult] = None
   hostResults: list[pyVmomi.vim.host.VsanHostVmdkLoadTestResult] = []


class VsanClusterWhatifHostFailuresResult(pyVmomi.vmodl.DynamicData):
   numFailures: pyVmomi.VmomiSupport.long
   totalUsedCapacityB: pyVmomi.VmomiSupport.long
   totalCapacityB: pyVmomi.VmomiSupport.long
   totalRcReservationB: pyVmomi.VmomiSupport.long
   totalRcSizeB: pyVmomi.VmomiSupport.long
   usedComponents: pyVmomi.VmomiSupport.long
   totalComponents: pyVmomi.VmomiSupport.long
   componentLimitHealth: _typing.Optional[str] = None
   diskFreeSpaceHealth: _typing.Optional[str] = None
   rcFreeReservationHealth: _typing.Optional[str] = None
   slackSpaceCapRequired: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   diskSpaceThreshold: _typing.Optional[pyVmomi.vim.vsan.VsanHealthThreshold] = None
   capacityReservationInfo: _typing.Optional[pyVmomi.vim.vsan.CapacityReservationInfo] = None


class VsanComponentBasicInfo(pyVmomi.vmodl.DynamicData):
   uuid: str
   componentState: str
   hostName: str
   hostNodeUuid: str
   faultDomainUuid: _typing.Optional[str] = None
   faultDomainName: _typing.Optional[str] = None
   cacheDiskInfo: _typing.Optional[pyVmomi.vim.vsan.DiskInfo] = None
   capacityDiskInfo: _typing.Optional[pyVmomi.vim.vsan.DiskInfo] = None


class VsanComponentPlacement(pyVmomi.vmodl.DynamicData):
   type: str
   children: list[VsanComponentPlacement] = []
   basicInfo: _typing.Optional[VsanComponentBasicInfo] = None

class VsanComponentStates:
   pass


class VsanConfigGeneration(pyVmomi.vmodl.DynamicData):
   vcUuid: str
   genNum: pyVmomi.VmomiSupport.long
   genTime: pyVmomi.VmomiSupport.long


class VsanDataDrivenAPIAction(pyVmomi.vmodl.DynamicData):
   actionId: str
   actionLabel: pyVmomi.vmodl.LocalizableMessage
   actionDescription: pyVmomi.vmodl.LocalizableMessage
   enabled: bool
   parameters: list[pyVmomi.vim.KeyValue] = []

class VsanDatastoreType:
   pass


class VsanDiagnosticsSystem(pyVmomi.VmomiSupport.ManagedObject):
   def QueryNetworkDiagnostics(self, cluster: pyVmomi.vim.ComputeResource, host: _typing.Optional[pyVmomi.vim.HostSystem]) -> list[VsanNetworkDiagnostics]: ...
   def GetThresholds(self, cluster: pyVmomi.vim.ComputeResource, entityType: _typing.Optional[str], metric: _typing.Optional[str]) -> list[VsanDiagnosticsThreshold]: ...
   def SetThresholds(self, cluster: pyVmomi.vim.ComputeResource, thresholds: list[VsanDiagnosticsThreshold]) -> None: ...
   def StartIODiagnosticsTask(self, targets: list[pyVmomi.vim.vsan.IODiagnosticsTarget], cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], duration: _typing.Optional[pyVmomi.VmomiSupport.long]) -> pyVmomi.vim.Task: ...
   def QueryIODiagnosticsInstances(self, querySpec: pyVmomi.vim.vsan.IODiagnosticsInstanceQuerySpec, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> list[pyVmomi.vim.vsan.IODiagnosticsInstance]: ...
   def QueryIODiagnosticsStats(self, instanceName: str, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> list[pyVmomi.vim.vsan.IODiagnosticsTargetStats]: ...
   def CreateIOTripAnalyzerRecurrences(self, cluster: pyVmomi.vim.ComputeResource, recurrences: list[pyVmomi.vim.vsan.VsanIOTripAnalyzerRecurrence]) -> list[pyVmomi.vim.vsan.VsanIOTripAnalyzerRecurrence]: ...
   def GetIOTripAnalyzerSchedulerConfig(self, cluster: pyVmomi.vim.ComputeResource) -> _typing.Optional[pyVmomi.vim.vsan.VsanIOTripAnalyzerConfig]: ...
   def EditIOTripAnalyzerRecurrences(self, cluster: pyVmomi.vim.ComputeResource, recurrences: list[pyVmomi.vim.vsan.VsanIOTripAnalyzerRecurrence]) -> list[pyVmomi.vim.vsan.VsanIOTripAnalyzerRecurrence]: ...
   def RemoveIOTripAnalyzerRecurrences(self, cluster: pyVmomi.vim.ComputeResource, names: list[str]) -> None: ...
   def SetTraceObjectPolicy(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], traceObjectUuid: str, profile: _typing.Optional[pyVmomi.vim.vm.ProfileSpec]) -> bool: ...


class VsanDiagnosticsThreshold(pyVmomi.vmodl.DynamicData):
   entityType: str
   metric: str
   yellow: _typing.Optional[int] = None
   red: _typing.Optional[int] = None


class VsanDiskFormatConversionCheckResult(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckResult):
   isSupported: bool
   targetVersion: _typing.Optional[int] = None
   isDataMovementRequired: _typing.Optional[bool] = None
   storagePoolDisk: _typing.Optional[str] = None


class VsanDiskFormatConversionSpec(pyVmomi.vmodl.DynamicData):
   dataEfficiencyConfig: _typing.Optional[pyVmomi.vim.vsan.DataEfficiencyConfig] = None
   dataEncryptionConfig: _typing.Optional[pyVmomi.vim.vsan.DataEncryptionConfig] = None
   skipHostRemediation: _typing.Optional[bool] = None
   allowDataMovement: _typing.Optional[bool] = None


class VsanDiskMappingsConfigSpec(pyVmomi.vmodl.DynamicData):
   hostDiskMappings: list[VsanHostDiskMapping] = []


class VsanEffectiveSpaceUsage(pyVmomi.vmodl.DynamicData):
   totalUsableB: pyVmomi.VmomiSupport.long
   freeUsableB: pyVmomi.VmomiSupport.long
   actualWrittenB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   overReservedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   totalProvisionB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   snapshotSpace: _typing.Optional[VsanSnapshotSpace] = None


class VsanEntitySpaceUsage(pyVmomi.vmodl.DynamicData):
   entityId: _typing.Optional[str] = None
   spaceUsageByObjectType: list[VsanObjectSpaceSummary] = []
   totalCapacityB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   freeCapacityB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   efficientCapacity: _typing.Optional[pyVmomi.vim.vsan.DataEfficiencyCapacityState] = None


class VsanFaultDomainSpec(pyVmomi.vmodl.DynamicData):
   hosts: list[pyVmomi.vim.HostSystem] = []
   name: str


class VsanFaultDomainsConfigSpec(pyVmomi.vmodl.DynamicData):
   faultDomains: list[VsanFaultDomainSpec] = []
   witness: _typing.Optional[VsanWitnessSpec] = None

class VsanHciMeshDitEncryptionIssue:
   pass


class VsanHealthActionBase(pyVmomi.vmodl.DynamicData):
   description: str


class VsanHealthActionSteps(VsanHealthActionBase):
   steps: list[VsanHealthActionBase] = []

class VsanHealthApiBasedAction(VsanHealthActionBase):
   apiAction: VsanClusterHealthAction

class VsanHealthCmdBasedAction(VsanHealthActionBase):
   commands: list[str] = []


class VsanHealthConfirmationDialog(pyVmomi.vmodl.DynamicData):
   title: str
   subTitle: _typing.Optional[str] = None
   content: str
   agreeLabel: _typing.Optional[str] = None
   closeLabel: _typing.Optional[str] = None
   isWarning: _typing.Optional[bool] = None


class VsanHealthCorrelation(pyVmomi.vmodl.DynamicData):
   primaryHealthTests: list[str] = []
   relatedHealthTests: list[str] = []
   skippedHealthTests: list[str] = []


class VsanHealthDataDrivenAction(VsanHealthActionBase):
   apiAction: VsanDataDrivenAPIAction
   confirmation: _typing.Optional[VsanHealthConfirmationDialog] = None


class VsanHealthExtMgmtPreCheckResult(pyVmomi.vmodl.DynamicData):
   overallResult: bool
   esxVersionCheckPassed: _typing.Optional[bool] = None
   drsCheckPassed: _typing.Optional[bool] = None
   eamConnectionCheckPassed: _typing.Optional[bool] = None
   installStateCheckPassed: _typing.Optional[bool] = None
   results: list[VsanClusterHealthTest] = []
   vumRegistered: _typing.Optional[bool] = None


class VsanHealthStatusCounts(pyVmomi.vmodl.DynamicData):
   error: int
   warning: int
   info: int


class VsanHealthTroubleshooting(pyVmomi.vmodl.DynamicData):
   diagnosticSteps: list[VsanHealthActionBase] = []
   remediations: list[VsanHealthActionBase] = []

class VsanHealthTxtBasedAction(VsanHealthActionBase):
   pass


class VsanHistoricalHealthQuerySpec(pyVmomi.vmodl.DynamicData):
   clusters: list[pyVmomi.vim.ClusterComputeResource] = []
   start: _datetime.datetime
   end: _typing.Optional[_datetime.datetime] = None
   testId: _typing.Optional[str] = None
   groupId: _typing.Optional[str] = None
   includeHealthRemediation: _typing.Optional[bool] = None


class VsanHistoricalHealthTest(pyVmomi.vmodl.DynamicData):
   timestamp: _datetime.datetime
   health: str
   testDetails: list[VsanClusterHealthResultBase] = []
   testCorrelation: _typing.Optional[VsanHealthCorrelation] = None


class VsanHostClomdLivenessResult(pyVmomi.vmodl.DynamicData):
   hostname: str
   clomdStat: str
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VsanHostCreateVmHealthTestResult(pyVmomi.vmodl.DynamicData):
   hostname: str
   state: str
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VsanHostDiskMapping(pyVmomi.vmodl.DynamicData):
   class VsanDiskGroupCreationType(pyVmomi.VmomiSupport.Enum):
      allflash: _typing.ClassVar['VsanDiskGroupCreationType'] = 'allflash'
      hybrid: _typing.ClassVar['VsanDiskGroupCreationType'] = 'hybrid'
      vsandirect: _typing.ClassVar['VsanDiskGroupCreationType'] = 'vsandirect'
      pmem: _typing.ClassVar['VsanDiskGroupCreationType'] = 'pmem'
      VsanDiskGroupCreationType_Unknown: _typing.ClassVar['VsanDiskGroupCreationType'] = 'VsanDiskGroupCreationType_Unknown'

   host: pyVmomi.vim.HostSystem
   cacheDisks: list[pyVmomi.vim.host.ScsiDisk] = []
   capacityDisks: list[pyVmomi.vim.host.ScsiDisk] = []
   type: str


class VsanHostHealthSystemVersionResult(pyVmomi.vmodl.DynamicData):
   hostname: str
   version: _typing.Optional[str] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   build: _typing.Optional[str] = None


class VsanIoInsightInstance(pyVmomi.vmodl.DynamicData):
   runName: str
   state: _typing.Optional[str] = None
   startTime: _typing.Optional[_datetime.datetime] = None
   endTime: _typing.Optional[_datetime.datetime] = None
   hostsIoInsightInfo: list[pyVmomi.vim.host.VsanHostIoInsightInfo] = []
   hostUuids: list[str] = []
   vmUuids: list[str] = []


class VsanIoInsightInstanceQuerySpec(pyVmomi.vmodl.DynamicData):
   state: _typing.Optional[str] = None
   entityRefId: _typing.Optional[str] = None

class VsanIoInsightInstanceState:
   pass


class VsanIoInsightManager(pyVmomi.VmomiSupport.ManagedObject):
   def StartIoInsight(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], runName: _typing.Optional[str], durationSec: _typing.Optional[pyVmomi.VmomiSupport.long], targetHosts: list[pyVmomi.vim.HostSystem], targetVMs: list[pyVmomi.vim.VirtualMachine]) -> pyVmomi.vim.Task: ...
   def StopIoInsight(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], runName: _typing.Optional[str], hostsIoInsightInfos: list[pyVmomi.vim.host.VsanHostIoInsightInfo]) -> pyVmomi.vim.Task: ...
   def QueryIoInsightInstances(self, querySpec: VsanIoInsightInstanceQuerySpec, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> list[VsanIoInsightInstance]: ...
   def DeleteIoInsightInstance(self, runName: str, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> None: ...
   def RenameIoInsightInstance(self, oldRunName: str, newRunName: str, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> None: ...


class VsanIscsiHomeObjectSpec(pyVmomi.vmodl.DynamicData):
   storagePolicy: _typing.Optional[pyVmomi.vim.vm.ProfileSpec] = None
   defaultConfig: _typing.Optional[VsanIscsiTargetServiceDefaultConfigSpec] = None


class VsanIscsiInitiatorGroup(pyVmomi.vmodl.DynamicData):
   name: str
   initiators: list[str] = []
   targets: list[VsanIscsiTargetBasicInfo] = []


class VsanIscsiLUN(VsanIscsiLUNCommonInfo):
   targetAlias: str
   uuid: str
   actualSize: pyVmomi.VmomiSupport.long
   objectInformation: _typing.Optional[VsanObjectInformation] = None


class VsanIscsiLUNCommonInfo(pyVmomi.vmodl.DynamicData):
   class VsanIscsiLUNStatus(pyVmomi.VmomiSupport.Enum):
      Online: _typing.ClassVar['VsanIscsiLUNStatus'] = 'Online'
      Offline: _typing.ClassVar['VsanIscsiLUNStatus'] = 'Offline'
      VsanIscsiLUNStatus_Unknown: _typing.ClassVar['VsanIscsiLUNStatus'] = 'VsanIscsiLUNStatus_Unknown'

   lunId: _typing.Optional[int] = None
   alias: _typing.Optional[str] = None
   lunSize: pyVmomi.VmomiSupport.long
   status: _typing.Optional[str] = None

class VsanIscsiLUNRuntimeStatusType:
   pass


class VsanIscsiLUNSpec(VsanIscsiLUNCommonInfo):
   storagePolicy: _typing.Optional[pyVmomi.vim.vm.ProfileSpec] = None
   newLunId: _typing.Optional[int] = None


class VsanIscsiTarget(VsanIscsiTargetCommonInfo):
   lunCount: _typing.Optional[int] = None
   objectInformation: _typing.Optional[VsanObjectInformation] = None
   ioOwnerHost: _typing.Optional[str] = None
   initiators: list[str] = []
   initiatorGroups: list[str] = []


class VsanIscsiTargetAuthSpec(pyVmomi.vmodl.DynamicData):
   class VsanIscsiTargetAuthType(pyVmomi.VmomiSupport.Enum):
      NoAuth: _typing.ClassVar['VsanIscsiTargetAuthType'] = 'NoAuth'
      CHAP: _typing.ClassVar['VsanIscsiTargetAuthType'] = 'CHAP'
      CHAP_Mutual: _typing.ClassVar['VsanIscsiTargetAuthType'] = 'CHAP_Mutual'
      VsanIscsiTargetAuthType_Unknown: _typing.ClassVar['VsanIscsiTargetAuthType'] = 'VsanIscsiTargetAuthType_Unknown'

   authType: _typing.Optional[str] = None
   userNameAttachToTarget: _typing.Optional[str] = None
   userSecretAttachToTarget: _typing.Optional[str] = None
   userNameAttachToInitiator: _typing.Optional[str] = None
   userSecretAttachToInitiator: _typing.Optional[str] = None


class VsanIscsiTargetBasicInfo(pyVmomi.vmodl.DynamicData):
   alias: str
   iqn: _typing.Optional[str] = None


class VsanIscsiTargetCommonInfo(VsanIscsiTargetBasicInfo):
   authSpec: _typing.Optional[VsanIscsiTargetAuthSpec] = None
   port: _typing.Optional[int] = None
   networkInterface: _typing.Optional[str] = None
   affinityLocation: _typing.Optional[str] = None


class VsanIscsiTargetServiceConfig(pyVmomi.vmodl.DynamicData):
   defaultConfig: _typing.Optional[VsanIscsiTargetServiceDefaultConfigSpec] = None
   enabled: _typing.Optional[bool] = None
   vipConfigs: list[pyVmomi.vim.vsan.VipConfigSpec] = []


class VsanIscsiTargetServiceDefaultConfigSpec(pyVmomi.vmodl.DynamicData):
   networkInterface: _typing.Optional[str] = None
   port: _typing.Optional[int] = None
   iscsiTargetAuthSpec: _typing.Optional[VsanIscsiTargetAuthSpec] = None

class VsanIscsiTargetServiceProcessStatus:
   pass


class VsanIscsiTargetServiceSpec(VsanIscsiTargetServiceConfig):
   homeObjectStoragePolicy: _typing.Optional[pyVmomi.vim.vm.ProfileSpec] = None


class VsanIscsiTargetSpec(VsanIscsiTargetCommonInfo):
   storagePolicy: _typing.Optional[pyVmomi.vim.vm.ProfileSpec] = None
   newAlias: _typing.Optional[str] = None


class VsanIscsiTargetSystem(pyVmomi.VmomiSupport.ManagedObject):
   def QueryIscsiTargetServiceVersion(self) -> str: ...
   def GetHomeObject(self, cluster: pyVmomi.vim.ClusterComputeResource) -> VsanObjectInformation: ...
   def GetIscsiTargets(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[VsanIscsiTarget]: ...
   def GetIscsiTarget(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str) -> _typing.Optional[VsanIscsiTarget]: ...
   def AddIscsiTarget(self, cluster: pyVmomi.vim.ClusterComputeResource, targetSpec: VsanIscsiTargetSpec) -> _typing.Optional[pyVmomi.vim.Task]: ...
   def EditIscsiTarget(self, cluster: pyVmomi.vim.ClusterComputeResource, targetSpec: VsanIscsiTargetSpec) -> _typing.Optional[pyVmomi.vim.Task]: ...
   def RemoveIscsiTarget(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str) -> _typing.Optional[pyVmomi.vim.Task]: ...
   def GetIscsiLUNs(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAliases: list[str]) -> list[VsanIscsiLUN]: ...
   def GetIscsiLUN(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str, lunId: int) -> _typing.Optional[VsanIscsiLUN]: ...
   def AddIscsiLUN(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str, lunSpec: VsanIscsiLUNSpec) -> _typing.Optional[pyVmomi.vim.Task]: ...
   def EditIscsiLUN(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str, lunSpec: VsanIscsiLUNSpec) -> _typing.Optional[pyVmomi.vim.Task]: ...
   def RemoveIscsiLUN(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str, lunId: int) -> _typing.Optional[pyVmomi.vim.Task]: ...
   def AddIscsiInitiatorsToTarget(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str, initiatorNames: list[str]) -> None: ...
   def RemoveIscsiInitiatorsFromTarget(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str, initiatorNames: list[str]) -> None: ...
   def GetIscsiInitiatorGroups(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[VsanIscsiInitiatorGroup]: ...
   def GetIscsiInitiatorGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str) -> _typing.Optional[VsanIscsiInitiatorGroup]: ...
   def AddIscsiInitiatorGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str) -> None: ...
   def RemoveIscsiInitiatorGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str) -> None: ...
   def AddIscsiInitiatorsToGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str, initiatorNames: list[str]) -> None: ...
   def RemoveIscsiInitiatorsFromGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str, initiatorNames: list[str]) -> None: ...
   def AddIscsiTargetToGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str, targetAlias: str) -> None: ...
   def RemoveIscsiTargetFromGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str, targetAlias: str) -> None: ...
   def RemediateIscsiLunsRuntimeStatus(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task: ...


class VsanNetworkDiagnostics(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   eventTypeId: str
   severity: str
   createdTime: _datetime.datetime
   arguments: list[pyVmomi.vmodl.KeyAnyValue] = []


class VsanObjIdentityQuerySpec(pyVmomi.vmodl.DynamicData):
   knownSpbmProfileUuids: list[str] = []
   includeEffectiveCapacity: _typing.Optional[bool] = None


class VsanObjectExtAttrs(pyVmomi.vmodl.DynamicData):
   uuid: str
   objectType: _typing.Optional[str] = None
   objectPath: _typing.Optional[str] = None
   groupUuid: _typing.Optional[str] = None
   directoryName: _typing.Optional[str] = None


class VsanObjectExtraAttributes(pyVmomi.vmodl.DynamicData):
   uuid: str
   objPath: str
   objClass: int
   ufn: str
   isHbrCfg: bool
   ownerClusterUuid: _typing.Optional[str] = None


class VsanObjectIdentity(pyVmomi.vmodl.DynamicData):
   uuid: str
   type: str
   vmInstanceUuid: _typing.Optional[str] = None
   vmNsObjectUuid: _typing.Optional[str] = None
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   description: _typing.Optional[str] = None
   spbmProfileUuid: _typing.Optional[str] = None
   metadatas: list[pyVmomi.vim.KeyValue] = []
   typeExtId: _typing.Optional[str] = None
   spbmProfileName: _typing.Optional[str] = None


class VsanObjectIdentityAndHealth(pyVmomi.vmodl.DynamicData):
   identities: list[VsanObjectIdentity] = []
   health: _typing.Optional[pyVmomi.vim.host.VsanObjectOverallHealth] = None
   spaceSummary: list[VsanObjectSpaceSummary] = []
   rawData: _typing.Optional[str] = None


class VsanObjectInformation(pyVmomi.vmodl.DynamicData):
   directoryName: _typing.Optional[str] = None
   vsanObjectUuid: _typing.Optional[str] = None
   vsanHealth: _typing.Optional[str] = None
   policyAttributes: list[pyVmomi.vim.KeyValue] = []
   spbmProfileUuid: _typing.Optional[str] = None
   spbmProfileGenerationId: _typing.Optional[str] = None
   spbmComplianceResult: _typing.Optional[StorageComplianceResult] = None


class VsanObjectPlacement(pyVmomi.vmodl.DynamicData):
   details: list[VsanObjectPlacementDetails] = []


class VsanObjectPlacementDetails(pyVmomi.vmodl.DynamicData):
   uuid: str
   type: str
   name: _typing.Optional[str] = None
   isRemote: bool
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   spbmProfileUuid: _typing.Optional[str] = None
   spbmProfileName: _typing.Optional[str] = None
   isLocalPolicy: _typing.Optional[bool] = None
   remoteDatastoreUuid: _typing.Optional[str] = None
   remoteDatastoreName: _typing.Optional[str] = None
   remoteCluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource] = None
   remoteClusterName: _typing.Optional[str] = None
   remoteVc: _typing.Optional[str] = None
   healthState: _typing.Optional[str] = None
   components: list[VsanComponentPlacement] = []


class VsanObjectQuerySpec(pyVmomi.vmodl.DynamicData):
   uuid: str
   spbmProfileGenerationId: _typing.Optional[str] = None


class VsanObjectSpaceSummary(pyVmomi.vmodl.DynamicData):
   class VsanObjectTypeEnum(pyVmomi.VmomiSupport.Enum):
      vmswap: _typing.ClassVar['VsanObjectTypeEnum'] = 'vmswap'
      vdisk: _typing.ClassVar['VsanObjectTypeEnum'] = 'vdisk'
      namespace: _typing.ClassVar['VsanObjectTypeEnum'] = 'namespace'
      vmem: _typing.ClassVar['VsanObjectTypeEnum'] = 'vmem'
      statsdb: _typing.ClassVar['VsanObjectTypeEnum'] = 'statsdb'
      iscsiTarget: _typing.ClassVar['VsanObjectTypeEnum'] = 'iscsiTarget'
      iscsiLun: _typing.ClassVar['VsanObjectTypeEnum'] = 'iscsiLun'
      other: _typing.ClassVar['VsanObjectTypeEnum'] = 'other'
      fileSystemOverhead: _typing.ClassVar['VsanObjectTypeEnum'] = 'fileSystemOverhead'
      dedupOverhead: _typing.ClassVar['VsanObjectTypeEnum'] = 'dedupOverhead'
      spaceUnderDedupConsideration: _typing.ClassVar['VsanObjectTypeEnum'] = 'spaceUnderDedupConsideration'
      checksumOverhead: _typing.ClassVar['VsanObjectTypeEnum'] = 'checksumOverhead'
      improvedVirtualDisk: _typing.ClassVar['VsanObjectTypeEnum'] = 'improvedVirtualDisk'
      transientSpace: _typing.ClassVar['VsanObjectTypeEnum'] = 'transientSpace'
      slackSpaceCapRequiredForHost: _typing.ClassVar['VsanObjectTypeEnum'] = 'slackSpaceCapRequiredForHost'
      resynPauseThresholdForHost: _typing.ClassVar['VsanObjectTypeEnum'] = 'resynPauseThresholdForHost'
      minSpaceRequiredForVsanOp: _typing.ClassVar['VsanObjectTypeEnum'] = 'minSpaceRequiredForVsanOp'
      hostRebuildCapacity: _typing.ClassVar['VsanObjectTypeEnum'] = 'hostRebuildCapacity'
      physicalTransientSpace: _typing.ClassVar['VsanObjectTypeEnum'] = 'physicalTransientSpace'
      haMetadataObject: _typing.ClassVar['VsanObjectTypeEnum'] = 'haMetadataObject'
      fileServiceRoot: _typing.ClassVar['VsanObjectTypeEnum'] = 'fileServiceRoot'
      attachedCnsVolBlock: _typing.ClassVar['VsanObjectTypeEnum'] = 'attachedCnsVolBlock'
      detachedCnsVolBlock: _typing.ClassVar['VsanObjectTypeEnum'] = 'detachedCnsVolBlock'
      attachedCnsVolFile: _typing.ClassVar['VsanObjectTypeEnum'] = 'attachedCnsVolFile'
      detachedCnsVolFile: _typing.ClassVar['VsanObjectTypeEnum'] = 'detachedCnsVolFile'
      cnsVolFile: _typing.ClassVar['VsanObjectTypeEnum'] = 'cnsVolFile'
      fileShare: _typing.ClassVar['VsanObjectTypeEnum'] = 'fileShare'
      extension: _typing.ClassVar['VsanObjectTypeEnum'] = 'extension'
      hbrDisk: _typing.ClassVar['VsanObjectTypeEnum'] = 'hbrDisk'
      hbrCfg: _typing.ClassVar['VsanObjectTypeEnum'] = 'hbrCfg'
      hbrPersist: _typing.ClassVar['VsanObjectTypeEnum'] = 'hbrPersist'
      traceobject: _typing.ClassVar['VsanObjectTypeEnum'] = 'traceobject'
      esaObjectOverhead: _typing.ClassVar['VsanObjectTypeEnum'] = 'esaObjectOverhead'
      pgNamespace: _typing.ClassVar['VsanObjectTypeEnum'] = 'pgNamespace'
      clusterDBNamespace: _typing.ClassVar['VsanObjectTypeEnum'] = 'clusterDBNamespace'
      aggregatedSystemObjects: _typing.ClassVar['VsanObjectTypeEnum'] = 'aggregatedSystemObjects'
      nativeObjectStore: _typing.ClassVar['VsanObjectTypeEnum'] = 'nativeObjectStore'
      VsanObjectTypeEnum_Unknown: _typing.ClassVar['VsanObjectTypeEnum'] = 'VsanObjectTypeEnum_Unknown'

   class VsanObjectTypeEnum90(pyVmomi.VmomiSupport.Enum):
      dedupSharedUserData: _typing.ClassVar['VsanObjectTypeEnum90'] = 'dedupSharedUserData'

   objType: _typing.Optional[str] = None
   overheadB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   temporaryOverheadB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   primaryCapacityB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   provisionCapacityB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   reservedCapacityB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   overReservedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   physicalUsedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   usedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   objTypeExt: _typing.Optional[str] = None
   objTypeExtDesc: _typing.Optional[str] = None
   snapshotUsedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanObjectSystem(pyVmomi.VmomiSupport.ManagedObject):
   def SetVsanObjectPolicy(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], vsanObjectUuid: str, profile: _typing.Optional[pyVmomi.vim.vm.ProfileSpec]) -> bool: ...
   def QueryVsanObjectInformation(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], vsanObjectQuerySpecs: list[VsanObjectQuerySpec]) -> list[VsanObjectInformation]: ...
   def QueryObjectIdentities(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], objUuids: list[str], objTypes: list[str], includeHealth: _typing.Optional[bool], includeObjIdentity: _typing.Optional[bool], includeSpaceSummary: _typing.Optional[bool], extraQuerySpec: _typing.Optional[VsanObjIdentityQuerySpec]) -> _typing.Optional[VsanObjectIdentityAndHealth]: ...
   def DeleteObjects(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], objUuids: list[str], force: _typing.Optional[bool]) -> pyVmomi.vim.Task: ...
   def QueryInaccessibleVmSwapObjects(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[str]: ...
   def QuerySyncingVsanObjectsSummary(self, cluster: pyVmomi.vim.ComputeResource, syncingObjectFilter: _typing.Optional[VsanSyncingObjectFilter]) -> pyVmomi.vim.vsan.host.VsanSyncingObjectQueryResult: ...
   def RelayoutObjects(self, cluster: pyVmomi.vim.ComputeResource) -> pyVmomi.vim.Task: ...
   def QueryPhysicalPlacements(self, cluster: pyVmomi.vim.ComputeResource, specs: _typing.Optional[VsanQueryPhysicalPlacementSpecs]) -> list[VsanObjectPlacement]: ...


class VsanPerfDiagnoseQuerySpec(pyVmomi.vmodl.DynamicData):
   startTime: _datetime.datetime
   endTime: _datetime.datetime
   queryType: str
   context: _typing.Optional[str] = None


class VsanPerfDiagnosticException(pyVmomi.vmodl.DynamicData):
   exceptionId: str
   exceptionMessage: str
   exceptionDetails: str
   exceptionUrl: str

class VsanPerfDiagnosticQueryType:
   pass


class VsanPerfDiagnosticResult(pyVmomi.vmodl.DynamicData):
   exceptionId: str
   recommendation: _typing.Optional[str] = None
   aggregationFunction: _typing.Optional[str] = None
   aggregationData: _typing.Optional[VsanPerfEntityMetricCSV] = None
   exceptionData: list[VsanPerfEntityMetricCSV] = []


class VsanPerfEntityMetricCSV(pyVmomi.vmodl.DynamicData):
   entityRefId: str
   sampleInfo: _typing.Optional[str] = None
   value: list[VsanPerfMetricSeriesCSV] = []


class VsanPerfEntityType(pyVmomi.vmodl.DynamicData):
   name: str
   id: str
   graphs: list[VsanPerfGraph] = []
   description: _typing.Optional[str] = None
   advancedGraphs: list[VsanPerfGraph] = []
   verboseGraphs: list[VsanPerfGraph] = []
   hotspotGraphs: list[VsanPerfGraph] = []


class VsanPerfGraph(pyVmomi.vmodl.DynamicData):
   class VsanPerfStatsUnitType(pyVmomi.VmomiSupport.Enum):
      number: _typing.ClassVar['VsanPerfStatsUnitType'] = 'number'
      time_ms: _typing.ClassVar['VsanPerfStatsUnitType'] = 'time_ms'
      percentage: _typing.ClassVar['VsanPerfStatsUnitType'] = 'percentage'
      size_bytes: _typing.ClassVar['VsanPerfStatsUnitType'] = 'size_bytes'
      rate_bytes: _typing.ClassVar['VsanPerfStatsUnitType'] = 'rate_bytes'
      permille: _typing.ClassVar['VsanPerfStatsUnitType'] = 'permille'
      time_s: _typing.ClassVar['VsanPerfStatsUnitType'] = 'time_s'
      time_us: _typing.ClassVar['VsanPerfStatsUnitType'] = 'time_us'
      time_ns: _typing.ClassVar['VsanPerfStatsUnitType'] = 'time_ns'
      VsanPerfStatsUnitType_Unknown: _typing.ClassVar['VsanPerfStatsUnitType'] = 'VsanPerfStatsUnitType_Unknown'

   id: str
   metrics: list[VsanPerfMetricId] = []
   unit: str
   threshold: _typing.Optional[VsanPerfThreshold] = None
   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   secondGraph: _typing.Optional[VsanPerfGraph] = None


class VsanPerfHotspotEntitiesMetrics(pyVmomi.vmodl.DynamicData):
   entityRefId: str
   startTime: _datetime.datetime
   endTime: _datetime.datetime
   metricsValue: list[VsanPerfMetricSeriesCSV] = []


class VsanPerfHotspotEntityType(pyVmomi.vmodl.DynamicData):
   name: str
   id: str
   sortingMetrics: list[VsanPerfMetricId] = []
   originalEntityTypes: list[str] = []
   description: _typing.Optional[str] = None


class VsanPerfHotspotQuerySpec(pyVmomi.vmodl.DynamicData):
   startTime: _datetime.datetime
   endTime: _datetime.datetime
   entity: str
   metricId: str
   numEntities: _typing.Optional[int] = None


class VsanPerfMasterInformation(pyVmomi.vmodl.DynamicData):
   secSinceLastStatsWrite: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   secSinceLastStatsCollect: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   statsIntervalSec: pyVmomi.VmomiSupport.long
   collectionFailureHostUuids: list[str] = []
   renamedStatsDirectories: list[str] = []
   statsDirectoryPercentFree: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   verboseMode: _typing.Optional[bool] = None
   verboseModeLastUpdate: _typing.Optional[_datetime.datetime] = None


class VsanPerfMemberInfo(pyVmomi.vmodl.DynamicData):
   thumbprint: str
   thumbprintList: list[pyVmomi.vim.vm.CertThumbprint] = []
   memberUuid: _typing.Optional[str] = None
   isSupportUnicast: _typing.Optional[bool] = None
   unicastAddressInfos: list[VsanUnicastAddressInfo] = []
   hostname: _typing.Optional[str] = None


class VsanPerfMetricId(pyVmomi.vmodl.DynamicData):
   class VsanPerfSummaryType(pyVmomi.VmomiSupport.Enum):
      average: _typing.ClassVar['VsanPerfSummaryType'] = 'average'
      maximum: _typing.ClassVar['VsanPerfSummaryType'] = 'maximum'
      minimum: _typing.ClassVar['VsanPerfSummaryType'] = 'minimum'
      latest: _typing.ClassVar['VsanPerfSummaryType'] = 'latest'
      summation: _typing.ClassVar['VsanPerfSummaryType'] = 'summation'
      none: _typing.ClassVar['VsanPerfSummaryType'] = 'none'
      VsanPerfSummaryType_Unknown: _typing.ClassVar['VsanPerfSummaryType'] = 'VsanPerfSummaryType_Unknown'

   class VsanPerfStatsType(pyVmomi.VmomiSupport.Enum):
      absolute: _typing.ClassVar['VsanPerfStatsType'] = 'absolute'
      delta: _typing.ClassVar['VsanPerfStatsType'] = 'delta'
      rate: _typing.ClassVar['VsanPerfStatsType'] = 'rate'
      VsanPerfStatsType_Unknown: _typing.ClassVar['VsanPerfStatsType'] = 'VsanPerfStatsType_Unknown'

   label: str
   group: _typing.Optional[str] = None
   rollupType: _typing.Optional[str] = None
   statsType: _typing.Optional[str] = None
   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   metricsCollectInterval: _typing.Optional[int] = None


class VsanPerfMetricSeriesCSV(pyVmomi.vmodl.DynamicData):
   metricId: VsanPerfMetricId
   threshold: _typing.Optional[VsanPerfThreshold] = None
   numExceptions: _typing.Optional[str] = None
   values: _typing.Optional[str] = None


class VsanPerfNodeInformation(pyVmomi.vmodl.DynamicData):
   version: str
   hostname: _typing.Optional[str] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   isCmmdsMaster: bool
   isStatsMaster: bool
   vsanMasterUuid: _typing.Optional[str] = None
   vsanNodeUuid: _typing.Optional[str] = None
   masterInfo: _typing.Optional[VsanPerfMasterInformation] = None
   diagnosticMode: _typing.Optional[bool] = None


class VsanPerfQuerySpec(pyVmomi.vmodl.DynamicData):
   entityRefId: str
   startTime: _typing.Optional[_datetime.datetime] = None
   endTime: _typing.Optional[_datetime.datetime] = None
   group: _typing.Optional[str] = None
   labels: list[str] = []
   interval: _typing.Optional[int] = None


class VsanPerfThreshold(pyVmomi.vmodl.DynamicData):
   class VsanPerfThresholdDirectionType(pyVmomi.VmomiSupport.Enum):
      upper: _typing.ClassVar['VsanPerfThresholdDirectionType'] = 'upper'
      lower: _typing.ClassVar['VsanPerfThresholdDirectionType'] = 'lower'
      VsanPerfThresholdDirectionType_Unknown: _typing.ClassVar['VsanPerfThresholdDirectionType'] = 'VsanPerfThresholdDirectionType_Unknown'

   direction: str
   yellow: _typing.Optional[str] = None
   red: _typing.Optional[str] = None


class VsanPerfTimeRange(pyVmomi.vmodl.DynamicData):
   name: str
   startTime: _datetime.datetime
   endTime: _datetime.datetime


class VsanPerfTimeRangeQuerySpec(pyVmomi.vmodl.DynamicData):
   name: _typing.Optional[str] = None
   startTimeFrom: _typing.Optional[_datetime.datetime] = None
   startTimeTo: _typing.Optional[_datetime.datetime] = None
   endTimeFrom: _typing.Optional[_datetime.datetime] = None
   endTimeTo: _typing.Optional[_datetime.datetime] = None


class VsanPerfTopEntities(pyVmomi.vmodl.DynamicData):
   metricId: VsanPerfMetricId
   entities: list[VsanPerfTopEntity] = []


class VsanPerfTopEntity(pyVmomi.vmodl.DynamicData):
   entityRefId: str
   value: str


class VsanPerfTopQuerySpec(pyVmomi.vmodl.DynamicData):
   timeStamp: _datetime.datetime
   entity: str
   metricId: str
   numEntities: _typing.Optional[int] = None


class VsanPerformanceManager(pyVmomi.VmomiSupport.ManagedObject):
   def QueryVsanPerfTopEntities(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], querySpec: VsanPerfTopQuerySpec) -> list[VsanPerfEntityMetricCSV]: ...
   def QueryVsanPerfHotspotEntities(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], querySpec: VsanPerfHotspotQuerySpec) -> list[VsanPerfHotspotEntitiesMetrics]: ...
   def VsanPerfDiagnose(self, perfDiagnoseQuery: VsanPerfDiagnoseQuerySpec, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[VsanPerfDiagnosticResult]: ...
   def VsanPerfDiagnoseTask(self, perfDiagnoseQuery: VsanPerfDiagnoseQuerySpec, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> pyVmomi.vim.Task: ...
   def GetVsanPerfDiagnosisResult(self, task: pyVmomi.vim.Task, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[VsanPerfDiagnosticResult]: ...
   def QueryVsanPerf(self, querySpecs: list[VsanPerfQuerySpec], cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[VsanPerfEntityMetricCSV]: ...
   def QueryNodeInformation(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[VsanPerfNodeInformation]: ...
   def CreateStatsObject(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], profile: _typing.Optional[pyVmomi.vim.vm.ProfileSpec]) -> str: ...
   def CreateStatsObjectTask(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], profile: _typing.Optional[pyVmomi.vim.vm.ProfileSpec]) -> pyVmomi.vim.Task: ...
   def DeleteStatsObject(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> bool: ...
   def DeleteStatsObjectTask(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> pyVmomi.vim.Task: ...
   def SetStatsObjectPolicy(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], profile: _typing.Optional[pyVmomi.vim.vm.ProfileSpec]) -> bool: ...
   def QueryStatsObjectInformation(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> VsanObjectInformation: ...
   def QueryClusterHealth(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[VsanClusterHealthGroup]: ...
   def QueryTimeRanges(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], querySpec: VsanPerfTimeRangeQuerySpec) -> list[VsanPerfTimeRange]: ...
   def SaveTimeRanges(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], timeRanges: list[VsanPerfTimeRange]) -> None: ...
   def DeleteTimeRange(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], name: str) -> None: ...
   def ToggleVerboseMode(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], verboseMode: bool) -> None: ...
   def GetSupportedEntityTypes(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[VsanPerfEntityType]: ...
   def GetSupportedHotspotEntityTypes(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[VsanPerfHotspotEntityType]: ...
   def GetSupportedDiagnosticExceptions(self) -> list[VsanPerfDiagnosticException]: ...
   def GetAggregatedEntityTypes(self) -> list[VsanPerfEntityType]: ...
   def QueryRemoteServerClusters(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], querySpec: _typing.Optional[VsanRemoteClusterQuerySpec]) -> list[str]: ...


class VsanPerfsvcConfig(pyVmomi.vmodl.DynamicData):
   enabled: bool
   profile: _typing.Optional[pyVmomi.vim.vm.ProfileSpec] = None
   diagnosticMode: _typing.Optional[bool] = None
   verboseMode: _typing.Optional[bool] = None


class VsanQueryPhysicalPlacementSpecs(pyVmomi.vmodl.DynamicData):
   vms: list[pyVmomi.vim.VirtualMachine] = []

class VsanRelayoutObjectsErrorCode:
   pass


class VsanRemoteClusterQuerySpec(pyVmomi.vmodl.DynamicData):
   startTime: _typing.Optional[_datetime.datetime] = None
   endTime: _typing.Optional[_datetime.datetime] = None


class VsanRemoteDatastoreSystem(pyVmomi.VmomiSupport.ManagedObject):
   def MountPrecheck(self, cluster: pyVmomi.vim.ClusterComputeResource, datastore: pyVmomi.vim.Datastore, serverClusterInfo: _typing.Optional[pyVmomi.vim.vsan.VcRemoteVsanServerClusterInfo]) -> pyVmomi.vim.vsan.MountPrecheckResult: ...
   def RemoteVcMountPrecheck(self, cluster: pyVmomi.vim.ClusterComputeResource, xvcDatastore: pyVmomi.vim.vsan.XVCDatastoreInfo, serverClusterInfo: _typing.Optional[pyVmomi.vim.vsan.VcRemoteVsanServerClusterInfo]) -> pyVmomi.vim.vsan.MountPrecheckResult: ...
   def QueryDatastoreSource(self, vcHosts: list[str]) -> list[pyVmomi.vim.vsan.HciMeshDatastoreSource]: ...
   def PrecheckDatastoreSource(self, datastoreSource: pyVmomi.vim.vsan.HciMeshDatastoreSource, operation: _typing.Optional[str]) -> pyVmomi.vim.vsan.DatastoreSourcePrecheckResult: ...
   def CreateDatastoreSource(self, datastoreSource: pyVmomi.vim.vsan.HciMeshDatastoreSource) -> pyVmomi.vim.Task: ...
   def UpdateDatastoreSource(self, datastoreSource: pyVmomi.vim.vsan.HciMeshDatastoreSource) -> pyVmomi.vim.Task: ...
   def DestroyDatastoreSource(self, datastoreSource: pyVmomi.vim.vsan.HciMeshDatastoreSource) -> pyVmomi.vim.Task: ...
   def QueryHciMeshDatastores(self, querySpecs: list[pyVmomi.vim.vsan.XvcQuerySpec], extraVcInfos: list[pyVmomi.vim.vsan.RemoteVcInfo]) -> list[pyVmomi.vim.vsan.XvcQueryResultSet]: ...


class VsanSnapshotSpace(pyVmomi.vmodl.DynamicData):
   snapshotCount: _typing.Optional[int] = None
   actualSnapshotUsedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   fullyInflatedSnapshotUsedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanSpaceQuerySpec(pyVmomi.vmodl.DynamicData):
   entityType: str
   entityIds: list[str] = []


class VsanSpaceReportSystem(pyVmomi.VmomiSupport.ManagedObject):
   def QuerySpaceUsage(self, cluster: pyVmomi.vim.ComputeResource, storagePolicies: list[pyVmomi.vim.vm.ProfileSpec], whatifCapacityOnly: _typing.Optional[bool]) -> VsanSpaceUsage: ...
   def QueryVsanManagedStorageSpaceUsage(self, cluster: pyVmomi.vim.ComputeResource, querySpec: QueryVsanManagedStorageSpaceUsageSpec) -> list[VsanSpaceUsageWithDatastoreType]: ...
   def QueryEntitySpaceUsage(self, cluster: pyVmomi.vim.ComputeResource, querySpec: VsanSpaceQuerySpec) -> list[VsanEntitySpaceUsage]: ...

class VsanSpaceReportingEntityType:
   pass


class VsanSpaceUsage(pyVmomi.vmodl.DynamicData):
   totalCapacityB: pyVmomi.VmomiSupport.long
   freeCapacityB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   spaceOverview: _typing.Optional[VsanObjectSpaceSummary] = None
   spaceDetail: _typing.Optional[VsanSpaceUsageDetailResult] = None
   efficientCapacity: _typing.Optional[pyVmomi.vim.vsan.DataEfficiencyCapacityState] = None
   whatifCapacities: list[VsanWhatifCapacity] = []
   uncommittedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   capacityHealthThreshold: _typing.Optional[pyVmomi.vim.vsan.VsanHealthThreshold] = None
   spaceEfficiencyRatio: _typing.Optional[pyVmomi.vim.vsan.VsanSpaceEfficiencyRatio] = None
   effectiveSpaceUsage: _typing.Optional[VsanEffectiveSpaceUsage] = None


class VsanSpaceUsageDetailResult(pyVmomi.vmodl.DynamicData):
   spaceUsageByObjectType: list[VsanObjectSpaceSummary] = []


class VsanSpaceUsageWithDatastoreType(pyVmomi.vmodl.DynamicData):
   spaceUsage: _typing.Optional[VsanSpaceUsage] = None
   datastoreType: _typing.Optional[str] = None


class VsanStorageWorkloadType(pyVmomi.vmodl.DynamicData):
   specs: list[pyVmomi.vim.host.VsanVmdkLoadTestSpec] = []
   typeId: str
   name: str
   description: str
   duration: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanStretchedClusterConfig(pyVmomi.vmodl.DynamicData):
   cluster: pyVmomi.vim.ClusterComputeResource
   preferredFdName: _typing.Optional[str] = None
   faultDomainConfig: _typing.Optional[VSANStretchedClusterFaultDomainConfig] = None


class VsanSyncingObjectFilter(pyVmomi.vmodl.DynamicData):
   resyncType: _typing.Optional[str] = None
   resyncStatus: _typing.Optional[str] = None
   numberOfObjects: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   offset: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   includeDedupObject: _typing.Optional[bool] = None


class VsanUnicastAddressInfo(pyVmomi.vmodl.DynamicData):
   address: str
   port: _typing.Optional[int] = None
   nicType: _typing.Optional[str] = None


class VsanUpgradeStatusEx(pyVmomi.vim.VsanUpgradeSystem.UpgradeStatus):
   isPrecheck: _typing.Optional[bool] = None
   precheckResult: _typing.Optional[VsanDiskFormatConversionCheckResult] = None


class VsanUpgradeSystemUpgradeHistoryStoragePoolOp(pyVmomi.vim.VsanUpgradeSystem.UpgradeHistoryItem):
   operation: str
   diskInfo: pyVmomi.vim.vsan.host.StoragePoolDiskInfo


class VsanVcClusterConfigSystem(pyVmomi.VmomiSupport.ManagedObject):
   def ReconfigureEx(self, cluster: pyVmomi.vim.ClusterComputeResource, vsanReconfigSpec: pyVmomi.vim.vsan.ReconfigSpec) -> pyVmomi.vim.Task: ...
   def GetConfigInfoEx(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.vsan.ConfigInfoEx: ...
   def RekeyEncryptedCluster(self, encryptedCluster: pyVmomi.vim.ClusterComputeResource, deepRekey: _typing.Optional[bool], allowReducedRedundancy: _typing.Optional[bool]) -> pyVmomi.vim.Task: ...
   def GetRuntimeStats(self, cluster: pyVmomi.vim.ClusterComputeResource, stats: list[str]) -> list[pyVmomi.vim.vsan.RuntimeStatsHostMap]: ...
   def QueryClusterDrsStats(self, cluster: pyVmomi.vim.ClusterComputeResource, vms: list[pyVmomi.vim.VirtualMachine]) -> list[pyVmomi.vim.vsan.host.DrsStats]: ...
   def ValidateConfigSpec(self, cluster: pyVmomi.vim.ClusterComputeResource, vsanReconfigSpec: pyVmomi.vim.vsan.ReconfigSpec) -> list[pyVmomi.vim.ClusterComputeResource.ValidationResultBase]: ...
   def RunLifecycleCheck(self, cluster: pyVmomi.vim.ClusterComputeResource, vsanLifecycleCheckSpec: VsanVcLifecycleCheckSpec) -> VsanVcLifecycleCheckResult: ...
   def GetClaimedCapacity(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.VmomiSupport.long: ...
   def GetConfigurationLimits(self) -> list[pyVmomi.vmodl.KeyAnyValue]: ...
   def GetClusterAutoRAIDInfo(self, cluster: pyVmomi.vim.ClusterComputeResource) -> _typing.Optional[pyVmomi.vim.vsan.AutoRAIDInfo]: ...


class VsanVcClusterHealthSystem(pyVmomi.VmomiSupport.ManagedObject):
   class VsanHealthLogLevelEnum(pyVmomi.VmomiSupport.Enum):
      INFO: _typing.ClassVar['VsanHealthLogLevelEnum'] = 'INFO'
      WARNING: _typing.ClassVar['VsanHealthLogLevelEnum'] = 'WARNING'
      ERROR: _typing.ClassVar['VsanHealthLogLevelEnum'] = 'ERROR'
      DEBUG: _typing.ClassVar['VsanHealthLogLevelEnum'] = 'DEBUG'
      CRITICAL: _typing.ClassVar['VsanHealthLogLevelEnum'] = 'CRITICAL'
      VsanHealthLogLevelEnum_Unknown: _typing.ClassVar['VsanHealthLogLevelEnum'] = 'VsanHealthLogLevelEnum_Unknown'

   def QueryVerifyClusterHealthSystemVersions(self, cluster: pyVmomi.vim.ClusterComputeResource) -> VsanClusterHealthSystemVersionResult: ...
   def QueryFileServiceHealthSummary(self, cluster: pyVmomi.vim.ClusterComputeResource, includeFileServerHealth: _typing.Optional[bool], includeFileShareHealth: _typing.Optional[bool]) -> _typing.Optional[VsanClusterFileServiceHealthSummary]: ...
   def QueryClusterCreateVmHealthTest(self, cluster: pyVmomi.vim.ClusterComputeResource, timeout: int, datastore: _typing.Optional[pyVmomi.vim.Datastore]) -> VsanClusterCreateVmHealthTestResult: ...
   def QueryClusterHealthSummary(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], vmCreateTimeout: _typing.Optional[int], objUuids: list[str], includeObjUuids: _typing.Optional[bool], fields: list[str], fetchFromCache: _typing.Optional[bool], perspective: _typing.Optional[str], hosts: list[pyVmomi.vim.HostSystem], spec: _typing.Optional[VsanClusterHealthQuerySpec]) -> VsanClusterHealthSummary: ...
   def QueryClusterHealthSummaryTask(self, cluster: pyVmomi.vim.ClusterComputeResource, hosts: list[pyVmomi.vim.HostSystem], includeDataProtectionHealth: _typing.Optional[bool], includeOnlineHealth: _typing.Optional[bool]) -> pyVmomi.vim.Task: ...
   def QueryVsanObjExtAttrs(self, cluster: pyVmomi.vim.ClusterComputeResource, uuids: list[str]) -> list[VsanObjectExtAttrs]: ...
   def QueryAllSupportedHealthChecks(self) -> list[VsanClusterHealthCheckInfo]: ...
   def QueryClusterNetworkPerfTest(self, cluster: pyVmomi.vim.ClusterComputeResource, multicast: bool, durationSec: _typing.Optional[int]) -> VsanClusterNetworkLoadTestResult: ...
   def QueryClusterNetworkPerfTask(self, cluster: pyVmomi.vim.ClusterComputeResource, spec: _typing.Optional[VsanClusterNetworkPerfTaskSpec]) -> pyVmomi.vim.Task: ...
   def RunVmdkLoadTest(self, cluster: pyVmomi.vim.ClusterComputeResource, runname: str, durationSec: _typing.Optional[int], specs: list[pyVmomi.vim.host.VsanVmdkLoadTestSpec], action: _typing.Optional[str]) -> pyVmomi.vim.Task: ...
   def QueryVsanClusterHealthConfig(self, cluster: pyVmomi.vim.ClusterComputeResource) -> VsanClusterHealthConfigs: ...
   def QueryVsanClusterHealthCheckInterval(self, cluster: pyVmomi.vim.ClusterComputeResource) -> int: ...
   def SetVsanClusterHealthCheckInterval(self, cluster: pyVmomi.vim.ClusterComputeResource, vsanClusterHealthCheckInterval: int) -> None: ...
   def GetVsanClusterSilentChecks(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[str]: ...
   def SetVsanClusterSilentChecks(self, cluster: pyVmomi.vim.ClusterComputeResource, addSilentChecks: list[str], removeSilentChecks: list[str]) -> bool: ...
   def SetVsanClusterTelemetryConfig(self, cluster: pyVmomi.vim.ClusterComputeResource, vsanClusterHealthConfig: VsanClusterHealthConfigs) -> None: ...
   def TestVsanClusterTelemetryProxy(self, proxyConfig: VsanClusterTelemetryProxyConfig) -> bool: ...
   def SendVsanTelemetry(self, cluster: pyVmomi.vim.ClusterComputeResource) -> None: ...
   def RepairClusterObjectsImmediate(self, cluster: pyVmomi.vim.ClusterComputeResource, uuids: list[str]) -> pyVmomi.vim.Task: ...
   def UpdateDefaultDSPolicyRecommendation(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task: ...
   def QueryClusterCreateVmHealthHistoryTest(self, cluster: pyVmomi.vim.ClusterComputeResource, count: _typing.Optional[int], datastore: _typing.Optional[pyVmomi.vim.Datastore]) -> list[VsanClusterCreateVmHealthTestResult]: ...
   def QueryClusterNetworkPerfHistoryTest(self, cluster: pyVmomi.vim.ClusterComputeResource, count: _typing.Optional[int], spec: _typing.Optional[VsanClusterNetworkPerfTaskSpec]) -> list[VsanClusterNetworkLoadTestResult]: ...
   def QueryClusterVmdkLoadHistoryTest(self, cluster: pyVmomi.vim.ClusterComputeResource, count: _typing.Optional[int], taskId: _typing.Optional[str]) -> list[VsanClusterVmdkLoadTestResult]: ...
   def QueryClusterVmdkWorkloadTypes(self) -> list[VsanStorageWorkloadType]: ...
   def QueryAttachToSrHistory(self, cluster: pyVmomi.vim.ClusterComputeResource, count: _typing.Optional[int], taskId: _typing.Optional[str]) -> list[VsanAttachToSrOperation]: ...
   def AttachVsanSupportBundleToSr(self, cluster: pyVmomi.vim.ClusterComputeResource, srNumber: str) -> pyVmomi.vim.Task: ...
   def GetClusterHclInfo(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], includeHostsResult: _typing.Optional[bool], includeVendorInfo: _typing.Optional[bool], esxRelease: _typing.Optional[str], querySpec: _typing.Optional[pyVmomi.vim.vsan.VsanHclQuerySpec]) -> VsanClusterHclInfo: ...
   def GetHclInfoForVsanEligibleDisks(self, querySpec: pyVmomi.vim.vsan.VsanHclQuerySpec) -> VsanClusterHclInfo: ...
   def DownloadHclFile(self, sha1sums: list[str]) -> pyVmomi.vim.Task: ...
   def GetClusterHclConstraints(self, cluster: pyVmomi.vim.ClusterComputeResource, release: str) -> pyVmomi.vim.vsan.VsanHclReleaseConstraint: ...
   def GetDiskHclConstraints(self, release: _typing.Optional[str], diskModels: list[pyVmomi.vim.vsan.VsanDiskModelInfo]) -> list[pyVmomi.vim.vsan.VsanHclDiskConstraint]: ...
   def GetClusterReleaseRecommendation(self, cluster: pyVmomi.vim.ClusterComputeResource, minor: list[str], major: list[str]) -> list[pyVmomi.vim.vsan.VsanHclReleaseConstraint]: ...
   def PurgeHclFiles(self, sha1sums: list[str]) -> None: ...
   def DownloadAndInstallVendorTool(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task: ...
   def UploadHclDb(self, db: str) -> bool: ...
   def UpdateHclDbFromWeb(self, url: _typing.Optional[str]) -> bool: ...
   def RebalanceCluster(self, cluster: pyVmomi.vim.ClusterComputeResource, targetHosts: list[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task: ...
   def StopRebalanceCluster(self, cluster: pyVmomi.vim.ClusterComputeResource, targetHosts: list[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task: ...
   def IsRebalanceRunning(self, cluster: pyVmomi.vim.ClusterComputeResource, targetHosts: list[pyVmomi.vim.HostSystem]) -> bool: ...
   def SetLogLevel(self, level: _typing.Optional[str]) -> None: ...
   def QuerySmartStatsSummary(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[pyVmomi.vim.host.VsanSmartStatsHostSummary]: ...
   def QueryVsanProxyConfig(self) -> VsanClusterTelemetryProxyConfig: ...
   def QueryClusterHistoricalHealth(self, spec: VsanHistoricalHealthQuerySpec) -> list[VsanClusterHealthSummary]: ...
   def SetVsanVcgMappingForHwDevices(self, spec: pyVmomi.vim.vsan.VsanHwToVcgInfoMappingSpec) -> bool: ...


class VsanVcDiskManagementSystem(pyVmomi.VmomiSupport.ManagedObject):
   def RetrieveAllFlashCapabilities(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[pyVmomi.vim.vsan.host.VsanHostCapability]: ...
   def InitializeDiskMappings(self, spec: pyVmomi.vim.vsan.host.DiskMappingCreationSpec) -> pyVmomi.vim.Task: ...
   def QueryDiskMappings(self, host: pyVmomi.vim.HostSystem) -> list[pyVmomi.vim.vsan.host.DiskMapInfoEx]: ...
   def QueryVsanManagedDisks(self, host: pyVmomi.vim.HostSystem, filterSpec: _typing.Optional[pyVmomi.vim.vsan.host.QueryVsanDisksSpec]) -> _typing.Optional[pyVmomi.vim.vsan.host.VsanManagedDisksInfo]: ...
   def QueryClusterDataEfficiencyCapacityState(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.vsan.DataEfficiencyCapacityState: ...
   def RebuildDiskMapping(self, host: pyVmomi.vim.HostSystem, mapping: pyVmomi.vim.vsan.host.DiskMapping, maintenanceSpec: pyVmomi.vim.host.MaintenanceSpec) -> pyVmomi.vim.Task: ...
   def UnmountDiskMappingEx(self, cluster: pyVmomi.vim.ClusterComputeResource, mappings: list[pyVmomi.vim.vsan.host.DiskMapping], maintenanceSpec: pyVmomi.vim.host.MaintenanceSpec) -> pyVmomi.vim.Task: ...
   def RemoveDiskMappingEx(self, cluster: pyVmomi.vim.ClusterComputeResource, mappings: list[pyVmomi.vim.vsan.host.DiskMapping], maintenanceSpec: pyVmomi.vim.host.MaintenanceSpec) -> pyVmomi.vim.Task: ...
   def RemoveDiskEx(self, cluster: pyVmomi.vim.ClusterComputeResource, disks: list[pyVmomi.vim.host.ScsiDisk], maintenanceSpec: pyVmomi.vim.host.MaintenanceSpec) -> pyVmomi.vim.Task: ...
   def AddStoragePoolDisks(self, specs: list[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec]) -> pyVmomi.vim.Task: ...
   def DeleteStoragePoolDisk(self, cluster: pyVmomi.vim.ClusterComputeResource, spec: pyVmomi.vim.vsan.host.DeleteStoragePoolDiskSpec) -> pyVmomi.vim.Task: ...
   def UnmountStoragePoolDisks(self, cluster: pyVmomi.vim.ClusterComputeResource, spec: pyVmomi.vim.vsan.host.DeleteStoragePoolDiskSpec) -> pyVmomi.vim.Task: ...


class VsanVcKmipServersHealth(pyVmomi.vmodl.DynamicData):
   health: _typing.Optional[str] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   kmsProviderId: _typing.Optional[str] = None
   kmsHealth: list[pyVmomi.vim.host.VsanKmsHealth] = []
   clientCertHealth: _typing.Optional[str] = None
   clientCertExpireDate: _typing.Optional[_datetime.datetime] = None
   isAwsKms: _typing.Optional[bool] = None
   cmkHealth: _typing.Optional[str] = None
   kekExpireHealth: _typing.Optional[str] = None
   kekExpireDate: _typing.Optional[_datetime.datetime] = None
   hostKeyExpireHealth: _typing.Optional[str] = None
   hostKeyExpireDate: _typing.Optional[_datetime.datetime] = None


class VsanVcLifecycleCheckResult(pyVmomi.vmodl.DynamicData):
   status: str
   preCheckResults: list[pyVmomi.vim.vsan.LifecyclePreCheckResult] = []
   configDetails: pyVmomi.vim.vsan.LifecycleConfigDetails


class VsanVcLifecycleCheckSpec(pyVmomi.vmodl.DynamicData):
   operation: str


class VsanVcStretchedClusterSystem(pyVmomi.VmomiSupport.ManagedObject):
   def AddWitnessHost(self, cluster: pyVmomi.vim.ClusterComputeResource, witnessHost: pyVmomi.vim.HostSystem, preferredFd: str, diskMapping: _typing.Optional[pyVmomi.vim.vsan.host.DiskMapping], metadataMode: _typing.Optional[bool], storagePoolSpec: _typing.Optional[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec]) -> pyVmomi.vim.Task: ...
   def RemoveWitnessHost(self, cluster: pyVmomi.vim.ClusterComputeResource, witnessHost: _typing.Optional[pyVmomi.vim.HostSystem], witnessAddress: _typing.Optional[str]) -> pyVmomi.vim.Task: ...
   def ConvertToStretchedCluster(self, cluster: pyVmomi.vim.ClusterComputeResource, faultDomainConfig: VSANStretchedClusterFaultDomainConfig, witnessHost: pyVmomi.vim.HostSystem, preferredFd: str, diskMapping: _typing.Optional[pyVmomi.vim.vsan.host.DiskMapping], storagePoolSpec: _typing.Optional[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec]) -> pyVmomi.vim.Task: ...
   def SetPreferredFaultDomain(self, cluster: pyVmomi.vim.ClusterComputeResource, preferredFd: str, witnessHost: _typing.Optional[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task: ...
   def GetPreferredFaultDomain(self, cluster: pyVmomi.vim.ClusterComputeResource) -> _typing.Optional[VSANPreferredFaultDomainInfo]: ...
   def IsWitnessHost(self, host: pyVmomi.vim.HostSystem) -> bool: ...
   def GetWitnessHosts(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[VSANWitnessHostInfo]: ...
   def RetrieveStretchedClusterVcCapability(self, cluster: pyVmomi.vim.ClusterComputeResource, verifyAllConnected: _typing.Optional[bool]) -> list[VSANStretchedClusterCapability]: ...
   def IsWitnessVirtualAppliance(self, hosts: list[pyVmomi.vim.HostSystem]) -> list[pyVmomi.vim.host.VsanHostVirtualApplianceInfo]: ...
   def QuerySharedWitnessCompatibility(self, sharedWitnessHost: pyVmomi.vim.HostSystem, roboClusters: list[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.vsan.SharedWitnessCompatibilityResult: ...
   def QueryWitnessHostClusterInfo(self, witnessHost: pyVmomi.vim.HostSystem, skipComponentsCount: _typing.Optional[bool]) -> list[pyVmomi.vim.vsan.ClusterRuntimeInfo]: ...
   def ReplaceWitnessHostForClusters(self, configSpec: pyVmomi.vim.vsan.VsanVcStretchedClusterConfigSpec) -> pyVmomi.vim.Task: ...
   def AddWitnessHostForClusters(self, configSpec: pyVmomi.vim.vsan.VsanVcStretchedClusterConfigSpec) -> pyVmomi.vim.Task: ...


class VsanVsanClusterPcapGroup(pyVmomi.vmodl.DynamicData):
   master: str
   members: list[str] = []


class VsanVsanClusterPcapResult(pyVmomi.vmodl.DynamicData):
   pkts: list[str] = []
   groups: list[VsanVsanClusterPcapGroup] = []
   issues: list[str] = []
   hostResults: list[pyVmomi.vim.host.VsanVsanPcapResult] = []


class VsanVumSystem(pyVmomi.VmomiSupport.ManagedObject):
   def GetVsanVumConfig(self) -> VsanVumSystemConfig: ...
   def FetchIsoDepotCookie(self, username: str, password: str) -> None: ...
   def UpdateHostFirmware(self, host: pyVmomi.vim.HostSystem) -> pyVmomi.vim.Task: ...
   def UploadReleaseDb(self, db: str) -> None: ...


class VsanVumSystemConfig(pyVmomi.vmodl.DynamicData):
   enabled: _typing.Optional[bool] = None
   autoCheckInterval: _typing.Optional[int] = None
   metadataUpdateInterval: _typing.Optional[int] = None
   releaseDbLastUpdate: _typing.Optional[_datetime.datetime] = None


class VsanWhatifCapacity(pyVmomi.vmodl.DynamicData):
   totalWhatifCapacityB: pyVmomi.VmomiSupport.long
   freeWhatifCapacityB: pyVmomi.VmomiSupport.long
   storagePolicy: pyVmomi.vim.vm.ProfileSpec
   isSatisfiable: bool


class VsanWitnessSpec(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   preferredFaultDomainName: str
   diskMapping: _typing.Optional[pyVmomi.vim.vsan.host.DiskMapping] = None
   storagePoolSpec: _typing.Optional[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec] = None
