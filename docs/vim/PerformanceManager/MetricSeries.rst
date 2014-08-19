
vim.PerformanceManager.MetricSeries
===================================
  This is a generic data object type that stores values for a specific performance metric. Useful data objects that store actual metric values extend this data object (see `PerfMetricIntSeries <vim/PerformanceManager/IntSeries.rst>`_ ).
:extends: vmodl.DynamicData_

Attributes:
    id (`vim.PerformanceManager.MetricId <vim/PerformanceManager/MetricId.rst>`_):

       An identifier for the performance metric.
