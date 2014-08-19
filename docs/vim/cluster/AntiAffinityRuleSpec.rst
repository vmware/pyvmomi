
vim.cluster.AntiAffinityRuleSpec
================================
  The `ClusterAntiAffinityRuleSpec <vim/cluster/AntiAffinityRuleSpec.rst>`_ data object defines a set of virtual machines. DRS will attempt to schedule the virtual machines to run on different hosts.
:extends: vim.cluster.RuleInfo_

Attributes:
    vm ([`vim.VirtualMachine <vim/VirtualMachine.rst>`_]):

       List of virtual machine references.
