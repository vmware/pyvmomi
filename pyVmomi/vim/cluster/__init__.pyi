from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, long


class EVCManager(vim.ExtensibleManagedObject):
    @property
    def managedCluster(self) -> vim.ClusterComputeResource: ...
    @property
    def evcState(self) -> EVCManager.EVCState: ...
    def ConfigureEvc(self, evcModeKey: str, evcGraphicsModeKey: str) -> vim.Task: ...
    def DisableEvc(self) -> vim.Task: ...
    def CheckConfigureEvc(self, evcModeKey: str, evcGraphicsModeKey: str) -> vim.Task: ...
    def CheckAddHostEvc(self, cnxSpec: vim.host.ConnectSpec) -> vim.Task: ...


    class CheckResult(vmodl.DynamicData):
        @property
        def evcModeKey(self) -> str: ...
        @evcModeKey.setter
        def evcModeKey(self, value: str):
            self._evcModeKey = value
        @property
        def error(self) -> vmodl.MethodFault: ...
        @error.setter
        def error(self, value: vmodl.MethodFault):
            self._error = value
        @property
        def host(self) -> List[vim.HostSystem]: ...
        @host.setter
        def host(self, value: List[vim.HostSystem]):
            self._host = value


    class EVCState(vmodl.DynamicData):
        @property
        def supportedEVCMode(self) -> List[vim.EVCMode]: ...
        @supportedEVCMode.setter
        def supportedEVCMode(self, value: List[vim.EVCMode]):
            self._supportedEVCMode = value
        @property
        def currentEVCModeKey(self) -> str: ...
        @currentEVCModeKey.setter
        def currentEVCModeKey(self, value: str):
            self._currentEVCModeKey = value
        @property
        def guaranteedCPUFeatures(self) -> List[vim.host.CpuIdInfo]: ...
        @guaranteedCPUFeatures.setter
        def guaranteedCPUFeatures(self, value: List[vim.host.CpuIdInfo]):
            self._guaranteedCPUFeatures = value
        @property
        def featureCapability(self) -> List[vim.host.FeatureCapability]: ...
        @featureCapability.setter
        def featureCapability(self, value: List[vim.host.FeatureCapability]):
            self._featureCapability = value
        @property
        def featureMask(self) -> List[vim.host.FeatureMask]: ...
        @featureMask.setter
        def featureMask(self, value: List[vim.host.FeatureMask]):
            self._featureMask = value
        @property
        def featureRequirement(self) -> List[vim.vm.FeatureRequirement]: ...
        @featureRequirement.setter
        def featureRequirement(self, value: List[vim.vm.FeatureRequirement]):
            self._featureRequirement = value


class Action(vmodl.DynamicData):
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def target(self) -> ManagedObject: ...
    @target.setter
    def target(self, value: ManagedObject):
        self._target = value


    class ActionType(Enum):
        MigrationV1 = "MigrationV1"
        VmPowerV1 = "VmPowerV1"
        HostPowerV1 = "HostPowerV1"
        IncreaseLimitV1 = "IncreaseLimitV1"
        IncreaseSizeV1 = "IncreaseSizeV1"
        IncreaseSharesV1 = "IncreaseSharesV1"
        IncreaseReservationV1 = "IncreaseReservationV1"
        DecreaseOthersReservationV1 = "DecreaseOthersReservationV1"
        IncreaseClusterCapacityV1 = "IncreaseClusterCapacityV1"
        DecreaseMigrationThresholdV1 = "DecreaseMigrationThresholdV1"
        HostMaintenanceV1 = "HostMaintenanceV1"
        StorageMigrationV1 = "StorageMigrationV1"
        StoragePlacementV1 = "StoragePlacementV1"
        PlacementV1 = "PlacementV1"
        HostInfraUpdateHaV1 = "HostInfraUpdateHaV1"


class ActionHistory(vmodl.DynamicData):
    @property
    def action(self) -> Action: ...
    @action.setter
    def action(self, value: Action):
        self._action = value
    @property
    def time(self) -> datetime: ...
    @time.setter
    def time(self, value: datetime):
        self._time = value


class AffinityRuleSpec(RuleInfo):
    @property
    def vm(self) -> List[vim.VirtualMachine]: ...
    @vm.setter
    def vm(self, value: List[vim.VirtualMachine]):
        self._vm = value


class AntiAffinityRuleSpec(RuleInfo):
    @property
    def vm(self) -> List[vim.VirtualMachine]: ...
    @vm.setter
    def vm(self, value: List[vim.VirtualMachine]):
        self._vm = value


class AttemptedVmInfo(vmodl.DynamicData):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def task(self) -> vim.Task: ...
    @task.setter
    def task(self, value: vim.Task):
        self._task = value


class ClusterInitialPlacementAction(Action):
    @property
    def targetHost(self) -> vim.HostSystem: ...
    @targetHost.setter
    def targetHost(self, value: vim.HostSystem):
        self._targetHost = value
    @property
    def pool(self) -> vim.ResourcePool: ...
    @pool.setter
    def pool(self, value: vim.ResourcePool):
        self._pool = value
    @property
    def configSpec(self) -> vim.vm.ConfigSpec: ...
    @configSpec.setter
    def configSpec(self, value: vim.vm.ConfigSpec):
        self._configSpec = value


class ConfigInfo(vmodl.DynamicData):
    @property
    def dasConfig(self) -> DasConfigInfo: ...
    @dasConfig.setter
    def dasConfig(self, value: DasConfigInfo):
        self._dasConfig = value
    @property
    def dasVmConfig(self) -> List[DasVmConfigInfo]: ...
    @dasVmConfig.setter
    def dasVmConfig(self, value: List[DasVmConfigInfo]):
        self._dasVmConfig = value
    @property
    def drsConfig(self) -> DrsConfigInfo: ...
    @drsConfig.setter
    def drsConfig(self, value: DrsConfigInfo):
        self._drsConfig = value
    @property
    def drsVmConfig(self) -> List[DrsVmConfigInfo]: ...
    @drsVmConfig.setter
    def drsVmConfig(self, value: List[DrsVmConfigInfo]):
        self._drsVmConfig = value
    @property
    def rule(self) -> List[RuleInfo]: ...
    @rule.setter
    def rule(self, value: List[RuleInfo]):
        self._rule = value


class ConfigInfoEx(vim.ComputeResource.ConfigInfo):
    @property
    def systemVMsConfig(self) -> SystemVMsConfigInfo: ...
    @systemVMsConfig.setter
    def systemVMsConfig(self, value: SystemVMsConfigInfo):
        self._systemVMsConfig = value
    @property
    def dasConfig(self) -> DasConfigInfo: ...
    @dasConfig.setter
    def dasConfig(self, value: DasConfigInfo):
        self._dasConfig = value
    @property
    def dasVmConfig(self) -> List[DasVmConfigInfo]: ...
    @dasVmConfig.setter
    def dasVmConfig(self, value: List[DasVmConfigInfo]):
        self._dasVmConfig = value
    @property
    def drsConfig(self) -> DrsConfigInfo: ...
    @drsConfig.setter
    def drsConfig(self, value: DrsConfigInfo):
        self._drsConfig = value
    @property
    def drsVmConfig(self) -> List[DrsVmConfigInfo]: ...
    @drsVmConfig.setter
    def drsVmConfig(self, value: List[DrsVmConfigInfo]):
        self._drsVmConfig = value
    @property
    def rule(self) -> List[RuleInfo]: ...
    @rule.setter
    def rule(self, value: List[RuleInfo]):
        self._rule = value
    @property
    def orchestration(self) -> OrchestrationInfo: ...
    @orchestration.setter
    def orchestration(self, value: OrchestrationInfo):
        self._orchestration = value
    @property
    def vmOrchestration(self) -> List[VmOrchestrationInfo]: ...
    @vmOrchestration.setter
    def vmOrchestration(self, value: List[VmOrchestrationInfo]):
        self._vmOrchestration = value
    @property
    def dpmConfigInfo(self) -> DpmConfigInfo: ...
    @dpmConfigInfo.setter
    def dpmConfigInfo(self, value: DpmConfigInfo):
        self._dpmConfigInfo = value
    @property
    def dpmHostConfig(self) -> List[DpmHostConfigInfo]: ...
    @dpmHostConfig.setter
    def dpmHostConfig(self, value: List[DpmHostConfigInfo]):
        self._dpmHostConfig = value
    @property
    def vsanConfigInfo(self) -> ConfigInfo: ...
    @vsanConfigInfo.setter
    def vsanConfigInfo(self, value: ConfigInfo):
        self._vsanConfigInfo = value
    @property
    def vsanHostConfig(self) -> List[vim.vsan.host.ConfigInfo]: ...
    @vsanHostConfig.setter
    def vsanHostConfig(self, value: List[vim.vsan.host.ConfigInfo]):
        self._vsanHostConfig = value
    @property
    def group(self) -> List[GroupInfo]: ...
    @group.setter
    def group(self, value: List[GroupInfo]):
        self._group = value
    @property
    def infraUpdateHaConfig(self) -> InfraUpdateHaConfigInfo: ...
    @infraUpdateHaConfig.setter
    def infraUpdateHaConfig(self, value: InfraUpdateHaConfigInfo):
        self._infraUpdateHaConfig = value
    @property
    def proactiveDrsConfig(self) -> ProactiveDrsConfigInfo: ...
    @proactiveDrsConfig.setter
    def proactiveDrsConfig(self, value: ProactiveDrsConfigInfo):
        self._proactiveDrsConfig = value
    @property
    def cryptoConfig(self) -> CryptoConfigInfo: ...
    @cryptoConfig.setter
    def cryptoConfig(self, value: CryptoConfigInfo):
        self._cryptoConfig = value


class ConfigSpec(vmodl.DynamicData):
    @property
    def dasConfig(self) -> DasConfigInfo: ...
    @dasConfig.setter
    def dasConfig(self, value: DasConfigInfo):
        self._dasConfig = value
    @property
    def dasVmConfigSpec(self) -> List[DasVmConfigSpec]: ...
    @dasVmConfigSpec.setter
    def dasVmConfigSpec(self, value: List[DasVmConfigSpec]):
        self._dasVmConfigSpec = value
    @property
    def drsConfig(self) -> DrsConfigInfo: ...
    @drsConfig.setter
    def drsConfig(self, value: DrsConfigInfo):
        self._drsConfig = value
    @property
    def drsVmConfigSpec(self) -> List[DrsVmConfigSpec]: ...
    @drsVmConfigSpec.setter
    def drsVmConfigSpec(self, value: List[DrsVmConfigSpec]):
        self._drsVmConfigSpec = value
    @property
    def rulesSpec(self) -> List[RuleSpec]: ...
    @rulesSpec.setter
    def rulesSpec(self, value: List[RuleSpec]):
        self._rulesSpec = value


class ConfigSpecEx(vim.ComputeResource.ConfigSpec):
    @property
    def systemVMsConfig(self) -> SystemVMsConfigSpec: ...
    @systemVMsConfig.setter
    def systemVMsConfig(self, value: SystemVMsConfigSpec):
        self._systemVMsConfig = value
    @property
    def dasConfig(self) -> DasConfigInfo: ...
    @dasConfig.setter
    def dasConfig(self, value: DasConfigInfo):
        self._dasConfig = value
    @property
    def dasVmConfigSpec(self) -> List[DasVmConfigSpec]: ...
    @dasVmConfigSpec.setter
    def dasVmConfigSpec(self, value: List[DasVmConfigSpec]):
        self._dasVmConfigSpec = value
    @property
    def drsConfig(self) -> DrsConfigInfo: ...
    @drsConfig.setter
    def drsConfig(self, value: DrsConfigInfo):
        self._drsConfig = value
    @property
    def drsVmConfigSpec(self) -> List[DrsVmConfigSpec]: ...
    @drsVmConfigSpec.setter
    def drsVmConfigSpec(self, value: List[DrsVmConfigSpec]):
        self._drsVmConfigSpec = value
    @property
    def rulesSpec(self) -> List[RuleSpec]: ...
    @rulesSpec.setter
    def rulesSpec(self, value: List[RuleSpec]):
        self._rulesSpec = value
    @property
    def orchestration(self) -> OrchestrationInfo: ...
    @orchestration.setter
    def orchestration(self, value: OrchestrationInfo):
        self._orchestration = value
    @property
    def vmOrchestrationSpec(self) -> List[VmOrchestrationSpec]: ...
    @vmOrchestrationSpec.setter
    def vmOrchestrationSpec(self, value: List[VmOrchestrationSpec]):
        self._vmOrchestrationSpec = value
    @property
    def dpmConfig(self) -> DpmConfigInfo: ...
    @dpmConfig.setter
    def dpmConfig(self, value: DpmConfigInfo):
        self._dpmConfig = value
    @property
    def dpmHostConfigSpec(self) -> List[DpmHostConfigSpec]: ...
    @dpmHostConfigSpec.setter
    def dpmHostConfigSpec(self, value: List[DpmHostConfigSpec]):
        self._dpmHostConfigSpec = value
    @property
    def vsanConfig(self) -> ConfigInfo: ...
    @vsanConfig.setter
    def vsanConfig(self, value: ConfigInfo):
        self._vsanConfig = value
    @property
    def vsanHostConfigSpec(self) -> List[vim.vsan.host.ConfigInfo]: ...
    @vsanHostConfigSpec.setter
    def vsanHostConfigSpec(self, value: List[vim.vsan.host.ConfigInfo]):
        self._vsanHostConfigSpec = value
    @property
    def groupSpec(self) -> List[GroupSpec]: ...
    @groupSpec.setter
    def groupSpec(self, value: List[GroupSpec]):
        self._groupSpec = value
    @property
    def infraUpdateHaConfig(self) -> InfraUpdateHaConfigInfo: ...
    @infraUpdateHaConfig.setter
    def infraUpdateHaConfig(self, value: InfraUpdateHaConfigInfo):
        self._infraUpdateHaConfig = value
    @property
    def proactiveDrsConfig(self) -> ProactiveDrsConfigInfo: ...
    @proactiveDrsConfig.setter
    def proactiveDrsConfig(self, value: ProactiveDrsConfigInfo):
        self._proactiveDrsConfig = value
    @property
    def inHciWorkflow(self) -> bool: ...
    @inHciWorkflow.setter
    def inHciWorkflow(self, value: bool):
        self._inHciWorkflow = value
    @property
    def cryptoConfig(self) -> CryptoConfigInfo: ...
    @cryptoConfig.setter
    def cryptoConfig(self, value: CryptoConfigInfo):
        self._cryptoConfig = value


class CryptoConfigInfo(vmodl.DynamicData):
    @property
    def cryptoMode(self) -> str: ...
    @cryptoMode.setter
    def cryptoMode(self, value: str):
        self._cryptoMode = value


    class CryptoMode(Enum):
        onDemand = "onDemand"
        forceEnable = "forceEnable"


class DasAamHostInfo(DasHostInfo):
    @property
    def hostDasState(self) -> List[DasAamNodeState]: ...
    @hostDasState.setter
    def hostDasState(self, value: List[DasAamNodeState]):
        self._hostDasState = value
    @property
    def primaryHosts(self) -> List[str]: ...
    @primaryHosts.setter
    def primaryHosts(self, value: List[str]):
        self._primaryHosts = value


class DasAamNodeState(vmodl.DynamicData):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def configState(self) -> str: ...
    @configState.setter
    def configState(self, value: str):
        self._configState = value
    @property
    def runtimeState(self) -> str: ...
    @runtimeState.setter
    def runtimeState(self, value: str):
        self._runtimeState = value


    class DasState(Enum):
        uninitialized = "uninitialized"
        initialized = "initialized"
        configuring = "configuring"
        unconfiguring = "unconfiguring"
        running = "running"
        error = "error"
        agentShutdown = "agentShutdown"
        nodeFailed = "nodeFailed"


class DasAdmissionControlInfo(vmodl.DynamicData): ...


class DasAdmissionControlPolicy(vmodl.DynamicData):
    @property
    def resourceReductionToToleratePercent(self) -> int: ...
    @resourceReductionToToleratePercent.setter
    def resourceReductionToToleratePercent(self, value: int):
        self._resourceReductionToToleratePercent = value
    @property
    def pMemAdmissionControlEnabled(self) -> bool: ...
    @pMemAdmissionControlEnabled.setter
    def pMemAdmissionControlEnabled(self, value: bool):
        self._pMemAdmissionControlEnabled = value


class DasAdvancedRuntimeInfo(vmodl.DynamicData):
    @property
    def dasHostInfo(self) -> DasHostInfo: ...
    @dasHostInfo.setter
    def dasHostInfo(self, value: DasHostInfo):
        self._dasHostInfo = value
    @property
    def vmcpSupported(self) -> DasAdvancedRuntimeInfo.VmcpCapabilityInfo: ...
    @vmcpSupported.setter
    def vmcpSupported(self, value: DasAdvancedRuntimeInfo.VmcpCapabilityInfo):
        self._vmcpSupported = value
    @property
    def heartbeatDatastoreInfo(self) -> List[DasAdvancedRuntimeInfo.HeartbeatDatastoreInfo]: ...
    @heartbeatDatastoreInfo.setter
    def heartbeatDatastoreInfo(self, value: List[DasAdvancedRuntimeInfo.HeartbeatDatastoreInfo]):
        self._heartbeatDatastoreInfo = value


    class HeartbeatDatastoreInfo(vmodl.DynamicData):
        @property
        def datastore(self) -> vim.Datastore: ...
        @datastore.setter
        def datastore(self, value: vim.Datastore):
            self._datastore = value
        @property
        def hosts(self) -> List[vim.HostSystem]: ...
        @hosts.setter
        def hosts(self, value: List[vim.HostSystem]):
            self._hosts = value


    class VmcpCapabilityInfo(vmodl.DynamicData):
        @property
        def storageAPDSupported(self) -> bool: ...
        @storageAPDSupported.setter
        def storageAPDSupported(self, value: bool):
            self._storageAPDSupported = value
        @property
        def storagePDLSupported(self) -> bool: ...
        @storagePDLSupported.setter
        def storagePDLSupported(self, value: bool):
            self._storagePDLSupported = value


class DasConfigInfo(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def vmMonitoring(self) -> str: ...
    @vmMonitoring.setter
    def vmMonitoring(self, value: str):
        self._vmMonitoring = value
    @property
    def hostMonitoring(self) -> str: ...
    @hostMonitoring.setter
    def hostMonitoring(self, value: str):
        self._hostMonitoring = value
    @property
    def vmComponentProtecting(self) -> str: ...
    @vmComponentProtecting.setter
    def vmComponentProtecting(self, value: str):
        self._vmComponentProtecting = value
    @property
    def failoverLevel(self) -> int: ...
    @failoverLevel.setter
    def failoverLevel(self, value: int):
        self._failoverLevel = value
    @property
    def admissionControlPolicy(self) -> DasAdmissionControlPolicy: ...
    @admissionControlPolicy.setter
    def admissionControlPolicy(self, value: DasAdmissionControlPolicy):
        self._admissionControlPolicy = value
    @property
    def admissionControlEnabled(self) -> bool: ...
    @admissionControlEnabled.setter
    def admissionControlEnabled(self, value: bool):
        self._admissionControlEnabled = value
    @property
    def defaultVmSettings(self) -> DasVmSettings: ...
    @defaultVmSettings.setter
    def defaultVmSettings(self, value: DasVmSettings):
        self._defaultVmSettings = value
    @property
    def option(self) -> List[vim.option.OptionValue]: ...
    @option.setter
    def option(self, value: List[vim.option.OptionValue]):
        self._option = value
    @property
    def heartbeatDatastore(self) -> List[vim.Datastore]: ...
    @heartbeatDatastore.setter
    def heartbeatDatastore(self, value: List[vim.Datastore]):
        self._heartbeatDatastore = value
    @property
    def hBDatastoreCandidatePolicy(self) -> str: ...
    @hBDatastoreCandidatePolicy.setter
    def hBDatastoreCandidatePolicy(self, value: str):
        self._hBDatastoreCandidatePolicy = value


    class HBDatastoreCandidate(Enum):
        userSelectedDs = "userSelectedDs"
        allFeasibleDs = "allFeasibleDs"
        allFeasibleDsWithUserPreference = "allFeasibleDsWithUserPreference"


    class ServiceState(Enum):
        disabled = "disabled"
        enabled = "enabled"


    class VmMonitoringState(Enum):
        vmMonitoringDisabled = "vmMonitoringDisabled"
        vmMonitoringOnly = "vmMonitoringOnly"
        vmAndAppMonitoring = "vmAndAppMonitoring"


class DasData(vmodl.DynamicData): ...


class DasDataSummary(DasData):
    @property
    def hostListVersion(self) -> long: ...
    @hostListVersion.setter
    def hostListVersion(self, value: long):
        self._hostListVersion = value
    @property
    def clusterConfigVersion(self) -> long: ...
    @clusterConfigVersion.setter
    def clusterConfigVersion(self, value: long):
        self._clusterConfigVersion = value
    @property
    def compatListVersion(self) -> long: ...
    @compatListVersion.setter
    def compatListVersion(self, value: long):
        self._compatListVersion = value


class DasFailoverLevelAdvancedRuntimeInfo(DasAdvancedRuntimeInfo):
    @property
    def slotInfo(self) -> DasFailoverLevelAdvancedRuntimeInfo.SlotInfo: ...
    @slotInfo.setter
    def slotInfo(self, value: DasFailoverLevelAdvancedRuntimeInfo.SlotInfo):
        self._slotInfo = value
    @property
    def totalSlots(self) -> int: ...
    @totalSlots.setter
    def totalSlots(self, value: int):
        self._totalSlots = value
    @property
    def usedSlots(self) -> int: ...
    @usedSlots.setter
    def usedSlots(self, value: int):
        self._usedSlots = value
    @property
    def unreservedSlots(self) -> int: ...
    @unreservedSlots.setter
    def unreservedSlots(self, value: int):
        self._unreservedSlots = value
    @property
    def totalVms(self) -> int: ...
    @totalVms.setter
    def totalVms(self, value: int):
        self._totalVms = value
    @property
    def totalHosts(self) -> int: ...
    @totalHosts.setter
    def totalHosts(self, value: int):
        self._totalHosts = value
    @property
    def totalGoodHosts(self) -> int: ...
    @totalGoodHosts.setter
    def totalGoodHosts(self, value: int):
        self._totalGoodHosts = value
    @property
    def hostSlots(self) -> List[DasFailoverLevelAdvancedRuntimeInfo.HostSlots]: ...
    @hostSlots.setter
    def hostSlots(self, value: List[DasFailoverLevelAdvancedRuntimeInfo.HostSlots]):
        self._hostSlots = value
    @property
    def vmsRequiringMultipleSlots(self) -> List[DasFailoverLevelAdvancedRuntimeInfo.VmSlots]: ...
    @vmsRequiringMultipleSlots.setter
    def vmsRequiringMultipleSlots(self, value: List[DasFailoverLevelAdvancedRuntimeInfo.VmSlots]):
        self._vmsRequiringMultipleSlots = value


    class HostSlots(vmodl.DynamicData):
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def slots(self) -> int: ...
        @slots.setter
        def slots(self, value: int):
            self._slots = value


    class SlotInfo(vmodl.DynamicData):
        @property
        def numVcpus(self) -> int: ...
        @numVcpus.setter
        def numVcpus(self, value: int):
            self._numVcpus = value
        @property
        def cpuMHz(self) -> int: ...
        @cpuMHz.setter
        def cpuMHz(self, value: int):
            self._cpuMHz = value
        @property
        def memoryMB(self) -> int: ...
        @memoryMB.setter
        def memoryMB(self, value: int):
            self._memoryMB = value


    class VmSlots(vmodl.DynamicData):
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @vm.setter
        def vm(self, value: vim.VirtualMachine):
            self._vm = value
        @property
        def slots(self) -> int: ...
        @slots.setter
        def slots(self, value: int):
            self._slots = value


class DasFdmHostState(vmodl.DynamicData):
    @property
    def state(self) -> str: ...
    @state.setter
    def state(self, value: str):
        self._state = value
    @property
    def stateReporter(self) -> vim.HostSystem: ...
    @stateReporter.setter
    def stateReporter(self, value: vim.HostSystem):
        self._stateReporter = value


class DasHostInfo(vmodl.DynamicData): ...


class DasHostRecommendation(vmodl.DynamicData):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def drsRating(self) -> int: ...
    @drsRating.setter
    def drsRating(self, value: int):
        self._drsRating = value


class DasVmConfigInfo(vmodl.DynamicData):
    @property
    def key(self) -> vim.VirtualMachine: ...
    @key.setter
    def key(self, value: vim.VirtualMachine):
        self._key = value
    @property
    def restartPriority(self) -> DasVmConfigInfo.Priority: ...
    @restartPriority.setter
    def restartPriority(self, value: DasVmConfigInfo.Priority):
        self._restartPriority = value
    @property
    def powerOffOnIsolation(self) -> bool: ...
    @powerOffOnIsolation.setter
    def powerOffOnIsolation(self, value: bool):
        self._powerOffOnIsolation = value
    @property
    def dasSettings(self) -> DasVmSettings: ...
    @dasSettings.setter
    def dasSettings(self, value: DasVmSettings):
        self._dasSettings = value


    class Priority(Enum):
        disabled = "disabled"
        low = "low"
        medium = "medium"
        high = "high"


class DasVmConfigSpec(vim.option.ArrayUpdateSpec):
    @property
    def info(self) -> DasVmConfigInfo: ...
    @info.setter
    def info(self, value: DasVmConfigInfo):
        self._info = value


class DasVmSettings(vmodl.DynamicData):
    @property
    def restartPriority(self) -> str: ...
    @restartPriority.setter
    def restartPriority(self, value: str):
        self._restartPriority = value
    @property
    def restartPriorityTimeout(self) -> int: ...
    @restartPriorityTimeout.setter
    def restartPriorityTimeout(self, value: int):
        self._restartPriorityTimeout = value
    @property
    def isolationResponse(self) -> str: ...
    @isolationResponse.setter
    def isolationResponse(self, value: str):
        self._isolationResponse = value
    @property
    def vmToolsMonitoringSettings(self) -> VmToolsMonitoringSettings: ...
    @vmToolsMonitoringSettings.setter
    def vmToolsMonitoringSettings(self, value: VmToolsMonitoringSettings):
        self._vmToolsMonitoringSettings = value
    @property
    def vmComponentProtectionSettings(self) -> VmComponentProtectionSettings: ...
    @vmComponentProtectionSettings.setter
    def vmComponentProtectionSettings(self, value: VmComponentProtectionSettings):
        self._vmComponentProtectionSettings = value


    class IsolationResponse(Enum):
        none = "none"
        powerOff = "powerOff"
        shutdown = "shutdown"
        clusterIsolationResponse = "clusterIsolationResponse"


    class RestartPriority(Enum):
        disabled = "disabled"
        lowest = "lowest"
        low = "low"
        medium = "medium"
        high = "high"
        highest = "highest"
        clusterRestartPriority = "clusterRestartPriority"


class DatastoreUpdateSpec(vim.option.ArrayUpdateSpec):
    @property
    def datastore(self) -> vim.Datastore: ...
    @datastore.setter
    def datastore(self, value: vim.Datastore):
        self._datastore = value


class DependencyRuleInfo(RuleInfo):
    @property
    def vmGroup(self) -> str: ...
    @vmGroup.setter
    def vmGroup(self, value: str):
        self._vmGroup = value
    @property
    def dependsOnVmGroup(self) -> str: ...
    @dependsOnVmGroup.setter
    def dependsOnVmGroup(self, value: str):
        self._dependsOnVmGroup = value


class DpmConfigInfo(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def defaultDpmBehavior(self) -> DpmConfigInfo.DpmBehavior: ...
    @defaultDpmBehavior.setter
    def defaultDpmBehavior(self, value: DpmConfigInfo.DpmBehavior):
        self._defaultDpmBehavior = value
    @property
    def hostPowerActionRate(self) -> int: ...
    @hostPowerActionRate.setter
    def hostPowerActionRate(self, value: int):
        self._hostPowerActionRate = value
    @property
    def option(self) -> List[vim.option.OptionValue]: ...
    @option.setter
    def option(self, value: List[vim.option.OptionValue]):
        self._option = value


    class DpmBehavior(Enum):
        manual = "manual"
        automated = "automated"


class DpmHostConfigInfo(vmodl.DynamicData):
    @property
    def key(self) -> vim.HostSystem: ...
    @key.setter
    def key(self, value: vim.HostSystem):
        self._key = value
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def behavior(self) -> DpmConfigInfo.DpmBehavior: ...
    @behavior.setter
    def behavior(self, value: DpmConfigInfo.DpmBehavior):
        self._behavior = value


class DpmHostConfigSpec(vim.option.ArrayUpdateSpec):
    @property
    def info(self) -> DpmHostConfigInfo: ...
    @info.setter
    def info(self, value: DpmHostConfigInfo):
        self._info = value


class DrsConfigInfo(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def enableVmBehaviorOverrides(self) -> bool: ...
    @enableVmBehaviorOverrides.setter
    def enableVmBehaviorOverrides(self, value: bool):
        self._enableVmBehaviorOverrides = value
    @property
    def defaultVmBehavior(self) -> DrsConfigInfo.DrsBehavior: ...
    @defaultVmBehavior.setter
    def defaultVmBehavior(self, value: DrsConfigInfo.DrsBehavior):
        self._defaultVmBehavior = value
    @property
    def vmotionRate(self) -> int: ...
    @vmotionRate.setter
    def vmotionRate(self, value: int):
        self._vmotionRate = value
    @property
    def scaleDescendantsShares(self) -> str: ...
    @scaleDescendantsShares.setter
    def scaleDescendantsShares(self, value: str):
        self._scaleDescendantsShares = value
    @property
    def option(self) -> List[vim.option.OptionValue]: ...
    @option.setter
    def option(self, value: List[vim.option.OptionValue]):
        self._option = value


    class DrsBehavior(Enum):
        manual = "manual"
        partiallyAutomated = "partiallyAutomated"
        fullyAutomated = "fullyAutomated"


class DrsFaults(vmodl.DynamicData):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def faultsByVm(self) -> List[DrsFaults.FaultsByVm]: ...
    @faultsByVm.setter
    def faultsByVm(self, value: List[DrsFaults.FaultsByVm]):
        self._faultsByVm = value


    class FaultsByVirtualDisk(DrsFaults.FaultsByVm):
        @property
        def disk(self) -> vim.vm.device.VirtualDiskId: ...
        @disk.setter
        def disk(self, value: vim.vm.device.VirtualDiskId):
            self._disk = value


    class FaultsByVm(vmodl.DynamicData):
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @vm.setter
        def vm(self, value: vim.VirtualMachine):
            self._vm = value
        @property
        def fault(self) -> List[vmodl.MethodFault]: ...
        @fault.setter
        def fault(self, value: List[vmodl.MethodFault]):
            self._fault = value


class DrsMigration(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def time(self) -> datetime: ...
    @time.setter
    def time(self, value: datetime):
        self._time = value
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def cpuLoad(self) -> int: ...
    @cpuLoad.setter
    def cpuLoad(self, value: int):
        self._cpuLoad = value
    @property
    def memoryLoad(self) -> long: ...
    @memoryLoad.setter
    def memoryLoad(self, value: long):
        self._memoryLoad = value
    @property
    def source(self) -> vim.HostSystem: ...
    @source.setter
    def source(self, value: vim.HostSystem):
        self._source = value
    @property
    def sourceCpuLoad(self) -> int: ...
    @sourceCpuLoad.setter
    def sourceCpuLoad(self, value: int):
        self._sourceCpuLoad = value
    @property
    def sourceMemoryLoad(self) -> long: ...
    @sourceMemoryLoad.setter
    def sourceMemoryLoad(self, value: long):
        self._sourceMemoryLoad = value
    @property
    def destination(self) -> vim.HostSystem: ...
    @destination.setter
    def destination(self, value: vim.HostSystem):
        self._destination = value
    @property
    def destinationCpuLoad(self) -> int: ...
    @destinationCpuLoad.setter
    def destinationCpuLoad(self, value: int):
        self._destinationCpuLoad = value
    @property
    def destinationMemoryLoad(self) -> long: ...
    @destinationMemoryLoad.setter
    def destinationMemoryLoad(self, value: long):
        self._destinationMemoryLoad = value


class DrsRecommendation(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def rating(self) -> int: ...
    @rating.setter
    def rating(self, value: int):
        self._rating = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def reasonText(self) -> str: ...
    @reasonText.setter
    def reasonText(self, value: str):
        self._reasonText = value
    @property
    def migrationList(self) -> List[DrsMigration]: ...
    @migrationList.setter
    def migrationList(self, value: List[DrsMigration]):
        self._migrationList = value


    class ReasonCode(Enum):
        fairnessCpuAvg = "fairnessCpuAvg"
        fairnessMemAvg = "fairnessMemAvg"
        jointAffin = "jointAffin"
        antiAffin = "antiAffin"
        hostMaint = "hostMaint"


class DrsVmConfigInfo(vmodl.DynamicData):
    @property
    def key(self) -> vim.VirtualMachine: ...
    @key.setter
    def key(self, value: vim.VirtualMachine):
        self._key = value
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def behavior(self) -> DrsConfigInfo.DrsBehavior: ...
    @behavior.setter
    def behavior(self, value: DrsConfigInfo.DrsBehavior):
        self._behavior = value


class DrsVmConfigSpec(vim.option.ArrayUpdateSpec):
    @property
    def info(self) -> DrsVmConfigInfo: ...
    @info.setter
    def info(self, value: DrsVmConfigInfo):
        self._info = value


class EnterMaintenanceResult(vmodl.DynamicData):
    @property
    def recommendations(self) -> List[Recommendation]: ...
    @recommendations.setter
    def recommendations(self, value: List[Recommendation]):
        self._recommendations = value
    @property
    def fault(self) -> DrsFaults: ...
    @fault.setter
    def fault(self, value: DrsFaults):
        self._fault = value


class FailoverHostAdmissionControlInfo(DasAdmissionControlInfo):
    @property
    def hostStatus(self) -> List[FailoverHostAdmissionControlInfo.HostStatus]: ...
    @hostStatus.setter
    def hostStatus(self, value: List[FailoverHostAdmissionControlInfo.HostStatus]):
        self._hostStatus = value


    class HostStatus(vmodl.DynamicData):
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def status(self) -> vim.ManagedEntity.Status: ...
        @status.setter
        def status(self, value: vim.ManagedEntity.Status):
            self._status = value


class FailoverHostAdmissionControlPolicy(DasAdmissionControlPolicy):
    @property
    def failoverHosts(self) -> List[vim.HostSystem]: ...
    @failoverHosts.setter
    def failoverHosts(self, value: List[vim.HostSystem]):
        self._failoverHosts = value
    @property
    def failoverLevel(self) -> int: ...
    @failoverLevel.setter
    def failoverLevel(self, value: int):
        self._failoverLevel = value


class FailoverLevelAdmissionControlInfo(DasAdmissionControlInfo):
    @property
    def currentFailoverLevel(self) -> int: ...
    @currentFailoverLevel.setter
    def currentFailoverLevel(self, value: int):
        self._currentFailoverLevel = value


class FailoverLevelAdmissionControlPolicy(DasAdmissionControlPolicy):
    @property
    def failoverLevel(self) -> int: ...
    @failoverLevel.setter
    def failoverLevel(self, value: int):
        self._failoverLevel = value
    @property
    def slotPolicy(self) -> SlotPolicy: ...
    @slotPolicy.setter
    def slotPolicy(self, value: SlotPolicy):
        self._slotPolicy = value


class FailoverResourcesAdmissionControlInfo(DasAdmissionControlInfo):
    @property
    def currentCpuFailoverResourcesPercent(self) -> int: ...
    @currentCpuFailoverResourcesPercent.setter
    def currentCpuFailoverResourcesPercent(self, value: int):
        self._currentCpuFailoverResourcesPercent = value
    @property
    def currentMemoryFailoverResourcesPercent(self) -> int: ...
    @currentMemoryFailoverResourcesPercent.setter
    def currentMemoryFailoverResourcesPercent(self, value: int):
        self._currentMemoryFailoverResourcesPercent = value
    @property
    def currentPMemFailoverResourcesPercent(self) -> int: ...
    @currentPMemFailoverResourcesPercent.setter
    def currentPMemFailoverResourcesPercent(self, value: int):
        self._currentPMemFailoverResourcesPercent = value


class FailoverResourcesAdmissionControlPolicy(DasAdmissionControlPolicy):
    @property
    def cpuFailoverResourcesPercent(self) -> int: ...
    @cpuFailoverResourcesPercent.setter
    def cpuFailoverResourcesPercent(self, value: int):
        self._cpuFailoverResourcesPercent = value
    @property
    def memoryFailoverResourcesPercent(self) -> int: ...
    @memoryFailoverResourcesPercent.setter
    def memoryFailoverResourcesPercent(self, value: int):
        self._memoryFailoverResourcesPercent = value
    @property
    def failoverLevel(self) -> int: ...
    @failoverLevel.setter
    def failoverLevel(self, value: int):
        self._failoverLevel = value
    @property
    def autoComputePercentages(self) -> bool: ...
    @autoComputePercentages.setter
    def autoComputePercentages(self, value: bool):
        self._autoComputePercentages = value
    @property
    def pMemFailoverResourcesPercent(self) -> int: ...
    @pMemFailoverResourcesPercent.setter
    def pMemFailoverResourcesPercent(self, value: int):
        self._pMemFailoverResourcesPercent = value
    @property
    def autoComputePMemFailoverResourcesPercent(self) -> bool: ...
    @autoComputePMemFailoverResourcesPercent.setter
    def autoComputePMemFailoverResourcesPercent(self, value: bool):
        self._autoComputePMemFailoverResourcesPercent = value


class FixedSizeSlotPolicy(SlotPolicy):
    @property
    def cpu(self) -> int: ...
    @cpu.setter
    def cpu(self, value: int):
        self._cpu = value
    @property
    def memory(self) -> int: ...
    @memory.setter
    def memory(self, value: int):
        self._memory = value


class GroupInfo(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def userCreated(self) -> bool: ...
    @userCreated.setter
    def userCreated(self, value: bool):
        self._userCreated = value
    @property
    def uniqueID(self) -> str: ...
    @uniqueID.setter
    def uniqueID(self, value: str):
        self._uniqueID = value


class GroupSpec(vim.option.ArrayUpdateSpec):
    @property
    def info(self) -> GroupInfo: ...
    @info.setter
    def info(self, value: GroupInfo):
        self._info = value


class HostGroup(GroupInfo):
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @host.setter
    def host(self, value: List[vim.HostSystem]):
        self._host = value


class HostInfraUpdateHaModeAction(Action):
    @property
    def operationType(self) -> str: ...
    @operationType.setter
    def operationType(self, value: str):
        self._operationType = value


    class OperationType(Enum):
        enterQuarantine = "enterQuarantine"
        exitQuarantine = "exitQuarantine"
        enterMaintenance = "enterMaintenance"


class HostPowerAction(Action):
    @property
    def operationType(self) -> HostPowerAction.OperationType: ...
    @operationType.setter
    def operationType(self, value: HostPowerAction.OperationType):
        self._operationType = value
    @property
    def powerConsumptionWatt(self) -> int: ...
    @powerConsumptionWatt.setter
    def powerConsumptionWatt(self, value: int):
        self._powerConsumptionWatt = value
    @property
    def cpuCapacityMHz(self) -> int: ...
    @cpuCapacityMHz.setter
    def cpuCapacityMHz(self, value: int):
        self._cpuCapacityMHz = value
    @property
    def memCapacityMB(self) -> int: ...
    @memCapacityMB.setter
    def memCapacityMB(self, value: int):
        self._memCapacityMB = value


class HostRecommendation(vmodl.DynamicData):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def rating(self) -> int: ...
    @rating.setter
    def rating(self, value: int):
        self._rating = value


class InfraUpdateHaConfigInfo(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def behavior(self) -> str: ...
    @behavior.setter
    def behavior(self, value: str):
        self._behavior = value
    @property
    def moderateRemediation(self) -> str: ...
    @moderateRemediation.setter
    def moderateRemediation(self, value: str):
        self._moderateRemediation = value
    @property
    def severeRemediation(self) -> str: ...
    @severeRemediation.setter
    def severeRemediation(self, value: str):
        self._severeRemediation = value
    @property
    def providers(self) -> List[str]: ...
    @providers.setter
    def providers(self, value: List[str]):
        self._providers = value


    class BehaviorType(Enum):
        Manual = "Manual"
        Automated = "Automated"


    class RemediationType(Enum):
        QuarantineMode = "QuarantineMode"
        MaintenanceMode = "MaintenanceMode"


class InitialPlacementAction(Action):
    @property
    def targetHost(self) -> vim.HostSystem: ...
    @targetHost.setter
    def targetHost(self, value: vim.HostSystem):
        self._targetHost = value
    @property
    def pool(self) -> vim.ResourcePool: ...
    @pool.setter
    def pool(self, value: vim.ResourcePool):
        self._pool = value


class MigrationAction(Action):
    @property
    def drsMigration(self) -> DrsMigration: ...
    @drsMigration.setter
    def drsMigration(self, value: DrsMigration):
        self._drsMigration = value


class NotAttemptedVmInfo(vmodl.DynamicData):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class OrchestrationInfo(vmodl.DynamicData):
    @property
    def defaultVmReadiness(self) -> VmReadiness: ...
    @defaultVmReadiness.setter
    def defaultVmReadiness(self, value: VmReadiness):
        self._defaultVmReadiness = value


class PlacementAction(Action):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def targetHost(self) -> vim.HostSystem: ...
    @targetHost.setter
    def targetHost(self, value: vim.HostSystem):
        self._targetHost = value
    @property
    def relocateSpec(self) -> vim.vm.RelocateSpec: ...
    @relocateSpec.setter
    def relocateSpec(self, value: vim.vm.RelocateSpec):
        self._relocateSpec = value


class PlacementResult(vmodl.DynamicData):
    @property
    def recommendations(self) -> List[Recommendation]: ...
    @recommendations.setter
    def recommendations(self, value: List[Recommendation]):
        self._recommendations = value
    @property
    def drsFault(self) -> DrsFaults: ...
    @drsFault.setter
    def drsFault(self, value: DrsFaults):
        self._drsFault = value


class PlacementSpec(vmodl.DynamicData):
    @property
    def priority(self) -> vim.VirtualMachine.MovePriority: ...
    @priority.setter
    def priority(self, value: vim.VirtualMachine.MovePriority):
        self._priority = value
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def configSpec(self) -> vim.vm.ConfigSpec: ...
    @configSpec.setter
    def configSpec(self, value: vim.vm.ConfigSpec):
        self._configSpec = value
    @property
    def relocateSpec(self) -> vim.vm.RelocateSpec: ...
    @relocateSpec.setter
    def relocateSpec(self, value: vim.vm.RelocateSpec):
        self._relocateSpec = value
    @property
    def hosts(self) -> List[vim.HostSystem]: ...
    @hosts.setter
    def hosts(self, value: List[vim.HostSystem]):
        self._hosts = value
    @property
    def datastores(self) -> List[vim.Datastore]: ...
    @datastores.setter
    def datastores(self, value: List[vim.Datastore]):
        self._datastores = value
    @property
    def storagePods(self) -> List[vim.StoragePod]: ...
    @storagePods.setter
    def storagePods(self, value: List[vim.StoragePod]):
        self._storagePods = value
    @property
    def disallowPrerequisiteMoves(self) -> bool: ...
    @disallowPrerequisiteMoves.setter
    def disallowPrerequisiteMoves(self, value: bool):
        self._disallowPrerequisiteMoves = value
    @property
    def rules(self) -> List[RuleInfo]: ...
    @rules.setter
    def rules(self, value: List[RuleInfo]):
        self._rules = value
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def placementType(self) -> str: ...
    @placementType.setter
    def placementType(self, value: str):
        self._placementType = value
    @property
    def cloneSpec(self) -> vim.vm.CloneSpec: ...
    @cloneSpec.setter
    def cloneSpec(self, value: vim.vm.CloneSpec):
        self._cloneSpec = value
    @property
    def cloneName(self) -> str: ...
    @cloneName.setter
    def cloneName(self, value: str):
        self._cloneName = value


    class PlacementType(Enum):
        create = "create"
        reconfigure = "reconfigure"
        relocate = "relocate"
        clone = "clone"


class PowerOnVmResult(vmodl.DynamicData):
    @property
    def attempted(self) -> List[AttemptedVmInfo]: ...
    @attempted.setter
    def attempted(self, value: List[AttemptedVmInfo]):
        self._attempted = value
    @property
    def notAttempted(self) -> List[NotAttemptedVmInfo]: ...
    @notAttempted.setter
    def notAttempted(self, value: List[NotAttemptedVmInfo]):
        self._notAttempted = value
    @property
    def recommendations(self) -> List[Recommendation]: ...
    @recommendations.setter
    def recommendations(self, value: List[Recommendation]):
        self._recommendations = value


class PreemptibleVmPairInfo(vmodl.DynamicData):
    @property
    def id(self) -> int: ...
    @id.setter
    def id(self, value: int):
        self._id = value
    @property
    def monitoredVm(self) -> vim.VirtualMachine: ...
    @monitoredVm.setter
    def monitoredVm(self, value: vim.VirtualMachine):
        self._monitoredVm = value
    @property
    def preemptibleVm(self) -> vim.VirtualMachine: ...
    @preemptibleVm.setter
    def preemptibleVm(self, value: vim.VirtualMachine):
        self._preemptibleVm = value


class PreemptibleVmPairSpec(vim.option.ArrayUpdateSpec):
    @property
    def info(self) -> PreemptibleVmPairInfo: ...
    @info.setter
    def info(self, value: PreemptibleVmPairInfo):
        self._info = value


class ProactiveDrsConfigInfo(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value


class Recommendation(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def time(self) -> datetime: ...
    @time.setter
    def time(self, value: datetime):
        self._time = value
    @property
    def rating(self) -> int: ...
    @rating.setter
    def rating(self, value: int):
        self._rating = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def reasonText(self) -> str: ...
    @reasonText.setter
    def reasonText(self, value: str):
        self._reasonText = value
    @property
    def warningText(self) -> str: ...
    @warningText.setter
    def warningText(self, value: str):
        self._warningText = value
    @property
    def warningDetails(self) -> vmodl.LocalizableMessage: ...
    @warningDetails.setter
    def warningDetails(self, value: vmodl.LocalizableMessage):
        self._warningDetails = value
    @property
    def prerequisite(self) -> List[str]: ...
    @prerequisite.setter
    def prerequisite(self, value: List[str]):
        self._prerequisite = value
    @property
    def action(self) -> List[Action]: ...
    @action.setter
    def action(self, value: List[Action]):
        self._action = value
    @property
    def target(self) -> ManagedObject: ...
    @target.setter
    def target(self, value: ManagedObject):
        self._target = value


    class RecommendationType(Enum):
        V1 = "V1"


class ResourceUsageSummary(vmodl.DynamicData):
    @property
    def cpuUsedMHz(self) -> int: ...
    @cpuUsedMHz.setter
    def cpuUsedMHz(self, value: int):
        self._cpuUsedMHz = value
    @property
    def cpuCapacityMHz(self) -> int: ...
    @cpuCapacityMHz.setter
    def cpuCapacityMHz(self, value: int):
        self._cpuCapacityMHz = value
    @property
    def memUsedMB(self) -> int: ...
    @memUsedMB.setter
    def memUsedMB(self, value: int):
        self._memUsedMB = value
    @property
    def memCapacityMB(self) -> int: ...
    @memCapacityMB.setter
    def memCapacityMB(self, value: int):
        self._memCapacityMB = value
    @property
    def pMemAvailableMB(self) -> long: ...
    @pMemAvailableMB.setter
    def pMemAvailableMB(self, value: long):
        self._pMemAvailableMB = value
    @property
    def pMemCapacityMB(self) -> long: ...
    @pMemCapacityMB.setter
    def pMemCapacityMB(self, value: long):
        self._pMemCapacityMB = value
    @property
    def storageUsedMB(self) -> long: ...
    @storageUsedMB.setter
    def storageUsedMB(self, value: long):
        self._storageUsedMB = value
    @property
    def storageCapacityMB(self) -> long: ...
    @storageCapacityMB.setter
    def storageCapacityMB(self, value: long):
        self._storageCapacityMB = value


class RuleInfo(vmodl.DynamicData):
    @property
    def key(self) -> int: ...
    @key.setter
    def key(self, value: int):
        self._key = value
    @property
    def status(self) -> vim.ManagedEntity.Status: ...
    @status.setter
    def status(self, value: vim.ManagedEntity.Status):
        self._status = value
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def mandatory(self) -> bool: ...
    @mandatory.setter
    def mandatory(self, value: bool):
        self._mandatory = value
    @property
    def userCreated(self) -> bool: ...
    @userCreated.setter
    def userCreated(self, value: bool):
        self._userCreated = value
    @property
    def inCompliance(self) -> bool: ...
    @inCompliance.setter
    def inCompliance(self, value: bool):
        self._inCompliance = value
    @property
    def ruleUuid(self) -> str: ...
    @ruleUuid.setter
    def ruleUuid(self, value: str):
        self._ruleUuid = value


class RuleSpec(vim.option.ArrayUpdateSpec):
    @property
    def info(self) -> RuleInfo: ...
    @info.setter
    def info(self, value: RuleInfo):
        self._info = value


class SlotPolicy(vmodl.DynamicData): ...


class SystemVMsConfigInfo(vmodl.DynamicData):
    @property
    def allowedDatastores(self) -> List[vim.Datastore]: ...
    @allowedDatastores.setter
    def allowedDatastores(self, value: List[vim.Datastore]):
        self._allowedDatastores = value
    @property
    def notAllowedDatastores(self) -> List[vim.Datastore]: ...
    @notAllowedDatastores.setter
    def notAllowedDatastores(self, value: List[vim.Datastore]):
        self._notAllowedDatastores = value
    @property
    def dsTagCategoriesToExclude(self) -> List[str]: ...
    @dsTagCategoriesToExclude.setter
    def dsTagCategoriesToExclude(self, value: List[str]):
        self._dsTagCategoriesToExclude = value


class SystemVMsConfigSpec(vmodl.DynamicData):
    @property
    def allowedDatastores(self) -> List[DatastoreUpdateSpec]: ...
    @allowedDatastores.setter
    def allowedDatastores(self, value: List[DatastoreUpdateSpec]):
        self._allowedDatastores = value
    @property
    def notAllowedDatastores(self) -> List[DatastoreUpdateSpec]: ...
    @notAllowedDatastores.setter
    def notAllowedDatastores(self, value: List[DatastoreUpdateSpec]):
        self._notAllowedDatastores = value
    @property
    def dsTagCategoriesToExclude(self) -> List[TagCategoryUpdateSpec]: ...
    @dsTagCategoriesToExclude.setter
    def dsTagCategoriesToExclude(self, value: List[TagCategoryUpdateSpec]):
        self._dsTagCategoriesToExclude = value


class TagCategoryUpdateSpec(vim.option.ArrayUpdateSpec):
    @property
    def category(self) -> str: ...
    @category.setter
    def category(self, value: str):
        self._category = value


class UsageSummary(vmodl.DynamicData):
    @property
    def totalCpuCapacityMhz(self) -> int: ...
    @totalCpuCapacityMhz.setter
    def totalCpuCapacityMhz(self, value: int):
        self._totalCpuCapacityMhz = value
    @property
    def totalMemCapacityMB(self) -> int: ...
    @totalMemCapacityMB.setter
    def totalMemCapacityMB(self, value: int):
        self._totalMemCapacityMB = value
    @property
    def cpuReservationMhz(self) -> int: ...
    @cpuReservationMhz.setter
    def cpuReservationMhz(self, value: int):
        self._cpuReservationMhz = value
    @property
    def memReservationMB(self) -> int: ...
    @memReservationMB.setter
    def memReservationMB(self, value: int):
        self._memReservationMB = value
    @property
    def poweredOffCpuReservationMhz(self) -> int: ...
    @poweredOffCpuReservationMhz.setter
    def poweredOffCpuReservationMhz(self, value: int):
        self._poweredOffCpuReservationMhz = value
    @property
    def poweredOffMemReservationMB(self) -> int: ...
    @poweredOffMemReservationMB.setter
    def poweredOffMemReservationMB(self, value: int):
        self._poweredOffMemReservationMB = value
    @property
    def cpuDemandMhz(self) -> int: ...
    @cpuDemandMhz.setter
    def cpuDemandMhz(self, value: int):
        self._cpuDemandMhz = value
    @property
    def memDemandMB(self) -> int: ...
    @memDemandMB.setter
    def memDemandMB(self, value: int):
        self._memDemandMB = value
    @property
    def statsGenNumber(self) -> long: ...
    @statsGenNumber.setter
    def statsGenNumber(self, value: long):
        self._statsGenNumber = value
    @property
    def cpuEntitledMhz(self) -> int: ...
    @cpuEntitledMhz.setter
    def cpuEntitledMhz(self, value: int):
        self._cpuEntitledMhz = value
    @property
    def memEntitledMB(self) -> int: ...
    @memEntitledMB.setter
    def memEntitledMB(self, value: int):
        self._memEntitledMB = value
    @property
    def poweredOffVmCount(self) -> int: ...
    @poweredOffVmCount.setter
    def poweredOffVmCount(self, value: int):
        self._poweredOffVmCount = value
    @property
    def totalVmCount(self) -> int: ...
    @totalVmCount.setter
    def totalVmCount(self, value: int):
        self._totalVmCount = value


class VmComponentProtectionSettings(vmodl.DynamicData):
    @property
    def vmStorageProtectionForAPD(self) -> str: ...
    @vmStorageProtectionForAPD.setter
    def vmStorageProtectionForAPD(self, value: str):
        self._vmStorageProtectionForAPD = value
    @property
    def enableAPDTimeoutForHosts(self) -> bool: ...
    @enableAPDTimeoutForHosts.setter
    def enableAPDTimeoutForHosts(self, value: bool):
        self._enableAPDTimeoutForHosts = value
    @property
    def vmTerminateDelayForAPDSec(self) -> int: ...
    @vmTerminateDelayForAPDSec.setter
    def vmTerminateDelayForAPDSec(self, value: int):
        self._vmTerminateDelayForAPDSec = value
    @property
    def vmReactionOnAPDCleared(self) -> str: ...
    @vmReactionOnAPDCleared.setter
    def vmReactionOnAPDCleared(self, value: str):
        self._vmReactionOnAPDCleared = value
    @property
    def vmStorageProtectionForPDL(self) -> str: ...
    @vmStorageProtectionForPDL.setter
    def vmStorageProtectionForPDL(self, value: str):
        self._vmStorageProtectionForPDL = value


    class StorageVmReaction(Enum):
        disabled = "disabled"
        warning = "warning"
        restartConservative = "restartConservative"
        restartAggressive = "restartAggressive"
        clusterDefault = "clusterDefault"


    class VmReactionOnAPDCleared(Enum):
        none = "none"
        reset = "reset"
        useClusterDefault = "useClusterDefault"


class VmGroup(GroupInfo):
    @property
    def vm(self) -> List[vim.VirtualMachine]: ...
    @vm.setter
    def vm(self, value: List[vim.VirtualMachine]):
        self._vm = value


class VmHostRuleInfo(RuleInfo):
    @property
    def vmGroupName(self) -> str: ...
    @vmGroupName.setter
    def vmGroupName(self, value: str):
        self._vmGroupName = value
    @property
    def affineHostGroupName(self) -> str: ...
    @affineHostGroupName.setter
    def affineHostGroupName(self, value: str):
        self._affineHostGroupName = value
    @property
    def antiAffineHostGroupName(self) -> str: ...
    @antiAffineHostGroupName.setter
    def antiAffineHostGroupName(self, value: str):
        self._antiAffineHostGroupName = value


class VmOrchestrationInfo(vmodl.DynamicData):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def vmReadiness(self) -> VmReadiness: ...
    @vmReadiness.setter
    def vmReadiness(self, value: VmReadiness):
        self._vmReadiness = value


class VmOrchestrationSpec(vim.option.ArrayUpdateSpec):
    @property
    def info(self) -> VmOrchestrationInfo: ...
    @info.setter
    def info(self, value: VmOrchestrationInfo):
        self._info = value


class VmReadiness(vmodl.DynamicData):
    @property
    def readyCondition(self) -> str: ...
    @readyCondition.setter
    def readyCondition(self, value: str):
        self._readyCondition = value
    @property
    def postReadyDelay(self) -> int: ...
    @postReadyDelay.setter
    def postReadyDelay(self, value: int):
        self._postReadyDelay = value


    class ReadyCondition(Enum):
        none = "none"
        poweredOn = "poweredOn"
        guestHbStatusGreen = "guestHbStatusGreen"
        appHbStatusGreen = "appHbStatusGreen"
        useClusterDefault = "useClusterDefault"


class VmToolsMonitoringSettings(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def vmMonitoring(self) -> str: ...
    @vmMonitoring.setter
    def vmMonitoring(self, value: str):
        self._vmMonitoring = value
    @property
    def clusterSettings(self) -> bool: ...
    @clusterSettings.setter
    def clusterSettings(self, value: bool):
        self._clusterSettings = value
    @property
    def failureInterval(self) -> int: ...
    @failureInterval.setter
    def failureInterval(self, value: int):
        self._failureInterval = value
    @property
    def minUpTime(self) -> int: ...
    @minUpTime.setter
    def minUpTime(self, value: int):
        self._minUpTime = value
    @property
    def maxFailures(self) -> int: ...
    @maxFailures.setter
    def maxFailures(self, value: int):
        self._maxFailures = value
    @property
    def maxFailureWindow(self) -> int: ...
    @maxFailureWindow.setter
    def maxFailureWindow(self, value: int):
        self._maxFailureWindow = value