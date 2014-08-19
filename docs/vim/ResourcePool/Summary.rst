
vim.ResourcePool.Summary
========================
  This data object type encapsulates a typical set of resource pool information that is useful for list views and summary pages.
:extends: vmodl.DynamicData_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of resource pool.
    config (`vim.ResourceConfigSpec <vim/ResourceConfigSpec.rst>`_):

       Current configuration of the resource pool.
    runtime (`vim.ResourcePool.RuntimeInfo <vim/ResourcePool/RuntimeInfo.rst>`_):

       Current runtime state of the resource pool.
    quickStats (`vim.ResourcePool.Summary.QuickStats <vim/ResourcePool/Summary/QuickStats.rst>`_, optional):

       A set of statistics that are typically updated with near real-time regularity. This data object type does not support notification, for scalability reasons. Therefore, changes in QuickStats do not generate property collector updates. To monitor statistics values, use the statistics and alarms modules instead.
    configuredMemoryMB (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Total configured memory of all virtual machines in the resource pool, in MB.
