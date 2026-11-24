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
   """
   Both `pyVmomi.vim.StorageResourceManager.recommendDatastores` and
   `pyVmomi.vim.Datastore.enterMaintenanceMode` methods may invoke Storage DRS
   for recommendations on placing or evacuating virtual disks.
   
   All initial placement recommendations, and some enterMaintenanceMode
   recommendations need to be approved by the user. Recommendations that
   are approved will be applied using the
   `pyVmomi.vim.StorageResourceManager.applyRecommendation`
   method.
   This class encapsulates the result of applying a subset of the
   recommendations.
   
   Attributes:
       vm: The result applying the recommendation, if it was successful.
           
           This is the equivalent of the `pyVmomi.vim.TaskInfo.result` key for the
           task launched when the recommendation was applied.
   """
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None


class AutomationConfig(pyVmomi.vmodl.DynamicData):
   """
   Storage DRS fine grain automation controls
   
   Attributes:
       spaceLoadBalanceAutomationMode: Specifies the behavior of Storage DRS when it generates
           recommendations for correcting space load imbalance in a
           datastore cluster.
           
           See `pyVmomi.vim.storageDrs.PodConfigInfo`. If specified, this option
           overrides the datastore cluster level automation behavior defined in the
           `pyVmomi.vim.storageDrs.PodConfigInfo`.
       ioLoadBalanceAutomationMode: Specifies the behavior of Storage DRS when it generates
           recommendations for correcting I/O load imbalance in a datastore
           cluster.
           
           See `pyVmomi.vim.storageDrs.PodConfigInfo`. If specified, this option
           overrides the datastore cluster level automation behavior defined in the
           `pyVmomi.vim.storageDrs.PodConfigInfo`.
       ruleEnforcementAutomationMode: Specifies the behavior of Storage DRS when it generates
           recommendations for correcting affinity rule violations in a
           datastore cluster.
           
           See `pyVmomi.vim.storageDrs.PodConfigInfo.Behavior`. If
           specified, this option overrides the datastore cluster level
           automation behavior defined in the `pyVmomi.vim.storageDrs.PodConfigInfo` for
           recommendations aimed at fixing rule violations.
       policyEnforcementAutomationMode: Specifies the behavior of Storage DRS when it generates
           recommendations for correcting storage and Vm policy violations
           in a datastore cluster.
           
           See `pyVmomi.vim.storageDrs.PodConfigInfo.Behavior`. If
           specified, this option overrides the datastore cluster level
           automation behavior defined in the `pyVmomi.vim.storageDrs.PodConfigInfo` for
           recommendations aimed at fixing storage policy violations.
       vmEvacuationAutomationMode: Specifies the behavior of Storage DRS when it generates
           recommendations for datastore evacuations in a datastore
           cluster.
           
           See `pyVmomi.vim.storageDrs.PodConfigInfo.Behavior`. If specified, this
           option overrides the datastore cluster level automation behavior
           defined in the `pyVmomi.vim.storageDrs.PodConfigInfo` for recommendations aimed at
           evacuating Vms from a datastore.
   """
   spaceLoadBalanceAutomationMode: _typing.Optional[str] = None
   ioLoadBalanceAutomationMode: _typing.Optional[str] = None
   ruleEnforcementAutomationMode: _typing.Optional[str] = None
   policyEnforcementAutomationMode: _typing.Optional[str] = None
   vmEvacuationAutomationMode: _typing.Optional[str] = None


class ConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.storageDrs.ConfigInfo` data object describes storage DRS configuration
   for a pod `pyVmomi.vim.StoragePod`.
   
   Attributes:
       podConfig: Pod-wide configuration of the storage DRS service.
       vmConfig: List of virtual machine configurations for the storage DRS
           service.
           
           Each entry applies to all the virtual disks of the virtual machine
           on this pod.
           
           If a virtual machine is not specified in this array, the service uses
           the default settings for that virtual machine.
   """
   podConfig: PodConfigInfo
   vmConfig: list[VmConfigInfo] = []


class ConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.storageDrs.ConfigSpec` data object provides a set of update
   specifications for storage DRS configuration.
   
   To support
   incremental changes, these properties are all optional.
   
   Attributes:
       podConfigSpec: Changes to the configuration of the storage DRS service.
       vmConfigSpec: Changes to the per-virtual-machine storage DRS settings.
   """
   podConfigSpec: _typing.Optional[PodConfigSpec] = None
   vmConfigSpec: list[VmConfigSpec] = []


class HbrDiskMigrationAction(pyVmomi.vim.cluster.Action):
   """
   Describes a single HBR secondary disk migration action.
   
   The storage migration
   action applies either to a single disk or a set of secondary virtual disks.
   
   Attributes:
       collectionId: HMS Service specific collection id
       collectionName: HMS specific name of this collection
       diskIds: HBR disk ids of secondary disks moved by this action
       source: Source datastore.
       destination: Destination datastore.
       sizeTransferred: The amount of data to be transferred.
           
           Unit: KB.
       spaceUtilSrcBefore: Space utilization on the source datastore before storage migration.
           
           Unit: percentage. For example, if set to 70.0, space utilization is 70%.
           If not set, the value is not available.
       spaceUtilDstBefore: Space utilization on the destination datastore before storage migration.
           
           Unit: percentage. For example, if set to 70.0, space utilization is 70%.
           If not set, the value is not available.
       spaceUtilSrcAfter: Expected space utilization on the source datastore after storage migration.
           
           Unit: percentage. For example, if set to 70.0, space utilization is 70%.
           If not set, the value is not available.
       spaceUtilDstAfter: Expected space utilization on the destination datastore after storage migration.
           
           Unit: percentage. For example, if set to 70.0, space utilization is 70%.
           If not set, the value is not available.
       ioLatencySrcBefore: I/O latency on the source datastore before storage migration.
           
           Unit: millisecond.
           If not set, the value is not available.
       ioLatencyDstBefore: I/O latency on the destination datastore before storage migration.
           
           Unit: millisecond.
           If not set, the value is not available.
   """
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
   """
   Deprecated: As of vSphere8.0 U3, and there is no replacement for it.Storage DRS configuration for I/O load balancing.
   
   Attributes:
       reservablePercentThreshold: Storage DRS makes storage migration recommendations if total
           IOPs reservation of all VMs running on a datastore is higher than
           the specified threshold.
           
           Storage DRS recommends migration out of
           all such datastores, if more than one datastore exceed their reserved
           IOPs threshold.
           
           The actual Iops used to determine threshold are computed from Storage
           DRS estimation of IOPs capacity of a datastore. The absolute value
           may change over time, according to storage response to workloads.
           
           The valid values are in the range of 30 (i.e., 30%) to 100 (i.e., 100%).
           If not specified, the default value is 60%.
       reservableIopsThreshold: Storage DRS makes storage migration recommendations if total
           IOPs reservation of all VMs running on a datastore is higher than
           the specified threshold.
           
           Storage DRS recommends migration out of
           all such datastores, if more than one datastore exceed their reserved
           IOPs threshold.
           
           This is an advanced option, and should only be used if Storage DRS
           estimated IOPs capacity is incorrect for datastores. The value
           should be based on conservative estimate of storage performance,
           and ideally should be set to about 50-60% of worse case peak
           performance of backing LUN.
       reservableThresholdMode: Determines which reservation threshold specification to use.
           
           See `pyVmomi.vim.storageDrs.PodConfigInfo.Behavior`. If unspecified, the
           mode is assumed automatic by default. Storage DRS uses
           percentage value in that case.
           If mode is specified, but corresponding reservationThreshold
           value is absent, option specific defaults are used.
       ioLatencyThreshold: Storage DRS makes storage migration recommendations if
           I/O latency on one (or more) of the datastores is higher than
           the specified threshold.
           
           Unit: millisecond.
           The valid values are in the range of 5 to 100. If not specified,
           the default value is 15.
       ioLoadImbalanceThreshold: Storage DRS makes storage migration recommendations if
           I/O load imbalance level is higher than the specified threshold.
           
           Unit: a number.
           The valid values are in the range of 1 to 100. If not specified,
           the default value is 5.
   """
   reservablePercentThreshold: _typing.Optional[int] = None
   reservableIopsThreshold: _typing.Optional[int] = None
   reservableThresholdMode: _typing.Optional[str] = None
   ioLatencyThreshold: _typing.Optional[int] = None
   ioLoadImbalanceThreshold: _typing.Optional[int] = None


class OptionSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """An incremental update to the advance settings."""
   option: _typing.Optional[pyVmomi.vim.option.OptionValue] = None


class PlacementAffinityRule(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.storageDrs.PlacementAffinityRule` data object specifies
   affinity rules for placement
   
   Attributes:
       ruleType: Type of affinity rule.
           
           The set of possible values are described in
           `pyVmomi.vim.storageDrs.PlacementAffinityRule.RuleType`
       ruleScope: Scope of the affinity rule.
           
           The set of possible values are described in
           `pyVmomi.vim.storageDrs.PlacementAffinityRule.RuleScope`
       vms: List of virtual machines that are part of this rule.
       keys: List of PlacementSpec keys that are part of this rule representing
           virtual machines yet to be placed.
   """
   class RuleType(pyVmomi.VmomiSupport.Enum):
      """
      Rule type determines how the affinity rule is to be enforced:
      affinity: Vms in the list are kept together within the rule
      scope.
      
      anti-affinity: Vms in the rule list are kept separate
      across the objects in the rule scope.
      soft rule: The enforcement is best effort.
      
      Attributes:
          affinity: Affinity
          antiAffinity: Anti-Affinity
          softAffinity: Best-effort affinity
          softAntiAffinity: Best-effort anti-affinity
      """
      affinity: _typing.ClassVar['PlacementAffinityRule.RuleType'] = 'affinity'
      antiAffinity: _typing.ClassVar['PlacementAffinityRule.RuleType'] = 'antiAffinity'
      softAffinity: _typing.ClassVar['PlacementAffinityRule.RuleType'] = 'softAffinity'
      softAntiAffinity: _typing.ClassVar['PlacementAffinityRule.RuleType'] = 'softAntiAffinity'

   class RuleScope(pyVmomi.VmomiSupport.Enum):
      """
      Rule scope determines conditions when an affinity rule is
      satisfied.
      
      The following uses affinity rule as example.
      cluster: All Vms in the rule list are placed in a single cluster.
      host: All Vms in the rule list are placed in a single host.
      storagePod: All Vms in the rule list are placed in a single storagePod.
      datastore: All Vms in the rule list are placed in a single datastore.
      
      Attributes:
          cluster: clusters are the scope
          host: individual hosts are the scope
          storagePod: datastore cluster is the scope
          datastore: individual datastores are the scope
      """
      cluster: _typing.ClassVar['PlacementAffinityRule.RuleScope'] = 'cluster'
      host: _typing.ClassVar['PlacementAffinityRule.RuleScope'] = 'host'
      storagePod: _typing.ClassVar['PlacementAffinityRule.RuleScope'] = 'storagePod'
      datastore: _typing.ClassVar['PlacementAffinityRule.RuleScope'] = 'datastore'

   ruleType: str
   ruleScope: str
   vms: list[pyVmomi.vim.VirtualMachine] = []
   keys: list[str] = []


class PlacementRankResult(pyVmomi.vmodl.DynamicData):
   """
   PlacementRankResult is the class of the result returned by
   the vCenter Server for rankClustersForPlacement method
   
   Attributes:
       key: Reference key for the placement request
       candidate: Candidate cluster for the placement problem
       reservedSpaceMB: The reserved storage space for the candidate cluster after placement
           The unit is in Megabytes
       usedSpaceMB: The expected space usage for the candidate cluster after placement
           The unit is in Megabytes
       totalSpaceMB: The expected total space for the candidate cluster after placement
           The unit is in Megabytes
       utilization: The expected aggregate resource utilization for the candidate cluster
           after placement
           The unit is a fractional value between 0 and 1.
       faults: Information about why a given cluster is not recommended for
           placement
   """
   key: str
   candidate: pyVmomi.vim.ClusterComputeResource
   reservedSpaceMB: pyVmomi.VmomiSupport.long
   usedSpaceMB: pyVmomi.VmomiSupport.long
   totalSpaceMB: pyVmomi.VmomiSupport.long
   utilization: pyVmomi.VmomiSupport.double
   faults: list[pyVmomi.vmodl.MethodFault] = []


class PlacementRankSpec(pyVmomi.vmodl.DynamicData):
   """
   PlacementRankSpec encapsulates all of the inputs passed to
   the `pyVmomi.vim.StorageResourceManager.rankForPlacement` method.
   
   Attributes:
       specs: List of VM placement specifications for ranking clusters
       clusters: List of candidate clusters for the placement request
       rules: List of affinity rules for the placement request
       placementRankByVm: List of preferred clusters for individual VM placement requests
   """
   specs: list[pyVmomi.vim.cluster.PlacementSpec] = []
   clusters: list[pyVmomi.vim.ClusterComputeResource] = []
   rules: list[PlacementAffinityRule] = []
   placementRankByVm: list[PlacementRankVmSpec] = []


class PlacementRankVmSpec(pyVmomi.vmodl.DynamicData):
   """
   Attributes:
       vmPlacementSpec: Individual VM placement specification for ranking clusters
       vmClusters: Set of candidate clusters for the placement request
   """
   vmPlacementSpec: pyVmomi.vim.cluster.PlacementSpec
   vmClusters: list[pyVmomi.vim.ClusterComputeResource] = []


class PodConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.storageDrs.PodConfigInfo` data object contains pod-wide configuration information
   for the storage DRS service.
   
   Attributes:
       enabled: Flag indicating whether or not storage DRS is enabled.
       ioLoadBalanceEnabled: Flag indicating whether or not storage DRS takes into account storage I/O
           workload when making load balancing and initial placement recommendations.
       defaultVmBehavior: Specifies the pod-wide default storage DRS behavior for virtual machines.
           
           For currently supported storage DRS behavior, see `pyVmomi.vim.storageDrs.PodConfigInfo.Behavior`.
           You can override the default behavior for a virtual machine
           by using the `pyVmomi.vim.storageDrs.VmConfigInfo` object.
       loadBalanceInterval: Specify the interval that storage DRS runs to load balance among datastores
           within a storage pod.
           
           Unit: minute.
           The valid values are from 60 (1 hour) to 43200 (30 days).
           If not specified, the default value is 480 (8 hours).
       defaultIntraVmAffinity: Specifies whether or not each virtual machine in this pod should have its virtual
           disks on the same datastore by default.
           
           If set to true, virtual machines will have
           all their virtual disks on the same datastore. If set to false, the virtual disks
           of a virtual machine may or may not be placed on the same datastore.
           If not set, the default value is true.
           You can override the default behavior for a virtual machine
           by using the `pyVmomi.vim.storageDrs.VmConfigInfo` object.
       spaceLoadBalanceConfig: The configuration settings for load balancing storage space.
       ioLoadBalanceConfig: The configuration settings for load balancing I/O workload.
           
           This takes effect only if `pyVmomi.vim.storageDrs.PodConfigInfo.ioLoadBalanceEnabled` is `true`.
       automationOverrides: Configuration settings for fine-grain automation overrides on
           the cluster level setting.
       rule: Pod-wide rules.
       option: Advanced settings.
   """
   class Behavior(pyVmomi.VmomiSupport.Enum):
      """
      Storage DRS behavior.
      
      Attributes:
          manual: Specifies that VirtualCenter should generate recommendations for
              virtual disk migration and for placement with a datastore,
              but should not execute the recommendations automatically.
          automated: Specifies that VirtualCenter should generate recommendations
              for virtual disk migration and for placement with a
              datastore.
              
              The recommendations for virtual disk migrations
              will be executed automatically, but the placement
              recommendations will be done manually.
      """
      manual: _typing.ClassVar['PodConfigInfo.Behavior'] = 'manual'
      automated: _typing.ClassVar['PodConfigInfo.Behavior'] = 'automated'

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
   """
   The `pyVmomi.vim.storageDrs.PodConfigSpec` data object provides a set of update
   specifications for pod-wide storage DRS configuration.
   
   To support
   incremental changes, these properties are all optional.
   
   Attributes:
       enabled: Flag indicating whether or not storage DRS is enabled.
       ioLoadBalanceEnabled: Flag indicating whether or not storage DRS takes into account storage I/O
           workload when making load balancing and initial placement recommendations.
       defaultVmBehavior: Specifies the pod-wide default storage DRS behavior for virtual machines.
           
           For currently supported storage DRS behavior, see `pyVmomi.vim.storageDrs.PodConfigInfo.Behavior`.
           You can override the default behavior for a virtual machine
           by using the `pyVmomi.vim.storageDrs.VmConfigInfo` object.
       loadBalanceInterval: Specify the interval that storage DRS runs to load balance among datastores
           within a storage pod.
       defaultIntraVmAffinity: Specifies whether or not each virtual machine in this pod should have its virtual
           disks on the same datastore by default.
       spaceLoadBalanceConfig: The configuration settings for load balancing storage space.
       ioLoadBalanceConfig: The configuration settings for load balancing I/O workload.
           
           This takes effect only if `pyVmomi.vim.storageDrs.PodConfigInfo.ioLoadBalanceEnabled` is `true`.
       automationOverrides: Configuration settings for fine-grain automation overrides on
           the cluster level setting.
       rule: Changes to the set of rules.
       option: Changes to advance settings.
   """
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
   """
   Specification for moving or copying a virtual machine to a different Storage Pod.
   
   Attributes:
       initialVmConfig: An optional list that allows specifying the storage pod location
           for each virtual disk and the VM configurations and overrides to be
           used during placement.
       storagePod: The storage pod where the virtual machine should be located.
   """
   class VmPodConfig(pyVmomi.vmodl.DynamicData):
      """
      Initial VM configuration for the specified pod.
      
      This configuration will be saved to the pod config
      `pyVmomi.vim.storageDrs.ConfigInfo`
      when the placement recommendations are applied.
      
      Attributes:
          storagePod: The pod that this initial configuration applies to.
              
              Since there could be multiple pods in a single placement request,
              we may need to specify multiple initial VM configurations, one per
              pod.
          disk: Array of PodDiskLocator objects.
          vmConfig: The VM configuration for the VM that is being placed.
          interVmRule: The initial interVmRules that should during placement of this
              virtual machine.
              
              It may not always be possible to specify that the
              virtual machine being placed is part of the rule because the
              virtual machine may not have been created yet. So for simplicity,
              we assume the virtual machine being placed is always implicitly
              part of any rule specified. It will be explicitly added to the
              rule before it is saved to the pod config.
      """
      storagePod: pyVmomi.vim.StoragePod
      disk: list[PodSelectionSpec.DiskLocator] = []
      vmConfig: _typing.Optional[VmConfigInfo] = None
      interVmRule: list[pyVmomi.vim.cluster.RuleInfo] = []

   class DiskLocator(pyVmomi.vmodl.DynamicData):
      """
      The disk locator class.
      
      Attributes:
          diskId: The disk ID.
          diskMoveType: The disk move type.
          diskBackingInfo: The disk backing info.
          profile: Virtual Disk Profile requirement.
              
              Profiles are solution specific.
              Profile Based Storage Management is a vSphere server extension.
              The API users who want to provision VMs using Storage Profiles, need to
              interact with it.
              This is an optional parameter and if user doesn't specify profile,
              the default behavior will apply.
      """
      diskId: int
      diskMoveType: _typing.Optional[str] = None
      diskBackingInfo: _typing.Optional[pyVmomi.vim.vm.device.VirtualDevice.BackingInfo] = None
      profile: list[pyVmomi.vim.vm.ProfileSpec] = []

   initialVmConfig: list[PodSelectionSpec.VmPodConfig] = []
   storagePod: _typing.Optional[pyVmomi.vim.StoragePod] = None


class SpaceLoadBalanceConfig(pyVmomi.vmodl.DynamicData):
   """
   Storage DRS configuration for space load balancing.
   
   Attributes:
       spaceUtilizationThreshold: Storage DRS makes storage migration recommendations if
           space utilization on one (or more) of the datastores is higher than
           the specified threshold.
           
           The valid values are in the range of 50 (i.e., 50%) to 100 (i.e., 100%).
           If not specified, the default value is 80%.
       freeSpaceThresholdGB: Storage DRS makes storage migration recommendations if
           free space on one (or more) of the datastores falls below
           the specified threshold.
           
           The unit is in gigabytes and the minimum value is 1GB.
           The maximum value is limited by the capacity of the smallest
           datastore in a datastore cluster.
           If not specified, the default value is 50GB.
       minSpaceUtilizationDifference: Storage DRS considers making storage migration recommendations if
           the difference in space utilization between the source and destination datastores
           is higher than the specified threshold.
           
           The valid values are in the range of 1 (i.e., 1%) to 50 (i.e., 50%).
           If not specified, the default value is 5%.
   """
   class SpaceThresholdMode(pyVmomi.VmomiSupport.Enum):
      """
      Defines the two ways a space utilization threshold can be specified.
      
      Attributes:
          utilization: Default mode: threshold as a percentage of datastore capacity
          freeSpace: Threshold as an absolute value of free space in GBs
      """
      utilization: _typing.ClassVar['SpaceLoadBalanceConfig.SpaceThresholdMode'] = 'utilization'
      freeSpace: _typing.ClassVar['SpaceLoadBalanceConfig.SpaceThresholdMode'] = 'freeSpace'

   spaceThresholdMode: _typing.Optional[str] = None
   spaceUtilizationThreshold: _typing.Optional[int] = None
   freeSpaceThresholdGB: _typing.Optional[int] = None
   minSpaceUtilizationDifference: _typing.Optional[int] = None


class StorageMigrationAction(pyVmomi.vim.cluster.Action):
   """
   Describes a single storage migration action.
   
   The storage migration
   action applies either to a virtual machine or a set of virtual disks.
   
   Attributes:
       vm: Virtual machine reference.
       relocateSpec: Specification for moving a virtual machine or a set of virtual disks
           to a different datastore.
       source: Source datastore.
       destination: Destination datastore.
       sizeTransferred: The amount of data to be transferred.
           
           Unit: KB.
       spaceUtilSrcBefore: Space utilization on the source datastore before storage migration.
           
           Unit: percentage. For example, if set to 70.0, space utilization is 70%.
           If not set, the value is not available.
       spaceUtilDstBefore: Space utilization on the destination datastore before storage migration.
           
           Unit: percentage. For example, if set to 70.0, space utilization is 70%.
           If not set, the value is not available.
       spaceUtilSrcAfter: Expected space utilization on the source datastore after storage migration.
           
           Unit: percentage. For example, if set to 70.0, space utilization is 70%.
           If not set, the value is not available.
       spaceUtilDstAfter: Expected space utilization on the destination datastore after storage migration.
           
           Unit: percentage. For example, if set to 70.0, space utilization is 70%.
           If not set, the value is not available.
       ioLatencySrcBefore: I/O latency on the source datastore before storage migration.
           
           Unit: millisecond.
           If not set, the value is not available.
       ioLatencyDstBefore: I/O latency on the destination datastore before storage migration.
           
           Unit: millisecond.
           If not set, the value is not available.
   """
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
   """
   Describes a single storage initial placement action for placing a virtual
   machine or a set of virtual disks on a datastore.
   
   Attributes:
       vm: Virtual machine reference.
           
           It is possible that the VM has not been created, in which case,
           this property is left unset.
       relocateSpec: Specification for placing a virtual machine or a set of virtual disks
           to a datastore.
       destination: Target datastore.
       spaceUtilBefore: Current space utilization on the target datastore.
           
           Unit: percentage. For example, if set to 70.0, space utilization is 70%.
           If not set, the value is not available.
       spaceDemandBefore: Current space demand on the target datastore.
           
           Unit: percentage. For example, if set to 70.0, space demand is 70%. This
           value include the space demanded by thin provisioned VMs. Hence, it may
           be higher than 100%. If not set, the value is not available.
       spaceUtilAfter: Space utilization on the target datastore after placing the virtual disk.
           
           Unit: percentage. For example, if set to 70.0, space utilization is 70%.
           If not set, the value is not available.
       spaceDemandAfter: Space demand on the target datastore after placing the virtual disk.
           
           Unit: percentage. For example, if set to 70.0, space demand is 70%. This
           value include the space demanded by thin provisioned VMs. Hence, it may
           be higher than 100%. If not set, the value is not available.
       ioLatencyBefore: Current I/O latency on the target datastore.
           
           Unit: millisecond.
           If not set, the value is not available.
   """
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   relocateSpec: pyVmomi.vim.vm.RelocateSpec
   destination: pyVmomi.vim.Datastore
   spaceUtilBefore: _typing.Optional[float] = None
   spaceDemandBefore: _typing.Optional[float] = None
   spaceUtilAfter: _typing.Optional[float] = None
   spaceDemandAfter: _typing.Optional[float] = None
   ioLatencyBefore: _typing.Optional[float] = None


class StoragePlacementResult(pyVmomi.vmodl.DynamicData):
   """
   Both `pyVmomi.vim.StorageResourceManager.recommendDatastores` and
   `pyVmomi.vim.Datastore.enterMaintenanceMode` methods may invoke Storage DRS
   for recommendations on placing or evacuating virtual disks.
   
   StoragePlacementResult is the class of the result returned by
   the methods.
   
   Attributes:
       recommendations: The list of recommendations that the client needs to approve manually.
       drsFault: Information about any fault in case Storage DRS failed to make a recommendation.
       task: The ID of the task, which monitors the storage placement or datastore entering
           maintennace mode operation.
   """
   recommendations: list[pyVmomi.vim.cluster.Recommendation] = []
   drsFault: _typing.Optional[pyVmomi.vim.cluster.DrsFaults] = None
   task: _typing.Optional[pyVmomi.vim.Task] = None


class StoragePlacementSpec(pyVmomi.vmodl.DynamicData):
   """
   StoragePlacementSpec encapsulates all of the inputs passed to the
   `pyVmomi.vim.StorageResourceManager.recommendDatastores` method.
   
   Attributes:
       type: The storage placement type.
           
           The set of possible values is described in
           `pyVmomi.vim.storageDrs.StoragePlacementSpec.PlacementType`
       priority: Priority of this placement operation.
       vm: The relevant virtual machine.
       podSelectionSpec: Specification for moving a virtual machine or a set of virtual disks
           to a different storage pod.
       cloneSpec: Specification for a virtual machine cloning operation.
       cloneName: Name for cloned virtual machine.
       configSpec: Configuration for the virtual machine.
       relocateSpec: Specification for relocating a virtual machine.
       resourcePool: The resource pool to which this virtual machine should be attached.
       host: The target host for the virtual machine.
       folder: The target virtual machine folder for the virtual machine.
           
           Note that this is a different folder than the pod(s) that the virtual
           machine belongs to. The pod mapping represents the storage view of
           the virtual machine, while the virtual machine folder mapping
           represents an inventory view of the virtual machine.
           For manual VM provisioning operations, this is specified implicitly
           as the object that the `pyVmomi.vim.Folder.createVm` method is invoked on.
       disallowPrerequisiteMoves: Specification for whether to disable pre-requisite storage vmotions
           for storage placements.
           
           If unset, default behavior is to allow such
           prerequisite moves.
       resourceLeaseDurationSec: Resource lease duration in seconds.
           
           If the duration is within bounds,
           Storage DRS will hold onto resources needed for applying recommendations
           generated as part of that call.
           Only initial placement recommendations generated by storage DRS can reserve
           resources this way.
   """
   class PlacementType(pyVmomi.VmomiSupport.Enum):
      """
      Defines the storage placement operation type.
      
      Attributes:
          create: Create a VM.
          reconfigure: Reconfigure a VM.
          relocate: Relocate a VM.
          clone: Clone a VM.
      """
      create: _typing.ClassVar['StoragePlacementSpec.PlacementType'] = 'create'
      reconfigure: _typing.ClassVar['StoragePlacementSpec.PlacementType'] = 'reconfigure'
      relocate: _typing.ClassVar['StoragePlacementSpec.PlacementType'] = 'relocate'
      clone: _typing.ClassVar['StoragePlacementSpec.PlacementType'] = 'clone'

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
   """
   Pod-wide anit-affinity rule for virtual disks.
   
   The set of virtual disks should
   be placed on different datastores.
   
   Attributes:
       diskId: The list of virtual disks.
   """
   diskId: list[int] = []


class VirtualDiskRuleSpec(pyVmomi.vim.cluster.RuleInfo):
   """
   The set of virtual disks that are currently disabled
   
   Attributes:
       diskRuleType: Type of the virtual disks rule.
           
           The set of possible values are described
           in `pyVmomi.vim.storageDrs.VirtualDiskRuleSpec.RuleType`
       diskId: The list of virtual disks for this rule.
   """
   class RuleType(pyVmomi.VmomiSupport.Enum):
      """
      Rule type determines how the virtual disks in a vm can be grouped
      together.
      
      Attributes:
          affinity: Virtual disks in the list are grouped together and placed on
              the same data store.
          antiAffinity: Virtual disks in the list are placed on different data stores.
          disabled: SDRS will be disabled for the disks in the list.
      """
      affinity: _typing.ClassVar['VirtualDiskRuleSpec.RuleType'] = 'affinity'
      antiAffinity: _typing.ClassVar['VirtualDiskRuleSpec.RuleType'] = 'antiAffinity'
      disabled: _typing.ClassVar['VirtualDiskRuleSpec.RuleType'] = 'disabled'

   diskRuleType: str
   diskId: list[int] = []


class VmConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   Storage DRS configuration for a single virtual machine.
   
   This makes it
   possible to override the default behavior for an individual virtual machine.
   
   Attributes:
       vm: Reference to the virtual machine.
           
           Can be NULL during initial placement.
       enabled: Flag to indicate whether or not VirtualCenter is allowed to perform any
           storage migration or initial placement recommendations for this virtual
           machine on the pod `pyVmomi.vim.StoragePod`.
           
           If this flag is false, the virtual machine is effectively excluded from
           storage DRS.
           
           If no individual DRS specification exists for a virtual machine,
           this property defaults to true.
       behavior: Specifies the particular storage DRS behavior for this virtual machine.
           
           For supported values, see `pyVmomi.vim.storageDrs.PodConfigInfo.Behavior`.
       intraVmAffinity: Specifies whether or not to have the affinity rule for the virtual disks
           of this virtual machine.
           
           If not set, the default value is derived from
           the pod-wide default `pyVmomi.vim.storageDrs.PodConfigInfo.defaultIntraVmAffinity`.
       intraVmAntiAffinity: Specifies the disks for this virtual machine that should be placed
           on different datastores.
           
           A VM cannot have both an affinity and an
           anti-affinity rule at the same time. Virtual machine disks that are
           not in this rule are unconstrained and can be placed either on the
           same datastore or on a different datastore as other disks from this
           virtual machine.
       virtualDiskRules: List of the virtual disk rules that can be overridden/created.
   """
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   enabled: _typing.Optional[bool] = None
   behavior: _typing.Optional[str] = None
   intraVmAffinity: _typing.Optional[bool] = None
   intraVmAntiAffinity: _typing.Optional[VirtualDiskAntiAffinityRuleSpec] = None
   virtualDiskRules: list[VirtualDiskRuleSpec] = []


class VmConfigSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """Updates the per-virtual-machine storage DRS configuration."""
   info: _typing.Optional[VmConfigInfo] = None
