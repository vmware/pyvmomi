.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _rule: ../../vim/cluster/ConfigInfoEx.rst#rule

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _rulesSpec: ../../vim/cluster/ConfigSpecEx.rst#rulesSpec

.. _ClusterVmGroup: ../../vim/cluster/VmGroup.rst

.. _ClusterRuleInfo: ../../vim/cluster/RuleInfo.rst

.. _ClusterHostGroup: ../../vim/cluster/HostGroup.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _ClusterConfigInfoEx: ../../vim/cluster/ConfigInfoEx.rst

.. _ClusterConfigSpecEx: ../../vim/cluster/ConfigSpecEx.rst

.. _ClusterVmHostRuleInfo: ../../vim/cluster/VmHostRuleInfo.rst

.. _ClusterAffinityRuleSpec: ../../vim/cluster/AffinityRuleSpec.rst

.. _vim.ManagedEntity.Status: ../../vim/ManagedEntity/Status.rst

.. _VirtualMachineAffinityInfo: ../../vim/vm/AffinityInfo.rst

.. _ClusterAntiAffinityRuleSpec: ../../vim/cluster/AntiAffinityRuleSpec.rst


vim.cluster.RuleInfo
====================
  The `ClusterRuleInfo`_ data object is the base type for affinity and anti-affinity rules. The affinity and anti-affinity rules are DRS (Distributed Resource Scheduling) rules that affect the placement of virtual machines in a cluster. Hosts and virtual machines referenced in a DRS rule must be in the same cluster.Note: DRS rules are different than an individual host's CPU affinity rules ( `VirtualMachineAffinityInfo`_ ).The Server uses DRS rule objects to describe the current rule configuration ( `ClusterConfigInfoEx`_ . `rule`_ ). Your client application uses rule objects to configure the affinity and anti-affinity rules ( `ClusterConfigSpecEx`_ . `rulesSpec`_ ).You can create the following types of rules:
   * An affinity rule defines a set of virtual machines that should run on the same host. The
   * `ClusterAffinityRuleSpec`_
   * object describes a rule that identifies virtual machines, but does not identify any specific host.
   * An anti-affinity rule defines a set of virtual machines that should run on different hosts. The
   * `ClusterAntiAffinityRuleSpec`_
   * object describes a rule that identifies virtual machines, but does not identify any specific host.
   * A VM-Host rule defines affinity and anti-affinity relationships between virtual machines and hosts. The
   * `ClusterVmHostRuleInfo`_
   * object describes a rule that identifies a virtual machine group (
   * `ClusterVmGroup`_
   * ) and affinity and anti-affinity host groups (
   * `ClusterHostGroup`_
   * ).Rule configuration is a dynamic process. When you create or modify a DRS rule, the Server applies the rule to the cluster. If the existing cluster configuration violates the rule, the Server attempts to correct the situation. If that is not possible, the Server generates a fault and produces a log event. DRS rules do not have precedence; all rules are applied equally. DRS does not validate one rule against another. If you create conflicting rules, the older rule takes precedence and DRS disables the newer rule.Improperly used, DRS rules can fragment the cluster and inhibit the proper functioning of DRS, HA, and DPM services. vSphere services never take any actions that would result in the violation of mandatory DRS rules. An operation that violates a mandatory rule would produce the following consequences.
   * DRS does not evacuate virtual machines to place a host in maintenance mode.
   * DRS does not place virtual machines for power-on or load balance virtual machines.
   * HA does not perform failovers.
   * DPM does not optimize power management by placing hosts into standby mode.To avoid these situations, exercise caution when creating more than one mandatory rule, or consider using only optional rules. Make sure that the number of hosts with which a virtual machine is related by affinity rule is large enough that losing a host does not prevent the virtual machine from running.For manual and partially automated DRS clusters, the Server produces migration recommendations to satisfy the DRS rules. You are not required to act on the recommendations, but the Server maintains the recommendations until the rules are satisfied.
:extends: vmodl.DynamicData_

Attributes:
    key (`int`_, optional):

       Unique ID for rules. When adding a new rule, do not specify this property. The Server will assign the key.
    status (`vim.ManagedEntity.Status`_, optional):

       Flag to indicate whether or not the rule is currently satisfied.
    enabled (`bool`_, optional):

       Flag to indicate whether or not the rule is enabled. Set this property when you configure the rule. The default value is false (disabled). If there is a rule conflict, the Server can override the setting to disable a rule.
    name (`str`_, optional):

       Name of the rule.
    mandatory (`bool`_, optional):

       Flag to indicate whether compliance with this rule is mandatory or optional. The default value is false (optional).
        * A mandatory rule will prevent a virtual machine from being powered on or migrated to a host that does not satisfy the rule.
        * An optional rule specifies a preference. DRS takes an optional rule into consideration when it places a virtual machine in the cluster. DRS will act on an optional rule as long as it does not impact the ability of the host to satisfy current CPU or memory requirements for virtual machines on the system. (As long as the operation does not cause any host to be more than 100% utilized.)
        * 
    userCreated (`bool`_, optional):

       Flag to indicate whether the rule is created by the user or the system.
    inCompliance (`bool`_, optional):

       Flag to indicate whether or not the placement of Virtual Machines is currently in compliance with this rule. The Server does not currently use this property.
