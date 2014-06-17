.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.ManagedEntity.Status: ../../vim/ManagedEntity/Status.rst

.. _vim.ResourcePool.ResourceUsage: ../../vim/ResourcePool/ResourceUsage.rst


vim.ResourcePool.RuntimeInfo
============================
  Current runtime resource usage and state of the resource pool
:extends: vmodl.DynamicData_

Attributes:
    memory (`vim.ResourcePool.ResourceUsage`_):

       Runtime resource usage for memory. Values are in bytes.
    cpu (`vim.ResourcePool.ResourceUsage`_):

       Runtime resource usage for CPU. Values are in Mhz.
    overallStatus (`vim.ManagedEntity.Status`_):

       Overall health of the tree. See header for description of various statuses and when they are set
