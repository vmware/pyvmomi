.. _str: https://docs.python.org/2/library/stdtypes.html

.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.ResourceConfigSpec: ../../vim/ResourceConfigSpec.rst

.. _vim.ResourcePool.RuntimeInfo: ../../vim/ResourcePool/RuntimeInfo.rst

.. _vim.ResourcePool.Summary.QuickStats: ../../vim/ResourcePool/Summary/QuickStats.rst


vim.ResourcePool.Summary
========================
  This data object type encapsulates a typical set of resource pool information that is useful for list views and summary pages.
:extends: vmodl.DynamicData_

Attributes:
    name (`str`_):

       Name of resource pool.
    config (`vim.ResourceConfigSpec`_):

       Current configuration of the resource pool.
    runtime (`vim.ResourcePool.RuntimeInfo`_):

       Current runtime state of the resource pool.
    quickStats (`vim.ResourcePool.Summary.QuickStats`_, optional):

       A set of statistics that are typically updated with near real-time regularity. This data object type does not support notification, for scalability reasons. Therefore, changes in QuickStats do not generate property collector updates. To monitor statistics values, use the statistics and alarms modules instead.
    configuredMemoryMB (`int`_, optional):

       Total configured memory of all virtual machines in the resource pool, in MB.
