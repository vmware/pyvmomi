.. _vim.cluster.DrsConfigInfo: ../../../vim/cluster/DrsConfigInfo.rst

.. _vim.cluster.DrsConfigInfo.DrsBehavior: ../../../vim/cluster/DrsConfigInfo/DrsBehavior.rst

vim.cluster.DrsConfigInfo.DrsBehavior
=====================================
  :contained by: `vim.cluster.DrsConfigInfo`_

  :type: `vim.cluster.DrsConfigInfo.DrsBehavior`_

  :name: fullyAutomated

values:
--------

fullyAutomated
   Specifies that VirtualCenter should automate both the migration of virtual machines and their placement with a host at power on.

manual
   Specifies that VirtualCenter should generate recommendations for virtual machine migration and for placement with a host, but should not implement the recommendations automatically.

partiallyAutomated
   Specifies that VirtualCenter should generate recommendations for virtual machine migration and for placement with a host, but should automatically implement only the placement at power on.
