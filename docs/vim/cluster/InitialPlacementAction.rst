.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.HostSystem: ../../vim/HostSystem.rst

.. _vim.ResourcePool: ../../vim/ResourcePool.rst

.. _vim.cluster.Action: ../../vim/cluster/Action.rst


vim.cluster.InitialPlacementAction
==================================
  Describes an initial placement of a single virtual machine
:extends: vim.cluster.Action_
:since: `VI API 2.5`_

Attributes:
    targetHost (`vim.HostSystem`_):

       The host where the virtual machine should be initially placed.
    pool (`vim.ResourcePool`_, optional):

       The resource pool to place the virtual machine into in case this action is for migrating from outside cluster.
