
vim.ResourcePlanningManager.DatabaseSizeParam
=============================================
  DatabaseSizeParam contains information about a sample inventory. Using this information, database size requirements for that sample inventory can be computed. Depending on the accuracy of estimate desired, users can choose to specify the number of different types of managed entities. The numHosts and numVirtualMachines are the only two required fields. Rest are all optional fields filled up by Virtual Center based on some heuristics. These parameters need not represent a real inventory. The user can use these parameters to estimate the database size required by a hypothetical VirtualCenter setup.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    inventoryDesc (`vim.ResourcePlanningManager.InventoryDescription <vim/ResourcePlanningManager/InventoryDescription.rst>`_):

       Object to capture inventory description
    perfStatsDesc (`vim.ResourcePlanningManager.PerfStatsDescription <vim/ResourcePlanningManager/PerfStatsDescription.rst>`_, optional):

       Object to capture performance statistics related parameters
