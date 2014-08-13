.. _EVCMode: ../../vim/EVCMode.rst

.. _enabled: ../../vim/vsan/cluster/ConfigInfo.rst#enabled

.. _Datastore: ../../vim/Datastore.rst

.. _vsanConfig: ../../vim/cluster/ConfigSpecEx.rst#vsanConfig

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmMonitoring: ../../vim/cluster/DasConfigInfo.rst#vmMonitoring

.. _ClusterVmGroup: ../../vim/cluster/VmGroup.rst

.. _hostMonitoring: ../../vim/cluster/DasConfigInfo.rst#hostMonitoring

.. _PowerOnVM_Task: ../../vim/VirtualMachine.rst#powerOn

.. _CreateClusterEx: ../../vim/Folder.rst#createClusterEx

.. _ClusterHostGroup: ../../vim/cluster/HostGroup.rst

.. _defaultVmBehavior: ../../vim/cluster/DrsConfigInfo.rst#defaultVmBehavior

.. _defaultVmSettings: ../../vim/cluster/DasConfigInfo.rst#defaultVmSettings

.. _defaultDpmBehavior: ../../vim/cluster/DpmConfigInfo.rst#defaultDpmBehavior

.. _ClusterConfigSpecEx: ../../vim/cluster/ConfigSpecEx.rst

.. _ClusterDrsConfigInfo: ../../vim/cluster/DrsConfigInfo.rst

.. _vim.cluster.RuleSpec: ../../vim/cluster/RuleSpec.rst

.. _ClusterDpmConfigInfo: ../../vim/cluster/DpmConfigInfo.rst

.. _ClusterDasConfigInfo: ../../vim/cluster/DasConfigInfo.rst

.. _VsanClusterConfigInfo: ../../vim/vsan/cluster/ConfigInfo.rst

.. _vim.cluster.GroupSpec: ../../vim/cluster/GroupSpec.rst

.. _ClusterVmHostRuleInfo: ../../vim/cluster/VmHostRuleInfo.rst

.. _CreateSecondaryVM_Task: ../../vim/VirtualMachine.rst#createSecondary

.. _EnableSecondaryVM_Task: ../../vim/VirtualMachine.rst#enableSecondary

.. _admissionControlEnabled: ../../vim/cluster/DasConfigInfo.rst#admissionControlEnabled

.. _vim.vsan.host.ConfigInfo: ../../vim/vsan/host/ConfigInfo.rst

.. _vim.cluster.DrsConfigInfo: ../../vim/cluster/DrsConfigInfo.rst

.. _vim.cluster.DpmConfigInfo: ../../vim/cluster/DpmConfigInfo.rst

.. _vim.cluster.DasConfigInfo: ../../vim/cluster/DasConfigInfo.rst

.. _vim.cluster.DasVmConfigSpec: ../../vim/cluster/DasVmConfigSpec.rst

.. _vim.vsan.cluster.ConfigInfo: ../../vim/vsan/cluster/ConfigInfo.rst

.. _vim.cluster.DrsVmConfigSpec: ../../vim/cluster/DrsVmConfigSpec.rst

.. _vim.cluster.DpmHostConfigSpec: ../../vim/cluster/DpmHostConfigSpec.rst

.. _TerminateFaultTolerantVM_Task: ../../vim/VirtualMachine.rst#terminateFaultTolerantVM

.. _vim.ComputeResource.ConfigSpec: ../../vim/ComputeResource/ConfigSpec.rst

.. _ReconfigureComputeResource_Task: ../../vim/ComputeResource.rst#reconfigureEx

.. _ClusterVmToolsMonitoringSettings: ../../vim/cluster/VmToolsMonitoringSettings.rst

.. _CannotChangeHaSettingsForFtSecondary: ../../vim/fault/CannotChangeHaSettingsForFtSecondary.rst

.. _ClusterDasVmSettingsIsolationResponse: ../../vim/cluster/DasVmSettings/IsolationResponse.rst

.. _CannotChangeDrsBehaviorForFtSecondary: ../../vim/fault/CannotChangeDrsBehaviorForFtSecondary.rst


vim.cluster.ConfigSpecEx
========================
  The `ClusterConfigSpecEx`_ data object provides a set of update specifications for complete cluster configuration. You can configure a cluster when you create a new cluster (the `CreateClusterEx`_ method) or when you reconfigure an existing cluster (the `ReconfigureComputeResource_Task`_ method).All fields are optional. If you set themodifyparameter totruewhen you call `ReconfigureComputeResource_Task`_ , an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set themodifyparameter tofalsewhen you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied.Use the properties defined for this object to configure the following services:
   * HA (High Availability) - provides failover protection for virtual machines running in a cluster of ESX Server hosts. The virtual machines are located in a
   * `Datastore`_
   * , which provides shared storage for the cluster. When a failure occurs that affects a protected virtual machine, HA will restart the virtual machine on another host. When HA detects a host failure, either the host has failed or it may be isolated from the network. The HA agent on an isolated host will power off or shutdown the virtual machines running on that host so that they can be restarted elsewhere. See
   * `ClusterDasVmSettingsIsolationResponse`_
   * for information about how a host handles network isolation.
   * When it chooses a failover host, HA selects a host that is compatible with the virtual machine and that can support resource allocation for that virtual machine so that service level guarantees remain intact. HA does not consider hosts that are in maintenance mode, standby mode, or which are disconnected from the vCenter Server. When a host powers on or becomes available again, HA is reenabled on that host, so it becomes available for failover again. VMware recommends that you configure hosts and virtual machines so that all virtual machines can run on all hosts in the cluster. This will maximize the chances of restarting a VM after a failure.
   * HA also restarts a virtual machine after a guest operating system failure. In this case, the virtual machine health monitoring service detects the guest failure, and HA restarts the virtual machine on the same host. The service monitors heartbeats from the VmTools service and optionally heartbeats that are generated by a third-party application monitor. See
   * `ClusterVmToolsMonitoringSettings`_
   * and
   * `ClusterDasConfigInfo`_
   * .
   * `vmMonitoring`_
   * .
   * To enable HA for a cluster, set the
   * `ClusterDasConfigInfo`_
   * .
   * `enabled`_
   * property to
   * true
   * and the
   * `ClusterDasConfigInfo`_
   * .
   * `hostMonitoring`_
   * property to
   * `enabled`_
   * . (The vSphere API uses the substring "das" in object, property, and method names for HA.
   * 1
   * )
   * DRS (Distributed Resource Scheduling) - provides automatic initial virtual machine placement on any of the hosts in the cluster. DRS also makes automatic resource relocation and optimization decisions as hosts or virtual machines are added or removed from the cluster. You can also configure DRS for manual control, so that it only makes recommendations that you can review and carry out.
   * To enable DRS for a cluster, set the
   * `ClusterDrsConfigInfo`_
   * .
   * `enabled`_
   * property to
   * true
   * .
   * DPM (Distributed Power Management) - supports optimized power consumption on the cluster. When virtual machines in a DRS cluster require fewer resources, DPM consolidates workloads onto fewer servers while maintaining quality of service guarantees and powers off the rest to reduce power consumption. When more resources are required, DPM brings the powered-down hosts online.
   * To enable DPM for a cluster, set the
   * `ClusterDpmConfigInfo`_
   * .
   * `enabled`_
   * property to
   * true
   * .
   * VSAN - aggregrates hosts' local disks to present a single shared datastore to the cluster.
   * To enable VSAN for a cluster, set the
   * `enabled`_
   * property to
   * true
   * for
   * `vsanConfig`_
   * .The HA, DRS, and DPM services are integrated with the FT (Fault Tolerance) and EVC (Enhanced vMotion Compatibility) services. Use the `CreateSecondaryVM_Task`_ method to establish fault tolerance for a virtual machine. Use the vSphere Client to configure EVC. The HA, DRS, DPM, FT, and EVC services interact under the following circumstances.
   * To determine initial placement of a virtual machine, DRS checks to see if the HA admission control policy on a potential host supports the addition of the powered on virtual machine. With the default setting, DRS will not power on more than four FT virtual machines per host. You can use the configuration editor in the vSphere Client to set the HA advanced option
   * das.maxFtVmsPerHost
   * to the desired number or to zero to disable.
   * When a host fails, HA determines placement within the cluster when it restarts the virtual machines. If there is insufficient capacity, and DPM has put one or more compatible hosts into standby, HA relies on DPM to bring more capacity online.
   * To use FT in a cluster, the cluster must be HA-enabled.
   * You can disable HA in a cluster while there are FT virtual machines registered on hosts in the cluster. While HA is disabled, powered on FT virtual machines will continue to run, but HA will not restart any virtual machines after a failure. When HA is disabled, you cannot use the following FT operations:
   * 
   * Turn on FT (
   * `CreateSecondaryVM_Task`_
   * )
   * Enable FT (
   * `EnableSecondaryVM_Task`_
   * )
   * Power on an FT virtual machine (
   * `PowerOnVM_Task`_
   * )
   * Test failover and test secondary restart (
   * `TerminateFaultTolerantVM_Task`_
   * )
   * In a cluster using DRS and HA with admission control turned on (
   * `ClusterDasConfigInfo`_
   * .
   * `admissionControlEnabled`_
   * ), the vCenter Server might not migrate virtual machines from hosts entering maintenance mode. This is because resources are reserved to maintain the failover level. You must use vMotion to manually migrate the virtual machines off the hosts.
   * When admission control is disabled, failover resource constraints are not passed on to DRS and DPM. The constraints are not enforced.
   * 
   * DRS determines virtual machine placement and status (maintenance mode, standby mode) regardless of the impact this might have on failover requirements.
   * DPM powers off hosts (places them in standby mode) even if doing so violates failover requirements. If there is insufficient capacity when a failover occurs, DPM will attempt to bring more capacity online in order to correct the situation.
   * You must enable EVC in a cluster to enable DRS to manage FT primary and secondary virtual machine pairs in the cluster. For information about EVC clusters, see
   * `EVCMode`_
   * .
   * If EVC is disabled, vCenter automatically creates overrides to disable DRS for FT primary/secondary pairs in the cluster. vCenter will still use DRS to place a secondary virtual machine when it powers on. Attempts to remove the overrides or to enable DRS operations will fail.
   * EVC clusters support load balancing of powered on FT primary and secondary virtual machines. DRS behavior is governed by the overrides defined for the primary virtual machine. The secondary inherits DRS behavior from its primary. If you do not configure a DRS override for an FT virtual machine, DRS uses the cluster default (
   * `defaultVmBehavior`_
   * ).1High Availability was previously called Distributed Availability Services.
:extends: vim.ComputeResource.ConfigSpec_
:since: `VI API 2.5`_

Attributes:
    dasConfig (`vim.cluster.DasConfigInfo`_, optional):

       HA configuration; includes default settings for virtual machines.
    dasVmConfigSpec ([`vim.cluster.DasVmConfigSpec`_], optional):

       HA configuration for individual virtual machines. The entries in this array override the cluster default settings ( `ClusterDasConfigInfo`_ . `defaultVmSettings`_ ). You cannot specify an HA override for a secondary FT virtual machine. The secondary virtual machine will inherit whatever settings apply to its primary virtual machine. If you include an entry for a secondary, the reconfigure method will throw the fault `CannotChangeHaSettingsForFtSecondary`_ .
    drsConfig (`vim.cluster.DrsConfigInfo`_, optional):

       DRS configuration; includes default settings for virtual machines.
    drsVmConfigSpec ([`vim.cluster.DrsVmConfigSpec`_], optional):

       DRS configuration for individual virtual machines. The entries in this array override the cluster default settings ( `ClusterDrsConfigInfo`_ . `defaultVmBehavior`_ ). You cannot specify a DRS override for a secondary FT virtual machine. The secondary virtual machine will inherit whatever setting applies to its primary virtual machine. If you include an entry for a secondary, the reconfigure method will throw the fault `CannotChangeDrsBehaviorForFtSecondary`_ .
    rulesSpec ([`vim.cluster.RuleSpec`_], optional):

       Cluster affinity and anti-affinity rule configuration.
    dpmConfig (`vim.cluster.DpmConfigInfo`_, optional):

       DPM configuration; includes default settings for hosts.
    dpmHostConfigSpec ([`vim.cluster.DpmHostConfigSpec`_], optional):

       DPM configuration for individual hosts. The entries in this array override the cluster default settings ( `ClusterDpmConfigInfo`_ . `defaultDpmBehavior`_ ).
    vsanConfig (`vim.vsan.cluster.ConfigInfo`_, optional):

       VSAN configuration; includes default settings for hosts.
    vsanHostConfigSpec ([`vim.vsan.host.ConfigInfo`_], optional):

       VSAN configuration for individual hosts. The entries in this array override the cluster default settings as specified in `VsanClusterConfigInfo`_ .
    groupSpec ([`vim.cluster.GroupSpec`_], optional):

       Cluster-wide group configuration. The array contains one or more group specification objects. A group specification object contains a virtual machine group ( `ClusterVmGroup`_ ) or a host group ( `ClusterHostGroup`_ ). Groups can be related; see `ClusterVmHostRuleInfo`_ .
