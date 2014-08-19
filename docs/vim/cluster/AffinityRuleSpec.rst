
vim.cluster.AffinityRuleSpec
============================
  The `ClusterAffinityRuleSpec <vim/cluster/AffinityRuleSpec.rst>`_ data object defines a set of virtual machines. DRS will attempt to schedule the virtual machines to run on the same host.
:extends: vim.cluster.RuleInfo_

Attributes:
    vm ([`vim.VirtualMachine <vim/VirtualMachine.rst>`_]):

       List of virtual machine references.
