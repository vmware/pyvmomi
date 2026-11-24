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
   """
   Base class for all action recommendations in VirtualCenter.
   
   Attributes:
       type: Type of the action.
           
           This is encoded to differentiate between
           different types of actions aimed at achieving different goals.
       target: The target object on which this action will be applied.
           
           For
           instance, a migration action will have a virtual machine as its
           target object, while a host power action will have a host as its
           target action.
   """
   class ActionType(pyVmomi.VmomiSupport.Enum):
      """
      Pre-defined constants for possible action types.
      
      Virtual Center
      uses this information to coordinate with the clients.
      
      Attributes:
          MigrationV1: Migration action type
          VmPowerV1: Virtual machine power action type
          HostPowerV1: Host power action type
          IncreaseLimitV1: Increase resource limit action type
          IncreaseSizeV1: Increase VM size, e.g., number of vcpus and memory size, action type
          IncreaseSharesV1: Increase resource shares action type
          IncreaseReservationV1: Increase resource reservation action type
          DecreaseOthersReservationV1: Decrease other VMs' or RPs' resource reservation action type
          IncreaseClusterCapacityV1: Increase cluster capacity action type
          DecreaseMigrationThresholdV1: Decrease migration threshold action type
          HostMaintenanceV1: Host entering maintenance mode action type
          StorageMigrationV1: Storage migration action type
          StoragePlacementV1: Initial placement action for a virtual machine or a virtual disk
          PlacementV1: Initial placement action for a virtual machine and its virtual disks
          HostInfraUpdateHaV1: Host changing infrastructure update ha mode action type.
      """
      MigrationV1: _typing.ClassVar['Action.ActionType'] = 'MigrationV1'
      VmPowerV1: _typing.ClassVar['Action.ActionType'] = 'VmPowerV1'
      HostPowerV1: _typing.ClassVar['Action.ActionType'] = 'HostPowerV1'
      IncreaseLimitV1: _typing.ClassVar['Action.ActionType'] = 'IncreaseLimitV1'
      IncreaseSizeV1: _typing.ClassVar['Action.ActionType'] = 'IncreaseSizeV1'
      IncreaseSharesV1: _typing.ClassVar['Action.ActionType'] = 'IncreaseSharesV1'
      IncreaseReservationV1: _typing.ClassVar['Action.ActionType'] = 'IncreaseReservationV1'
      DecreaseOthersReservationV1: _typing.ClassVar['Action.ActionType'] = 'DecreaseOthersReservationV1'
      IncreaseClusterCapacityV1: _typing.ClassVar['Action.ActionType'] = 'IncreaseClusterCapacityV1'
      DecreaseMigrationThresholdV1: _typing.ClassVar['Action.ActionType'] = 'DecreaseMigrationThresholdV1'
      HostMaintenanceV1: _typing.ClassVar['Action.ActionType'] = 'HostMaintenanceV1'
      StorageMigrationV1: _typing.ClassVar['Action.ActionType'] = 'StorageMigrationV1'
      StoragePlacementV1: _typing.ClassVar['Action.ActionType'] = 'StoragePlacementV1'
      PlacementV1: _typing.ClassVar['Action.ActionType'] = 'PlacementV1'
      HostInfraUpdateHaV1: _typing.ClassVar['Action.ActionType'] = 'HostInfraUpdateHaV1'

   type: str
   target: _typing.Optional[pyVmomi.VmomiSupport.ManagedObject] = None


class ActionHistory(pyVmomi.vmodl.DynamicData):
   """
   Base class for all action history.
   
   Attributes:
       action: The action that was executed recently.
       time: The time when the action was executed.
   """
   action: Action
   time: _datetime.datetime


class RuleInfo(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.cluster.RuleInfo` data object is the base type for affinity
   and anti-affinity rules.
   
   The affinity and anti-affinity rules
   are DRS (Distributed Resource Scheduling) rules that affect the placement
   of virtual machines in a cluster. Hosts and virtual machines referenced
   in a DRS rule must be in the same cluster.
   
   Note: DRS rules are different than an individual host's CPU affinity rules
   (`pyVmomi.vim.vm.AffinityInfo`).
   
   The Server uses DRS rule objects to describe the current rule configuration
   (`pyVmomi.vim.cluster.ConfigInfoEx`.`pyVmomi.vim.cluster.ConfigInfoEx.rule`).
   Your client application uses rule objects to configure the affinity and
   anti-affinity rules
   (`pyVmomi.vim.cluster.ConfigSpecEx`.`pyVmomi.vim.cluster.ConfigSpecEx.rulesSpec`).
   
   You can create the following types of rules:
   - An affinity rule defines a set of virtual machines that should run
     on the same host.
     The `pyVmomi.vim.cluster.AffinityRuleSpec` object describes a rule that
     identifies virtual machines, but does not identify any specific host.
   - An anti-affinity rule defines a set of virtual machines that should run
     on different hosts.
     The `pyVmomi.vim.cluster.AntiAffinityRuleSpec` object describes a rule that
     identifies virtual machines, but does not identify any specific host.
   - A VM-Host rule defines affinity and anti-affinity relationships between
     virtual machines and hosts.
     The `pyVmomi.vim.cluster.VmHostRuleInfo` object describes a rule that identifies
     a virtual machine group (`pyVmomi.vim.cluster.VmGroup`) and affinity and
     anti-affinity host groups (`pyVmomi.vim.cluster.HostGroup`).
     
   Rule configuration is a dynamic process. When you create or modify a DRS rule,
   the Server applies the rule to the cluster. If the existing cluster configuration
   violates the rule, the Server attempts to correct the situation. If that is not
   possible, the Server generates a fault and produces a log event.
   DRS rules do not have precedence; all rules are applied equally.
   DRS does not validate one rule against another. If you create conflicting
   rules, the older rule takes precedence and DRS disables the newer rule.
   
   Improperly used, DRS rules can fragment the cluster and inhibit the proper
   functioning of DRS, HA, and DPM services. vSphere services never
   take any actions that would result in the violation of mandatory DRS rules.
   An operation that violates a mandatory rule would produce the following
   consequences.
   - DRS does not evacuate virtual machines to place a host in maintenance
     mode.
   - DRS does not place virtual machines for power-on or load balance virtual
     machines.
   - HA does not perform failovers.
   - DPM does not optimize power management by placing hosts into standby
     mode.
     
   To avoid these situations, exercise caution when creating more than one
   mandatory rule, or consider using only optional rules. Make sure that
   the number of hosts with which a virtual machine is related by affinity rule
   is large enough that losing a host does not prevent the virtual machine
   from running.
   
   For manual and partially automated DRS clusters, the Server produces migration
   recommendations to satisfy the DRS rules. You are not required to act on the
   recommendations, but the Server maintains the recommendations until the rules
   are satisfied.
   
   Attributes:
       key: Unique ID for rules.
           
           When adding a new rule, do not specify this property.
           The Server will assign the key.
       status: Flag to indicate whether or not the rule is currently satisfied.
       enabled: Flag to indicate whether or not the rule is enabled.
           
           Set this property
           when you configure the rule. The default value is false (disabled).
           If there is a rule conflict, the Server can override the setting to disable
           a rule.
       name: Name of the rule.
       mandatory: Flag to indicate whether compliance with this rule is mandatory or optional.
           
           The default value is false (optional).
           - A mandatory rule will prevent a virtual machine from being powered on
             or migrated to a host that does not satisfy the rule.
           - An optional rule specifies a preference. DRS takes an optional rule
             into consideration when it places a virtual machine in the cluster.
             DRS will act on an optional rule as long as it does not impact
             the ability of the host to satisfy current CPU or memory requirements
             for virtual machines on the system. (As long as the operation does not
             cause any host to be more than 100% utilized.)
       userCreated: Flag to indicate whether the rule is created by the user or the system.
       inCompliance: Flag to indicate whether or not the placement of Virtual Machines is currently
           in compliance with this rule.
           
           The Server does not currently use this property.
       ruleUuid: UUID for the rule.
           
           When adding a new rule, do not specify this
           property. The Server will assign the key.
   """
   key: _typing.Optional[int] = None
   status: _typing.Optional[pyVmomi.vim.ManagedEntity.Status] = None
   enabled: _typing.Optional[bool] = None
   name: _typing.Optional[str] = None
   mandatory: _typing.Optional[bool] = None
   userCreated: _typing.Optional[bool] = None
   inCompliance: _typing.Optional[bool] = None
   ruleUuid: _typing.Optional[str] = None


class AffinityRuleSpec(RuleInfo):
   """
   The `pyVmomi.vim.cluster.AffinityRuleSpec` data object defines a set
   of virtual machines.
   
   DRS will attempt to schedule the virtual machines
   to run on the same host.
   
   Attributes:
       vm: List of virtual machine references.
   """
   vm: list[pyVmomi.vim.VirtualMachine] = []


class AntiAffinityRuleSpec(RuleInfo):
   """
   The `pyVmomi.vim.cluster.AntiAffinityRuleSpec` data object defines
   a set of virtual machines.
   
   DRS will attempt to schedule the virtual
   machines to run on different hosts.
   
   Attributes:
       vm: List of virtual machine references.
   """
   vm: list[pyVmomi.vim.VirtualMachine] = []


class AttemptedVmInfo(pyVmomi.vmodl.DynamicData):
   """
   This data class reports virtual machine powerOn information.
   
   Attributes:
       vm: The virtual machine being powered on.
       task: The ID of the task, which monitors powering on.
   """
   vm: pyVmomi.vim.VirtualMachine
   task: _typing.Optional[pyVmomi.vim.Task] = None


class ClusterInitialPlacementAction(Action):
   """
   Describes an action for the initial placement of a virtual machine in a
   cluster.
   
   This action is used by the cross cluster placement API when a
   virtual machine needs to be placed across a set of given clusters. See
   `pyVmomi.vim.Folder.placeVmsXCluster`. This action encapsulates details
   about the chosen cluster (via the resource pool inside that cluster), the
   chosen host and the chosen datastores for the disks of the virtual machine.
   
   Attributes:
       targetHost: The host where the virtual machine should be initially placed.
           
           This field
           is optional because the primary use case of
           `pyVmomi.vim.Folder.placeVmsXCluster` is to select the best cluster for
           placing VMs. This `pyVmomi.vim.cluster.ClusterInitialPlacementAction.targetHost`
           denotes the best host within the best cluster and it is only returned
           if the client asks for it, which is determined by
           `pyVmomi.vim.PlaceVmsXClusterSpec.hostRecommRequired`. If
           `pyVmomi.vim.PlaceVmsXClusterSpec.hostRecommRequired` is set to true, then
           the targetHost is returned with a valid value and if it is either set to
           false or left unset, then targetHost is also left unset. When this field
           is unset, then it means that the client did not ask for the target host
           within the recommended cluster. It does not mean that there is no
           recommended host for placing this VM in the recommended cluster.
       pool: The chosen resource pool for placing the virtual machine.
           
           This is non-
           optional because recommending the best cluster (by recommending the
           resource pool in the best cluster) is the primary use case for the
           `pyVmomi.vim.cluster.ClusterInitialPlacementAction`.
       availableNetworks: List of all networks available to all virtual NICs of the virtual machine
           on the chosen cluster.
           
           This field is set if the input spec to
           `pyVmomi.vim.Folder.placeVmsXCluster` has
           `pyVmomi.vim.PlaceVmsXClusterSpec.VmPlacementSpec.candidateNetworks`
           specified.
           When `pyVmomi.vim.PlaceVmsXClusterSpec.VmPlacementSpec.candidateNetworks`
           is supplied to the cross cluster placement API, the API response will set
           this field by selecting networks specified for all virtual network
           interfaces in
           `pyVmomi.vim.PlaceVmsXClusterSpec.VmPlacementSpec.candidateNetworks` that
           are available on the chosen cluster.
           Example: Assume
           `pyVmomi.vim.PlaceVmsXClusterSpec.VmPlacementSpec.candidateNetworks` is
           specified with three network interfaces specified with the following
           networks:
           \\- NIC 0: [A, B, C]
           \\- NIC 1: [B, E, F]
           \\- NIC 2: [B, H, I]
           If the available networks on the chosen cluster are B, F, and I, this
           field will contain [B, F, I] networks.
           
           Since: vSphere API Release 9.1.0.0
       configSpec: The config spec of the virtual machine to be placed.
           
           The `pyVmomi.vim.Folder.placeVmsXCluster` method takes
           input of `pyVmomi.vim.vm.ConfigSpec` from client and populates the backing
           for each virtual disk and the VM home path in it unless the input
           ConfigSpec already provides them. The existing settings in the input
           ConfigSpec are preserved and not overridden in the returned ConfigSpec
           in this action as well as the resulting
           `pyVmomi.vim.cluster.Recommendation`. This field is set based on whether
           the client needs `pyVmomi.vim.Folder.placeVmsXCluster` to recommend a
           backing datastore for the disks of the candidate VMs or not, which is
           specified via `pyVmomi.vim.PlaceVmsXClusterSpec.datastoreRecommRequired`.
           If `pyVmomi.vim.PlaceVmsXClusterSpec.datastoreRecommRequired` is set to
           true, then this
           `pyVmomi.vim.cluster.ClusterInitialPlacementAction.configSpec` is also set
           with the backing of each disk populated. If
           `pyVmomi.vim.PlaceVmsXClusterSpec.datastoreRecommRequired` is either set to
           false or left unset, then this field is also left unset. When this field
           is left unset, then it means that the client did not ask to populate the
           backing datastore for the disks of the candidate VMs.
   
   Since: vSphere API Release 8.0.0.1
   """
   targetHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
   pool: pyVmomi.vim.ResourcePool
   availableNetworks: list[pyVmomi.vim.Network] = []
   configSpec: _typing.Optional[pyVmomi.vim.vm.ConfigSpec] = None


class ClusterPowerContext(pyVmomi.vmodl.DynamicData):
   """
   Contains the current cluster power context including current
   ClusterPowerStatus, all needed intermediate ClusterPowerStatus to the final
   clusterPoweredOff or clusterPoweredOn status and the executing task.
   
   Attributes:
       currentClusterPowerStatus: The current ClusterPowerStatus.
       orderedClusterPowerStatus: A full list of ClusterPowerStatus with its corresponding executing
           order to final status.
           
           It contains only the relevant actions based on
           the target ClusterPowerStatus.
       trackingTask: A task that is executing the power action.
           
           None is returned if there is no
           on-going task
       lastErrorMessage: The description of error message if the previous task failed.
       lastErrorMOs: The MO list that causes the previous task to fail.
           
           i.e. if previous task
           failed because of having not powered-off VMs during power off cluster, the
           list contains some of the not powered-off VMs.
   """
   currentClusterPowerStatus: str
   orderedClusterPowerStatus: list[str] = []
   trackingTask: _typing.Optional[pyVmomi.vim.Task] = None
   lastErrorMessage: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None
   lastErrorMOs: list[pyVmomi.VmomiSupport.ManagedObject] = []

class ClusterPowerStatus:
   """Defines the detailed cluster wide power action."""
   pass


class ConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: As of VI API 2.5, use `pyVmomi.vim.cluster.ConfigInfoEx`.A complete cluster configuration.
   
   Attributes:
       dasConfig: Cluster-wide configuration of the vSphere HA service.
       dasVmConfig: List of virtual machine configurations for the vSphere HA
           service.
           
           Each entry applies to one virtual machine.
           
           If a virtual machine is not specified in this array, the service uses
           the default settings for that virtual machine.
       drsConfig: Cluster-wide configuration of the VMware DRS service.
       drsVmConfig: List of virtual machine configurations for the VMware DRS
           service.
           
           Each entry applies to one virtual machine.
           
           If a virtual machine is not specified in this array, the service uses
           the default settings for that virtual machine.
       rule: Cluster-wide rules.
   """
   dasConfig: DasConfigInfo
   dasVmConfig: list[DasVmConfigInfo] = []
   drsConfig: DrsConfigInfo
   drsVmConfig: list[DrsVmConfigInfo] = []
   rule: list[RuleInfo] = []


class ConfigInfoEx(pyVmomi.vim.ComputeResource.ConfigInfo):
   """
   The `pyVmomi.vim.cluster.ConfigInfoEx` data object describes a complete cluster
   configuration.
   
   For information about configuring a cluster, see
   `pyVmomi.vim.cluster.ConfigSpecEx`.
   
   Attributes:
       systemVMsConfig: Configuration for vCLS system VMs deployment.
           
           Since: vSphere API Release 7.0.3.0
       dasConfig: Cluster-wide configuration of the vSphere HA service.
       dasVmConfig: List of virtual machine configurations for the vSphere HA
           service.
           
           Each entry applies to one virtual machine.
           
           If a virtual machine is not specified in this array, the service uses
           the default settings for that virtual machine.
       drsConfig: Cluster-wide configuration of the VMware DRS service.
       drsVmConfig: List of virtual machine configurations for the VMware DRS
           service.
           
           Each entry applies to one virtual machine.
           
           If a virtual machine is not specified in this array, the service uses
           the default settings for that virtual machine.
       rule: Cluster-wide rules.
       orchestration: Cluster-wide configuration of VM orchestration.
       vmOrchestration: List of virtual machine configurations that apply during cluster wide
           VM orchestration.
           
           Each entry applies to one virtual machine.
           
           If a virtual machine is not specified in this array, the service uses
           the default settings for that virtual machine.
       dpmConfigInfo: Cluster-wide configuration of the VMware DPM service.
       dpmHostConfig: List of host configurations for the VMware DPM
           service.
           
           Each entry applies to one host.
           
           If a host is not specified in this array, the service uses
           the cluster default settings for that host.
       vsanConfigInfo: Cluster-wide configuration of the VMware VSAN service.
       vsanHostConfig: List of host configurations for the VMware VSAN service.
           
           Each entry applies to one host.
           
           If a host is not specified in this array, the service uses
           the cluster default settings for that host.
       group: Cluster-wide groups.
       infraUpdateHaConfig: Cluster-wide configuration of the VMware InfraUpdateHA service.
       proactiveDrsConfig: Cluster-wide configuration of the ProactiveDRS service.
       cryptoConfig: Cluster-wide configuration of the encryption mode.
       vsanCoreConfig: vSAN first-class settings that will be configured together with
           vSAN enablement.
           
           Since: vSphere API Release 9.0.0.0
   """
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
   """
   Deprecated: As of VI API 2.5, use `pyVmomi.vim.cluster.ConfigSpecEx`.A complete cluster configuration.
   
   All fields are defined as
   optional. In case of a reconfiguration, unset fields are
   unchanged.
   
   Attributes:
       dasConfig: Changes to the configuration of vSphere HA.
       dasVmConfigSpec: Changes to the per-virtual-machine vSphere HA settings.
       drsConfig: Changes to the configuration of the VMware DRS service.
       drsVmConfigSpec: Changes to the per-virtual-machine DRS settings.
       rulesSpec: Changes to the set of rules.
   """
   dasConfig: _typing.Optional[DasConfigInfo] = None
   dasVmConfigSpec: list[DasVmConfigSpec] = []
   drsConfig: _typing.Optional[DrsConfigInfo] = None
   drsVmConfigSpec: list[DrsVmConfigSpec] = []
   rulesSpec: list[RuleSpec] = []


class ConfigSpecEx(pyVmomi.vim.ComputeResource.ConfigSpec):
   """
   The `pyVmomi.vim.cluster.ConfigSpecEx` data object provides a set of update
   specifications for complete cluster configuration.
   
   You can configure a cluster when you create a new cluster
   (the `pyVmomi.vim.Folder.createClusterEx` method) or when you
   reconfigure an existing cluster
   (the `pyVmomi.vim.ComputeResource.reconfigureEx` method).
   
   All fields are optional. If you set the `modify`
   parameter to `true` when you call
   `pyVmomi.vim.ComputeResource.reconfigureEx`, an unset property has no effect
   on the existing property value in the cluster configuration on the Server.
   If you set the `modify` parameter to `false` when you
   reconfigure a cluster, the cluster configuration is reverted to the default
   values, then the new configuration values are applied.
   
   Use the properties defined for this object to configure
   the following services:
   - HA (High Availability) -
     provides failover protection for virtual machines
     running in a cluster of ESX Server hosts.
     The virtual machines are located in a `pyVmomi.vim.Datastore`, which
     provides shared storage for the cluster.
     When a failure occurs that affects a protected virtual machine,
     HA will restart the virtual machine on another host.
     When HA detects a host failure, either the host has failed or it may be
     isolated from the network. The HA agent on an isolated host will power off
     or shutdown the virtual machines running on that host so that they
     can be restarted elsewhere.
     See `pyVmomi.vim.cluster.DasVmSettings.IsolationResponse` for information
     about how a host handles network isolation.
     
     When it chooses a failover host, HA selects a host that is compatible
     with the virtual machine and that can support resource allocation for
     that virtual machine so that service level guarantees remain intact.
     HA does not consider hosts that are in maintenance mode, standby mode,
     or which are disconnected from the vCenter Server. When a host powers
     on or becomes available again, HA is reenabled on that host,
     so it becomes available for failover again.
     VMware recommends that you configure hosts and virtual machines
     so that all virtual machines can run on all hosts in the cluster.
     This will maximize the chances of restarting a VM after a failure.
     
     HA also restarts a virtual machine after a guest operating system failure.
     In this case, the virtual machine health monitoring service detects
     the guest failure, and HA restarts the virtual machine on the same host.
     The service monitors heartbeats from the VmTools service and optionally
     heartbeats that are generated by a third-party application monitor.
     See `pyVmomi.vim.cluster.VmToolsMonitoringSettings` and
     `pyVmomi.vim.cluster.DasConfigInfo`.`pyVmomi.vim.cluster.DasConfigInfo.vmMonitoring`.
     
     To enable HA for a cluster, set the
     `pyVmomi.vim.cluster.DasConfigInfo`.`pyVmomi.vim.cluster.DasConfigInfo.enabled`
     property to `true` and the
     `pyVmomi.vim.cluster.DasConfigInfo`.`pyVmomi.vim.cluster.DasConfigInfo.hostMonitoring`
     property to `enabled`.
     (The vSphere API uses the substring \"das\" in object, property,
     and method names for HA.1)
   - DRS (Distributed Resource Scheduling) - provides automatic initial
     virtual machine placement on any of the hosts in the cluster. DRS
     also makes automatic resource relocation and optimization decisions
     as hosts or virtual machines are added or removed from the cluster.
     You can also configure DRS for manual control, so that it only makes
     recommendations that you can review and carry out.
     
     To enable DRS for a cluster, set the
     `pyVmomi.vim.cluster.DrsConfigInfo`.`pyVmomi.vim.cluster.DrsConfigInfo.enabled`
     property to `true`.
   - DPM (Distributed Power Management) - supports optimized power
     consumption on the cluster. When virtual machines in a DRS
     cluster require fewer resources, DPM consolidates workloads
     onto fewer servers while maintaining quality of service guarantees
     and powers off the rest to reduce power consumption.
     When more resources are required, DPM brings the powered-down hosts online.
     
     To enable DPM for a cluster, set the
     `pyVmomi.vim.cluster.DpmConfigInfo`.`pyVmomi.vim.cluster.DpmConfigInfo.enabled`
     property to `true`.
   - VSAN - aggregates hosts' local disks to present a single
     shared datastore to the cluster.
     
     To enable VSAN for a cluster, set the
     `pyVmomi.vim.vsan.cluster.ConfigInfo.enabled` property to
     `true` for `pyVmomi.vim.cluster.ConfigSpecEx.vsanConfig`.
   - InfraUpdateHA (Infrastructure update HA) - supports automatic
     migration of virtual machines to hosts with low risk of a
     catastrophic failure. Similar to DRS, you can also configure
     InfraUpdateHA for manual control to only makes recommendations that
     you can review and carry out. The health state of the hosts are
     propagated to HA to enable restarting of virtual machines in healthy
     hosts as possible.
     
     To enable InfraUpdateHA for a cluster, set the
     `pyVmomi.vim.cluster.InfraUpdateHaConfigInfo`.`pyVmomi.vim.cluster.InfraUpdateHaConfigInfo.enabled` property to
     `true`.
   - ProactiveDRS (Proactive Distributed Resources Scheduling) - supports
     virtual machine load balancing decisions that take predicted
     resource demand information into account.
     
     To enable ProactiveDRS for a cluster, set the
     `pyVmomi.vim.cluster.ProactiveDrsConfigInfo`.`pyVmomi.vim.cluster.ProactiveDrsConfigInfo.enabled` property to
     `true`.
     
   The HA, DRS, and DPM services are integrated with the FT (Fault Tolerance)
   and EVC (Enhanced vMotion Compatibility) services.
   Use the `pyVmomi.vim.VirtualMachine.createSecondary` method to establish
   fault tolerance for a virtual machine. Use the vSphere Client to configure EVC.
   The HA, DRS, DPM, FT, and EVC services interact under
   the following circumstances.
   - To determine initial placement of a virtual machine, DRS
     checks to see if the HA admission control policy on a
     potential host supports the addition of the powered on
     virtual machine. With the default setting, DRS will not
     power on more than four FT virtual machines per host.
     You can use the configuration editor in the vSphere Client
     to set the HA advanced option `das.maxFtVmsPerHost`
     to the desired number or to zero to disable.
   - When a host fails, HA determines placement within
     the cluster when it restarts the virtual machines.
     If there is insufficient capacity, and DPM has put one or more
     compatible hosts into standby, HA relies on DPM to bring more
     capacity online.
   - To use FT in a cluster, the cluster must be HA-enabled.
   - You can disable HA in a cluster while there are FT virtual
     machines registered on hosts in the cluster.
     While HA is disabled, powered on FT virtual machines will continue
     to run, but HA will not restart any virtual machines after a failure.
     When HA is disabled, you cannot use the following FT operations:
     - Turn on FT (`pyVmomi.vim.VirtualMachine.createSecondary`)
     - Enable FT (`pyVmomi.vim.VirtualMachine.enableSecondary`)
     - Power on an FT virtual machine
       (`pyVmomi.vim.VirtualMachine.powerOn`)
     - Test failover and test secondary restart
       (`pyVmomi.vim.VirtualMachine.terminateFaultTolerantVM`)
   - In a cluster using DRS and HA with admission control turned on
     (`pyVmomi.vim.cluster.DasConfigInfo`.`pyVmomi.vim.cluster.DasConfigInfo.admissionControlEnabled`),
     the vCenter Server might not migrate virtual machines from hosts
     entering maintenance mode. This is because resources are reserved
     to maintain the failover level. You must use vMotion to manually
     migrate the virtual machines off the hosts.
     
     When admission control is disabled, failover resource constraints
     are not passed on to DRS and DPM. The constraints are not enforced.
     - DRS determines virtual machine placement and status
       (maintenance mode, standby mode) regardless of the impact
       this might have on failover requirements.
     - DPM powers off hosts (places them in standby mode)
       even if doing so violates failover requirements.
       If there is insufficient capacity when a failover
       occurs, DPM will attempt to bring more capacity online
       in order to correct the situation.
   - You must enable EVC in a cluster to enable DRS to manage FT primary
     and secondary virtual machine pairs in the cluster.
     For information about EVC clusters, see `pyVmomi.vim.EVCMode`.
     
     If EVC is disabled, vCenter automatically creates overrides
     to disable DRS for FT primary/secondary pairs in the cluster.
     vCenter will still use DRS to place a secondary virtual machine
     when it powers on.
     Attempts to remove the overrides or to enable DRS operations
     will fail.
   - EVC clusters support load balancing of powered on FT primary
     and secondary virtual machines. DRS behavior
     is governed by the overrides defined for the primary virtual
     machine. The secondary inherits DRS behavior from its primary.
     If you do not configure a DRS override for an FT virtual
     machine, DRS uses the cluster default
     (`pyVmomi.vim.cluster.DrsConfigInfo.defaultVmBehavior`).
     
   1High Availability was previously called Distributed
   Availability Services.
   
   Attributes:
       systemVMsConfig: Configuration for vCLS system VMs deployment.
           
           Since: vSphere API Release 7.0.3.0
       dasConfig: HA configuration; includes default settings for virtual machines.
       dasVmConfigSpec: HA configuration for individual virtual machines.
           
           The entries in this array override the cluster default
           settings
           (`pyVmomi.vim.cluster.DasConfigInfo`.`pyVmomi.vim.cluster.DasConfigInfo.defaultVmSettings`).
           You cannot specify an HA override for a secondary FT virtual
           machine. The secondary virtual machine will inherit whatever
           settings apply to its primary virtual machine. If you
           include an entry for a secondary, the reconfigure method
           will throw the fault
           `pyVmomi.vim.fault.CannotChangeHaSettingsForFtSecondary`.
       drsConfig: DRS configuration; includes default settings for virtual machines.
       drsVmConfigSpec: DRS configuration for individual virtual machines.
           
           The entries in this array override the cluster default
           settings
           (`pyVmomi.vim.cluster.DrsConfigInfo`.`pyVmomi.vim.cluster.DrsConfigInfo.defaultVmBehavior`).
           You cannot specify a DRS override for a secondary FT virtual
           machine. The secondary virtual machine will inherit whatever
           setting applies to its primary virtual machine. If you
           include an entry for a secondary, the reconfigure method
           will throw the fault
           `pyVmomi.vim.fault.CannotChangeDrsBehaviorForFtSecondary`.
       rulesSpec: Cluster affinity and anti-affinity rule configuration.
       orchestration: Cluster configuration of VM orchestration.
       vmOrchestrationSpec: List of specific VM configurations that apply during cluster wide
           VM orchestration.
           
           Each entry applies to one virtual machine, and
           overrides the cluster default settings.
       dpmConfig: DPM configuration; includes default settings for hosts.
       dpmHostConfigSpec: DPM configuration for individual hosts.
           
           The entries in this array override the cluster default
           settings
           (`pyVmomi.vim.cluster.DpmConfigInfo`.`pyVmomi.vim.cluster.DpmConfigInfo.defaultDpmBehavior`).
       vsanConfig: VSAN configuration; includes default settings for hosts.
           
           When it is requested to change, vSAN related sub tasks will be
           generated automatically per member hosts, which are identified
           by using cluster reconfiguration task id as
           `pyVmomi.vim.TaskInfo.parentTaskKey`, and should be monitored
           and tracked separately.
       vsanHostConfigSpec: VSAN configuration for individual hosts.
           
           The entries in this array override the cluster default settings
           as specified in `pyVmomi.vim.vsan.cluster.ConfigInfo`.
       groupSpec: Cluster-wide group configuration.
           
           The array contains one or more group specification objects.
           A group specification object contains a virtual machine group
           (`pyVmomi.vim.cluster.VmGroup`) or a host group (`pyVmomi.vim.cluster.HostGroup`).
           Groups can be related; see `pyVmomi.vim.cluster.VmHostRuleInfo`.
       infraUpdateHaConfig: InfraUpdateHA configuration.
       proactiveDrsConfig: ProactiveDrs configuration.
       inHciWorkflow: Flag to place the cluster in the HCI workflow during cluster creation.
           
           This flag is specified only at the time of cluster creation.
           A cluster cannot be reconfigured to place it in the HCI workflow.
       cryptoConfig: Cluster-wide configuration of encryption mode.
       vsanCoreConfigSpec: vSAN first-class settings that will be configured together with
           vSAN enablement.
           
           Since: vSphere API Release 9.0.0.0
   """
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
   """
   Attributes:
       cryptoMode: The cluster encryption mode.
           
           See `pyVmomi.vim.cluster.CryptoConfigInfo.CryptoMode` for supported values.
       policy: The encryption mode policy for the cluster.
           
           When unset, host keys will be automatically generated using the current
           default key provider.
           
           Since: vSphere API Release 8.0.3.0
   """
   class CryptoMode(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          onDemand: Put each host into the crypto safe state automatically when needed.
          forceEnable: Put each host into the crypto safe state immediately.
      """
      onDemand: _typing.ClassVar['CryptoConfigInfo.CryptoMode'] = 'onDemand'
      forceEnable: _typing.ClassVar['CryptoConfigInfo.CryptoMode'] = 'forceEnable'

   cryptoMode: _typing.Optional[str] = None
   policy: _typing.Optional[pyVmomi.vim.ClusterComputeResource.CryptoModePolicy] = None


class DasHostInfo(pyVmomi.vmodl.DynamicData):
   """HA specific advanced information pertaining to the hosts in the cluster."""
   pass


class DasAamHostInfo(DasHostInfo):
   """
   Deprecated: As of vSphere API 5.0, this object is no longer returned by
   vCenter Server. Availability information is now reported using
   `pyVmomi.vim.host.RuntimeInfo.dasHostState`.The `pyVmomi.vim.cluster.DasAamHostInfo` object contains a list of the ESX hosts
   in an HA cluster and a list that identifies the primary hosts.
   
   (AAM is a component of the HA service.)
   The primary hosts share the joint responsibility of maintaining all cluster
   state and one will initiate failover actions should a failure occur.
   
   When you add an ESX host to a vSphere HA cluster, the host
   downloads HA agent components from the vCenter Server.
   The HA agent maintains communication with the vCenter Server.
   
   When the host downloads the HA agent, the host configures the agent
   to communicate with other agents in the cluster. A host that joins
   the cluster communicates with an existing primary host to complete
   its configuration (except when you are adding the first host to the cluster).
   - The first five hosts added to the cluster are designated
     as primary hosts. All subsequent hosts are designated as secondary hosts.
   - If a primary host is removed from the cluster,
     the vCenter Server promotes another host to primary status.
   - There must be at least one functional primary host for vSphere HA
     to operate correctly. If there is not an available primary host
     (no response), host configuration for HA will fail.
     If there is a total cluster failure, HA will begin restarting virtual
     machines as soon as one host recovers and its HA agent is up and running.
     
   One of the primary hosts assumes the role of the active primary host.
   The active primary host responsibilities include the following activities:
   - Decides where to restart virtual machines.
   - Tracks failed restart attempts.
   - Determines when it is appropriate to continue attempts to restart
     a virtual machine.
     
   If the active primary host fails, another primary host replaces it.
   
   Attributes:
       hostDasState: The state of HA on the hosts.
       primaryHosts: The list of primary hosts.
   """
   hostDasState: list[DasAamNodeState] = []
   primaryHosts: list[str] = []


class DasAamNodeState(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: As of vSphere API 5.0, this object is no longer returned by
   vCenter Server. See `pyVmomi.vim.host.RuntimeInfo.dasHostState` for a
   description of the objects now used.The `pyVmomi.vim.cluster.DasAamNodeState` data object represents the state
   of the HA service on an ESX host.
   
   (AAM is a component of this service.)
   
   Attributes:
       host: Reference to the host.
       name: Name of the host
           (`pyVmomi.vim.HostSystem`.`pyVmomi.vim.ManagedEntity.name`).
       configState: Configuration state of the HA agent on the host.
           
           The property can be one of the following values:
           
           configuring  
           error  
           unconfiguring  
           running  
           
           `configState` represents setting or resetting the HA
           configuration on the host. If the configuration operation is
           successful, the value of `configState` changes
           to `running`. See `pyVmomi.vim.cluster.DasAamNodeState.DasState`.
       runtimeState: The runtime state of the HA agent on the node.
           
           The property can be one of the following values:
           
           uninitialized  
           initialized  
           running  
           error  
           agentShutdown  
           nodeFailed
           
           See `pyVmomi.vim.cluster.DasAamNodeState.DasState`.
   """
   class DasState(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.vim.cluster.DasAamNodeState.DasState` enumerated type defines
      values for host HA configuration and runtime state properties
      (`pyVmomi.vim.cluster.DasAamNodeState.configState` and
      `pyVmomi.vim.cluster.DasAamNodeState.runtimeState`).
      
      Attributes:
          uninitialized: HA has never been enabled on the the host.
          initialized: HA agents have been installed but are not running on the the host.
          configuring: HA configuration is in progress.
          unconfiguring: HA configuration is being removed.
          running: HA agent is running on this host.
          error: There is an error condition.
              
              This can represent a configuration
              error or a host agent runtime error.
          agentShutdown: The HA agent has been shut down.
          nodeFailed: The host is not reachable.
              
              This can represent a host failure
              or an isolated host.
      """
      uninitialized: _typing.ClassVar['DasAamNodeState.DasState'] = 'uninitialized'
      initialized: _typing.ClassVar['DasAamNodeState.DasState'] = 'initialized'
      configuring: _typing.ClassVar['DasAamNodeState.DasState'] = 'configuring'
      unconfiguring: _typing.ClassVar['DasAamNodeState.DasState'] = 'unconfiguring'
      running: _typing.ClassVar['DasAamNodeState.DasState'] = 'running'
      error: _typing.ClassVar['DasAamNodeState.DasState'] = 'error'
      agentShutdown: _typing.ClassVar['DasAamNodeState.DasState'] = 'agentShutdown'
      nodeFailed: _typing.ClassVar['DasAamNodeState.DasState'] = 'nodeFailed'

   host: pyVmomi.vim.HostSystem
   name: str
   configState: str
   runtimeState: str


class DasAdmissionControlInfo(pyVmomi.vmodl.DynamicData):
   """Base class for admission control related information of a vSphere HA cluster."""
   pass


class DasAdmissionControlPolicy(pyVmomi.vmodl.DynamicData):
   """
   Base class for specifying how admission control should be done for vSphere HA.
   
   Attributes:
       resourceReductionToToleratePercent: Percentage of resource reduction that a cluster of VMs can tolerate
           in case of a failover.
       pMemAdmissionControlEnabled: Flag that determines whether strict admission control for persistent
           memory is enabled.
           
           By default, this value is false.
           This flag can only be set to true if
           `pyVmomi.vim.cluster.DasConfigInfo.admissionControlEnabled` is set to true.
           When you use persistent memory admission control, the following
           operations are prevented, if doing so would violate the
           `pyVmomi.vim.cluster.DasConfigInfo.admissionControlEnabled`.
           - Creating a virtual machine with persistent memory.
           - Adding a virtual persistent memory device to a virtual machine.
           - Increasing the capacity of a virtual persistent memory device.
           
           Since: vSphere API Release 7.0.2.0
   """
   resourceReductionToToleratePercent: _typing.Optional[int] = None
   pMemAdmissionControlEnabled: _typing.Optional[bool] = None


class DasAdvancedRuntimeInfo(pyVmomi.vmodl.DynamicData):
   """
   Base class for advanced runtime information related to the high
   availability service for a cluster.
   
   Attributes:
       dasHostInfo: The information pertaining to the HA agents on the hosts
       vmcpSupported: Whether HA VM Component Protection can be enabled for the cluster.
       heartbeatDatastoreInfo: The map of a datastore to the set of hosts that are using
           the datastore for storage heartbeating.
   """
   class VmcpCapabilityInfo(pyVmomi.vmodl.DynamicData):
      """
      Class for capability to support VM Component Protection
      
      Attributes:
          storageAPDSupported: If all hosts in the cluster support the reaction of VM Component Protection
              to storage All Paths Down timeout
              `AllPathsDown_Timeout`
          storagePDLSupported: If all hosts in the cluster support the reaction of VM Component Protection
              to storage Permanent Device Loss
              `PermanentDeviceLoss`
      """
      storageAPDSupported: bool
      storagePDLSupported: bool

   class HeartbeatDatastoreInfo(pyVmomi.vmodl.DynamicData):
      """Class for the selection of heartbeat datastores"""
      datastore: pyVmomi.vim.Datastore
      hosts: list[pyVmomi.vim.HostSystem] = []

   dasHostInfo: _typing.Optional[DasHostInfo] = None
   vmcpSupported: _typing.Optional[DasAdvancedRuntimeInfo.VmcpCapabilityInfo] = None
   heartbeatDatastoreInfo: list[DasAdvancedRuntimeInfo.HeartbeatDatastoreInfo] = []


class DasConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.cluster.DasConfigInfo` data object contains configuration data
   about the HA service on a cluster.
   
   All fields are optional. If you set the `modify`
   parameter to `true` when you call
   `pyVmomi.vim.ComputeResource.reconfigureEx`, an unset property has no effect
   on the existing property value in the cluster configuration on the Server.
   If you set the `modify` parameter to `false` when you
   reconfigure a cluster, the cluster configuration is reverted to the default
   values, then the new configuration values are applied.
   
   Attributes:
       enabled: Flag to indicate whether or not vSphere HA feature is enabled.
       vmMonitoring: Level of HA Virtual Machine Health Monitoring Service.
           
           You can monitor both guest and application heartbeats, guest heartbeats only,
           or you can disable the service. See `pyVmomi.vim.cluster.DasConfigInfo.VmMonitoringState`.
           The default value is `vmMonitoringDisabled`.
           
           The Service level specified for the cluster determines
           the possible monitoring settings that you can use for individual virtual machines.
           See `pyVmomi.vim.cluster.VmToolsMonitoringSettings`.`pyVmomi.vim.cluster.VmToolsMonitoringSettings.vmMonitoring`.
       hostMonitoring: Determines whether HA restarts virtual machines after a host fails.
           
           The default value is
           `pyVmomi.vim.cluster.DasConfigInfo.ServiceState`.`enabled`.
           This property is meaningful only when
           `pyVmomi.vim.cluster.DasConfigInfo`.`pyVmomi.vim.cluster.DasConfigInfo.enabled` is `true`.
           
           When `hostMonitoring` is
           `enabled`, HA restarts virtual machines
           after a host fails.
           
           When `hostMonitoring` is
           `disabled`, HA does not restart
           virtual machines after a host fails.
           The status of Host Monitoring does not affect other services such
           as virtual machine Health Monitoring or Fault Tolerance.
           The rest of the cluster operations follow normal processing.
           No configuration information is lost and re-enabling the service
           is a quick operation.
       vmComponentProtecting: This property indicates if vSphere HA VM Component Protection service
           is enabled.
           
           The default value is `disabled`.
           
           When `vmComponentProtecting` is set to
           `disabled`, reaction to all types of VM
           component failures is disabled.
           
           When `vmComponentProtecting` is set to
           `enabled`, VM Component Protection service
           will detect and react to component failures. The actual reaction is determined
           by `pyVmomi.vim.cluster.VmComponentProtectionSettings` which is referenced by both cluster
           level configuration (`pyVmomi.vim.cluster.DasConfigInfo.defaultVmSettings`) and per-VM
           override `pyVmomi.vim.cluster.ConfigInfoEx.dasVmConfig`.
       failoverLevel: Configured failover level.
           
           This is the number of physical host failures
           that can be tolerated without impacting the ability to satisfy the
           minimums for all running virtual machines. Acceptable values range from one to
           four.
       admissionControlPolicy: Virtual machine admission control policy for vSphere HA.
           
           The policies specify resource availability for failover support.
           - Failover host admission policy
             `pyVmomi.vim.cluster.FailoverHostAdmissionControlPolicy` -
             specify one or more dedicated failover hosts.
           - Failover level policy
             `pyVmomi.vim.cluster.FailoverLevelAdmissionControlPolicy` -
             the limit of host failures for which resources are reserved.
             When you use the failover level policy,
             HA partitions resources into slots. A slot represents the minimum
             CPU and memory resources that are required to support
             any powered on virtual machine in the cluster.
             To retrieve information about partitioned resources, use the
             `pyVmomi.vim.ClusterComputeResource.retrieveDasAdvancedRuntimeInfo`
             method.
           - Resources admission policy
             `pyVmomi.vim.cluster.FailoverResourcesAdmissionControlPolicy` -
             CPU and memory resources reserved for failover support.
             When you use the resources policy, you can reserve
             a percentage of the aggregate cluster resource for failover.
       admissionControlEnabled: Flag that determines whether strict admission control is enabled.
           
           When you use admission control, the following operations are
           prevented, if doing so would violate the `pyVmomi.vim.cluster.DasConfigInfo.admissionControlPolicy`.
           - Powering on a virtual machine in the cluster.
           - Migrating a virtual machine into the cluster.
           - Increasing the CPU or memory reservation of powered-on
             virtual machines in the cluster.
             
           With admission control disabled, there is no assurance that
           all virtual machines in the HA cluster can be restarted after
           a host failure. VMware recommends that you do not disable
           admission control, but you might need to do so temporarily,
           for the following reasons:
           - If you need to violate the failover constraints when there
             are not enough resources to support them (for example,
             if you are placing hosts in standby mode to test them
             for use with DPM).
           - If an automated process needs to take actions that might
             temporarily violate the failover constraints (for example,
             as part of an upgrade directed by VMware Update Manager).
           - If you need to perform testing or maintenance operations.
       defaultVmSettings: Cluster-wide defaults for virtual machine HA settings.
           
           When a virtual machine has no HA configuration
           (`pyVmomi.vim.cluster.DasVmConfigSpec`), it uses the values
           specified here.
       option: Advanced settings.
       heartbeatDatastore: The list of preferred datastores to use for storage heartbeating.
           
           Each of the specified datastores should be active and mounted
           by more than one host. There is no limit on the number of specified
           datastores and no priority among them.
           The specified datastores will replace those previously specified and
           an empty list will delete all such earlier specified ones.
           
           vCenter Server chooses the heartbeat datastores for a host from the
           set specified by `pyVmomi.vim.cluster.DasConfigInfo.hBDatastoreCandidatePolicy`.
           The choice is made based on datastore connectivity and storage array
           redundancy (in case of VMFS).
           
           The final set of selected heartbeat datastores is reported via
           `pyVmomi.vim.cluster.DasAdvancedRuntimeInfo.heartbeatDatastoreInfo`.
       hBDatastoreCandidatePolicy: The policy on what datastores will be used by vCenter Server to choose
           heartbeat datastores.
           
           See `pyVmomi.vim.cluster.DasConfigInfo.HBDatastoreCandidate` for all options.
           The default value is
           `allFeasibleDsWithUserPreference`.
   """
   class ServiceState(pyVmomi.VmomiSupport.Enum):
      """
      Possible states of an HA service.
      
      All services support the
      disabled and enabled states.
      
      Attributes:
          disabled: HA service is disabled.
          enabled: HA service is enabled.
      """
      disabled: _typing.ClassVar['DasConfigInfo.ServiceState'] = 'disabled'
      enabled: _typing.ClassVar['DasConfigInfo.ServiceState'] = 'enabled'

   class VmMonitoringState(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.vim.cluster.DasConfigInfo.VmMonitoringState` enum defines values that indicate
      the state of Virtual Machine Health Monitoring.
      
      Health Monitoring
      uses the vmTools (guest) and application agent heartbeat modules.
      You can configure HA to respond to heartbeat failures of either one
      or both modules. You can also disable the HA response to heartbeat failures.
      - To set the cluster default for health monitoring, use the
        ClusterConfigSpecEx.dasConfig.`pyVmomi.vim.cluster.DasConfigInfo.vmMonitoring` property.
      - To set health monitoring for a virtual machine, use the
        ClusterConfigSpecEx.dasVmConfigSpec.info.dasSettings.`pyVmomi.vim.cluster.DasVmSettings.vmToolsMonitoringSettings` property.
      - To retrieve the current state of health monitoring (cluster setting), use the
        ClusterConfigInfoEx.dasConfig.`pyVmomi.vim.cluster.DasConfigInfo.vmMonitoring`
        property.
      - To retrieve the current state of health monitoring for a virtual machine, use the
        ClusterConfigInfoEx.dasVmConfig[].dasSettings.vmToolsMonitoringSettings.`pyVmomi.vim.cluster.VmToolsMonitoringSettings.vmMonitoring`
        property.
      
      Attributes:
          vmMonitoringDisabled: Virtual machine health monitoring is disabled.
              
              In this state,
              HA response to guest and application heartbeat failures are disabled.
          vmMonitoringOnly: HA response to guest heartbeat failure is enabled.
              
              To retrieve the guest heartbeat status, use the
              `pyVmomi.vim.VirtualMachine`.`pyVmomi.vim.VirtualMachine.guestHeartbeatStatus`
              property.
          vmAndAppMonitoring: HA response to both guest and application heartbeat failure is enabled.
              - To retrieve the guest heartbeat status, use the
                `pyVmomi.vim.VirtualMachine`.`pyVmomi.vim.VirtualMachine.guestHeartbeatStatus`
                property.
              - To retrieve the application heartbeat status, use the
                `pyVmomi.vim.vm.GuestInfo`.`pyVmomi.vim.vm.GuestInfo.appHeartbeatStatus`
                property.
      """
      vmMonitoringDisabled: _typing.ClassVar['DasConfigInfo.VmMonitoringState'] = 'vmMonitoringDisabled'
      vmMonitoringOnly: _typing.ClassVar['DasConfigInfo.VmMonitoringState'] = 'vmMonitoringOnly'
      vmAndAppMonitoring: _typing.ClassVar['DasConfigInfo.VmMonitoringState'] = 'vmAndAppMonitoring'

   class HBDatastoreCandidate(pyVmomi.VmomiSupport.Enum):
      """
      The policy to determine the candidates from which vCenter Server can
      choose heartbeat datastores.
      
      Attributes:
          userSelectedDs: vCenter Server chooses heartbeat datastores from the set specified
              by the user (see `pyVmomi.vim.cluster.DasConfigInfo.heartbeatDatastore`).
              
              More specifically,
              datastores not included in the set will not be chosen. Note that if
              `pyVmomi.vim.cluster.DasConfigInfo.heartbeatDatastore` is empty, datastore heartbeating will
              be disabled for HA.
          allFeasibleDs: vCenter Server chooses heartbeat datastores from all the feasible ones,
              i.e., the datastores that are accessible to more than one host in
              the cluster.
              
              The choice will be made without giving preference to those
              specified by the user (see `pyVmomi.vim.cluster.DasConfigInfo.heartbeatDatastore`).
          allFeasibleDsWithUserPreference: vCenter Server chooses heartbeat datastores from all the feasible ones
              while giving preference to those specified by the user (see `pyVmomi.vim.cluster.DasConfigInfo.heartbeatDatastore`).
              
              More specifically, the datastores not included in `pyVmomi.vim.cluster.DasConfigInfo.heartbeatDatastore` will be
              chosen if and only if the specified ones are not sufficient.
      """
      userSelectedDs: _typing.ClassVar['DasConfigInfo.HBDatastoreCandidate'] = 'userSelectedDs'
      allFeasibleDs: _typing.ClassVar['DasConfigInfo.HBDatastoreCandidate'] = 'allFeasibleDs'
      allFeasibleDsWithUserPreference: _typing.ClassVar['DasConfigInfo.HBDatastoreCandidate'] = 'allFeasibleDsWithUserPreference'

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
   """Base class for DAS data for high availability service for a cluster."""
   pass


class DasDataSummary(DasData):
   """
   This class contains the summary of the data that DAS needs/uses.
   
   The actual data is available in `pyVmomi.vim.cluster.DasDataDetails` and can be retrieved
   using the `pyVmomi.vim.ClusterComputeResource.retrieveDasData` method.
   This class is meant for VMware internal use only.
   
   Attributes:
       hostListVersion: The version corresponding to the hostList
       clusterConfigVersion: The version corresponding to the clusterConfig
       compatListVersion: The version corresponding to the compatList
   """
   hostListVersion: pyVmomi.VmomiSupport.long
   clusterConfigVersion: pyVmomi.VmomiSupport.long
   compatListVersion: pyVmomi.VmomiSupport.long


class DasFailoverLevelAdvancedRuntimeInfo(DasAdvancedRuntimeInfo):
   """
   Advanced runtime information related to the high availability service
   for a cluster that has been configured with a failover level admission control
   policy.
   
   See `pyVmomi.vim.cluster.FailoverLevelAdmissionControlPolicy`.
   
   Attributes:
       slotInfo: Slot information for this cluster.
       totalSlots: The total number of slots available in the cluster.
       usedSlots: The number of slots currently being used.
       unreservedSlots: The number of slots that are not used by currently powered on virtual machines
           and not reserved to satisfy the configured failover level.
           
           This number gives
           an indication of how many additional virtual machines can be powered on in
           this cluster without violating the failover level (assuming the new virtual
           machine's reservations are satisfied by the current slot size).
           This value is computed as follows (where m is the configured failover level):
           Remove the m largest hosts (ie. the ones with the most slots) from the list
           of \"good\" hosts (see `pyVmomi.vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.totalGoodHosts`). Sum up the number of slots on
           the remaining hosts and deduct the number of currently used slots
           (see `pyVmomi.vim.cluster.DasFailoverLevelAdvancedRuntimeInfo.usedSlots`). If this number is negative, use zero instead.
       totalVms: The total number of powered on vms in the cluster.
       totalHosts: The total number of hosts in the cluster.
       totalGoodHosts: The total number of connected hosts that are not in maintenance mode and that
           do not have any DAS-related config issues on them.
       vmsRequiringMultipleSlots: The list of virtual machines whose reservations and memory overhead are not
           satisfied by a single slot.
   """
   class SlotInfo(pyVmomi.vmodl.DynamicData):
      """
      A slot represents an amount of memory and cpu resources on a physical host for use
      by a virtual machine.
      
      It is used in computing the resources to be reserved for
      failover.
      
      Attributes:
          numVcpus: The number of virtual cpus of a slot is defined as the maximum number of
              virtual cpus any powered on virtual machine has.
          cpuMHz: The cpu speed of a slot is defined as the maximum cpu reservation of any
              powered on virtual machine in the cluster, or any otherwise defined minimum,
              whichever is larger.
          memoryMB: The memory size of a slot is defined as the maximum memory reservation plus
              memory overhead of any powered on virtual machine in the cluster, or any
              otherwise defined minimum, whichever is larger.
      """
      numVcpus: int
      cpuMHz: int
      memoryMB: int

   class HostSlots(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          host: The reference to the host.
          slots: The number of slots in this host.
      """
      host: pyVmomi.vim.HostSystem
      slots: int

   class VmSlots(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          vm: The reference to the virtual machine
          slots: The number of slots required by this virtual machine
      """
      vm: pyVmomi.vim.VirtualMachine
      slots: int

   slotInfo: DasFailoverLevelAdvancedRuntimeInfo.SlotInfo
   totalSlots: int
   usedSlots: int
   unreservedSlots: int
   totalVms: int
   totalHosts: int
   totalGoodHosts: int
   hostSlots: list[DasFailoverLevelAdvancedRuntimeInfo.HostSlots] = []
   vmsRequiringMultipleSlots: list[DasFailoverLevelAdvancedRuntimeInfo.VmSlots] = []

class DasFdmAvailabilityState:
   """
   The `pyVmomi.vim.cluster.DasFdmAvailabilityState` enumeration describes the
   availability states of hosts in a vSphere HA cluster.
   
   In the HA
   architecture, a agent called the Fault Domain Manager runs on
   each active host. These agents elect a master and the others become
   its slaves. The availability state assigned to a given host is
   determined from information reported by the Fault Domain Manager
   running on the host, by a Fault Domain Manager that has been elected
   master, and by vCenter Server. See `pyVmomi.vim.cluster.DasFdmHostState`
   for more information about the vSphere HA architecture.
   """
   pass


class DasFdmHostState(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.cluster.DasFdmHostState` data object
   describes the availability state of each active host in a
   vSphere HA enabled cluster.
   
   In a vSphere HA cluster, the active hosts form a fault domain.
   A host is inactive if it is in standby or maintenance mode, or
   it has been disconnected from vCenter Server. A vSphere HA
   agent, called the Fault Domain Manager (FDM), runs on each host in the
   fault domain.
   
   One FDM serves as the master and the remaining FDMs as its slaves.
   The master is responsible for monitoring the availability of the hosts
   and VMs in the cluster, and restarting any VMs that fail due to a
   host failure or non-user-initiated power offs. The master is also
   responsible for reporting fault-domain state to vCenter Server.
   
   The master FDM is determined through election by the FDMs that are
   alive at the time. An election occurs in the following circumstances:
   - When the vSphere HA feature is enabled for the cluster.
   - When the master's host fails.
   - When the management network is partitioned. In a network partition
     there will be a master for each partition. However, only one master
     will be responsible for a given VM. When the partition is
     resolved, all but one of the masters will abdicate.
   - After a host in a vSphere HA cluster powers back up following a failure
     that caused all hosts in the cluster to power off.
     
   The slaves are responsible for reporting state updates to the master and
   restarting VMs as required. All FDMs provide the VM/Application Health
   Monitoring Service.
   
   Attributes:
       state: The Availability State of a host based on information
           reported by the entity given by the
           `pyVmomi.vim.cluster.DasFdmHostState.stateReporter` property.
           
           See
           `pyVmomi.vim.cluster.DasFdmAvailabilityState` for the set of
           states.
       stateReporter: The entity reporting the state of the host.
           
           If the reporter is a host,
           the property reports which host, whereas if the reporter is vCenter Server,
           the property is unset.
   """
   state: str
   stateReporter: _typing.Optional[pyVmomi.vim.HostSystem] = None


class DasHostRecommendation(pyVmomi.vmodl.DynamicData):
   """
   A host recommendation for a virtual machine managed by the VMware
   HA Service.
   
   Attributes:
       host: The recommended host.
       drsRating: Rating as computed by DRS for a DRS-enabled cluster.
           
           Rating
           range from 1 to 5, and the higher the rating, the stronger DRS
           suggests this host is picked for the operation.
   """
   host: pyVmomi.vim.HostSystem
   drsRating: _typing.Optional[int] = None


class DasVmConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.cluster.DasVmConfigInfo` data object contains
   the HA configuration for a single virtual machine.
   
   All fields are optional. If you set the `modify`
   parameter to `true` when you call
   `pyVmomi.vim.ComputeResource.reconfigureEx`, an unset property has no effect
   on the existing property value in the cluster configuration on the Server.
   If you set the `modify` parameter to `false` when you
   reconfigure a cluster, the cluster configuration is reverted to the default
   values, then the new configuration values are applied.
   
   Attributes:
       key: Reference to the virtual machine.
       restartPriority: Restart priority for a virtual machine.
           
           If there is nothing specified here, then the defaults are picked up from
           `pyVmomi.vim.cluster.DasConfigInfo.defaultVmSettings`.
       powerOffOnIsolation: Flag to indicate whether or not the virtual machine should be powered off if a
           host determines that it is isolated from the rest of the compute resource.
           
           If there is nothing specified here, then the defaults are picked up from
           `pyVmomi.vim.cluster.DasConfigInfo.defaultVmSettings`.
       dasSettings: HA settings that apply to this virtual machine.
           
           Values specified in this object override the cluster-wide
           defaults for virtual machines (`pyVmomi.vim.cluster.DasConfigInfo.defaultVmSettings`).
   """
   class Priority(pyVmomi.VmomiSupport.Enum):
      """
      Deprecated: As of VI API 2.5, use `pyVmomi.vim.cluster.DasVmSettings.RestartPriority`.The priority of the virtual machine determines the preference
      given to it if sufficient capacity is not available to power
      on all failed virtual machines.
      
      For example, high priority
      virtual machines on a host get preference over low priority
      virtual machines.
      
      Attributes:
          disabled: vSphere HA is disabled for this virtual machine.
          low: Virtual machines with this priority have a lower chance of powering on after a
              failure if there is insufficient capacity on hosts to meet all virtual machine
              needs.
          medium: Virtual machines with this priority have an intermediate chance of powering
              on after a failure if there is insufficient capacity on hosts to meet all
              virtual machine needs.
          high: Virtual machines with this priority have a higher chance of powering on after a
              failure if there is insufficient capacity on hosts to meet all virtual machine
              needs.
      """
      disabled: _typing.ClassVar['DasVmConfigInfo.Priority'] = 'disabled'
      low: _typing.ClassVar['DasVmConfigInfo.Priority'] = 'low'
      medium: _typing.ClassVar['DasVmConfigInfo.Priority'] = 'medium'
      high: _typing.ClassVar['DasVmConfigInfo.Priority'] = 'high'

   key: pyVmomi.vim.VirtualMachine
   restartPriority: _typing.Optional[DasVmConfigInfo.Priority] = None
   powerOffOnIsolation: _typing.Optional[bool] = None
   dasSettings: _typing.Optional[DasVmSettings] = None


class DasVmConfigSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """An incremental update to the per-virtual-machine vSphere HA configuration."""
   info: _typing.Optional[DasVmConfigInfo] = None


class DasVmSettings(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.cluster.DasVmSettings` data object contains the HA configuration
   settings specified for a single virtual machine (identified by
   `pyVmomi.vim.cluster.DasVmConfigInfo`.`pyVmomi.vim.cluster.DasVmConfigInfo.key`)
   or as cluster-wide defaults
   `pyVmomi.vim.cluster.DasConfigInfo`.`pyVmomi.vim.cluster.DasConfigInfo.defaultVmSettings`
   
   All fields are optional. If you set the `modify` parameter to
   `true` when you call `pyVmomi.vim.ComputeResource.reconfigureEx`,
   an unset property has no effect on the existing property value in the
   cluster configuration on the Server. If you set the `modify`
   parameter to `false` when you reconfigure a cluster, the cluster
   configuration is reverted to the default values, then the new configuration
   values are applied.
   
   Attributes:
       restartPriority: Restart priority for a virtual machine.
           
           If not specified at either the cluster level or
           the virtual machine level, this will default to `medium`.
       restartPriorityTimeout: This setting is used to specify a maximum time the lower priority VMs
           should wait for the higher priority VMs to be ready.
           
           If the higher
           priority Vms are not ready by this time, then the lower priority VMs
           are restarted irrespective of the VM ready state. This timeout can be
           used to prevent the failover of lower priority VMs to be stuck
           infinitely.
           
           This timeout is not used if ready condition is
           `none`
           
           Timeout specified in seconds. To use cluster setting for a VM override,
           set to -1 in per-VM.
           setting.
       isolationResponse: Indicates whether or not the virtual machine should be powered off if a
           host determines that it is isolated from the rest of the compute
           resource.
           
           If not specified at either the cluster level or
           the virtual machine level, this will default to `powerOff`.
       vmToolsMonitoringSettings: Configuration for the VM Health Monitoring Service.
       vmComponentProtectionSettings: Configuration for the VM Component Protection Service.
   """
   class RestartPriority(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.vim.cluster.DasVmSettings.RestartPriority` enum defines
      virtual machine restart priority values to resolve resource contention.
      
      The priority determines the preference that HA gives to a virtual
      machine if sufficient capacity is not available to power on all failed
      virtual machines. For example, high priority virtual machines on a host
      get preference over low priority virtual machines.
      
      All priority values are valid for the restart priority specified in a
      single virtual machine HA configuration (`pyVmomi.vim.cluster.DasVmConfigInfo.dasSettings`).
      All values except for `clusterRestartPriority` are valid for
      the cluster-wide default HA configuration for virtual machines
      (`pyVmomi.vim.cluster.DasConfigInfo.defaultVmSettings`).
      
      Attributes:
          disabled: vSphere HA is disabled for this virtual machine.
          lowest: Virtual machines with this priority have the lowest chance of
              powering on after a failure if there is insufficient capacity on
              hosts to meet all virtual machine needs.
          low: Virtual machines with this priority have a lower chance of powering
              on after a failure if there is insufficient capacity on hosts to meet
              all virtual machine needs.
          medium: Virtual machines with this priority have an intermediate chance of
              powering on after a failure if there is insufficient capacity on
              hosts to meet all virtual machine needs.
          high: Virtual machines with this priority have a higher chance of powering
              on after a failure if there is insufficient capacity on hosts to meet
              all virtual machine needs.
          highest: Virtual machines with this priority have the highest chance of
              powering on after a failure if there is insufficient capacity on
              hosts to meet all virtual machine needs.
          clusterRestartPriority: Virtual machines with this priority use the default restart
              priority defined for the cluster that contains this virtual machine.
      """
      disabled: _typing.ClassVar['DasVmSettings.RestartPriority'] = 'disabled'
      lowest: _typing.ClassVar['DasVmSettings.RestartPriority'] = 'lowest'
      low: _typing.ClassVar['DasVmSettings.RestartPriority'] = 'low'
      medium: _typing.ClassVar['DasVmSettings.RestartPriority'] = 'medium'
      high: _typing.ClassVar['DasVmSettings.RestartPriority'] = 'high'
      highest: _typing.ClassVar['DasVmSettings.RestartPriority'] = 'highest'
      clusterRestartPriority: _typing.ClassVar['DasVmSettings.RestartPriority'] = 'clusterRestartPriority'

   class IsolationResponse(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.vim.cluster.DasVmSettings.IsolationResponse` enum defines
      values that indicate whether or not the virtual machine should be
      powered off if a host determines that it is isolated from the rest of
      the cluster.
      
      Host network isolation occurs when a host is still running but it can no
      longer communicate with other hosts in the cluster and it cannot ping
      the configured isolation address(es). When the HA agent on a host loses
      contact with the other hosts, it will ping the isolation addresses. If
      the pings fail, the host will declare itself isolated.
      
      Once the HA agent declares the host isolated, it will initiate the
      isolation response workflow after a 30 second delay. You can use the FDM
      advanced option fdm.isolationPolicyDelaySec to increase the delay. For
      each virtual machine, the HA agent attempts to determine if a master is
      responsible for restarting the virtual machine. If it cannot make the
      determination, or there is a master that is responsible, the agent will
      apply the configured isolation response. This workflow will continue
      until the configuration policy, has been applied to all virtual
      machines, the agent reconnects to another HA agent in the cluster, or
      the isolation address pings start succeeding. If there is a master agent
      in the cluster, it will attempt to restart the virtual machines that
      were powered off during isolation.
      
      By default, the isolated host leaves its virtual machines powered on.
      You can override the isolation response default with a cluster-wide
      setting (`pyVmomi.vim.cluster.DasConfigInfo.defaultVmSettings`)
      or a virtual machine setting
      (`pyVmomi.vim.cluster.DasVmSettings.isolationResponse`).
      - All isolation response values are valid for the
        `pyVmomi.vim.cluster.DasVmSettings.isolationResponse`
        property specified in a single virtual machine HA configuration.
      - All values except for `clusterIsolationResponse` are valid
        for the cluster-wide default HA configuration for virtual machines
        (`pyVmomi.vim.cluster.DasConfigInfo.defaultVmSettings`).
        
      If you ensure that your network infrastructure is sufficiently redundant
      and that at least one network path is available at all times, host network
      isolation should be a rare occurrence.
      
      Attributes:
          none: Do not power off the virtual machine in the event of a host network
              isolation.
          powerOff: Power off the virtual machine in the event of a host network
              isolation.
          shutdown: Shut down the virtual machine guest operating system in the event of
              a host network isolation.
              
              If the guest operating system fails to
              shutdown within five minutes, HA will initiate a forced power off.
              
              When you use the shutdown isolation response, failover can take
              longer (compared to the
              `powerOff`
              response) because the virtual machine cannot fail over until it is
              shutdown.
          clusterIsolationResponse: Use the default isolation response defined for the cluster
              that contains this virtual machine.
      """
      none: _typing.ClassVar['DasVmSettings.IsolationResponse'] = 'none'
      powerOff: _typing.ClassVar['DasVmSettings.IsolationResponse'] = 'powerOff'
      shutdown: _typing.ClassVar['DasVmSettings.IsolationResponse'] = 'shutdown'
      clusterIsolationResponse: _typing.ClassVar['DasVmSettings.IsolationResponse'] = 'clusterIsolationResponse'

   restartPriority: _typing.Optional[str] = None
   restartPriorityTimeout: _typing.Optional[int] = None
   isolationResponse: _typing.Optional[str] = None
   vmToolsMonitoringSettings: _typing.Optional[VmToolsMonitoringSettings] = None
   vmComponentProtectionSettings: _typing.Optional[VmComponentProtectionSettings] = None


class DatastoreUpdateSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """
   Deprecated: as of vSphere 9.0 with no replacement. In a future release
   of vSphere, the vCLS functionality will be disabled, vCLS
   system VMs will be deleted, and vCLS APIs will be removed.An incremental update to a Datastore list.
   
   Since: vSphere API Release 7.0.3.0
   """
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None

class DependencyRuleInfo(RuleInfo):
   """
   The `pyVmomi.vim.cluster.DependencyRuleInfo` data object identifies VM-to-VM
   dependencies.
   
   A VM-VM Dependency rule identifies the following groups.
   - A virtual machine group - `pyVmomi.vim.cluster.DependencyRuleInfo.vmGroup`
   - A \"depends on\" virtual machine group - `pyVmomi.vim.cluster.DependencyRuleInfo.dependsOnVmGroup`.
     
   The VMs in `pyVmomi.vim.cluster.DependencyRuleInfo.vmGroup` depends on the list of VMs specified in `pyVmomi.vim.cluster.DependencyRuleInfo.dependsOnVmGroup`.
   
   For example, this rule is used during vSphere HA VM recovery
   orchestration. vSphere HA will not restart the VMs in `pyVmomi.vim.cluster.DependencyRuleInfo.vmGroup`
   until all the VMs in `pyVmomi.vim.cluster.DependencyRuleInfo.dependsOnVmGroup` are deemded \"ready\" (See
   `pyVmomi.vim.cluster.VmReadiness`).
   
   All the virtual machines referenced by this rule must be in
   the same cluster.
   
   Attributes:
       vmGroup: Virtual group name.
           
           The virtual group may contain one or more virtual
           machines.
           `pyVmomi.vim.cluster.VmGroup`.`pyVmomi.vim.cluster.GroupInfo.name`
       dependsOnVmGroup: Dependency virtual group name
           (`pyVmomi.vim.cluster.VmGroup`.`pyVmomi.vim.cluster.GroupInfo.name`).
           
           The virtual group may contain one or more virtual machines.
   """
   vmGroup: str
   dependsOnVmGroup: str


class DpmConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   Configuration of the VMware DPM service.
   
   All fields are defined as optional. In case of a reconfiguration,
   unset fields are not changed.
   
   Attributes:
       enabled: Flag indicating whether or not the service is enabled.
           
           This
           service can not be enabled, unless DRS is enabled as well.
       defaultDpmBehavior: Specifies the default VMware DPM behavior for
           hosts.
           
           This default behavior can be overridden on a per host
           basis using the `pyVmomi.vim.cluster.DpmHostConfigInfo` object.
       hostPowerActionRate: DPM generates only those recommendations that are above the
           specified rating.
           
           Ratings vary from 1 to 5. This setting applies
           to both manual and automated `pyVmomi.vim.cluster.DpmConfigInfo.DpmBehavior` DPM clusters.
       option: Advanced settings.
   """
   class DpmBehavior(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          manual: Specifies that VirtualCenter should generate recommendations
              for host power operations, but should not execute the
              recommendations automatically.
          automated: Specifies that VirtualCenter should generate recommendations
              for host power operations, and should execute the
              recommendations automatically.
      """
      manual: _typing.ClassVar['DpmConfigInfo.DpmBehavior'] = 'manual'
      automated: _typing.ClassVar['DpmConfigInfo.DpmBehavior'] = 'automated'

   enabled: _typing.Optional[bool] = None
   defaultDpmBehavior: _typing.Optional[DpmConfigInfo.DpmBehavior] = None
   hostPowerActionRate: _typing.Optional[int] = None
   option: list[pyVmomi.vim.option.OptionValue] = []


class DpmHostConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   DPM configuration for a single host.
   
   This makes
   it possible to override the default behavior for an individual
   host.
   
   Attributes:
       key: Reference to the host.
       enabled: Flag to indicate whether or not VirtualCenter is allowed to perform any
           power related operations or recommendations for this host.
           
           If this flag is false, the host is effectively excluded from
           DPM service.
           
           If no individual DPM specification exists for a host,
           this property defaults to true.
       behavior: Specifies the particular DPM behavior for this host.
   """
   key: pyVmomi.vim.HostSystem
   enabled: _typing.Optional[bool] = None
   behavior: _typing.Optional[DpmConfigInfo.DpmBehavior] = None


class DpmHostConfigSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """
   The `pyVmomi.vim.cluster.DpmHostConfigSpec` data object provides information
   that the Server uses to update the DPM configuration for a
   single host (identified by the
   `pyVmomi.vim.cluster.DpmHostConfigInfo.key` property).
   
   The host DPM configuration overrides the cluster
   default DPM setting
   (`pyVmomi.vim.cluster.ConfigSpecEx`.`pyVmomi.vim.cluster.ConfigSpecEx.dpmConfig`).
   
   The vSphere API defines three update operations
   (`pyVmomi.vim.option.ArrayUpdateSpec`.`pyVmomi.vim.option.ArrayUpdateSpec.operation`).
   - add: Define DPM behavior for a host. If the cluster
     configuration already includes a DPM behavior override
     for the specified host, this operation
     removes the existing override and adds the new one.
     The new DPM override will use the cluster default value
     if you do not specify the behavior property
     (`pyVmomi.vim.cluster.DpmConfigInfo.defaultDpmBehavior`).
   - edit: Perform an incremental update to an existing
     DPM configuration entry for a host.
     The reconfigure method changes only the properties
     that you set in the data object. The entry must exist
     in the
     `pyVmomi.vim.cluster.ConfigSpecEx`.`pyVmomi.vim.cluster.ConfigSpecEx.dpmHostConfigSpec` array.
   - remove: Remove the DPM override for the specified
     host. To identify the host to delete, use the
     `pyVmomi.vim.option.ArrayUpdateSpec.removeKey` property
     to specify the `pyVmomi.vim.cluster.DpmHostConfigInfo.key`
     in the host override.
     
   Use the `pyVmomi.vim.ComputeResource.reconfigureEx` method
   to update the DPM configuration. If you set the modify parameter
   to true, you can use any of the three operations (add, edit, or remove).
   If you set the modify parameter to false, you can use only the
   add operation.
   """
   info: _typing.Optional[DpmHostConfigInfo] = None


class DrsConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.cluster.DrsConfigInfo` data object contains configuration information
   for the VMware DRS service.
   
   All fields are optional. If you set the `modify`
   parameter to `true` when you call
   `pyVmomi.vim.ComputeResource.reconfigureEx`, an unset property has no effect
   on the existing property value in the cluster configuration on the Server.
   If you set the `modify` parameter to `false` when you
   reconfigure a cluster, the cluster configuration is reverted to the default
   values, then the new configuration values are applied.
   
   Attributes:
       enabled: Flag indicating whether or not DRS service is enabled.
       enableVmBehaviorOverrides: Flag that dictates whether DRS Behavior overrides for individual
           virtual machines (`pyVmomi.vim.cluster.DrsVmConfigInfo`) are enabled.
           
           The default
           value is `true`.
           
           When this flag is `true`, the
           `pyVmomi.vim.cluster.ConfigSpecEx`.`pyVmomi.vim.cluster.ConfigSpecEx.drsVmConfigSpec`
           values override the `pyVmomi.vim.cluster.DrsConfigInfo.defaultVmBehavior`.
           
           When this flag is `false`, the
           `pyVmomi.vim.cluster.DrsConfigInfo.defaultVmBehavior` value applies to all virtual
           machines, with the following exception: in a cluster that has EVC disabled,
           you cannot override the virtual machine setting
           (`pyVmomi.vim.cluster.ConfigSpecEx.drsVmConfigSpec`)
           for Fault Tolerance virtual machines.
       defaultVmBehavior: Specifies the cluster-wide default DRS behavior for virtual machines.
           
           You can override the default behavior for a virtual machine
           by using the `pyVmomi.vim.cluster.DrsVmConfigInfo` object.
       vmotionRate: Threshold for generated `pyVmomi.vim.cluster.Recommendation`s.
           
           DRS generates only those recommendations that are above the
           specified vmotionRate. Ratings vary from 1 to 5. This setting applies
           to manual, partiallyAutomated, and fullyAutomated
           DRS clusters. See `pyVmomi.vim.cluster.DrsConfigInfo.DrsBehavior`.
       scaleDescendantsShares: Specifies the scaling behavior of the shares of all resource pools
           in the cluster.
           
           See `pyVmomi.vim.ResourceConfigSpec.ScaleSharesBehavior`
           for possible values. If any scaling behavior other than
           `disabled` is specified,
           the system will scale the CPU and memory shares allocated to each
           resource pool with the total shares of all powered on virtual machines
           under each respective pool. The system will also use the
           `pyVmomi.vim.SharesInfo` set on each resource pool as a multiplier for the
           scale. Setting the
           `pyVmomi.vim.cluster.DrsConfigInfo.scaleDescendantsShares` on the cluster
           is equivalent to setting the
           `pyVmomi.vim.ResourceConfigSpec.scaleDescendantsShares` on the root
           resource pool.
       option: Advanced settings.
   """
   class DrsBehavior(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          manual: Specifies that VirtualCenter should generate recommendations for
              virtual machine migration and for placement with a host,
              but should not implement the recommendations automatically.
          partiallyAutomated: Specifies that VirtualCenter should generate recommendations for
              virtual machine migration and for placement with a host,
              but should automatically implement only the placement at power on.
          fullyAutomated: Specifies that VirtualCenter should automate both the migration
              of virtual machines and their placement with a host at power on.
      """
      manual: _typing.ClassVar['DrsConfigInfo.DrsBehavior'] = 'manual'
      partiallyAutomated: _typing.ClassVar['DrsConfigInfo.DrsBehavior'] = 'partiallyAutomated'
      fullyAutomated: _typing.ClassVar['DrsConfigInfo.DrsBehavior'] = 'fullyAutomated'

   enabled: _typing.Optional[bool] = None
   enableVmBehaviorOverrides: _typing.Optional[bool] = None
   defaultVmBehavior: _typing.Optional[DrsConfigInfo.DrsBehavior] = None
   vmotionRate: _typing.Optional[int] = None
   scaleDescendantsShares: _typing.Optional[str] = None
   option: list[pyVmomi.vim.option.OptionValue] = []


class DrsFaults(pyVmomi.vmodl.DynamicData):
   """
   The faults generated by DRS when it tries to make recommendations
   for rule enforcement, power management, etc., and indexed in a tree
   structure with reason for recommendations and VM to migrate (optional)
   as the index keys.
   
   Attributes:
       reason: A reason code explaining why this set of recommendations were attempted
           by DRS when it generated the faults.
       faultsByVm: The faults grouped by VMs that DRS was trying to migrate.
   """
   class FaultsByVm(pyVmomi.vmodl.DynamicData):
      """
      FaultsByVm is the faults generated by DRS when it tries to
      move a VM.
      
      Attributes:
          vm: The VM that DRS was trying to migrate when it generated the faults.
              
              If this property is NULL, the fault is not associated with a particular VM.
          fault: The faults generated by DRS when it was trying to move the given VM.
      """
      vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
      fault: list[pyVmomi.vmodl.MethodFault] = []

   class FaultsByVirtualDisk(DrsFaults.FaultsByVm):
      """
      The faults generated by storage DRS when it tries to move a virtual disk.
      
      Attributes:
          disk: The virtual disk that storage DRS was trying to migrate when it
              generated the faults.
              
              If this property is NULL, the fault is not
              associated with a particular virtual disk.
      """
      disk: _typing.Optional[pyVmomi.vim.vm.device.VirtualDiskId] = None

   reason: str
   faultsByVm: list[DrsFaults.FaultsByVm] = []


class DrsMigration(pyVmomi.vmodl.DynamicData):
   """
   Describes a single virtual machine migration.
   
   Attributes:
       key: A unique key that identifies this recommendation.
           
           This
           is used as an argument to
           ComputeResource.applyRecommendation.
       time: The time this recommendation was computed.
       vm: The virtual machine selected for migration.
       cpuLoad: Current CPU load for the virtual machine, in MHz.
           
           This property is only populated for recommendations.
       memoryLoad: Current memory load for the virtual machine, in bytes.
           
           This field is only populated for recommendations.
       source: Source host.
       sourceCpuLoad: Current CPU load on the source host, in MHz.
       sourceMemoryLoad: Current memory usage on the source host, in bytes.
       destination: Destination host.
       destinationCpuLoad: Current CPU load on the destination host, in MHz.
       destinationMemoryLoad: Current memory usage on the destination host, in bytes.
   """
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
   """
   Deprecated: As of VI API 2.5 use `pyVmomi.vim.cluster.Recommendation`.DrsRecommendation describes a recommendation to migrate
   one or more virtual machines.
   
   Attributes:
       key: Key to identify the recommendation when calling applyRecommendation.
       rating: A rating of the recommendation.
           
           Valid values range from 1 (lowest confidence) to 5 (highest confidence).
       reason: A reason code explaining why this set of migrations is being suggested.
       reasonText: Text that provides more information about the reason code for the suggested
           set of migrations.
       migrationList: List of migrations in this recommendation and all the parent
           recommendations on which this recommendation depends.
           
           All the
           migrations in this list can be constructed from `pyVmomi.vim.cluster.Recommendation.prerequisite` and `pyVmomi.vim.cluster.Recommendation.action`.
   """
   class ReasonCode(pyVmomi.VmomiSupport.Enum):
      """
      Deprecated: As of VI API 2.5 use `pyVmomi.vim.cluster.Recommendation.ReasonCode`.List of defined migration reason codes:
      
      Attributes:
          fairnessCpuAvg: Balance average CPU utilization.
          fairnessMemAvg: Balance average memory utilization.
          jointAffin: Fulfill affinity rule.
          antiAffin: Fulfill anti-affinity rule.
          hostMaint: Host entering maintenance mode.
      """
      fairnessCpuAvg: _typing.ClassVar['DrsRecommendation.ReasonCode'] = 'fairnessCpuAvg'
      fairnessMemAvg: _typing.ClassVar['DrsRecommendation.ReasonCode'] = 'fairnessMemAvg'
      jointAffin: _typing.ClassVar['DrsRecommendation.ReasonCode'] = 'jointAffin'
      antiAffin: _typing.ClassVar['DrsRecommendation.ReasonCode'] = 'antiAffin'
      hostMaint: _typing.ClassVar['DrsRecommendation.ReasonCode'] = 'hostMaint'

   key: str
   rating: int
   reason: str
   reasonText: str
   migrationList: list[DrsMigration] = []


class DrsVmConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   DRS configuration for a single virtual machine.
   
   This makes it possible
   to override the default behavior for an individual virtual machine.
   
   Attributes:
       key: Reference to the virtual machine.
       enabled: Flag to indicate whether or not VirtualCenter is allowed to perform any
           DRS migration or initial placement recommendations for this virtual
           machine.
           
           If this flag is false, the virtual machine is effectively excluded from
           DRS.
           
           If no individual DRS specification exists for a virtual machine,
           this property defaults to true.
       behavior: Specifies the particular DRS behavior for this virtual machine.
   """
   key: pyVmomi.vim.VirtualMachine
   enabled: _typing.Optional[bool] = None
   behavior: _typing.Optional[DrsConfigInfo.DrsBehavior] = None


class DrsVmConfigSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """
   Updates the per-virtual-machine DRS configuration.
   
   To update the DRS configuration of a virtual machine, a copy of this object
   is included in the `pyVmomi.vim.cluster.ConfigSpecEx` object passed to the method
   `pyVmomi.vim.ComputeResource.reconfigureEx`.
   
   If reconfigureEx is used to
   incrementally update the cluster configuration (i.e., the parameter modify is true),
   then three operations are provided for updating the DRS configuration for a virtual machine.
   These operations are listed below (see `pyVmomi.vim.option.ArrayUpdateSpec` for more
   information on these operations).
   - add: add a configuration for the virtual machine, overwriting the existing
     configuration if one exists
   - edit: incrementally update the existing configuration; an existing configuration
     must exist
   - remove: remove the existing configuration; an existing configuration must exist
     
   If, instead, this method is used to overwrite the cluster configuration (i.e., the parameter
   modify is false) thereby creating a new configuration, only the add operation is allowed.
   In this case, add creates a DRS configuration for a virtual machine in the new cluster
   configuration.
   """
   info: _typing.Optional[DrsVmConfigInfo] = None


class EVCManager(pyVmomi.vim.ExtensibleManagedObject):
   """
   Controls Enhanced vMotion Compatibility mode for a particular cluster given
   by `pyVmomi.vim.cluster.EVCManager.managedCluster`.
   
   VMware Enhanced vMotion Compatibility (EVC) facilitates vMotion between
   different CPU generations through the use of Intel Flex Migration and AMD-V
   Extended Migration technologies. When enabled for a cluster, EVC ensures
   that all VMs are vMotion-compatible with the CPUs of all hosts in the
   cluster.
   
   See Also: `pyVmomi.vim.EVCMode`
   """
   class EVCState(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          supportedEVCMode: All supported EVC modes.
              
              Identical to
              `pyVmomi.vim.Capability.supportedEVCMode`.
          currentEVCModeKey: If unset, then EVC is disabled.
              
              If set, then EVC is enabled, and the
              value references an EVC mode described in one of the elements of the
              `pyVmomi.vim.cluster.EVCManager.EVCState.supportedEVCMode` array property. The EVC mode determines the
              set of guaranteed clusterwide CPU features. While EVC is enabled, CPU
              compatibility issues will not block any VMotion within the cluster
              (unless some VM is specifically configured to do different CPUID
              overrides).
          guaranteedCPUFeatures: When EVC is enabled, this array contains the CPU feature bits that are
              guaranteed (by EVC) to be the same among all hosts in the cluster.
              
              This property has the same value as the guaranteedCPUFeatures property
              of the configured EVC mode. On any host in the EVC cluster, the CPU
              features either naturally match these values because of the CPU
              hardware, or else CPU feature override is used to mask out differences
              and enforce a match. This array is empty when EVC is disabled.
          featureCapability: When EVC is enabled, this array contains the feature capabilities that
              are guaranteed (by EVC) to be the same among all hosts in the cluster.
              
              This property has the same value as the featureCapability property
              of the configured EVC mode. On any host in the EVC cluster, the feature
              capabilities either naturally match these values because of the CPU
              hardware, or else feature masks are used to mask out differences and
              enforce a match. This array is empty when EVC is disabled.
          featureMask: The masks (modifications to a host's feature capabilities) that limit a
              host's capabilities to that of the EVC mode baseline.
          featureRequirement: The conditions that must be true of a host's feature capabilities in order
              for the host to meet the minimum requirements of the EVC mode baseline.
      """
      supportedEVCMode: list[pyVmomi.vim.EVCMode] = []
      currentEVCModeKey: _typing.Optional[str] = None
      guaranteedCPUFeatures: list[pyVmomi.vim.host.CpuIdInfo] = []
      featureCapability: list[pyVmomi.vim.host.FeatureCapability] = []
      featureMask: list[pyVmomi.vim.host.FeatureMask] = []
      featureRequirement: list[pyVmomi.vim.vm.FeatureRequirement] = []

   class CheckResult(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          evcModeKey: The EVC mode being tested for legal application.
          error: A problem that would prevent applying the desired EVC mode.
          host: The set of hosts which would generate the fault described by the
              `pyVmomi.vim.cluster.EVCManager.CheckResult.error` property when the desired EVC mode is applied.
      """
      evcModeKey: str
      error: pyVmomi.vmodl.MethodFault
      host: list[pyVmomi.vim.HostSystem] = []

   @property
   def managedCluster(self) -> pyVmomi.vim.ClusterComputeResource:
      """Cluster associated with this manager object."""
      ...
   @property
   def evcState(self) -> EVCManager.EVCState:
      """EVC-related state of the managed cluster."""
      ...

   def ConfigureEvc(self, evcModeKey: str, evcGraphicsModeKey: _typing.Optional[str]) -> pyVmomi.vim.Task:
      """
      Set the EVC mode.
      
      If EVC is currently disabled, then this will enable
      EVC. The parameter must specify a key to one of the EVC modes listed in
      the `pyVmomi.vim.cluster.EVCManager.EVCState.supportedEVCMode` array
      property. If there are no modes listed there,
      then EVC may not currently be enabled; reference the other properties
      in `pyVmomi.vim.cluster.EVCManager.EVCState` to determine what conditions are blocking EVC.
      
      Args:
          evcModeKey: A key referencing the desired EVC mode.
          evcGraphicsModeKey: A key referencing the desired EVC Graphics
              mode `pyVmomi.vim.Capability.supportedEVCGraphicsMode`.
              
              Since: vSphere API Release 7.0.1.0
      
      Raises:
          pyVmomi.vim.fault.EVCConfigFault: if configuring EVC failed. Typically, a more
              specific subclass is thrown.
      """
      ...
   def DisableEvc(self) -> pyVmomi.vim.Task:
      """
      Disable EVC.
      
      EVC may be disabled at any time.
      """
      ...
   def CheckConfigureEvc(self, evcModeKey: str, evcGraphicsModeKey: _typing.Optional[str]) -> pyVmomi.vim.Task:
      """
      Test the validity of configuring an EVC mode on the managed cluster.
      
      Args:
          evcModeKey: A key referencing the desired EVC mode.
          evcGraphicsModeKey: A key referencing the desired EVC Graphics
              mode `pyVmomi.vim.Capability.supportedEVCGraphicsMode`.
              
              Since: vSphere API Release 7.0.1.0
      
      Returns:
          The set of errors, if any, that would result from an attempt
          to configure the desired EVC mode. Each element in the returned
          array describes an error and the hosts to which it applies.
      """
      ...
   def CheckAddHostEvc(self, cnxSpec: pyVmomi.vim.host.ConnectSpec) -> pyVmomi.vim.Task:
      """
      Test the validity of adding a host into the managed cluster.
      
      Note that
      this method only tests EVC admission control; host-add may fail for
      other reasons.
      
      Args:
          cnxSpec: The spec that will be used to add the host.
      
      Returns:
          The set of EVC-related errors, if any, that would result from
          an attempt to add the indicated host.
      
      Raises:
          pyVmomi.vim.fault.InvalidLogin: if authentication with the host fails.
          pyVmomi.vim.fault.HostConnectFault: if an error occurred when attempting to connect
              to the host. Typically, a more specific subclass is thrown.
      """
      ...


class EnterMaintenanceResult(pyVmomi.vmodl.DynamicData):
   """
   EnterMaintenanceResult is the base class of the result returned to the
   `pyVmomi.vim.ClusterComputeResource.enterMaintenanceMode` method.
   
   Attributes:
       recommendations: The list of recommendations for hosts that Virtual Center will
           be able to evacuate.
           
           Each recommendation consists of a host
           maintenance action `pyVmomi.vim.cluster.Action` for a host, along
           with zero or more vmotions for evacuation. Application of the
           recommendations is not supported currently. The client will have
           to put the hosts into maintenance mode by calling the separate
           method `pyVmomi.vim.HostSystem.enterMaintenanceMode`.
       fault: The faults that explain why the Virtual Center cannot evacuate
           some hosts.
   """
   recommendations: list[Recommendation] = []
   fault: _typing.Optional[DrsFaults] = None


class FailoverHostAdmissionControlInfo(DasAdmissionControlInfo):
   """
   The current admission control related information if the cluster was configured
   with a FailoverHostAdmissionControlPolicy.
   
   Attributes:
       hostStatus: Status of the failover hosts in the cluster.
   """
   class HostStatus(pyVmomi.vmodl.DynamicData):
      """
      Data object containing the status of a failover host.
      
      Attributes:
          host: The failover host.
          status: The status of the failover host.
              
              The status is green for a connected host with no vSphere HA errors and
              no virtual machines running on it.
              The status is yellow for a connected host with no vSphere HA errors and
              some virtual machines running on it.
              The status red for a disconnected or not responding host, a host that
              is in maintenance or standby mode or that has a vSphere HA error on it.
      """
      host: pyVmomi.vim.HostSystem
      status: pyVmomi.vim.ManagedEntity.Status

   hostStatus: list[FailoverHostAdmissionControlInfo.HostStatus] = []


class FailoverHostAdmissionControlPolicy(DasAdmissionControlPolicy):
   """
   The `pyVmomi.vim.cluster.FailoverHostAdmissionControlPolicy` dedicates
   one or more hosts for use during failover.
   
   When a host fails with this policy in place, vSphere HA attempts
   to restart its virtual machines on a dedicated failover host.
   If this is not possible, for example the failover host itself has failed
   or it has insufficient resources, HA attempts to restart those virtual
   machines on another host in the cluster.
   
   To support the availability of a failover host,
   the vCenter Server will prevent users from powering on virtual machines
   on that host, or from using vMotion to migrate virtual machines to the host.
   Also, DRS does not use the failover host for load balancing.
   
   To obtain the status of a failover host, use the
   `pyVmomi.vim.cluster.FailoverHostAdmissionControlInfo.hostStatus`
   property
   (`pyVmomi.vim.ClusterComputeResource.Summary`.`pyVmomi.vim.ClusterComputeResource.Summary.admissionControlInfo`.`pyVmomi.vim.cluster.FailoverHostAdmissionControlInfo.hostStatus`).
   
   Attributes:
       failoverHosts: List of managed object references to failover hosts.
       failoverLevel: Number of host failures that should be tolerated, still guaranteeing
           sufficient resources to restart virtual machines on available hosts.
           
           If not set, we assume 1.
   """
   failoverHosts: list[pyVmomi.vim.HostSystem] = []
   failoverLevel: _typing.Optional[int] = None

class FailoverLevelAdmissionControlInfo(DasAdmissionControlInfo):
   """
   The current admission control related information if the cluster was
   configured with a FailoverLevelAdmissionControlPolicy.
   
   Attributes:
       currentFailoverLevel: Current failover level.
           
           This is the number of physical host failures that
           can be tolerated without impacting the ability to satisfy the minimums for
           all running virtual machines. This represents the current value, as
           opposed to desired value configured by the user.
   """
   currentFailoverLevel: int


class FailoverLevelAdmissionControlPolicy(DasAdmissionControlPolicy):
   """
   The `pyVmomi.vim.cluster.FailoverLevelAdmissionControlPolicy`
   defines the number of host failures that should be tolerated and still
   guarantee enough unfragmented resources to failover all powered on virtual
   machines on those failed hosts.
   
   When you use the failover level policy, vSphere HA partitions resources
   into slots. A slot represents the minimum CPU and memory resources
   that are required to support any powered-on virtual machine in the cluster.
   
   With the failover level policy in place, HA uses the following slot
   calculations to control virtual machine migration within the cluster:
   1. Calculate the slot size from CPU and memory reservations.
      The CPU value is the largest CPU reservation for all powered-on
      virtual machines in the cluster. The memory value is the largest
      memory reservation (plus memory overhead).
      
      If your cluster contains any virtual machines that have much larger
      reservations than the others, they will distort slot size calculation.
      To avoid this, you can specify an upper bound for slot sizes;
      use the configuration editor in the vSphere Client to set the
      das.slotCpuInMHz and das.slotMemInMB attributes. When you use these
      attributes, there is a risk that resource fragmentation will cause
      virtual machines with resource requirements larger than the slot size
      to be assigned multiple slots. In a cluster that is close to capacity,
      there might be enough slots in aggregate for HA to successfully
      failover a virtual machine. However, if those slots are located
      on multiple hosts, a virtual machine assigned multiple slots cannot
      use them because a virtual machine can run on only a single host
      at a time.
   2. Determine how many slots each host in the cluster can hold.
      HA uses the CPU and memory resources in a host's root resource pool
      to determine host slot capacity, not the total physical resources
      of the host. Resources used for virtualization purposes are not
      included. HA uses connected hosts that are not in maintenance mode
      and that do not have any HA errors.
      
      The CPU slot resource is the host CPU resource amount divided
      by the CPU component of the slot size; the result is rounded down.
      HA makes the same calculation for host memory resource amount.
      HA compares the results; the lower of the two numbers is the
      host slot capacity.
   3. Determine the current failover capacity of the cluster. This is the
      number of hosts (starting from the largest) that can fail and still
      leave enough slots to satisfy all of the powered-on virtual machines.
   4. Compare the current failover capacity to the configured
      `pyVmomi.vim.cluster.FailoverLevelAdmissionControlPolicy.failoverLevel`.
      If the current failover capacity is less than the configured
      failover level, HA disallows the operation.
   
   Attributes:
       failoverLevel: Number of host failures that should be tolerated, still guaranteeing
           sufficient resources to restart virtual machines on available hosts.
       slotPolicy: A policy for how to compute the slot size.
           
           If left unset, the slot is
           computed using the maximum reservations and memory overhead of any
           powered on virtual machine in the cluster.
   """
   failoverLevel: int
   slotPolicy: _typing.Optional[SlotPolicy] = None


class FailoverResourcesAdmissionControlInfo(DasAdmissionControlInfo):
   """
   The current admission control related information if the cluster was configured
   with a FailoverResourcesAdmissionControlPolicy.
   
   Attributes:
       currentCpuFailoverResourcesPercent: The percentage of cpu resources in the cluster available for failover.
       currentMemoryFailoverResourcesPercent: The percentage of memory resources in the cluster available for failover.
       currentPMemFailoverResourcesPercent: The percentage of persistent memory resources in the cluster available
           for failover.
           
           Since: vSphere API Release 7.0.2.0
   """
   currentCpuFailoverResourcesPercent: int
   currentMemoryFailoverResourcesPercent: int
   currentPMemFailoverResourcesPercent: _typing.Optional[int] = None


class FailoverResourcesAdmissionControlPolicy(DasAdmissionControlPolicy):
   """
   The `pyVmomi.vim.cluster.FailoverResourcesAdmissionControlPolicy`
   reserves a specified percentage of aggregate cluster resources for failover.
   
   With the resources failover policy in place, vSphere HA uses the following
   calculations to control virtual machine migration in the cluster.
   1. Calculate the total resource requirements for all powered-on
      virtual machines in the cluster.
   2. Calculate the total host resources available for virtual machines.
   3. Calculate the Current CPU failover capacity, memory failover
      capacity and optionally, persistent memory failover capacity
      for the cluster.
   4. Compare the current CPU failover capacity and current memory failover
      capacity with the configured resource percentages
      (`pyVmomi.vim.cluster.FailoverResourcesAdmissionControlPolicy.cpuFailoverResourcesPercent`
      and
      `pyVmomi.vim.cluster.FailoverResourcesAdmissionControlPolicy.memoryFailoverResourcesPercent`).
      If either current capacity is less than the corresponding configured
      capacity, HA does not allow the operation.
      
   HA uses the actual reservations of the virtual machines. If a virtual machine
   does not have reservations, meaning that the reservation is 0, a default
   of 0MB memory and 256MHz CPU is applied. This is controlled by the same
   HA advanced options used for the failover level policy
   (`pyVmomi.vim.cluster.FailoverLevelAdmissionControlPolicy`).
   
   Attributes:
       cpuFailoverResourcesPercent: Percentage of CPU resources in the cluster to reserve for failover.
           
           You can specify up to 100% of CPU resources for failover.
       memoryFailoverResourcesPercent: Percentage of memory resources in the cluster to reserve for failover.
           
           You can specify up to 100% of memory resources for failover.
       failoverLevel: Number of host failures that should be tolerated, still guaranteeing
           sufficient resources to restart virtual machines on available hosts.
           
           If not set, we assume 1.
       autoComputePercentages: Flag to enable user input values for
           `pyVmomi.vim.cluster.FailoverResourcesAdmissionControlPolicy.cpuFailoverResourcesPercent`
           and
           `pyVmomi.vim.cluster.FailoverResourcesAdmissionControlPolicy.memoryFailoverResourcesPercent`
           By default, this is true and the default calculation is using the
           `pyVmomi.vim.cluster.FailoverResourcesAdmissionControlPolicy.failoverLevel`
           hosts' resources.
           
           If users want to override the percentage values,
           they must disable the auto-compute by setting this field to false.
       pMemFailoverResourcesPercent: Percentage of persistent memory resources in the cluster to reserve for
           the failover.
           
           You can specify up to 100% of persistent memory resources for failover.
           
           Since: vSphere API Release 7.0.2.0
       autoComputePMemFailoverResourcesPercent: Flag to enable user input values for
           `pyVmomi.vim.cluster.FailoverResourcesAdmissionControlPolicy.pMemFailoverResourcesPercent`
           By default, this is true and the default calculation is done using the
           `pyVmomi.vim.cluster.FailoverResourcesAdmissionControlPolicy.failoverLevel` hosts' resources.
           
           If a user wants to override the percentage values, they
           must disable the auto-compute by setting this field to false.
           
           Since: vSphere API Release 7.0.2.0
   """
   cpuFailoverResourcesPercent: int
   memoryFailoverResourcesPercent: int
   failoverLevel: _typing.Optional[int] = None
   autoComputePercentages: _typing.Optional[bool] = None
   pMemFailoverResourcesPercent: _typing.Optional[int] = None
   autoComputePMemFailoverResourcesPercent: _typing.Optional[bool] = None


class VsanFaultDomainSpec(pyVmomi.vmodl.DynamicData):
   """
   Describes a fault domain structure.
   
   Attributes:
       hosts: List of hosts that will participate in the newly created fault domain.
       name: The name of the fault domain.
   """
   hosts: list[pyVmomi.vim.HostSystem] = []
   name: str

class FaultDomainDestroySpec(VsanFaultDomainSpec):
   """The specification to destroy a site fault domain."""
   pass

class FaultDomainUpdateSpec(VsanFaultDomainSpec):
   """
   The incremental modification specification to site fault domain members.
   
   Attributes:
       operation: The operation requested to this specific vSAN site fault domain,
           identified by `pyVmomi.vim.cluster.VsanFaultDomainSpec.name`,
           allowed values please check `pyVmomi.vim.option.ArrayUpdateSpec.Operation`:
           - add: Add specified hosts into the existing fault domain incrementally
           - remove: Remove the given set of hosts from specified fault domain
           - edit: Overwrite the associated members with given set of hosts
   """
   operation: str


class SlotPolicy(pyVmomi.vmodl.DynamicData):
   """
   The base class `pyVmomi.vim.cluster.SlotPolicy` is used for specifying how
   the slot size is to be computed for the failover level HA admission control
   policy.
   
   By default, vSphere HA defines the slot size using the largest memory
   and cpu reservations of any powered on virtual machine in the cluster.
   Subclasses of this class define various policies to modify how the slot size
   is chosen to prevent outlier virtual machines (i.e. those with much larger
   reservations than the average) from skewing the slot size. If such a policy is chosen,
   outlier virtual machines will use multiple slots. Using such a policy introduces
   a risk that vSphere HA will be unable to failover these virtual machines because
   of resource fragmentation.
   """
   pass

class FixedSizeSlotPolicy(SlotPolicy):
   """
   This policy allows setting a fixed slot size
   
   Attributes:
       cpu: The cpu component of the slot size (in MHz)
       memory: The memory component of the slot size (in megabytes)
   """
   cpu: int
   memory: int


class FtVmHostRuleInfo(RuleInfo):
   """
   An `pyVmomi.vim.cluster.FtVmHostRuleInfo` object provides control of the
   placement of virtual machines across two host groups.
   
   The virtual machines
   and hosts referenced by an FT VM-Host rule must be in the same cluster.
   
   An FT VM-Host rule identifies the following groups.
   - A virtual machine group name (`pyVmomi.vim.cluster.VmGroup`).
   - An array of two host groups (`pyVmomi.vim.cluster.HostGroup`).
     
   `pyVmomi.vim.cluster.FtVmHostRuleInfo` stores only the names of the relevant
   virtual machine and host groups. The group contents are stored in
   the virtual machine and host group objects.
   
   When employing this rule, take care to ensure that the specified
   host groups have sufficient resources to support the requirements
   of all VMs specified.
   
   Attributes:
       vmGroupName: Virtual machine group name
           (`pyVmomi.vim.cluster.VmGroup`.`pyVmomi.vim.cluster.GroupInfo.name`).
           
           The named virtual machine group may have zero or more VMs.
           A virtual machine in this group may be a normal virtual machine
           or a fault tolerant primary virtual machine; it cannot
           be a fault tolerant secondary virtual machine.
           
           Control of FT secondary virtual machines is implied by the presence
           of the primary FT virtual machine.
           
           A virtual machine in this group should not be referenced in any other
           FT VM-Host rule or VM-Host rule `pyVmomi.vim.cluster.VmHostRuleInfo`.
       hostGroupName: Array of two Host Groups (`pyVmomi.vim.cluster.HostGroup`).
           
           The hostGroup array must have two host groups. Each host group in the
           hostGroup array will have a set of hosts. For each Fault Tolerance primary
           VM that is part of VmGroup, the primary and secondary VMs would be placed
           on hosts that are not part of the same host group.
           
           The members of each host group should be disjoint from the members
           of all other host group specified.
   
   Since: vSphere API Release 8.0.3.0
   """
   vmGroupName: str
   hostGroupName: list[str] = []


class GroupInfo(pyVmomi.vmodl.DynamicData):
   """
   `pyVmomi.vim.cluster.GroupInfo` is the base type for all virtual machine
   and host groups.
   
   All virtual machines and hosts that are part of a group
   must be part of the same cluster.
   
   Attributes:
       name: Unique name of the group.
       userCreated: Flag to indicate whether the group is created by the user or the system.
       uniqueID: Unique ID for the group.
           
           uniqueID is unique within a cluster.
           Groups residing in different clusters might share a uniqueID.
   """
   name: str
   userCreated: _typing.Optional[bool] = None
   uniqueID: _typing.Optional[str] = None


class GroupSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """An incremental update to the cluster-wide groups."""
   info: _typing.Optional[GroupInfo] = None


class HostGroup(GroupInfo):
   """
   The `pyVmomi.vim.cluster.HostGroup` data object identifies hosts for VM-Host rules.
   
   VM-Host rules determine placement of virtual machines on hosts in a cluster.
   The logic specified in a `pyVmomi.vim.cluster.VmHostRuleInfo` object
   determines where virtual machines can be powered-on.
   
   Attributes:
       host: List of hosts that are part of this group.
           
           A host group can contain zero or more hosts.
   """
   host: list[pyVmomi.vim.HostSystem] = []


class HostInfraUpdateHaModeAction(Action):
   """
   Describes a HostSystem's quarantine or maintenance mode change action.
   
   Attributes:
       operationType: Specify the action type.
           
           Values are of type
           `pyVmomi.vim.cluster.HostInfraUpdateHaModeAction.OperationType`.
   """
   class OperationType(pyVmomi.VmomiSupport.Enum):
      """
      Describes the operation type of the action.
      
      enterexitQuarantine suggests
      that the host is only exiting the quarantine state (i.e. not the
      maintenance mode).
      """
      enterQuarantine: _typing.ClassVar['HostInfraUpdateHaModeAction.OperationType'] = 'enterQuarantine'
      exitQuarantine: _typing.ClassVar['HostInfraUpdateHaModeAction.OperationType'] = 'exitQuarantine'
      enterMaintenance: _typing.ClassVar['HostInfraUpdateHaModeAction.OperationType'] = 'enterMaintenance'

   operationType: str


class HostPowerAction(Action):
   """
   Describes a single host power action.
   
   Attributes:
       operationType: Specify whether the action is power on or power off
       powerConsumptionWatt: Estimated power consumption of the host.
           
           In case of power-on,
           this is the projected increase in the cluster's power
           consumption. In case of power off, this is the projected
           decrease in the cluster's power consumption
       cpuCapacityMHz: CPU capacity of the host in units of MHz.
           
           In case of power-on
           action, this is the projected increase in the cluster's CPU
           capacity. In case of power off, this is the projected decrease
           in the cluster's CPU capacity.
       memCapacityMB: Memory capacity of the host in units of MM.
           
           In case of power-on
           action, this is the projected increase in the cluster's memory
           capacity. In case of power off, this is the projected decrease
           in the cluster's memory capacity.
   """
   class OperationType(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          powerOn: Power On Operation
          powerOff: Power Off Operation.
              
              Power off operation puts the host in
              a state that can be woken up remotely.
      """
      powerOn: _typing.ClassVar['HostPowerAction.OperationType'] = 'powerOn'
      powerOff: _typing.ClassVar['HostPowerAction.OperationType'] = 'powerOff'

   operationType: HostPowerAction.OperationType
   powerConsumptionWatt: _typing.Optional[int] = None
   cpuCapacityMHz: _typing.Optional[int] = None
   memCapacityMB: _typing.Optional[int] = None


class HostRecommendation(pyVmomi.vmodl.DynamicData):
   """
   A DRS recommended host for either powering on, resuming or
   reverting a virtual machine, or migrating a virtual machine from
   outside the cluster.
   
   Attributes:
       host: The recommended host.
       rating: Rating for the recommendation.
           
           Ratings range from 1 to 5, and
           the higher the rating, the stronger DRS suggests this host is
           picked for the operation.
   """
   host: pyVmomi.vim.HostSystem
   rating: int


class InfraUpdateHaConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   Configuration of the vSphere InfraUpdateHA service.
   
   All fields are defined as optional. In case of a reconfiguration,
   unset fields are not changed.
   
   Attributes:
       enabled: Flag indicating whether or not the service is enabled.
           
           InfraUpdateHA
           will not be active, unless DRS is enabled as well.
       behavior: Configured behavior.
           
           Values are of type
           `pyVmomi.vim.cluster.InfraUpdateHaConfigInfo.BehaviorType`.
       moderateRemediation: Configured remediation for moderately degraded hosts.
           
           Values are of type
           `pyVmomi.vim.cluster.InfraUpdateHaConfigInfo.RemediationType`.
           Configuring MaintenanceMode for moderateRemedation and QuarantineMode for
           severeRemediation is not supported and will throw InvalidArgument.
       severeRemediation: Configured remediation for severely degraded hosts.
           
           Values are of type
           `pyVmomi.vim.cluster.InfraUpdateHaConfigInfo.RemediationType`.
       providers: The list of health update providers configured for this cluster.
           
           Providers are identified by their id.
           
           When reconfiguring the cluster, a list with a single element {\"\"} will
           clear the list of providers.
           
           If the provider list is empty, InfraUpdateHA will not be active.
   """
   class BehaviorType(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          Manual: With this behavior configured, the proposed DRS recommendations
              require manual approval before they are executed.
          Automated: With this behavior configured, the proposed DRS recommendations are
              executed immediately.
      """
      Manual: _typing.ClassVar['InfraUpdateHaConfigInfo.BehaviorType'] = 'Manual'
      Automated: _typing.ClassVar['InfraUpdateHaConfigInfo.BehaviorType'] = 'Automated'

   class RemediationType(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          QuarantineMode: With this behavior configured, a degraded host will be recommended
              to be placed in Quarantine Mode.
          MaintenanceMode: With this behavior configured, a degraded host will be recommended
              to be placed in Maintenance Mode.
      """
      QuarantineMode: _typing.ClassVar['InfraUpdateHaConfigInfo.RemediationType'] = 'QuarantineMode'
      MaintenanceMode: _typing.ClassVar['InfraUpdateHaConfigInfo.RemediationType'] = 'MaintenanceMode'

   enabled: _typing.Optional[bool] = None
   behavior: _typing.Optional[str] = None
   moderateRemediation: _typing.Optional[str] = None
   severeRemediation: _typing.Optional[str] = None
   providers: list[str] = []


class InitialPlacementAction(Action):
   """
   Describes an initial placement of a single virtual machine
   
   Attributes:
       targetHost: The host where the virtual machine should be initially placed.
       pool: The resource pool to place the virtual machine into in case this
           action is for migrating from outside cluster.
   """
   targetHost: pyVmomi.vim.HostSystem
   pool: _typing.Optional[pyVmomi.vim.ResourcePool] = None


class MigrationAction(Action):
   """
   Describes a single VM migration action.
   
   Attributes:
       drsMigration: The details of the migration action
   """
   drsMigration: _typing.Optional[DrsMigration] = None


class NotAttemptedVmInfo(pyVmomi.vmodl.DynamicData):
   """
   This data class reports one virtual machine powerOn failure.
   
   Attributes:
       vm: The virtual machine that can not be powered on.
       fault: The exception returned.
   """
   vm: pyVmomi.vim.VirtualMachine
   fault: pyVmomi.vmodl.MethodFault


class OrchestrationInfo(pyVmomi.vmodl.DynamicData):
   """
   vSphere cluster VM orchestration settings.
   
   Used by vSphere HA when restarting failed VMs. For example, if a host
   fails, vSphere HA identifies the list of VMs to be restarted. The order in
   which the failed VMs to be restarted is determined by:
   - VM restart priority setting (`pyVmomi.vim.cluster.DasVmSettings.restartPriority`).
     Lower priority VMs are restarted only after higher priority VMs are
     restarted and ready (`pyVmomi.vim.cluster.VmReadiness`).
   - VM dependency rule (`pyVmomi.vim.cluster.DependencyRuleInfo`). If a VM
     depends on other VMs, then it will be restarted only after all the VMs in
     its dependency list are ready. Cyclic dependency is not permitted across
     VMs. Also, higher priority VMs cannot depend on lower priority VMs.
   
   Attributes:
       defaultVmReadiness: Cluster-wide defaults for virtual machine readiness
   """
   defaultVmReadiness: _typing.Optional[VmReadiness] = None


class PerformClusterPowerActionSpec(pyVmomi.vmodl.DynamicData):
   """
   This class describes the PerformClusterPowerActionSpec spec.
   
   It can be
   used in `pyVmomi.vim.cluster.VsanClusterPowerSystem.performClusterPowerAction`.
   
   Attributes:
       targetPowerStatus: Specify the target vim.cluster.ClusterPowerStatus.
           
           If the spec is applied on VC, only clusterPoweredOn and clusterPoweredOff are
           allowed.
           If the spec is applied on host with isOrchestration set to true, only
           clusterPoweredOn and clusterPoweredOff are allowed and initialPowerStatus
           must be set.
           If the spec is applied on host with isOrchestration set to false, only host
           level status are allowed as following: vsanMemberShipUpdateDisabled,
           vsanDOMPauseAllCCPsSet, hostsInMM, hostsPoweredOff, hostsOutOfMM,
           vsanMemberShipUpdateEnabled, vsanDOMPauseAllCCPsUnset.
       isOrchestration: Note this only works in a host level API call to indicate
           whether this call applies the orchestration host logic or not.
           
           If isOrchestration is True, the host coordinates all other hosts in the
           cluster to take power action. Otherwise, it executes each step on the host
           itself.
       initialPowerStatus: Note this only works in an orchestration host level API call to indicate
           which power action item step is to begin with.
       powerOffReason: Provide the power off reason.
           
           It should be less than 512 characters in
           length.
       infraVMs: The infrastructure VMs that will be force to power off during the power off
           workflow and will be automatically powered on.
           
           This only works in a vc
           level API call and is ignored in the host level API call.
       infraVMUuids: The uuid of infrastructure VMs that will be force to power off during the
           power off workflow and will be automatically powered on.
           
           This only works
           in a host level API call and is ignored in the vc level API call.
   """
   targetPowerStatus: str
   isOrchestration: _typing.Optional[bool] = None
   initialPowerStatus: _typing.Optional[str] = None
   powerOffReason: _typing.Optional[str] = None
   infraVMs: list[pyVmomi.vim.VirtualMachine] = []
   infraVMUuids: list[str] = []


class PlacementAction(Action):
   """
   Describes a placement action of a single virtual machine.
   
   One or more of such actions can be included in a placement recommendation,
   and such recommendations can be generated by the
   `pyVmomi.vim.ClusterComputeResource.placeVm` method.
   
   Attributes:
       vm: Virtual machine reference.
           
           Unset if the VM has not been created.
       targetHost: The host where the virtual machine should be placed.
           
           Unset if no host recommendation is provided.
       relocateSpec: Specification for placing the configuration files and the virtual
           disks of the virtual machine on one or more datastores.
           
           Unset if no datastore recommendation is provided.
   """
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   targetHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
   relocateSpec: _typing.Optional[pyVmomi.vim.vm.RelocateSpec] = None


class PlacementResult(pyVmomi.vmodl.DynamicData):
   """
   `pyVmomi.vim.ClusterComputeResource.placeVm` method can invoke DRS
   for recommendations for target hosts and datastores for placing a
   virtual machine and its virtual disks using xVMotion.
   
   PlacementResult is the class of the result returned by that method.
   
   Attributes:
       recommendations: The list of recommendations for where to place the virtual machine
           and its virtual disks.
       drsFault: Information about any fault in case DRS fails to make a recommendation.
   """
   recommendations: list[Recommendation] = []
   drsFault: _typing.Optional[DrsFaults] = None


class PlacementSpec(pyVmomi.vmodl.DynamicData):
   """
   PlacementSpec encapsulates all of the information passed to the
   `pyVmomi.vim.ClusterComputeResource.placeVm` method, which asks
   DRS for recommendations for target hosts and datastores for placing
   a virtual machine and its virtual disks in a cluster using
   unified VMotion.
   
   Attributes:
       priority: Priority of the migration operation.
           
           The default value is defaultPriority.
       vm: The virtual machine to be placed.
           
           For an intra-vCenter migration, this argument is required.
           For a cross-vCenter migration, this argument should be unset,
           and the caller is responsible for applying the DRS-recommended
           placement to the correct vm.
       configSpec: Configuration information for the virtual machine.
           
           For an intra-vCenter migration, this argument should be unset.
           For a cross-vCenter migration, this argument is required.
           In the latter case, the following elements of the configSpec
           will be expected: version, cpuAllocation, memoryAllocation, numCPUs,
           memoryMB, files, swapPlacement; in addition, the configSpec.deviceChange
           should contain all the virtual disks of the virtual machine to be migrated.
           If configSpec.deviceChange is empty, the vm will be treated as a
           diskless vm.
           If a storage profile is specified for a virtual disk or vm configuration,
           only datastores that match this profile will be considered for that
           virtual disk or vm configuration.
       relocateSpec: Specification for relocating a virtual machine.
           
           Can be used to optionally specify a target host, a target datastore,
           or a target resource pool. If a target host is specified, this host
           becomes the recommended host; if a target datastore is specified,
           this datastore becomes the recommended datastore; if no resource
           pool is specified, the virtual machine will be attached to the
           cluster root resource pool; if the target resource pool specified
           is a VirtualApp, an InvalidArgument fault will be thrown.
           If a storage profile is specified for a virtual disk or vm configuration,
           only datastores that match this profile will be considered for that
           virtual disk or vm configuration.
           For cross-vCenter migration, the caller
           should set the service and the folder arguments properly either in
           the input relocateSpec or in the output relocateSpec in the placement
           recommendation before passing the relocateSpec to the RelocateVM API.
       hosts: A list of compatible hosts for the virtual machine.
           
           This list is ignored if relocateSpec.host is set.
           For both intra-vCenter and cross-vCenter migrations, this list is required
           if relocateSpec.host is unset.
           If neither relocateSpec.host nor a list of compatible hosts are specified,
           all hosts in the cluster will be considered, in which case, the selected
           hosts in the PlacementResult are not guaranteed to be compatible with the
           incoming virtual machine.
       datastores: A list of compatible datastores for the virtual machine.
           
           This list is ignored if relocateSpec.datastore is set.
           For both intra-vCenter and cross-vCenter migrations, this list is required
           if relocateSpec.datastore is unset.
           If neither relocateSpec.datastore nor a list of compatible datastores are
           specified, all datastores connected to hosts in the cluster will be
           considered, in which case, the selected datastores in the PlacementResult
           are not guaranteed to be compatible with the incoming virtual machine.
       storagePods: A list of compatible datastore clusters for the virtual machine.
           
           This list is ignored if relocateSpec.datastore is set.
           For both intra-vCenter and cross-vCenter migrations, this list can be
           empty, in which case, the user should set either RelocateSpec.datastore
           or PlacementSpec.datastores as the target datastore or the list of
           compatible datastores.
       disallowPrerequisiteMoves: Specification for whether to disable pre-requisite vmotions or storage
           vmotions for virtual machine placement.
           
           The default value is true,
           that is, to disallow such prerequisite moves.
       rules: A list of rules to respect while placing the virtual machine on
           target cluster.
           
           If the list is empty, rules will not be considered during placement,
           in case of cross-cluster placement within a VC and cross VC
           placement across VCs.
       key: Client generated identifier as a reference to the placement request
       placementType: Type of the placement.
           
           The set of possible values are described in
           `pyVmomi.vim.cluster.PlacementSpec.PlacementType`
       cloneSpec: Specification for a virtual machine clone operation
       cloneName: Name for the cloned virtual machine, if the operation type is a clone
   """
   class PlacementType(pyVmomi.VmomiSupport.Enum):
      """
      Defines the type of placement
      
      Attributes:
          create: Create a new VM
          reconfigure: Reconfigure a VM
          relocate: Relocate a VM
          clone: Clone a VM
      """
      create: _typing.ClassVar['PlacementSpec.PlacementType'] = 'create'
      reconfigure: _typing.ClassVar['PlacementSpec.PlacementType'] = 'reconfigure'
      relocate: _typing.ClassVar['PlacementSpec.PlacementType'] = 'relocate'
      clone: _typing.ClassVar['PlacementSpec.PlacementType'] = 'clone'

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
   """Defines the options for a Datacenter::powerOnVm() invocation."""
   pass


class PowerOnVmResult(pyVmomi.vmodl.DynamicData):
   """
   PowerOnVmResult is the base class of the result returned to the
   `pyVmomi.vim.Datacenter.powerOnVm` method.
   
   Attributes:
       attempted: The list of virtual machines the Virtual Center has attempted to power on.
           
           For a virtual machine not managed by DRS, a task ID is also returned.
       notAttempted: The list of virtual machines DRS can not find suitable hosts for powering on.
           
           There is one fault associated with each virtual machine.
       recommendations: The list of recommendations that need the client to approve manually.
   """
   attempted: list[AttemptedVmInfo] = []
   notAttempted: list[NotAttemptedVmInfo] = []
   recommendations: list[Recommendation] = []


class PreemptibleVmPairInfo(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.cluster.PreemptibleVmPairInfo` data object contains the monitored and the
   preemptible VM pair in a HA-enabled cluster.
   
   Monitored virtual machine is a desired protected virtual machine in
   HA-enabled cluster when it is powered on. Any failures of this VM will
   continue to be handled by HA based on the VM's settings in cluster.
   
   Preemptible virtual machine is the desired protected virtual machine in HA
   when it is powered on. The lowest restart priority \"disabled\"
   `pyVmomi.vim.cluster.DasVmSettings.RestartPriority` will be enforced for the
   `pyVmomi.vim.cluster.PreemptibleVmPairInfo.preemptibleVm`. A virtual machine can be marked as preemptible
   irrespective of its `pyVmomi.vim.vm.RuntimeInfo.powerState` but its
   extra configuration should identify it as preemptible.
   
   In case of failure of `pyVmomi.vim.cluster.PreemptibleVmPairInfo.monitoredVm`, the `pyVmomi.vim.cluster.PreemptibleVmPairInfo.preemptibleVm` will
   be terminated. This will free up any resources associated with
   `pyVmomi.vim.cluster.PreemptibleVmPairInfo.preemptibleVm`.
   
   In case of insufficient resources for failover of any VM in the cluster, the
   `pyVmomi.vim.cluster.PreemptibleVmPairInfo.preemptibleVm` will be terminated to free up resources.
   
   This data object is intended for VMware use and other usage is not
   supported. This data object will be removed in a future release.
   
   Attributes:
       id: Server-assigned unique ID for pairs.
           
           When adding a new pair, do not
           specify this property. The server will assign the key and any assigned
           value will be ignored.
       monitoredVm: The virtual machine whose failure will cause the virtual machine specified
           by `pyVmomi.vim.cluster.PreemptibleVmPairInfo.preemptibleVm` to be terminated.
       preemptibleVm: The preemptible virtual machine associated with the virtual machine
           specified as `pyVmomi.vim.cluster.PreemptibleVmPairInfo.monitoredVm`.
   
   Since: vSphere API Release 8.0.0.1
   """
   id: _typing.Optional[int] = None
   monitoredVm: pyVmomi.vim.VirtualMachine
   preemptibleVm: pyVmomi.vim.VirtualMachine


class PreemptibleVmPairSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """
   Provides monitored and preemptible VM pair along with any of the operations
   (add, edit or remove) to append, modify or remove this pair info from
   `pyVmomi.vim.cluster.PreemptibleVmPairInfo` list.
   
   This data object is intended for VMware use and other usage is not supported.
   This data object will be removed in a future release.
   
   Since: vSphere API Release 8.0.0.1
   """
   info: _typing.Optional[PreemptibleVmPairInfo] = None


class ProactiveDrsConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   Attributes:
       enabled: Flag indicating whether or not the service is enabled.
   """
   enabled: _typing.Optional[bool] = None


class QueryVsanManagedStorageSpaceUsageSpec(pyVmomi.vmodl.DynamicData):
   """
   This class describes the QueryVsanManagedStorageSpaceUsage spec.
   
   It can be
   used in
   `pyVmomi.vim.cluster.VsanSpaceReportSystem.queryVsanManagedStorageSpaceUsage`.
   
   Attributes:
       datastoreTypes: Specify the datastore types to query from.
           
           The detailed datastore types
           Please refer to `pyVmomi.vim.cluster.VsanDatastoreType`.
   """
   datastoreTypes: list[str] = []


class Recommendation(pyVmomi.vmodl.DynamicData):
   """
   Recommendation is the base class for any packaged group of
   actions that are intended to take the system from one
   state to another one.
   
   Attributes:
       key: Key to identify the recommendation when calling applyRecommendation.
       type: Type of the recommendation.
           
           This differentiates between various
           of recommendations aimed at achieving different goals.
       time: The time this recommendation was computed.
       rating: A rating of the recommendation.
           
           Valid values range from 1 (lowest confidence) to 5 (highest confidence).
       reason: A reason code explaining why this set of migrations is being suggested.
       reasonText: Text that provides more information about the reason code for the suggested
           set of migrations.
       warningText: Text that provides warnings about potential adverse implications of
           applying this recommendation
       warningDetails: Warning about potential adverse implications of applying a recommendation
       prerequisite: This recommendation may depend on some other recommendations.
           
           The prerequisite recommendations are listed by their keys.
       action: List of actions that are executed as part of this recommendation
       target: The target object of this recommendation.
   """
   class RecommendationType(pyVmomi.VmomiSupport.Enum):
      """
      Pre-defined constants for possible recommendation types.
      
      Virtual Center
      uses this information to coordinate with the clients.
      """
      V1: _typing.ClassVar['Recommendation.RecommendationType'] = 'V1'

   class ReasonCode(pyVmomi.VmomiSupport.Enum):
      """
      List of defined migration reason codes:
      
      Attributes:
          fairnessCpuAvg: Balance average CPU utilization.
          fairnessMemAvg: Balance average memory utilization.
          jointAffin: Fulfill affinity rule.
          antiAffin: Fulfill anti-affinity rule.
          hostMaint: Host entering maintenance mode.
          enterStandby: Host entering standby mode.
          reservationCpu: balance CPU reservations
          reservationMem: balance memory reservations
          powerOnVm: Power on virtual machine
          powerSaving: Power off host for power savings
          increaseCapacity: Power on host to increase cluster capacity
          checkResource: Sanity-check resource pool hierarchy
          unreservedCapacity: Maintain unreserved capacity
          colocateCommunicatingVM: Co-locate communicating VMs
          balanceNetworkBandwidthUsage: Balance average network bandwidth utilization
          vmHostHardAffinity: Fix hard VM/host affinity rule violation
          vmHostSoftAffinity: Fix soft VM/host affinity rule violation
          increaseAllocation: Increase resource allocation for a VM or VMs
          balanceDatastoreSpaceUsage: Balance datastore space usage.
          balanceDatastoreIOLoad: Balance datastore I/O workload.
          balanceDatastoreIOPSReservation: Balance datastore IOPS reservation
          datastoreMaint: Datastore entering maintenance mode.
          virtualDiskJointAffin: Fix virtual disk affinity rule violation.
          virtualDiskAntiAffin: Fix virtual disk anti-affinity rule violation.
          datastoreSpaceOutage: Fix the issue that a datastore run out of space.
          storagePlacement: Satisfy storage initial placement requests.
          iolbDisabledInternal: IO load balancing was disabled internally.
          xvmotionPlacement: Satisfy unified vmotion placement requests.
          networkBandwidthReservation: Fix network bandwidth reservation violation
          hostInDegradation: Host is partially degraded.
          hostExitDegradation: Host is not degraded.
          maxVmsConstraint: Fix maxVms constraint violation
          ftConstraints: Fix ft maxVMs and maxVcpus constraint violations
          vmHostAffinityPolicy: Fix VM/host affinity policy violation
          vmHostAntiAffinityPolicy: Fix VM/host anti-affinity policy violation
          vmAntiAffinityPolicy: Fix VM-VM anti-affinity policy violations
          balanceVsanUsage: Since: vSphere API Release 7.0.2.0
          ahPlacementOptimization: Optimize assignable hardware resource orchestration
              
              Since: vSphere API Release 8.0.2.0
          vmxUpgrade: Upgrade virtual machine to new vmx binary
              
              Since: vSphere API Release 8.0.3.0
      """
      fairnessCpuAvg: _typing.ClassVar['Recommendation.ReasonCode'] = 'fairnessCpuAvg'
      fairnessMemAvg: _typing.ClassVar['Recommendation.ReasonCode'] = 'fairnessMemAvg'
      jointAffin: _typing.ClassVar['Recommendation.ReasonCode'] = 'jointAffin'
      antiAffin: _typing.ClassVar['Recommendation.ReasonCode'] = 'antiAffin'
      hostMaint: _typing.ClassVar['Recommendation.ReasonCode'] = 'hostMaint'
      enterStandby: _typing.ClassVar['Recommendation.ReasonCode'] = 'enterStandby'
      reservationCpu: _typing.ClassVar['Recommendation.ReasonCode'] = 'reservationCpu'
      reservationMem: _typing.ClassVar['Recommendation.ReasonCode'] = 'reservationMem'
      powerOnVm: _typing.ClassVar['Recommendation.ReasonCode'] = 'powerOnVm'
      powerSaving: _typing.ClassVar['Recommendation.ReasonCode'] = 'powerSaving'
      increaseCapacity: _typing.ClassVar['Recommendation.ReasonCode'] = 'increaseCapacity'
      checkResource: _typing.ClassVar['Recommendation.ReasonCode'] = 'checkResource'
      unreservedCapacity: _typing.ClassVar['Recommendation.ReasonCode'] = 'unreservedCapacity'
      colocateCommunicatingVM: _typing.ClassVar['Recommendation.ReasonCode'] = 'colocateCommunicatingVM'
      balanceNetworkBandwidthUsage: _typing.ClassVar['Recommendation.ReasonCode'] = 'balanceNetworkBandwidthUsage'
      vmHostHardAffinity: _typing.ClassVar['Recommendation.ReasonCode'] = 'vmHostHardAffinity'
      vmHostSoftAffinity: _typing.ClassVar['Recommendation.ReasonCode'] = 'vmHostSoftAffinity'
      increaseAllocation: _typing.ClassVar['Recommendation.ReasonCode'] = 'increaseAllocation'
      balanceDatastoreSpaceUsage: _typing.ClassVar['Recommendation.ReasonCode'] = 'balanceDatastoreSpaceUsage'
      balanceDatastoreIOLoad: _typing.ClassVar['Recommendation.ReasonCode'] = 'balanceDatastoreIOLoad'
      balanceDatastoreIOPSReservation: _typing.ClassVar['Recommendation.ReasonCode'] = 'balanceDatastoreIOPSReservation'
      datastoreMaint: _typing.ClassVar['Recommendation.ReasonCode'] = 'datastoreMaint'
      virtualDiskJointAffin: _typing.ClassVar['Recommendation.ReasonCode'] = 'virtualDiskJointAffin'
      virtualDiskAntiAffin: _typing.ClassVar['Recommendation.ReasonCode'] = 'virtualDiskAntiAffin'
      datastoreSpaceOutage: _typing.ClassVar['Recommendation.ReasonCode'] = 'datastoreSpaceOutage'
      storagePlacement: _typing.ClassVar['Recommendation.ReasonCode'] = 'storagePlacement'
      iolbDisabledInternal: _typing.ClassVar['Recommendation.ReasonCode'] = 'iolbDisabledInternal'
      xvmotionPlacement: _typing.ClassVar['Recommendation.ReasonCode'] = 'xvmotionPlacement'
      networkBandwidthReservation: _typing.ClassVar['Recommendation.ReasonCode'] = 'networkBandwidthReservation'
      hostInDegradation: _typing.ClassVar['Recommendation.ReasonCode'] = 'hostInDegradation'
      hostExitDegradation: _typing.ClassVar['Recommendation.ReasonCode'] = 'hostExitDegradation'
      maxVmsConstraint: _typing.ClassVar['Recommendation.ReasonCode'] = 'maxVmsConstraint'
      ftConstraints: _typing.ClassVar['Recommendation.ReasonCode'] = 'ftConstraints'
      vmHostAffinityPolicy: _typing.ClassVar['Recommendation.ReasonCode'] = 'vmHostAffinityPolicy'
      vmHostAntiAffinityPolicy: _typing.ClassVar['Recommendation.ReasonCode'] = 'vmHostAntiAffinityPolicy'
      vmAntiAffinityPolicy: _typing.ClassVar['Recommendation.ReasonCode'] = 'vmAntiAffinityPolicy'
      balanceVsanUsage: _typing.ClassVar['Recommendation.ReasonCode'] = 'balanceVsanUsage'
      ahPlacementOptimization: _typing.ClassVar['Recommendation.ReasonCode'] = 'ahPlacementOptimization'
      vmxUpgrade: _typing.ClassVar['Recommendation.ReasonCode'] = 'vmxUpgrade'

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
   """
   This class contains cpu, memory and storage usage information at cluster
   level.
   
   Attributes:
       pMemAvailableMB: Do not use.
       pMemCapacityMB: Do not use.
   """
   cpuUsedMHz: int
   cpuCapacityMHz: int
   memUsedMB: int
   memCapacityMB: int
   pMemAvailableMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   pMemCapacityMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   storageUsedMB: pyVmomi.VmomiSupport.long
   storageCapacityMB: pyVmomi.VmomiSupport.long


class RuleSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """An incremental update to the cluster rules."""
   info: _typing.Optional[RuleInfo] = None


class SiteFaultDomain(pyVmomi.vmodl.DynamicData):
   """
   The configuration of a site fault domain.
   
   Attributes:
       hosts: List of hosts that associate to this site fault domain.
       name: The name of the site fault domain.
   """
   hosts: list[pyVmomi.vim.HostSystem] = []
   name: str


class SiteFaultDomainConfig(pyVmomi.vmodl.DynamicData):
   """
   The cluster configuration of site fault domains.
   
   Attributes:
       siteFaultDomains: The set of site fault domains configured.
   """
   siteFaultDomains: list[SiteFaultDomain] = []


class StorageComplianceResult(pyVmomi.vmodl.DynamicData):
   """
   Describes the results of profile compliance checking for vSAN object.
   
   Attributes:
       checkTime: Time when the compliance was checked.
       profile: Requirement profile with which the compliance was checked.
       objectUUID: Requirement vSAN object with which the compliance was checked.
       complianceStatus: Status of the compliance operation.
       mismatch: True if there is a profile version mismatch between the Storage
           Profile Server and the storage provider.
           
           If you receive a result that
           indicates a mismatch, you must use the vSphere API to update the profile
           associated with the virtual machine or virtual disk.
       violatedPolicies: Values for capabilities that are known to be non-compliant with the specified constraints.
       operationalStatus: Additional information on the effects of backend resources and operations on the storage object.
       objPolicyGenerationId: The actual object policy generation ID indicating if the object policy is out of date
           against the SPBM policy
   """
   class StorageComplianceStatus(pyVmomi.VmomiSupport.Enum):
      """
      Defines the set of status values for compliance operations.
      
      Attributes:
          compliant: Entity is compliant.
          nonCompliant: Entity is not compliant.
          unknown: Compliance status of the entity is unknown.
          notApplicable: Compliance computation is not applicable for this entity, because it does not have any storage policy requirement for the datastore where the entity is placed.
      """
      compliant: _typing.ClassVar['StorageComplianceResult.StorageComplianceStatus'] = 'compliant'
      nonCompliant: _typing.ClassVar['StorageComplianceResult.StorageComplianceStatus'] = 'nonCompliant'
      unknown: _typing.ClassVar['StorageComplianceResult.StorageComplianceStatus'] = 'unknown'
      notApplicable: _typing.ClassVar['StorageComplianceResult.StorageComplianceStatus'] = 'notApplicable'

   checkTime: _typing.Optional[_datetime.datetime] = None
   profile: _typing.Optional[str] = None
   objectUUID: _typing.Optional[str] = None
   complianceStatus: str
   mismatch: bool
   violatedPolicies: list[StoragePolicyStatus] = []
   operationalStatus: _typing.Optional[StorageOperationalStatus] = None
   objPolicyGenerationId: _typing.Optional[str] = None


class StorageOperationalStatus(pyVmomi.vmodl.DynamicData):
   """
   Additional information on the effects of backend resources and
   operations on the storage object.
   
   Attributes:
       healthy: Whether the object is currently affected by the failure of
           backend storage resources.
       operationETA: Estimated completion time of a backend operation affecting the object.
           
           If set, then \"transitional\" will be true.
       operationProgress: Percent progress of a backend operation affecting the object.
           
           If set, then \"transitional\" will be true.
       transitional: Whether an object is undergoing a backend operation that may affect
           its performance.
           
           This may be a rebalancing the resources of a healthy
           object or recovery tasks for an unhealthy object.
   """
   healthy: _typing.Optional[bool] = None
   operationETA: _typing.Optional[_datetime.datetime] = None
   operationProgress: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   transitional: _typing.Optional[bool] = None


class StoragePolicyStatus(pyVmomi.vmodl.DynamicData):
   """
   Provides information when compliance checking produces non-compliant results.
   
   Attributes:
       id: The checked policy ID.
       expectedValue: The expected policy value.
       currentValue: The current policy value.
   """
   id: _typing.Optional[str] = None
   expectedValue: _typing.Optional[str] = None
   currentValue: _typing.Optional[str] = None


class SystemVMsConfigInfo(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: as of vSphere 9.0 with no replacement. In a future release
   of vSphere, the vCLS functionality will be disabled, vCLS
   system VMs will be deleted, and vCLS APIs will be removed.Configuration for System VMs deployment.
   
   Attributes:
       allowedDatastores: The only datastores which can be used for System VMs deployment.
       notAllowedDatastores: Datastores which cannot be used for System VMs deployment.
       dsTagCategoriesToExclude: Tag categories identifying datastores, which cannot be used for System VMs
           deployment.
       deploymentMode: The System VM deployment mode for vSphere clusters.
           
           Supported values are enumerated by the
           `pyVmomi.vim.cluster.SystemVMsConfigInfo.DeploymentMode`
           type.
           An unset value implies SYSTEM_MANAGED,
           unless the cluster is put in \"Retreat Mode\".
           
           Since: vSphere API Release 8.0.2.0
   
   Since: vSphere API Release 7.0.3.0
   """
   class DeploymentMode(pyVmomi.VmomiSupport.Enum):
      """
      Attributes:
          SYSTEM_MANAGED: System VMs are fully managed by the system.
          ABSENT: System VMs are absent on the managed entity.
      
      Since: vSphere API Release 8.0.2.0
      """
      SYSTEM_MANAGED: _typing.ClassVar['SystemVMsConfigInfo.DeploymentMode'] = 'SYSTEM_MANAGED'
      ABSENT: _typing.ClassVar['SystemVMsConfigInfo.DeploymentMode'] = 'ABSENT'

   allowedDatastores: list[pyVmomi.vim.Datastore] = []
   notAllowedDatastores: list[pyVmomi.vim.Datastore] = []
   dsTagCategoriesToExclude: list[str] = []
   deploymentMode: _typing.Optional[str] = None


class SystemVMsConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: as of vSphere 9.0 with no replacement. In a future release
   of vSphere, the vCLS functionality will be disabled, vCLS
   system VMs will be deleted, and vCLS APIs will be removed.Configuration for System VMs deployment.
   
   Attributes:
       allowedDatastores: The only datastores which can be used for System VMs deployment.
       notAllowedDatastores: Datastores which cannot be used for System VMs deployment.
       dsTagCategoriesToExclude: Tag categories identifying datastores, which cannot be used for System VMs
           deployment.
       deploymentMode: The System VM deployment mode for vSphere clusters.
           
           Supported values are enumerated by the
           `pyVmomi.vim.cluster.SystemVMsConfigInfo.DeploymentMode`
           type.
           Providing an unset value does not modify deploymentMode.
           
           Since: vSphere API Release 8.0.2.0
   
   Since: vSphere API Release 7.0.3.0
   """
   allowedDatastores: list[DatastoreUpdateSpec] = []
   notAllowedDatastores: list[DatastoreUpdateSpec] = []
   dsTagCategoriesToExclude: list[TagCategoryUpdateSpec] = []
   deploymentMode: _typing.Optional[str] = None


class TagCategoryUpdateSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """
   Deprecated: as of vSphere 9.0 with no replacement. In a future release
   of vSphere, the vCLS functionality will be disabled, vCLS
   system VMs will be deleted, and vCLS APIs will be removed.An incremental update to a TagCategory list.
   
   Since: vSphere API Release 7.0.3.0
   """
   category: _typing.Optional[str] = None


class UsageSummary(pyVmomi.vmodl.DynamicData):
   """
   This class contains cluster usage summary that is populated
   by DRS and used by Cloud Placement Engine in VCD.
   
   Attributes:
       totalCpuCapacityMhz: Total CPU capacity of the cluster.
       totalMemCapacityMB: Total memory capacity of the cluster.
       cpuReservationMhz: Sum of CPU reservation of all the Resource Pools and powered-on VMs in the cluster.
       memReservationMB: Sum of memory reservation of all the Resource Pools and powered-on VMs in the cluster.
       poweredOffCpuReservationMhz: Sum of CPU reservation of all the powered-off VMs in the cluster.
       poweredOffMemReservationMB: Sum of memory reservation of all the powered-off VMs in the cluster.
       cpuDemandMhz: Sum of CPU demand of all the powered-on VMs in the cluster.
       memDemandMB: Sum of memory demand of all the powered-on VMs in the cluster.
       statsGenNumber: Generation number of the usage stats.
           
           Updated during every DRS load
           balancing call.
       cpuEntitledMhz: This is the current CPU entitlement across the cluster
       memEntitledMB: This is the current memory entitlement across the cluster
       poweredOffVmCount: The number of powered off VMs in the cluster
       totalVmCount: The number of VMs in the cluster
       tier0MemCapacityMB: Total Tier 0 memory capacity in a cluster.
           
           Since: vSphere API Release 9.0.0.0
       reservedTier0MemMB: Total amount of Tier 0 memory used to satisfy virtual machine reservation.
           
           Since: vSphere API Release 9.0.0.0
       unreservedTier0MemMB: Total amount of Tier 0 memory available to satisfy reservation.
           
           Available
           reservation is calculated after accounting for DRS overheads and current
           reservation.
           
           Since: vSphere API Release 9.0.0.0
   """
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
   """
   Configuration of preferred Fault Domain of vSAN
   stretched cluster.
   
   A vSAN stretched cluster is configured into two sites,
   through vSAN Fault Domain configuration.
   Since virtual machines can run on any of the two sites, if
   network connectivity is lost between site A and site B, but
   both still have connectivity to the witness, the preferred
   site is the one that survives and its components remains active,
   while the storage on the non-preferred site is marked as down
   and components on that site are marked as absent.
   
   Attributes:
       preferredFaultDomainName: User friendly name of preferred Fault Domain
       preferredFaultDomainId: UUID of preferred Fault Domain
   """
   preferredFaultDomainName: _typing.Optional[str] = None
   preferredFaultDomainId: _typing.Optional[str] = None


class VSANStretchedClusterCapability(pyVmomi.vmodl.DynamicData):
   """
   Capability that whether a host can support vSAN stretched cluster
   
   Attributes:
       hostMoId: ManagedEntity Id of target host
       connStatus: Connection status to present whether this host is connected to
           vCenter server, valid values include: connected, notResponding
           and disconnected.
       isSupported: Whether ESXi software of target host can support vSAN
           stretched cluster.
           
           The vSAN stretched cluster feature
           is supported since vSphere vSAN 6.1.
       hostCapability: Detailed information of ESXi software to support vSAN
           stretched cluster, for now, it only contains the feature version
           information.
           
           For vSphere vSAN 6.1, the version is 1.0;
           and vSphere vSAN 6.2, the version is 2.0.
   """
   hostMoId: str
   connStatus: _typing.Optional[str] = None
   isSupported: _typing.Optional[bool] = None
   hostCapability: _typing.Optional[pyVmomi.vim.host.VSANStretchedClusterHostCapability] = None


class VSANStretchedClusterFaultDomainConfig(pyVmomi.vmodl.DynamicData):
   """
   vSAN Fault Domain configuration, to determine how to configure
   a vSAN stretched cluster into two sites.
   
   Hosts specified in site
   A and site B, are expected to cover all hosts reside in target vSAN
   cluster, and a host is not allowed to exist in both sites, otherwise
   InvalidArgument fault will be met during vSAN stretched cluster
   conversion.
   
   Attributes:
       firstFdName: User friendly Fault Domain name of site A.
           
           The length of name should not exceed 256 characters.
       firstFdHosts: vSAN data hosts to be put in site A.
           
           Hosts are expected
           to reside in vSAN cluster.
       secondFdName: User friendly Fault Domain name of site B.
           
           The length of name should not exceed 256 characters.
       secondFdHosts: vSAN data hosts to be put in site B.
           
           Hosts are expected
           to reside in vSAN cluster.
   """
   firstFdName: str
   firstFdHosts: list[pyVmomi.vim.HostSystem] = []
   secondFdName: str
   secondFdHosts: list[pyVmomi.vim.HostSystem] = []


class VSANStretchedClusterHostVirtualApplianceStatus(pyVmomi.vmodl.DynamicData):
   """
   The host virtual appliance status in vSAN.
   
   Attributes:
       vcCluster: Cluster compute resource of the vSAN cluster, which is a stretched
           cluster.
           
           This attribute is planning to be deprecated, please use vcClusters
           instead of this vcCluster.
       isVirtualApp: Host is a virtual appliance or not
       vcClusters: Cluster compute resources of the vSAN clusters that using this host virtual
           appliance as witness host, which is a list of stretched clusters.
       isVirtualAppValid: Witness appliance has been updated
   """
   vcCluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource] = None
   isVirtualApp: _typing.Optional[bool] = None
   vcClusters: list[pyVmomi.vim.ClusterComputeResource] = []
   isVirtualAppValid: _typing.Optional[bool] = None


class VSANWitnessHostInfo(pyVmomi.vmodl.DynamicData):
   """
   Configurations of witness host of vSAN stretched cluster
   
   Attributes:
       nodeUuid: vSAN UUID of witness host
       faultDomainName: User friendly name of Fault Domain, which witness host resides in
       preferredFdName: User friendly name of preferred Fault Domain configured in witness
           host.
       preferredFdUuid: UUID of preferred Fault Domain configured in witness host.
       unicastAgentAddr: IP address used by witness host, to communicate with data hosts
           in vSAN stretched cluster.
           
           The IP protocol supports IPv4 and IPv6, and which protocol to
           take, is determined by concrete vSAN network configurations
           on all hosts of vSAN stretched cluster. If both protocols
           are supported by all hosts, IPv4 will be taken. This IP address
           is from the first discovered virtual adapter of witness host, which
           enables vSAN traffic and supports taken IP protocol.
       host: ManagedEntity of witness host.
       metadataMode: True to indicate the host is a metadata host as opposed to witness host.
           
           Default to False if unset, meaning it is witness host.
           Metadata host is currently unsupported vSAN feature and it is not used
           for vSAN stretched cluster.
   """
   nodeUuid: str
   faultDomainName: _typing.Optional[str] = None
   preferredFdName: _typing.Optional[str] = None
   preferredFdUuid: _typing.Optional[str] = None
   unicastAgentAddr: _typing.Optional[str] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   metadataMode: _typing.Optional[bool] = None


class VmComponentProtectionSettings(pyVmomi.vmodl.DynamicData):
   """
   vSphere HA Virtual Machine Component Protection Service settings.
   
   vSphere HA Virtual Machine Component Protection Service detects
   and reacts to storage failures that do not necessarily cause a
   virtual machine to go down, but may impact the health or QoS of
   the virtual machine.
   
   All fields are defined as optional. In case of a reconfiguration, fields left unset
   are not changed.
   
   Attributes:
       vmStorageProtectionForAPD: VM storage protection setting for storage failures categorized as All Paths
           Down (APD).
           
           APD is a condition where a storage has become inaccessible
           for unknown reasons. It only indicates loss of connectivity and does not indicate
           storage device failure or LUN removal (Permanent Device Loss or PDL). The details
           of APD and PDL are described in `pyVmomi.vim.host.MountInfo.InaccessibleReason`.
           
           This property is meaningful only when vSphere HA is turned on. Valid values are
           specified by `pyVmomi.vim.cluster.VmComponentProtectionSettings.StorageVmReaction`. The default value is
           `disabled` for cluster setting and
           `clusterDefault` for per-VM setting.
           
           When an APD condition happens and the host begins timing out I/Os
           `AllPathsDown_Timeout`, VM Component
           Protection service will react based on the specific value of this property:
           - `disabled`, no reaction, i.e., no
             VM failover and no event reporting for the failures.
           - `warning`, service will issue events,
             alarms and/or config issues for component failures.
           - `restartConservative`, service will
             terminate the impacted VMs after a preconfigured time interval
             (`pyVmomi.vim.cluster.VmComponentProtectionSettings.vmTerminateDelayForAPDSec`) if they are to be restarted.
           - `restartAggressive`, service might
             terminate the impacted VMs after a preconfigured time interval
             (`pyVmomi.vim.cluster.VmComponentProtectionSettings.vmTerminateDelayForAPDSec`). In some cases, a VM is terminated
             even if it may not able to be restarted or lose Fault Tolerance redundancy.
           - `clusterDefault`, service will implement
             cluster default.
       enableAPDTimeoutForHosts: This property indicates if APD timeout will be enabled for all the hosts
           in the cluster when vSphere HA is configured.
           
           The details of APD timeout are
           described in `pyVmomi.vim.host.MountInfo.InaccessibleReason`.
           
           If `pyVmomi.vim.cluster.DasConfigInfo.vmComponentProtecting` is `disabled`,
           the property will be ignored. Otherwise, for each host in the cluster,
           APD timeout will be enabled. Note that no change will be made for a host if it
           already had APD timeout enabled.
           
           This property is meaningful only for cluster setting. It is ignored if specified at VM level.
           The default value is false if not specified.
           
           Note that this property is not persisted by vSphere backend. It does not impact any cluster
           reconfiguration or host operation (such as adding a host to a cluster) that might happen later.
       vmTerminateDelayForAPDSec: The time interval after an APD timeout has been declared and before VM Component
           Protection service will terminate the VM.
           
           The value only applies if
           `pyVmomi.vim.cluster.VmComponentProtectionSettings.vmStorageProtectionForAPD` is set to `restartConservative` or
           `restartAggressive`.
           
           The default value is 180 seconds if not specified. To use cluster setting for a VM override,
           set to -1 in per-VM setting.
       vmReactionOnAPDCleared: Action taken by VM Component Protection service for a powered on VM when APD
           condition clears after APD timeout.
           
           This property is meaningful only when vSphere HA is turned on. Valid values are
           specified by `pyVmomi.vim.cluster.VmComponentProtectionSettings.VmReactionOnAPDCleared`. The default value is
           `none` for cluster setting and
           `useClusterDefault` for per-VM setting.
       vmStorageProtectionForPDL: VM storage protection setting for storage failures categorized as Permanent Device
           Loss (PDL).
           
           PDL indicates storage device failure or LUN removal. In case of PDL,
           the failed datastore or device is unlikely to recover. The details of PDL are
           described in `pyVmomi.vim.host.MountInfo.InaccessibleReason`.
           
           This property is meaningful only when vSphere HA is turned on. Valid values are
           `disabled`, `warning`,
           `restartAggressive` and `clusterDefault`.
           The default value is `disabled` for cluster setting and
           `clusterDefault` for per-VM setting.
           
           When set to `restartAggressive`, VM Component Protection service
           will immediately terminate the VMs impacted by PDL and will attempt to restart the VMs
           with best effort. When set to the other values, the behavior is the same as described for
           `pyVmomi.vim.cluster.VmComponentProtectionSettings.vmStorageProtectionForAPD`.
   """
   class StorageVmReaction(pyVmomi.VmomiSupport.Enum):
      """
      The VM policy settings that determine the response to
      storage failures.
      
      Attributes:
          disabled: VM Component Protection service will not monitor or react to
              the component failure.
              
              This setting does not affect other vSphere
              HA services such as Host Monitoring or VM Health Monitoring.
          warning: VM Component Protection service will monitor component failures but
              will not restart an affected VM.
              
              Rather it will notify users about
              the component failures. This setting does not affect other vSphere HA
              services such as Host Monitoring or VM Health Monitoring.
          restartConservative: VM Component Protection service protects VMs conservatively.
              
              With this
              setting, when the service can't determine that capacity is available to
              restart a VM, it will favor keeping the VM running.
          restartAggressive: VM Component Protection service protects VMs aggressively.
              
              With this setting,
              the service will terminate an affected VM even if it can't determine that
              capacity exists to restart the VM.
          clusterDefault: VM will use the cluster default setting.
              
              This option is only meaningful for
              per-VM settings.
      """
      disabled: _typing.ClassVar['VmComponentProtectionSettings.StorageVmReaction'] = 'disabled'
      warning: _typing.ClassVar['VmComponentProtectionSettings.StorageVmReaction'] = 'warning'
      restartConservative: _typing.ClassVar['VmComponentProtectionSettings.StorageVmReaction'] = 'restartConservative'
      restartAggressive: _typing.ClassVar['VmComponentProtectionSettings.StorageVmReaction'] = 'restartAggressive'
      clusterDefault: _typing.ClassVar['VmComponentProtectionSettings.StorageVmReaction'] = 'clusterDefault'

   class VmReactionOnAPDCleared(pyVmomi.VmomiSupport.Enum):
      """
      If an APD condition clears after an APD timeout condition has been declared and before
      VM Component Protection service terminated the VM, the guestOS and application may
      no longer be operational.
      
      VM Component Protection may be configured to reset the
      VM (`pyVmomi.vim.VirtualMachine.reset`) to restore the service of guest applications.
      
      Attributes:
          none: VM Component Protection service will not react after APD condition is cleared.
          reset: VM Component Protection service will reset the VM after APD condition is cleared.
              
              Note this only applies if the subject VM is still powered on.
          useClusterDefault: VM will use the cluster default setting.
              
              This option is only meaningful for
              per-VM settings.
      """
      none: _typing.ClassVar['VmComponentProtectionSettings.VmReactionOnAPDCleared'] = 'none'
      reset: _typing.ClassVar['VmComponentProtectionSettings.VmReactionOnAPDCleared'] = 'reset'
      useClusterDefault: _typing.ClassVar['VmComponentProtectionSettings.VmReactionOnAPDCleared'] = 'useClusterDefault'

   vmStorageProtectionForAPD: _typing.Optional[str] = None
   enableAPDTimeoutForHosts: _typing.Optional[bool] = None
   vmTerminateDelayForAPDSec: _typing.Optional[int] = None
   vmReactionOnAPDCleared: _typing.Optional[str] = None
   vmStorageProtectionForPDL: _typing.Optional[str] = None


class VmGroup(GroupInfo):
   """
   The `pyVmomi.vim.cluster.VmGroup` data object identifies virtual machines
   for VM-Host rules.
   
   VM-Host rules determine placement of virtual machines
   on hosts in a cluster.
   The logic specified in a `pyVmomi.vim.cluster.VmHostRuleInfo` object
   determines where virtual machines can be powered-on.
   
   If a virtual machine is removed from the cluster, it loses its DRS group
   affiliation. The Server does not restore any group affiliations if the
   virtual machine is returned to the cluster.
   
   Attributes:
       vm: List of virtual machines that are part of this group.
           
           A virtual machine group can contain zero or more virtual machines.
   """
   vm: list[pyVmomi.vim.VirtualMachine] = []


class VmHostRuleInfo(RuleInfo):
   """
   A `pyVmomi.vim.cluster.VmHostRuleInfo` object identifies virtual machines
   and host groups that determine virtual machine placement.
   
   The virtual
   machines and hosts referenced by a VM-Host rule must be in the same cluster.
   
   A VM-Host rule identifies the following groups.
   - A virtual machine group (`pyVmomi.vim.cluster.VmGroup`).
   - Two host groups - an affine host group and an anti-affine host group
     (`pyVmomi.vim.cluster.HostGroup`).
     At least one of the groups must contain one or more hosts.
     
   `pyVmomi.vim.cluster.VmHostRuleInfo` stores only the names of the relevant
   virtual machine and host groups. The group contents are stored in
   the virtual machine and host group objects.
   
   When you modify a VM-Host rule, only the fields that are specified are set.
   
   Attributes:
       vmGroupName: Virtual group name (`pyVmomi.vim.cluster.VmGroup`.`pyVmomi.vim.cluster.GroupInfo.name`).
           
           The virtual group may contain one or more virtual machines.
       affineHostGroupName: Name of the affine host group
           (`pyVmomi.vim.cluster.HostGroup`.`pyVmomi.vim.cluster.GroupInfo.name`).
           
           The affine host group identifies hosts on which
           `pyVmomi.vim.cluster.VmHostRuleInfo.vmGroupName` virtual machines can be powered-on.
           The value of the `pyVmomi.vim.cluster.RuleInfo.mandatory` property
           determines how the Server interprets the rule.
       antiAffineHostGroupName: Name of the anti-affine host group
           (`pyVmomi.vim.cluster.HostGroup`.`pyVmomi.vim.cluster.GroupInfo.name`).
           
           The anti-affine host group identifies hosts on which
           `pyVmomi.vim.cluster.VmHostRuleInfo.vmGroupName` virtual machines should not
           be powered-on.
           The value of the `pyVmomi.vim.cluster.RuleInfo.mandatory` property
           determines how the Server interprets the rule.
   """
   vmGroupName: _typing.Optional[str] = None
   affineHostGroupName: _typing.Optional[str] = None
   antiAffineHostGroupName: _typing.Optional[str] = None


class VmOrchestrationInfo(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.cluster.VmOrchestrationInfo` data object contains the orchestration
   configuration for a single virtual machine.
   
   This makes it possible to
   override the default behavior for an individual virtual machine.
   
   Attributes:
       vm: Reference to the VM that the ready state is applied to.
       vmReadiness: Readiness policy that apply to this virtual machine.
           
           Values specified in this object override the cluster-wide
           defaults for virtual machines.
           `pyVmomi.vim.cluster.OrchestrationInfo.defaultVmReadiness`
   """
   vm: pyVmomi.vim.VirtualMachine
   vmReadiness: VmReadiness


class VmOrchestrationSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   """An incremental update to the per-VM orchestration config."""
   info: _typing.Optional[VmOrchestrationInfo] = None


class VmReadiness(pyVmomi.vmodl.DynamicData):
   """
   VM readiness policy specifies when a VM is deemed ready.
   
   This is used in cluster VM orchestration settings. For example, vSphere HA
   restarts lower priority VMs only after higher priority VMs are ready.
   
   Attributes:
       readyCondition: Ready condition for a virtual machine.
           
           See `pyVmomi.vim.cluster.VmReadiness.ReadyCondition`.
           
           If not specified at either the cluster level or the virtual machine
           level, this will default to `none`.
       postReadyDelay: Additional delay in seconds after ready condition is met.
           
           A VM is
           considered ready at this point.
           
           If not specified in a VM override, cluster default setting is
           used. Alternatively, set to -1 in per-VM setting to use cluster default
           value.
   """
   class ReadyCondition(pyVmomi.VmomiSupport.Enum):
      """
      Condition for VM's readiness
      
      Attributes:
          none: No ready condition specified.
              
              In case of vSphere HA, higher restart priority VMs are still
              placed before lower priority VMs.
          poweredOn: VM is powered on.
          guestHbStatusGreen: VM guest operating system is up and responding normally (VM tools
              heartbeat status is green).
          appHbStatusGreen: An application running inside the VM is responding normally.
              
              To enable Application Monitoring, you must first obtain the
              appropriate SDK (or be using an application that supports VMware
              Application Monitoring) and use it to set up customized heartbeats
              for the applications you want to monitor.
              See `pyVmomi.vim.cluster.DasConfigInfo.vmMonitoring`.
          useClusterDefault: VM will use the cluster default setting.
              
              This option is only
              meaningful for per-VM settings.
      """
      none: _typing.ClassVar['VmReadiness.ReadyCondition'] = 'none'
      poweredOn: _typing.ClassVar['VmReadiness.ReadyCondition'] = 'poweredOn'
      guestHbStatusGreen: _typing.ClassVar['VmReadiness.ReadyCondition'] = 'guestHbStatusGreen'
      appHbStatusGreen: _typing.ClassVar['VmReadiness.ReadyCondition'] = 'appHbStatusGreen'
      useClusterDefault: _typing.ClassVar['VmReadiness.ReadyCondition'] = 'useClusterDefault'

   readyCondition: _typing.Optional[str] = None
   postReadyDelay: _typing.Optional[int] = None


class VmToolsMonitoringSettings(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.cluster.VmToolsMonitoringSettings` data object contains
   virtual machine monitoring settings that are used by the Virtual Machine Health Monitoring Service.
   
   The Service checks the VMware Tools heartbeat of a virtual machine.
   If heartbeats have not been received within a specified time interval, the Service
   declares the virtual machine as failed and resets the virtual machine.
   
   These settings are applied to individual virtual machines during cluster reconfiguration
   (`pyVmomi.vim.cluster.DasVmConfigInfo`.`pyVmomi.vim.cluster.DasVmConfigInfo.dasSettings`.`pyVmomi.vim.cluster.DasVmSettings.vmToolsMonitoringSettings`). You can also specify them as default values
   (`pyVmomi.vim.cluster.DasConfigInfo`.`pyVmomi.vim.cluster.DasConfigInfo.defaultVmSettings`).
   
   All fields are optional. In case of a reconfiguration, fields left unset are not changed.
   
   Attributes:
       enabled: Flag indicating whether or not the Virtual Machine Health Monitoring
           service is enabled.
           
           The Server does not use this property.
       vmMonitoring: Indicates the type of virtual machine monitoring.
           
           Specify a string value corresponding to one of the
           following `pyVmomi.vim.cluster.DasConfigInfo.VmMonitoringState` values:
           - `vmMonitoringDisabled` (the default value)
           - `vmMonitoringOnly`
           - `vmAndAppMonitoring`
             
           The individual VMware Tools setting for virtual machine monitoring depends on
           the HA Virtual Machine Health Monitoring Service level that is
           defined for the cluster
           (`pyVmomi.vim.cluster.DasConfigInfo`.`pyVmomi.vim.cluster.DasConfigInfo.vmMonitoring`).
           The following list indicates the supported VMware Tools `vmMonitoring` values
           according to the cluster configuration.
           - If the cluster configuration specifies `vmMonitoringDisabled`,
             the Service is disabled and the HA Service ignores the VMware Tools monitoring setting.
           - If the cluster configuration specifies `vmMonitoringOnly`,
             the Service supports `vmMonitoringOnly` or `vmMonitoringDisabled` only.
           - If the cluster configuration specifies `vmAndAppMonitoring`,
             you can use any of the `pyVmomi.vim.cluster.DasConfigInfo.VmMonitoringState` values.
             
           The `pyVmomi.vim.cluster.VmToolsMonitoringSettings.clusterSettings` value has no
           effect on the constraint imposed by the HA Virtual Machine Health Monitoring Service
           level that is defined for the cluster
           (`pyVmomi.vim.cluster.DasConfigInfo`.`pyVmomi.vim.cluster.DasConfigInfo.vmMonitoring`).
           
           Application monitoring events are generated regardless of the
           currently configured type of virtual machine monitoring.
           You can use these events even if monitoring is being disabled
           or set to `vmMonitoringOnly`.
       clusterSettings: Flag indicating whether to use the cluster settings or the per VM settings.
           
           The default value is true.
       failureInterval: If no heartbeat has been received for at least the specified number of seconds,
           the virtual machine is declared as failed.
           
           The default value is 30.
       minUpTime: The number of seconds for the virtual machine's heartbeats to stabilize
           after the virtual machine has been powered on.
           
           This time should include
           the guest operating system boot-up time. The virtual machine monitoring
           will begin only after this period.
           
           The default value is 120.
       maxFailures: Maximum number of failures and automated resets allowed during the time that
           `pyVmomi.vim.cluster.VmToolsMonitoringSettings.maxFailureWindow` specifies.
           
           If `pyVmomi.vim.cluster.VmToolsMonitoringSettings.maxFailureWindow` is -1
           (no window), this represents the absolute number of failures after which
           automated response is stopped.
           
           If a virtual machine exceeds this threshold, in-depth problem analysis is
           usually needed.
           
           The default value is 3.
       maxFailureWindow: The number of seconds for the window during which up to `pyVmomi.vim.cluster.VmToolsMonitoringSettings.maxFailures`
           resets can occur before automated responses stop.
           
           If set to -1, no failure window is specified.
           
           The default value is -1.
   """
   enabled: _typing.Optional[bool] = None
   vmMonitoring: _typing.Optional[str] = None
   clusterSettings: _typing.Optional[bool] = None
   failureInterval: _typing.Optional[int] = None
   minUpTime: _typing.Optional[int] = None
   maxFailures: _typing.Optional[int] = None
   maxFailureWindow: _typing.Optional[int] = None


class VsanAttachToSrOperation(pyVmomi.vmodl.DynamicData):
   """
   Class for the historical operation of attaching to Support Request (SR)
   
   Attributes:
       task: The task associates with this test result
       success: Indicate the attach to SR operation is successful or not
           The success value will be empty when the operation is not completed
           when the task is running
       timestamp: The time for attaching to SR operation
           The timestamp will be empty when the operation is not completed
           when the task is running
       srNumber: The SR number
   """
   task: _typing.Optional[pyVmomi.vim.Task] = None
   success: _typing.Optional[bool] = None
   timestamp: _typing.Optional[_datetime.datetime] = None
   srNumber: str

class VsanBaselinePreferenceType:
   """
   Represents various baseline preference types.
   
   Any patch or update release is considered part of the same \"release family\",
   while both updates to the major version number (e.g. 7.0) or to the minor
   version number (e.g. 7.1) would be considered different \"release families\".
   """
   pass


class VsanCapability(pyVmomi.vmodl.DynamicData):
   """
   Holds the information about the capabilities a concrete ManagedObject has.
   
   Attributes:
       target: The managed object that owns the capabilities.
           
           It is an optional field that
           could be HostSystem, ClusterComputeResource or nothing. If it is empty, this
           means that the attached capabilities rely to the vCenter itself.
       capabilities: A list of capabilities that the target object supports.
           
           All valid
           capabilities are listed in below enumerations:
           `pyVmomi.vim.cluster.VsanCapabilityType`,
           `pyVmomi.vim.cluster.VsanCapabilityType90`
           `pyVmomi.vim.cluster.VsanCapabilityType91`
       statuses: A list of statuses that indicate target object's status when retrieving
           capabilities.
           
           For example, if capabilities retrieved from a host is empty,
           this field can be used to clarify the specific reasons.
   """
   target: _typing.Optional[pyVmomi.VmomiSupport.ManagedObject] = None
   capabilities: list[str] = []
   statuses: list[str] = []

class VsanCapabilityStatus:
   """
   Represents a condition that an object is in when retrieving capability on
   it.
   
   A host can be in multiple conditions at the same time. Currently we
   have the following ones.
   """
   pass


class VsanCapabilitySystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   The VsanCapabilitySystem exposes interfaces to retrieve the supported
   capabilities on the current system.
   
   The Managed Entity can be accessed
   through MOID of vsan-vc-capability-system at vCenter server side or
   vsan-capability-system at ESXi server side.
   """
   def GetCapabilities(self, targets: list[pyVmomi.VmomiSupport.ManagedObject]) -> list[VsanCapability]:
      """
      Retrieves the supported capabilities on the current system.
      
      The calculation
      is based on the available APIs and registered managed objects. This way the
      client can be sure if a certain feature is supported on the system or not.
      For scenarios like disconnected hosts, older version hosts than ESXi 6.0 U1,
      or unable to retrieve capabilities due to other reasons, along with empty
      capability set, status of target managed object at the retrieving time is
      also returned to explain the reason. For a host whose capabilities are
      calculated according to host version, a 'calculated' capability status is
      returned. For other cases, the statuses field in
      `pyVmomi.vim.cluster.VsanCapability`
      is omitted.
      
      Args:
          targets: An optional list of targeted managed objects. The supported
              targets are HostSystem and ClusterComputeResource instances. If a HostSystem
              is given, the result contains information about the capabilities of this
              certain host. If a cluster is passed, the result contains information about
              the capabilities of all hosts that reside in the cluster and the capabilities
              of the vCenter. If the targets parameter is empty, the result contains only
              the capabilities of the current vCenter.
      
      Returns:
          A list of vim.cluster.VsanCapability.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...

class VsanCapabilityType:
   """Represents a feature capability (for 8.x and previous releases)."""
   pass

class VsanCapabilityType90:
   """Represents a feature capability for 9.0 release."""
   pass

class VsanCapabilityType91:
   """Represents a feature capability for 90u1 release."""
   pass


class VsanClientServerHciMeshDitEncryptionHealthSummary(pyVmomi.vmodl.DynamicData):
   """
   This class defines the HCI Mesh data-in-transit encryption health summary for a cluster.
   
   It includes the HCI Mesh data-in-transit encryption health summary between this cluster and
   any peer client clusters that mount this cluster if this cluster acts as a server cluster, or
   any peer server clusters that this cluster mounts if this cluster acts as a client cluster.
   
   Attributes:
       clusterUuid: The peer client or server cluster UUID.
       clusterName: The peer client or server cluster name.
       ownerVc: The vCenter that owns the peer client or server cluster.
       isLocalOwnerVc: If the owner vCenter is local.
       health: The health status.
       issues: The health issues.
   """
   clusterUuid: str
   clusterName: str
   ownerVc: _typing.Optional[str] = None
   isLocalOwnerVc: _typing.Optional[bool] = None
   health: str
   issues: list[str] = []


class VsanClusterAdvCfgSyncHostResult(pyVmomi.vmodl.DynamicData):
   """
   Value of a config option on a given host
   
   Attributes:
       hostname: Name of the host
       value: Value of the config option
       isDefault: Is default value or not.
   """
   hostname: str
   value: str
   isDefault: _typing.Optional[bool] = None


class VsanClusterAdvCfgSyncResult(pyVmomi.vmodl.DynamicData):
   """
   Result of a advanced config sync check across the cluster.
   
   Captures both the high
   level result as well as per host results.
   
   Attributes:
       inSync: True if all hosts use the same value
       name: Name of the advanced config option
       hostValues: Values across the hosts
   """
   inSync: bool
   name: str
   hostValues: list[VsanClusterAdvCfgSyncHostResult] = []


class VsanClusterBalancePerDiskInfo(pyVmomi.vmodl.DynamicData):
   """
   Information about the disk utilization balance as it related to a single capacity
   disk.
   
   Attributes:
       uuid: The UUID of the vSAN disk.
       fullness: Usage level in percent.
       variance: Usage percentage points above the lowest fullness.
           
           If lowest fullness is 10, and
           this disk has 80, then the variance will be 80 - 10 = 70.
       fullnessAboveThreshold: Usage percentage points above the acceptable fullness.
           
           Acceptable fullness is a
           margin of percentage points above the lowest fullness.
       dataToMoveB: Amount of data to move to restore balance.
       compFullness: Component usage level in percent.
           
           Since: 8.0.0.4
       compVariance: Usage percentage points above the lowest component fullness.
           
           If lowest component fullness is 10, and this disk has 80,
           then the variance will be 80 - 10 = 70.
           
           Since: 8.0.0.4
   """
   uuid: _typing.Optional[str] = None
   fullness: pyVmomi.VmomiSupport.long
   variance: pyVmomi.VmomiSupport.long
   fullnessAboveThreshold: pyVmomi.VmomiSupport.long
   dataToMoveB: pyVmomi.VmomiSupport.long
   compFullness: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   compVariance: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanClusterBalanceSummary(pyVmomi.vmodl.DynamicData):
   """
   Information about the disk utilization balance across the cluster.
   
   Only healthy disks
   are considered in this summary/analysis.
   
   Attributes:
       varianceThreshold: Percentage points that are allowed above the lowest fullness of any disk.
           
           Any disk with
           a variance higher than this threshold is considered too loaded from a balance
           perspective.
       disks: List of all healthy capacity disks in the cluster with their detailed balance
           evaluation.
   """
   varianceThreshold: pyVmomi.VmomiSupport.long
   disks: list[VsanClusterBalancePerDiskInfo] = []


class VsanClusterClomdLivenessResult(pyVmomi.vmodl.DynamicData):
   """
   Result of checking CLOMD liveness on vSAN cluster wide.
   
   It contains result of
   checking CLOMD liveness on each of the vSAN host.
   
   Attributes:
       clomdLivenessResult: Results of checking CLOMD liveness on all the vSAN hosts
       issueFound: True if any problem occurred in checking CLOMD liveness on any vSAN host
   """
   clomdLivenessResult: list[VsanHostClomdLivenessResult] = []
   issueFound: bool


class VsanClusterConfig(pyVmomi.vmodl.DynamicData):
   """
   Configuration of a standalone vSAN cluster.
   
   Not applicable if
   cluster integration is working with vpxd.
   
   Attributes:
       config: The vSAN configuration of the cluster, to present
           vSAN's enablement, cluster UUID, and auto-claim setting.
       name: A user friendly name for the cluster.
           
           Must be unique.
       hosts: Host BIOS UUIDs of hosts that are configured by user to be part
           of this cluster.
       toBeDeleted: Indicates whether this cluster is being deleted.
           
           If toBeDeleted is set True,
           then no Host will be added to this cluster.
           Default: False.
   """
   config: pyVmomi.vim.vsan.cluster.ConfigInfo
   name: str
   hosts: list[str] = []
   toBeDeleted: _typing.Optional[bool] = None


class VsanClusterCreateVmHealthTestResult(pyVmomi.vmodl.DynamicData):
   """
   This class encapsulates the result of VM creation test for vSAN cluster
   
   Attributes:
       clusterResult: The overall vSAN cluster result for VM creation test
       hostResults: The VM creation test result for each of host
   """
   clusterResult: VsanClusterProactiveTestResult
   hostResults: list[VsanHostCreateVmHealthTestResult] = []


class VsanClusterDitEncryptionHealthSummary(pyVmomi.vmodl.DynamicData):
   """
   This class defines data-in-transit encryption health summary
   in cluster level.
   
   The health summary is aggregated from each health check
   result from all hosts across the cluster.
   
   Attributes:
       overallHealth: Data-in-transit encryption configuration consistency
           health across all hosts in the cluster.
       enabled: Whether data-in-transit encryption is enabled in the cluster.
       hostResults: Data-in-transit encryption health results on all of vSAN hosts in
           the cluster.
   """
   overallHealth: str
   enabled: _typing.Optional[bool] = None
   hostResults: list[pyVmomi.vim.host.VsanDitEncryptionHealthSummary] = []


class VsanClusterEncryptionHealthSummary(pyVmomi.vmodl.DynamicData):
   """
   This class defines encryption health summary in cluster level.
   
   The encryption health summary is aggregated from each health
   check result from all hosts across the cluster and checked
   configuration consistency against cluster configuration on
   vCenter side.
   
   Attributes:
       overallHealth: Overall health state for encryption configuration and
           Key Management Server connection on vCenter and across all hosts in
           the cluster.
       configHealth: Encryption configuration consistency health across all
           hosts in the cluster.
       kmsHealth: Key Management Server connection health on vCenter and across all hosts
           in the cluster.
       vcKmsResult: Key Management Servers connection health result on vCenter side.
       hostResults: Encryption health results on all of vSAN hosts in
           the cluster.
       aesniHealth: AES-NI configuration consistency health across all
           hosts in the cluster.
           
           Valid value can be ['green'
           , 'yellow', 'red', 'unknown']
   """
   overallHealth: _typing.Optional[str] = None
   configHealth: _typing.Optional[str] = None
   kmsHealth: _typing.Optional[str] = None
   vcKmsResult: _typing.Optional[VsanVcKmipServersHealth] = None
   hostResults: list[pyVmomi.vim.host.VsanEncryptionHealthSummary] = []
   aesniHealth: _typing.Optional[str] = None


class VsanClusterFileServiceHealthSummary(pyVmomi.vmodl.DynamicData):
   """
   This class defines file service health summary in cluster level.
   
   The file
   service health summary is aggregated from the file service health check
   result from the hosts in the cluster.
   
   Attributes:
       overallHealth: Overall health state for vSAN file service configuration and runtime
           status, through the aggregation from vCenter and the hosts in the cluster.
       hostResults: The vSAN file service health status from all the hosts in this cluster.
   """
   overallHealth: _typing.Optional[str] = None
   hostResults: list[pyVmomi.vim.host.VsanFileServiceHealthSummary] = []


class VsanClusterGlobalDedupHealthSummary(pyVmomi.vmodl.DynamicData):
   """
   This class defines the global dedup health summary in cluster level.
   
   The global dedup health summary is aggregated from each host across
   the cluster, and it includes 2 parts: host global dedup config health
   and global dedup store health.
   
   Attributes:
       dedupConfigHealth: The global dedup config health for all hosts.
       dedupStoreHealth: The global dedup store health that is the value of enum type vim.host.
           
           VsanObjectHealthState. The values are as below.
           
           health
            - Condition
           
           'inaccessible' 
            - If the most serious store object health is 'inaccessible' 
           
           'reducedavailabilitywithactiverebuild' 
            - If the most serious store object health is 'reducedavailabilitywithactiverebuild' 
           
           'reducedavailabilitywithnorebuilddelaytimer' 
            - If the most serious store object health is 'reducedavailabilitywithnorebuilddelaytimer' 
           
           'reducedavailabilitywithpolicypending' 
            - If the most serious store object health is 'reducedavailabilitywithpolicypending' 
           
           'reducedavailabilitywithpolicypendingfailed' 
            - If the most serious store object health is 'reducedavailabilitywithpolicypendingfailed' 
           
           'reducedavailabilitywithpausedrebuild' 
            - If the most serious store object health is 'reducedavailabilitywithpausedrebuild' 
           
           'reducedavailabilitywithnorebuild' 
            - If the most serious store object health is 'reducedavailabilitywithnorebuild' 
           
           'nonavailabilityrelatedreconfig' 
            - If the most serious store object health is 'nonavailabilityrelatedreconfig' 
           
           'nonavailabilityrelatedincompliancewithpolicypending' 
            - If the most serious store object health is 'nonavailabilityrelatedincompliancewithpolicypending' 
           
           'nonavailabilityrelatedincompliancewithpolicypendingfailed' 
            - If the most serious store object health is 'nonavailabilityrelatedincompliancewithpolicypendingfailed' 
           
           'nonavailabilityrelatedincompliancewithpausedrebuild' 
            - If the most serious store object health is 'nonavailabilityrelatedincompliancewithpausedrebuild' 
           
           'nonavailabilityrelatedincompliance' 
            - If the most serious store object health is 'nonavailabilityrelatedincompliance' 
           
           'datamove' 
            - If the most serious store object health is 'datamove' 
           
           'remoteAccessible' 
            - If the most serious store object health is 'remoteAccessible' 
           
           'healthy' 
            - If the most serious store object health is 'healthy'
   """
   dedupConfigHealth: list[pyVmomi.vim.host.VsanHostGlobalDedupConfigHealthSummary] = []
   dedupStoreHealth: _typing.Optional[str] = None


class VsanClusterHciMeshDitEncryptionHealthSummary(pyVmomi.vmodl.DynamicData):
   """
   This class defines the HCI Mesh data-in-transit encryption health summary for a cluster.
   
   Attributes:
       overallHealth: The overall HCI Mesh data-in-transit encryption health state.
       hostClientClusterSummary: The list of this cluster's all hosts' HCI Mesh data-in-transit encryption health summary for all the peer client clusters that mount this cluster.
       hostServerClusterSummary: The list of this cluster's all hosts' HCI Mesh data-in-transit encryption health summary for all the peer server clusters that this cluster mount.
       serverClusterSummary: The list of HCI Mesh data-in-transit encryption health summary between this cluster and all the peer server clusters that this cluster mounts.
   """
   overallHealth: str
   hostClientClusterSummary: list[pyVmomi.vim.host.VsanHostHciMeshDitEncryptionHealthSummary] = []
   hostServerClusterSummary: list[pyVmomi.vim.host.VsanHostHciMeshDitEncryptionHealthSummary] = []
   serverClusterSummary: list[VsanClientServerHciMeshDitEncryptionHealthSummary] = []


class VsanClusterHclInfo(pyVmomi.vmodl.DynamicData):
   """
   The vSAN cluster HCL information.
   
   Attributes:
       hclDbLastUpdate: The time (UTC time) from when the currently used HCL DB was known to be
           the latest up-to-date version.
       hclDbAgeHealth: The age health of the HCL DB.
           
           If older than 90 days, state is yellow. If older
           than 180 days, it is red. If no age known, state is \"unknown\".
       hostResults: HCL status of each host.
       updateItems: List of things (firmwares, drivers, VIBs, etc.) recommended to be installed
           on the cluster.
           
           Each item in the list applies to a specific host, as not
           all hosts are assumed to be at the same level. This field is only populated
           if explicitly requested.
       hclDbAbsent: True indicates the vSAN HCL DB is absent so that the HCL validation is not
           able to be performed.
           
           To resolve the issue, please check vSAN Health
           UI.
   """
   hclDbLastUpdate: _typing.Optional[_datetime.datetime] = None
   hclDbAgeHealth: _typing.Optional[str] = None
   hostResults: list[pyVmomi.vim.host.VsanHostHclInfo] = []
   updateItems: list[pyVmomi.vim.vsan.VsanUpdateItem] = []
   hclDbAbsent: _typing.Optional[bool] = None


class VsanClusterHealthAction(pyVmomi.vmodl.DynamicData):
   """
   vSAN Cluster health action defines the action needed by vSphere/storage
   admin to fix the potential vSAN health problem detecting by the vSAN
   health service.
   
   Attributes:
       actionId: The unique action ID
       actionLabel: The action label showing in UI
       actionDescription: The action description
       enabled: True indicates the action will be enabled and vSphere/storage admin can
           perform the remediation operation to resolve the health issue, but it's not
           always appropriate to trigger such operation and user need to use judgment
           of the situation to decide.
       parameters: The action parameters which can be used as the parameters for this action API when calling from UI.
   """
   class VsanClusterHealthActionIdEnum(pyVmomi.VmomiSupport.Enum):
      """
      The vSAN cluster health action ID enumeration.
      
      Actions are remediation operations user can take to resolve health issues.
      Each action is identified by ID. The user performs the action by calling the
      associated first-class API. But it's not always appropriate to trigger such
      operation and user need to use judgment of the situation to decide. This is
      why the action is not automatically executed, as it may be the wrong choice
      in some situations.
      Some actions don't directly correspond to an API, but rather a workflow, in
      the case of the UI a wizard.
      
      Attributes:
          RepairClusterObjectsAction: Mapped to `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.repairClusterObjectsImmediate` API.
          UploadHclDb: Mapped to `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.uploadHclDb` API.
          UpdateHclDbFromInternet: Mapped to `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.updateHclDbFromWeb` API.
          EnableHealthService: Deprecated.
          DiskBalance: Mapped to `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.rebalanceCluster` API.
          StopDiskBalance: Mapped to `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.stopRebalanceCluster` API.
          RemediateDedup: Mapped to `pyVmomi.vim.VsanUpgradeSystemEx.performUpgrade` API.
          UpgradeVsanDiskFormat: Mapped to `pyVmomi.vim.VsanUpgradeSystemEx.performUpgrade` API.
          CreateDVS: Mapped to UI workflow \"Create VDS\".
          ConfigureHA: Mapped to UI workflow \"Configure HA\".
          ConfigureDRS: Mapped to UI workflow \"Configure DRS\".
          ConfigureVSAN: Mapped to UI workflow \"Configure vSAN\".
          ClaimVSANDisks: Mapped to UI workflow \"Claim vSAN Disks\".
          ClusterUpgrade: Mapped to UI workflow \"vSAN On-click Upgrade Wizard\".
          CreateVMKnic: Mapped to UI workflow \"Create vmknic Wizard\".
          CreateVMKnicWithVMotion: Mapped to UI workflow \"Create vmknic with vMotion Wizard\".
          RunBurnInTest: Mapped to UI workflow \"Run Storage performance test\".
          EnableIscsiTargetService: Mapped to UI workflow \"Enable vSAN iSCSI service\".
          EnablePerformanceServiceAction: Mapped to `pyVmomi.vim.cluster.VsanPerformanceManager.createStatsObjectTask` API.
          RemediateClusterConfig: Mapped to UI workflow \"Remediate inconsistent configuration\".
          EnableCeip: Mapped to UI workflow \"Customer Experience Improvement Program (CEIP) page\".
          LoginVumIsoDepot: Mapped to `pyVmomi.vim.cluster.VsanVumSystem.fetchIsoDepotCookie` API.
          PurgeInaccessSwapObjs: Mapped to UI workflow \"Purge Inaccessible VM Swap Objects\".
          UploadReleaseCatalog: Mapped to UI workflow \"Update release catalog from file\".
      """
      RepairClusterObjectsAction: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'RepairClusterObjectsAction'
      UploadHclDb: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'UploadHclDb'
      UpdateHclDbFromInternet: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'UpdateHclDbFromInternet'
      EnableHealthService: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'EnableHealthService'
      DiskBalance: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'DiskBalance'
      StopDiskBalance: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'StopDiskBalance'
      RemediateDedup: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'RemediateDedup'
      UpgradeVsanDiskFormat: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'UpgradeVsanDiskFormat'
      CreateDVS: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'CreateDVS'
      ConfigureHA: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'ConfigureHA'
      ConfigureDRS: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'ConfigureDRS'
      ConfigureVSAN: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'ConfigureVSAN'
      ClaimVSANDisks: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'ClaimVSANDisks'
      ClusterUpgrade: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'ClusterUpgrade'
      CreateVMKnic: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'CreateVMKnic'
      CreateVMKnicWithVMotion: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'CreateVMKnicWithVMotion'
      RunBurnInTest: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'RunBurnInTest'
      EnableIscsiTargetService: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'EnableIscsiTargetService'
      EnablePerformanceServiceAction: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'EnablePerformanceServiceAction'
      RemediateClusterConfig: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'RemediateClusterConfig'
      EnableCeip: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'EnableCeip'
      LoginVumIsoDepot: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'LoginVumIsoDepot'
      PurgeInaccessSwapObjs: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'PurgeInaccessSwapObjs'
      UploadReleaseCatalog: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'UploadReleaseCatalog'
      ConfigureAutomaticRebalance: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'ConfigureAutomaticRebalance'
      RemediateFileService: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'RemediateFileService'
      RelayoutVsanObjects: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'RelayoutVsanObjects'
      RemediateFileServiceImbalance: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'RemediateFileServiceImbalance'
      SelectNvme: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'SelectNvme'
      CreateFileServiceDomain: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'CreateFileServiceDomain'
      RemediateIscsiLunsRuntimeStatus: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'RemediateIscsiLunsRuntimeStatus'
      ShallowRekey: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'ShallowRekey'
      VsanClusterHealthActionIdEnum_Unknown: _typing.ClassVar['VsanClusterHealthAction.VsanClusterHealthActionIdEnum'] = 'VsanClusterHealthActionIdEnum_Unknown'

   actionId: str
   actionLabel: pyVmomi.vmodl.LocalizableMessage
   actionDescription: pyVmomi.vmodl.LocalizableMessage
   enabled: bool
   parameters: list[pyVmomi.vim.KeyValue] = []

class VsanClusterHealthCategoryEnum:
   """
   The vSAN cluster health category enumeration.
   
   Each of non-green health check belongs to a specific category
   according to its actual user impact. The health score can be
   calculated based on it.
   """
   pass


class VsanClusterHealthCheckInfo(pyVmomi.vmodl.DynamicData):
   """
   Generic class for health check info, including testId, testName, groupId and groupName
   
   Attributes:
       testId: The id of health check
       testName: The name of health check
       groupId: The id of health group which the check belongs to
       groupName: The name of health check group which the check belongs to
   """
   testId: str
   testName: _typing.Optional[str] = None
   groupId: str
   groupName: _typing.Optional[str] = None


class VsanClusterHealthConfigs(pyVmomi.vmodl.DynamicData):
   """
   Attributes:
       enableVsanTelemetry: Enable flag to vSAN telemetry collection.
           
           The flag doesn't take effect any more and the value will be ignored
       vsanTelemetryInterval: The periodical vSAN telemetry collection interval in minutes.
           
           The smaller value will collect vSAN telemetry more frequently
           but increase the system overhead and vice versa.
           The default is one week.
       vsanTelemetryProxy: The proxy used for sending vSAN telemetry.
           
           The proxy can be
           either user configured or auto-discovered and will be applied for
           collecting all of vSAN telemetry data
       configs: Any other vSAN cluster health configurations.
           
           Each of configuration
           is the key/value pair. Currently, no additional configuration will be supported
   """
   enableVsanTelemetry: _typing.Optional[bool] = None
   vsanTelemetryInterval: _typing.Optional[int] = None
   vsanTelemetryProxy: _typing.Optional[VsanClusterTelemetryProxyConfig] = None
   configs: list[VsanClusterHealthResultKeyValuePair] = []


class VsanClusterHealthLinkBase(pyVmomi.vmodl.DynamicData):
   """
   Defines a link in the context of a ResultTable cell, which
   will be consumed by vSAN UI for UI navigation
   
   Attributes:
       label: The label string showing on top of the link.
   """
   label: _typing.Optional[str] = None


class VsanClusterHealthExternalLink(VsanClusterHealthLinkBase):
   """
   Defines a link in the context of a ResultTable cell.
   
   Attributes:
       url: The address to navigate to.
       category: The category for the link content like known issue KB, document etc.
   """
   url: str
   category: _typing.Optional[str] = None


class VsanClusterHealthGroup(pyVmomi.vmodl.DynamicData):
   """
   This class defines vSAN cluster health group result.
   
   The vSAN health check
   results with the same category will be grouped into a group result, which include the group
   name and ID, group health which is aggregated from each of health check item and the health
   check details
   
   Attributes:
       groupId: The health check group ID.
           
           It's the identifier for a group of the vSAN health check
           result and will keep stable for future releases
       groupName: The health check group name.
           
           It will be used as UI label to show the name of the grouped health
           check result
       groupHealth: The group health status aggregating from each of health check item.
           
           All of possible health
           status ordering in severity level are \"red, yellow, info, unknown, green\". The aggregated
           group health status will be the most severe status in each of sub health check item
       groupTests: The health check results for each of check item in the group
       inProgress: True indicates health check of this group is still in progress.
           
           It could return True for some health check groups if you are
           trying to get health summary via API
           `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.queryClusterHealthSummary`.
           The health check result under this group will not be available until the flag is false.
   """
   groupId: str
   groupName: str
   groupHealth: str
   groupTests: list[VsanClusterHealthTest] = []
   groupDetails: list[VsanClusterHealthResultBase] = []
   inProgress: _typing.Optional[bool] = None


class VsanClusterHealthQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   Attributes:
       task: Task ID returned from API
           `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.queryClusterHealthSummaryTask`.
           
           This is used to get the health summary performed by the given task.
           If the task is still running, `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.queryClusterHealthSummary`
           returns health check groups which are already completed.
           If the task is completed, `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.queryClusterHealthSummary`
           returns full health summary from cache (Notes: fetchFromCache should be True).
           `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.queryClusterHealthSummary`
           returns VsanFault if task ID is invalid or task state is 'error'.
       diskNames: A list of disks to be validated for hardware compatibility.
           
           If this field is set, the hardware compatibility check will only return
           the result of the disks in list. Both disk canonical name (e.g. 'mpx.vmhba0:C0:T0:L0')
           and UUID are supported.
           The field only takes effect with perspective 'vcsaInstallerForVsanEsa'.
       includeHealthRemediation: True to include vSAN health remediation and troubleshooting information
           in the data driven health test result.
           
           It's false by default or when
           it's not set.
       excludeChecks: A list of health checks to be excluded in this health query.
           
           Each health check item in this list is a testId string.
           If this field is set, the health checks in this list will not be
           included in the health query result.
           This is mainly used to support skipping some health checks in vLCM
           upgrade precheck workflow.
   """
   task: _typing.Optional[pyVmomi.vim.Task] = None
   diskNames: list[str] = []
   includeHealthRemediation: _typing.Optional[bool] = None
   excludeChecks: list[str] = []


class VsanClusterHealthResultBase(pyVmomi.vmodl.DynamicData):
   """
   The base class for vSAN health summary test result
   
   Attributes:
       label: The label name for the vSAN health test
   """
   label: _typing.Optional[str] = None


class VsanClusterHealthResultColumnInfo(pyVmomi.vmodl.DynamicData):
   """
   This class defines the column information for the vSAN health finding, which
   is used in data driven UI for rendering the health check result.
   
   It includes the
   column label and the data value type in the column.
   
   Attributes:
       label: The column label
       type: Type of this column, a valid type can be either of the following:
           1.
           
           string
           2\\. mor
           3\\. health
           4\\. long
           5\\. float
           6\\. listMor
           7\\. dynamic
           8\\. vsanObjectHealth, which is the enumeration type of all of vSAN object health status
           Note that \"dynamic\" means the column type can be either of the 1-6 listed above, and it must follow the convention:
           For MOR: ManagedObjectReference:<class>:<id>
           For listMor: ManagedObjectReference:<class>:<id>, ManagedObjectReference:<class>:<id>, ...
           For HostReference: HostReference:<hostname> or HostReference:<ip>
           For others: type:<value>, e.g. string:<string>
   """
   label: str
   type: str


class VsanClusterHealthResultKeyValuePair(pyVmomi.vmodl.DynamicData):
   """
   Generic class for key value pair structure
   
   Attributes:
       key: The key in the key value pair
       value: The value for the key value pair, which could be any text string
   """
   key: _typing.Optional[str] = None
   value: _typing.Optional[str] = None


class VsanClusterHealthResultRow(pyVmomi.vmodl.DynamicData):
   """
   This class defines the row values in vSAN health finding for rendering data drive UI
   
   Attributes:
       values: All of row values for a column
       actions: Support row based action, such as row based health check silencing.
           
           Since: 8.0.0.4
   """
   values: list[str] = []
   nestedRows: list[VsanClusterHealthResultRow] = []
   actions: list[VsanHealthDataDrivenAction] = []


class VsanClusterHealthResultTable(VsanClusterHealthResultBase):
   """
   The class defines the generic vSAN cluster health finding table which is
   used in data driven UI to rendering the health finding.
   
   This table class includes
   the column and row list handling in pair. In other words, each of column defines
   the column schema while the row with the same index in the list contains the value
   list for this column
   
   Attributes:
       columns: The column list in the data driven UI table
       rows: The row list in the data driven UI table
   """
   columns: list[VsanClusterHealthResultColumnInfo] = []
   rows: list[VsanClusterHealthResultRow] = []


class VsanClusterHealthResultWithRemediation(VsanClusterHealthResultBase):
   """
   This class extends `pyVmomi.vim.cluster.VsanClusterHealthResultBase`
   to support showing a specific health issue of health check result
   with proper remediation guideline.
   
   Specifically, it includes the
   following information.
     
   1\\. The health table which demonstrates the test detail for
   the health check result.
     
   2\\. The troubleshooting and remediation information to guide
   user how to troubleshooting and remediation this health issue.
   
   Attributes:
       issueDescription: It explains why this specific health issue has occurred like
           the health threshold if has or the trigger conditions for this
           health issue.
           
           This field might be unset since it will be the
           same as corresponding health test description if the health test
           only contains one issue.
       issueDetail: It's the health result table to show the detailed information of
           the health issue
       troubleshooting: The vSAN health issue troubleshooting information.
       additionalResources: Any additional resources like known issue KB or
           any kind of related documentations.
   """
   issueDescription: _typing.Optional[str] = None
   issueDetail: list[VsanClusterHealthResultTable] = []
   troubleshooting: _typing.Optional[VsanHealthTroubleshooting] = None
   additionalResources: list[VsanClusterHealthExternalLink] = []


class VsanClusterHealthSummary(pyVmomi.vmodl.DynamicData):
   """
   Cluster vSAN health summary, which aggregates all individual health findings.
   
   Includes data structures both for data driven UIs, as well as programmatic
   access by non-UI consumers.
   
   Attributes:
       timestamp: The timestamp for generating the health summary.
           
           The timestamp
           will remain unchanged if the health summary is cached and fetched
           in future indicating when the health check was performed
       clusterVersions: Health system version information across the cluster.
           
           Meant for programmatic
           consumption.
       objectHealth: Object health information across the cluster.
           
           Meant for programmatic
           consumption.
       vmHealth: Ignore this value.
       networkHealth: Network health information across the cluster.
           
           Meant for programmatic
           consumption.
       limitHealth: Limits health information across the cluster.
           
           Meant for programmatic
           consumption.
       advCfgSync: Advanced configuration synchronization information across the cluster.
           
           Meant
           for programmatic consumption.
       createVmHealth: VM creation results information across the cluster.
           
           Meant for programmatic
           consumption. Will only be populated if the respective test was run.
       physicalDisksHealth: Physical vSAN disk information across the cluster.
           
           Meant for programmatic
           consumption.
       encryptionHealth: Encryption information across the cluster.
           
           Meant for programmatic
           consumption.
       hclInfo: HCL check information across the cluster.
           
           Meant for programmatic
           consumption.
       groups: Data driven structure to display all health findings for purpose of rendering
           a UI.
           
           The health findings are grouped into \"groups\" of \"tests\". Each group
           and each test has a description, health, and optionally one or more \"details\"
           tables to display additional information about the test. Programmatic
           consumption of the health findings should avoid parsing this structure
           because it is meant for UI consumption and the content will change to
           improve user experience.
       overallHealth: Health Enum.
           
           Summarizes all groups and provides a high level status across
           all categories of health. This Enum defines sets labels for sets of health checks.
       overallHealthDescription: A human readable, short, description of the overallHealth status.
           
           As there
           may be many issues detected, the most important one is selected to be
           described. This should be the one getting first customer attention.
       clomdLiveness: CLOMD liveness on every vSAN host.
           
           Meant for programmatic consumption
       diskBalance: Balance of disk utilization across the cluster.
       genericCluster: Generic cluster configuration best practices checks.
       networkConfig: Network configuration best practices checks.
       vsanConfig: vSAN configuration checks.
       burnInTest: vSAN burn in test checks.
       perfsvcHealth: vSAN performance service health check result.
       cluster: The target cluster
       fileServiceHealth: File service health information across the cluster.
           
           Meant for programmatic
           consumption. If the file service is not enabled, this field would not be set.
       ditEncryptionHealth: Data-in-transit encryption information across the cluster.
           
           Meant for programmatic consumption.
       healthScore: The overall health score ranging from 0 to 100 based on the
           vSAN cluster health check result.
       globalDedupHealth: The global deduplication health summary across the cluster.
           
           Meant
           for programmatic consumption.
       hciMeshDitEncryptionHealth: The HCI Mesh data-in-transit encryption health summary across the cluster.
           
           Meant for programmatic consumption.
       healthStatusCounts: The overall count of health checks by status level, including error (red),
           warning (yellow), and informational (info).
   """
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
   """
   The vSAN Cluster Health System exposes the vSAN cluster health service API
   and serves as an aggregator to collect the result from each of hosts in the vSAN
   cluster.
   """
   def QueryVerifyClusterNetworkSettings(self, hosts: list[str], esxRootPassword: str) -> VsanClusterNetworkHealthResult:
      """
      Queries the vSAN cluster network setting and connectivity health status
      
      Args:
          hosts: The vSAN hosts
          esxRootPassword: The root password for the host. The password should
              be the same for all of hosts in the vSAN cluster
      
      Returns:
          The vSAN cluster network health result
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryCheckLimits(self, hosts: list[str], esxRootPassword: str) -> VsanClusterLimitHealthResult:
      """
      Queries the vSAN cluster component limits, disk space and read cache
      reservation assuming one host failure
      
      Args:
          hosts: The vSAN hosts
          esxRootPassword: The root password for the host. The password should
              be the same for all of hosts in the vSAN cluster
      
      Returns:
          The vSAN cluster limit health result
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryPhysicalDiskHealthSummary(self, hosts: list[str], esxRootPassword: str) -> list[pyVmomi.vim.host.VsanPhysicalDiskHealthSummary]:
      """
      Queries the vSAN physical disks health on all of vSAN hosts
      
      Args:
          hosts: The vSAN hosts
          esxRootPassword: The root password for the host. The password should
              be the same for all of hosts in the vSAN cluster
      
      Returns:
          The vSAN physical disks health result.
          If empty, it indicates there is no connected host in the cluster.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryAdvCfgSync(self, hosts: list[str], esxRootPassword: str, options: list[str]) -> list[VsanClusterAdvCfgSyncResult]:
      """
      Queries vSAN advanced configuration and checks if all of the hosts in a
      vSAN cluster have consistent advanced configuration options
      
      Args:
          hosts: The vSAN hosts
          esxRootPassword: The root password for the host. The password should
              be the same for all of hosts in the vSAN cluster
          options: list of vsi path for the configuration name
      
      Returns:
          The vSAN cluster advanced configuration consistent result.
          If empty, indicates all in sync.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryClusterCreateVmHealthTest(self, hosts: list[str], esxRootPassword: str, timeout: int) -> VsanClusterCreateVmHealthTestResult:
      """
      Executes VM creation test and checks if a tiny VM can be created on each of
      host of the vSAN cluster
      
      Args:
          hosts: The vSAN hosts
          esxRootPassword: The root password for the host. The password should
              be the same for all of hosts in the vSAN cluster
          timeout: The timeout time for the VM creation test
      
      Returns:
          The vSAN cluster VM creation test result
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryClusterNetworkPerfTest(self, hosts: list[str], esxRootPassword: str, multicast: bool, durationSec: _typing.Optional[int]) -> VsanClusterNetworkLoadTestResult:
      """
      Queries the vSAN network performance and checks if it meets the bandwidth requirements.
      
      Args:
          hosts: The vSAN hosts
          esxRootPassword: The root password for the host. The password should
              be the same for all of hosts in the vSAN cluster
          multicast: True to test vSAN multicast network performance.
              False to test vSAN unicast network performance.
          durationSec: The duration time for the Network Performance test. Default is 15
              seconds if not set.
      
      Returns:
          The vSAN cluster network performance test result
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryCaptureVsanPcap(self, hosts: list[str], esxRootPassword: str, duration: int, vmknic: list[VsanClusterHostVmknicMapping], includeRawPcap: _typing.Optional[bool], includeIgmp: _typing.Optional[bool], cmmdsMsgTypeFilter: list[str], cmmdsPorts: list[int], clusterUuid: _typing.Optional[str]) -> VsanVsanClusterPcapResult:
      """
      Captures the vSAN cluster multicast network trace to ensure that all
      of hosts in the cluster can receive multicast packets
      
      Args:
          hosts: The vSAN hosts
          esxRootPassword: The root password for the host. The password should
              be the same for all of hosts in the vSAN cluster
          duration: Duration to watch for packets in second. 1 minute is recommended
          vmknic: The map for host and the vmknic using for vSAN
          includeRawPcap: True to include the raw pcap data in the result. Default is False
          includeIgmp: True to include the IGMP network test data. Default is True
          cmmdsMsgTypeFilter: The filter for vSAN message type. The network message
              whose type is not in the filter list will be ignored. All of
              the supported message types include \"MASTER_HEARTBEAT\",
              \"MASTER_UPDATE\" and \"AGENT_HEARTBEAT\".
          cmmdsPorts: The vSAN multicast ports. Unset will use the default vSAN
              multicast ports.
          clusterUuid: The vSAN cluster UUID.
      
      Returns:
          The vSAN cluster multicast trace result
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryClusterHealthSystemVersions(self, hosts: list[str], esxRootPassword: str) -> VsanClusterHealthSystemVersionResult:
      """
      Queries vSAN health service version number string for each host and
      check if all of them are consistent.
      
      Mark issueFound flag as True if they
      are not consistent.
      
      As of vSphere API version 9.0, this API is deprecated and should not be
      used. There is no dedicated vSAN health service version as the vSAN health
      functionality is always part of vCenter Server and ESX host. The vSAN health
      version will always equal the vCenter Server or ESX host version, which
      can be queried directly from the vCenter Server or ESX host APIs. Use
      `pyVmomi.vim.AboutInfo.version` from vCenter Server or the appropriate ESX host
      version API instead.
      
      Args:
          hosts: The vSAN hosts
          esxRootPassword: The root password for the host. The password should
              be the same for all of hosts in the vSAN cluster
      
      Returns:
          The vSAN cluster health service version result
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def CheckClusterClomdLiveness(self, hosts: list[str], esxRootPassword: str) -> VsanClusterClomdLivenessResult:
      """
      Queries the CLOM daemon liveness on all of vSAN hosts
      
      Args:
          hosts: The vSAN hosts
          esxRootPassword: The root password for the host. The password should
              be the same for all of hosts in the vSAN cluster
      
      Returns:
          The vSAN cluster clomd health result
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def RepairClusterImmediateObjects(self, hosts: list[str], esxRootPassword: str, uuids: list[str]) -> VsanClusterHealthSystemObjectsRepairResult:
      """
      Fix absent and degraded components in object immediately.
      
      The result will contain which object have been in queue for
      repair or failed to be repaired
      
      Args:
          hosts: The vSAN hosts
          esxRootPassword: The root password for the host. The password should
              be the same for all of hosts in the vSAN cluster
          uuids: The vSAN objects UUID to be repaired. Unset to repair
              all of reduced objects in the vSAN cluster
      
      Returns:
          The vSAN cluster object repair result
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def GetClusterHclInfo(self, hosts: list[str], esxRootPassword: str) -> VsanClusterHclInfo:
      """
      Fetch HCL information about all devices in use by vSAN on all hosts.
      
      Args:
          hosts: The vSAN hosts
          esxRootPassword: The root password for the host. The password should
              be the same for all of hosts in the vSAN cluster
      
      Returns:
          The vSAN cluster HCL information
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...


class VsanClusterHealthSystemObjectsRepairResult(pyVmomi.vmodl.DynamicData):
   """
   Result for repairing vSAN objects immediately under the cluster.
   
   The result will contains the objects which have been in queue for repairing
   and those objects which cannot be repairing
   
   Attributes:
       inRepairingQueueObjects: The objects were queued for repairing
       failedRepairObjects: All of objects which are failed to be repaired
       issueFound: True if ANY of host is failed to repair the objects belonging to them
   """
   inRepairingQueueObjects: list[str] = []
   failedRepairObjects: list[pyVmomi.vim.host.VsanFailedRepairObjectResult] = []
   issueFound: bool


class VsanClusterHealthSystemStatusResult(pyVmomi.vmodl.DynamicData):
   """
   Structure which aggregates vSAN Health service installation status
   of all ESX hosts in cluster.
   
   Attributes:
       status: The current vSAN health cluster status.
           
           Status 'green' indicates all of hosts have
           been installed/uninstalled health service, 'yellow' indicates the install or uninstall process
           is on going. 'red' indicates not all of hosts in the cluster has been installed or uninstalled
           the health service successfully. This status should be used with goalState which indicates the
           service should be in installed or uninstalled state.
       goalState: The target vSAN health cluster state.
           
           Status 'installed' or 'enabled' indicated the health
           service should be enabled (all of hosts should have been installed health service), 'uninstalled'
           indicates the health service should have been uninstalled/disabled (all of hosts should have been
           uninstalled health service).
       untrackedHosts: The host name list which are not traced by EAM.
       trackedHostsStatus: The EAM tracked host name list.
   """
   status: str
   goalState: str
   untrackedHosts: list[str] = []
   trackedHostsStatus: list[pyVmomi.vim.host.VsanHostHealthSystemStatusResult] = []


class VsanClusterHealthSystemVersionResult(pyVmomi.vmodl.DynamicData):
   """
   Result for querying vSAN health service version for a cluster
   level.
   
   It will contain information for all of the hosts in the
   cluster or the hosts list passed as parameter for the version
   query method.
   
   As of vSphere API version 9.0, this structure is deprecated and
   should not be used. There is no dedicated vSAN health service version
   as the vSAN health functionality is always part of vCenter Server and
   ESX host. The vSAN health version will always equal the vCenter Server
   or ESX host version which can be queried directly from the vCenter Server
   or ESX host APIs.
   
   Attributes:
       hostResults: The version information for all the hosts requested
           includes disconnected hosts and hosts without response.
       vcVersion: Return vSAN health service version number string on vCenter Server side.
           
           If the query is not requested from vCenter Server, it will be unset.
       issueFound: True if the vSAN health service versions are inconsistent or
           query fails on some host.
       upgradePossible: True if the vSAN health service version can be upgraded on at
           least one host.
           
           Takes into account which upgrade paths are supported,
           not just if the version is outdated.
       vcBuild: Return the build number of VMware vCenter.
           
           If the query is not requested from vCenter Server, it will be unset.
   """
   hostResults: list[VsanHostHealthSystemVersionResult] = []
   vcVersion: _typing.Optional[str] = None
   issueFound: bool
   upgradePossible: _typing.Optional[bool] = None
   vcBuild: _typing.Optional[str] = None


class VsanClusterHealthTest(pyVmomi.vmodl.DynamicData):
   """
   The generic class for the vSAN cluster health test result.
   
   All of the text message in this class will be localized except for
   test ID.
   
   Attributes:
       testId: A unique ID for this test (i.e., In the vsphere web client, this is used as a ID for
           composing the AskVmware link, for example:
           http://www.vmware.com/esx/support/askvmware/index.php?eventtype=<id>&language=en_US).
       testName: The name for this health test.
       testDescription: The full test description.
       testShortDescription: The short test description.
       testHealthyEntities: The number of entities considered healthy in the context of the current test.
           
           Each test can set this field to the number of entities that are heatlhy
           in the context of its execution. For example if the test examines the connectivity
           state of the hosts, the healthy entities in its context are the \"connected\"
           hosts. This field is optional as not all tests can have \"healthy\" objects.
           An example for such tests are the tests that contain only errors. In such context
           there is no \"healthy\" entity so the test should leave this field unset.
       testAllEntities: The number of entities examined by the current test.
           
           Each test can set this field to the number of examined entities. For example
           if the test checks the connectivity of the hosts, this field should be set to
           the number of hosts that are being tested.
       testHealth: The test result enumeration.
           
           The possible values are
           'green', 'yellow', 'red', 'unknown', or 'info'.
       testDetails: The test result data.
           
           Each data item include the UI presentation structure
           and the actual value.
       testActions: The actions needed by user for potential vSAN health problem.
       historicalResults: The historical check results for this test.
       testCorrelation: The health correlation for the current health test
       reducedScore: The reduced health score when it is not green.
           
           It will be 0 if it's green.
       category: The health category of this health test when it's not green.
           
           Notice the same health test may belong to the different
           category according to its actual health status since it may
           have different user impact.
       riskIfNotFix: The potential risk if this vSAN health warning is not resolved
           from user perspective.
           
           The main purpose for this field is to
           let user understand the possible impact for this health finding
           and then decide the proper remediation plan.
       lastStatusChangeTime: The last time when the health status was changed.
           
           For example, if
           the current health status is green, then it will be the last time when
           the health status was changed from non-green status and vice
           versa. It will be unset if the health status has never been changed.
   """
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
   """
   The mapping between the host and the vSAN vmknic
   
   Attributes:
       host: The host name
       vmknic: The name of vSAN vmknic
   """
   host: str
   vmknic: str


class VsanClusterLimitHealthResult(pyVmomi.vmodl.DynamicData):
   """
   This class encapsulates the result of vSAN cluster limit health
   
   Attributes:
       issueFound: Whether any health issue was found
       componentLimitHealth: The component usage health status.
           
           The status will be red if the used of component
           number exceeds 90% of total component number limit, the status will be yellow if it
           exceeds 80% of total component number and it will be green if it's less than 80% of
           total component number
       diskFreeSpaceHealth: The aggregated result of the host level disk usage health status.
           
           On one
           host, the status will be red if the used disk space is greater than 90% of
           the host's total space and the status will be yellow if the used percentage
           is greater than 70% and not greater than 90%. The status will be green if
           the used percentage is not greater than 70%.
       rcFreeReservationHealth: The read cache reservation health status.
           
           The status will be red if the reserved read
           cache space is larger than 90% of total space, the status will be yellow if it's larger
           than 70% of total space and it will be green if it's less than 70% of total space
       hostResults: Per host results.
           
           Hosts for which the limit check failed will not be included.
       whatifHostFailures: Simulation results for 0, 1 or more host failures.
       hostsCommFailure: Indicates names of hosts which are not able to communicate with
   """
   issueFound: bool
   componentLimitHealth: str
   diskFreeSpaceHealth: str
   rcFreeReservationHealth: str
   hostResults: list[pyVmomi.vim.host.VsanLimitHealthResult] = []
   whatifHostFailures: list[VsanClusterWhatifHostFailuresResult] = []
   hostsCommFailure: list[str] = []


class VsanClusterMgmtInternalSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   This system provides interfaces to remediate inconsistency of vSAN configurations
   at both cluster and host level.
   
   It can be accessed through MOID vsan-cluster-mgmt-internal-system at vCenter side.
   """
   def RemediateVsanCluster(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task:
      """
      Remediate a cluster, to ensure vSAN cluster state matches vpxd cluster state,
      and also guarantee vSAN state of all member hosts is updated if required.
      
      Args:
          cluster: The target vim.ClusterComputeResource to remediate.
      
      Returns:
          vim.Task
      
      Raises:
          pyVmomi.vim.fault.NotFound: when specified cluster doesn't exist.
      """
      ...
   def RemediateVsanHost(self, host: pyVmomi.vim.HostSystem) -> pyVmomi.vim.Task:
      """
      Remediate a single standalone host.
      
      Will ensure the vSAN state of the host is
      updated if required. If the host was removed from a cluster, the cluster needs
      to remediate in order for the vSAN cluster to correctly reflect that the host
      is no longer part of the cluster.
      
      Args:
          host: The target vim.HostSystem to remediate.
      
      Returns:
          vim.Task
      
      Raises:
          pyVmomi.vim.fault.NotFound: when specified host doesn't exist.
      """
      ...


class VsanClusterNetworkHealthResult(pyVmomi.vmodl.DynamicData):
   """
   Contains the vSAN cluster network health test result.
   
   This structure aggregates network health information from all hosts in
   a vSAN cluster. It includes per-host network connectivity results,
   cluster-wide connectivity test outcomes, configuration consistency
   information, and flags indicating detected network issues. The structure
   provides comprehensive information about network health that can affect
   vSAN operations, including connectivity between hosts, network latency,
   vSAN vmknic presence, and network partition detection.
   
   Attributes:
       hostResults: Per-host network health test results in the vSAN cluster.
           
           This field contains network health information for each host in the
           cluster, including connectivity test results, vmknic configuration,
           and any host-specific network issues detected.
       issueFound: Indicates whether any vSAN cluster network health issue was found.
           
           This field is set to true when any network health problems are detected
           in the cluster, for example:
           - Multiple partitions exist
           - vsanVmknicPresent is False
           - issueFound in hostResults is True for any host
           - Any ping test fails
           - The hostLatencyCheckSuccess test fails
           - Hosts are disconnected from or not-responding to vCenter
       vsanVmknicPresent: Indicates whether at least one vSAN vmknic is found on the hosts.
           
           This field is set to true if each connected host in the vSAN cluster
           has at least one vSAN vmknic configured.
       matchingMulticastConfig: Indicates whether all hosts in the vSAN cluster have matching multicast
           configuration.
           
           This field is set to true when all hosts in the cluster have consistent
           multicast configuration for vSAN traffic. Inconsistent multicast
           configuration can lead to network connectivity issues and vSAN
           communication problems.
           
           As of vSphere API 6.7.0 Update 1 release. vSAN has moved from multicast
           to unicast networking. This field is no longer relevant for clusters
           using unicast mode. Use `pyVmomi.vim.cluster.VsanClusterNetworkHealthResult.clusterInUnicastMode` to determine the
           cluster's networking mode instead.
       matchingIpSubnets: Indicates whether all hosts in the vSAN cluster are in the same
           network subnets.
           
           This field is set to true when all hosts have vSAN vmknics configured
           in the same IP subnet. Hosts in different subnets may experience
           network connectivity issues depending on the network configuration.
       pingTestSuccess: True if the network ping test with small package size is successful between all
           connected hosts.
           
           The ping test between any of two connected hosts fails when
           there are lost packets.
       largePingTestSuccess: True if the network ping test with large package size (9000 bytes) is successful
           between all connected hosts.
           
           The ping test between any of two connected hosts
           fails when there are lost packets.
       hostLatencyCheckSuccess: True if the ping test for network latency using small-sized packets is successful
           between all connected hosts.  
           The network latency test fails when:
           - The ping latency between any two data hosts > 5ms or
           - The ping latency between a data site and a witness(non-ROBO) > 200ms or
           - The ping latency between a data site and a witness(ROBO) > 500ms
       potentialMulticastIssue: True if the vSAN cluster has potential multicast issue if any one
           of the checks fails including if there is vSAN partition, any ping
           test fails, if the vSAN multicast configuration matches among all
           of hosts and if there is at lease one vSAN vmknic present for all
           of hosts.
           
           As of vSphere API 6.7.0 Update 1 release. vSAN has moved from multicast
           to unicast networking. This field is no longer relevant for clusters
           using unicast mode. Use `pyVmomi.vim.cluster.VsanClusterNetworkHealthResult.issueFound` and examine the specific
           test results in `pyVmomi.vim.cluster.VsanClusterNetworkHealthResult.hostResults` to identify network issues instead.
       otherHostsInVsanCluster: The UUID list of hosts which are in the vSAN cluster but not found in the
           vCenter cluster, including VC disconnected hosts that are in the vSAN
           cluster but excluding vSAN-disabled hosts in the vCenter cluster.
       partitions: A list of partitions, where each partition is a collection of host UUIDs
           representing a group of hosts that are network-connected and mutually
           reachable from a vSAN perspective.
           
           In a healthy vSAN cluster, this list should contain exactly one partition
           to which all participating hosts belong. If hosts within the cluster lose
           communication with one another, the vSAN cluster is considered split,
           resulting in multiple partitions.
           
           Hosts that are not-responding are grouped into a dedicated \"unknown\"
           partition. Note that hosts disconnected from VC and hosts in maintenance
           mode do not impact the vSAN partition and are still included in this
           partition list.
       hostsWithVsanDisabled: The host name list which are disabled vSAN.
           
           Disconnected or not-responding hosts are not included.
       hostsDisconnected: The host name list which are disconnected from vCenter.
       hostsCommFailure: The host name list on which the vSAN service cannot cannot communicate
           with the vSAN service in vCenter.
           
           Disconnected or not-responding hosts are not included.
       hostsInEsxMaintenanceMode: The host name list which are in the maintenance mode.
       hostsInVsanMaintenanceMode: The host name list which are in the vSAN maintenance mode.
       infoAboutUnexpectedHosts: Any additional information about hosts in otherHostsInVsanCluster field will
           be captured here.
           
           If there is no additional info available, then the host will
           not be listed here.
           
           These unexpected hosts are those in the vSAN cluster but not in the VC cluster,
           excluding not-responding hosts.
       clusterInUnicastMode: True if all connected hosts in the cluster are in unicast mode, otherwise,
           return False.
           
           vSAN disabled hosts are excluded.
       clusterInRDMAMode: True indicates Cluster has enabled RDMA for data traffic among host.
           
           Only when all hosts in the cluster are enabled RDMA and use RoCEv2
           protocol for data traffic, the cluster will be considered as RDMA mode.
   """
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
   """
   This class encapsulates the result of multicast performance test for vSAN
   cluster.
   
   Attributes:
       clusterResult: The overall vSAN cluster result for multicast performance test
       hostResults: The multicast performance test result for each of host
   """
   clusterResult: VsanClusterProactiveTestResult
   hostResults: list[pyVmomi.vim.host.VsanNetworkLoadTestResult] = []


class VsanClusterNetworkPartitionInfo(pyVmomi.vmodl.DynamicData):
   """
   The vSAN cluster network partition information
   
   Attributes:
       hosts: The host name list in the same vSAN network partition
       partitionUnknown: If true, the host(s) in field hosts is(are) disconnected from
           where the partitions info is collected.
           
           They belong to one or several
           partitions that is unknown to this host.
   """
   hosts: list[str] = []
   partitionUnknown: _typing.Optional[bool] = None


class VsanClusterNetworkPerfTaskSpec(pyVmomi.vmodl.DynamicData):
   """
   The additional spec for querying vSAN cluster network performance test
   
   Attributes:
       Cluster: The target cluster against which network performance test will be run.
           
           It could be the local vSAN cluster or the remote vSAN cluster whose
           datastore has been mounted to the local cluster. If not specified,
           it will run against the local vSAN cluster itself.
       DurationSec: The duration of the network performance test.
           
           Default is
           15 seconds if not set.
       ownerVc: The owner vCenter server FQDN or ip address for the given cluster parameter
           in this spec.
           
           It can be unset if the cluster is from local VC but should
           be set for the vSAN cluster from remote VC when it's mounted as remote vSAN
           datastore.
   """
   Cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource] = None
   DurationSec: _typing.Optional[int] = None
   ownerVc: _typing.Optional[str] = None


class VsanClusterPowerSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed object type provides the service interface for vsan cluster
   power action.
   
   i.e. power off a whole cluster, query current cluster power
   context, power on the cluster, etc. The vSAN cluster power system will be
   supported in both of VC and ESXi host.
   When the ManagedEntity is accessed with MOID of 'vsan-cluster-power-system'
   through vSAN service at vCenter server, it acts as cluster-level APIs.
   When it accessed with MOID of 'ha-vsan-power-system' through vSAN service
   at ESXi host side, its scope is only limited to that host.
   """
   def PerformClusterPowerAction(self, cluster: pyVmomi.vim.ComputeResource, spec: PerformClusterPowerActionSpec) -> pyVmomi.vim.Task:
      """
      Execute cluster power off or power on action.
      
      When it's called from VC, it will acts as cluster level API to perform the
      cluster power action.
      When it's called from host, if it's an orchestration host, it will act the
      similar role of VC to orchestrate the cluster power worflow. Otherwise, it
      will execute specific host power actions such as power off according to spec
      
      Args:
          cluster: The cluster where to take power action.
          spec: Indicate the detailed power action specification.
      
      Returns:
          A task object tracking the power action. In case there is something
          wrong, the task would contain the detailed error message and the
          error steps.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              power off the cluster without powerOffReason.
          pyVmomi.vim.fault.VsanFault: Exception for generic vSAN related errors, for example,
              some hosts are disconnected when starting to power off.
      """
      ...
   def QueryClusterPowerContext(self, cluster: pyVmomi.vim.ComputeResource) -> ClusterPowerContext:
      """
      Query the ClusterPowerContext.
      
      Args:
          cluster: The cluster which to query ClusterPowerContext.
      
      Returns:
          ClusterPowerContext
      """
      ...
   def UpdateClusterPowerStatus(self, cluster: pyVmomi.vim.ComputeResource, status: str) -> bool:
      """
      Update the current cluster power status.
      
      Args:
          cluster: The cluster which to update the power status.
          status: The target status needs to be set.
      
      Returns:
          a boolean indicates success or not.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Exception for generic vSAN related errors, for example,
              trying to update the power status when there is a running
              power action task.
      """
      ...


class VsanClusterProactiveTestResult(pyVmomi.vmodl.DynamicData):
   """
   The generic class for vSAN cluster proactive test result.
   
   Attributes:
       overallStatus: The overall proactive test result status enumeration.
           
           The all possible values are 'green', 'yellow', 'red',
           'unknown', or 'info'.
       overallStatusDescription: A human readable, short description of the overall status result
           to let user know the potential problem in the first glance.
       timestamp: The time when the test was performed.
       healthTest: It's the data driven structure to display the health test result
           for purpose of rendering a UI.
           
           The structure has a description, health status,
           and optionally one or more \"details\" tables to display additional information
           about the test. Programmatic consumption of the health findings should avoid
           parsing this structure because it is meant for UI consumption and the content
           will change to improve user experience.
   """
   overallStatus: str
   overallStatusDescription: str
   timestamp: _datetime.datetime
   healthTest: _typing.Optional[VsanClusterHealthTest] = None


class VsanClusterTelemetryProxyConfig(pyVmomi.vmodl.DynamicData):
   """
   The HTTP proxy configuration for sending vSAN cluster telemetry
   
   Attributes:
       host: The proxy host.
           
           Empty value indicates to remove the proxy setting
       port: The proxy port.
           
           Empty value indicates to remove the proxy setting
       user: The user name for the proxy host
       password: The password for the user on the proxy host
       autoDiscovered: True indicates the proxy is auto discovered in the system
           False indicates the proxy is set by user
   """
   host: _typing.Optional[str] = None
   port: _typing.Optional[int] = None
   user: _typing.Optional[str] = None
   password: _typing.Optional[str] = None
   autoDiscovered: _typing.Optional[bool] = None


class VsanClusterVMsHealthOverallResult(pyVmomi.vmodl.DynamicData):
   """
   Ignore this class.
   
   Attributes:
       healthStateList: VMs state ('green', 'yellow' and 'red') list
       overallHealthState: The overall vm health state.
   """
   healthStateList: list[VsanClusterVMsHealthSummaryResult] = []
   overallHealthState: _typing.Optional[str] = None


class VsanClusterVMsHealthSummaryResult(pyVmomi.vmodl.DynamicData):
   """
   Captures how many (and which) VM share a given health status.
   
   The VM
   considered may be a subset of the total VM, as specified by the query API.
   
   Attributes:
       numVMs: Number of VMs that have this health status.
       state: The VM health state.
           
           All of possible state include 'green', 'yellow',
           'red' and 'info'
       health: The VM state in vSAN cluster.
           
           The VM state is computed by fetching
           the most severe state of virtual disk in this VM. All of possible states
           with severity order include
           'inaccessible',
           'reduced-availability-with-no-rebuild',
           'reduced-availability-with-no-rebuild-delay-timer',
           'reduced-availability-with-active-rebuild',
           'data-move',
           'non-availability-related-reconfig',
           'non-availability-related-incompliance' and
           'healthy'
       vmInstanceUuids: instanceUuids of VM that have this health status.
           
           Only included if query API
           requested it due to size.
   """
   numVMs: int
   state: _typing.Optional[str] = None
   health: str
   vmInstanceUuids: list[str] = []


class VsanClusterVmdkLoadTestResult(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: As of vSphere API 6.7.Class for the VMDK workload performance test result for the vSAN cluster.
   
   Attributes:
       task: The VC task associates with this test result
       clusterResult: The overall vSAN cluster result for VMDK workload test.
           
           The cluster result will be empty when the task is running.
       hostResults: The VMDK load test result for each of host.
           
           The host result will be empty when the task is running.
   """
   task: _typing.Optional[pyVmomi.vim.Task] = None
   clusterResult: _typing.Optional[VsanClusterProactiveTestResult] = None
   hostResults: list[pyVmomi.vim.host.VsanHostVmdkLoadTestResult] = []


class VsanClusterWhatifHostFailuresResult(pyVmomi.vmodl.DynamicData):
   """
   This class encapsulates the result of vSAN cluster capacity and
   limit health by simulating one or more hosts failure
   
   Attributes:
       numFailures: The number of simulated host failures
       totalUsedCapacityB: The total physically used capacity in bytes aggregating from all of disks
           of all of available hosts.
           
           The physically used capacity for vSAN disk is
           defined as the maximum value between reserved capacity and data size
           physically written into the disk
       totalCapacityB: The total vSAN capacity in byte.
           
           It's the total of physical space which can be
           used for writing data including any of user data, metadata and the overhead data
       totalRcReservationB: The total read cache reservation in bytes
       totalRcSizeB: The total read cache size in byes
       usedComponents: The number of used components
       totalComponents: The maximum number of components
       componentLimitHealth: The component usage health status.
           
           The status will be red if the used of component
           number exceeds 90% of total component number limit, the status will be yellow if it
           exceeds 80% of total component number and it will be green if it's less than 80% of
           total component number
       diskFreeSpaceHealth: The disk usage health status.
           
           The status will be red if the used disk space is larger
           than 90% of total space, the status will be yellow if it's larger than 70% of total
           space and it will be green if it's less than 70% of total space
       rcFreeReservationHealth: The read cache reservation health status.
           
           The status will be red if the reserved read
           cache space is larger than 90% of total space, the status will be yellow if it's larger
           than 70% of total space and it will be green if it's less than 70% of total space
       slackSpaceCapRequired: The total space required by the vSAN internal operations like policy
           reconfiguration and we expect user to reserve this in cluster.
       diskSpaceThreshold: Indicates the yellow or red threshold, in bytes, for the 'disk space'
           health check.
           
           The thresholds are computed based on current cluster's
           capacity reservation info.
       capacityReservationInfo: Indicates the capacity reservation info,
           `pyVmomi.vim.vsan.CapacityReservationInfo`.
   """
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
   """
   vSAN component basic information.
   
   The component information includes the component UUID,
   component state, owner host, and else.
   This information is only valid when the component type
   is \"Component\" without any children.
   
   Attributes:
       uuid: Component UUID.
       componentState: Component state.
           
           This variable will be one of the enums pre-defined in
           `VsanComponentStateTypes`.
       hostName: Owner host name.
       hostNodeUuid: Owner host node UUID.
       faultDomainUuid: Fault domain UUID.
           
           Used when the component is in a stretched cluster.
       faultDomainName: Fault domain name.
           
           Used when the component is in a stretched cluster.
       cacheDiskInfo: Cache disk information.
           
           Used when the component is in vSAN
           OSA environment.
       capacityDiskInfo: Capacity disk information.
           
           Supported for both vSAN OSA and ESA
           environment.
           Unset if the component is in abnormal state
           like 'stale' or 'absent'.
   """
   uuid: str
   componentState: str
   hostName: str
   hostNodeUuid: str
   faultDomainUuid: _typing.Optional[str] = None
   faultDomainName: _typing.Optional[str] = None
   cacheDiskInfo: _typing.Optional[pyVmomi.vim.vsan.DiskInfo] = None
   capacityDiskInfo: _typing.Optional[pyVmomi.vim.vsan.DiskInfo] = None


class VsanComponentPlacement(pyVmomi.vmodl.DynamicData):
   """
   vSAN component placement details.
   
   The component placement details are the physical placement
   details for the object components and the disks.
   It is a tree structure for the component details based on
   the RAID configration.
   
   Attributes:
       type: Component type.
           
           The type can be \"Concatenation\", \"RAID_1\", \"RAID_0\",
           \"Component\" or else.
       children: Component placement tree structure.
           
           The root node is the component type \"Concatenation\",
           \"RAID_1\", \"RAID_0\" or else.
           For the leaf nodes:
           - The `pyVmomi.vim.cluster.VsanComponentPlacement.type` set to \"Component\".
           - The `pyVmomi.vim.cluster.VsanComponentPlacement.basicInfo` is set.
           - This field is unset.
       basicInfo: Component basic information.
           
           Set only when the component type is \"Component\",
           and the component is a leaf node.
   """
   type: str
   children: list[VsanComponentPlacement] = []
   basicInfo: _typing.Optional[VsanComponentBasicInfo] = None

class VsanComponentStates:
   """vSAN component state types."""
   pass


class VsanConfigGeneration(pyVmomi.vmodl.DynamicData):
   """
   Generation tracker for vSAN configuration.
   
   By storing this information
   on ESX and comparing it against VCs version, the goal is to determine
   if they got out of sync, and if so, who is up to date.
   
   Attributes:
       vcUuid: VC instance UUID to determine which VC generated the config.
       genNum: Generation number, a monotonically increasing number.
       genTime: Generation timestamp, used for human readable consumption, not
           used to determine which generation is \"newer\", as timestamps
           can't be trusted for this in distributed systems.
           
           The unit of this value is in milli-seconds since the epoch.
   """
   vcUuid: str
   genNum: pyVmomi.VmomiSupport.long
   genTime: pyVmomi.VmomiSupport.long


class VsanDataDrivenAPIAction(pyVmomi.vmodl.DynamicData):
   """
   The vSAN Cluster health action is a set of instructions that guide vSphere
   and storage administrators on how to address potential health problems
   detected by the vSAN health service.
   
   The data-driven API action,
   in this case, refers to the action button in the user interface,
   which is defined by vSAN remediation rules and does not require any code
   changes from the UI side. This approach offers flexibility as it allows
   administrators to invoke any APIs provided by the vSAN service using the
   button in the UI.
   
   Attributes:
       actionId: The unique action ID
       actionLabel: The localized label for the action that is displayed in the UI.
       actionDescription: The localized description for the action that is displayed in the UI.
       enabled: True indicates the action will be enabled from UI.
           
           In the data-driven action use case, it is not possible for it to be False.
       parameters: The action parameters which can be used as the parameters for
           this action API when calling from UI.
   """
   actionId: str
   actionLabel: pyVmomi.vmodl.LocalizableMessage
   actionDescription: pyVmomi.vmodl.LocalizableMessage
   enabled: bool
   parameters: list[pyVmomi.vim.KeyValue] = []

class VsanDatastoreType:
   """
   The vSAN Datastore type.
   
   It can be used in
   `pyVmomi.vim.cluster.QueryVsanManagedStorageSpaceUsageSpec`.
   """
   pass


class VsanDiagnosticsSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed object provides the diagnostics service that operates at cluster
   level.
   
   It runs the periodical diagnostics on the vSAN related statistics, as
   well as the on-demand diagnostics operation, e.g., the diagnostics of the
   IOs for a certain virtual machine.
   The ManagedEntity can be accessed with MOID of
   'vsan-cluster-diagnostics-system' through vSAN service at at vCenter side.
   """
   def QueryNetworkDiagnostics(self, cluster: pyVmomi.vim.ComputeResource, host: _typing.Optional[pyVmomi.vim.HostSystem]) -> list[VsanNetworkDiagnostics]:
      """
      Get the latest network events that triggered network alarms.
      
      Args:
          cluster: The cluster where the network diagnostics is performed.
          host: Get only for the specified host.
      
      Returns:
          vim.cluster.VsanNetworkDiagnostics[]
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def GetThresholds(self, cluster: pyVmomi.vim.ComputeResource, entityType: _typing.Optional[str], metric: _typing.Optional[str]) -> list[VsanDiagnosticsThreshold]:
      """
      Get the threshold.
      
      If \"entityType\" is not set, all threshold settings will be returned;
      If \"entityType\" is set but \"metric\" is not set, threshold settings for the
      specified \"entityType\" will be returned; If threshold settings doesn't exist
      for \"entityType\", empty result ([]) will be returned;
      If both \"entityType\" and \"metric\" are set, threshold settings for the
      specified \"entityType\" and \"metric\" will be returned; If threshold settings
      doesn't exist for either \"entityType\" or \"metric\", empty result ([]) will be
      returned.
      If \"metric\" is set but \"entityType\" is not set, \"metric\" will be ignored and
      all threshold settings will be returned.
      
      Args:
          cluster: The cluster where the threshold is to get from
          entityType: Get threshold only for the specified entity type.
          metric: Get threshold only for the specified metric, \"entityType\" must
              also be set if \"metric\" is set.
      
      Returns:
          vim.cluster.VsanDiagnosticsThreshold[]
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def SetThresholds(self, cluster: pyVmomi.vim.ComputeResource, thresholds: list[VsanDiagnosticsThreshold]) -> None:
      """
      Set the threshold.
      
      The \"entityType\" and \"metric\" of the new threshold must be in current
      supported list (see `pyVmomi.vim.cluster.VsanDiagnosticsThreshold.entityType`),
      or fault \"vmodl.fault.InvalidArgument\" will be raised.
      If \"yellow\" or \"red\" value is \"0\" or not set in the new threshold, the
      existing \"yellow\" or \"red\" value of current threshold setting will keep
      unchanged.
      
      Args:
          cluster: The cluster where the threshold is to set to
          thresholds: The new threshold value to set
      
      Returns:
          void
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
      """
      ...
   def StartIODiagnosticsTask(self, targets: list[pyVmomi.vim.vsan.IODiagnosticsTarget], cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], duration: _typing.Optional[pyVmomi.VmomiSupport.long]) -> pyVmomi.vim.Task:
      """
      Start IO diagnostics task against the given targets running on vSAN datastore.
      
      It's not supported to run multiple diagnostics tasks at the same time. You
      need either cancel the running task or wait until it completes before
      starting a new diagnostics task.
      
      Args:
          targets: The targets to run the diagnostics.
          cluster: The cluster where the targets belong to, ignored when calling
              against ESXi hosts.
          duration: The duration time in seconds to run diagnostics. The valid range
              is [300, 3600], default is 300.
      
      Returns:
          The task that runs the diagnostics.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the targets are not valid.
          pyVmomi.vmodl.fault.NotSupported: if there's already a running diagnostics task.
          pyVmomi.vim.fault.VsanFault: if the caller doesn't have the required privilege or
              if the pre-check tests failed.
      """
      ...
   def QueryIODiagnosticsInstances(self, querySpec: pyVmomi.vim.vsan.IODiagnosticsInstanceQuerySpec, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> list[pyVmomi.vim.vsan.IODiagnosticsInstance]:
      """
      Query the completed diagnostics instances by the given query spec.
      
      Args:
          querySpec: The spec for instance query.
          cluster: The cluster where the diagnostics is performed, ignored when
              calling against ESXi hosts.
      
      Returns:
          The list of the completed diagnostics instances.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the query spec is not valid.
          pyVmomi.vim.fault.VsanFault: if the caller doesn't have the required privilege or if
              the vSAN performance service is disabled.
      """
      ...
   def QueryIODiagnosticsStats(self, instanceName: str, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> list[pyVmomi.vim.vsan.IODiagnosticsTargetStats]:
      """
      Query the IO diagnostics stats according to the given diagnostics instance
      name.
      
      Args:
          instanceName: The completed diagnostics instance name.
          cluster: The cluster where the diagnostics is performed.
      
      Returns:
          The diagnostics stats.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the given diagnostics instance name represent a
              running instance.
          pyVmomi.vim.fault.VsanFault: if the caller doesn't have the required privilege or if
              the vSAN performance service is disabled.
      """
      ...
   def CreateIOTripAnalyzerRecurrences(self, cluster: pyVmomi.vim.ComputeResource, recurrences: list[pyVmomi.vim.vsan.VsanIOTripAnalyzerRecurrence]) -> list[pyVmomi.vim.vsan.VsanIOTripAnalyzerRecurrence]:
      """
      Schedule a set of IO trip analyzer recurrences.
      
      Currently only 1 recurrence supported for each vSAN cluster.
      
      Args:
          cluster: The cluster on which the IO trip analyzer scheduler is
              configured.
          recurrences: The scheduler recurrences configurations.
      
      Returns:
          The list of recurrences that are configured successfully. If the
          name of the recurrence is not given, it will fill the name with
          automatically generated name and return it in the list.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the recurrence(s) setting(s) are not valid.
          pyVmomi.vim.fault.AlreadyExists: if the recurrence(s) name(s) already exists.
          pyVmomi.vim.fault.VsanFault: if internal vSAN error hit.
      """
      ...
   def GetIOTripAnalyzerSchedulerConfig(self, cluster: pyVmomi.vim.ComputeResource) -> _typing.Optional[pyVmomi.vim.vsan.VsanIOTripAnalyzerConfig]:
      """
      Get the IO trip analyzer scheduler configurations for the given cluster.
      
      Args:
          cluster: The cluster on which the IO trip analyzer scheduler is
              configured.
      
      Returns:
          The IO trip analyzer scheduler configuration.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: if internal vSAN error hit.
      """
      ...
   def EditIOTripAnalyzerRecurrences(self, cluster: pyVmomi.vim.ComputeResource, recurrences: list[pyVmomi.vim.vsan.VsanIOTripAnalyzerRecurrence]) -> list[pyVmomi.vim.vsan.VsanIOTripAnalyzerRecurrence]:
      """
      Edit the IO trip analyzer recurrences with the given configuration.
      
      The name of the recurrence is used to find the recurrence to be updated. It
      must be provided when editing.
      
      Args:
          cluster: The cluster on which the IO trip analyzer scheduler is
              configured.
          recurrences: The updated recurrence(s) configuration.
      
      Returns:
          The list of recurrence(s) that are edited successfully.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the recurrence(s) setting(s) are not valid.
          pyVmomi.vim.fault.NotFound: if the recurrence(s) name(s) not found.
          pyVmomi.vim.fault.VsanFault: if internal vSAN error hit.
      """
      ...
   def RemoveIOTripAnalyzerRecurrences(self, cluster: pyVmomi.vim.ComputeResource, names: list[str]) -> None:
      """
      Remove the IO trip analyzer recurrence(s) with the given name(s).
      
      Args:
          cluster: The cluster on which the IO trip analyzer scheduler is
              configured.
          names: The name(s) of the IO trip analyzer recurrence(s) to be
              removed.
      
      Returns:
          void
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the recurrence(s) name(s) not found.
          pyVmomi.vim.fault.VsanFault: if internal vSAN error hit.
      """
      ...
   def SetTraceObjectPolicy(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], traceObjectUuid: str, profile: _typing.Optional[pyVmomi.vim.vm.ProfileSpec]) -> bool:
      """
      Set the policy of the vSAN namespace object that hold the vSAN trace files.
      
      The cluster parameter is ignored if called on ESXi.
      Profile can be:
      - VirtualMachineDefinedProfileSpec where profileId is an empty string and
        instead the profileData is set for extensionKey 'com.vmware.vim.sps'. In this
        case the objectData field can be either the vSAN expression format, or a SPBM
        XML string.
        
        
      If no profile is supplied, a default profile with hostFailuresToTolerate
      setting will be used.
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
          profile: See above description for all possible options.
      
      Returns:
          True
      
      Raises:
          pyVmomi.vim.fault.VsanFault: if the caller doesn't have the required privilege
      """
      ...


class VsanDiagnosticsThreshold(pyVmomi.vmodl.DynamicData):
   """
   Define the threshold value for the alarms raised by VsanDiagnosticsSystem.
   
   Attributes:
       entityType: The \"entityType\" is used to identify the target entity to get/set the
           threshold value.
           
           Current supported entity types and metrics:  
           
           Entity Type - Metrics
           
           'vsan-pnic-net'
            - 
           'rxCrcErr', 'txCarErr', 'rxErr', 'txErr', 'pauseCount', 'rxMissErr', 'rxOvErr', 'rxFifoErr'
           
           'rdt-net'
            - 
           'checksumMismatchCount'
       metric: The \"metric\" is used to identify the stats of an entity, e.g.:
           rxCrcErr (CRC error of physical NIC), txCarErr (Carrier error of physical NIC).
           
           Current supported metrics:  
           See `pyVmomi.vim.cluster.VsanDiagnosticsThreshold.entityType`
       yellow: The yellow value of threshold indicates light severe warnings.
           
           The unit is
           the same as the metric.
       red: The red value of threshold indicates severe warnings.
           
           The unit is the same as the metric.
   """
   entityType: str
   metric: str
   yellow: _typing.Optional[int] = None
   red: _typing.Optional[int] = None


class VsanDiskFormatConversionCheckResult(pyVmomi.vim.VsanUpgradeSystem.PreflightCheckResult):
   """
   Extended DataType from Vim.VsanUpgradeSystem.PreflightCheckResult,
   added more fields to present more detailed information from
   vSAN preflight check.
   
   Attributes:
       isSupported: Whether vSAN could process disk format conversion
           on given cluster with specified conversion options.
           
           If
           this field is set to false, please check the issues field
           to get the detailed reason which blocks disk format conversion.
       targetVersion: Goal format version the given cluster could support.
           
           The goal
           format version is up to the versions of ESXi hosts under given
           cluster, please reference to below:
           ESXi of vSphere6.0U2 and latter, supported version is 3 in upgrade
           process, and 2 in downgrade process;
           ESXi of vSphere6.0 series before vSphere6.0U2, supported version is 2
           in upgrade process, and 1 in downgrade process;
           ESXi of lower version, is not supported;
       isDataMovementRequired: Whether data movement is required if disk format conversion process is triggered.
       storagePoolDisk: Cannonical name of the disk removed by previous DFC but not added back.
   """
   isSupported: bool
   targetVersion: _typing.Optional[int] = None
   isDataMovementRequired: _typing.Optional[bool] = None
   storagePoolDisk: _typing.Optional[str] = None


class VsanDiskFormatConversionSpec(pyVmomi.vmodl.DynamicData):
   """
   Advanced vSAN disk format specification that governs
   which format to use for the disks newly formatted.
   
   However,
   it does NOT change the cluster configuration. Therefore,
   the advanced feature configurations below should be picked
   in sync with the cluster configuration, or users can invoke
   the cluster configuration change, which will automatically
   run the vSAN disk format conversion with the changed
   feature configurations.
   
   Attributes:
       dataEfficiencyConfig: Whether to enable or disable vSAN data efficiency
           from disk format layer.
       dataEncryptionConfig: vSAN encryption configuration parameters for
           disk format layer.
       skipHostRemediation: Do not perform host configuration remediation on hosts as part of the
           Disk Format Conversion.
           
           Remediation is performed by default to ensure hosts
           are consistent. This will prevent errors as part of Disk Format Conversion
           due to inconsistent hosts. This field can be set to True when it is already
           known that all hosts are already consistent and have the latest
           configuration avoiding this extra step.
           Unset means False.
       allowDataMovement: Whether data movement is allowed for upcoming disk format conversion process.
           
           If 'allowDataMovement' is set to False, disk format conversion flow will
           check whether data movement is required. If disk format conversion need to
           move data to complete the operation, the
           `pyVmomi.vim.vsan.upgradesystem.DisallowDataMovementIssue` will fail
           the disk format conversion task.
   """
   dataEfficiencyConfig: _typing.Optional[pyVmomi.vim.vsan.DataEfficiencyConfig] = None
   dataEncryptionConfig: _typing.Optional[pyVmomi.vim.vsan.DataEncryptionConfig] = None
   skipHostRemediation: _typing.Optional[bool] = None
   allowDataMovement: _typing.Optional[bool] = None


class VsanDiskMappingsConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   Spec for configuring the hosts' disk mappings when the vSAN
   cluster is in MANUAL claiming mode.
   
   Attributes:
       hostDiskMappings: The list of mappings to be applied.
   """
   hostDiskMappings: list[VsanHostDiskMapping] = []


class VsanEffectiveSpaceUsage(pyVmomi.vmodl.DynamicData):
   """
   Describes the metrics of vSAN effective space usage view,
   all the metrics exclude all kinds of system overhead,
   like RAID overhead as well as vSAN operation reservation.
   
   For example, the total usable capacity is the total of free
   vSAN storage space which can be fully used for writing user data.
   
   Attributes:
       totalUsableB: The total usable vSAN capacity in bytes.
           
           It's the total of free vSAN physical storage space
           for user workloads in the vSAN datastore, excluding
           all system reservations and overhead such as RAID
           redundancy.
       freeUsableB: The free usable vSAN capacity in bytes.
           
           Free usable capacity refers to the remaining portion
           of the total usable capacity in the vSAN datastore
           that is still available for user data, after
           subtracting the space already consumed by user
           workloads.
           The totalUsableB - freeUsableB = used capacity.
       actualWrittenB: The actual written vSAN capacity in bytes.
           
           It is actual used capacity but excluding the reserved
           data by thick provisioning in this cluster, excluding
           all system reservations and overhead such as RAID
           redundancy.
       overReservedB: The over reserved capacity in bytes by thick provisioning
           but not actually used yet in this cluster,
           excluding all system reservations and overhead such as RAID
           redundancy.
       totalProvisionB: The total provisioned capacity in bytes in cluster.
           
           It is aggregated by the provisioning capacity of all
           user objects in this cluster without taking RAID overhead
           into consideration.
           Below are the types of objects will be regarded as
           exceptions:
           1\\. Namespace objects
           2\\. Swap objects
           3\\. Some other system objects like global deduplication store
           objects. The thin provisioning size of these objects will
           not be counted into the total provisioned capacity, but
           only the actual primary written capacity will be counted.
       snapshotSpace: The snapshot space usage metrics, excluding all system
           reservations and overhead such as RAID redundancy.
   """
   totalUsableB: pyVmomi.VmomiSupport.long
   freeUsableB: pyVmomi.VmomiSupport.long
   actualWrittenB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   overReservedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   totalProvisionB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   snapshotSpace: _typing.Optional[VsanSnapshotSpace] = None


class VsanEntitySpaceUsage(pyVmomi.vmodl.DynamicData):
   """
   This is base class describing the vSAN space usage for the general vSAN
   entity like virtual machine.
   
   Attributes:
       entityId: The vSAN object entity ID.
           
           For the entity like virtual machine, it's the
           managed object ID like 'vm-1'.
       spaceUsageByObjectType: The vSAN space usage breakdown by object type for all of vSAN objects
           belonging to the entity.
       totalCapacityB: The total capacity in byte, which is the total used and free capacity
           combined.
           
           It's the total of physical space which can be use for writing data
           including any of user data, metadata and the overhead data.
       freeCapacityB: The free capacity in byte.
           
           It's the total of free physical space which can be
           used for writing data including any of user data, metadata and the overhead
           data.
       efficientCapacity: The efficient capacity breakdown details when the vSAN cluster enables data
           efficiency.
   """
   entityId: _typing.Optional[str] = None
   spaceUsageByObjectType: list[VsanObjectSpaceSummary] = []
   totalCapacityB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   freeCapacityB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   efficientCapacity: _typing.Optional[pyVmomi.vim.vsan.DataEfficiencyCapacityState] = None


class VsanFaultDomainsConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   Spec for configuring vSAN host fault domains and/or stretched cluster
   in the vSAN cluster.
   
   Or configuring site fault domains in compute
   only cluster to make it work in stretched compute mode.
   
   Attributes:
       faultDomains: The list of fault domains to be configured.
       witness: The configuration for the witness host.
           
           If specified, the faultDomains
           list should contain exactly two items. An exception is thrown if the
           requirements are not met.
   """
   faultDomains: list[VsanFaultDomainSpec] = []
   witness: _typing.Optional[VsanWitnessSpec] = None

class VsanHciMeshDitEncryptionIssue:
   """The vSAN HCI Mesh data-in-transit encryption health issue enumeration."""
   pass


class VsanHealthActionBase(pyVmomi.vmodl.DynamicData):
   """
   This is the base class for vSAN health issue remediation or troubleshooting.
   
   Attributes:
       description: The descriptive message for explaining what the action it is.
           
           Notice it can support the following mark up tags.
           1\\. Hyperlink <tag.link>{link_content}</tag.link>
           2\\. Host entity <tag.icon.host>${host_ip}</tag.icon.host>
   """
   description: str


class VsanHealthActionSteps(VsanHealthActionBase):
   """
   The action steps for vSAN health remediation or troubleshooting.
   
   It will
   include multiple steps for a specific remediation/troubleshooting approach.
   
   Attributes:
       steps: The action steps for a specific remediation/troubleshooting approach.
   """
   steps: list[VsanHealthActionBase] = []

class VsanHealthApiBasedAction(VsanHealthActionBase):
   """
   The vSAN health action APIs based remediation or
   troubleshooting for the vSAN health issues.
   
   Attributes:
       apiAction: The API based action for troubleshooting or remediating a health
           issue, which can be triggered either from UI or automation script.
   """
   apiAction: VsanClusterHealthAction

class VsanHealthCmdBasedAction(VsanHealthActionBase):
   """
   The VC or ESXi host command based remediation or troubleshooting
   for vSAN health issues.
   
   The commands will be listed in the UI so that user can copy to execute
   on the specified host to remediate or troubleshoot health issue. Notice
   we cannot support executing the command from UI directly.
   
   Attributes:
       commands: The command string lists.
           
           Each of command will be shown in the UI with copy
           capability supported.
   """
   commands: list[str] = []


class VsanHealthConfirmationDialog(pyVmomi.vmodl.DynamicData):
   """
   The attributes of a confirmation dialog.
   
   Attributes:
       title: The title of the confirmation dialog.
       subTitle: The subtitle of the confirmation dialog.
           
           If the field is not set, the name of cluster will be used as the subtitle.
       content: The content displayed on the confirmation dialog.
       agreeLabel: The label of the OK button.
           
           If the field is not set, \"OK\" will be used as the label.
       closeLabel: The label of the close button.
           
           If the field is not set, \"Cancel\" will be used as the label.
       isWarning: The severity of the operation.
           
           If it's True, the red confirmation button will be rendered in UI
           instead of a blue one.
   """
   title: str
   subTitle: _typing.Optional[str] = None
   content: str
   agreeLabel: _typing.Optional[str] = None
   closeLabel: _typing.Optional[str] = None
   isWarning: _typing.Optional[bool] = None


class VsanHealthCorrelation(pyVmomi.vmodl.DynamicData):
   """
   This class presents the correlation between
   health check results in case the primary health
   issue may lead to other health warnings.
   
   From the health correlation, we can provide the
   guided troubleshooting capability so that user can
   always focus on primary health issues if there are many.
   
   Attributes:
       primaryHealthTests: The health test ids which indicate the primary health issues
           causing the current health warning so that user should address
           at first.
       relatedHealthTests: The related health test ids which may be triggered
           by primary health issue.
       skippedHealthTests: The health test ids which have been skipped and shown
           as green due to the prerequisite doesn't satisfy.
           
           For example,
           if disk controller is not in the vSAN Hardware Compatibility
           List (HCL), then all of following HCL checks like driver/firmware
           version check will be skipped and shown as green.
   """
   primaryHealthTests: list[str] = []
   relatedHealthTests: list[str] = []
   skippedHealthTests: list[str] = []


class VsanHealthDataDrivenAction(VsanHealthActionBase):
   """
   The data type of data driven action for vSAN troubleshooting.
   
   Attributes:
       apiAction: The API based action for troubleshooting or remediating a health
           issue, which can be triggered either from UI or automation script.
       confirmation: The object which defines a confirmation dialog.
           
           This is optional. If it's unset, UI won't show confirmation dialog after
           clicking the button.
   """
   apiAction: VsanDataDrivenAPIAction
   confirmation: _typing.Optional[VsanHealthConfirmationDialog] = None


class VsanHealthExtMgmtPreCheckResult(pyVmomi.vmodl.DynamicData):
   """
   Result for pre-checking if a cluster is qualified to install or uninstall vSAN
   Health service extension on ESX hosts of this cluster.
   
   Attributes:
       overallResult: Indicates if all the pre-checks are passed
       esxVersionCheckPassed: Indicates if the ESX version check is passed or not.
           
           The required ESX version must be higher than 6.0.0
       drsCheckPassed: Indicates if the DRS fully automated check is passed or not.
           
           DRS must be enabled for installing health service extension
       eamConnectionCheckPassed: Indicates if the EAM connectivity check is passed or not
           The EAM must be connected for installing health service extension
       installStateCheckPassed: Indicates if the vSAN health extension is ready for
           uninstallation.
           
           The health extension can be uninstalled if
           the installation is completed
       results: Pre-checks test results for install/uninstall vSAN health service
           Detail results are combined in tables for client to retrieve
       vumRegistered: Indicates whether VUM has registered to current vCenter.
   """
   overallResult: bool
   esxVersionCheckPassed: _typing.Optional[bool] = None
   drsCheckPassed: _typing.Optional[bool] = None
   eamConnectionCheckPassed: _typing.Optional[bool] = None
   installStateCheckPassed: _typing.Optional[bool] = None
   results: list[VsanClusterHealthTest] = []
   vumRegistered: _typing.Optional[bool] = None


class VsanHealthStatusCounts(pyVmomi.vmodl.DynamicData):
   """
   Represents the count of health checks grouped by status level for
   a specific point in time.
   
   This summary provides a quick overview of overall cluster health by
   showing how many checks fall into each status category. Includes only
   non-green statuses (error, warning, info) to highlight potential issues
   or noteworthy conditions. Green (healthy) checks are intentionally excluded.
   
   Attributes:
       error: Number of health checks with error status.
       warning: Number of health checks with warning status.
       info: Number of health checks with info status.
   """
   error: int
   warning: int
   info: int


class VsanHealthTroubleshooting(pyVmomi.vmodl.DynamicData):
   """
   This class describes how to troubleshoot a specific
   health issue, which will provide either diagnostic steps
   for further root cause with any kind of support data or
   remediation approaches for how to recover or both.
   
   Attributes:
       diagnosticSteps: The diagnostic steps for further root cause or providing
           more support data for current health issue.
       remediations: The supported remediations for this health issue.
           
           Notice we may support multiple remediation options and the
           first one in the list should always be the recommended one.
   """
   diagnosticSteps: list[VsanHealthActionBase] = []
   remediations: list[VsanHealthActionBase] = []

class VsanHealthTxtBasedAction(VsanHealthActionBase):
   """
   The plain text based remediation or troubleshooting
   for the vSAN health issue.
   """
   pass


class VsanHistoricalHealthQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   Generic class to define the query spec for vSAN cluster
   historical health information.
   
   Attributes:
       clusters: The target cluster list.
           
           Only the query for a single cluster is supported for
           now.
       start: The start time querying from the historical result.
       end: The end time querying from the historical result.
           
           Default is till now if not specified.
       testId: The target health test ID.
           
           To get all supported health test IDs and their associated group ID,
           refer to `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.queryAllSupportedHealthChecks`
       groupId: The group ID which the health test belongs to.
           
           To get all supported health test IDs and their associated group ID,
           refer to `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.queryAllSupportedHealthChecks`
       includeHealthRemediation: True to populate the vSAN health remediation information
           in the historical health test result.
           
           It's false by default or when
           it's not set.
   """
   clusters: list[pyVmomi.vim.ClusterComputeResource] = []
   start: _datetime.datetime
   end: _typing.Optional[_datetime.datetime] = None
   testId: _typing.Optional[str] = None
   groupId: _typing.Optional[str] = None
   includeHealthRemediation: _typing.Optional[bool] = None


class VsanHistoricalHealthTest(pyVmomi.vmodl.DynamicData):
   """
   The generic class for the historical health test result.
   
   Attributes:
       timestamp: The timestamp.
       health: The health result enumeration.
           
           The possible values are
           'green', 'yellow', 'red', 'unknown', or 'info'.
       testDetails: The health check detail tables.
       testCorrelation: The health correlation for the current health test.
   """
   timestamp: _datetime.datetime
   health: str
   testDetails: list[VsanClusterHealthResultBase] = []
   testCorrelation: _typing.Optional[VsanHealthCorrelation] = None


class VsanHostClomdLivenessResult(pyVmomi.vmodl.DynamicData):
   """
   Result of checking CLOMD liveness on an ESX host belongs to a vSAN cluster.
   
   Field 'error' keeps the error output in checking CLOMD liveness.
   
   Attributes:
       hostname: Name of a vSAN host
       clomdStat: Indicate CLOMD state on the vSAN host.
           
           The possible states are 'alive', 'abnormal' (if any error occurred during checking
           the ClOMD state) and 'unknown' (if vSAN health service is
           not installed on the host)
       error: Error output for checking CLOMD state on the vSAN host
   """
   hostname: str
   clomdStat: str
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VsanHostCreateVmHealthTestResult(pyVmomi.vmodl.DynamicData):
   """
   This class encapsulates VM creation test result for a single vSAN host
   
   Attributes:
       hostname: The host name
       state: The VM creation test state.
           
           All of possible states are \"error\", \"timeout\"
           and \"success\"
       fault: The exception fault for the VM creation test, which will be set when the host
           is disconnected, cannot create virtual machine or timed out when creating VM
           and any exception throwing from destroying the created VM
   """
   hostname: str
   state: str
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VsanHostDiskMapping(pyVmomi.vmodl.DynamicData):
   """
   Contains the disk mappings for a host.
   
   Attributes:
       host: The host that the mappings are related.
       cacheDisks: List of disk that should be used for the cache tier.
       capacityDisks: List of disks that should be used for the capacity tier.
           
           This field can also be used in vSAN direct datastore provision,
           i.e. `pyVmomi.vim.cluster.VsanHostDiskMapping.type` set to
           \"vsandirect\". It represents all the disk(s) used to create vSAN direct
           datastores. All disk(s) specified to this field must not be used by vSAN
           or any other datastores.
       type: The type of the groups that should be created.
   """
   class VsanDiskGroupCreationType(pyVmomi.VmomiSupport.Enum):
      """
      The type of the disk group to created.
      
      Attributes:
          pmem: Do not use.
      """
      allflash: _typing.ClassVar['VsanHostDiskMapping.VsanDiskGroupCreationType'] = 'allflash'
      hybrid: _typing.ClassVar['VsanHostDiskMapping.VsanDiskGroupCreationType'] = 'hybrid'
      vsandirect: _typing.ClassVar['VsanHostDiskMapping.VsanDiskGroupCreationType'] = 'vsandirect'
      pmem: _typing.ClassVar['VsanHostDiskMapping.VsanDiskGroupCreationType'] = 'pmem'
      VsanDiskGroupCreationType_Unknown: _typing.ClassVar['VsanHostDiskMapping.VsanDiskGroupCreationType'] = 'VsanDiskGroupCreationType_Unknown'

   host: pyVmomi.vim.HostSystem
   cacheDisks: list[pyVmomi.vim.host.ScsiDisk] = []
   capacityDisks: list[pyVmomi.vim.host.ScsiDisk] = []
   type: str


class VsanHostHealthSystemVersionResult(pyVmomi.vmodl.DynamicData):
   """
   The vSAN health service version information for a single ESX host.
   
   The error field will show the reason for host not connected or without
   vSAN health service installed.
   
   Attributes:
       hostname: The name of the host
       version: Version number string of vSAN health service of host.
           
           If vSAN health service is not installed on this host, the
           version value returned will be '0.0', and an error message will
           be set in error field of this model.
           The field will be unset if the query fails except the case
           that the service is not install on this host.
       error: This field will be set only when the query fails, it
           stores the error message for querying vSAN health service
           version to a host.
       build: The build number of the ESXi host.
   """
   hostname: str
   version: _typing.Optional[str] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   build: _typing.Optional[str] = None


class VsanIoInsightInstance(pyVmomi.vmodl.DynamicData):
   """
   This data object describes a set of information related to one time
   ioinsight execution, which includes ioinsight run name,
   state(running or stopped), execution time range and a list of ioinsight
   information along with the host.
   
   Attributes:
       runName: Run name of the ioinsight instance, which is specified when invoking
           `pyVmomi.vim.cluster.VsanIoInsightManager.startIoInsight`
       state: State of the ioinsight instance, that is, ioinsight instance is in running
           or completed.
           
           This attribute can be optional for ioinsight instance update operation.
       startTime: Start timestamp of the ioinsight instance.
           
           This attribute can be optional for ioinsight instance update operation.
       endTime: End timestamp of the ioinsight instance.
           
           This attribute is optional for either running ioinsight instance, or
           ioinsight instance update operation.
       hostsIoInsightInfo: One or multiple ioinsights information along with the hosts, which belong
           to the ioinsight instance.
           
           This attribute is optional for ioinsight instance update operation.
       hostUuids: The uuid of hosts which are related to ioinsight instance.
       vmUuids: The uuid of VMs which are related to ioinsight instance.
   """
   runName: str
   state: _typing.Optional[str] = None
   startTime: _typing.Optional[_datetime.datetime] = None
   endTime: _typing.Optional[_datetime.datetime] = None
   hostsIoInsightInfo: list[pyVmomi.vim.host.VsanHostIoInsightInfo] = []
   hostUuids: list[str] = []
   vmUuids: list[str] = []


class VsanIoInsightInstanceQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   Describe specifications for ioinsight instance query operation.
   
   Attributes:
       state: Indicate the state in which ioinsight instance will be returned.
           
           If this attribute is not provided, ioinsight instance state will be skipped
           during the query operation.
       entityRefId: The 'entityRefId' is a reference id of the target entity, which acts as
           filter condition for ioinsight instance query.
           
           For example, if host entity is provided then the query operation
           will return all ioinsight instances containing the host.
           If this attribute is not provided, the query operation will return all
           ioinsight instances matching
           `pyVmomi.vim.cluster.VsanIoInsightInstanceQuerySpec.state`
           The reference id consists of entity type and ID, which is formated as
           <entity-type>:<entity-id>
           Below are the examples:
           
           Entity Type
            - Entity ID format
            - EntityRefId Example
           
           Host
            - Host UUID
            - 'host:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
           
           VM
            - VM InstanceUUID
            - 'vm:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
           
           runName
            - IOInsight runName
            - 'runName:xxxxxx'
   """
   state: _typing.Optional[str] = None
   entityRefId: _typing.Optional[str] = None

class VsanIoInsightInstanceState:
   """Type of ioinsight instance, which can be either running or completed."""
   pass


class VsanIoInsightManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed object is designed to provide service interfaces to manage
   ioinsight(s) for VMs virtual disks I/O performance metrics monitor and
   collection on the target hosts.
   
   It can be accessed through MOID of 'vsan-cluster-ioinsight-manager' via vSAN
   service on vCenter, or accessed through MOID of 'vsan-ioinsight-manager' on
   ESXi host.
   """
   def StartIoInsight(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], runName: _typing.Optional[str], durationSec: _typing.Optional[pyVmomi.VmomiSupport.long], targetHosts: list[pyVmomi.vim.HostSystem], targetVMs: list[pyVmomi.vim.VirtualMachine]) -> pyVmomi.vim.Task:
      """
      Start ioinsight tool(s) running on the whole vSAN cluster or on the
      specified ESXi host(s) for VMs virtual disks I/O performance metrics
      monitor.
      
      Given the parameters passed-in, ioinsight tool(s) will be started
      on the ESXi host(s) to monitor and collect VMDKs I/O performance metrics of
      the specified VMs.
      Once the specified run duration has expired, ioinsight will stop running
      automatically. The collected performance metrics will be persisted in vSAN
      datastore.
      This API returns a task which is running background and performing actually
      ioinsight start operation on each host. Please wait for the task to be
      completed, and retrieve the final result - one or more
      `pyVmomi.vim.host.VsanHostIoInsightInfo` from the corresponding task
      information.
      
      Args:
          cluster: The cluster to which the ESXi host(s) belong.
              This parameter is ignored while the API is called against
              host.
          runName: Caller can specify a meaningful name for ioinsight one time
              execution, and use that name for ioinsight metrics query in
              the future.
              This parameter can be ignored while the API is called against
              host.
          durationSec: Duration in seconds for ioinsight execution.
              Once duration has expired ioinsight will stop on it's
              own. The valid range of duration is between from 60 second
              to 86400 seconds (24 hours).
              If this parameter is not provided, the API will try to
              append targetVMs to the ioinsight(s) running on
              targetHosts as new monitor targets.
          targetHosts: One or multiple ESXi hosts on which ioinsight is
              installed and going to be started.
              If this parameter is not provided, all hosts of the
              cluster will be treated as targets, and this case is only
              supported while being invoked against vCenter.
              If the API is called against host, this parameter is must
              to have and should be exactly same as the target host.
          targetVMs: One or multiple target VMs will be monitored by ioinsight.
              If this parameter is not provided, all VMs on the host
              will be treated as targets.
      
      Returns:
          Task which is performing actually ioinsight start operation in the
          background.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: If any argument passed to the API is not specified
              correctly.
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.NotFound: if no ESXi host could be contacted to perform the operation
              when this method is called against vCenter, or ioinsight
              cannot be found on host.
          pyVmomi.vim.fault.VsanFault: If any other unexpected failure happened during starting
              ioinsight.
      """
      ...
   def StopIoInsight(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], runName: _typing.Optional[str], hostsIoInsightInfos: list[pyVmomi.vim.host.VsanHostIoInsightInfo]) -> pyVmomi.vim.Task:
      """
      Stop ioinsight tool(s) running on the ESXi host(s) by given parameters
      passed-in.
      
      The collected VMDKs I/O performance metrics will be persisted in vSAN
      datastore for further query by:
      `pyVmomi.vim.cluster.VsanPerformanceManager.queryVsanPerf`.
      This API returns a task which is running background and performing actually
      ioinsight stop operation on each host. Please wait for the task to be
      completed, and retrieve the final result - one or more
      `pyVmomi.vim.host.VsanHostIoInsightInfo` from the corresponding task
      information.
      
      Args:
          cluster: The cluster to which the target ESXi host(s) belong. This
              parameter is ignored while the API is called against host.
          runName: The name of running ioinsight to be stopped. This parameter
              can be ingnored while being called against host.
          hostsIoInsightInfos: One or multiple host ioinsight(s) information, which
              indicate the target ioinsight(s) to be stopped or the
              VMs to be unmonitored.
              If `pyVmomi.vim.host.VsanIoInsightInfo.monitoredVMs`
              are specified by the parameter, the API will try to
              unmonitor the VMs from running ioinsight(s), otherwise
              it will entirely stop the specified ioinsight(s) if no
              valid runName is provided.
              If neither this parameter nor runName is provided,
              the API will try to stop ioinsight(s) on each host in
              the cluster, and this case is only supported while
              being invoked against vCenter. If the API is called
              against host, this parameter is must to have and
              `pyVmomi.vim.host.VsanHostIoInsightInfo.host` should be
              exactly same as the target host.
      
      Returns:
          Task which is performing actually ioinsight stop operation in the
          background on each host.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: If any argument passed to the function is not
              specified correctly.
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.NotFound: If no ESXi host could be contacted to perform the operation
              when this method is called against vCenter.
          pyVmomi.vim.fault.VsanFault: If the caller doesn't have the required privilege, or the
              cluster has no hosts.
      """
      ...
   def QueryIoInsightInstances(self, querySpec: VsanIoInsightInstanceQuerySpec, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> list[VsanIoInsightInstance]:
      """
      Retrieve all ioinsight instances
      `pyVmomi.vim.cluster.VsanIoInsightInstance` according to the passed in
      parameters.
      
      Args:
          querySpec: Describe specifications for the query operation.
          cluster: The target cluster where the ioinsight instances belong to.
              This parameter is ignored while the API is called against
              host.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: If any argument passed to the function is not
              specified correctly.
          pyVmomi.vmodl.fault.NotSupported: If the API is not supported by the called host.
          pyVmomi.vim.fault.VsanFault: If any other unexpected fault is encountered.
          pyVmomi.vim.fault.NotFound: If the stats primary node is not found in target cluster.
      """
      ...
   def DeleteIoInsightInstance(self, runName: str, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> None:
      """
      Delete information of a completed ioinsight instance specified by
      the passed-in runName.
      
      Args:
          runName: Run name of the ioinsight instance.
          cluster: The target cluster where the ioinsight instance belongs to.
              This parameter is ignored while the API is called against
              host.
      
      Returns:
          void
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: If any argument passed to the function is not
              specified correctly.
          pyVmomi.vmodl.fault.NotSupported: If the API is not supported by the called host.
          pyVmomi.vim.fault.NotFound: If the specified ioinsight instance is not found.
          pyVmomi.vim.fault.VsanFault: If any other unexpected fault is encountered.
      """
      ...
   def RenameIoInsightInstance(self, oldRunName: str, newRunName: str, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource]) -> None:
      """
      Rename an ioinsight instance which is completed already
      (see `pyVmomi.vim.cluster.VsanIoInsightInstanceState`).
      
      Args:
          oldRunName: The current run name of an completed ioinsight instance.
          newRunName: New run name for the completed ioinsight instance.
          cluster: The target cluster where the ioinsight instance belongs to.
              This parameter is ignored while the API is called against
              host.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: If any argument passed to the function is not
              specified correctly.
          pyVmomi.vmodl.fault.NotSupported: If the API is not supported by the called host.
          pyVmomi.vim.fault.NotFound: If the specified ioinsight instance is not found.
          pyVmomi.vim.fault.VsanFault: If any other unexpected fault is encountered.
      """
      ...


class VsanIscsiHomeObjectSpec(pyVmomi.vmodl.DynamicData):
   """
   Defines iSCSI home object specification for creating home object.
   
   Attributes:
       storagePolicy: Default storage policy for the home object, which acts as a descriptor for the targets.
           
           If it is not specified, vSAN datastore vmnamespace policy should be used by default.
       defaultConfig: iSCSI target service default configuration, the networkInterface property
           in this field is required when create home object.
   """
   storagePolicy: _typing.Optional[pyVmomi.vim.vm.ProfileSpec] = None
   defaultConfig: _typing.Optional[VsanIscsiTargetServiceDefaultConfigSpec] = None


class VsanIscsiInitiatorGroup(pyVmomi.vmodl.DynamicData):
   """
   Defines the initiator group, which serves as a container to contain a
   initiator name list.
   
   If user add one initiator group to one target, it means
   all initiators in it can access this target.  
   An initiator functions as an iSCSI client. An initiator
   negotiates with a target to establish
   connectivity to a LUN and it treats iSCSI LUNs the same way as they would a
   raw SCSI or IDE hard drive.
   
   Attributes:
       name: The initiator group name.
       initiators: The initiator name list.
       targets: The target basic information list for targets associate with this group.
   """
   name: str
   initiators: list[str] = []
   targets: list[VsanIscsiTargetBasicInfo] = []


class VsanIscsiLUNCommonInfo(pyVmomi.vmodl.DynamicData):
   """
   Specifies common properties for iSCSI LUN.
   
   Attributes:
       lunId: The optional ID of the LUN [0..255].
           
           If not provided, next free identifier will be used.
           If provided, ID must be unique within target.
       alias: An optional alias for LUN.
           
           Can be used to indicate additional info about the LUN.
       lunSize: Size of the LUN object, unit is byte.
       status: LUN status, the default value is 'Online'.
   """
   class VsanIscsiLUNStatus(pyVmomi.VmomiSupport.Enum):
      """
      Defines iSCSI LUN status, supported values are Online, Offline.
      
      Attributes:
          Online: LUN is a configuration status, which is a desired state.
              
              If LUN is online, initiators can discover the LUN after login to the target.
          Offline: LUN is a configuration status, which is a desired state.
              
              If LUN is offline, initiators can not discover the LUN after login to the target, all existing connections are closed.
      """
      Online: _typing.ClassVar['VsanIscsiLUNCommonInfo.VsanIscsiLUNStatus'] = 'Online'
      Offline: _typing.ClassVar['VsanIscsiLUNCommonInfo.VsanIscsiLUNStatus'] = 'Offline'
      VsanIscsiLUNStatus_Unknown: _typing.ClassVar['VsanIscsiLUNCommonInfo.VsanIscsiLUNStatus'] = 'VsanIscsiLUNStatus_Unknown'

   lunId: _typing.Optional[int] = None
   alias: _typing.Optional[str] = None
   lunSize: pyVmomi.VmomiSupport.long
   status: _typing.Optional[str] = None


class VsanIscsiLUN(VsanIscsiLUNCommonInfo):
   """
   Defines iSCSI LUN(Logical unit number), LUN is LU(Logical Unit) has an
   address within a target.
   
   Attributes:
       targetAlias: Target alias for the target which this LUN belongs to.
       uuid: UUID of vSAN object which is used to provide storage for this LUN.
       actualSize: Actual size of LUN used, unit is byte.
       objectInformation: Object information for vSAN Object containing this LUN.
   """
   targetAlias: str
   uuid: str
   actualSize: pyVmomi.VmomiSupport.long
   objectInformation: _typing.Optional[VsanObjectInformation] = None

class VsanIscsiLUNRuntimeStatusType:
   """Defines iSCSI LUN runtime status type for iSCSI target service."""
   pass


class VsanIscsiLUNSpec(VsanIscsiLUNCommonInfo):
   """
   Attributes:
       storagePolicy: Storage policy used by this LUN, if not set when create LUN, the default one
           defined in iSCSI service will be used.
       newLunId: The new ID of the LUN [0..255].
           
           If provided, ID must be unique within target.
   """
   storagePolicy: _typing.Optional[pyVmomi.vim.vm.ProfileSpec] = None
   newLunId: _typing.Optional[int] = None


class VsanIscsiTargetBasicInfo(pyVmomi.vmodl.DynamicData):
   """
   Specifies the basic properties for iSCSI target.
   
   Attributes:
       alias: Alias, i.e., the human readable name.
       iqn: The IQN of the target.
           
           This parameter is optional and should be unique if provided.
           If not provided, appropriate IQN will be generated by the system.
   """
   alias: str
   iqn: _typing.Optional[str] = None


class VsanIscsiTargetCommonInfo(VsanIscsiTargetBasicInfo):
   """
   Specifies the common properties for vSAN iSCSI target.
   
   Attributes:
       authSpec: Authentication information.
       port: The network port on which target is accessible.
           
           If not specified, at the same time,
           if networkInterface is also not specified, defaults to the defaultPort specified
           in iSCSI target service. If networkInterface is specified, defaults to port 3260.
           The firewall should be opened automatically for port specified by the user.
       networkInterface: Name of the VMkernel Network interface which will handle the iSCSI traffic.
           
           If
           not specified, the default one defined in iSCSI target service will be used.
       affinityLocation: The site affinity location option is only available when the cluster is
           configured into the streched cluster mode.
           
           No site affinity will be
           configured when this field is not present.
   """
   authSpec: _typing.Optional[VsanIscsiTargetAuthSpec] = None
   port: _typing.Optional[int] = None
   networkInterface: _typing.Optional[str] = None
   affinityLocation: _typing.Optional[str] = None


class VsanIscsiTarget(VsanIscsiTargetCommonInfo):
   """
   Defines iSCSI Target, which is a storage resource located on iSCSI target
   service.
   
   Attributes:
       lunCount: LUN count, it may be zero.
       objectInformation: Object information for vSAN Object containing this target.
       ioOwnerHost: I/O owner host, i.e.
           
           the mof string that represents the host.
       initiators: Associated initiator name list.
       initiatorGroups: Associated initiator group name list.
   """
   lunCount: _typing.Optional[int] = None
   objectInformation: _typing.Optional[VsanObjectInformation] = None
   ioOwnerHost: _typing.Optional[str] = None
   initiators: list[str] = []
   initiatorGroups: list[str] = []


class VsanIscsiTargetAuthSpec(pyVmomi.vmodl.DynamicData):
   """
   Authentication specification for iSCSI target.
   
   Attributes:
       authType: Authentication type.
       userNameAttachToTarget: CHAP user name for target
       userSecretAttachToTarget: CHAP user secret attach to this target
       userNameAttachToInitiator: CHAP user name attach to initiator, only set when \"CHAP mutual\"
       userSecretAttachToInitiator: CHAP user secret attach to initiator, only set when \"CHAP mutual\"
   """
   class VsanIscsiTargetAuthType(pyVmomi.VmomiSupport.Enum):
      """
      Defines iSCSI authentication type.
      
      Attributes:
          NoAuth: No authentication is used, the target can be connected by any initiator.
          CHAP: The Challenge-Handshake Authentication Protocol (CHAP), user name and secret attached to the target is needed to provide for any initiator to authenticate to this target.
          CHAP_Mutual: The Challenge-Handshake Authentication Protocol (CHAP) with Mutual option enabled, not only user name and secret attached to the target is needed to provide for any initiator to authenticate to this target, but also user name and secret attached to the initiator is needed to provide for one initiator to authenticate to any target.
      """
      NoAuth: _typing.ClassVar['VsanIscsiTargetAuthSpec.VsanIscsiTargetAuthType'] = 'NoAuth'
      CHAP: _typing.ClassVar['VsanIscsiTargetAuthSpec.VsanIscsiTargetAuthType'] = 'CHAP'
      CHAP_Mutual: _typing.ClassVar['VsanIscsiTargetAuthSpec.VsanIscsiTargetAuthType'] = 'CHAP_Mutual'
      VsanIscsiTargetAuthType_Unknown: _typing.ClassVar['VsanIscsiTargetAuthSpec.VsanIscsiTargetAuthType'] = 'VsanIscsiTargetAuthType_Unknown'

   authType: _typing.Optional[str] = None
   userNameAttachToTarget: _typing.Optional[str] = None
   userSecretAttachToTarget: _typing.Optional[str] = None
   userNameAttachToInitiator: _typing.Optional[str] = None
   userSecretAttachToInitiator: _typing.Optional[str] = None


class VsanIscsiTargetServiceConfig(pyVmomi.vmodl.DynamicData):
   """
   Specified common properties for vSAN iSCSI target service.
   
   Attributes:
       defaultConfig: vSAN iSCSI target service default configuration.
       enabled: Whether vSAN iSCSI target service is enabled.
       vipConfigs: Virtual IP (VIP) configurations.
           
           Currently,
           only 1 Virutal IP configuration is allowed.
   """
   defaultConfig: _typing.Optional[VsanIscsiTargetServiceDefaultConfigSpec] = None
   enabled: _typing.Optional[bool] = None
   vipConfigs: list[pyVmomi.vim.vsan.VipConfigSpec] = []


class VsanIscsiTargetServiceDefaultConfigSpec(pyVmomi.vmodl.DynamicData):
   """
   Specified default configuration for iSCSI target service.
   
   Attributes:
       networkInterface: Name of default VMkernel network interface which will handle the iSCSI traffic,
           can be overridden per target.
           
           The networkInterface and port need to be specified
           together when trying to update default VIT configuration.
       port: Default network port, 3260 is used here, can be overridden per target.
           
           The firewall
           should be opened automatically for port specified by the user. The port can be
           changed and need to be set together with networkInterface for default config.
       iscsiTargetAuthSpec: Default iSCSI target authentication.
           
           If not provided, the authentication with
           authType None is used here.
   """
   networkInterface: _typing.Optional[str] = None
   port: _typing.Optional[int] = None
   iscsiTargetAuthSpec: _typing.Optional[VsanIscsiTargetAuthSpec] = None

class VsanIscsiTargetServiceProcessStatus:
   """Defines iSCSI target service process status."""
   pass


class VsanIscsiTargetServiceSpec(VsanIscsiTargetServiceConfig):
   """
   Defines iSCSI target specification used when create iSCSI target.
   
   Attributes:
       homeObjectStoragePolicy: Default storage policy for the vSAN iSCSI target home object.
           
           If it is not specified, vSAN datastore vmnamespace policy should be used by default.
   """
   homeObjectStoragePolicy: _typing.Optional[pyVmomi.vim.vm.ProfileSpec] = None


class VsanIscsiTargetSpec(VsanIscsiTargetCommonInfo):
   """
   Attributes:
       storagePolicy: Storage policy used by this target.
           
           If not specified, the
           vSAN datastore vmnamespace policy should be used by default.
       newAlias: The new alias for the iSCSI target.
   """
   storagePolicy: _typing.Optional[pyVmomi.vim.vm.ProfileSpec] = None
   newAlias: _typing.Optional[str] = None


class VsanIscsiTargetSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   The VsanIscsiTargetSystem exposes interfaces from vCenter to perform
   vSAN iSCSI target service related operations.
   
   To access these APIs from vCenter, user should possess correct privileges of
   the target cluster: cluster edit privilege is required for the adding,
   editing and removal of target, LUN, initiator and initiator group, while
   system read/view privilege is required for the view of these entities.
   The Managed Entity can be accessed through MOID of
   vsan-cluster-iscsi-target-system, through vSAN service at both vCenter
   server and ESXi host side.
   """
   def QueryIscsiTargetServiceVersion(self) -> str:
      """
      Queries iSCSI service version, if version file is not found, a NotFound
      exception is raised.
      
      When it is invoked from an ESXi host on MO
      'vsan-cluster-iscsi-target-system', it just returns the iSCSI version on
      this host.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def GetHomeObject(self, cluster: pyVmomi.vim.ClusterComputeResource) -> VsanObjectInformation:
      """
      Gets the home object which stores the metadata for
      vSAN iSCSI target service.
      
      If the home object is not
      found, a VsanFault will be raised.  
      Please don't rely on this function to decide whether need
      to create the home object or not, because the home object
      may be in creation process.
      
      Args:
          cluster: : reference to cluster resource.
      
      Returns:
          VsanObjectInformation for the home object.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def GetIscsiTargets(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[VsanIscsiTarget]:
      """
      Gets iSCSI target list for one cluster.
      
        
      If the operation fails, a VsanFault will be raised.
      
      Args:
          cluster: : reference to cluster resource.
      
      Returns:
          iSCSI target list, it may be empty.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def GetIscsiTarget(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str) -> _typing.Optional[VsanIscsiTarget]:
      """
      Gets one iSCSI target.
      
        
      If the target cannot be found, a VsanFault will be raised.
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          targetAlias: : target alias.
      
      Returns:
          iSCSI target detail.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def AddIscsiTarget(self, cluster: pyVmomi.vim.ClusterComputeResource, targetSpec: VsanIscsiTargetSpec) -> _typing.Optional[pyVmomi.vim.Task]:
      """
      Adds iSCSI target to this cluster.  
      The alias in VsanIscsiTargetSpec
      must be provided and unique.
      
      If iqn provided, it should be unique, if either
      of them is not met, a VsanFault will be raised.
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          targetSpec: : reference to iSCSI target specification.
      
      Returns:
          The related task.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def EditIscsiTarget(self, cluster: pyVmomi.vim.ClusterComputeResource, targetSpec: VsanIscsiTargetSpec) -> _typing.Optional[pyVmomi.vim.Task]:
      """
      Edits iSCSI target in this cluster.  
      All properties in
      VsanIscsiTargetSpec can be changed.
      
      If authType changed, all existing
      connections are not effected, but the new connection to this target need to
      use the new authentication type, if port or network interface changed, it has
      the same impact to connection as authType change. If IQN or alias provided,
      it should be unique.  
      If IQN or alias is not unique, a VsanFault will be raised.
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          targetSpec: : reference to iSCSI target specification.
      
      Returns:
          The related task.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def RemoveIscsiTarget(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str) -> _typing.Optional[pyVmomi.vim.Task]:
      """
      Removes iSCSI target from this cluster.  
      If the target cannot be found, a VsanFault will be raised.
      
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          targetAlias: : the target alias
      
      Returns:
          The related task.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def GetIscsiLUNs(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAliases: list[str]) -> list[VsanIscsiLUN]:
      """
      Gets iSCSI LUN list for specified target list.  
      If some targets cannot be found, a VsanFault will be raised.
      
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          targetAliases: : target alias list, if not specified, all targets are
              used here.
      
      Returns:
          iSCSI LUN list, it may be empty.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def GetIscsiLUN(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str, lunId: int) -> _typing.Optional[VsanIscsiLUN]:
      """
      Gets one iSCSI LUN for specified target.  
      If the target or the LUN cannot be found, a VsanFault will be raised.
      
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          targetAlias: : the target alias.
          lunId: : the LUN id.
      
      Returns:
          iSCSI LUN.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def AddIscsiLUN(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str, lunSpec: VsanIscsiLUNSpec) -> _typing.Optional[pyVmomi.vim.Task]:
      """
      Adds iSCSI LUN to specified target.  
      If the target
      cannot be found, a VsanFault exception is raised.
      
      If the LUN
      id is provided, it should be in
      range [0, 255] and be unique in the specified target. The LUN size should be
      provided, its minimum size is 1MB, the maximum size is 62TB. If either of
      them is not met, a VsanFault will be raised.
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          targetAlias: : target alias
          lunSpec: : reference to iSCSI LUN specification.
      
      Returns:
          The related task.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def EditIscsiLUN(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str, lunSpec: VsanIscsiLUNSpec) -> _typing.Optional[pyVmomi.vim.Task]:
      """
      Edits iSCSI LUN in specified target.  
      All properties in
      `VsanIscsiLUNSpec` can be changed.
      
      If new LUN id is provided, it
      should be in range [0, 255] and be unique in the specified target, if lunSize
      is provided, it should be greater than existing size, i.e., LUNs are only
      allowed to grow, if either of them are not met, a VsanFault exception will be
      raised. If storagePolicy is provided, it is set by calling
      `SetVsanObjectPolicy` in `VsanObjectSystem`.
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          targetAlias: : iSCSI target alias.
          lunSpec: : reference to iSCSI LUN specification.
      
      Returns:
          The related task.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def RemoveIscsiLUN(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str, lunId: int) -> _typing.Optional[pyVmomi.vim.Task]:
      """
      Removes iSCSI LUN from this target.  
      If
      the target or the LUN cannot be
      found, a VsanFault will be raised.
      
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          targetAlias: : iSCSI target alias.
          lunId: : iSCSI LUN id.
      
      Returns:
          The related task.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def AddIscsiInitiatorsToTarget(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str, initiatorNames: list[str]) -> None:
      """
      Adds iSCSI initiators or initiator groups to one target.  
        
      If the target cannot be found or if there are
      initiators or initiator groups in the
      initiatorNames parameter are already associated with the specified target, a
      VsanFault will be raised.
      
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          targetAlias: : target alias.
          initiatorNames: : initiator or initiator group name list.
      
      Returns:
          void
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def RemoveIscsiInitiatorsFromTarget(self, cluster: pyVmomi.vim.ClusterComputeResource, targetAlias: str, initiatorNames: list[str]) -> None:
      """
      Removes iSCSI initiator or initiator groups from one target.  
      If the specified target cannot be found or if the initiators or initiator
      groups specified by the initiatorNames cannot be associated with the
      specified target, a VsanFault will be raised.
      
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          targetAlias: : target alias.
          initiatorNames: : initiator or initiator group name list.
      
      Returns:
          void.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def GetIscsiInitiatorGroups(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[VsanIscsiInitiatorGroup]:
      """
      Gets iSCSI initiator group list for one cluster.  
      If the operation fails, a VsanFault will be raised.
      
      Args:
          cluster: : reference to cluster resource.
      
      Returns:
          iSCSI initiator group list.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def GetIscsiInitiatorGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str) -> _typing.Optional[VsanIscsiInitiatorGroup]:
      """
      Gets one iSCSI initiator group.  
      If the initiator group doesn't exists, a VsanFault will be raised.
      
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          initiatorGroupName: : the initiator group name.
      
      Returns:
          iSCSI initiator group.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def AddIscsiInitiatorGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str) -> None:
      """
      Adds iSCSI initiator group to one cluster.  
      If the initiator group already exists, a VsanFault will be raised.
      
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          initiatorGroupName: : the iSCSI initiator group name.
      
      Returns:
          void.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def RemoveIscsiInitiatorGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str) -> None:
      """
      Removes iSCSI initiator group from one cluster.  
      If there are initiators in the group, the initiators will be
      removed at the same time.
      
      If the initiator
      group doesn't exist, a VsanFault will be raised.
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          initiatorGroupName: : the initiator group name.
      
      Returns:
          void.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def AddIscsiInitiatorsToGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str, initiatorNames: list[str]) -> None:
      """
      Adds iSCSI initiators to one initiator group.  
      If the
      initiator group doesn't exist, or some of the initiators
      are already in the specified initiator
      group, a VsanFault will be raised.
      
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          initiatorGroupName: : the initiator group name.
          initiatorNames: : the iSCSI initiator name list.
      
      Returns:
          void.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def RemoveIscsiInitiatorsFromGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str, initiatorNames: list[str]) -> None:
      """
      Removes iSCSI initiators from one initiator group.  
      If the initiator group does not exist, or some of the initiators
      are not in the specified initiator group, a VsanFault will be raised.
      
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          initiatorGroupName: : the initiator group name.
          initiatorNames: : the initiator name list.
      
      Returns:
          void.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def AddIscsiTargetToGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str, targetAlias: str) -> None:
      """
      Adds the iSCSI target to the specified initiator group.  
      If the initiator group is not found or the target is already in the
      accessible targets of the group, a VsanFault will be raised.
      
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          initiatorGroupName: : the initiator group name.
          targetAlias: : the iSCSI target alias.
      
      Returns:
          void.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def RemoveIscsiTargetFromGroup(self, cluster: pyVmomi.vim.ClusterComputeResource, initiatorGroupName: str, targetAlias: str) -> None:
      """
      Removes accessible iSCSI target from one initiator group.  
      If the initiator group is not found or the target is not in the accessible
      targets of the group, a VsanFault will be raised.
      
      Some unhealthy status of the vSAN iSCSI service can also lead to this
      VsanFault exception, e.g., the unavailability of the home object.
      
      Args:
          cluster: : reference to cluster resource.
          initiatorGroupName: : the initiator group name.
          targetAlias: : the iSCSI target alias.
      
      Returns:
          void.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def RemediateIscsiLunsRuntimeStatus(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task:
      """
      Remediates the iSCSI LUNs which runtime status are not consistent
      with configuration.  
      The remediation result will be returned after the task is finished.  
      Only if the remediation succeed for all LUNs, the task state will be
      \"success\".
      
      If the remediation fails with no exception raised, the task state will
      be \"failure\".
      If hit internal vSAN error, the task state will be \"error\" with error
      message in the fault field.
      Unhealthy status of the vSAN iSCSI service can lead to this
      vim.fault.VsanFault exception, e.g., the unavailability of the home object.
      Multiple entry of this function at the same time is not allowed.
      
      Args:
          cluster: , reference to cluster resource.
      
      Returns:
          task.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...


class VsanNetworkDiagnostics(pyVmomi.vmodl.DynamicData):
   """
   Defines the IO latency related statistics in vSAN.
   
   This object will include
   the time range these statistics are collected, the number of IOs monitored,
   and the corresponding statistics.
   
   Attributes:
       host: The Host object of the event.
       eventTypeId: The type of the event.
       severity: The severity level of the message.
       createdTime: The time the event was created.
       arguments: The event arguments associated with the event.
   """
   host: pyVmomi.vim.HostSystem
   eventTypeId: str
   severity: str
   createdTime: _datetime.datetime
   arguments: list[pyVmomi.vmodl.KeyAnyValue] = []


class VsanObjIdentityQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   The vSAN object identity query spec to specify detailed query specification
   for `pyVmomi.vim.cluster.VsanObjectSystem.queryObjectIdentities`.
   
   Attributes:
       knownSpbmProfileUuids: The UUID list for the known SPBM profile(s) on VC.
           
           This field is specific for host API. It will be
           ignored when provided to VC API call.
           If this field is set, `pyVmomi.vim.cluster.VsanObjectSystem.queryObjectIdentities`
           will not return SPBM profile name to caller to save the memory consumption.
       includeEffectiveCapacity: The flag determines if effective capacity attributes need to be included.
           
           The effective capacity attributes will not be included in the result if
           this field is unset.
   """
   knownSpbmProfileUuids: list[str] = []
   includeEffectiveCapacity: _typing.Optional[bool] = None


class VsanObjectExtAttrs(pyVmomi.vmodl.DynamicData):
   """
   Class for the extended attributes of vSAN cluster object
   
   Attributes:
       uuid: The object UUID
       objectType: The object type
       objectPath: The object path
       groupUuid: The group UUID of the object
       directoryName: The user friendly name of object
   """
   uuid: str
   objectType: _typing.Optional[str] = None
   objectPath: _typing.Optional[str] = None
   groupUuid: _typing.Optional[str] = None
   directoryName: _typing.Optional[str] = None


class VsanObjectExtraAttributes(pyVmomi.vmodl.DynamicData):
   """
   Extra attributes for vSAN objects.
   
   Attributes:
       uuid: vSAN object UUID.
       objPath: vSAN object path.
           
           e.g.
           /vmfs/volumes/vsan:52cc5b8f6c993df7-09d4123399c5b741/917e495d-166d-bfd0-34c1-020064ae18bb/hbrdisk.RDID-af365505-fed7-4b65-aa3d-7bfe764c257f.20.132464144063983.vmdk
       objClass: vSAN object class.
           
           The object class and its integer value is defined in objlib.
           The mapping relationships between value and object type are listed below.
           - 1 - OBJTYPE_CLASS_VDISK
           - 2 - OBJTYPE_CLASS_SNAPSHOT
           - 3 - OBJTYPE_CLASS_VMNAMESPACE
           - 4 - OBJTYPE_CLASS_VMSWAP
           - 5 - OBJTYPE_CLASS_GENERIC
           - 6 - OBJTYPE_CLASS_VMEM
           - 7 - OBJTYPE_CLASS_DIGEST
           - 8 - OBJTYPE_CLASS_SIDECAR
           - 9 - OBJTYPE_CLASS_HBRPERSIST
       ufn: vSAN object ufn (User friendly name).
       isHbrCfg: Whether this vSAN object is the hbrCfg (HBR CFGFILE) object.
       ownerClusterUuid: Owner cluster UUID for this object.
           
           It is only set for the VM namespace
           objects. It shows the UUID for the cluster on which this VM is
           created/registered.
   """
   uuid: str
   objPath: str
   objClass: int
   ufn: str
   isHbrCfg: bool
   ownerClusterUuid: _typing.Optional[str] = None


class VsanObjectIdentity(pyVmomi.vmodl.DynamicData):
   """
   Contains various information about the identity of a single vSAN object, including
   which type it is and any related objects, e.g.
   
   a VM.
   
   Attributes:
       uuid: The unique identifier for the object.
           
           It's vSAN UUID for the vSAN object or
           the CNS volume ID if it's CNS object deploying in vSAN direct storage.
       type: Can be one of: 'vmswap', 'vdisk', 'namespace', 'vmem', 'stats', 'other',
           'iscsiHome', 'iscsiLun', 'iscsiTarget' and 'fileShare'.
       vmInstanceUuid: Instance UUID of the VM this object belongs to
       vmNsObjectUuid: Name space object UUID of the VM this object belongs to
       vm: Reference to VM this object belongs to.
           
           If the API was executed against a
           host (even if proxied through vCenter) the VM reference will use the MoRef
           of the host, not that of vCenter. The vmInstanceUuid should be used instead
           to match to the vCenter MoRef in such cases.
       description: Description
       spbmProfileUuid: UUID of SPBM profile used for the policy of the object when it was applied to
           vSAN Object.
           
           Not set if the object doesn't use an SPBM managed policy.
       metadatas: Metadata for the object identity to describe the additional attributes
       typeExtId: The vSAN extension object type id.
           
           The extension object type will be
           created by any of persistency service building on top of vSAN
       spbmProfileName: Name of SPBM profile used for the policy of the object when it was applied to
           vSAN Object.
           
           Not set if the object doesn't use an SPBM managed policy.
   """
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
   """
   Contains various information about the identity and health of a set of vSAN objects.
   
   Attributes:
       identities: vSAN Object identities.
       health: vSAN Object health.
       spaceSummary: vSAN space usage summaries for each of vSAN object type defined
           in below enumerations:
           `pyVmomi.vim.cluster.VsanObjectSpaceSummary.VsanObjectTypeEnum`,
           `pyVmomi.vim.cluster.VsanObjectSpaceSummary.VsanObjectTypeEnum90`
       rawData: The raw Json string for objects identity and health structure.
           
           It's internal used only for performance purpose.
   """
   identities: list[VsanObjectIdentity] = []
   health: _typing.Optional[pyVmomi.vim.host.VsanObjectOverallHealth] = None
   spaceSummary: list[VsanObjectSpaceSummary] = []
   rawData: _typing.Optional[str] = None


class VsanObjectInformation(pyVmomi.vmodl.DynamicData):
   """
   Information for the vSAN object, e.g.
   
   vSAN performance DB etc.
   
   Attributes:
       directoryName: The friendly name of a namespace object.
       vsanObjectUuid: vSAN object UUID.
           
           If not set, object couldn't be found in the current
           cluster.
       vsanHealth: Health of the vSAN object, as seen by the host.
           
           The possible value is
           'inaccessible', 'reduced-availability-with-no-rebuild',
           'reduced-availability-with-no-rebuild-delay-timer',
           'reduced-availability-with-active-rebuild', 'data-move',
           'non-availability-related-reconfig', 'non-availability-related-incompliance',
           'healthy'
       policyAttributes: vSAN policy attributes used for the policy of the object.
           
           Not set if
           the object couldn't be found, or if the object is not healthy enough to
           determine its policy. Its format is key-value pair list, each key-value pair
           represents one attribute, the key is the attribute name, the value is the
           attribute value represented by string format.
       spbmProfileUuid: UUID of SPBM profile used for the policy of the object when it was applied to
           vSAN Object.
           
           Not set if the object couldn't be found, if the object is
           not healthy enough to determine its policy, or if the object doesn't use a
           SPBM managed policy.
       spbmProfileGenerationId: Generation ID of SPBM profile used for the policy of the object when it was
           applied to vSAN Object.
           
           Not set if the object couldn't be found, if
           the object is not healthy enough to determine its policy, or if the object
           doesn't use a SPBM managed policy.
       spbmComplianceResult: Describes the results of profile compliance checking for a vSAN object.
   """
   directoryName: _typing.Optional[str] = None
   vsanObjectUuid: _typing.Optional[str] = None
   vsanHealth: _typing.Optional[str] = None
   policyAttributes: list[pyVmomi.vim.KeyValue] = []
   spbmProfileUuid: _typing.Optional[str] = None
   spbmProfileGenerationId: _typing.Optional[str] = None
   spbmComplianceResult: _typing.Optional[StorageComplianceResult] = None


class VsanObjectPlacement(pyVmomi.vmodl.DynamicData):
   """
   Physical placement summary with the details for object.
   
   Within the placement summary, the object UUIDs are listed.
   The object UUIDs are the same as the object UUIDs
   in the object placement details.
   The object placement details are the physical placement
   details for the object. It contains the placement details for
   the object components and the disks.
   If the object is remote, the object placement details will
   provide the remote placement information like the remote
   datastore, remote cluster, remote VC IP, and else.
   
   Attributes:
       details: vSAN Object physical placement details.
   """
   details: list[VsanObjectPlacementDetails] = []


class VsanObjectPlacementDetails(pyVmomi.vmodl.DynamicData):
   """
   vSAN object placement details.
   
   Attributes:
       uuid: Object UUID
       type: Object type identification.
           
           For example, it can be one of \"vmswap\", \"vdisk\",
           \"namespace\", \"vmem\", \"attachedCnsVolBlock\", \"detachedCnsVolBlock\",
           or else.
       name: Object display name.
       isRemote: Flag if the object storage is configured remotely.
           
           If True, the object will be reported under the Remote Object view
           If False, the object will be reported under the Local Object view,
           neither remoteDatastoreUuid or remoteVcUuid should not exist.
       vm: Virtual machine reference.
           
           It exists if the object is backed by
           an virtual machine.
       spbmProfileUuid: UUID of SPBM profile.
           
           It is used for identifying the policy of the object
           when it was applied to vSAN Object. Not set if the
           object doesn't use an SPBM managed policy.
           Unset if this profile is unidentified, it can happen
           when the object is not in a healthy state.
       spbmProfileName: Name of SPBM profile.
           
           It is used for the policy of the object when it was
           applied to vSAN Object. Not set if the object doesn't
           use an SPBM managed policy.
           Unset if this profile is unidentified, it can happen
           when the object is not in a healthy state.
       isLocalPolicy: Flag if the SPBM policy can be identified as a local policy.
           
           Unset if this profile is unidentified.
           It can happen when the object is not in a healthy state.
       remoteDatastoreUuid: Remote vSAN datastore UUID.
           
           It exists only when the object is from remote vSAN datastore.
       remoteDatastoreName: Remote vSAN datastore name.
           
           It exists only when the object is from remote vSAN datastore.
       remoteCluster: Remote vSAN cluster reference.
           
           It exists only when the object is from remote vSAN cluster.
       remoteClusterName: Remote vSAN cluster name.
           
           It exists only when the object is from remote vSAN cluster.
       remoteVc: Remote VC identification.
           
           It exists only when the object is mounted from a remote VC.
           This information is determined from the remote datastore source
           `pyVmomi.vim.vsan.HciMeshDatastoreSource` when registering
           by `pyVmomi.vim.cluster.VsanRemoteDatastoreSystem.createDatastoreSource`
           or vSphere UI.
       healthState: The object health state.
           
           This variable will be one of the enums pre-defined in
           vim.host.VsanObjectHealth.VsanObjectHealthState.
           Unset if the object health state can not be identified.
       components: Component placement details.
           
           Unset if the object placement details can not be identified.
   """
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
   """
   Specification for querying vSAN object information.
   
   Attributes:
       uuid: vSAN object UUID.
       spbmProfileGenerationId: Current storage profile generation id for the profile used by vSAN
           object, it should be retrieved from SPBM service.
           
           If vSAN object
           doesn't use a storage profile in SPBM service, the generation id should be
           null. It is used to compare with the generation id of the profile at the time
           the profile was applied the to vSAN object, if they are not the same,
           it means the profile used by the vSAN object is out of date.
   """
   uuid: str
   spbmProfileGenerationId: _typing.Optional[str] = None


class VsanObjectSpaceSummary(pyVmomi.vmodl.DynamicData):
   """
   Describe the vSAN space usage aggregation by the object type
   defined in VsanObjectTypeEnum.
   
   There are multiple ways to breakdown
   the space usage of an object. One breakdown is about understanding
   the vSAN replication overhead, by separating user data, permanent
   overhead for failure tolerance and temporary overhead. A second breakdown
   is understanding how much data is physically written into disk and
   how much space is reserved and over-reserved for the vSAN object
   so that we can know the potentially wasted space due to object reservation.
   
   Attributes:
       objType: The vSAN object type.
           
           It could be one of types defined in below enumerations:
           `pyVmomi.vim.cluster.VsanObjectSpaceSummary.VsanObjectTypeEnum`,
           `pyVmomi.vim.cluster.VsanObjectSpaceSummary.VsanObjectTypeEnum90`
       overheadB: The overhead for this type of vSAN object in byte.
           
           The overhead
           includes the space like replica data, witness metadata and RAID 5/6 parity
           data etc. The sum of overhead, temporary overhead
           and the primary data size will equal to the object total used size
       temporaryOverheadB: The temporary overhead for this type of vSAN object in byte.
           
           The temporary overhead include the space like used for data moving
           and will be released eventually.
       primaryCapacityB: The primary capacity for this type of vSAN object in byte.
           
           The primary data is the actual user data written into physical
           disk which doesn't include any overhead, e.g. temporary overhead
           or replica data.
       provisionCapacityB: The total provisioned capacity for this type of vSAN object in byte.
           
           It's the total
           user requested logical capacity from the vSAN data store
       reservedCapacityB: The total reserved capacity for this type of vSAN object in byte.
           
           When user create
           the virtual disk from vSAN datastore, he/she can specify how many physical space
           should be reserved for the virtual disk through disk provisioning policy or legacy
           thick provisioning.
       overReservedB: The total over reserved capacity for this type of vSAN object in byte.
           
           It indicates
           how much capacity is over-reserved between the total reserved capacity and the actual
           user data written into disk. In other words, such space is potentially wasted, and
           reducing the reservation would free up space.
       physicalUsedB: The total of physically used capacity for this type of vSAN object in byte.
           
           It indicates how much data are written into the physical disk.
       usedB: The total of used capacity for this type of vSAN object in byte.
           
           It's the max
           value between physically used capacity and the reserved capacity.
       objTypeExt: Extended type for extension object to identify different extension volume
       objTypeExtDesc: Description of extended type for extension object
       snapshotUsedB: The physical storage consumed by vSAN snapshots.
   """
   class VsanObjectTypeEnum(pyVmomi.VmomiSupport.Enum):
      """
      Defines the possible types for the vSAN objects in 8.x and previous
      releases.
      
      Attributes:
          vmswap: The VM swap files.
          vdisk: The virtual disks.
          namespace: The VM home objects.
          vmem: The VM snapshot memory files.
          statsdb: The vSAN performance management objects.
          iscsiTarget: The vSAN iSCSI home and target objects.
          iscsiLun: The vSAN iSCSI LUNs.
          other: Other vSAN objects.
          fileSystemOverhead: vSAN File system overhead.
          dedupOverhead: Deduplication and compression overhead.
          checksumOverhead: Checksum overhead.
          improvedVirtualDisk: First Class Disks.
      """
      vmswap: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'vmswap'
      vdisk: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'vdisk'
      namespace: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'namespace'
      vmem: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'vmem'
      statsdb: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'statsdb'
      iscsiTarget: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'iscsiTarget'
      iscsiLun: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'iscsiLun'
      other: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'other'
      fileSystemOverhead: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'fileSystemOverhead'
      dedupOverhead: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'dedupOverhead'
      spaceUnderDedupConsideration: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'spaceUnderDedupConsideration'
      checksumOverhead: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'checksumOverhead'
      improvedVirtualDisk: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'improvedVirtualDisk'
      transientSpace: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'transientSpace'
      slackSpaceCapRequiredForHost: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'slackSpaceCapRequiredForHost'
      resynPauseThresholdForHost: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'resynPauseThresholdForHost'
      minSpaceRequiredForVsanOp: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'minSpaceRequiredForVsanOp'
      hostRebuildCapacity: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'hostRebuildCapacity'
      physicalTransientSpace: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'physicalTransientSpace'
      haMetadataObject: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'haMetadataObject'
      fileServiceRoot: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'fileServiceRoot'
      attachedCnsVolBlock: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'attachedCnsVolBlock'
      detachedCnsVolBlock: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'detachedCnsVolBlock'
      attachedCnsVolFile: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'attachedCnsVolFile'
      detachedCnsVolFile: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'detachedCnsVolFile'
      cnsVolFile: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'cnsVolFile'
      fileShare: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'fileShare'
      extension: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'extension'
      hbrDisk: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'hbrDisk'
      hbrCfg: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'hbrCfg'
      hbrPersist: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'hbrPersist'
      traceobject: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'traceobject'
      esaObjectOverhead: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'esaObjectOverhead'
      pgNamespace: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'pgNamespace'
      clusterDBNamespace: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'clusterDBNamespace'
      aggregatedSystemObjects: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'aggregatedSystemObjects'
      nativeObjectStore: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'nativeObjectStore'
      VsanObjectTypeEnum_Unknown: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum'] = 'VsanObjectTypeEnum_Unknown'

   class VsanObjectTypeEnum90(pyVmomi.VmomiSupport.Enum):
      """Defines the possible types for the vSAN objects in 9.0 release."""
      dedupSharedUserData: _typing.ClassVar['VsanObjectSpaceSummary.VsanObjectTypeEnum90'] = 'dedupSharedUserData'

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
   """
   This managed object type provides the service interface for setting the
   storage policy to one vSAN object, querying the vSAN object
   status information, i.e., its storage profile, its health status.  
   When the ManagedEntity is accessed with MOID of 'vsan-cluster-object-system'
   through vSAN service at vCenter server and ESXi host side, it acts as
   cluster-level APIs.
   
   When it accessed with MOID of 'vsan-object-system' through vSAN service
   at ESXi host side, its scope is only limited to that host.
   """
   def SetVsanObjectPolicy(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], vsanObjectUuid: str, profile: _typing.Optional[pyVmomi.vim.vm.ProfileSpec]) -> bool:
      """
      Set the policy of the vSAN object.
      
      The cluster parameters is ignored if called on ESX.  
      Profile can be 3 formats:  
      1\\. `VirtualMachineEmptyProfileSpec` means to use the empty vSAN
      policy. This is not the default policy, but a policy where all fields
      have default values.  
      2\\. `VirtualMachineDefinedProfileSpec` where profileId is set, in
      which case this profileId will be looked up in SPBM for the detailed
      policy information.  
      3\\. `VirtualMachineDefinedProfileSpec` where profileId is an empty
      string and instead the profileData is set for extensionKey
      'com.vmware.vim.sps'. In this case the objectData field can be either the
      vSAN expression format, or a SPBM XML string. If no profile is
      supplied, and the call is executed against vCenter, then SPBM will be
      consulted for the vSAN datastore's default profile.  
      When this method returns successfully, the profile has been applied, but
      vSAN may still be remediating in order to implement the new policy.
      The health state of the object and resync information should be monitored to
      check on the progress.  
      Only the third option for profile is available when called on ESXi, other
      formats will raise InvalidArgument exception. If SPBM needs to be contacted,
      but SPBM is not available, RuntimeFault exception will be raised. If the
      profileId can not be resolved with SPBM, InvalidArgument exception will be
      raised. If objectData was provided but is neither of the two supported
      formats, InvalidArgument exception will be raised. If the vSAN object
      can not be found, FileNotFound exception will be raised. If the vSAN
      object failed to set the policy, e.g. because it is not accessible,
      FileNotWritable exception will be raised. If called against vCenter, but no
      ESXi host could be contacted to perform the operation, the exception is
      logged and the False is returned by this method.
      NOTE: This API requires additional Global.Settings privilege if called
      against vSphere 65P02 release.
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
          vsanObjectUuid: vSAN object UUID.
          profile: See above description for all possible options.
      
      Returns:
          True when the operation successfully, False when it is failed and
          there is no exception raised.
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
          pyVmomi.vim.fault.FileNotFound: This fault is thrown when an operation fails because the specified file
              does not exist.
          pyVmomi.vim.fault.FileNotWritable: Thrown if an attempt is made to write to a read-only file.
      """
      ...
   def QueryVsanObjectInformation(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], vsanObjectQuerySpecs: list[VsanObjectQuerySpec]) -> list[VsanObjectInformation]:
      """
      Get information about the vSAN object/directory.
      
        
      If it's called in VC, the spbmProfileGenerationId can be safely ignored in
      vim.cluster.VsanObjectQuerySpec, it will be automatically set to the correct
      value by using SPBM service. If it's called in host with MOID
      'vsan-object-system', both fields in
      `pyVmomi.vim.cluster.VsanObjectQuerySpec` should be provided, if
      spbmProfileGenerationId is not provided, the one from vSAN CMMDS will
      be used here, as a result, the mismatch field for storage compliance result
      is not reliable in some cases, e.g. profile is updated or deleted in vCenter
      after the vSAN object creation. If it's called in host with MOID
      'vsan-cluster-object-system', the spbmProfileGenerationId in
      `pyVmomi.vim.cluster.VsanObjectQuerySpec` would be ignored and mismatch field
      is not reliable. Note this API can query maximum 500 vSAN objects
      at once when it's called from ESXi host for performance consideration,
      otherwise, the `pyVmomi.vmodl.fault.InvalidArgument` exception will
      be thrown.
        
      If the vSAN object can not be found,
      `pyVmomi.vim.fault.FileNotFound` exception will be
      raised. If the vSAN object failed to read the policy, e.g. because it
      is not accessible, FileNotReadable exception will be raised.
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
          vsanObjectQuerySpecs: vSAN object query spec list.
      
      Returns:
          Object information list.
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.FileNotFound: This fault is thrown when an operation fails because the specified file
              does not exist.
          pyVmomi.vim.fault.FileNotWritable: Thrown if an attempt is made to write to a read-only file.
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
      """
      ...
   def QueryObjectIdentities(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], objUuids: list[str], objTypes: list[str], includeHealth: _typing.Optional[bool], includeObjIdentity: _typing.Optional[bool], includeSpaceSummary: _typing.Optional[bool], extraQuerySpec: _typing.Optional[VsanObjIdentityQuerySpec]) -> _typing.Optional[VsanObjectIdentityAndHealth]:
      """
      Map from vSAN object UUIDs to their identities.
      
      The results contain the identities of all objects that could be resolved. The
      identity includes things like the object type, references to the VM the object
      belongs to and such. If called against a host with MOID 'vsan-object-system',
      the cluster argument is ignored and, only those objects are resolved which
      can be resolved by that host. For VM related objects a host can only resolve
      the objects if the VM they belong to is registered on that host.
      If called against a host with MOID 'vsan-cluster-object-system', the cluster
      argument is ignored and cluster wide object identities would be returned
      except template VM, and in identities, the VM property would be left unset.
      If called against vCenter, all connected hosts will be contacted for
      this information and the results will be aggregated. Any VMs registered with
      hosts which are disconnected will hence not be resolved.
      It's not recommended to use this API to get all of vSAN object identities
      at once to avoid potential performance issue due to large response in large
      scale cluster. Instead, we should limit the output by specifying various
      filter parameters like the objects UUID, object type, only including
      health or identity result etc.
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
          objUuids: The vSAN object UUIDs for querying. Unset to query
              all of vSAN objects
          objTypes: Querying the vSAN objects with given types, only the object whose
              type in this list will be returned. All of available object types
              include 'vmswap', 'vdisk', 'namespace', 'vmem', 'stats', 'other',
              'iscsiHome', 'iscsiLun', 'iscsiTarget' and 'fileShare'.
              Unset to query all of vSAN objects with any type
          includeHealth: If the result includes the object health status.
              Default is False
          includeObjIdentity: If the result includes all of the object identity.
              Default is True if it's unset
          includeSpaceSummary: If the result includes the vSAN space consumption
              summarizing by object type. Currently, it's not
              supported to include both of space summary and
              object identity in the result. Default is false.
          extraQuerySpec: This parameter only takes effect for host level API.
              The vSAN object identity query spec to specify
              detailed query specification like remote vSAN or VMFS
              datastores. If no extraQquerySpec is specified, the
              original logic to return all identities of local vSAN
              datastores will be applied. Note for any nonlocal
              vsan datastores provided, all the specified filter like
              objUuids, objTypes, include* won't take affect.
      
      Returns:
          Object information structure
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def DeleteObjects(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], objUuids: list[str], force: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      Delete vSAN Objects on vSAN cluster.
      
      When the 'cluster' parameter is
      specified, this is a cluster level asynchronous API. The delete operation
      will return a task result which tracks progress, please check the task
      state when use.
      When it's called against host, it's a host level asynchronous API, which
      deprecates the 'DeleteVsanObjects' in `pyVmomi.vim.host.VsanInternalSystem`.
      WARNING: This API can be slow because we do IOs to all the objects.
      This API can be used to delete vSAN objects. vSAN won't allow access to
      objects which have lost quorum. Such objects can be deleted with the
      optional \"force\" flag.
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
          objUuids: The vSAN object UUIDs to delete.
          force: The force flag, inaccessible objects can't be deleted without
              this flag. WARNING: it's at your own risk.
      
      Returns:
          vim.Task
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
      """
      ...
   def QueryInaccessibleVmSwapObjects(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[str]:
      """
      Query all inaccessible vmswap objects on a vSAN cluster.
      
      It works on
      both cluster level and host level.
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
      
      Returns:
          list of inaccessible vmswap objects.
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
      """
      ...
   def QuerySyncingVsanObjectsSummary(self, cluster: pyVmomi.vim.ComputeResource, syncingObjectFilter: _typing.Optional[VsanSyncingObjectFilter]) -> pyVmomi.vim.vsan.host.VsanSyncingObjectQueryResult:
      """
      Query summary information about the syncing objects in this cluster.
      
      It will retrieve information about syncing objects based on object
      filter options.
      
      Args:
          cluster: vSAN cluster.
          syncingObjectFilter: Filter spec for summary.
      
      Returns:
          result VsanSyncingObjectQueryResult.
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
      """
      ...
   def RelayoutObjects(self, cluster: pyVmomi.vim.ComputeResource) -> pyVmomi.vim.Task:
      """
      The re-layout task for the objects which need change in object format.
      
      This
      may involve physical on-disk re-layout of objects which will cause data
      movement in the cluster. Objects in the old format might not be able to use
      some of the new features.
      
      Returns:
          The task object which represents the vSan
          RelayoutObjects task.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def QueryPhysicalPlacements(self, cluster: pyVmomi.vim.ComputeResource, specs: _typing.Optional[VsanQueryPhysicalPlacementSpecs]) -> list[VsanObjectPlacement]:
      """
      Retrieves the physical disk placement detail for the backing
      vSAN objects from the specified entities like virtual machine.
      
      This method provides detailed information about the physical
      placement of vSAN objects deployed on the specified cluster.
      The results include:
      \\- Object details.
      \\- Component structures.
      \\- Disk placement details.
      All the given object specs registered within this cluster will be
      retrieved.
      This API supports the object query mounted from remote datastores.
      Calling this API from host level is not supported. If the cluster
      argument is ignored or the object query specs are empty, the API
      will return an empty result.
      Currently, this API only supports single virtual machine.
      
      Args:
          cluster: The vSAN cluster. This parameter is only applicable for
              cluster-level API calls.
          specs: The query specifications for the objects. Multiple object
              specifications are supported. If unset, the method will
              return an empty result.
      
      Returns:
          An list containing the physical placement information for the
          specified entities like virtual machine.
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: If run directly on an ESX Server host.
          pyVmomi.vim.fault.VsanFault: If run with some faults found. E.g. the VM count of the given specs exceeds the limit, and other faults like no datastore properties found in the given cluster. Details can be found in VsanFault message.
      """
      ...


class VsanPerfDiagnoseQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   This data object specifies the query parameters for the vSAN Performance
   diagnostic query.
   
   Attributes:
       startTime: The start time of the period for which the cluster performance will be
           diagnosed.
           
           This parameter must be specified.
       endTime: The end time of the period for which the cluster performance will be
           diagnosed.
           
           This parameter must be specified.
       queryType: The query type for which the cluster performance will be diagnosed.
       context: Any additional context that can be supplied as a hint to the diagnosis.
           
           As an example, if for HCIBench workloads, the string 'HCIBench' can be
           supplied here.
   """
   startTime: _datetime.datetime
   endTime: _datetime.datetime
   queryType: str
   context: _typing.Optional[str] = None


class VsanPerfDiagnosticException(pyVmomi.vmodl.DynamicData):
   """
   This data object contains details of the performance exception.
   
   Attributes:
       exceptionId: The exception id which is an unique identifier for this exception.
       exceptionMessage: A brief message about the exception.
       exceptionDetails: A detailed description about this exception.
       exceptionUrl: A reference/link (such as a KB article), which has more details on how this
           performance exception can be addressed.
   """
   exceptionId: str
   exceptionMessage: str
   exceptionDetails: str
   exceptionUrl: str

class VsanPerfDiagnosticQueryType:
   """
   The query type indicating the goal of the vSAN performance diagnostic
   query, with the following values.
   """
   pass


class VsanPerfDiagnosticResult(pyVmomi.vmodl.DynamicData):
   """
   This data object type stores a performance diagnostic exception,
   relevant performance data, with a goal to
   help root cause a performance issue in a vSAN cluster.
   
   A performance diagnostic exception points to a possible
   reason due to which the vSAN cluster may be seeing poorer performance
   during the queried time interval. We raise an independent performance
   diagnostic exception for each issue that we find, and do _not_ group
   similar types of performance exceptions currently. It is left to the user
   (such as the UI), to do the grouping.
   
   Attributes:
       exceptionId: The exception Id identifying a cause of poor performance.
           
           Use
           GetSupportedDiagnosticExceptions to get more details for the particular
           exceptionId
       recommendation: The recommendation message explaining what can be done to avoid this
           performance exception.
       aggregationFunction: In case an aggregation is applied to raw performance service data, this
           field denotes the aggregation function.
           
           Examples are: spread, max, min,
           sum, compare, etc. If an aggregation is not applied, this field is empty.
       aggregationData: A time series data that identifies the result of the aggregation applied to
           raw data returned by performance service.
           
           When this field is empty, it
           implies that no aggregation operation was performed for this exception.
           The entityRefId captures the unique entity type being aggregated.
           This could either be a single entity type, such as, capacity-disk, or it
           could be denoting a comparison between two entities, such as,
           cluster-domclient/diskgroup. The value field (VsanPerfMetricSeriesCSV) will
           contain the unique metricIds for which the aggregation is computed. Just like
           entityRefId, this could be a single metric, e.g. latencyRead, or a comparison between
           two metrics, such as throughputRead/iopsRead. The values field will contain the
           result of the aggregation operation in CSV.
       exceptionData: An array of time series data that identifies why this performance exception
           was raised.
           
           When this array has multiple elements, aggregatedFunction will
           identify the aggregation function applied on the raw data to get the end result
           which identifies a performance exception. Each time series is of type
           VsanPerfEntityMetricCSV and is an independent cause of the performance exception.
           The entityRefId in VsanPerfEntityMetricCSV would refer to an entity type which is
           limiting performance, such as, a diskgroup. The values in VsanPerfEntityMetricCSV
           (VsanPerfMetricSeriesCSV) contain the metricId for which the exception was
           raised, and the values corresponding to the queried time.
   """
   exceptionId: str
   recommendation: _typing.Optional[str] = None
   aggregationFunction: _typing.Optional[str] = None
   aggregationData: _typing.Optional[VsanPerfEntityMetricCSV] = None
   exceptionData: list[VsanPerfEntityMetricCSV] = []


class VsanPerfEntityMetricCSV(pyVmomi.vmodl.DynamicData):
   """
   This data object type stores values and metadata for vSAN metrics associated
   with a specific entity.
   
   Attributes:
       entityRefId: The entity reference id in format <type>:<id> like managed object reference.
           
           For supported entity types, metric groups, metrics,
           see `pyVmomi.vim.cluster.VsanPerformanceManager.queryVsanPerf`
       sampleInfo: The SampleInfo (timestamp,interval) encoded in the following CSV
           format: [date1], [date2], and so on.
       value: A list of values that corresponds to the samples collected.
   """
   entityRefId: str
   sampleInfo: _typing.Optional[str] = None
   value: list[VsanPerfMetricSeriesCSV] = []


class VsanPerfEntityType(pyVmomi.vmodl.DynamicData):
   """
   See `pyVmomi.vim.cluster.VsanPerformanceManager.getSupportedEntityTypes`
   
   Attributes:
       name: The entity type name.
           
           It is used to compose the entity reference id, which is
           <entity_type_name>:<entity_uuid>  
           For an example: host-domclient:<hostUuid> is used to identify a vSAN
           host for querying stats in vSAN clients consumption viewpoint.
       id: Id for the entity type.
       graphs: The supported metrics (organized by graphs) for this entity type
       description: The description of the entity type.
       advancedGraphs: The advanced supported metrics (organized by graphs) for this entity type,
           these graphs will be shown in performance for support page.
       verboseGraphs: The verbose supported metrics (organized by graphs) for this entity type,
           these graphs will be shown in performance for support detail page.
       hotspotGraphs: The hotspot supported metrics (organized by graphs) for this entity type,
           these graphs will be shown in performance top contributors page.
   """
   name: str
   id: str
   graphs: list[VsanPerfGraph] = []
   description: _typing.Optional[str] = None
   advancedGraphs: list[VsanPerfGraph] = []
   verboseGraphs: list[VsanPerfGraph] = []
   hotspotGraphs: list[VsanPerfGraph] = []


class VsanPerfGraph(pyVmomi.vmodl.DynamicData):
   """
   see `pyVmomi.vim.cluster.VsanPerformanceManager.getSupportedEntityTypes`
   
   Attributes:
       id: Graph ID (i.e.
           
           In the vSphere web client, this is used as a ID for composing
           the AskVmware link, for example:
           http://www.vmware.com/esx/support/askvmware/index.php?eventtype=<id>&language=en_US).
       metrics: The metrics to display in the graph.
       unit: The unit for metrics in the graph.
       threshold: The threshold in the graph
       name: The display name of the graph.
       description: The description of the graph.
       secondGraph: The second y-axis support.
   """
   class VsanPerfStatsUnitType(pyVmomi.VmomiSupport.Enum):
      """
      Stats unit types indicate the unit display for UI
      Valid types are:
      
      Attributes:
          number: a number (int) without unit, like IOPS.
          time_ms: a time unit (int) measured by milliseconds.
          percentage: a number (int) between 0 and 100, representing the percentage.
          size_bytes: a unit for the size measured by bytes.
          rate_bytes: a rate unit for bytes per second.
          permille: a number (int) between 0 and 1000, representing the permille.
      """
      number: _typing.ClassVar['VsanPerfGraph.VsanPerfStatsUnitType'] = 'number'
      time_ms: _typing.ClassVar['VsanPerfGraph.VsanPerfStatsUnitType'] = 'time_ms'
      percentage: _typing.ClassVar['VsanPerfGraph.VsanPerfStatsUnitType'] = 'percentage'
      size_bytes: _typing.ClassVar['VsanPerfGraph.VsanPerfStatsUnitType'] = 'size_bytes'
      rate_bytes: _typing.ClassVar['VsanPerfGraph.VsanPerfStatsUnitType'] = 'rate_bytes'
      permille: _typing.ClassVar['VsanPerfGraph.VsanPerfStatsUnitType'] = 'permille'
      time_s: _typing.ClassVar['VsanPerfGraph.VsanPerfStatsUnitType'] = 'time_s'
      time_us: _typing.ClassVar['VsanPerfGraph.VsanPerfStatsUnitType'] = 'time_us'
      time_ns: _typing.ClassVar['VsanPerfGraph.VsanPerfStatsUnitType'] = 'time_ns'
      VsanPerfStatsUnitType_Unknown: _typing.ClassVar['VsanPerfGraph.VsanPerfStatsUnitType'] = 'VsanPerfStatsUnitType_Unknown'

   id: str
   metrics: list[VsanPerfMetricId] = []
   unit: str
   threshold: _typing.Optional[VsanPerfThreshold] = None
   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   secondGraph: _typing.Optional[VsanPerfGraph] = None


class VsanPerfHotspotEntitiesMetrics(pyVmomi.vmodl.DynamicData):
   """
   This data object type stores values and metadata for vSAN metrics associated
   with a specific entity.
   
   Attributes:
       entityRefId: The entity reference id in format <type>:<id> like managed object reference.
           
           For supported entity types, metric groups, metrics,
           see `pyVmomi.vim.cluster.VsanPerformanceManager.queryVsanPerf`.
       startTime: The start time of the hotspot entities query.
       endTime: The end time of the hotspot entities query.
       metricsValue: The queried metrics value of the hotspot entities.
   """
   entityRefId: str
   startTime: _datetime.datetime
   endTime: _datetime.datetime
   metricsValue: list[VsanPerfMetricSeriesCSV] = []


class VsanPerfHotspotEntityType(pyVmomi.vmodl.DynamicData):
   """
   See `pyVmomi.vim.cluster.VsanPerformanceManager.getSupportedHotspotEntityTypes`
   
   Attributes:
       name: The supported hotspot query entity type.
       id: ID for the entity type, this field is for localization.
       sortingMetrics: The sorting metrics when querying the hotspot entities.
       originalEntityTypes: The original entity types to query all raw metrics which are aggregated (e.g., average)
           to identify hotspot entities.
       description: The description of the hotspot entity type.
   """
   name: str
   id: str
   sortingMetrics: list[VsanPerfMetricId] = []
   originalEntityTypes: list[str] = []
   description: _typing.Optional[str] = None


class VsanPerfHotspotQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   Describes specification for the query operation to retrieve vSAN performance
   hotspot entities.
   
   Attributes:
       startTime: Indicates the start time of the time period to return the desired vSAN performance
           hostspot entities.
       endTime: Indicates the end time of the time period to return the desired vSAN performance
           hotspot entities.
       entity: Represents the managed object type of the top entities,
           they are: virtual-machine, disk-group, host-domclient, host-domcompmgr
           and vsan-esa-disk-layer.
           
           for detailed info, see `pyVmomi.vim.cluster.VsanPerformanceManager.queryVsanPerf`
       metricId: Indicates which one metric is used to decide the order of the hotspot entities
           from resource consuming perspective.
           
           The valid metric types for top entities query of entities virtual-machine,
           disk-group, host-domclient and host-domcompmgr include iopsRead, iopsWrite,
           throughputRead, throughputWrite, latencyRead, latencyWrite.
           The valid metric types of entity vsan-esa-disk-layer include iopsReadCapacity, iopsWriteCapacity,
           tputReadCapacity, tputWriteCapacity, avgLatReadCapacity, avgLatWriteCapacity
       numEntities: Represents the number of the hotspot entities to be returned.
           
           The default value is 10 and the maximum is 64.
   """
   startTime: _datetime.datetime
   endTime: _datetime.datetime
   entity: str
   metricId: str
   numEntities: _typing.Optional[int] = None


class VsanPerfMasterInformation(pyVmomi.vmodl.DynamicData):
   """
   vSAN Performance Service information specific to Master nodes.
   
   Attributes:
       secSinceLastStatsWrite: Seconds since last time we successfully wrote stats to the DB.
           
           If larger than 2
           intervals, we definitely have an issue. If not set, means there was never a successful
           stats write on this master.
       secSinceLastStatsCollect: Seconds since last time we successfully collected stats from the cluster.
           
           If larger
           than 2 intervals, we definitely have an issue. If not set, means there was never a
           successful stats collection on this master.
       statsIntervalSec: Configured stats collection interval, in seconds.
       collectionFailureHostUuids: vSAN UUIDs of hosts that we failed to collect stats for in last successful stats
           collection.
       renamedStatsDirectories: Names of directories which are likely renamed previously used vSAN stats DB objects.
           
           Renames can occur if two stats DB objects (hence with the same name) were to exist
           in the same cluster, e.g. after a cluster merge.
       statsDirectoryPercentFree: Percentage of free space in the vSAN stats DB object.
           
           The object is of fixed
           size. This number represents the logical free space, i.e., it is possible
           that the overall datastore or underlying physical disks are out of space
           without this metric showing a low free percentage.
       verboseMode: Verbose mode By default, performance service run with verbose mode disabled.
           
           It only collects the statistics in the 'always collect' categories. Users can
           configure performance via API or vSphere Web Client to enable/disable
           verbose mode.
           In verbose mode, performance service collects extra stats for support cases.
           The verbose mode is a vSAN cluster level configuration item, which is pushed
           to each host in vSAN clusters.
       verboseModeLastUpdate: Verbose mode last update time.
   """
   secSinceLastStatsWrite: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   secSinceLastStatsCollect: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   statsIntervalSec: pyVmomi.VmomiSupport.long
   collectionFailureHostUuids: list[str] = []
   renamedStatsDirectories: list[str] = []
   statsDirectoryPercentFree: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   verboseMode: _typing.Optional[bool] = None
   verboseModeLastUpdate: _typing.Optional[_datetime.datetime] = None


class VsanPerfMemberInfo(pyVmomi.vmodl.DynamicData):
   """
   Information about a cluster member, like its SSL certificate thumbprint.
   
   Attributes:
       thumbprint: SSL certificate thumbprint (SHA1 hash of binary certificate string)
       thumbprintList: A list of SSL certificate thumbprints with supported secure hashing
           algorithms.
           
           See `pyVmomi.vim.vm.CertThumbprint`
       memberUuid: UUID of the cluster member.
       isSupportUnicast: vSAN software format version of the cluster member.
       unicastAddressInfos: Unicast configuration of the cluster member.
       hostname: The hostname of the cluster member.
   """
   thumbprint: str
   thumbprintList: list[pyVmomi.vim.vm.CertThumbprint] = []
   memberUuid: _typing.Optional[str] = None
   isSupportUnicast: _typing.Optional[bool] = None
   unicastAddressInfos: list[VsanUnicastAddressInfo] = []
   hostname: _typing.Optional[str] = None


class VsanPerfMetricId(pyVmomi.vmodl.DynamicData):
   """
   A metric is used identify the stats of an entity.
   
   i.e., IOPS, Throughput, Latency
   
   Attributes:
       label: This is an identification label of a performance metric - VsanPerfMetricId
           (i.e., 'iopsRead', 'iopsWrite').
           
           It is unique for a type of monitored
           entities like VMs, but not unique among different types of entities. For
           example both VM and disk entities have 'iopsRead' metric label. All
           performance statistics are represented using performance metrics. It is a
           basic element used in perforamnce stats querying and performance stats
           presentation. When querying stats of an entity, you can use metric
           labels to specify what kind of metrics you want in the query spec
           (see `pyVmomi.vim.cluster.VsanPerfQuerySpec.labels`). In performance stats query
           results, metric labels are also used to identify stats data for different
           metrics (used in VsanPerfMetricId). You can get all supported metrics of an
           entity using the API of
           `pyVmomi.vim.cluster.VsanPerformanceManager.getSupportedEntityTypes`.
       group: The group label of the performance metric.
           
           i.e., Metric groups include \"domclient\", \"domowner\", \"domcompmgr\".
       rollupType: Unused field.
       statsType: Unused field.
       name: The display name of a performance metric
       description: The description a performance metric
       metricsCollectInterval: Metrics collect interval value from the vSAN performance configuration.
   """
   class VsanPerfSummaryType(pyVmomi.VmomiSupport.Enum):
      """
      Stats summarization types indicate how multiple samples of a specific metric
      are transformed or aggregated into a single statistical value.
      
      Valid types are:
      
      Attributes:
          average: The actual value collected or the average of all values collected during the summary period.
          maximum: The maximum value of the performance metric value over the summarization period.
          minimum: The minimum value of the performance metric value over the summarization period.
          latest: The most recent value of the performance metric over the summarization period.
          summation: The sum of all the values of the performance metric over the summarization period.
          none: The counter is never rolled up.
      """
      average: _typing.ClassVar['VsanPerfMetricId.VsanPerfSummaryType'] = 'average'
      maximum: _typing.ClassVar['VsanPerfMetricId.VsanPerfSummaryType'] = 'maximum'
      minimum: _typing.ClassVar['VsanPerfMetricId.VsanPerfSummaryType'] = 'minimum'
      latest: _typing.ClassVar['VsanPerfMetricId.VsanPerfSummaryType'] = 'latest'
      summation: _typing.ClassVar['VsanPerfMetricId.VsanPerfSummaryType'] = 'summation'
      none: _typing.ClassVar['VsanPerfMetricId.VsanPerfSummaryType'] = 'none'
      VsanPerfSummaryType_Unknown: _typing.ClassVar['VsanPerfMetricId.VsanPerfSummaryType'] = 'VsanPerfSummaryType_Unknown'

   class VsanPerfStatsType(pyVmomi.VmomiSupport.Enum):
      """
      The type of statistical measurement that a metric value represents.
      
      Valid types are:
      
      Attributes:
          absolute: Represents an actual value, level, or state of the counter.
              
              For example, the capacity metric represents the actual configured size of the specified disk. In other words, number of samples, samplingPeriod, and intervals have no bearing on an absolute metric value.
          delta: Represents an amount of change for the metric during the sampling period as compared to the previous interval.
          rate: Represents a value that has been normalized over the sampling period, enabling values for the same counter type to be compared, regardless of interval.
              
              For example, the number of reads per second.
      """
      absolute: _typing.ClassVar['VsanPerfMetricId.VsanPerfStatsType'] = 'absolute'
      delta: _typing.ClassVar['VsanPerfMetricId.VsanPerfStatsType'] = 'delta'
      rate: _typing.ClassVar['VsanPerfMetricId.VsanPerfStatsType'] = 'rate'
      VsanPerfStatsType_Unknown: _typing.ClassVar['VsanPerfMetricId.VsanPerfStatsType'] = 'VsanPerfStatsType_Unknown'

   label: str
   group: _typing.Optional[str] = None
   rollupType: _typing.Optional[str] = None
   statsType: _typing.Optional[str] = None
   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   metricsCollectInterval: _typing.Optional[int] = None


class VsanPerfMetricSeriesCSV(pyVmomi.vmodl.DynamicData):
   """
   This data object type represents a metric series encoded in CSV format.
   
   Attributes:
       metricId: Information about the metric this data object has values for
       threshold: The threshold used by VsanPerfDiagnosticService to indicate the level of
           performance issue seen in the data.
           
           Only populated in return from
           GetVsanPerfDiagnosisResult
       numExceptions: The number of exceptions is used by VsanPerfDiagnosticService to indicate
           the number of times that the corresponding rule in VsanPerfDiagnosticService
           sees the threshold getting violated.
           
           Only populated in return from
           GetVsanPerfDiagnosisResult.
       values: An array of sample values in CSV format
   """
   metricId: VsanPerfMetricId
   threshold: _typing.Optional[VsanPerfThreshold] = None
   numExceptions: _typing.Optional[str] = None
   values: _typing.Optional[str] = None


class VsanPerfNodeInformation(pyVmomi.vmodl.DynamicData):
   """
   Runtime information about the vSAN Performance service of a single vSAN host.
   
     
   CMMDS master
     
   The Cluster Monitoring, Membership, and Directory Service (CMMDS) of vSAN elects
   exactly one master node in every network partition. In a well formed cluster there is
   exactly one master, but when there are partition, each partition will have its own
   master. The master doesn't have any special user visible role, it is purely an
   internal state and any node can be master. The vSAN performance service uses the
   CMMDS Master node to establish its own notion of \"Stats Master\". Note though that to
   be \"Stats master\" it is not sufficient for a node to be CMMDS Master. The node must
   also have accessibility to the Stats DB object. Using this scheme guarantees that
   - The Stats Master is easily discoverable.
   - There is only ever one Stats Master in the cluster.
     
     
   Stats master:
     
   vSAN performance service is a distributed/clustered solution. Every host in a
   performance service enabled cluster is running a performance service instance. One
   host is elected to a master named as Stats Master. Stats Master is elected from CMMDS
   Master hosts only.
   The Stats Master is the only one writing to the DB. It periodically queries the
   performance service on the other members of the cluster, aggregates the results and
   persists them into the database.
   Stats Master is the host which can response APIs. Every request from front-end client
   will be handled by Stats Master.
   
   Attributes:
       version: vSAN performance service version.
       hostname: Name of the host.
           
           Only set if queried via vCenter
       error: If error is set, it means that collection of node information failed.
       isCmmdsMaster: Whether or not the node is CMMDS Master.
       isStatsMaster: Whether or not the node is Stats Master.
       vsanMasterUuid: The vSAN Node UUID of the CMMDS Master.
           
           May be itself.
       vsanNodeUuid: The vSAN Node UUID of the node being queried
       masterInfo: Additional information in case the node is a stats master.
       diagnosticMode: Whether the node has diagnostic mode enabled.
   """
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
   """
   This data object specifies the query parameters, including the
   reference ID to the target entity for statistics retrieval.  
   
   For supported entity types, metric groups, metrics:  
   See `pyVmomi.vim.cluster.VsanPerformanceManager.queryVsanPerf`
   
   Attributes:
       entityRefId: The 'entityRefId' is an entity reference id, which is used to identify the target
           entity (i.e.
           
           clusters, hosts) you want to query. Here an entity reference id
           consists of an entity type and an UUID of the entity. Its format is
           <entity-type>:<entity-uuid>. It is possible to pass '*' as the value
           for entity-uuid in case one wants to query all entities of a certain type.
           For supported entity types:  
           See `pyVmomi.vim.cluster.VsanPerformanceManager.queryVsanPerf`
       startTime: The startTime is the server time from which to obtain counters.
           
           This field must be specified, and the returned samples do not
           include the sample at startTime.
       endTime: The endTime is the server time up to which statistics are retrieved.
           
           This field will be replaced by current server time if it is
           later than current server time. This field must be specified and the
           returned samples include the sample at endTime.
       group: A type of entity (like hosts) may have metrics with same names (i.e.
           
           IOPS,
           Throughput) in different groups/view-points (i.e. DOMClient, DOMCompMgr).
           Here the 'group' attribute is used to identify which group of metrics is to
           be queried for an entity. If group is not set, a default group will be used.
           For supported entity types, metric groups, metrics:  
           See `pyVmomi.vim.cluster.VsanPerformanceManager.queryVsanPerf`
       labels: The performance metrics (labels) to be retrieved.
           
           The label is also used in
           VsanPerfMetricId of returned metrics data.
       interval: The interval, in seconds, for aggregated performance statistics.
           
           Please ignore this field. It is not used in this version.
   """
   entityRefId: str
   startTime: _typing.Optional[_datetime.datetime] = None
   endTime: _typing.Optional[_datetime.datetime] = None
   group: _typing.Optional[str] = None
   labels: list[str] = []
   interval: _typing.Optional[int] = None


class VsanPerfThreshold(pyVmomi.vmodl.DynamicData):
   """
   The threshold to display hot-spot line in graph
   
   Attributes:
       direction: The direction of threshold value indicates whether it is upper limit or lower limit.
       yellow: The yellow value of threshold indicates light severe warnings.
           
           When the
           performance metric value reaches the yellow threshold, you should be aware
           and plan ahead to avoid possible problems.
           Use string to present the number value of the threshold, like \"30\", \"65\".
       red: The red value of threshold indicates severe warnings.
           
           When the performance
           metric value reaches the red threshold, you should take action to avoid
           dangerous problems.
           Use string to present the number value of the threshold, like \"30\", \"65\".
   """
   class VsanPerfThresholdDirectionType(pyVmomi.VmomiSupport.Enum):
      """
      The direction of threshold value indicates whether it is upper limit or
      lower limit.
      
      Attributes:
          upper: The threshold is an upper limit.
              
              When the performance metric value exceeds the threshold, it will display warnings in graph.
          lower: The threshold is a lower limit.
              
              When the performance metric value is lower than the threshold, it will display warnings in graph.
      """
      upper: _typing.ClassVar['VsanPerfThreshold.VsanPerfThresholdDirectionType'] = 'upper'
      lower: _typing.ClassVar['VsanPerfThreshold.VsanPerfThresholdDirectionType'] = 'lower'
      VsanPerfThresholdDirectionType_Unknown: _typing.ClassVar['VsanPerfThreshold.VsanPerfThresholdDirectionType'] = 'VsanPerfThresholdDirectionType_Unknown'

   direction: str
   yellow: _typing.Optional[str] = None
   red: _typing.Optional[str] = None


class VsanPerfTimeRange(pyVmomi.vmodl.DynamicData):
   """
   Time ranges are specific start time and end time saved under a name.
   
   The time ranges can be used to query and analyze performance data
   during the specified period.
   
   Attributes:
       name: Name for the saved time range.
           
           It is up to 256 characters.
       startTime: Start timestamp for the saved time range.
       endTime: End timestamp for the saved time range.
   """
   name: str
   startTime: _datetime.datetime
   endTime: _datetime.datetime


class VsanPerfTimeRangeQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   This data object specifies the VsanPerfTimeRange query parameters.
   
   Attributes:
       name: Specify the name to query VsanPerfTimeRange.
       startTimeFrom: Specify start timestamp lower bound to query VsanPerfTimeRange.
       startTimeTo: Specify start timestamp upper bound to query VsanPerfTimeRange.
       endTimeFrom: Specify end timestamp lower bound to query VsanPerfTimeRange.
       endTimeTo: Specify end timestamp upper bound to query VsanPerfTimeRange.
   """
   name: _typing.Optional[str] = None
   startTimeFrom: _typing.Optional[_datetime.datetime] = None
   startTimeTo: _typing.Optional[_datetime.datetime] = None
   endTimeFrom: _typing.Optional[_datetime.datetime] = None
   endTimeTo: _typing.Optional[_datetime.datetime] = None


class VsanPerfTopEntities(pyVmomi.vmodl.DynamicData):
   """
   Result structure for fetching the top entities by a certain metric
   
   Attributes:
       metricId: Metric for which we are getting the top entities
       entities: Sorted list of entities and their value
   """
   metricId: VsanPerfMetricId
   entities: list[VsanPerfTopEntity] = []


class VsanPerfTopEntity(pyVmomi.vmodl.DynamicData):
   """
   Result structure for fetching a single top entity, with value and entity information.
   
   Attributes:
       entityRefId: The entity reference id in format <type>:<id> like managed object reference.
           
           For supported entity types, metric groups, metrics,
           see `pyVmomi.vim.cluster.VsanPerformanceManager.queryVsanPerf`
       value: Value of the entity at a specific point in time
   """
   entityRefId: str
   value: str


class VsanPerfTopQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   Describe specification for query operation to retrieve vSAN performance
   top entities.
   
   Attributes:
       timeStamp: Indicate the sampling time to return the desired vSAN performance top
           entities.
       entity: Represent the managed object type of the top entities, including
           virtual-machine, host-domclient, and host-domcompmgr.
           
           In vSAN setup,
           it also includes disk-group.
       metricId: Indicate which one metric is used to decide the order of the top entities
           from resource consuming perspective.
           
           The valid metric types for top entities query, for virtual-machine, disk-group, host-domclient
           and host-domcompmgr, including iopsRead, iopsWrite, throughputRead, throughputWrite,
           latencyRead, latencyWrite.
       numEntities: Represent the number of the top entities to be returned.
           
           The default value is 10 and the maximum is 50.
   """
   timeStamp: _datetime.datetime
   entity: str
   metricId: str
   numEntities: _typing.Optional[int] = None


class VsanPerformanceManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed object type provides the service interface for obtaining
   statistical data about various aspects of vSAN performance, as generated
   and maintained by the vSAN performance service of the cluster.
   
   It also offers
   methods to enable/disable, configure and perform other maintenance tasks
   about the vSAN performance service. It is available on both vCenter as well
   as ESXi under the vSAN extension endpoint. On both systems a singleton object
   is registered under the Managed Object ID 'vsan-performance-manager'.
     
   All the vSAN hosts belongs to one of the following two type in performance service
   perspective.
     
   Stats Master node: see `pyVmomi.vim.cluster.VsanPerfNodeInformation`
     
   Agent node: all other nodes except the master node, which collect its performance
   statistics when receive the request from master then send it back.
   """
   def QueryVsanPerfTopEntities(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], querySpec: VsanPerfTopQuerySpec) -> list[VsanPerfEntityMetricCSV]:
      """
      The API is designed to return a list of top contributors with either type of
      VM or disk group that are consuming the most IOPS, throughput or latency in
      the vSAN cluster.
      
      Args:
          cluster: vSAN cluster, which is ignored if the API is called against
              host.
          querySpec: Represent query specification to retrieve the desired top
              entities.
      
      Returns:
          A list of top entities with the expected metric values at the given
          time stamp.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the set of arguments passed to the function is
              not specified correctly, e.g., numEntities is above 50.
          pyVmomi.vim.fault.VsanNodeNotMaster: if this API is invokded against stats agent node.
      """
      ...
   def QueryVsanPerfHotspotEntities(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], querySpec: VsanPerfHotspotQuerySpec) -> list[VsanPerfHotspotEntitiesMetrics]:
      """
      The API is designed to return a list of hotspot entities that are consuming the
      most IOPS, throughput or latency according to given start time and end time in
      the vSAN cluster.
      
      Args:
          cluster: vSAN cluster, which is ignored if the API is called against
              host.
          querySpec: Represent query specification to retrieve the desired top
              entities.
      
      Returns:
          A list of hotspot entities with the expected metric values at the given
          start time and end time.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the set of arguments passed to the function is
              not specified correctly, e.g., numEntities is more than 64.
          pyVmomi.vim.fault.Timedout: if this API is timeout.
          pyVmomi.vim.fault.VsanNodeNotMaster: if this API is invokded against stats agent node.
          pyVmomi.vim.fault.NotFound: if the stats primary node is not found in target cluster.
          pyVmomi.vmodl.fault.NotSupported: if vSAN is not enabled in target cluster.
      """
      ...
   def VsanPerfDiagnose(self, perfDiagnoseQuery: VsanPerfDiagnoseQuerySpec, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[VsanPerfDiagnosticResult]:
      """
      Deprecated: As of vSphere API 6.7, please use VsanPerfDiagnoseTask instead.API to do performance diagnosis.
      
      Args:
          perfDiagnoseQuery: The query describing details of diagnosis
              required, such as the period of diagnosis and the query type.
          cluster: vSAN cluster. Ignored if called against host.
      
      Returns:
          The list of performance issues found. Each performance issue is
          returned as a VsanPerfDiagnosticResult. The VsanPerfDiagnosticResult
          object will contain the entity and the metrics that caused the performance
          exception.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.VsanNodeNotMaster: Fault means that the operation attempted is only possible on a vSAN
              performance collection master node, and that this node was not in that state
              at the point of the API call.
              
              Information about the identity of the master
              is provided for convenience.
          pyVmomi.vim.fault.Timedout: Timedout exception is thrown when a server abandons an operation that
              is taking longer than expected.
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def VsanPerfDiagnoseTask(self, perfDiagnoseQuery: VsanPerfDiagnoseQuerySpec, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> pyVmomi.vim.Task:
      """
      Runs a diagnostic query to determine performance issues in a vSAN
      cluster.
      
      This API call investigates the state of the vSAN cluster during
      the chosen period of time, and returns any issues (list of
      VsanPerfDiagnosticResult) that may be limiting the
      performance of the vSAN cluster. This API is available from only the vCenter,
      it is not available at the end-host. Processing is performed in the
      background, and a task is returned. Please wait for the task to finish, and
      then call GetVsanPerfDiagnosisResult to retrieve results.
      
      Args:
          perfDiagnoseQuery: The query describing details of diagnosis
              required, such as the period of diagnosis and the query type.
          cluster: vSAN cluster. Ignored if called against host.
      
      Returns:
          A task doing the asynchronous work.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the set of arguments passed to the function is
              not specified correctly.
          pyVmomi.vim.fault.VsanNodeNotMaster: Fault means that the operation attempted is only possible on a vSAN
              performance collection master node, and that this node was not in that state
              at the point of the API call.
              
              Information about the identity of the master
              is provided for convenience.
          pyVmomi.vim.fault.Timedout: Timedout exception is thrown when a server abandons an operation that
              is taking longer than expected.
          pyVmomi.vim.fault.NotFound: if no ESXi host could be contacted to perform the
              operation when called against vCenter or if the API was not invoked on
              vCenter or if CEIP is not enabled
          pyVmomi.vim.fault.VsanFault: if the caller doesn't have the required privilege, or the
              cluster has no hosts.
      """
      ...
   def GetVsanPerfDiagnosisResult(self, task: pyVmomi.vim.Task, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[VsanPerfDiagnosticResult]:
      """
      Returns the diagnosis result from the in memory cache for the supplied
      task.
      
      The task should have been returned by VsanPerfDiagnoseTask. This API
      is available only in the vCenter, it is not available at the end-host.
      
      Args:
          task: Task returned by VsanPerfDiagnoseTask
          cluster: vSAN cluster. Ignored if called against host.
      
      Returns:
          A list of performance issues.
      
      Raises:
          pyVmomi.vim.fault.Timedout: Timedout exception is thrown when a server abandons an operation that
              is taking longer than expected.
          pyVmomi.vim.fault.VsanFault: if the caller doesn't have the required privilege, or the
              cluster has no hosts.
          pyVmomi.vim.fault.NotFound: If no result is found in the cache for the specified task
      """
      ...
   def QueryVsanPerf(self, querySpecs: list[VsanPerfQuerySpec], cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[VsanPerfEntityMetricCSV]:
      """
      Retrieves the performance metrics for the specified
      vSAN entity (or entities) based on the properties specified in
      the VsanPerfQuerySpec data object
      The supported entity types are listed as bellow.
      - 'cluster-domclient'
      - 'cluster-domcompmgr'
      - 'host-domclient'
      - 'host-domcompmgr'
      - 'cache-disk'
      - 'capacity-disk'
      - 'disk-group'
      - 'vscsi'
      - 'virtual-machine'
      - 'virtual-disk'
      - 'vsan-host-net'
      - 'vsan-vnic-net'
      - 'vsan-pnic-net'
      - 'lsom-world-cpu'
      - 'dom-world-cpu'
      - 'host-cpu'
      - 'nic-world-cpu'
      - 'vsan-cpu'
      - 'vsan-memory'
      - 'rdt-net'
        
      The below entity types are used for vSAN ESA related metrics.
      - 'vsan-esa-disk-layer'
      - 'vsan-esa-disk-scsifw'
      - 'zdom-vtx'
        
      The below entity types are used for HCI mesh related metrics.
      - 'cluster-remotedomclient'
      - 'computeCluster-remotedomclient'
        
      The below entity types are used for vSAN direct related metrics.
      - 'vsan-direct-cluster'
      - 'vsan-direct-host'
        
      The below entity types are used for PMem related metrics.
      - 'host-pmem'
      - 'cluster-pmem'
        
      The below entity types are used for vSAN iSCSI service related metrics.
      The metrics are only collected when vSAN iSCSI service is enabled.
      - 'vsan-iscsi-host'
      - 'vsan-iscsi-lun'
      - 'vsan-iscsi-target'
        
      The below entity type is used for vSAN datastore capacity historical data.
      - 'vsan-cluster-capacity'
        
      The below entity type is used for vSAN file service related metrics.
      The metrics are only collected when vSAN file service is enabled.
      - 'vsan-file-service'
        
      The below entity type is used for IOInsight related metrics.
      The metrics are only collected when the IOInsight instance is running.
      - 'ioinsight'
      - 'ioinsight-histogram'
        
      To identify an entity in vSAN performance query spec, a vSAN performance
      entity reference is used.  
      An vSAN performance entity is in this format
      <entity-type>:<entity-uuid>.  
      Below are the examples:
      
      Entity Type
       - Entity ID format
       - Example
       - Notes
      
      cluster-domclient
       - <cluster-UUID>
       - 'cluster-domclient:52c89b61-f818-e495-af20-816d24c850b8'
       - The UUID is represented by the associated cluster UUID.
      
      cluster-domcompmgr
       - <cluster-UUID>
       - 'cluster-domcompmgr:52c89b61-f818-e495-af20-816d24c850b8'
       - The UUID is represented by the associated cluster UUID.
      
      host-domclient
       - <host-UUID>
       - 'host-domclient:588b2225-c58c-8365-c47b-02001065be12'
       - The UUID is represented by the associated ESXi host UUID.
      
      host-domcompmgr
       - <host-UUID>
       - 'host-domcompmgr:588b2225-c58c-8365-c47b-02001065be12'
       - The UUID is represented by the associated ESXi host UUID.
      
      cache-disk
       - <CacheDisk-UUID>
       - 'cache-disk:55c98c4d-41f0-6ff7-2784-0200103eb5e1'
       - The UUID is represented by the associated cache disk UUID.
      
      capacity-disk
       - <CapacityDisk-UUID>
       - 'capacity-disk:55c98c4d-41f0-6ff7-2784-0200103eb5e1'
       - The UUID is represented by the associated capacity disk UUID.
      
      disk-group
       - <CacheDisk-UUID>
       - 'disk-group:55c98c4d-41f0-6ff7-2784-0200103eb5e1'
       - The UUID is represented by the associated disk group UUID, which is the same as cache disk UUID.
      
      vscsi
       - <VM-instance-UUID>|<VSCSI-name>
       - 'vscsi:55c98c4d-41f0-6ff7-2784-0200103eb5e1|vscsi0:1'
       - The UUID is represented by the associated VM instance UUID with its VSCSI name. Virtual disk IOPS limit statistics are associated with 'virtual-disk'.
      
      virtual-machine
       - <VM-instance-UUID>
       - 'virtual-machine:55c98c4d-41f0-6ff7-2784-0200103eb5e1'
       - The UUID is represented by the associated VM instance UUID.
      
      virtual-disk
       - <VM-dir-uuid>/<VMDK-file-name>
       - 'virtual-disk:a2a04b57-e0e6-502b-e4a0-0200073bd703/iops-160-10.160.109.28-1_1.vmdk'
       - The UUID is represented by the VMDK file path, which can be retrieved using the vSphere API.
      
      vsan-vnic-net
       - <host-UUID>|<stack-name>|<vnic-name>
       - 'vsan-vnic-net:588b2225-c58c-8365-c47b-02001065be12|defaultTcpipStack|vmknic0'
       - The UUID is represented by the associated ESXi host UUID with its stack name and vNIC name.
      
      vsan-pnic-net
       - <host-UUID>|<pnic-name>
       - 'vsan-pnic-net:588b2225-c58c-8365-c47b-02001065be12|vmnic0'
       - This UUID is represented by the associated ESXi host UUID with the pNIC name.
      
      lsom-world-cpu
       - <host-UUID>|<world-name>|<world-id>
       - 'lsom-world-cpu:5ad47458-3bca-870a-602c-02002c89fe44|VSAN_0x43050bf3f7f8_LSOMLLOG|1001393599'
       - The UUID is represented by the associated ESXi host UUID with the LSOM world name and its world ID.
      
      dom-world-cpu
       - <host-UUID>|<world-name>|<world-id>
       - 'dom-world-cpu:5ad47458-3bca-870a-602c-02002c89fe44|VSAN_0x430bfa348888_CompServer|1001393015'
       - The UUID is represented by the associated ESXi host UUID with its DOM world name and world ID.
      
      host-cpu
       - <host-UUID>
       - 'host-cpu:5ad47458-3bca-870a-602c-02002c89fe44'
       - The UUID is represented by the associated ESXi host UUID.
      
      iscsi-target-alias
       - <iscsi-target-alias>|<lunid>
       - 'iscsi-target-alias:iscsitargetaliasexample|1'
       - The UUID is represented by iSCSI target alias with the LUN ID.
      
      vsan-cluster-capacity
       - <cluster-UUID>
       - 'vsan-cluster-capacity:52c89b61-f818-e495-af20-816d24c850b8'
       - The UUID is represented by the associated cluster UUID.
      
      vsan-file-service
       - <domain-name>|<share-name>
       - 'vsan-file-service:VSANFS-LOCAL.PRV|genericShare'
       - The UUID is represented by the domain name and the share name.
      
      nic-world-cpu
       - <host-UUID>|<world-name>
       - 'nic-world-cpu:5b9f8fd9-3687-7003-2f0b-02002fc9daae|vmnic0-pollWorld-0'
       - The UUID is represented by the associated ESXi host UUID with its vNIC/pNIC world name.
      
      vsan-cpu
       - <host-UUID>
       - 'vsan-cpu:5afa638a-f98a-c9f5-9f8a-0050569ee233'
       - The UUID represents the associated ESXi host UUID.
      
      vsan-memory
       - <host-UUID>
       - 'vsan-memory:5afa638a-f98a-c9f5-9f8a-0050569ee233'
       - The UUID represents the associated ESXi host UUID.
      
      rdt-net
       - <host-UUID>
       - 'rdt-net:5afa638a-f98a-c9f5-9f8a-0050569ee233'
       - The UUID represents the associated ESXi host UUID.
      
      vsan-esa-disk-layer
       - <host-UUID>
       - 'vsan-esa-disk-layer:5afa638a-f98a-c9f5-9f8a-0050569ee233'
       - The UUID represents the associated ESXi host UUID.
      
      vsan-esa-disk-scsifw
       - <host-UUID>
       - 'vsan-esa-disk-scsifw:5afa638a-f98a-c9f5-9f8a-0050569ee233'
       - The UUID represents the associated ESXi host UUID.
      
      zdom-vtx
       - <host-UUID>
       - 'zdom-vtx:5afa638a-f98a-c9f5-9f8a-0050569ee233'
       - The UUID represents the associated ESXi host UUID.
      
      cluster-remotedomclient
       - <cluster-UUID>
       - 'cluster-remotedomclient:52c89b61-f818-e495-af20-816d24c850b8'
       - The UUID is represented by the associated cluster UUID.
      
      computeCluster-remotedomclient
       - <cluster-UUID>
       - 'computeCluster-remotedomclient:52c89b61-f818-e495-af20-816d24c850b8'
       - The UUID is represented by the associated cluster UUID.
      
      vsan-direct-cluster
       - <cluster-UUID>
       - 'vsan-direct-cluster:52c89b61-f818-e495-af20-816d24c850b8'
       - The UUID is represented by the associated cluster UUID.
      
      vsan-direct-host
       - <host-UUID>
       - 'vsan-direct-host:5afa638a-f98a-c9f5-9f8a-0050569ee233'
       - The UUID represents the associated ESXi host UUID.
      
      host-pmem
       - <host-UUID>
       - 'host-pmem:5afa638a-f98a-c9f5-9f8a-0050569ee233'
       - The UUID represents the associated ESXi host hardware UUID.
      
      cluster-pmem
       - <cluster-MOID>
       - 'cluster-pmem:domain-c21'
       - The MOID represents the associated managed object ID.
      
      ioinsight
       - <VM-instance-UUID>|<VSCSI-name>
       - 'ioinsight:55c98c4d-41f0-6ff7-2784-0200103eb5e1|vscsi0:1'
       - The UUID is represented by the associated VM instance UUID with its VSCSI name.
      
      ioinsight-histogram
       - <VM-instance-UUID>|<VSCSI-name>
       - 'ioinsight-histogram:55c98c4d-41f0-6ff7-2784-0200103eb5e1|vscsi0:1'
       - The UUID is represented by the associated VM instance UUID with its VSCSI name.
      
      Supported metrics for each entity type:  
      
      Entity Type - Metrics (Labels)
      
      'cluster-domclient'
       - 
      'iopsRead', 'throughputRead', 'latencyAvgRead',
      'iopsWrite', 'throughputWrite', 'latencyAvgWrite',
      'congestion', 'oio'
      
      'cluster-domcompmgr'
       - 
      'iopsRead', 'throughputRead', 'latencyAvgRead',
      'iopsWrite', 'throughputWrite', 'latencyAvgWrite',
      'iopsRecWrite', 'throughputRecWrite', 'latencyAvgRecWrite',
      'congestion', 'oio', 'iopsResyncRead', 'tputResyncRead',
      'latAvgResyncRead'
      
      'host-domclient'
       - 
      'iopsRead', 'throughputRead', 'latencyAvgRead', 'readCount',
      'iopsWrite', 'throughputWrite', 'latencyAvgWrite', 'writeCount',
      'congestion', 'oio', 'clientCacheHits', 'clientCacheHitRate',
      'iopsUnmap', 'throughputUnmap', 'latencyAvgUnmap'
      
      'host-domcompmgr'
       - 
      'iopsRead', 'throughputRead', 'latencyAvgRead', 'readCount',
      'iopsWrite', 'throughputWrite', 'latencyAvgWrite', 'writeCount',
      'iopsRecWrite', 'throughputRecWrite', 'latencyAvgRecWrite',
      'recWriteCount', 'congestion', 'oio', 'iopsResyncRead',
      'tputResyncRead', 'latAvgResyncRead', 'iopsUnmap', 'iopsRecUnmap',
      'throughputUnmap', 'throughputRecUnmap', 'latencyAvgUnmap',
      'latencyAvgRecUnmap'
      
      'cache-disk'
       - 
      'iopsDevRead', 'throughputDevRead', 'latencyDevRead',
      'ioCountDevRead', 'iopsDevWrite', 'throughputDevWrite', 'latencyDevWrite',
      'ioCountDevWrite', 'latencyDevDAvg', 'latencyDevGAvg'
      
      'capacity-disk'
       - 
      'iopsDevRead', 'throughputDevRead', 'latencyDevRead',
      'ioCountDevRead', 'iopsDevWrite', 'throughputDevWrite', 'latencyDevWrite',
      'ioCountDevWrite', 'latencyDevDAvg', 'latencyDevGAvg', 'iopsRead',
      'latencyRead', 'ioCountRead', 'iopsWrite', 'latencyWrite', 'ioCountWrite',
      'deleteCongestion'
      
      'disk-group'
       - 
      'iopsSched', 'latencySched', 'outstandingBytesSched',
      'iopsSchedQueueRec', 'throughputSchedQueueRec','latencySchedQueueRec',
      'iopsSchedQueueVM', 'throughputSchedQueueVM','latencySchedQueueVM',
      'iopsSchedQueueMeta', 'throughputSchedQueueMeta','latencySchedQueueMeta',
      'iopsDelayPctSched', 'latencyDelaySched',
      'rcHitRate', 'wbFreePct', 'warEvictions', 'quotaEvictions',
      'iopsRcRead', 'latencyRcRead', 'ioCountRcRead',
      'iopsWbRead', 'latencyWbRead', 'ioCountWbRead',
      'iopsRcWrite', 'latencyRcWrite', 'ioCountRcWrite',
      'iopsWbWrite', 'latencyWbWrite', 'ioCountWbWrite',
      'ssdBytesDrained', 'zeroBytesDrained',
      'memCongestion', 'slabCongestion', 'ssdCongestion',
      'iopsCongestion', 'logCongestion', 'compCongestion', 'iopsDirectSched',
      'iopsRead', 'throughputRead', 'latencyAvgRead', 'readCount',
      'iopsWrite', 'throughputWrite', 'latencyAvgWrite', 'writeCount',
      'oioWrite', 'oioRecWrite', 'oioWriteSize', 'oioRecWriteSize',
      'rcSize', 'wbSize', 'capacity', 'capacityUsed', 'capacityReserved',
      'throughputSched', 'iopsResyncReadPolicy', 'iopsResyncReadDecom',
      'iopsResyncReadRebalance', 'iopsResyncReadFixComp', 'iopsResyncWritePolicy',
      'iopsResyncWriteDecom', 'iopsResyncWriteRebalance', 'iopsResyncWriteFixComp',
      'tputResyncReadPolicy', 'tputResyncReadDecom', 'tputResyncReadRebalance',
      'tputResyncReadFixComp', 'tputResyncWritePolicy', 'tputResyncWriteDecom',
      'tputResyncWriteRebalance', 'tputResyncWriteFixComp', 'latResyncReadPolicy',
      'latResyncReadDecom', 'latResyncReadRebalance', 'latResyncReadFixComp',
      'latResyncWritePolicy', 'latResyncWriteDecom', 'latResyncWriteRebalance',
      'latResyncWriteFixComp', 'bytesPerSecondBandwidth'
      
      'virtual-machine'
       - 
      'iopsRead', 'throughputRead', 'latencyRead', 'readCount',
      'iopsWrite', 'throughputWrite', 'latencyWrite', 'writeCount'
      
      'vscsi'
       - 
      'iopsRead', 'throughputRead', 'latencyRead', 'readCount',
      'iopsWrite', 'throughputWrite', 'latencyWrite', 'writeCount'
      
      'virtual-disk'
       - 
      'iopsLimit', 'NIOPS', 'NIOPSDelayed'
      
      'vsan-host-net'
       - 
      'rxThroughput', 'rxPackets', 'rxPacketsLossRate',
      'txThroughput', 'txPackets', 'txPacketsLossRate',
      'portRxDrops', 'portTxDrops',
      'tcpTxRexmitRate', 'tcpRxErrRate'
      
      'vsan-vnic-net'
       - 
      'rxThroughput', 'rxPackets', 'rxPacketsLossRate',
      'txThroughput', 'txPackets', 'txPacketsLossRate',
      'portRxDrops', 'portTxDrops'
      
      'vsan-pnic-net'
       - 
      'rxThroughput', 'rxPackets', 'rxPacketsLossRate',
      'txThroughput', 'txPackets', 'txPacketsLossRate',
      'portRxDrops', 'portTxDrops', 'pauseCount'
      
      'lsom-world-cpu'
       - 
      'usedPct', 'readyPct'
      
      'dom-world-cpu'
       - 
      'usedPct', 'readyPct'
      
      'host-cpu'
       - 
      'coreUtilPct', 'pcpuUtilPct', 'pcpuUsedPct'
      
      'vsan-iscsi-host'
       - 
      'iopsRead', 'iopsWrite', 'iopsTotal',
      'bandwidthRead', 'bandwidthWrite', 'bandwidthTotal',
      'latencyRead', 'latencyWrite', 'latencyTotal', 'queueDepth'
      
      'vsan-iscsi-target'
       - 
      'iopsRead', 'iopsWrite', 'iopsTotal',
      'bandwidthRead', 'bandwidthWrite', 'bandwidthTotal',
      'latencyRead', 'latencyWrite', 'latencyTotal', 'queueDepth'
      
      'vsan-iscsi-lun'
       - 
      'iopsRead', 'iopsWrite', 'iopsTotal',
      'bandwidthRead', 'bandwidthWrite', 'bandwidthTotal',
      'latencyRead', 'latencyWrite', 'latencyTotal', 'queueDepth'
      
      'vsan-cluster-capacity'
       - 
      'total', 'used', 'free', 'savedByDedup', 'dedupRatio'
      
      'vsan-file-service'
       - 
      'readRequested', 'readTransferred', 'readOpTotal', 'readLatency',
      'writeRequested', 'writeTransferred', 'writeOpTotal', 'writeLatency'
      
      'nic-world-cpu'
       - 
      'usedPct', 'readyPct'
      
      'vsan-cpu'
       - 
      'usedPct', 'readyPct'
      
      'vsan-memory'
       - 
      'kernelReservedSize', 'uwReservedSize'
      
      'rdt-net'
       - 
      'checksumMismatchCount'
      
      'vsan-esa-disk-layer'
       - 
      'iopsReadCapacity', 'iopsWriteCapacity', 'tputReadCapacity', 'tputReadCapacity',
      'avgLatReadCapacity', 'avgLatReadCapacity'
      
      'vsan-esa-disk-scsifw'
       - 
      'iopsDevRead', 'iopsDevWrite', 'latencyDevRead', 'latencyDevWrite',
      'latencyDevGAvg', 'latencyDevDAvg', 'throughputDevRead', 'throughputDevWrite'
      
      'zdom-vtx'
       - 
      'rateTotalCacheMiss', 'rateTotalCacheRef', 'rateTotalLogicalTreeCacheMiss',
      'rateTotalMiddleTreeCacheMiss', 'rateTotalSnapTreeCacheMiss', 'rateTotalBitmapCacheMiss',
      'rateTotalSutCacheMiss', 'rateTxnPrefetchTotalCacheMiss', 'rateTxnPrefetchLogicalTreeCacheMiss',
      'rateTxnPrefetchMiddleTreeCacheMiss', 'rateTxnPrefetchSutCacheMiss', 'rateTxnBankTotalCacheMiss',
      'rateTxnBankLogicalTreeCacheMiss', 'rateTxnBankMiddleTreeCacheMiss', 'rateTxnBankSutCacheMiss',
      'rateTxnUnmapTotalCacheMiss, 'rateTxnUnmapLogicalTreeCacheMiss', 'rateTxnUnmapMiddleTreeCacheMiss',
      'rateTxnUnmapSutCacheMiss', 'rateTxnSegCleaningCtxDataTotalCacheMiss', 'rateTxnSegCleaningCtxDataLogicalTreeCacheMiss',
      'rateTxnSegCleaningCtxDataMiddleTreeCacheMiss', 'rateTxnSegCleaningCtxDataSutCacheMiss',
      'rateTxnlookUpCacheMiss', 'rateTxnlookUpLogicalTreeCacheMiss', 'rateTxnlookUpMiddleTreeCacheMiss',
      'latAvgCacheGet', 'latAvgTotalOpIO', 'latAvgTxnBank', 'latAvgTxnBankTotalIO', 'latAvgTxnUnmap',
      'latAvgTxnUnmapTotalIO', 'cacheMissPerPrefetchTxn', 'cacheMissPerBankFlushTxn', 'cacheMissPerLookupTxn'
      
      'cluster-remotedomclient'
       - 
      'iopsRead', 'iopsWrite', 'throughputRead',
      'throughputWrite', 'latencyAvgRead', 'latencyAvgWrite',
      'congestion', 'oio'
      
      'computeCluster-remotedomclient'
       - 
      'iopsRead', 'iopsWrite', 'throughputRead',
      'throughputWrite', 'latencyAvgRead', 'latencyAvgWrite',
      'congestion', 'oio'
      
      'vsan-direct-cluster'
       - 
      'iopsDevRead', 'iopsDevWrite', 'throughputDevRead',
      'throughputDevWrite', 'latencyDevRead', 'latencyDevWrite',
      'oioDevRead', 'oioDevWrite'
      
      'vsan-direct-host'
       - 
      'iopsDevRead', 'iopsDevWrite', 'throughputDevRead',
      'throughputDevWrite', 'latencyDevRead', 'latencyDevWrite',
      'oioDevRead', 'oioDevWrite'
      
      'host-pmem'
       - 
      'bandwidthRead', 'bandwidthWrite', 'bandwidthTotal',
      'latencyRead', 'latencyWrite', 'iopsRead', 'iopsWrite',
      'iopsTotal'
      
      'cluster-pmem'
       - 
      'bandwidthRead', 'bandwidthWrite', 'bandwidthTotal',
      'latencyRead', 'latencyWrite', 'iopsRead', 'iopsWrite',
      'iopsTotal'
      
      'ioinsight'
       - 
      'iopsRead', 'iopsWrite', 'iopsTotal', 'throughputRead', 'throughputWrite',
      'throughputSequential', 'throughputRandom', 'throughputTotal',
      'sequentialReadRatio', 'sequentialWriteRatio', 'sequentialRatio',
      'randomReadRatio', 'randomWriteRatio', 'randomRatio',
      'aligned4kReadRatio', 'aligned4kWriteRatio', 'aligned4kRatio',
      'unaligned4kReadRatio', 'unaligned4kWriteRatio', 'unaligned4kRatio',
      'readRatio', 'writeRatio'
      
      'ioinsight-histogram'
       - 
      'iosz0_4k', 'riosz0_4k', 'wiosz0_4k',
      'iosz4k', 'riosz4k', 'wiosz4k',
      'iosz4k_8k', 'riosz4k_8k', 'wiosz4k_8k',
      'iosz8k', 'riosz8k', 'wiosz8k',
      'iosz8k_16k', 'riosz8k_16k', 'wiosz8k_16k',
      'iosz16k', 'riosz16k', 'wiosz16k',
      'iosz16k_32k', 'riosz16k_32k', 'wiosz16k_32k',
      'iosz32k', 'riosz32k', 'wiosz32k',
      'iosz32k_64k', 'riosz32k_64k', 'wiosz32k_64k',
      'iosz64k', 'riosz64k', 'wiosz64k',
      'iosz64k_128k', 'riosz64k_128k', 'wiosz64k_128k',
      'iosz128k', 'riosz128k', 'wiosz128k',
      'iosz128k_256k', 'riosz128k_256k', 'wiosz128k_256k',
      'iosz256k', 'riosz256k', 'wiosz256k',
      'iosz256k_512k', 'riosz256k_512k', 'wiosz256k_512k',
      'iosz512k', 'riosz512k', 'wiosz512k',
      'iosz512k_1m', 'riosz512k_1m', 'wiosz512k_1m',
      'iosz1m', 'riosz1m', 'wiosz1m', 'iosz1_m', 'riosz1_m', 'wiosz1_m',
      'lat0_1us', 'rlat0_1us', 'wlat0_1us',
      'lat1_10us', 'rlat1_10us', 'wlat1_10us',
      'lat10_100us', 'rlat10_100us', 'wlat10_100us',
      'lat100_500us', 'rlat100_500us', 'wlat100_500us',
      'lat500us_1ms', 'rlat500us_1ms', 'wlat500us_1ms',
      'lat1_5ms', 'rlat1_5ms', 'wlat1_5ms',
      'lat5_10ms', 'rlat5_10ms', 'wlat5_10ms',
      'lat10_25ms', 'rlat10_25ms', 'wlat10_25ms',
      'lat25_50ms', 'rlat25_50ms', 'wlat25_50ms',
      'lat50_100ms', 'rlat50_100ms', 'wlat50_100ms',
      'lat100_ms', 'rlat100_ms', 'wlat100_ms'
      
      Args:
          querySpecs: A array of VsanPerfQuerySpec objects. The VsanPerfQuerySpec object
              specifies a reference for an entity, plus optional criteria for filtering
              results. Only metrics for the entities that can be resolved are returned in
              any result.  
              The VsanPerfQuerySpec object in this operation can
              query for different metrics. Or, select all types of statistics for a
              single entity. See above for supported entity types, metric groups and metrics  
              The VsanPerfQuerySpec object supports wildcard query by setting UUID to '*', it retrieves
              all entities based on the specified entity type, startTime, and endTime.  
              From version 8.0U2, the VsanPerfQuerySpec object supports multi-entity query for a single
              entity type and unified duration by setting queried node id to '<UUID1>,<UUID2>,..',
              it will return all relevant entities according to the entity type, startTime and endTime.
              The maximum limit of the number of UUIDs is 400.  
              Note: To avoid bad performance and resource usage issues caused by massive stats data
              from a stats query. There are some validation checks:
              - In each query, the startTime and endTime must be specified in
                the query spec. And the suggested time span is less than 24 hours. To query stats
                for larger time range, please use paging mechanism. For example, split the time range
                in to smaller ones, and use multiple status queries with smaller time ranges.
              - In each query, when there is no wildcard or multi-entity query specified in the parameter
                querySpecs, the number of items within querySpecs should not exceed 100. When the parameter
                querySpecs includes more than 100 items, please use the paging mechanism.
              - In each query, if there is wildcard query or multi-entity query, the parameter querySpecs
                can only contain either one wildcard query or one multi-entity query.
          cluster: vSAN cluster. Ignored if called against host.
      
      Returns:
          The metric values for the specified entity or entities.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if the set of arguments passed to the function is
              not specified correctly.
          pyVmomi.vmodl.fault.NotSupported: if the host queried is not a Stats Daemon master
          pyVmomi.vim.fault.VsanNodeNotMaster: Fault means that the operation attempted is only possible on a vSAN
              performance collection master node, and that this node was not in that state
              at the point of the API call.
              
              Information about the identity of the master
              is provided for convenience.
          pyVmomi.vim.fault.Timedout: Timedout exception is thrown when a server abandons an operation that
              is taking longer than expected.
          pyVmomi.vim.fault.NotFound: if no ESXi host could be contacted to perform the operation
              when called against vCenter.
      """
      ...
   def QueryNodeInformation(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[VsanPerfNodeInformation]:
      """
      Query performance service related information about the node(s).
      
      Always returns a list, but when run against the host the list is guaranteed
      to have length=1. If run against vCenter, information about all hosts in the
      cluster is retrieved. If information of one host can not be retrieved, there
      are 2 situations:
      1. If the host is connected: it will throw
         \"invalid Request\", \"method fault\",
         \"vsan fault\" or other run time exception message.
      2. If the host is not connected, it will throw
         \"host is not in connected status\"
         message.
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
      """
      ...
   def CreateStatsObject(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], profile: _typing.Optional[pyVmomi.vim.vm.ProfileSpec]) -> str:
      """
      Create the vSAN object/directory containing the vSAN Perf Stats DB.
      
      Creation of the object also starts the collection of statistics as a side effect,
      i.e., it effectively enables the vSAN performance service.
      Profile can be 3 formats:
      - VirtualMachineEmptyProfileSpec means to use the empty vSAN policy. This is not the
        default policy, but a policy where all fields have default values.
      - VirtualMachineDefinedProfileSpec where profileId is set, in which case this profileId
        will be looked up in SPBM for the detailed policy information.
      - VirtualMachineDefinedProfileSpec where profileId is an empty string and instead
        the profileData is set for extensionKey 'com.vmware.vim.sps'. In this case the
        objectData field can be either the vSAN expression format, or a SPBM XML string.
        
        
      If no profile is supplied, and the call is executed against vCenter, then SPBM will
      be consulted for the vSAN datastore's default profile.
        
      Profile is ignored if executed against ESXi host.
      - If the vSAN object is already exist, return directly.
      - If vSAN is disabled, DestinationVsanDisabled exception will be raised.
      - If SPBM needs to be contacted, but SPBM is not available, RuntimeFault exception will be raised.
      - If the profileId can not be resolved with SPBM, InvalidArgument exception will be raised.
      - If objectData was provided but is neither of the two supported formats, InvalidArgument exception
        will be raised.
      - If the statsDB object can not be found, FileNotFound exception will be raised.
      - If the statsDB object failed to set the policy, e.g. because it is not accessible,
        FileNotWritable exception will be raised.
      - If called against VC, but no ESX host could be contacted to perform the operation
        NotFound exception will be raised.
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
          profile: Profile to be used for the stats object, see above.
      
      Returns:
          mounted path of the vSAN stats object (using \"/\" as path separator)
          i.e. /vmfs/volumes/vsan:525218c52dce3d62-e51a774ec7aef712/
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.VsanFault: if the pre-check tests failed.
          pyVmomi.vim.fault.FileAlreadyExists: if the stats object already exists.
          pyVmomi.vim.fault.CannotCreateFile: if it cannot complete file creation operation.
          pyVmomi.vim.fault.NotFound: if no ESXi host could be contacted to perform the operation
              when called against vCenter.
      """
      ...
   def CreateStatsObjectTask(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], profile: _typing.Optional[pyVmomi.vim.vm.ProfileSpec]) -> pyVmomi.vim.Task:
      """
      The asynchronous API of CreateStatsObject.
      
      The stats obj is created in
      in background, with a task returned. This method is only supported on
      vCenter.
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
          profile: Profile to be used for the stats object, see above
      
      Returns:
          vim task
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.VsanFault: if the caller doesn't have the required privilege, or the
              cluster has no hosts.
      """
      ...
   def DeleteStatsObject(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> bool:
      """
      Delete vSAN object/directory containing the vSAN Perf Stats DB.
      
      This method is only supported on ESXi host.
      Note: this will destroy all history and shut down the vSAN performance
      service.
      If the vSAN object doesn't exist, FileNotWritable exception will be raised.
      If vSAN is disabled, DestinationVsanDisabled exception will be raised.
      The operation can only be performed by masters, so VsanNodeNotMaster is raised
      when the node is not Stats master.
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
      
      Returns:
          True on success
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.FileNotWritable: Thrown if an attempt is made to write to a read-only file.
          pyVmomi.vim.fault.VsanFault: if the pre-check tests failed, or the host in the states
              that do not allow objects deletion (i.e. maintenance mode
              with data migration mode: ensure accessibility).
          pyVmomi.vim.fault.CannotCreateFile: if it cannot complete file creation operation.
          pyVmomi.vim.fault.VsanNodeNotMaster: Fault means that the operation attempted is only possible on a vSAN
              performance collection master node, and that this node was not in that state
              at the point of the API call.
              
              Information about the identity of the master
              is provided for convenience.
          pyVmomi.vim.fault.NotFound: if no ESXi host could be contacted to perform the operation
              when called against vCenter.
      """
      ...
   def DeleteStatsObjectTask(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> pyVmomi.vim.Task:
      """
      The asynchronous API of DeleteStatsObject.
      
      The statistics object is created
      in background, with a task returned.
      This method is only supported on vCenter.
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
      
      Returns:
          vim task
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.VsanFault: if the caller doesn't have the required privilege, or the
              cluster has no hosts.
      """
      ...
   def SetStatsObjectPolicy(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], profile: _typing.Optional[pyVmomi.vim.vm.ProfileSpec]) -> bool:
      """
      Set the policy of the vSAN object/directory containing the vSAN Perf Stats DB.
      
      The cluster parameter is ignored if called on ESXi.
      Profile can be 3 formats:
      - 1\\. VirtualMachineEmptyProfileSpec means to use the empty vSAN policy. This is not the
        default policy, but a policy where all fields have default values.
      - 2\\. VirtualMachineDefinedProfileSpec where profileId is set, in which case this
        profileId will be looked up in SPBM for the detailed policy information.
      - 3\\. VirtualMachineDefinedProfileSpec where profileId is an empty string and instead
        the profileData is set for extensionKey 'com.vmware.vim.sps'. In this case the
        objectData field can be either the vSAN expression format, or a SPBM XML string.
        
        
      If no profile is supplied, and the call is executed against vCenter, then SPBM will
      be consulted for the vSAN datastore's default profile.
        
      When this method returns successfully, the profile has been applied, but vSAN may
      still be remediating in order to implement the new policy. The health state of the
      object and resync information should be monitored to check on the progress.
        
      Only the third option is available when called on ESXi, other formats will raise
      InvalidArgument exception.
        
      Exception:
      - If SPBM needs to be contacted, but SPBM is not available, RuntimeFault exception will
        be raised.
      - If the profileId can not be resolved with SPBM, InvalidArgument exception will be raised.
      - If objectData was provided but is neither of the two supported formats, InvalidArgument
        exception will be raised.
      - If the statsDB object can not be found, FileNotFound exception will be raised.
      - If the statsDB object failed to set the policy, e.g. because it is not accessible,
        FileNotWritable exception will be raised.
      - If called against vCenter, but no ESXi host could be contacted to perform
        the operation NotFound exception will be raised.
        
        
      Python code example:
        
      spec = vim.vm.DefinedProfileSpec()
        
      VsanPerfSetStatsObjectPolicy(self.clusterRef, spec)
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
          profile: See above description for all possible options.
      
      Returns:
          True
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
          pyVmomi.vim.fault.FileNotFound: This fault is thrown when an operation fails because the specified file
              does not exist.
          pyVmomi.vim.fault.FileNotWritable: Thrown if an attempt is made to write to a read-only file.
          pyVmomi.vim.fault.VsanFault: if the caller doesn't have the required privilege
          pyVmomi.vim.fault.NotFound: if no ESXi host could be contacted to perform the operation
              when called against vCenter.
      """
      ...
   def QueryStatsObjectInformation(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> VsanObjectInformation:
      """
      Get information about the vSAN object/directory containing the vSAN Perf Stats DB.
      
      If the statsDB object can not be found, FileNotFound exception will be raised.
      If the statsDB object failed to read the policy, e.g. because it is not accessible,
      FileNotWritable exception will be raised.
      If called against vCenter, but no ESXi host could be contacted to perform the
      operation NotFound exception will be raised.
      
      Args:
          cluster: vSAN cluster. Ignored if called against host.
      
      Returns:
          Object information structure
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.FileNotFound: This fault is thrown when an operation fails because the specified file
              does not exist.
          pyVmomi.vim.fault.FileNotWritable: Thrown if an attempt is made to write to a read-only file.
          pyVmomi.vim.fault.NotFound: if no ESXi host could be contacted to perform the operation
              when called against vCenter.
      """
      ...
   def QueryClusterHealth(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[VsanClusterHealthGroup]:
      """
      This API shall not be used to query the health status for vSAN performance service.
      
      Consider this API as deprecated. Use `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.queryClusterHealthSummary`
      instead.
      
      Args:
          cluster: The cluster for which to compute health for.
      
      Returns:
          vim.cluster.VsanClusterHealthGroup[] A list of health groups.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if no ESXi host could be contacted to perform the operation
              when called against vCenter.
      """
      ...
   def QueryTimeRanges(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], querySpec: VsanPerfTimeRangeQuerySpec) -> list[VsanPerfTimeRange]:
      """
      Query saved time ranges in performance service.
      
      Args:
          querySpec: Specify the name and time boundaries. See details
              in `pyVmomi.vim.cluster.VsanPerfTimeRangeQuerySpec`
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.VsanNodeNotMaster: Fault means that the operation attempted is only possible on a vSAN
              performance collection master node, and that this node was not in that state
              at the point of the API call.
              
              Information about the identity of the master
              is provided for convenience.
          pyVmomi.vim.fault.Timedout: Timedout exception is thrown when a server abandons an operation that
              is taking longer than expected.
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def SaveTimeRanges(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], timeRanges: list[VsanPerfTimeRange]) -> None:
      """
      Save time ranges in performance service.
      
      Args:
          timeRanges: `pyVmomi.vim.cluster.VsanPerfTimeRange` list to be saved.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.VsanNodeNotMaster: Fault means that the operation attempted is only possible on a vSAN
              performance collection master node, and that this node was not in that state
              at the point of the API call.
              
              Information about the identity of the master
              is provided for convenience.
          pyVmomi.vim.fault.Timedout: Timedout exception is thrown when a server abandons an operation that
              is taking longer than expected.
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def DeleteTimeRange(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], name: str) -> None:
      """
      Delete saved time range in performance service.
      
      Args:
          name: Delete by the name of `pyVmomi.vim.cluster.VsanPerfTimeRange`
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.VsanNodeNotMaster: Fault means that the operation attempted is only possible on a vSAN
              performance collection master node, and that this node was not in that state
              at the point of the API call.
              
              Information about the identity of the master
              is provided for convenience.
          pyVmomi.vim.fault.Timedout: Timedout exception is thrown when a server abandons an operation that
              is taking longer than expected.
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def ToggleVerboseMode(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], verboseMode: bool) -> None:
      """
      Toggle vSAN performance service verbose mode.
      
      Args:
          verboseMode: Switch of verbose mode, the type is boolean.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vim.fault.VsanNodeNotMaster: Fault means that the operation attempted is only possible on a vSAN
              performance collection master node, and that this node was not in that state
              at the point of the API call.
              
              Information about the identity of the master
              is provided for convenience.
          pyVmomi.vim.fault.Timedout: Timedout exception is thrown when a server abandons an operation that
              is taking longer than expected.
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def GetSupportedEntityTypes(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[VsanPerfEntityType]:
      """
      This API is used to build performance graphs in a data-driven and dynamic way.
      
      Before querying stats, you need to know the entity type for specifying entity ID of the
      query spec. If you want to query specific metrics, you need to know what metrics are
      supported by that type of entities. And you may want to know how to organize the metrics
      into different graphs. The returned list of
      `pyVmomi.vim.cluster.VsanPerfEntityType` data model
      tells you all the information you needed for above questions.
        
      Each `pyVmomi.vim.cluster.VsanPerfEntityType` object describes supported
      metrics grouped by graphs
      for a type of entities like VMs. The name attribute of
      `pyVmomi.vim.cluster.VsanPerfEntityType`
      is the entity type ID used as part of the entity ID in the query spec.
      See `pyVmomi.vim.cluster.VsanPerfQuerySpec.entityRefId`.
        
      The model of vim.cluster.VsanPerfEntityType defines a list of performance graphs
      (`pyVmomi.vim.cluster.VsanPerfGraph`). And
      `pyVmomi.vim.cluster.VsanPerfGraph` defines a list of metrics
      (`pyVmomi.vim.cluster.VsanPerfMetricId`). This tells you how to organized
      different metrics to a graph and supported metrics of a type of entities.
      Then front-end/client can compose
      query specs using the information from the VsanPerfEntityType list and entity instance
      UUIDs to retrieved wanted performance statistics.
      The parameter \"cluster\" is optional, when calling this API from a vCenter-managed object,
      if this parameter is specified, the API will return the cluster-level supported entity type of
      against the cluster. If not specified, the API will return the supported entity type
      of vCenter; when calling this API from a ESXi host-managed object, this parameter will be ignored,
      the API will return the supported entity type of the host.
      """
      ...
   def GetSupportedHotspotEntityTypes(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> list[VsanPerfHotspotEntityType]:
      """
      This API is used to build hotspot performance dashboard in a data-driven and dynamic way.
      
      Before querying stats, you need to know the entity type for specifying entity ID of the
      query spec. If you want to query the entity by sorting specific metrics, you need to know
      what metrics are supported by that type of entities. And you may want to know how to query
      the raw metrics that are used to calculate the hotspot. The returned list of
      `pyVmomi.vim.cluster.VsanPerfHotspotEntityType` data model
      tells you all the information you needed for above questions.
      The parameter \"cluster\" is optional, when calling this API from a vCenter manage object,
      if this parameter is specified, the API will return the cluster level supported entity type of
      against cluster, if this parameter is not specified, the API will return the supported entity type
      of vCenter; when calling this API from a ESXi host manage object, this parameter will be ignored,
      the API will return the supported entity type of the host.
      """
      ...
   def GetSupportedDiagnosticExceptions(self) -> list[VsanPerfDiagnosticException]:
      """
      Get supported performance exceptions for front end data-driven
      performance exception reporting
      """
      ...
   def GetAggregatedEntityTypes(self) -> list[VsanPerfEntityType]:
      """
      Get supported aggregated entity types for front end data-driven
      reporting of diagnostic exceptions which return aggregated data.
      
      This API can be used to build performance graphs of aggregated data in a
      dynamic way.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryRemoteServerClusters(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], querySpec: _typing.Optional[VsanRemoteClusterQuerySpec]) -> list[str]:
      """
      Query all remote server clusters ever mounted from perf database by the
      specified query specification and return their UUIDs.
      
      This API is available
      on VC and stats master node.
      
      Args:
          cluster: Local vSAN cluster. This parameter will be ignored if the API
              is called against host.
          querySpec: Specification for the query operation. If the parameter
              is not specified all available remote clusters will be
              returned.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: If any argument passed to the function is not
              specified correctly.
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...


class VsanPerfsvcConfig(pyVmomi.vmodl.DynamicData):
   """
   Attributes:
       enabled: vSAN performance service enablement state
       profile: This field can be 3 formats:
           - VirtualMachineEmptyProfileSpec means to use the empty
             vSAN policy.
             
             This is not the default policy, but a policy
             where all fields have default values.
           - VirtualMachineDefinedProfileSpec where profileId is set,
             in which case this profileId will be looked up in SPBM for
             the detailed policy information.
           - VirtualMachineDefinedProfileSpec where profileId is an
             empty string and instead the profileData is set for extensionKey
             'com.vmware.vim.sps'. In this case the objectData field can be
             either the vSAN expression format, or a SPBM XML string.
             
             
           If no profile is specified, SPBM will be consulted for the vSAN
           datastore's default profile.
           It is not required while disable vSAN performance service by
           setting field 'enabled' to False.
       diagnosticMode: vSAN performance service diagnostic mode
       verboseMode: vSAN performance service verbose mode
   """
   enabled: bool
   profile: _typing.Optional[pyVmomi.vim.vm.ProfileSpec] = None
   diagnosticMode: _typing.Optional[bool] = None
   verboseMode: _typing.Optional[bool] = None


class VsanQueryPhysicalPlacementSpecs(pyVmomi.vmodl.DynamicData):
   """
   Query specs which contains multiple object types for retrieving
   the object physical placement details.
   
   Currently, only virtual machine type is supported for
   object placement details.
   
   Attributes:
       vms: Virtual machine reference list.
           
           Unset if VM entities are not given.
   """
   vms: list[pyVmomi.vim.VirtualMachine] = []

class VsanRelayoutObjectsErrorCode:
   """Defines the error code of `pyVmomi.vim.cluster.VsanObjectSystem.relayoutObjects`."""
   pass


class VsanRemoteClusterQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   Describe specifications for remote cluster query operation.
   
   Attributes:
       startTime: Start of a time range for remote cluster query operation.
           
           If this attribute is not provided, the query time range doesn't have
           start limit.
       endTime: End of a time range for remote cluster query operation.
           
           If this attribute is not provided, the query time range doesn't have
           end limit.
   """
   startTime: _typing.Optional[_datetime.datetime] = None
   endTime: _typing.Optional[_datetime.datetime] = None


class VsanRemoteDatastoreSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   The managed object provides support for vSAN remote datastore management
   operations.
   
   It can be accessed with MOID of 'vsan-remote-datastore-system',
   through vSAN service at vCenter server side.
   """
   def MountPrecheck(self, cluster: pyVmomi.vim.ClusterComputeResource, datastore: pyVmomi.vim.Datastore, serverClusterInfo: _typing.Optional[pyVmomi.vim.vsan.VcRemoteVsanServerClusterInfo]) -> pyVmomi.vim.vsan.MountPrecheckResult:
      """
      Checks mount compatibility of a vSAN datastore with given vSAN cluster.
      
      Get mount pre-check results of a client cluster and remote
      vSAN datastore. Different types of checks are needed, see
      `pyVmomi.vim.vsan.MountPrecheckResult` for details.
      
      Args:
          cluster: Client cluster that triggers the mount precheck request.
          datastore: The server vSAN datastore to be checked for mount.
          serverClusterInfo: The server cluster information of the vSAN
              datastore to be checked for mount. It's used
              for stretched cluster and remote
              data-in-transit configuration check.
      
      Returns:
          Pre-check results of a client cluster mounting server vSAN datastore.
      """
      ...
   def RemoteVcMountPrecheck(self, cluster: pyVmomi.vim.ClusterComputeResource, xvcDatastore: pyVmomi.vim.vsan.XVCDatastoreInfo, serverClusterInfo: _typing.Optional[pyVmomi.vim.vsan.VcRemoteVsanServerClusterInfo]) -> pyVmomi.vim.vsan.MountPrecheckResult:
      """
      Checks mount compatibility of a cross VC vSAN datastore with given vSAN
      cluster.
      
      Get mount pre-check results of a client cluster and cross VC remote
      vSAN datastore. Different types of checks are needed, see
      `pyVmomi.vim.vsan.MountPrecheckResult` for details.
      
      Args:
          cluster: Client cluster that trigger the mount precheck request.
          serverClusterInfo: Server cluster information of the remote VC
              vSAN datastore to be checked for mount.
      
      Returns:
          Pre-check results of a client cluster mounting cross VC vSAN datastore.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: vSAN related faults.
      """
      ...
   def QueryDatastoreSource(self, vcHosts: list[str]) -> list[pyVmomi.vim.vsan.HciMeshDatastoreSource]:
      """
      Query Datastore Source information for specified remote vCenters.
      
      If no vCenter is specified, all Datastore Sources configured are returned.
      
      Args:
          vcHosts: The names (e.g. FQDNs) of the remote vCenters to be queried.
              Only those names configured through
              `pyVmomi.vim.cluster.VsanRemoteDatastoreSystem.createDatastoreSource`
              are valid to be used.
      
      Returns:
          The Datastore Sources information queried.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: vSAN related faults.
      """
      ...
   def PrecheckDatastoreSource(self, datastoreSource: pyVmomi.vim.vsan.HciMeshDatastoreSource, operation: _typing.Optional[str]) -> pyVmomi.vim.vsan.DatastoreSourcePrecheckResult:
      """
      Run prechecks for a Datastore Source.
      
      This can be used before creating,
      updating, destroying a Datastore Source or other places needing to verify
      a Datastore Source.
      
      Args:
          datastoreSource: The information of the Datastore Source to be
              prechecked.
          operation: The hint of the operation which the precheck is performed
              against, see
              `pyVmomi.vim.vsan.PrecheckDatastoreSourceOperation`.
      
      Returns:
          Pre-check results of the specified Datastore Source.
      
      Raises:
          pyVmomi.vim.fault.VsanSslVerifyCertFault: SSL verification fault for remote vCenter
              such as certificate not verified.
          pyVmomi.vim.fault.VsanFault: Other vSAN related faults.
      """
      ...
   def CreateDatastoreSource(self, datastoreSource: pyVmomi.vim.vsan.HciMeshDatastoreSource) -> pyVmomi.vim.Task:
      """
      Create a new Datastore Source.
      
      Args:
          datastoreSource: The information of the Datastore Source to be
              created. If the vCenter is an ELM linked vCenter, only
              `pyVmomi.vim.vsan.RemoteVcInfo.vcHost`
              needs to be specified. For a standalone vCenter, the
              `pyVmomi.vim.vsan.RemoteVcInfoStandalone.user` and
              `pyVmomi.vim.vsan.RemoteVcInfoStandalone.password`
              needs to be specified for an user credential with
              the privileges to create the service account.
      
      Returns:
          The task for creating Datastore Source operation.
      
      Raises:
          pyVmomi.vim.fault.AlreadyExists: if the Datastore Source being created has existed.
          pyVmomi.vim.fault.VsanSslVerifyCertFault: SSL verification fault for remote vCenter
              such as certificate not verified.
          pyVmomi.vim.fault.VsanFault: Other vSAN related faults.
      """
      ...
   def UpdateDatastoreSource(self, datastoreSource: pyVmomi.vim.vsan.HciMeshDatastoreSource) -> pyVmomi.vim.Task:
      """
      Update the configuration of an existing Datastore Source.
      
      Args:
          datastoreSource: The information of the Datastore Source to be
              updated. The updated Datastore Source is
              identified by the vcHost specified in the
              remote vCenter info of this param.
              If the original or updated vCenter is a standalone
              vCenter, the
              `pyVmomi.vim.vsan.RemoteVcInfoStandalone.user` and
              `pyVmomi.vim.vsan.RemoteVcInfoStandalone.password`
              needs to be specified for an user credential with
              the privilege to update the service account.
              If both original and updated vCenters are ELM
              vCenters only `pyVmomi.vim.vsan.RemoteVcInfo.vcHost`
              needs to be specified.
      
      Returns:
          The task for updating Datastore Source operation.
      
      Raises:
          pyVmomi.vim.fault.NotFound: The specified Datastore Source is not found.
          pyVmomi.vim.fault.VsanFault: Other vSAN related faults.
      """
      ...
   def DestroyDatastoreSource(self, datastoreSource: pyVmomi.vim.vsan.HciMeshDatastoreSource) -> pyVmomi.vim.Task:
      """
      Destroy an existing Datastore Source configuration.
      
      Args:
          datastoreSource: The Datastore Source to be destroyed. If the vCenter
              is an ELM linked vCenter, only
              `pyVmomi.vim.vsan.RemoteVcInfo.vcHost`
              needs to be specified. For a standalone vCenter, the
              `pyVmomi.vim.vsan.RemoteVcInfoStandalone.user` and
              `pyVmomi.vim.vsan.RemoteVcInfoStandalone.password`
              needs to be specified for an user credential with
              the privileges to delete the service account.
      
      Returns:
          The task for destroying Datastore Source operation.
      
      Raises:
          pyVmomi.vim.fault.NotFound: The specified Datastore Source is not found.
          pyVmomi.vim.fault.ResourceInUse: The specified Datastore Source still has datastores
              being mounted.
          pyVmomi.vim.fault.VsanFault: Other vSAN related faults.
      """
      ...
   def QueryHciMeshDatastores(self, querySpecs: list[pyVmomi.vim.vsan.XvcQuerySpec], extraVcInfos: list[pyVmomi.vim.vsan.RemoteVcInfo]) -> list[pyVmomi.vim.vsan.XvcQueryResultSet]:
      """
      This method takes a list of VsanXvcQuerySpec, then returns a list of
      VsanXvcQueryResultSet.
      
      Each element of returned VsanXvcQueryResultSet
      list maps to the query spec in the VsanXvcQuerySpec list by index.
      Caller can provide a proper VsanXvcQuerySpec, and specify the required
      properties to be returned. The full list of the properties for each kind
      of returned object is described in VsanXvcQueryResultSet.
      Optionally, user can provide a list of remote VCs' information
      `pyVmomi.vim.vsan.RemoteVcInfo` to specify the remote VC to query.
      The supported objects are listed in
      `pyVmomi.vim.vsan.XvcQuerySpec.objectModel`.
      Each item is one datastore's info mapping to the specified properties
      `pyVmomi.vim.vsan.XvcQuerySpec.properties` in spec.
      
      Args:
          querySpecs: The spec information to specify what to be queried.
          extraVcInfos: The remote vCenter information for communication if
              caller needs to explicitly specify a remote vCenter
              as a provider vCenter which is not configured as a
              Datastore Source configuration. The user credential
              needs to be provided in the remote vCenter
              information, e.g., use
              `pyVmomi.vim.vsan.RemoteVcInfoStandalone`.
      
      Returns:
          The query result information per the query specs.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: vSAN related faults.
      """
      ...


class VsanSnapshotSpace(pyVmomi.vmodl.DynamicData):
   """
   Describes the vSAN snapshot space usage overview,
   excluding the RAID overhead and other system overhead.
   
   Attributes:
       snapshotCount: The total count of snapshots of all objects in cluster.
       actualSnapshotUsedB: The actual written snapshot capacity in cluster
           excluding RAID overhead and file system usage.
       fullyInflatedSnapshotUsedB: Fully inflated snapshot capacity in bytes.
           
           It refers to the total storage that would be
           consumed if all snapshots occupied their full
           logical size, without benefiting from any space
           efficiency mechanisms such as native snapshot
           or deduplication.
   """
   snapshotCount: _typing.Optional[int] = None
   actualSnapshotUsedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   fullyInflatedSnapshotUsedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanSpaceQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   This class describes the vSAN space usage query spec for the object
   entities like virtual machines or fault domains.
   
   Attributes:
       entityType: Specify the entity type which is queried for the vSAN space usage
           computing by aggregating all of vSAN objects belonging to the entity.
           
           Please refer to `pyVmomi.vim.cluster.VsanSpaceReportingEntityType` for
           all of entity types.
       entityIds: Specify the entities UUID for query.
           
           For the virtual machine, it's the
           managed object id like \"vm-1\". The maximum number of supported entities
           is 100 in one query.
   """
   entityType: str
   entityIds: list[str] = []


class VsanSpaceReportSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed object type provides the service interface to report the
   vSAN cluster space usage information including the space overview, the
   space usage breakdown to various vSAN object types and the vSAN data
   efficiency info after enabling vSAN deduplication.  
   The ManagedEntity can be accessed with MOID of 'vsan-cluster-space-report-system',
   through vSAN service at vCenter server side.
   """
   def QuerySpaceUsage(self, cluster: pyVmomi.vim.ComputeResource, storagePolicies: list[pyVmomi.vim.vm.ProfileSpec], whatifCapacityOnly: _typing.Optional[bool]) -> VsanSpaceUsage:
      """
      Query the vSAN space usage including the space usage overview
      and the space usage breakdown according to vSAN object type.
      
      This API will take less than one or tens seconds to return according
      to the number of node and object in the vSAN cluster. The API can also
      be used to query vSAN datastore physical capacity and what-if capacity
      under specified storage policies.
      
      Args:
          cluster: vSAN cluster
          storagePolicies: Storage policies specified to calculate what-if
              capacity of the cluster vSAN datastore. Default
              value is None
          whatifCapacityOnly: Flag indicates if the API is called only
              for getting vSAN datastore physical capacity
              and what-if capacity. Default value is False,
              which returns the vSAN space usage including
              the space usage overview and the space usage
              breakdown according to vSAN object type. When
              it is True, the API only returns the vSAN
              datastore physical capacity and what-if capacity
              under given storage policies.
      
      Returns:
          the vSAN space usage and vSAN datastore capacities.
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
      """
      ...
   def QueryVsanManagedStorageSpaceUsage(self, cluster: pyVmomi.vim.ComputeResource, querySpec: QueryVsanManagedStorageSpaceUsageSpec) -> list[VsanSpaceUsageWithDatastoreType]:
      """
      Query the space usage including the space usage overview and the space usage
      breakdown based on different datastore types.
      
      The API can also be used to
      query physical capacity.
      
      Args:
          cluster: vSAN cluster
          querySpec: The QueryVsanManagedStorageSpaceUsageSpec to specify more
              detailed query specification.
      
      Returns:
          the space usage aggregated by different datastore type.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              if the querySpec contains invalid datastore type.
      """
      ...
   def QueryEntitySpaceUsage(self, cluster: pyVmomi.vim.ComputeResource, querySpec: VsanSpaceQuerySpec) -> list[VsanEntitySpaceUsage]:
      """
      Query the vSAN space usage for the given vSAN object entities which
      contain a group of objects like the virtual machine with virtual disks
      backed by vSAN objects.
      
      Note it can query maximum 100 entities' space
      usage in one call for performance consideration.
      
      Args:
          cluster: The vSAN cluster
          querySpec: The vSAN space usage query spec to specify the entity
              types like virtual machine and the entity UUIDs like
              the managed object ID for virtual machines.
      
      Returns:
          The vSAN space usage for the vSAN entity
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
          pyVmomi.vmodl.fault.InvalidArgument: An InvalidArgument exception is thrown if the
              set of arguments passed to the function is not
              specified correctly.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...

class VsanSpaceReportingEntityType:
   """
   The vSAN Entity type.
   
   An Entity may include vSAN objects like
   virtual machine or fault domain.
   """
   pass


class VsanSpaceUsage(pyVmomi.vmodl.DynamicData):
   """
   Describes the vSAN space usage.
   
   There are multiple ways to
   present the space usage. One way is presenting the overall vSAN
   cluster system space usage like total used space in which how much
   data is physically written into disk and how much is the over-reserved
   space size. A second is listing the space usage breakdown per vSAN
   object type defined in below enumerations:
   `pyVmomi.vim.cluster.VsanObjectSpaceSummary.VsanObjectTypeEnum`,
   `pyVmomi.vim.cluster.VsanObjectSpaceSummary.VsanObjectTypeEnum90`
   
   Attributes:
       totalCapacityB: The total vSAN capacity in byte, which is the total used
           and free capacity combined.
           
           It's the total of physical space which
           can be use for writing data including any of user data, metadata
           and the overhead data.
       freeCapacityB: The free vSAN capacity in byte.
           
           It's the total of free vSAN physical
           space which can be used for writing data including any of user data, metadata and
           the overhead data.
       spaceOverview: The vSAN space usage overview including the vSAN physically
           written capacity, the reserved and over-reserved capacity and the total used
           capacity.
           
           It shares the same data structure as the per vSAN object type
           space usage summary VsanObjectSpaceSummary without setting the object type.
       spaceDetail: The vSAN space usage detail by breakdown the usage into different vSAN object type.
       efficientCapacity: The vSAN efficient capacity breakdown details when the vSAN cluster
           enables data efficiency.
       whatifCapacities: The vSAN capacity details if all objects are stored with the
           specified storage policy.
       uncommittedB: Total additional storage space, in bytes, potentially used by all
           vSAN objects except for the virtual machine swap objects and namespace
           objects on this vSAN datastore.
           
           It can be retrieved through
           `pyVmomi.vim.cluster.VsanSpaceReportSystem.querySpaceUsage` by specifying
           whatifCapacityOnly as False.
       capacityHealthThreshold: Indicates the yellow or red threshold, in bytes, for capacity usage based
           on current cluster capacityReservationInfo.
       spaceEfficiencyRatio: Indicates the vSAN space efficiency ratio, it exists only when
           vSAN efficiency feature is enabled, including global
           deduplication and compression.
           
           Since: 8.0.0.4
   """
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
   """
   Describes the vSAN storage capacity breakdown by various vSAN object types.
   
   Attributes:
       spaceUsageByObjectType: The used vSAN capacity for vSAN object types.
   """
   spaceUsageByObjectType: list[VsanObjectSpaceSummary] = []


class VsanSpaceUsageWithDatastoreType(pyVmomi.vmodl.DynamicData):
   """
   Describe the vSAN space usage for the a specific datastore type.
   
   The space usage will be aggregated according to the datastore type.
   
   Attributes:
       spaceUsage: The specified result of space usage.
       datastoreType: The specified datastore type.
   """
   spaceUsage: _typing.Optional[VsanSpaceUsage] = None
   datastoreType: _typing.Optional[str] = None


class VsanStorageWorkloadType(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: As of vSphere API 6.7.Class for the storage workload type for testing the vSAN storage performance.
   
   Attributes:
       specs: The VMDK load test specs
       typeId: The type id
       name: The load type name
       description: The type description
       duration: The duration as a burn in test (in seconds)
   """
   specs: list[pyVmomi.vim.host.VsanVmdkLoadTestSpec] = []
   typeId: str
   name: str
   description: str
   duration: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanStretchedClusterConfig(pyVmomi.vmodl.DynamicData):
   """
   Config spec of single vSAN stretched cluster
   
   Attributes:
       cluster: The target vSAN cluster to add/replace witness host.
       preferredFdName: User friendly name of preferred Fault Domain configured in target cluster.
       faultDomainConfig: The mapping between Fault Domain and vSAN hosts reside in target cluster,
           to decide how to configure vSAN cluster into two sites.
   """
   cluster: pyVmomi.vim.ClusterComputeResource
   preferredFdName: _typing.Optional[str] = None
   faultDomainConfig: _typing.Optional[VSANStretchedClusterFaultDomainConfig] = None


class VsanSyncingObjectFilter(pyVmomi.vmodl.DynamicData):
   """
   Object to specify the various filter options for result.
   
   Attributes:
       resyncType: Return syncing objects based on resync type specified by user.
           
           User specifies one of the values defined in `pyVmomi.vim.vsan.VsanSyncReason`
       resyncStatus: Return syncing objects based on resync status specified by user.
           
           User specifies one of the values defined in `pyVmomi.vim.vsan.VsanSyncStatus`
       numberOfObjects: Number of actively resyncing objects for which component level details are required.
           
           Default value will be 0, none objects returned.
       offset: Indicates the number of objects to be skipped when for resyncing object to be returned.
           
           Objects to return is calculated based on start and number of objects. 0 if not specified.
           Value less than 0 is illegal.
       includeDedupObject: Whether the query result includes the dedup store objects.
           
           If do not set it to true, dedup store objects are not included by default.
   """
   resyncType: _typing.Optional[str] = None
   resyncStatus: _typing.Optional[str] = None
   numberOfObjects: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   offset: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   includeDedupObject: _typing.Optional[bool] = None


class VsanUnicastAddressInfo(pyVmomi.vmodl.DynamicData):
   """
   Unicast address information of a cluster member.
   
   When unicast is used for vSAN clustering, we need to tell each host about
   the addresses information of all hosts in the cluster. These information
   includes the IP address, port and the vmknic. Host uses such information
   to communicate with others (through others' IP address).
   One such object represents one address information.
   
   Attributes:
       address: IP address of a cluster member.
           
           It could be IPv4 or IPv6 address.
       port: Port of a cluster member used for unicast traffic.
       nicType: nictype of a cluster member for unicast traffic.
   """
   address: str
   port: _typing.Optional[int] = None
   nicType: _typing.Optional[str] = None


class VsanUpgradeStatusEx(pyVmomi.vim.VsanUpgradeSystem.UpgradeStatus):
   """
   Extends vim.VsanUpgradeSystem.UpgradeStatus, to give more information
   including precheck status and results.
   
   Attributes:
       isPrecheck: Is or was this a precheck call, instead of a full upgrade.
       precheckResult: If this was a precheck that completed, then the result will be in this field.
   """
   isPrecheck: _typing.Optional[bool] = None
   precheckResult: _typing.Optional[VsanDiskFormatConversionCheckResult] = None


class VsanUpgradeSystemUpgradeHistoryStoragePoolOp(pyVmomi.vim.VsanUpgradeSystem.UpgradeHistoryItem):
   """
   Extends Vim.VsanUpgradeSystemUpgradeHistoryItem, to give information
   for storage pool disk in history operation.
   
   Attributes:
       operation: Storage pool disk operation like add, remove.
       diskInfo: Storage pool disk info.
   """
   operation: str
   diskInfo: pyVmomi.vim.vsan.host.StoragePoolDiskInfo


class VsanVcClusterConfigSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed object type provides a comprehensive way to manage vSAN
   cluster configuration in below areas:
   - Enable or disable vSAN
   - Enable or disable Autoclaim mode for disk group
   - Enable or disable data efficiency feature
   - Configure vSAN iSCSI target feature
   - Manage disk groups
   - Manage fault domains
   - Retrieve vSAN generic configuration
   - Retrieve data efficiency configuration
     
   In this class, ReconfigureEx enhances the legacy API
   `pyVmomi.vim.ComputeResource.reconfigureEx`.
   
   Legacy API
   `pyVmomi.vim.ComputeResource.reconfigureEx` is deprecated.  
   The ManagedEntity can be accessed with MOID of 'vsan-cluster-config-system',
   through vSAN service at vCenter server side.
   """
   def ReconfigureEx(self, cluster: pyVmomi.vim.ClusterComputeResource, vsanReconfigSpec: pyVmomi.vim.vsan.ReconfigSpec) -> pyVmomi.vim.Task:
      """
      Reconfigure a vSAN cluster.
      
      This method is used to set vSAN specific configuration, the method can be used
      to modify all vSAN related configuration. From vSAN 6.2, this
      API is the replacement of `pyVmomi.vim.ComputeResource.reconfigureEx` in order
      to support more configurations such as deduplication and compression, fault
      domain, disk mapping configuration in the cluster. The legacy API
      `pyVmomi.vim.ComputeResource.reconfigureEx` is deprecated because new API
      provide everything that legacy API has.
      To modify generic vSAN cluster setting such as vSAN enablement and
      autoclaim enablement, `pyVmomi.vim.vsan.ReconfigSpec.vsanClusterConfig` needs to
      be setup.
      To modify vSAN cluster specific features such as deduplication and
      compression enablement, `pyVmomi.vim.vsan.ReconfigSpec.dataEfficiencyConfig`
      needs to be setup. Currently for vSAN 6.2, deduplication and
      and compression need to be enable/disable together. To enable/disable
      deduplication and compression on a vSAN cluster, disk convert process
      (`pyVmomi.vim.VsanUpgradeSystemEx.performUpgrade` for description
      about disk convert process) will be invoked. This is only supported for
      all-flash disk groups.
      To modify vSAN cluster fault domain configuration,
      `pyVmomi.vim.vsan.ReconfigSpec.faultDomainsSpec` needs to be setup.
      To modify vSAN cluster disk groups reconfiguration,
      `pyVmomi.vim.vsan.ReconfigSpec.diskMappingSpec` needs to be setup.
      To modify vSAN iSCSI target service configuration,
      `pyVmomi.vim.vsan.ReconfigSpec.iscsiSpec` needs to be setup.
      
      Reconfiguring vSAN cluster requires Host.Inventory.EditCluster privilege on
      the cluster, extra privileges may be required depending on what is being
      changed:
      - Cryptographer.ManageEncryptionPolicy and Cryptographer.ManageKeys if
        changing data encryption configuration.
      
      Args:
          cluster: The target VC cluster.
          vsanReconfigSpec: The configure spec for vSAN cluster.
      
      Returns:
          vim.Task
      
      Raises:
          pyVmomi.vim.fault.VsanFault: when turn on data efficiency feature on a cluster
              which has hybrid disk group.
          pyVmomi.vim.fault.InvalidState: if the vSAN is not enabled in current
              cluster.
      """
      ...
   def GetConfigInfoEx(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.vsan.ConfigInfoEx:
      """
      Get configInfoEx for a vSAN cluster  
      We can get vSAN configuration information through this method.
      
      Currently users can only get generic cluster configuration and data
      efficiency configuration through this API.
        
      This API cannot retrieve fault domain configuration and disk group
      configuration. Disk group configuration can be retrieved through
      `pyVmomi.vim.cluster.VsanVcDiskManagementSystem.queryDiskMappings`.
      Fault domain configuration
      can be retrieved through `pyVmomi.vim.host.VsanSystem.config`.
      
      Args:
          cluster: The target vCenter cluster
      
      Returns:
          The configuration spec for the vCenter cluster
          ConfigInfoEx inherits from `pyVmomi.vim.vsan.cluster.ConfigInfo`.
          It appends data efficiency configuration.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vim.fault.InvalidState: An InvalidState fault is thrown if the
              operation failed due to the current state of the system.
      """
      ...
   def RekeyEncryptedCluster(self, encryptedCluster: pyVmomi.vim.ClusterComputeResource, deepRekey: _typing.Optional[bool], allowReducedRedundancy: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      Regenerate the key(s) used by vSAN encryption for the given cluster.
      
      When the key(s) used for vSAN encryption is compromised, this API can
      be used to renew the key(s). As described in
      `pyVmomi.vim.vsan.host.EncryptionInfo`, vSAN uses Key Encryption Key
      (KEK) to wrap the Data Encryption Key (DEK). Generally a user will only need
      to renew the KEK and use new KEK to rewrap the DEK, when KEK is compromised,
      or on regular basis. This is referred to as \"shallow rekey\". If user suspects
      that DEK is also compromised, both KEK and DEK will be renewed.
      Correspondingly this is called \"deep rekey\". And as a consequence of DEK
      change, the data on vSAN datastore will be re-encrypted with the new
      DEK, so this will be a slow process.
        
      This API does not support switching to a different KMS cluster. When there is
      a need to switch to a different KMS cluster, call
      `pyVmomi.vim.cluster.VsanVcClusterConfigSystem.reconfigureEx` and specify
      a different KMS cluster in the configuration
      `pyVmomi.vim.vsan.DataEncryptionConfig.kmsProviderId`.
      
      To run either shallow rekey or deep rekey for an encrypted vSAN cluster, both
      Cryptographer.ManageKeys privilege and Host.Inventory.EditCluster privilege
      are required on the cluster. If it is a shallow rekey, alternatively, caller
      with Vsan.Cluster.ShallowRekey privilege on the cluster will also be allowed.
      
      Args:
          encryptedCluster: The target VC cluster
          deepRekey: True to perform a deep rekey. Its default value is false when
              not provided, which means shallow rekey is performed
          allowReducedRedundancy: This optional parameter is only applicable for
              deep rekey when it needs to migrate data across cluster for changing
              vSAN disk format. The default value is 'false' if not specified
              See `pyVmomi.vim.vsan.ReconfigSpec.allowReducedRedundancy`,
              `ensureObjectAccessibility`,
              and `evacuateAllData`.
      
      Returns:
          vim.Task
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vim.fault.InvalidState: if the vSAN is not enabled or encryption is not
              enabled on the cluster.
      """
      ...
   def GetRuntimeStats(self, cluster: pyVmomi.vim.ClusterComputeResource, stats: list[str]) -> list[pyVmomi.vim.vsan.RuntimeStatsHostMap]:
      """
      Get vSAN runtime stats of all hosts reside in specified cluster.
      
      This API is used to retrieve vSAN runtime stats from all hosts reside in
      specified vSAN cluster. It bases on specified stats type list, to retrieve
      expected vSAN runtime stats. If host is out of reach, such as disconnected
      from vCenter, its stats will be ignored and unset.
      
      Args:
          cluster: The target vCenter cluster
          stats: List of vSAN runtime stats type. Supported vSAN runtime stats
              types are declared in `pyVmomi.vim.vsan.host.StatsType`.
              If this parameter is omitted, all supported runtime stats will
              be collected and returned.
      
      Returns:
          vim.vsan.RuntimeStatsHostMap[] List of vSAN runtime stats, each item
          contains owner host and its stats. If
          specified cluster is empty, or vSAN is
          disabled on it, an empty list will be
          returned.
      """
      ...
   def QueryClusterDrsStats(self, cluster: pyVmomi.vim.ClusterComputeResource, vms: list[pyVmomi.vim.VirtualMachine]) -> list[pyVmomi.vim.vsan.host.DrsStats]:
      """
      To support integration between vSAN and DRS, we are expected to report runtime
      stats of vSAN member hosts and VMs locate in specified vSAN cluster from storage
      perspective.
      
      Per request from DRS service, below stats are requested:
      - 1\\. capacity contributed to vSAN datastore per host;
      - 2\\. capacity usage to vSAN datastore per host;
      - 3\\. total size per vSAN VM;
      - 4\\. valid data percentage on every host per vSAN VM;
        
      This API is used to retrieve runtime stats requested by DRS.
      
      Args:
          cluster: The target vSAN cluster;
          vms: Specified VM list of which runtime stats should be reported. If omitted
              return stats of all vSAN VMs locate in specified vSAN cluster;
      
      Returns:
          List of `pyVmomi.vim.vsan.host.DrsStats`, in which stats should be parsed by
          the order of returned DrsStats.
      """
      ...
   def ValidateConfigSpec(self, cluster: pyVmomi.vim.ClusterComputeResource, vsanReconfigSpec: pyVmomi.vim.vsan.ReconfigSpec) -> list[pyVmomi.vim.ClusterComputeResource.ValidationResultBase]:
      """
      Validate the vSAN cluster reconfig spec to figure out whether user spec can
      be supported by target cluster.
      
      This API cannot predict the runtime failure,
      but only check the spec based on software capability. If target cluster
      cannot support the spec, it returns the detailed config issues.
      
      Args:
          cluster: The target VC cluster to apply reconfig spec
          vsanReconfigSpec: The configure spec to be validated
      
      Returns:
          A list of different validation results.
          The result returned are of two types.
          1\\. If the spec enables vSAN ESA, then result for every precheck is returned using
          `pyVmomi.vim.vsan.ClusterConfigPrecheckItem`. This includes prechecks of
          all possible statuses as in `pyVmomi.vim.vsan.VsanHealthStatusType`
          2\\. If the spec does not enable vSAN ESA, then the result for prechecks are returned
          using `pyVmomi.vim.ClusterComputeResource.ValidationResultBase`. Here, only the
          the prechecks which fail the validation are returned. The field
          `pyVmomi.vim.ClusterComputeResource.ValidationResultBase.info` contains the
          precheck failure reason.
      """
      ...
   def RunLifecycleCheck(self, cluster: pyVmomi.vim.ClusterComputeResource, vsanLifecycleCheckSpec: VsanVcLifecycleCheckSpec) -> VsanVcLifecycleCheckResult:
      """
      Run checks for lifecycle operations on a given vSAN cluster.
      
      The specification indicates the lifecycle operation for which checks will
      be performed.
      The result contains an overall status of the checks, a list of the checks
      run, and vSAN cluster configurations details related to the checks.
      The overall status of the checks in the result represents the highest
      severity status of all the results of the individual checks. For example,
      if all tests pass, the highest severity status is green. If a test results
      in yellow status and another in red status, the overall status will be red.
      The list of checks contains a description of the check, its result status
      and in case of failure, a localized error message.
      The vSAN cluster configuration details contains information like witness
      host and fault domains information for stretched clusters, or no witness
      host information to indicate single-site cluster.
      
      Args:
          cluster: Cluster on which to perform lifecycle checks and return
              configuration information.
          vsanLifecycleCheckSpec: Specification for the lifecycle checks.
      
      Returns:
          Lifecycle checks and configuration results.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
      """
      ...
   def GetClaimedCapacity(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.VmomiSupport.long:
      """
      Get total raw capacity in bytes for all disks claimed in a vSAN cluster.
      
      In the case of ESA, that includes all disks in the storage pool. In the case
      of OSA, that includes the capacity tier disks but not the cache disks as the
      latter does not contribute to capacity. The same value is reported to the
      licensing service for capacity entitlement purposes. Note that it differs
      from vSAN datastore capacity in two ways. First, it is based on raw capacity
      reported by the disk vendor, which includes any and all overhead reserved
      internally by vSAN. Secondly, it reflects the cluster configuration, which
      is not affected by the runtime state of the cluster, such as disk health,
      host health, and network partition.
      The claimed capacity is initialized in an async process after enabling vSAN,
      so it is possible that the claimed capacity value is not ready yet when
      vSAN is still in initialization phase. In this case, API caller can retry in
      a short period of time.
      
      Args:
          cluster: The target vCenter cluster.
      
      Returns:
          The total claimed disk capacity in raw bytes.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: if the capacity value has not been initialized.
          pyVmomi.vmodl.fault.NotSupported: if the cluster has not enabled vSAN.
      
      Since: 8.0.0.4
      """
      ...
   def GetConfigurationLimits(self) -> list[pyVmomi.vmodl.KeyAnyValue]:
      """
      Returns configuration limits and supported values.
      
      This API is useful to determine
      limits supported for a particular vSphere version.
      
      Returns:
          KeyValue pairs with configuration limits
      """
      ...
   def GetClusterAutoRAIDInfo(self, cluster: pyVmomi.vim.ClusterComputeResource) -> _typing.Optional[pyVmomi.vim.vsan.AutoRAIDInfo]:
      """
      Get Actual RAID used in vSAN ESA cluster.
      
      Args:
          cluster: The target cluster.
      
      Returns:
          Information of RAID type actually used in the cluster.
          Or, None if the cluster does not support Auto Policy or failed
          to get RAID information.
      """
      ...


class VsanVcClusterHealthSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   This managed object provides access to vSAN Health related configuration
   and query APIs, operating at a vSAN cluster level.
   
   It can be accessed
   through MOID of 'vsan-cluster-health-system', through vSAN service at
   vCenter server side.
   """
   class VsanHealthLogLevelEnum(pyVmomi.VmomiSupport.Enum):
      """The supported vSAN health log level enumeration for Storage Infrastructure / vSAN"""
      INFO: _typing.ClassVar['VsanVcClusterHealthSystem.VsanHealthLogLevelEnum'] = 'INFO'
      WARNING: _typing.ClassVar['VsanVcClusterHealthSystem.VsanHealthLogLevelEnum'] = 'WARNING'
      ERROR: _typing.ClassVar['VsanVcClusterHealthSystem.VsanHealthLogLevelEnum'] = 'ERROR'
      DEBUG: _typing.ClassVar['VsanVcClusterHealthSystem.VsanHealthLogLevelEnum'] = 'DEBUG'
      CRITICAL: _typing.ClassVar['VsanVcClusterHealthSystem.VsanHealthLogLevelEnum'] = 'CRITICAL'
      VsanHealthLogLevelEnum_Unknown: _typing.ClassVar['VsanVcClusterHealthSystem.VsanHealthLogLevelEnum'] = 'VsanHealthLogLevelEnum_Unknown'

   def QueryVerifyClusterHealthSystemVersions(self, cluster: pyVmomi.vim.ClusterComputeResource) -> VsanClusterHealthSystemVersionResult:
      """
      Query the version information of the vSAN health service all hosts in the
      specified cluster and on the vCenter Server.
      
      The operation verifies the
      consistency of version numbers across all hosts and reports any inconsistencies
      or issues found during the query.
      
      The query result includes all connected hosts in the cluster, excluding
      disconnected hosts and hosts that fail to respond.
      
      As of vSphere API version 9.0, this API is deprecated and should not
      be used. There is no dedicated vSAN health service version as the vSAN
      health functionality is always part of vCenter Server and ESX host.
      The vSAN health version will always equal the vCenter Server or ESX
      host version, which can be queried directly from the vCenter Server or
      ESX host APIs. Use `pyVmomi.vim.AboutInfo.version` from vCenter Server or
      the appropriate ESX host version API instead.
      
      Args:
          cluster: The target cluster to query.
      
      Returns:
          The vSAN health service version result containing version
          information for all hosts in the cluster, the vCenter Server
          version, and flags indicating whether issues were found or
          upgrades are possible. The result includes per-host version
          information and any errors encountered during the query.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryFileServiceHealthSummary(self, cluster: pyVmomi.vim.ClusterComputeResource, includeFileServerHealth: _typing.Optional[bool], includeFileShareHealth: _typing.Optional[bool]) -> _typing.Optional[VsanClusterFileServiceHealthSummary]:
      """
      Query the vSAN file service health on all the hosts in the specified
      cluster.
      
      Use filter fields to determine whether to include infra health
      or container health. It will include infra health at least.
      
      Args:
          cluster: The target cluster.
          includeFileServerHealth: Whether to retrieve file server health,
              default value is True.
          includeFileShareHealth: Whether to retrieve file share health,
              default value is True.
      
      Returns:
          The file service health summary. Return None if the file service is
          not enabled.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments, for example,
              if the cluster is not found.
      """
      ...
   def QueryClusterCreateVmHealthTest(self, cluster: pyVmomi.vim.ClusterComputeResource, timeout: int, datastore: _typing.Optional[pyVmomi.vim.Datastore]) -> VsanClusterCreateVmHealthTestResult:
      """
      Executes VM creation test and checks if a tiny VM can be created on each of
      host of the vSAN cluster
      
      Args:
          cluster: The target cluster
          timeout: The timeout in seconds for the VM creation test.
              The suggested value could be 2 minutes
          datastore: The datastore where the VM creation test will be run. It
              could be the local datastore or the remote datastore that
              is mounted to the cluster. By default it will run with
              local vSAN datastore.
      
      Returns:
          The vSAN cluster VM creation test result
      
      Raises:
          pyVmomi.vim.fault.NotFound: If cluster's hosts could not be contacted to
              perform the operation.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments.
          pyVmomi.vmodl.fault.NotSupported: Exception for hostlevel API call for API
              with remote datastore in hostlevel call.
      """
      ...
   def QueryClusterHealthSummary(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], vmCreateTimeout: _typing.Optional[int], objUuids: list[str], includeObjUuids: _typing.Optional[bool], fields: list[str], fetchFromCache: _typing.Optional[bool], perspective: _typing.Optional[str], hosts: list[pyVmomi.vim.HostSystem], spec: _typing.Optional[VsanClusterHealthQuerySpec]) -> VsanClusterHealthSummary:
      """
      Perform a cluster wide health check across all types of health checks.
      
      It's the
      primary API for fetching vSAN health status.
      This API runs a wide variety of health checks in many different categories against
      the cluster and returns both API-friendly and UI-friendly data. The 'fields' parameter
      should be used to return what the client is really interested in to limit the big result
      size for performance consideration. The API can either perform a health check against
      the up-to-date state of the hosts in the cluster and takes several seconds to return or
      it can retrieve the latest cached result to return in second. It's encouraged to fetch
      the cached data to get the quick response unless an update is required.
      Note: when this API is called directly from an ESXi host, following test groups are
      not supported:
      groupId = com.vmware.vsan.health.test.hcl
      
      Querying vSAN cluster requires System.Read privilege on the cluster. If the API
      is called to have pre-flight health check on a bunch of hosts, System.Read privilege
      on all these hosts is required.
      
      See Also: `pyVmomi.vim.vsan.VsanHealthPerspective`, `pyVmomi.vim.vsan.VsanHealthPerspective90`
      
      Args:
          cluster: The target cluster
          includeObjUuids: Whether to include detailed per-object health in the
              result. Default to True. Set to false if this value
              is not of importance to save computing resources.
          fields: If set, only the properties listed in the array are returned in the
              result data object. Normally the output of this API can be quite large
              so this allows clients which are only interested in a subset to save
              network bandwidth and deserialization effort. The possible value is the
              field from the VsanClusterHealthSummary class like 'objectHealth',
              'networkHealth' etc
              If unset, following properties are included in the result.
              'clusterStatus',
              'timestamp',
              'clusterVersions',
              'objectHealth',
              'vmHealth',
              'networkHealth',
              'limitHealth',
              'advCfgSync',
              'createVmHealth',
              'physicalDisksHealth',
              'hclInfo',
              'groups',
              'overallHealth',
              'overallHealthDescription',
              'clomdLiveness',
              'diskBalance'
          fetchFromCache: True to return the result from cache directly instead
              of running the full health check. The cache will be
              updated and keep the latest vSAN health summary check
              result either triggering from user on-demand request or
              the periodical vSAN health check for triggering health
              event/alarm. Default is False.
          perspective: The total amount of health checks is split into multiple different
              perspectives. This parameter controls which health checks are
              performed/returned. All supported values are defined
              in below enumerations:
              `pyVmomi.vim.vsan.VsanHealthPerspective`,
              `pyVmomi.vim.vsan.VsanHealthPerspective90`.
          hosts: Include the individual host(s) into the health check, with
              other hosts specified with the cluster parameter.
          spec: Health summary query specification `pyVmomi.vim.cluster.VsanClusterHealthQuerySpec`.
      
      Returns:
          Returns a health summary data object.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: If the perspective validation failed, or
              the API is queried from vSAN witness node, or
              any unexpected runtime error.
      """
      ...
   def QueryClusterHealthSummaryTask(self, cluster: pyVmomi.vim.ClusterComputeResource, hosts: list[pyVmomi.vim.HostSystem], includeDataProtectionHealth: _typing.Optional[bool], includeOnlineHealth: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      An asynchronous API to perform all of cluster wide health checks including
      the online health checks if CEIP is enabled and returns the task.
      
      After the
      task is finished, all of health check result will be kept in the cache and
      can be fetched from the synchronous API
      `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.queryClusterHealthSummary` by
      setting the parameter fetchFromCache as True, the perspective as 'defaultView'
      or unset and the parameter hosts should keep the same while leaving the other
      parameters as unset.
      If a new task is triggered while there's running task for same cluster,
      the new triggered task will be pending and return immediately once the
      running task is completed. The new triggered task will share the same
      health summary result as the running one.
      
      Args:
          cluster: The target cluster
          hosts: Include the individual host(s) into the health check, with
              other hosts specified with the cluster parameter
          includeDataProtectionHealth: This parameter is not used,
              and no data protection health will be collected.
          includeOnlineHealth: True to trigger vSAN online health.
              The default is True.
      
      Returns:
          task VC Task
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryVsanObjExtAttrs(self, cluster: pyVmomi.vim.ClusterComputeResource, uuids: list[str]) -> list[VsanObjectExtAttrs]:
      """
      Query the extended attributes for vSAN cluster objects.
      
      Args:
          cluster: The target cluster
          uuids: List of object UUIDs.
      
      Returns:
          a list of vSAN cluster object extended attributes of given objects
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryAllSupportedHealthChecks(self) -> list[VsanClusterHealthCheckInfo]:
      """
      Query basic info of all supported health checks
      
      Returns:
          a list of health check info constructed by testId, testName, groupId and groupName
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def QueryClusterNetworkPerfTest(self, cluster: pyVmomi.vim.ClusterComputeResource, multicast: bool, durationSec: _typing.Optional[int]) -> VsanClusterNetworkLoadTestResult:
      """
      Query the vSAN network performance and checks if it meets the bandwidth
      requirements.
      
      For multicast performance, the test is done by picking one
      host as the sender, and having all other hosts be receivers. For unicast
      performance, the test is done by having all hosts form a circular list,
      and every host in the list will be sending packets to the next host,
      while receiving packets from the previous host at the same time.
      For multicast test, the status in test result will be:
      - red if the speed is less than 20 MB/s
      - yellow if the speed is between 20MB/s and 50MB/s
      - green if the speed is larger than 50MB/s
        
      For unicast test, the status in test result will be:
      - red if the speed is 0 Mb/s
      - yellow if the speed is less than 850 Mb/s
      - green if the speed is larger than or equal to 850 Mb/s
        
      Note: Calling this API requires vCenter and all the connected hosts to
      support the same network performance testing capability(multicast or
      unicast). As vSAN is moving from multicast to unicast, only the unicast
      test method is supported since vSphere 6.7 Update 1 release. This API
      will return \"Not Supported\" in case the test method is not currently
      supported by this cluster. User could query VsanGetCapabilities() API
      to check whether the cluster supports the unicast network performance
      test. The test is supported if the 'netperftest' capability can be found
      on the vCenter and all the hosts in this cluster.
      This API is intended for network bandwidth diagnostics in the environment
      with no production workloads. It is not designed for network bandwidth
      monitoring with production workloads as it might impact the actual network
      utilization during the test.
      
      Args:
          cluster: The target cluster
          multicast: True to test vSAN multicast network performance.
              False to test vSAN unicast network performance.
          durationSec: The duration of the Network Performance test. Default is
              15 seconds if not set.
      
      Returns:
          The vSAN cluster network performance test result
      
      Raises:
          pyVmomi.vim.fault.NotFound: If the host can not be contacted to perform
              the operation.
          pyVmomi.vmodl.fault.NotSupported: If run multicast in vSphere 6.7 above
              version.
      """
      ...
   def QueryClusterNetworkPerfTask(self, cluster: pyVmomi.vim.ClusterComputeResource, spec: _typing.Optional[VsanClusterNetworkPerfTaskSpec]) -> pyVmomi.vim.Task:
      """
      Asynchronous implementation of network performance test API
      `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.queryClusterNetworkPerfTest`
      This returns task to monitor progress on success result is cached which can
      be retrieved using API using API
      `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.queryClusterNetworkPerfHistoryTest`
      with the same datastore in query spec.
      
      Args:
          cluster: The target cluster
          spec: The additional query spec for network performance health
      
      Returns:
          The VC task.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If cluster's hosts could not be contacted to
              perform the operation.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments.
      """
      ...
   def RunVmdkLoadTest(self, cluster: pyVmomi.vim.ClusterComputeResource, runname: str, durationSec: _typing.Optional[int], specs: list[pyVmomi.vim.host.VsanVmdkLoadTestSpec], action: _typing.Optional[str]) -> pyVmomi.vim.Task:
      """
      Deprecated: As of vSphere API 6.7.Run VMDK load test for the given duration second with the IO workload test
      parameter specifying in spec.
      
      The test includes three steps. Firstly,
      it will create VMDKs on each of cluster host, and then run the IO work test,
      at last, it will clean up the all of created VMDKs on each of host.Each of step
      can be run separately by specifying the parameter action. The default action
      \"fullrun\" will run all of three steps together
      Note: if this API is called directly on ESXi host, for any element of specs'
      vmdkCreateSpec.profile should be either unset or empty as SPBM is not available
      on ESXi host for profile conversion.
      
      Args:
          cluster: The target vCenter cluster.
          runname: The name for this test.
          durationSec: The duration time for each of VMDK load test.
          action: The possible actions are \"prepare\", \"run\" and \"cleanup\"
              and \"fullrun\". Default is \"fullrun\".
      
      Returns:
          task VC Task.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryVsanClusterHealthConfig(self, cluster: pyVmomi.vim.ClusterComputeResource) -> VsanClusterHealthConfigs:
      """
      Get the vSAN cluster health system configuration for the cluster
      Note when the API is called directly from an ESXi host, the configuration
      options may differ from that of from the vCenter.
      
      It returns only ones that
      may be meaningful to the ESXi host and the health service itself.
      
      Args:
          cluster: The target vCenter cluster
      
      Returns:
          The vSAN cluster health service configuration
      """
      ...
   def QueryVsanClusterHealthCheckInterval(self, cluster: pyVmomi.vim.ClusterComputeResource) -> int:
      """
      Get the periodical vSAN health check interval (in minutes) for the cluster.
      
      The periodical vSAN health check will perform a full vSAN health
      check at the fix interval which can be used in refreshing the cache as well as
      triggering the health event and alarm as the supplement of host event based auto
      cache refresh mechanism
      
      Args:
          cluster: The target vCenter cluster
      
      Returns:
          The periodical health check interval in minutes. Return 0 indicates
          the scheduled health check is disabled
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def SetVsanClusterHealthCheckInterval(self, cluster: pyVmomi.vim.ClusterComputeResource, vsanClusterHealthCheckInterval: int) -> None:
      """
      Set the periodical vSAN health check interval (in minutes) for the cluster.
      
      The periodical vSAN health check will perform a full vSAN health
      check at the fix interval which can be used in refreshing the cache as well as
      triggering the health event and alarm as the supplement of host event based auto
      cache refresh mechanism.
      Smaller value will perform the vSAN health more frequently to keep the cache
      to be more up-to-date but will increase the system overhead and vice versa.
      The default value is 1 hour.
      
      Args:
          cluster: The target vCenter cluster
          vsanClusterHealthCheckInterval: The vSAN cluster periodical health check
              interval in minutes. The value 0 will disable the
              periodical health check
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def GetVsanClusterSilentChecks(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[str]:
      """
      Get the user configured silent health check list of the cluster.
      
      This API will not return the system configured silent health check
      items. vSAN will automatically configure the following health check
      items in the following conditions:
      - HCL DB auto update in the air gap case.
        
      This API only supported on vCenter.
      
      Args:
          cluster: The target VC cluster
      
      Returns:
          The list of all silent health checks testIds
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def SetVsanClusterSilentChecks(self, cluster: pyVmomi.vim.ClusterComputeResource, addSilentChecks: list[str], removeSilentChecks: list[str]) -> bool:
      """
      Set silent health check list of the cluster.
      
      Specify [testId/groupId] for 'addSilentChecks' to add add health
      checks to silent list.
      Specify [testId/groupId] for 'removeSilentChecks' to remove health
      checks from silent list.
      To restore the whole silent list, set 'removeSilentChecks' = ['all'].
      After the silent health check list is updated, it is recommended to
      refresh the vSAN cluster health summary to get the updated result.
      The health check items in the silent list should be skipped, and labeled
      with 'skipped' status.
      Note:
      - If groupId is added to silent list, all the checks under this
        group would be silent.
      - If groupId is removed from silent list, all the checks under
        this group would back to normal.
      - If given invalid testId/groupId, it will throw exception.
      - This method will do add first and then remove. So if the given
        health check is in both add and remove list, it would NOT be
        silent in the end.
      - This API only supported on vCenter.
      
      Args:
          cluster: The target vCenter cluster
          addSilentChecks: The health checks/groups to silent.
          removeSilentChecks: The health checks/groups to restore.
      
      Returns:
          True to indicate the value being set successfully.
          No return otherwise.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def SetVsanClusterTelemetryConfig(self, cluster: pyVmomi.vim.ClusterComputeResource, vsanClusterHealthConfig: VsanClusterHealthConfigs) -> None:
      """
      Set the vSAN clsuter CEIP (Customer Experience Improvement Program)
      configuration.
      
      The configuration includes the interval time for the periodical CEIP telemetry data
      collector and the network proxy for sending vSAN telemetry data as well as
      HCL updating and uploading vSAN support bundle. Notice this proxy will be shared
      across all of vCenter clusters.
      The default interval is 1 week.
      
      Args:
          cluster: The target vCenter cluster
          vsanClusterHealthConfig: The vSAN cluster CEIP configuration
      """
      ...
   def TestVsanClusterTelemetryProxy(self, proxyConfig: VsanClusterTelemetryProxyConfig) -> bool:
      """
      Test the vSAN proxy configuration, which is used for downloading,
      HCL DB, sending vSAN telemetry data and uploading support bundle.
      
      Return true if the proxy works fine. This API will take several of seconds
      to return if given wrong proxy.
      
      Args:
          proxyConfig: The proxy configuration
      
      Returns:
          True indicates the proxy test is successful
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def SendVsanTelemetry(self, cluster: pyVmomi.vim.ClusterComputeResource) -> None:
      """
      Collecting vSAN telemetry for the given vCenter cluster and send to VMware
      phonehome server.
      
      Args:
          cluster: The vCenter cluster for collecting vSAN telemetry data
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def RepairClusterObjectsImmediate(self, cluster: pyVmomi.vim.ClusterComputeResource, uuids: list[str]) -> pyVmomi.vim.Task:
      """
      Repair the absent or degraded vSAN object immediately under
      the cluster.
      
      The task triggered by this API will be finished after
      putting all of the required objects into repairing queue, but it doesn't
      mean the repair process is done or successful. The completing time for
      repairing all of objects is unpredictable and depends on vSAN
      backend.
      
      Args:
          cluster: The VC cluster.
          uuids: The object UUIDs need to be repaired.
              Unset to fix all of objects under the cluster
      
      Returns:
          task VC Task
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def UpdateDefaultDSPolicyRecommendation(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task:
      """
      Update the cluster datastore default policy recommendation for this cluster.
      
      Setting this property will result into a task which updates the SPBM policy.
      
      Args:
          cluster: The VC cluster.
      
      Returns:
          task VC Task
      
      Raises:
          pyVmomi.vim.fault.NotFound: when specified cluster does not exist
          pyVmomi.vim.fault.VsanFault: If unexpected error happened during update
              policy, such as spbm not available
      """
      ...
   def QueryClusterCreateVmHealthHistoryTest(self, cluster: pyVmomi.vim.ClusterComputeResource, count: _typing.Optional[int], datastore: _typing.Optional[pyVmomi.vim.Datastore]) -> list[VsanClusterCreateVmHealthTestResult]:
      """
      Query the historical create VM test result for the vCenter cluster.
      
      The
      historical data is only saved into memory and will disappear after the
      service is restart or shut down.
      
      Args:
          cluster: The vCenter cluster
          count: Collect the last test data for the given number at most.
              Default to get the latest one historical data
          datastore: The datastore where the create vm test has been run.
              It could be the local datastore or the remote datastore
              that is mounted to the cluster. By default it will run
              with local vSAN datastore.
      
      Returns:
          The VM creation test results.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If cluster's hosts could not be contacted to
              perform the operation.
      """
      ...
   def QueryClusterNetworkPerfHistoryTest(self, cluster: pyVmomi.vim.ClusterComputeResource, count: _typing.Optional[int], spec: _typing.Optional[VsanClusterNetworkPerfTaskSpec]) -> list[VsanClusterNetworkLoadTestResult]:
      """
      Query the historical network performance test result for the vCenter cluster.
      
      The historical data is only saved into memory and will disappear after the
      service is restart or shut down.
      
      Args:
          cluster: The vCenter cluster
          count: Collect the last test data for the given number at most.
              Default to get the latest one historical data.
          spec: The additional query spec for query network performance health
              test history.
      
      Returns:
          The vSAN cluster network performance test results.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If host could not be contacted to perform
              the operation.
      """
      ...
   def QueryClusterVmdkLoadHistoryTest(self, cluster: pyVmomi.vim.ClusterComputeResource, count: _typing.Optional[int], taskId: _typing.Optional[str]) -> list[VsanClusterVmdkLoadTestResult]:
      """
      Deprecated: As of vSphere API 6.7.Query the historical vSAN storage test result for the vCenter cluster.
      
      The historical data is only saved into memory and will disappear after the
      service is restart or shut down.
      
      Args:
          cluster: The vCenter cluster
          count: Collect the last test data for the given number at most.
              Default to get the latest one historical data.
          taskId: The task Id which run the VMDK performance test. Default is None
              The count parameter will be ignored when the taskId is not None
      
      Returns:
          The vSAN storage load test results.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
      """
      ...
   def QueryClusterVmdkWorkloadTypes(self) -> list[VsanStorageWorkloadType]:
      """
      Deprecated: As of vSphere API 6.7.Query the pre-defined workload types for the VMDK performance test.
      
      Returns:
          The vSAN cluster VMDK workload type
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
      """
      ...
   def QueryAttachToSrHistory(self, cluster: pyVmomi.vim.ClusterComputeResource, count: _typing.Optional[int], taskId: _typing.Optional[str]) -> list[VsanAttachToSrOperation]:
      """
      Query the historical attach to SR operation result for the vCenter cluster.
      
      The historical data is only saved into memory and will disappear after the
      service is restart or shut down.
      
      Args:
          cluster: The vCenter cluster
          count: Collect the last test data for the given number at most.
              Default to get the latest one historical data.
          taskId: The task Id which run the attach to SR operation.Default is None
              The count parameter will be ignored when the taskId is not None
      
      Returns:
          The attach to SR operation results
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def AttachVsanSupportBundleToSr(self, cluster: pyVmomi.vim.ClusterComputeResource, srNumber: str) -> pyVmomi.vim.Task:
      """
      Collect vSAN and vCenter support bundle and upload to VMware for the given
      SR (Service Request).
      
      The collected support bundles including vSAN health
      and tracing log bundle, all of ESXi host support bundle and VC support bundle
      The upload process will be in three stages separately with the order of
      bundle size to avoid possible time out, which are vCenter bundles, small high
      importance ESXi/vSAN manifests, vSAN traces and lower priority ESXi
      manifests. The network proxy for uploading is also supported by calling
      SetVsanClusterTelemetryConfig() in advance.
      
      Args:
          cluster: The vCenter cluster
          srNumber: The Customer Service Request number ID
      
      Returns:
          task vCenter Task
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def GetClusterHclInfo(self, cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource], includeHostsResult: _typing.Optional[bool], includeVendorInfo: _typing.Optional[bool], esxRelease: _typing.Optional[str], querySpec: _typing.Optional[pyVmomi.vim.vsan.VsanHclQuerySpec]) -> VsanClusterHclInfo:
      """
      Fetch HCL information including the HCL DB status in general and all devices
      used by vSAN on all hosts in the cluster(if any).
      
      Args:
          cluster: The target vCenter cluster. Set to NULL if only intent to get
              the HCL DB status in general
          includeHostsResult: True to include the HCL information for
              each of host in the cluster.
          includeVendorInfo: Include the vendor tool information in the result
          esxRelease: The ESXi release version which HCL is computed against
      
      Returns:
          The HCL information for the cluster
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def GetHclInfoForVsanEligibleDisks(self, querySpec: pyVmomi.vim.vsan.VsanHclQuerySpec) -> VsanClusterHclInfo:
      """
      Fetch HCL information for all vSAN ESA eligible disks of the target
      object which can be a vSAN cluster or a list of hosts.
      
      Check
      `pyVmomi.vim.vsan.VsanHclQuerySpec` for more details.
      Note that it only returns disk related HCL information, the fields of other
      hardware components like CPU, physical NIC will be unset.
      
      Args:
          querySpec: Provide the capability to customize the query
      
      Returns:
          The HCL information for the cluster
      
      Raises:
          pyVmomi.vim.fault.NotFound: If host could not be contacted to perform the operation.
          pyVmomi.vim.fault.VsanFault: If unexpected error happened during the query, such as the
              cluster HCL info is unable to be retrieved, etc.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def DownloadHclFile(self, sha1sums: list[str]) -> pyVmomi.vim.Task:
      """
      Deprecated: As of vSphere API 8.0.Download driver/firmware from the URL extracted from HCL database by
      'id' and 'md5sum'.
      
      The content will be save on the vCenter storage with
      the auto-generated filename. The checksum of content will be checked
      after content is saved on the disk.
      
      Returns:
          task Task
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def GetClusterHclConstraints(self, cluster: pyVmomi.vim.ClusterComputeResource, release: str) -> pyVmomi.vim.vsan.VsanHclReleaseConstraint:
      """
      Get the HCL driver/firmware constraints for PCIe devices used by vSAN in the
      cluster.
      
      Args:
          cluster: The target vSAN cluster
          release: The target vSphere release
      
      Returns:
          The HCL driver constraints for all the PCIe device used by vSAN, and
          current firmware versions of that device in the cluster.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: If unexpected error happened during the query, such as the
              cluster HCL info is unable to be retrieved, etc.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def GetDiskHclConstraints(self, release: _typing.Optional[str], diskModels: list[pyVmomi.vim.vsan.VsanDiskModelInfo]) -> list[pyVmomi.vim.vsan.VsanHclDiskConstraint]:
      """
      Get the vSAN HCL constraints for disk drives.
      
      Args:
          release: The target vSphere release. If not provided, HCL constraints
              for all the supported releases will be returned.
          diskModels: The disk models to query. If provided, the HCL constraints
              with matching disk model info as in the query options will
              be returned.
      
      Returns:
          The HCL constraints for all the disk drives.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: If unexpected error happened during the query, such as the
              cluster HCL info is unable to be retrieved, etc.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def GetClusterReleaseRecommendation(self, cluster: pyVmomi.vim.ClusterComputeResource, minor: list[str], major: list[str]) -> list[pyVmomi.vim.vsan.VsanHclReleaseConstraint]:
      """
      Get the vSAN recommendation of ESXi releases to update for a cluster, and
      the associated HCL device constraints to comply for those releases.
      
      Args:
          cluster: The target vSAN cluster
          minor: A list of minor update releases. E.g., ['ESXi 6.7 U2']
          major: A list of major update releases. E.g., ['ESXi 6.8', 'ESXi 7.0']
      
      Returns:
          A list of VsanHclReleaseConstraint consists of: Hcl Constraints for
          one recommended minor release(if applicable) and Hcl Constraints for
          one recommended major release(if applicable). If none of the minor or
          major releases are preferred by vSAN, an empty list will be returned.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: If unexpected error happened during the query, such as
              the releases to query is not recognized or supported by
              vSAN, or vSAN is not able to retrieve the HCL info from
              the cluster, etc.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def PurgeHclFiles(self, sha1sums: list[str]) -> None:
      """
      Deprecated: As of vSphere API 8.0.Purge driver/firmware that was previously put on vCenter (either
      via download from URL or upload to vCenter).
      
      Returns:
          task Task
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def DownloadAndInstallVendorTool(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.Task:
      """
      Deprecated: As of vSphere API 8.0.Download and install the vendor tool required for the target cluster.
      
      API iterate thru all the update items for the given cluster and download
      the all the vendor tools required by the cluster. Vendor tool update item
      is specified by vibSpecType as 'tool'. Download of vendor tool will be
      skipped if tool is already present on vCenter storage. Check
      VsanDownloadHclFile_Task for the details about download. After download
      vendor tools will be installed on the hosts referenced by the vibSpec of
      vendor tools.
      
      Returns:
          task Task
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def UploadHclDb(self, db: str) -> bool:
      """
      Upload a DB file in JSON format.
      
      The DB will replace any existing DB, even
      if the existing DB may appear newer.
      The API at host level is for internal use.
      
      Args:
          db: The new DB, in base64 encoded, gzipped JSON format
      
      Returns:
          Always return True, or throw exception. False is never returned.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def UpdateHclDbFromWeb(self, url: _typing.Optional[str]) -> bool:
      """
      Downloads the HCL database from the VMware official website
      http://partnerweb.vmware.com/service/vsan/all.json.
      
      The DB will replace any existing DB, even if the existing DB
      may appear newer. Caller can supply a custom URL. If not provided,
      DB is downloaded from its standard location on vmware.com.
      
      Args:
          url: The URL for downloading the HCL DB. Unset to use the official
              standard location on vmware.com
      
      Returns:
          Always return True, or throw exception. False is never returned.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...
   def RebalanceCluster(self, cluster: pyVmomi.vim.ClusterComputeResource, targetHosts: list[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task:
      """
      Proactive rebalance the vSAN objects on the cluster hosts based
      on the vSAN disks usage when the disks are in imbalance status.
      
      The typical use case will be adding new host/disk into the vSAN
      cluster. Users should be aware that rebalancing causes additional
      background IO requires for data movements
      
      Args:
          cluster: The vCenter cluster
          targetHosts: Leave this unset
      
      Returns:
          task vCenter Task to track the rebalance process on the hosts. The task
          will be completed if all of hosts complete the rebalance
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def StopRebalanceCluster(self, cluster: pyVmomi.vim.ClusterComputeResource, targetHosts: list[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task:
      """
      Stop proactive rebalance the vSAN objects on the cluster hosts
      
      Args:
          cluster: The vCenter cluster
          targetHosts: Leave this unset
      
      Returns:
          task vCenter Task to track the rebalance stop process. The task will
          be completed if all of hosts have stopped the rebalance
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def IsRebalanceRunning(self, cluster: pyVmomi.vim.ClusterComputeResource, targetHosts: list[pyVmomi.vim.HostSystem]) -> bool:
      """
      Check whether the proactive rebalance is running or not against the
      target cluster or the hosts
      
      Args:
          cluster: The target vCenter cluster.
          targetHosts: Leave this unset
      
      Returns:
          True if any of host has running rebalance process
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def SetLogLevel(self, level: _typing.Optional[str]) -> None:
      """
      Set the vSAN health log level which will be taken effect immediately.
      
      This setting will be refreshed and reverted to default INFO log level after
      vCenter system or health service is restarted. Setting the default log level
      as INFO in production because higher levels lead to too much log volume
      (reduced performance and too quick log rotation), while lower levels will not
      have enough information for troubleshooting by VMware support.
      
      Args:
          level: The log level to set. Unset will set the log level to the
              default log level as INFO. See all log levels through
              `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.VsanHealthLogLevelEnum`
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def QuerySmartStatsSummary(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[pyVmomi.vim.host.VsanSmartStatsHostSummary]:
      """
      Query vSAN physical disks S.M.A.R.T.
      
      stats across all hosts
      in the target cluster.
      
      Args:
          cluster: The target cluster
      
      Returns:
          The vSAN physical disks S.M.A.R.T. stats
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
      """
      ...
   def QueryVsanProxyConfig(self) -> VsanClusterTelemetryProxyConfig:
      """
      Get the vSAN proxy configuration.
      
      Return the proxy configuration for vSAN. The method gets the proxy
      configured via UI settings or vsan config file. If no proxy is configured,
      the api tries to check if any system level proxy is set.
      
      Returns:
          The vSAN proxy configuration
      """
      ...
   def QueryClusterHistoricalHealth(self, spec: VsanHistoricalHealthQuerySpec) -> list[VsanClusterHealthSummary]:
      """
      It queries vSAN cluster historical health information based
      on the query spec.
      - Query general historical health summary.
        If no groupId and testId specified in the query spec,
        it aggregates all the historical vSAN cluster health status
        for the given time range. Then returns a general health summary
        with only overallHealth, test group IDs, group healths,
        test IDs and test healths.
      - Query health status history for a certain health check.
        If groupId and testId are specified, and start time doesn't
        equal to end time, the result will only contain the historical
        testHealths for the given time range of the target health check.
      - Query a snapshot detail for a certain health check.
        If groupId and testId are specified, and start time equals to
        end time, the result will contain a full testDetail for the certain
        timestamp of the target health check.
      
      Args:
          spec: The query spec.
      
      Returns:
          vSAN cluster health summary with historical information.
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
          pyVmomi.vmodl.fault.InvalidArgument: Exception for invalid input arguments.
              For example, if given time range
              is more than one month. Or end time is
              smaller than the start time.
      """
      ...
   def SetVsanVcgMappingForHwDevices(self, spec: pyVmomi.vim.vsan.VsanHwToVcgInfoMappingSpec) -> bool:
      """
      This API can help to build up the mapping from the hardware information to
      the vSAN VCG entry.
      
      The hardware information in the spec can be fetched by
      `pyVmomi.vim.cluster.VsanVcClusterHealthSystem.getClusterHclInfo`.
      
      Args:
          spec: Refer to `pyVmomi.vim.vsan.VsanHwToVcgInfoMappingSpec`
      
      Returns:
          True to indicate the VCG product IDs are set successfully.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If an unexpected error happened during the process.
      """
      ...


class VsanVcDiskManagementSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   VimClusterVsanVcDiskManagementSystem enhances vSAN disk
   management part, provides vSAN all flash disk group support,
   exposes more detailed information of vSAN disk group, helps
   on configure and manage vSAN disk group.
   
     
   It deprecates APIs `pyVmomi.vim.host.VsanSystem.addDisks` and
   `pyVmomi.vim.host.VsanSystem.initializeDisks`, exposes
   `pyVmomi.vim.vsan.host.DiskMapInfoEx` through API
   `pyVmomi.vim.cluster.VsanVcDiskManagementSystem.queryDiskMappings`,
   to present whether a disk group is all flash, and whether
   deduplication and compression is enabled on this disk group,
   and deprecates `pyVmomi.vim.vsan.host.ConfigInfo.StorageInfo.diskMapping`
   exposed by `pyVmomi.vim.host.VsanSystem.config`.  
   The ManagedEntity can be accessed through MOID of
   vsan-disk-management-system, through vSAN service at vCenter
   server side.
   """
   def RetrieveAllFlashCapabilities(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[pyVmomi.vim.vsan.host.VsanHostCapability]:
      """
      Retrieve capabilities for hosts reside in specified cluster,
      to figure out whether all flash disk group is supported by
      hosts' ESXi softwares, and whether they are licensed.
      
      Args:
          cluster: Target cluster, of which hosts' capabilities
              will be queried;
      
      Returns:
          vim.vsan.host.VsanHostCapability[]
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def InitializeDiskMappings(self, spec: pyVmomi.vim.vsan.host.DiskMappingCreationSpec) -> pyVmomi.vim.Task:
      """
      This API is used to create new vSAN disk groups or attach
      more disks into existing vSAN disk group on specified host.
      
      It deprecates APIs `pyVmomi.vim.host.VsanSystem.addDisks` and
      `pyVmomi.vim.host.VsanSystem.initializeDisks`, to support creating both hybrid
      and all flash disk group.
      Scsi disks eligible for vSAN service, could be retrieved through
      API `pyVmomi.vim.host.VsanSystem.queryDisksForVsan`.
      If the \"creationType\" of the given spec is set to \"vsandirect\", then
      it will create vSAN direct datastores on each specified SSD and HDD.
      
      Args:
          spec: The specification to create vSAN disk group. Please
              reference to VimVsanHostDiskMappingCreationSpec;
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If below issues exist:
              1. Specified host doesn't exist;
              2. User doesn't have Host.Config.Storage
                 privilege on specified host;
              3. Specified host is not connected to
                 vCenter server;
              4. If requests to create all flash disk group
                 but host's ESX software doesn't support this
                 feature;
              5. If requests to create all flash disk group
                 but host is not licensed to support this
                 feature;
              6. If requests to append disks to existing
                 disk group, but specified more than one disks
                 for cache tier;
              7. If none of specified disks for capacity tier
                 is eligible for vSAN;
      """
      ...
   def QueryDiskMappings(self, host: pyVmomi.vim.HostSystem) -> list[pyVmomi.vim.vsan.host.DiskMapInfoEx]:
      """
      Get detailed information of vSAN disk groups managed by specified host,
      for each disk group, includes:
      Disk structure, presents as disk for cache tier, and disks for capacity tier;
      Whether is in-use for vSAN I/O by this host;
      Whether is all flash disk group;
      Whether vSAN deduplication and compression are enabled on this disk group.
      
      Args:
          host: Target host to query.
      
      Returns:
          List of DiskMapInfoEx, please reference to VimVsanHostDiskMapInfoEx.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If below issues exist:
              1. Specified host doesn't exist;
              2. Specified host is not connected to
                 vCenter server;
              3. Any unexpected runtime error;
      """
      ...
   def QueryVsanManagedDisks(self, host: pyVmomi.vim.HostSystem, filterSpec: _typing.Optional[pyVmomi.vim.vsan.host.QueryVsanDisksSpec]) -> _typing.Optional[pyVmomi.vim.vsan.host.VsanManagedDisksInfo]:
      """
      Get detailed information of all vSAN managed disks, which
      include disk groups, storage pool disks in vSAN datastore and all of
      vSAN direct storages for the specified host.
      
      The output can be filtered
      to show only disk group or storage pool disks or vSAN direct disks. It can
      also be filtered to show details for an individual disk on the host by
      specifying filter criteria through `pyVmomi.vim.vsan.host.QueryVsanDisksSpec`.
      The API
      `pyVmomi.vim.cluster.VsanVcDiskManagementSystem.queryDiskMappings`
      will be deprecated and replaced with this API.
      
      Args:
          host: Target host to query.
          filterSpec: Specification to filter vSAN disks.
              This spec can be used to filter query results by disktype types
              (diskGroup/storagePool/directDisk) or by diskName. If this spec is
              not specified, it will return all vSAN disks in the cluster.
              Refer `pyVmomi.vim.vsan.host.QueryVsanDisksSpec` for more details.
      
      Returns:
          All of vSAN managed disks including vSAN disk groups and vSAN
          direct storages
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If below issues exist:
              1. Specified host doesn't exist;
              2. Specified host is not connected to
                 vCenter server;
              3. Any unexpected runtime error;
      """
      ...
   def QueryClusterDataEfficiencyCapacityState(self, cluster: pyVmomi.vim.ClusterComputeResource) -> pyVmomi.vim.vsan.DataEfficiencyCapacityState:
      """
      Retrieve logical capacity, logical capacity used, physical capacity, physical
      capacity used and data efficiency metadata of a data efficiency enabled
      cluster.
      
      Args:
          cluster: The target cluster.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def RebuildDiskMapping(self, host: pyVmomi.vim.HostSystem, mapping: pyVmomi.vim.vsan.host.DiskMapping, maintenanceSpec: pyVmomi.vim.host.MaintenanceSpec) -> pyVmomi.vim.Task:
      """
      This API is used to rebuild an existing vSAN disk mapping on the
      specified host.
      
      Please note that the API does not support rebuilding unmounted DGs.
      Rebuild disk mapping is done in two steps:
      1\\. remove the existing disk mapping with user specified data evacuation mode;
      2\\. perform a trim operation on every disk in DG.
      3\\. re-create a new disk mapping with the same set of disks.
      Removal of a disk mapping may cause data movement so a disk data evacuation
      resource check `pyVmomi.vim.vsan.VsanResourceCheckSystem.performResourceCheck`
      will be done before removing the disk mapping. Before re-creating new disk
      mapping, the disks will be trimmed for refreshing possible bad blocks in the
      meta-data section of the disks.
      
      Args:
          host: Target host to rebuild.
          mapping: The disk mapping to be rebuilt from VSAN usage.
          maintenanceSpec: Specifies the data evacuation mode.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If below issues exist:
              1. Specified host doesn't exist;
              2. User doesn't have Host.Config.Storage
                 privilege on specified host;
              3. Specified host is not connected to
                 vCenter server;
              4. Resource check completes with \"red\"
                 status;
      """
      ...
   def UnmountDiskMappingEx(self, cluster: pyVmomi.vim.ClusterComputeResource, mappings: list[pyVmomi.vim.vsan.host.DiskMapping], maintenanceSpec: pyVmomi.vim.host.MaintenanceSpec) -> pyVmomi.vim.Task:
      """
      Unmount vSAN disk mapping(s) in a vSAN cluster with the specified
      data evacuation mode.
      
      Disk mapping(s) will be unmounted one by one with the specified data
      evacuation mode. Unmount a disk mapping may cause data movement so a
      disk data evacuation resource check
      `pyVmomi.vim.vsan.VsanResourceCheckSystem.performResourceCheck`
      will be done before unmounting each disk mapping.
      
      Args:
          cluster: The vSAN cluster which owns the given disk mapping(s).
          mappings: List of disk mapping(s) to be unmounted.
          maintenanceSpec: Specifies the data evacuation mode.
      
      Returns:
          A task to monitor the progress of disk mapping(s) unmount operation.
          Upon successful completion of the returned task, its
          `pyVmomi.vim.TaskInfo.result` field will be populated with a
          `pyVmomi.vim.vsan.host.DiskMapResult`[] filled with details for each
          disk mapping.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If resource check completes with \"red\" status or any error
              happens during the resource check stage or actual
              disk mapping(s) unmount stage.
      """
      ...
   def RemoveDiskMappingEx(self, cluster: pyVmomi.vim.ClusterComputeResource, mappings: list[pyVmomi.vim.vsan.host.DiskMapping], maintenanceSpec: pyVmomi.vim.host.MaintenanceSpec) -> pyVmomi.vim.Task:
      """
      Remove vSAN disk mapping(s) from use in a vSAN cluster with the
      specified data evacuation mode.
      
      Disk mapping(s) will be removed one by one with the specified data
      evacuation mode. Removing a disk mapping may cause data movement so a
      disk data evacuation resource check
      `pyVmomi.vim.vsan.VsanResourceCheckSystem.performResourceCheck`
      will be done before removing each disk mapping.
      
      Args:
          cluster: The vSAN cluster which owns the given disk mapping(s).
          mappings: List of disk mapping(s) to be removed.
          maintenanceSpec: Specifies the data evacuation mode.
      
      Returns:
          A task to monitor the progress of disk mapping(s) removal operation.
          Upon successful completion of the returned task, its
          `pyVmomi.vim.TaskInfo.result` field will be populated with a
          `pyVmomi.vim.vsan.host.DiskMapResult`[] filled with details for each
          disk mapping.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If resource check completes with \"red\" status or any error
              happens during the resource check stage or actual
              disk mapping(s) removal stage.
      """
      ...
   def RemoveDiskEx(self, cluster: pyVmomi.vim.ClusterComputeResource, disks: list[pyVmomi.vim.host.ScsiDisk], maintenanceSpec: pyVmomi.vim.host.MaintenanceSpec) -> pyVmomi.vim.Task:
      """
      Remove vSAN capacity-tier disk(s) from use in a vSAN cluster with the
      specified data evacuation mode or remove vSAN direct disk(s).
      
      It will auto-detect whether the disk(s) provided belong to
      vSAN capacity-tier disk or vSAN direct.
      If the disk(s) belong to vSAN capacity-tier disk, then vSAN disk
      will be removed. If the disk(s) belong to vSAN direct, then the
      vSAN direct disk(s) will be removed.
      For vSAN disk(s) removal, disk(s) will be removed one by one
      with the specified data evacuation mode.
      Removing a disk may cause data movement so a
      disk data evacuation resource check
      `pyVmomi.vim.vsan.VsanResourceCheckSystem.performResourceCheck`
      will be done before removing each disk.
      Note: This method cannot be used to remove the cache-tier disk or the last
      capacity-tier disk of a disk mapping since that will cause the whole disk
      mapping to be removed. Use
      `pyVmomi.vim.cluster.VsanVcDiskManagementSystem.removeDiskMappingEx` instead if that is
      the case.
      For vSAN direct disk(s) removal, the storage system build on top of
      these vSAN direct disk(s) will be destroyed one by one with the specified
      data evacuation mode.
      
      Args:
          cluster: The vSAN cluster which owns the given vSAN disk(s)
              and(or) vSAN direct disk(s).
          disks: List of vSAN disk(s) to be removed.
          maintenanceSpec: Specifies the data evacuation mode.
      
      Returns:
          A task to monitor the progress of disk(s) removal operation.
          If the removal operation includes vSAN disk(s) removal,
          then upon successful completion of the returned task, its
          `pyVmomi.vim.TaskInfo.result` field will be populated with a
          `pyVmomi.vim.vsan.host.DiskResult`[] filled with details for each
          vSAN disk.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If resource check completes with \"red\" status or any other
              error happens during the resource check stage or actual
              disk(s) removal stage for vSAN disk(s).
              If the specified disk is the last capacity-tier disk in a
              disk mapping, a more specific
              vim.fault.DiskIsLastRemainingNonSSD (which is a subclass
              of VsanFault) will be thrown instead.
      """
      ...
   def AddStoragePoolDisks(self, specs: list[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec]) -> pyVmomi.vim.Task:
      """
      This API can be used to add new disk(s) to the storage pool for vSAN ESA
      consumption.
      
      If StoragePoolDiskType is specified as 'SingleTier', disks will be added to
      'Single Tier' storagepool.
      Eligible disks for storagepool can be queried from 'QueryDisksForVsan'
      `pyVmomi.vim.host.VsanSystem.queryDisksForVsan`.
      
      Args:
          specs: The specifications to add disks to vSAN storage pool. Please
              reference to VimVsanHostAddStoragePoolDiskSpec.
              Multiple specs can be used by AddStoragePoolDisks to add disks
              on different hosts in one API call.
              All hosts should in same vSAN cluster.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If below issues exist:
              1. Specified host doesn't exist;
              2. User doesn't have Host.Config.Storage
                 privilege on specified host;
              3. Specified host is not connected to
                 vCenter server;
              4. If none of specified disks for storage
                 pool is eligible for vSAN ESA;
      """
      ...
   def DeleteStoragePoolDisk(self, cluster: pyVmomi.vim.ClusterComputeResource, spec: pyVmomi.vim.vsan.host.DeleteStoragePoolDiskSpec) -> pyVmomi.vim.Task:
      """
      This API can be used to delete a single or multiple disks from storage pool.
      
      The disk(s) can be specified by their uniquely identifiable disk uuid.
      
      Args:
          cluster: The vSAN cluster which owns the given storage pool disk(s).
          spec: The specification to delete vSAN storage pool. Please
              reference to VimVsanHostDeleteStoragePoolDiskSpec.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any error happens during storage pool removal stage.
      """
      ...
   def UnmountStoragePoolDisks(self, cluster: pyVmomi.vim.ClusterComputeResource, spec: pyVmomi.vim.vsan.host.DeleteStoragePoolDiskSpec) -> pyVmomi.vim.Task:
      """
      This API can be used to unmount a single or multiple disks from the storage
      pool.
      
      The disk(s) can be specified by their uniquely identifiable disk UUID.
      Storage pool disk(s) will be unmounted with the specified data evacuation
      mode. Unmount a storage pool disk may cause data movement so a disk data
      evacuation resource check
      `pyVmomi.vim.vsan.VsanResourceCheckSystem.performResourceCheck` will be done
      before unmounting each storage pool disk.
      
      Args:
          cluster: The vSAN cluster which owns the given storage pool disk(s).
          spec: The specification to unmount vSAN storage pool. Please
              reference to VimVsanHostDeleteStoragePoolDiskSpec.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If resource check completes with \"red\" status or any error
              happens during the resource check stage or actual storage
              disk unmount stage.
      """
      ...


class VsanVcKmipServersHealth(pyVmomi.vmodl.DynamicData):
   """
   This class defines KMIP servers connection status on vCenter side.
   
   It has detailed KMS connection status, client/servers certificate status and
   expiration date.
   
   Attributes:
       health: The overall KMIP servers health.
       error: If error is set, it means there are issues when trying to retrieve
           Key Management Servers status.
           
           The error message will describe the
           possible issues, such as \"Retrieve KMIP servers status timed out\".
       kmsProviderId: The Id of the KMS cluster to use for vSAN Encryption.
       kmsHealth: A list of the KMIP servers health result.
       clientCertHealth: The client certificate status.
           
           If the certificate is expired, the health
           is \"red\". If the certificate expires in 30 days, the health is \"yellow\".
           Otherwise the certificate health is \"green\".
       clientCertExpireDate: The client certificate expiry date.
       isAwsKms: Whether vSAN encryption is using AWS KMS.
       cmkHealth: The health status of Customer Master Key (CMK) from AWS KMS.
           
           This is only set when using AWS KMS for vSAN encryption.
       kekExpireHealth: KEK expiration state.
           
           'red' means that the KEK has expired or is going to expire
           in very close days(10 days by default), and 'yellow' means
           that the KEK will expire in certain days(30 days by default),
           and 'green' means that there is still a long time(more than
           30 days by default) before the KEK expires or the KEK will
           not expire.
       kekExpireDate: Key encryption key expiration date.
       hostKeyExpireHealth: Host Key expiration state.
           
           'red' means that the host key has expired or is going to expire
           in very close days(10 days by default), and 'yellow' means that
           the host key will expire in certain days(30 days by default),
           and 'green' means that there is still a long time(more than 30
           days by default) before the host key expires or the host key will
           not expire.
       hostKeyExpireDate: Host key expiration date.
   """
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
   """
   Result returned after running lifecycle checks containing check results
   and vSAN cluster configuration details required by lifecycle manager/vLCM.
   
   Attributes:
       status: The overall status of the lifecycle checks:
           green) All checks passed
           yellow) At least one yellow status check, no red status checks
           red) At least one red status check, yellow status checks also possible
       preCheckResults: The list of results for lifecycle checks.
           
           Check `pyVmomi.vim.vsan.LifecyclePreCheckResult` for details.
       configDetails: vSAN cluster configuration details.
   """
   status: str
   preCheckResults: list[pyVmomi.vim.vsan.LifecyclePreCheckResult] = []
   configDetails: pyVmomi.vim.vsan.LifecycleConfigDetails


class VsanVcLifecycleCheckSpec(pyVmomi.vmodl.DynamicData):
   """
   The specification for running lifecycle checks required by lifecycle
   manager/vLCM.
   
   Attributes:
       operation: The lifecycle operation for which checks should be performed.
           
           See `pyVmomi.vim.vsan.LifecycleCheckOperation` for all possible operations.
   """
   operation: str


class VsanVcStretchedClusterSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   vSAN stretched Cluster is a specific configuration implemented in
   environments where disaster/downtime avoidance is a key requirement.
   
   vSAN stretched Clusters with Witness Host refers to a deployment
   where a user sets up a vSAN cluster with 2 active/active sites with
   numbers of ESXi hosts between the two sites. The sites are connected via a
   high bandwidth/low latency link.
   The third site hosting the vSAN Witness Host is connected to both of
   the active/active data-sites. This connectivity can be via low bandwidth/high
   latency links.
   Each site is configured as a vSAN Fault Domain. The nomenclature used
   to describe a vSAN stretched Cluster configuration is X+Y+Z, where X is
   the number of ESXi hosts at data site A, Y is the number of ESXi hosts at data
   site B, and Z is the number of witness hosts at site C. Data sites are where
   virtual machines are deployed.
   The maximum configuration is 15+15+1 (31 nodes).  
   vSAN Remote Office / Branch Office Deployment, aka ROBO cluster,
   is a specific deployment of vSAN stretched cluster. A two-node
   vSAN cluster, and a vSphere vSAN witness host appliance as
   witness, forms a vSAN ROBO cluster. Copies of vSAN objects
   that make up a virtual machine are typically stored in two physical nodes,
   if one of the physical nodes is offline, it is still possible for virtual
   machines to run using the files located on another physical node. In the
   case where the hosts in a two-node cluster are unable to communicate across
   the network, the witness serves as a \"tie-breaker\" to achieve a quorum and
   enables the cluster to restart virtual machines impacted by an outage.
   Details to deploy a vSAN stretched cluster, please reference to API
   `pyVmomi.vim.cluster.VsanVcStretchedClusterSystem.convertToStretchedCluster`,
   and for ROBO cluster, please assign
   witness appliance to parameter 'witnessHost', and each physical host stands
   for a Fault Domain.  
   VsanVcStretchedClusterSystem is used to configure and manage vSAN
   stretched cluster. The ManagedEntity can be accessed through MOID of
   vsan-stretched-cluster-system, through vSAN service at vCenter server
   side.
   """
   def AddWitnessHost(self, cluster: pyVmomi.vim.ClusterComputeResource, witnessHost: pyVmomi.vim.HostSystem, preferredFd: str, diskMapping: _typing.Optional[pyVmomi.vim.vsan.host.DiskMapping], metadataMode: _typing.Optional[bool], storagePoolSpec: _typing.Optional[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec]) -> pyVmomi.vim.Task:
      """
      Add a host as witness host to vSAN cluster to re-enable vSAN
      stretched cluster.
      
      It is expected to be used in following scenarios:
      1\\. Stretched cluster is disabled by
      `pyVmomi.vim.cluster.VsanVcStretchedClusterSystem.removeWitnessHost`;
      2\\. Replace original witness host with a new one, this should happen
      when old witness host is out of service, such as host is down or removed
      from vCenter inventory;
      This function doesn't change existing Fault Domain configuration, and
      please be sure the old witness host was gone or out of service, because
      replacing witness host will reduce redundancy.
      Relative to API
      `pyVmomi.vim.cluster.VsanVcStretchedClusterSystem.convertToStretchedCluster`
      , it only takes care of
      witness host reconfiguration, vSAN cluster must already be configured
      for stretched cluster.
      
      Args:
          cluster: The target vSAN cluster to add/replace witness host;
          witnessHost: The witness host to be added into vSAN cluster.
              This host must be connected and managed by the same
              vCenter server, and cannot be a part of target
              cluster;
          preferredFd: The name of preferred Fault Domain;
          diskMapping: The diskMapping to be created on witness host. If
              disk claim is configured as auto-mode on witness host,
              this parameter is not required.
          metadataMode: True to indicate the host runs as metadata host instead
              of normal witness host. This is currently reserved by
              VMware internally to represent a different cluster type
              other than stretched cluster. Leave this unset for
              vSAN stretched cluster.
          storagePoolSpec: The specification to add disks to vSAN storage pool.
              This parameter cannot be set together with diskMapping
              param.
      
      Returns:
          vim.Task
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
          pyVmomi.vim.fault.InvalidState: If any host in target cluster is not
              connected to vCenter server;
          pyVmomi.vmodl.fault.InvalidArgument: If below issues exist:
              1\\. target cluster doesn't enable
              vSAN;
              2\\. witness host resides in target
              cluster;
              3\\. neither IPv4 nor IPv6 is properly
              configured for vSAN traffic
              on all hosts in target cluster;
              4\\. both diskMapping and storagePoolSpec
              are specified
          pyVmomi.vmodl.fault.NotEnoughLicenses: If any host in target cluster doesn't
              have vSAN stretched cluster license;
      """
      ...
   def RemoveWitnessHost(self, cluster: pyVmomi.vim.ClusterComputeResource, witnessHost: _typing.Optional[pyVmomi.vim.HostSystem], witnessAddress: _typing.Optional[str]) -> pyVmomi.vim.Task:
      """
      Remove witness host from the vSAN stretched cluster to disable
      vSAN stretched cluster.
      
      Detailed changes will happen on target
      cluster:
      1. vSAN on witness host will be disabled;
      2. Unicast agent setting will be removed from all
         data hosts in specified
         vSAN stretched cluster;
         
        
      Original Fault Domains for both two sites will be kept, and vSAN is
      still enabled on all data hosts.
      
      Args:
          cluster: The target cluster to disable;
          witnessHost: Witness host to remove;
          witnessAddress: The IP address of witness host used as unicast agent.
      
      Returns:
          vim.Task
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
          pyVmomi.vim.fault.InvalidState: If any host in target cluster is not
              connected to vCenter server;
          pyVmomi.vmodl.fault.InvalidArgument: If below issues exist:
              1. target cluster doesn't enable
                 vSAN;
              2. witness host is specified
                 but doesn't
                 match the in-use
                 configuration;
              3. target cluster is not vSAN
                 stretched cluster;
      """
      ...
   def ConvertToStretchedCluster(self, cluster: pyVmomi.vim.ClusterComputeResource, faultDomainConfig: VSANStretchedClusterFaultDomainConfig, witnessHost: pyVmomi.vim.HostSystem, preferredFd: str, diskMapping: _typing.Optional[pyVmomi.vim.vsan.host.DiskMapping], storagePoolSpec: _typing.Optional[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec]) -> pyVmomi.vim.Task:
      """
      This API is used to convert a traditional vSAN cluster to
      vSAN stretched cluster.
      
      It will help to:
      1. Configure vSAN cluster into two sites through
         vSAN Fault Domain setting;
      2. Add witness host and configure unicast communication
         at cluster wide;
      3. Setup preferred Fault Domain;
      4. Create vSAN disk group on witness host if
         auto-claim is not enabled on witness host;
         
        
      Relative to API
      `pyVmomi.vim.cluster.VsanVcStretchedClusterSystem.addWitnessHost`,
      it not only takes care of
      setting up witness host, but also help on vSAN sites configuration,
      to guarantee the vSAN cluster works in stretched mode.
      vSAN cluster already works in stretched mode, is not supported by
      this API.
      
      Args:
          cluster: The target cluster to be converted; It is expected
              to enable vSAN, but not a vSAN stretched
              cluster;
          faultDomainConfig: The mapping between Fault Domain and vSAN
              hosts reside in target cluster, to decide
              how to configure vSAN cluster into two
              sites;
          witnessHost: The witness host to be added into vSAN cluster.
              This host must be connected and managed by the same
              vCenter server, and cannot be a part of target
              cluster;
          preferredFd: The name of preferred Fault Domain;
          diskMapping: The diskMapping to be created on witness host. If
              disk claim is configured as auto-mode on witness host,
              this parameter is not required.
          storagePoolSpec: The specification to add disks to vSAN storage pool.
              This parameter cannot be set together with diskMapping
              param.
      
      Returns:
          vim.Task
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
          pyVmomi.vim.fault.InvalidState: If any host in target cluster is not
              connected to vCenter server;
          pyVmomi.vmodl.fault.InvalidArgument: If below issues exist:
              1. target cluster doesn't enable
                 vSAN;
              2. witness host resides in target
                 cluster;
              3. neither IPv4 nor IPv6
                 is properly
                 configured for vSAN traffic
                 on all hosts in target
                 cluster;
              4. target cluster is already a vSAN
                 stretched cluster;
              5. both diskMapping and storagePoolSpec
                 are specified;
      """
      ...
   def SetPreferredFaultDomain(self, cluster: pyVmomi.vim.ClusterComputeResource, preferredFd: str, witnessHost: _typing.Optional[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task:
      """
      Set preferred Fault Domain for a vSAN stretched cluster.
      
      This API could set/reconfigure preferred Fault Domain setting.
      
      Args:
          cluster: Target vSAN stretched cluster;
          preferredFd: The user friendly name of preferred Fault Domain;
          witnessHost: The witness host to apply preferred Fault Domain setting;
              if it is not specified, will take the in-use witness
              host configured at cluster side.
      
      Returns:
          vim.Task
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
          pyVmomi.vim.fault.InvalidState: If any host in target cluster is not
              connected to vCenter server;
      """
      ...
   def GetPreferredFaultDomain(self, cluster: pyVmomi.vim.ClusterComputeResource) -> _typing.Optional[VSANPreferredFaultDomainInfo]:
      """
      Query configuration of preferred Fault Domain of specified cluster.
      
      If call this API against vSAN service of version 6.5 and before,
      additional privilege Host.Inventory.EditCluster is required, please
      be noted.
      
      Args:
          cluster: Target cluster to query.
      
      Returns:
          VSANPreferredFaultDomainInfo which contains preferred Fault
          Domain's user friendly name and UUID. If specified cluster
          is not vSAN stretched cluster, both fields will be
          unset.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
          pyVmomi.vim.fault.InvalidState: If any host in target cluster is not
              connected to vCenter server;
      """
      ...
   def IsWitnessHost(self, host: pyVmomi.vim.HostSystem) -> bool:
      """
      Check whether specified host is a witness host.
      
      Args:
          host: The target host to check.
      
      Returns:
          true is host is a witness host,
          false is host is not a witness host.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
      """
      ...
   def GetWitnessHosts(self, cluster: pyVmomi.vim.ClusterComputeResource) -> list[VSANWitnessHostInfo]:
      """
      Query witness host configuration of specified cluster.
      
      Args:
          cluster: The target cluster to query;
      
      Returns:
          VSANWitnessHostInfo[] which contains witness host's UUID,
          ManagedEntity instance, preferred Fault Domain's user friendly
          name and UUID, IP address of unicast agent, and name of the Fault
          Domain that witness host resides in. If specified cluster in vSAN
          stretched cluster, all fields above will be set to actual setting,
          otherwise all fields will be unset.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
          pyVmomi.vim.fault.InvalidState: If any host in target cluster is not
              connected to vCenter server;
      """
      ...
   def RetrieveStretchedClusterVcCapability(self, cluster: pyVmomi.vim.ClusterComputeResource, verifyAllConnected: _typing.Optional[bool]) -> list[VSANStretchedClusterCapability]:
      """
      Query hosts' capabilities of supporting vSAN stretched cluster,
      which reside in specified cluster, to decide whether specified cluster
      supports vSAN stretched cluster feature.
      
      It could be used for
      any cluster, but only when all hosts reside in target cluster can
      support vSAN stretched cluster, it can be converted to
      vSAN stretched cluster.
      
      Args:
          cluster: The target cluster to query;
          verifyAllConnected: Whether to ignore disconnected hosts. If it is set
              to true, vim.fault.InvalidState will be met if any
              host in target cluster is disconnected; if it is set
              to false, disconnected hosts will be ignored. Default
              value is false. But a cluster with disconnected hosts
              cannot be converted to vSAN stretched cluster;
      
      Returns:
          List of VSANStretchedClusterCapability, to present whether each
          host can support vSAN stretched cluster.
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
          pyVmomi.vim.fault.InvalidState: If any host in target cluster is not
              connected to vCenter server and
              verifyAllConnected is set to true;
      """
      ...
   def IsWitnessVirtualAppliance(self, hosts: list[pyVmomi.vim.HostSystem]) -> list[pyVmomi.vim.host.VsanHostVirtualApplianceInfo]:
      """
      Return whether the host is a virtual appliance witness host
      for stretched cluster
      Witness host can be a VM deployed from vSAN witness server OVF, the VM added
      to vCenter datacenter as a ESXi host, and has no difference with other
      ESXi host in a stretched cluster, but the VM host can only used as witness
      host, UI need to know if the witness host is a virtual appliance, using this
      API can tell the host is a virtual appliance or not.
      
      Returns:
          dictionary of hosts' MO id and if the host is a virtual appliance
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
      """
      ...
   def QuerySharedWitnessCompatibility(self, sharedWitnessHost: pyVmomi.vim.HostSystem, roboClusters: list[pyVmomi.vim.ClusterComputeResource]) -> pyVmomi.vim.vsan.SharedWitnessCompatibilityResult:
      """
      Query whether a given host could be used as shared witness for a group of
      specified ROBO clusters.
      
      Result data would contain compatibility check result
      for both sharedWitnessHost and roboClusters.
      For sharedWitnessHost, it will check following items.
      1\\) Check whether given host is a witness host.
      2\\) Check whether this witness host has shared witness capability.
      3\\) Check whether clusters count would exceed per shared witness host's limit.
      For roboClusters, it will check following items.
      1\\) For a vSAN not enabled cluster, check whether it could be a candidate of
      ROBO cluster (cluster which has 2 hosts).
      2\\) For a vSAN enabled cluster, check whether it is a ROBO cluster (stretched
      cluster which has 2 hosts).
      3\\) For a ROBO cluster, check whether its component limit exceeds current
      shared witness host's component count limitation for individual cluster.
      
      Args:
          sharedWitnessHost: A host entity which would be used as a shared
              witness host.
          roboClusters: A list of ROBO clusters which would use
              sharedWitnessHost as their witness.
      
      Returns:
          SharedWitnessCompatibilityResult to present compatibility check
          result of given shared witness host and robo cluster list.
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: If this API is not supported on current platform.
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
      """
      ...
   def QueryWitnessHostClusterInfo(self, witnessHost: pyVmomi.vim.HostSystem, skipComponentsCount: _typing.Optional[bool]) -> list[pyVmomi.vim.vsan.ClusterRuntimeInfo]:
      """
      Query cluster runtime information for each cluster associated to given
      witness host.
      
      Args:
          witnessHost: Witness host managed entity.
          skipComponentsCount: Skip setting in the result the number of
              components for each cluster on the given
              witness host. This can fail if the host is
              disconnected, set to true to avoid failure
              and retrieve other information in the result.
      
      Returns:
          List of ClusterRuntimeInfo to present each cluster's information.
      
      Raises:
          pyVmomi.vmodl.fault.NotSupported: If this API is not supported on current platform.
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
      """
      ...
   def ReplaceWitnessHostForClusters(self, configSpec: pyVmomi.vim.vsan.VsanVcStretchedClusterConfigSpec) -> pyVmomi.vim.Task:
      """
      Replace witness host for all specified vSAN stretched clusters.
      
      In other word, It is used to configure multiple robo clusters for
      a given witness host.
      
      Each cluster in config is expected to be used in following scenario:
      Replace original witness host with a new one, and then the old witness host
      will no longer serve the target cluster. In this scenario, the
      preferredFdName and faultDomainConfig are optional parameters. If there is
      no specified preferredFdName/faultDomainConfig, target cluster will use the
      previous configuration to configure itself.
      Relative to API
      `pyVmomi.vim.cluster.VsanVcStretchedClusterSystem.addWitnessHost`,
      it takes care of witness host reconfiguration, and the stretched cluster
      system in each cluster may be reconfigured. Clusters that are working
      in normal mode(no-stretched) are not supported.
      
      If the configuration of one or more clusters fails, the remaining
      successful operations will not be rolled back because this is a batch
      operation for multiple clusters.
      
      Args:
          configSpec: The mapping between target witness host config and
              target clusters's config(configSpec.clusters), to decide
              how to reconfigure target stretched clusters with new
              witness host.
      
      Returns:
          vim.Task
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
          pyVmomi.vmodl.fault.InvalidArgument: If below issues exist:
              1. Target witness doesn't support
                 sharing to multiple clusters, but
                 does provide more than one cluster;
              2. Target witness and clusters do not
                 meet the number limit requirements
                 for components;
              3. One or more of target clusters
                 doesn't enable vSAN;
              4. witness host resides in one or more
                 target clusters;
              5. neither IPv4 nor IPv6 is properly
                 configured for vSAN traffic
                 on all hosts in target clusters;
          pyVmomi.vmodl.fault.NotSupported: If this API is not supported on current platform.
          pyVmomi.vmodl.fault.NotEnoughLicenses: If any host in target clusters doesn't
              have vSAN stretched cluster license;
      """
      ...
   def AddWitnessHostForClusters(self, configSpec: pyVmomi.vim.vsan.VsanVcStretchedClusterConfigSpec) -> pyVmomi.vim.Task:
      """
      This API is used to convert a batch of traditional vSAN clusters into
      vSAN stretched clusters sharing the same witness host.
      
      Relative to API
      `pyVmomi.vim.cluster.VsanVcStretchedClusterSystem.convertToStretchedCluster`
      , it takes care of witness host reconfiguration, and the stretched cluster
      system in each cluster may be configured:
      1. Configure vSAN cluster into two sites through the specified
         vSAN Fault Domain setting;
      2. Setup preferred Fault Domain through the specified
         preferredFault Domain setting;
         
        
      Clusters that are already working in stretched mode are not
      supported. If the configuration of one or more clusters fails, the
      remaining successful operations will not be rolled back because this is
      a batch operation for multiple clusters.
      
      Args:
          configSpec: The mapping between target witness host config and target
              clusters's config(configSpec.clusters), to decide how to
              configure target clusters to work in stretched mode.
      
      Returns:
          vim.Task
      
      Raises:
          pyVmomi.vim.fault.VsanFault: If any unexpected runtime fault is met.
          pyVmomi.vmodl.fault.InvalidArgument: If below issues exist:
              1. Target witness doesn't support
                 sharing to multiple clusters, but
                 does provide more than one cluster;
              2. Target witness and clusters do not
                 meet the number limit requirements
                 for components;
              3. One or more of target clusters
                 doesn't enable vSAN;
              4. witness host resides in one or more
                 target clusters;
              5. neither IPv4 nor IPv6 is properly
                 configured for vSAN traffic
                 on all hosts in target clusters;
          pyVmomi.vmodl.fault.NotSupported: If this API is not supported on current platform.
          pyVmomi.vmodl.fault.NotEnoughLicenses: If any host in target clusters doesn't
              have vSAN stretched cluster license;
      """
      ...


class VsanVsanClusterPcapGroup(pyVmomi.vmodl.DynamicData):
   """
   The vSAN Cluster Pcap Group maintains the map between the CMMDS master host
   and all of communication peers in the vSAN multicast connectivity test
   
   Attributes:
       master: The CMMDS master host
       members: The host name list as communication peer for the CMMDS master host
   """
   master: str
   members: list[str] = []


class VsanVsanClusterPcapResult(pyVmomi.vmodl.DynamicData):
   """
   The Pcap result for the vSAN cluster multicast connectivity test
   
   Attributes:
       pkts: The multicast network trace packets in the json format with the keys including
           \"seenBy\" (the host list which can communicate with this host), \"cmmdsMcastSeq\"
           (the CMMDS multicast packet sequence number), \"dstIp\" (the multicast destination IP),
           \"srcUuid\" (the source host UUID), \"sentBy\" (the host IP sending the multicast packet),
           \"timestamp\", \"srcPort\" , \"msgType\"(the multicast packet message type), \"srcIp\",
           \"clusterUuid\" (the vSAN cluster UUID), \"pktType\" (the packet type) and \"dstPort\"
       groups: The Pcap group result
       issues: The issue list contains the potential mutlicast communication issue between two
           communication entities with plain string format\"
       hostResults: Per host result for the vSAN multicast connectivity test
   """
   pkts: list[str] = []
   groups: list[VsanVsanClusterPcapGroup] = []
   issues: list[str] = []
   hostResults: list[pyVmomi.vim.host.VsanVsanPcapResult] = []


class VsanVumSystem(pyVmomi.VmomiSupport.ManagedObject):
   """
   As vSAN VUM integration feature is mostly an automatic backend
   feature, so currently only get and set config methods are available in its
   control path.
   
   The Managed Entity can be accessed through MOID of vsan-vum-system at
   vCenter server side.
   """
   def GetVsanVumConfig(self) -> VsanVumSystemConfig:
      """
      Fetch vSAN VUM integration configurable settings
      See `pyVmomi.vim.cluster.VsanVumSystemConfig` for more detail information
      about all configurable settings for vSAN VUM integration.
      """
      ...
   def FetchIsoDepotCookie(self, username: str, password: str) -> None:
      """
      Fetch and save support.broadcom.com cookie string for VMware ISO download
      authentication
      
      Args:
          username: Username for support.broadcom.com
          password: Password for support.broadcom.com
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
      """
      ...
   def UpdateHostFirmware(self, host: pyVmomi.vim.HostSystem) -> pyVmomi.vim.Task:
      """
      Deprecated: As of vSphere API 8.0.Perform full stack firmware update for the given vSAN host.
      
      API look for the current firmware version on the host and
      perform a firmware update if a new firmware version is
      available.
      This API returns a task and caller should monitor the task
      to track firmware upgrade status. Upon successful completion
      of the returned `pyVmomi.vim.Task`, its `pyVmomi.vim.TaskInfo.result`
      field will be populated with a flag to notify whether host reboot
      is required.
      
      Args:
          host: Target host
      
      Raises:
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.NotSupported: Thrown if the method is not supported on the
              server.
              
              Not all methods are supported on all servers
              (for example, an ESX Server host supports less functionality than
              a VirtualCenter server). A feature might also be disabled
              due to missing liceneses.
      """
      ...
   def UploadReleaseDb(self, db: str) -> None:
      """
      Upload a release DB in JSON format.
      
      The DB will replace any existing release DB, even
      if the existing DB may appear newer.
      
      Args:
          db: The new DB in JSON format
      
      Raises:
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vim.fault.VsanFault: Base exception class for VSAN-specific faults raised for host
              or cluster operations.
          pyVmomi.vmodl.fault.NotSupported: if run directly on an ESX Server host.
      """
      ...


class VsanVumSystemConfig(pyVmomi.vmodl.DynamicData):
   """
   Describes currently configurable settings of vSAN VUM integration
   This data type could be used to get and set VUM integration settings.
   
   See `pyVmomi.vim.cluster.VsanVumSystem.getVsanVumConfig` for get settings
   operation.
   
   Attributes:
       enabled: Indicate whether vSAN VUM integration is enabled.
       autoCheckInterval: Indicate how often would vSAN VUM integration trigger upgrade check
           automatically.
           
           Unit of this value is minute.
       metadataUpdateInterval: Indicate how often would vSAN VUM integration update vSAN
           release metadata information from Internet.
           
           Unit of this value is minute.
       releaseDbLastUpdate: The time (UTC time) from when the currently used release DB was known to be
           the latest up-to-date version.
   """
   enabled: _typing.Optional[bool] = None
   autoCheckInterval: _typing.Optional[int] = None
   metadataUpdateInterval: _typing.Optional[int] = None
   releaseDbLastUpdate: _typing.Optional[_datetime.datetime] = None


class VsanWhatifCapacity(pyVmomi.vmodl.DynamicData):
   """
   Describes how much data that vSAN can accommodate if all objects are
   stored with the specified storage policy
   
   Attributes:
       totalWhatifCapacityB: The total size of data in byte that a vSAN cluster can accommodate if all objects
           are stored with the specified storage policy.
       freeWhatifCapacityB: The total size of data in byte that the remaining free space of a vSAN cluster
           can accommodate if all objects are stored with the specified storage policy.
       storagePolicy: The string of the specified storage policy
       isSatisfiable: Describe if the vSAN datastore can satisfy the required FTT
           in the specified storage policy.
   """
   totalWhatifCapacityB: pyVmomi.VmomiSupport.long
   freeWhatifCapacityB: pyVmomi.VmomiSupport.long
   storagePolicy: pyVmomi.vim.vm.ProfileSpec
   isSatisfiable: bool


class VsanWitnessSpec(pyVmomi.vmodl.DynamicData):
   """
   Describes host witness host configuration.
   
   Attributes:
       host: The host that will act as a witness.
       preferredFaultDomainName: The preferred fault domain in the vSAN Stretched Cluster.
       diskMapping: The disk mappings of the witness host.
           
           This is needed if the vSAN cluster is
           in MANUAL claiming mode.
       storagePoolSpec: The specification to add disks to vSAN storage pool.
           
           This parameter cannot be set together with diskMapping param.
   """
   host: pyVmomi.vim.HostSystem
   preferredFaultDomainName: str
   diskMapping: _typing.Optional[pyVmomi.vim.vsan.host.DiskMapping] = None
   storagePoolSpec: _typing.Optional[pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec] = None
