# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.cluster
import pyVmomi.vim.option
import pyVmomi.vim.vm
import pyVmomi.vim.vm.device



class ApplyRecommendationResult(pyVmomi.vmodl.DynamicData):
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None


class AutomationConfig(pyVmomi.vmodl.DynamicData):
   spaceLoadBalanceAutomationMode: _typing.Optional[str] = None
   ioLoadBalanceAutomationMode: _typing.Optional[str] = None
   ruleEnforcementAutomationMode: _typing.Optional[str] = None
   policyEnforcementAutomationMode: _typing.Optional[str] = None
   vmEvacuationAutomationMode: _typing.Optional[str] = None


class ConfigInfo(pyVmomi.vmodl.DynamicData):
   podConfig: PodConfigInfo
   vmConfig: list[VmConfigInfo] = []


class ConfigSpec(pyVmomi.vmodl.DynamicData):
   podConfigSpec: _typing.Optional[PodConfigSpec] = None
   vmConfigSpec: list[VmConfigSpec] = []


class HbrDiskMigrationAction(pyVmomi.vim.cluster.Action):
   collectionId: str
   collectionName: str
   diskIds: list[str] = []
   source: pyVmomi.vim.Datastore
   destination: pyVmomi.vim.Datastore
   sizeTransferred: pyVmomi.VmomiSupport.long
   spaceUtilSrcBefore: _typing.Optional[float] = None
   spaceUtilDstBefore: _typing.Optional[float] = None
   spaceUtilSrcAfter: _typing.Optional[float] = None
   spaceUtilDstAfter: _typing.Optional[float] = None
   ioLatencySrcBefore: _typing.Optional[float] = None
   ioLatencyDstBefore: _typing.Optional[float] = None


class IoLoadBalanceConfig(pyVmomi.vmodl.DynamicData):
   reservablePercentThreshold: _typing.Optional[int] = None
   reservableIopsThreshold: _typing.Optional[int] = None
   reservableThresholdMode: _typing.Optional[str] = None
   ioLatencyThreshold: _typing.Optional[int] = None
   ioLoadImbalanceThreshold: _typing.Optional[int] = None


class OptionSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   option: _typing.Optional[pyVmomi.vim.option.OptionValue] = None


class PlacementAffinityRule(pyVmomi.vmodl.DynamicData):
   class RuleType(pyVmomi.VmomiSupport.Enum):
      affinity: _typing.ClassVar['RuleType'] = 'affinity'
      antiAffinity: _typing.ClassVar['RuleType'] = 'antiAffinity'
      softAffinity: _typing.ClassVar['RuleType'] = 'softAffinity'
      softAntiAffinity: _typing.ClassVar['RuleType'] = 'softAntiAffinity'

   class RuleScope(pyVmomi.VmomiSupport.Enum):
      cluster: _typing.ClassVar['RuleScope'] = 'cluster'
      host: _typing.ClassVar['RuleScope'] = 'host'
      storagePod: _typing.ClassVar['RuleScope'] = 'storagePod'
      datastore: _typing.ClassVar['RuleScope'] = 'datastore'

   ruleType: str
   ruleScope: str
   vms: list[pyVmomi.vim.VirtualMachine] = []
   keys: list[str] = []


class PlacementRankResult(pyVmomi.vmodl.DynamicData):
   key: str
   candidate: pyVmomi.vim.ClusterComputeResource
   reservedSpaceMB: pyVmomi.VmomiSupport.long
   usedSpaceMB: pyVmomi.VmomiSupport.long
   totalSpaceMB: pyVmomi.VmomiSupport.long
   utilization: pyVmomi.VmomiSupport.double
   faults: list[pyVmomi.vmodl.MethodFault] = []


class PlacementRankSpec(pyVmomi.vmodl.DynamicData):
   specs: list[pyVmomi.vim.cluster.PlacementSpec] = []
   clusters: list[pyVmomi.vim.ClusterComputeResource] = []
   rules: list[PlacementAffinityRule] = []
   placementRankByVm: list[PlacementRankVmSpec] = []


class PlacementRankVmSpec(pyVmomi.vmodl.DynamicData):
   vmPlacementSpec: pyVmomi.vim.cluster.PlacementSpec
   vmClusters: list[pyVmomi.vim.ClusterComputeResource] = []


class PodConfigInfo(pyVmomi.vmodl.DynamicData):
   class Behavior(pyVmomi.VmomiSupport.Enum):
      manual: _typing.ClassVar['Behavior'] = 'manual'
      automated: _typing.ClassVar['Behavior'] = 'automated'

   enabled: bool
   ioLoadBalanceEnabled: bool
   defaultVmBehavior: str
   loadBalanceInterval: _typing.Optional[int] = None
   defaultIntraVmAffinity: _typing.Optional[bool] = None
   spaceLoadBalanceConfig: _typing.Optional[SpaceLoadBalanceConfig] = None
   ioLoadBalanceConfig: _typing.Optional[IoLoadBalanceConfig] = None
   automationOverrides: _typing.Optional[AutomationConfig] = None
   rule: list[pyVmomi.vim.cluster.RuleInfo] = []
   option: list[pyVmomi.vim.option.OptionValue] = []


class PodConfigSpec(pyVmomi.vmodl.DynamicData):
   enabled: _typing.Optional[bool] = None
   ioLoadBalanceEnabled: _typing.Optional[bool] = None
   defaultVmBehavior: _typing.Optional[str] = None
   loadBalanceInterval: _typing.Optional[int] = None
   defaultIntraVmAffinity: _typing.Optional[bool] = None
   spaceLoadBalanceConfig: _typing.Optional[SpaceLoadBalanceConfig] = None
   ioLoadBalanceConfig: _typing.Optional[IoLoadBalanceConfig] = None
   automationOverrides: _typing.Optional[AutomationConfig] = None
   rule: list[pyVmomi.vim.cluster.RuleSpec] = []
   option: list[OptionSpec] = []


class PodSelectionSpec(pyVmomi.vmodl.DynamicData):
   class VmPodConfig(pyVmomi.vmodl.DynamicData):
      storagePod: pyVmomi.vim.StoragePod
      disk: list[DiskLocator] = []
      vmConfig: _typing.Optional[VmConfigInfo] = None
      interVmRule: list[pyVmomi.vim.cluster.RuleInfo] = []

   class DiskLocator(pyVmomi.vmodl.DynamicData):
      diskId: int
      diskMoveType: _typing.Optional[str] = None
      diskBackingInfo: _typing.Optional[pyVmomi.vim.vm.device.VirtualDevice.BackingInfo] = None
      profile: list[pyVmomi.vim.vm.ProfileSpec] = []

   initialVmConfig: list[VmPodConfig] = []
   storagePod: _typing.Optional[pyVmomi.vim.StoragePod] = None


class SpaceLoadBalanceConfig(pyVmomi.vmodl.DynamicData):
   class SpaceThresholdMode(pyVmomi.VmomiSupport.Enum):
      utilization: _typing.ClassVar['SpaceThresholdMode'] = 'utilization'
      freeSpace: _typing.ClassVar['SpaceThresholdMode'] = 'freeSpace'

   spaceThresholdMode: _typing.Optional[str] = None
   spaceUtilizationThreshold: _typing.Optional[int] = None
   freeSpaceThresholdGB: _typing.Optional[int] = None
   minSpaceUtilizationDifference: _typing.Optional[int] = None


class StorageMigrationAction(pyVmomi.vim.cluster.Action):
   vm: pyVmomi.vim.VirtualMachine
   relocateSpec: pyVmomi.vim.vm.RelocateSpec
   source: pyVmomi.vim.Datastore
   destination: pyVmomi.vim.Datastore
   sizeTransferred: pyVmomi.VmomiSupport.long
   spaceUtilSrcBefore: _typing.Optional[float] = None
   spaceUtilDstBefore: _typing.Optional[float] = None
   spaceUtilSrcAfter: _typing.Optional[float] = None
   spaceUtilDstAfter: _typing.Optional[float] = None
   ioLatencySrcBefore: _typing.Optional[float] = None
   ioLatencyDstBefore: _typing.Optional[float] = None


class StoragePlacementAction(pyVmomi.vim.cluster.Action):
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   relocateSpec: pyVmomi.vim.vm.RelocateSpec
   destination: pyVmomi.vim.Datastore
   spaceUtilBefore: _typing.Optional[float] = None
   spaceDemandBefore: _typing.Optional[float] = None
   spaceUtilAfter: _typing.Optional[float] = None
   spaceDemandAfter: _typing.Optional[float] = None
   ioLatencyBefore: _typing.Optional[float] = None


class StoragePlacementResult(pyVmomi.vmodl.DynamicData):
   recommendations: list[pyVmomi.vim.cluster.Recommendation] = []
   drsFault: _typing.Optional[pyVmomi.vim.cluster.DrsFaults] = None
   task: _typing.Optional[pyVmomi.vim.Task] = None


class StoragePlacementSpec(pyVmomi.vmodl.DynamicData):
   class PlacementType(pyVmomi.VmomiSupport.Enum):
      create: _typing.ClassVar['PlacementType'] = 'create'
      reconfigure: _typing.ClassVar['PlacementType'] = 'reconfigure'
      relocate: _typing.ClassVar['PlacementType'] = 'relocate'
      clone: _typing.ClassVar['PlacementType'] = 'clone'

   type: str
   priority: _typing.Optional[pyVmomi.vim.VirtualMachine.MovePriority] = None
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   podSelectionSpec: PodSelectionSpec
   cloneSpec: _typing.Optional[pyVmomi.vim.vm.CloneSpec] = None
   cloneName: _typing.Optional[str] = None
   configSpec: _typing.Optional[pyVmomi.vim.vm.ConfigSpec] = None
   relocateSpec: _typing.Optional[pyVmomi.vim.vm.RelocateSpec] = None
   resourcePool: _typing.Optional[pyVmomi.vim.ResourcePool] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   folder: _typing.Optional[pyVmomi.vim.Folder] = None
   disallowPrerequisiteMoves: _typing.Optional[bool] = None
   resourceLeaseDurationSec: _typing.Optional[int] = None


class VirtualDiskAntiAffinityRuleSpec(pyVmomi.vim.cluster.RuleInfo):
   diskId: list[int] = []


class VirtualDiskRuleSpec(pyVmomi.vim.cluster.RuleInfo):
   class RuleType(pyVmomi.VmomiSupport.Enum):
      affinity: _typing.ClassVar['RuleType'] = 'affinity'
      antiAffinity: _typing.ClassVar['RuleType'] = 'antiAffinity'
      disabled: _typing.ClassVar['RuleType'] = 'disabled'

   diskRuleType: str
   diskId: list[int] = []


class VmConfigInfo(pyVmomi.vmodl.DynamicData):
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   enabled: _typing.Optional[bool] = None
   behavior: _typing.Optional[str] = None
   intraVmAffinity: _typing.Optional[bool] = None
   intraVmAntiAffinity: _typing.Optional[VirtualDiskAntiAffinityRuleSpec] = None
   virtualDiskRules: list[VirtualDiskRuleSpec] = []


class VmConfigSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   info: _typing.Optional[VmConfigInfo] = None
