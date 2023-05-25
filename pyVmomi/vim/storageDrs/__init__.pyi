from typing import List, Literal
from enum import Enum
from pyVmomi import vim, vmodl
from pyVmomi.VmomiSupport import double, long


class ApplyRecommendationResult(vmodl.DynamicData):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value


class AutomationConfig(vmodl.DynamicData):
    @property
    def spaceLoadBalanceAutomationMode(self) -> str: ...
    @spaceLoadBalanceAutomationMode.setter
    def spaceLoadBalanceAutomationMode(self, value: str):
        self._spaceLoadBalanceAutomationMode = value
    @property
    def ioLoadBalanceAutomationMode(self) -> str: ...
    @ioLoadBalanceAutomationMode.setter
    def ioLoadBalanceAutomationMode(self, value: str):
        self._ioLoadBalanceAutomationMode = value
    @property
    def ruleEnforcementAutomationMode(self) -> str: ...
    @ruleEnforcementAutomationMode.setter
    def ruleEnforcementAutomationMode(self, value: str):
        self._ruleEnforcementAutomationMode = value
    @property
    def policyEnforcementAutomationMode(self) -> str: ...
    @policyEnforcementAutomationMode.setter
    def policyEnforcementAutomationMode(self, value: str):
        self._policyEnforcementAutomationMode = value
    @property
    def vmEvacuationAutomationMode(self) -> str: ...
    @vmEvacuationAutomationMode.setter
    def vmEvacuationAutomationMode(self, value: str):
        self._vmEvacuationAutomationMode = value


class ConfigInfo(vmodl.DynamicData):
    @property
    def podConfig(self) -> PodConfigInfo: ...
    @podConfig.setter
    def podConfig(self, value: PodConfigInfo):
        self._podConfig = value
    @property
    def vmConfig(self) -> List[VmConfigInfo]: ...
    @vmConfig.setter
    def vmConfig(self, value: List[VmConfigInfo]):
        self._vmConfig = value


class ConfigSpec(vmodl.DynamicData):
    @property
    def podConfigSpec(self) -> PodConfigSpec: ...
    @podConfigSpec.setter
    def podConfigSpec(self, value: PodConfigSpec):
        self._podConfigSpec = value
    @property
    def vmConfigSpec(self) -> List[VmConfigSpec]: ...
    @vmConfigSpec.setter
    def vmConfigSpec(self, value: List[VmConfigSpec]):
        self._vmConfigSpec = value


class HbrDiskMigrationAction(vim.cluster.Action):
    @property
    def collectionId(self) -> str: ...
    @collectionId.setter
    def collectionId(self, value: str):
        self._collectionId = value
    @property
    def collectionName(self) -> str: ...
    @collectionName.setter
    def collectionName(self, value: str):
        self._collectionName = value
    @property
    def diskIds(self) -> List[str]: ...
    @diskIds.setter
    def diskIds(self, value: List[str]):
        self._diskIds = value
    @property
    def source(self) -> vim.Datastore: ...
    @source.setter
    def source(self, value: vim.Datastore):
        self._source = value
    @property
    def destination(self) -> vim.Datastore: ...
    @destination.setter
    def destination(self, value: vim.Datastore):
        self._destination = value
    @property
    def sizeTransferred(self) -> long: ...
    @sizeTransferred.setter
    def sizeTransferred(self, value: long):
        self._sizeTransferred = value
    @property
    def spaceUtilSrcBefore(self) -> float: ...
    @spaceUtilSrcBefore.setter
    def spaceUtilSrcBefore(self, value: float):
        self._spaceUtilSrcBefore = value
    @property
    def spaceUtilDstBefore(self) -> float: ...
    @spaceUtilDstBefore.setter
    def spaceUtilDstBefore(self, value: float):
        self._spaceUtilDstBefore = value
    @property
    def spaceUtilSrcAfter(self) -> float: ...
    @spaceUtilSrcAfter.setter
    def spaceUtilSrcAfter(self, value: float):
        self._spaceUtilSrcAfter = value
    @property
    def spaceUtilDstAfter(self) -> float: ...
    @spaceUtilDstAfter.setter
    def spaceUtilDstAfter(self, value: float):
        self._spaceUtilDstAfter = value
    @property
    def ioLatencySrcBefore(self) -> float: ...
    @ioLatencySrcBefore.setter
    def ioLatencySrcBefore(self, value: float):
        self._ioLatencySrcBefore = value
    @property
    def ioLatencyDstBefore(self) -> float: ...
    @ioLatencyDstBefore.setter
    def ioLatencyDstBefore(self, value: float):
        self._ioLatencyDstBefore = value


class IoLoadBalanceConfig(vmodl.DynamicData):
    @property
    def reservablePercentThreshold(self) -> int: ...
    @reservablePercentThreshold.setter
    def reservablePercentThreshold(self, value: int):
        self._reservablePercentThreshold = value
    @property
    def reservableIopsThreshold(self) -> int: ...
    @reservableIopsThreshold.setter
    def reservableIopsThreshold(self, value: int):
        self._reservableIopsThreshold = value
    @property
    def reservableThresholdMode(self) -> str: ...
    @reservableThresholdMode.setter
    def reservableThresholdMode(self, value: str):
        self._reservableThresholdMode = value
    @property
    def ioLatencyThreshold(self) -> int: ...
    @ioLatencyThreshold.setter
    def ioLatencyThreshold(self, value: int):
        self._ioLatencyThreshold = value
    @property
    def ioLoadImbalanceThreshold(self) -> int: ...
    @ioLoadImbalanceThreshold.setter
    def ioLoadImbalanceThreshold(self, value: int):
        self._ioLoadImbalanceThreshold = value


class OptionSpec(vim.option.ArrayUpdateSpec):
    @property
    def option(self) -> vim.option.OptionValue: ...
    @option.setter
    def option(self, value: vim.option.OptionValue):
        self._option = value


class PlacementAffinityRule(vmodl.DynamicData):
    @property
    def ruleType(self) -> str: ...
    @ruleType.setter
    def ruleType(self, value: str):
        self._ruleType = value
    @property
    def ruleScope(self) -> str: ...
    @ruleScope.setter
    def ruleScope(self, value: str):
        self._ruleScope = value
    @property
    def vms(self) -> List[vim.VirtualMachine]: ...
    @vms.setter
    def vms(self, value: List[vim.VirtualMachine]):
        self._vms = value
    @property
    def keys(self) -> List[str]: ...
    @keys.setter
    def keys(self, value: List[str]):
        self._keys = value


    class RuleScope(Enum):
        cluster = "cluster"
        host = "host"
        storagePod = "storagePod"
        datastore = "datastore"


    class RuleType(Enum):
        affinity = "affinity"
        antiAffinity = "antiAffinity"
        softAffinity = "softAffinity"
        softAntiAffinity = "softAntiAffinity"


class PlacementRankResult(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def candidate(self) -> vim.ClusterComputeResource: ...
    @candidate.setter
    def candidate(self, value: vim.ClusterComputeResource):
        self._candidate = value
    @property
    def reservedSpaceMB(self) -> long: ...
    @reservedSpaceMB.setter
    def reservedSpaceMB(self, value: long):
        self._reservedSpaceMB = value
    @property
    def usedSpaceMB(self) -> long: ...
    @usedSpaceMB.setter
    def usedSpaceMB(self, value: long):
        self._usedSpaceMB = value
    @property
    def totalSpaceMB(self) -> long: ...
    @totalSpaceMB.setter
    def totalSpaceMB(self, value: long):
        self._totalSpaceMB = value
    @property
    def utilization(self) -> double: ...
    @utilization.setter
    def utilization(self, value: double):
        self._utilization = value
    @property
    def faults(self) -> List[vmodl.MethodFault]: ...
    @faults.setter
    def faults(self, value: List[vmodl.MethodFault]):
        self._faults = value


class PlacementRankSpec(vmodl.DynamicData):
    @property
    def specs(self) -> List[vim.cluster.PlacementSpec]: ...
    @specs.setter
    def specs(self, value: List[vim.cluster.PlacementSpec]):
        self._specs = value
    @property
    def clusters(self) -> List[vim.ClusterComputeResource]: ...
    @clusters.setter
    def clusters(self, value: List[vim.ClusterComputeResource]):
        self._clusters = value
    @property
    def rules(self) -> List[PlacementAffinityRule]: ...
    @rules.setter
    def rules(self, value: List[PlacementAffinityRule]):
        self._rules = value
    @property
    def placementRankByVm(self) -> List[PlacementRankVmSpec]: ...
    @placementRankByVm.setter
    def placementRankByVm(self, value: List[PlacementRankVmSpec]):
        self._placementRankByVm = value


class PlacementRankVmSpec(vmodl.DynamicData):
    @property
    def vmPlacementSpec(self) -> vim.cluster.PlacementSpec: ...
    @vmPlacementSpec.setter
    def vmPlacementSpec(self, value: vim.cluster.PlacementSpec):
        self._vmPlacementSpec = value
    @property
    def vmClusters(self) -> List[vim.ClusterComputeResource]: ...
    @vmClusters.setter
    def vmClusters(self, value: List[vim.ClusterComputeResource]):
        self._vmClusters = value


class PodConfigInfo(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def ioLoadBalanceEnabled(self) -> bool: ...
    @ioLoadBalanceEnabled.setter
    def ioLoadBalanceEnabled(self, value: bool):
        self._ioLoadBalanceEnabled = value
    @property
    def defaultVmBehavior(self) -> str: ...
    @defaultVmBehavior.setter
    def defaultVmBehavior(self, value: str):
        self._defaultVmBehavior = value
    @property
    def loadBalanceInterval(self) -> int: ...
    @loadBalanceInterval.setter
    def loadBalanceInterval(self, value: int):
        self._loadBalanceInterval = value
    @property
    def defaultIntraVmAffinity(self) -> bool: ...
    @defaultIntraVmAffinity.setter
    def defaultIntraVmAffinity(self, value: bool):
        self._defaultIntraVmAffinity = value
    @property
    def spaceLoadBalanceConfig(self) -> SpaceLoadBalanceConfig: ...
    @spaceLoadBalanceConfig.setter
    def spaceLoadBalanceConfig(self, value: SpaceLoadBalanceConfig):
        self._spaceLoadBalanceConfig = value
    @property
    def ioLoadBalanceConfig(self) -> IoLoadBalanceConfig: ...
    @ioLoadBalanceConfig.setter
    def ioLoadBalanceConfig(self, value: IoLoadBalanceConfig):
        self._ioLoadBalanceConfig = value
    @property
    def automationOverrides(self) -> AutomationConfig: ...
    @automationOverrides.setter
    def automationOverrides(self, value: AutomationConfig):
        self._automationOverrides = value
    @property
    def rule(self) -> List[vim.cluster.RuleInfo]: ...
    @rule.setter
    def rule(self, value: List[vim.cluster.RuleInfo]):
        self._rule = value
    @property
    def option(self) -> List[vim.option.OptionValue]: ...
    @option.setter
    def option(self, value: List[vim.option.OptionValue]):
        self._option = value


    class Behavior(Enum):
        manual = "manual"
        automated = "automated"


class PodConfigSpec(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def ioLoadBalanceEnabled(self) -> bool: ...
    @ioLoadBalanceEnabled.setter
    def ioLoadBalanceEnabled(self, value: bool):
        self._ioLoadBalanceEnabled = value
    @property
    def defaultVmBehavior(self) -> str: ...
    @defaultVmBehavior.setter
    def defaultVmBehavior(self, value: str):
        self._defaultVmBehavior = value
    @property
    def loadBalanceInterval(self) -> int: ...
    @loadBalanceInterval.setter
    def loadBalanceInterval(self, value: int):
        self._loadBalanceInterval = value
    @property
    def defaultIntraVmAffinity(self) -> bool: ...
    @defaultIntraVmAffinity.setter
    def defaultIntraVmAffinity(self, value: bool):
        self._defaultIntraVmAffinity = value
    @property
    def spaceLoadBalanceConfig(self) -> SpaceLoadBalanceConfig: ...
    @spaceLoadBalanceConfig.setter
    def spaceLoadBalanceConfig(self, value: SpaceLoadBalanceConfig):
        self._spaceLoadBalanceConfig = value
    @property
    def ioLoadBalanceConfig(self) -> IoLoadBalanceConfig: ...
    @ioLoadBalanceConfig.setter
    def ioLoadBalanceConfig(self, value: IoLoadBalanceConfig):
        self._ioLoadBalanceConfig = value
    @property
    def automationOverrides(self) -> AutomationConfig: ...
    @automationOverrides.setter
    def automationOverrides(self, value: AutomationConfig):
        self._automationOverrides = value
    @property
    def rule(self) -> List[vim.cluster.RuleSpec]: ...
    @rule.setter
    def rule(self, value: List[vim.cluster.RuleSpec]):
        self._rule = value
    @property
    def option(self) -> List[OptionSpec]: ...
    @option.setter
    def option(self, value: List[OptionSpec]):
        self._option = value


class PodSelectionSpec(vmodl.DynamicData):
    @property
    def initialVmConfig(self) -> List[PodSelectionSpec.VmPodConfig]: ...
    @initialVmConfig.setter
    def initialVmConfig(self, value: List[PodSelectionSpec.VmPodConfig]):
        self._initialVmConfig = value
    @property
    def storagePod(self) -> vim.StoragePod: ...
    @storagePod.setter
    def storagePod(self, value: vim.StoragePod):
        self._storagePod = value


    class DiskLocator(vmodl.DynamicData):
        @property
        def diskId(self) -> int: ...
        @diskId.setter
        def diskId(self, value: int):
            self._diskId = value
        @property
        def diskMoveType(self) -> str: ...
        @diskMoveType.setter
        def diskMoveType(self, value: str):
            self._diskMoveType = value
        @property
        def diskBackingInfo(self) -> vim.vm.device.VirtualDevice.BackingInfo: ...
        @diskBackingInfo.setter
        def diskBackingInfo(self, value: vim.vm.device.VirtualDevice.BackingInfo):
            self._diskBackingInfo = value
        @property
        def profile(self) -> List[vim.vm.ProfileSpec]: ...
        @profile.setter
        def profile(self, value: List[vim.vm.ProfileSpec]):
            self._profile = value


    class VmPodConfig(vmodl.DynamicData):
        @property
        def storagePod(self) -> vim.StoragePod: ...
        @storagePod.setter
        def storagePod(self, value: vim.StoragePod):
            self._storagePod = value
        @property
        def disk(self) -> List[PodSelectionSpec.DiskLocator]: ...
        @disk.setter
        def disk(self, value: List[PodSelectionSpec.DiskLocator]):
            self._disk = value
        @property
        def vmConfig(self) -> VmConfigInfo: ...
        @vmConfig.setter
        def vmConfig(self, value: VmConfigInfo):
            self._vmConfig = value
        @property
        def interVmRule(self) -> List[vim.cluster.RuleInfo]: ...
        @interVmRule.setter
        def interVmRule(self, value: List[vim.cluster.RuleInfo]):
            self._interVmRule = value


class SpaceLoadBalanceConfig(vmodl.DynamicData):
    @property
    def spaceThresholdMode(self) -> str: ...
    @spaceThresholdMode.setter
    def spaceThresholdMode(self, value: str):
        self._spaceThresholdMode = value
    @property
    def spaceUtilizationThreshold(self) -> int: ...
    @spaceUtilizationThreshold.setter
    def spaceUtilizationThreshold(self, value: int):
        self._spaceUtilizationThreshold = value
    @property
    def freeSpaceThresholdGB(self) -> int: ...
    @freeSpaceThresholdGB.setter
    def freeSpaceThresholdGB(self, value: int):
        self._freeSpaceThresholdGB = value
    @property
    def minSpaceUtilizationDifference(self) -> int: ...
    @minSpaceUtilizationDifference.setter
    def minSpaceUtilizationDifference(self, value: int):
        self._minSpaceUtilizationDifference = value


    class SpaceThresholdMode(Enum):
        utilization = "utilization"
        freeSpace = "freeSpace"


class StorageMigrationAction(vim.cluster.Action):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def relocateSpec(self) -> vim.vm.RelocateSpec: ...
    @relocateSpec.setter
    def relocateSpec(self, value: vim.vm.RelocateSpec):
        self._relocateSpec = value
    @property
    def source(self) -> vim.Datastore: ...
    @source.setter
    def source(self, value: vim.Datastore):
        self._source = value
    @property
    def destination(self) -> vim.Datastore: ...
    @destination.setter
    def destination(self, value: vim.Datastore):
        self._destination = value
    @property
    def sizeTransferred(self) -> long: ...
    @sizeTransferred.setter
    def sizeTransferred(self, value: long):
        self._sizeTransferred = value
    @property
    def spaceUtilSrcBefore(self) -> float: ...
    @spaceUtilSrcBefore.setter
    def spaceUtilSrcBefore(self, value: float):
        self._spaceUtilSrcBefore = value
    @property
    def spaceUtilDstBefore(self) -> float: ...
    @spaceUtilDstBefore.setter
    def spaceUtilDstBefore(self, value: float):
        self._spaceUtilDstBefore = value
    @property
    def spaceUtilSrcAfter(self) -> float: ...
    @spaceUtilSrcAfter.setter
    def spaceUtilSrcAfter(self, value: float):
        self._spaceUtilSrcAfter = value
    @property
    def spaceUtilDstAfter(self) -> float: ...
    @spaceUtilDstAfter.setter
    def spaceUtilDstAfter(self, value: float):
        self._spaceUtilDstAfter = value
    @property
    def ioLatencySrcBefore(self) -> float: ...
    @ioLatencySrcBefore.setter
    def ioLatencySrcBefore(self, value: float):
        self._ioLatencySrcBefore = value
    @property
    def ioLatencyDstBefore(self) -> float: ...
    @ioLatencyDstBefore.setter
    def ioLatencyDstBefore(self, value: float):
        self._ioLatencyDstBefore = value


class StoragePlacementAction(vim.cluster.Action):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def relocateSpec(self) -> vim.vm.RelocateSpec: ...
    @relocateSpec.setter
    def relocateSpec(self, value: vim.vm.RelocateSpec):
        self._relocateSpec = value
    @property
    def destination(self) -> vim.Datastore: ...
    @destination.setter
    def destination(self, value: vim.Datastore):
        self._destination = value
    @property
    def spaceUtilBefore(self) -> float: ...
    @spaceUtilBefore.setter
    def spaceUtilBefore(self, value: float):
        self._spaceUtilBefore = value
    @property
    def spaceDemandBefore(self) -> float: ...
    @spaceDemandBefore.setter
    def spaceDemandBefore(self, value: float):
        self._spaceDemandBefore = value
    @property
    def spaceUtilAfter(self) -> float: ...
    @spaceUtilAfter.setter
    def spaceUtilAfter(self, value: float):
        self._spaceUtilAfter = value
    @property
    def spaceDemandAfter(self) -> float: ...
    @spaceDemandAfter.setter
    def spaceDemandAfter(self, value: float):
        self._spaceDemandAfter = value
    @property
    def ioLatencyBefore(self) -> float: ...
    @ioLatencyBefore.setter
    def ioLatencyBefore(self, value: float):
        self._ioLatencyBefore = value


class StoragePlacementResult(vmodl.DynamicData):
    @property
    def recommendations(self) -> List[vim.cluster.Recommendation]: ...
    @recommendations.setter
    def recommendations(self, value: List[vim.cluster.Recommendation]):
        self._recommendations = value
    @property
    def drsFault(self) -> vim.cluster.DrsFaults: ...
    @drsFault.setter
    def drsFault(self, value: vim.cluster.DrsFaults):
        self._drsFault = value
    @property
    def task(self) -> vim.Task: ...
    @task.setter
    def task(self, value: vim.Task):
        self._task = value


class StoragePlacementSpec(vmodl.DynamicData):
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def priority(self) -> vim.VirtualMachine.MovePriority | Literal['lowPriority', 'highPriority', 'defaultPriority']: ...
    @priority.setter
    def priority(self, value: vim.VirtualMachine.MovePriority | Literal['lowPriority', 'highPriority', 'defaultPriority']):
        self._priority = value
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def podSelectionSpec(self) -> PodSelectionSpec: ...
    @podSelectionSpec.setter
    def podSelectionSpec(self, value: PodSelectionSpec):
        self._podSelectionSpec = value
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
    def resourcePool(self) -> vim.ResourcePool: ...
    @resourcePool.setter
    def resourcePool(self, value: vim.ResourcePool):
        self._resourcePool = value
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def folder(self) -> vim.Folder: ...
    @folder.setter
    def folder(self, value: vim.Folder):
        self._folder = value
    @property
    def disallowPrerequisiteMoves(self) -> bool: ...
    @disallowPrerequisiteMoves.setter
    def disallowPrerequisiteMoves(self, value: bool):
        self._disallowPrerequisiteMoves = value
    @property
    def resourceLeaseDurationSec(self) -> int: ...
    @resourceLeaseDurationSec.setter
    def resourceLeaseDurationSec(self, value: int):
        self._resourceLeaseDurationSec = value


    class PlacementType(Enum):
        create = "create"
        reconfigure = "reconfigure"
        relocate = "relocate"
        clone = "clone"


class VirtualDiskAntiAffinityRuleSpec(vim.cluster.RuleInfo):
    @property
    def diskId(self) -> List[int]: ...
    @diskId.setter
    def diskId(self, value: List[int]):
        self._diskId = value


class VirtualDiskRuleSpec(vim.cluster.RuleInfo):
    @property
    def diskRuleType(self) -> str: ...
    @diskRuleType.setter
    def diskRuleType(self, value: str):
        self._diskRuleType = value
    @property
    def diskId(self) -> List[int]: ...
    @diskId.setter
    def diskId(self, value: List[int]):
        self._diskId = value


class VmConfigInfo(vmodl.DynamicData):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
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
    def intraVmAffinity(self) -> bool: ...
    @intraVmAffinity.setter
    def intraVmAffinity(self, value: bool):
        self._intraVmAffinity = value
    @property
    def intraVmAntiAffinity(self) -> VirtualDiskAntiAffinityRuleSpec: ...
    @intraVmAntiAffinity.setter
    def intraVmAntiAffinity(self, value: VirtualDiskAntiAffinityRuleSpec):
        self._intraVmAntiAffinity = value
    @property
    def virtualDiskRules(self) -> List[VirtualDiskRuleSpec]: ...
    @virtualDiskRules.setter
    def virtualDiskRules(self, value: List[VirtualDiskRuleSpec]):
        self._virtualDiskRules = value


class VmConfigSpec(vim.option.ArrayUpdateSpec):
    @property
    def info(self) -> VmConfigInfo: ...
    @info.setter
    def info(self, value: VmConfigInfo):
        self._info = value