.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _vim.cluster.RuleInfo: ../../vim/cluster/RuleInfo.rst

.. _ClusterAntiAffinityRuleSpec: ../../vim/cluster/AntiAffinityRuleSpec.rst


vim.cluster.AntiAffinityRuleSpec
================================
  The `ClusterAntiAffinityRuleSpec`_ data object defines a set of virtual machines. DRS will attempt to schedule the virtual machines to run on different hosts.
:extends: vim.cluster.RuleInfo_

Attributes:
    vm (`vim.VirtualMachine`_):

       List of virtual machine references.
