.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _vim.cluster.RuleInfo: ../../vim/cluster/RuleInfo.rst

.. _ClusterAffinityRuleSpec: ../../vim/cluster/AffinityRuleSpec.rst


vim.cluster.AffinityRuleSpec
============================
  The `ClusterAffinityRuleSpec`_ data object defines a set of virtual machines. DRS will attempt to schedule the virtual machines to run on the same host.
:extends: vim.cluster.RuleInfo_

Attributes:
    vm ([`vim.VirtualMachine`_]):

       List of virtual machine references.
