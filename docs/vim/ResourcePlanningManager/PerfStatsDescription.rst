
vim.ResourcePlanningManager.PerfStatsDescription
================================================
  Data object to capture all information needed to describe a sample inventory.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    intervals ([`vim.HistoricalInterval <vim/HistoricalInterval.rst>`_], optional):

       Historic interval setting. Default value is the same as the historic interval settings of the current instance of running VC.
