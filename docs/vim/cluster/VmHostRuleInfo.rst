.. _str: https://docs.python.org/2/library/stdtypes.html

.. _name: ../../vim/cluster/GroupInfo.rst#name

.. _mandatory: ../../vim/cluster/RuleInfo.rst#mandatory

.. _vmGroupName: ../../vim/cluster/VmHostRuleInfo.rst#vmGroupName

.. _ClusterVmGroup: ../../vim/cluster/VmGroup.rst

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _ClusterHostGroup: ../../vim/cluster/HostGroup.rst

.. _vim.cluster.RuleInfo: ../../vim/cluster/RuleInfo.rst

.. _ClusterVmHostRuleInfo: ../../vim/cluster/VmHostRuleInfo.rst


vim.cluster.VmHostRuleInfo
==========================
  A `ClusterVmHostRuleInfo`_ object identifies virtual machines and host groups that determine virtual machine placement. The virtual machines and hosts referenced by a VM-Host rule must be in the same cluster.A VM-Host rule identifies the following groups.
   * A virtual machine group (
   * `ClusterVmGroup`_
   * ).
   * Two host groups - an affine host group and an anti-affine host group (
   * `ClusterHostGroup`_
   * ). At least one of the groups must contain one or more hosts.
   * 
   * 
   * `ClusterVmHostRuleInfo`_
   * stores only the names of the relevant virtual machine and host groups. The group contents are stored in the virtual machine and host group objects.
   * When you modify a VM-Host rule, only the fields that are specified are set.
:extends: vim.cluster.RuleInfo_
:since: `vSphere API 4.1`_

Attributes:
    vmGroupName (`str`_, optional):

       Virtual group name ( `ClusterVmGroup`_ . `name`_ ). The virtual group may contain one or more virtual machines.
    affineHostGroupName (`str`_, optional):

       Name of the affine host group ( `ClusterHostGroup`_ . `name`_ ). The affine host group identifies hosts on which `vmGroupName`_ virtual machines can be powered-on. The value of the `mandatory`_ property determines how the Server interprets the rule.
    antiAffineHostGroupName (`str`_, optional):

       Name of the anti-affine host group ( `ClusterHostGroup`_ . `name`_ ). The anti-affine host group identifies hosts on which `vmGroupName`_ virtual machines should not be powered-on. The value of the `mandatory`_ property determines how the Server interprets the rule.
