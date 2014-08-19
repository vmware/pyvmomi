
vim.cluster.VmHostRuleInfo
==========================
  A `ClusterVmHostRuleInfo <vim/cluster/VmHostRuleInfo.rst>`_ object identifies virtual machines and host groups that determine virtual machine placement. The virtual machines and hosts referenced by a VM-Host rule must be in the same cluster.A VM-Host rule identifies the following groups.
   * A virtual machine group (
   * `ClusterVmGroup <vim/cluster/VmGroup.rst>`_
   * ).
   * Two host groups - an affine host group and an anti-affine host group (
   * `ClusterHostGroup <vim/cluster/HostGroup.rst>`_
   * ). At least one of the groups must contain one or more hosts.
   * 
   * 
   * `ClusterVmHostRuleInfo <vim/cluster/VmHostRuleInfo.rst>`_
   * stores only the names of the relevant virtual machine and host groups. The group contents are stored in the virtual machine and host group objects.
   * When you modify a VM-Host rule, only the fields that are specified are set.
:extends: vim.cluster.RuleInfo_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    vmGroupName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Virtual group name ( `ClusterVmGroup <vim/cluster/VmGroup.rst>`_ . `name <vim/cluster/GroupInfo.rst#name>`_ ). The virtual group may contain one or more virtual machines.
    affineHostGroupName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the affine host group ( `ClusterHostGroup <vim/cluster/HostGroup.rst>`_ . `name <vim/cluster/GroupInfo.rst#name>`_ ). The affine host group identifies hosts on which `vmGroupName <vim/cluster/VmHostRuleInfo.rst#vmGroupName>`_ virtual machines can be powered-on. The value of the `mandatory <vim/cluster/RuleInfo.rst#mandatory>`_ property determines how the Server interprets the rule.
    antiAffineHostGroupName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the anti-affine host group ( `ClusterHostGroup <vim/cluster/HostGroup.rst>`_ . `name <vim/cluster/GroupInfo.rst#name>`_ ). The anti-affine host group identifies hosts on which `vmGroupName <vim/cluster/VmHostRuleInfo.rst#vmGroupName>`_ virtual machines should not be powered-on. The value of the `mandatory <vim/cluster/RuleInfo.rst#mandatory>`_ property determines how the Server interprets the rule.
