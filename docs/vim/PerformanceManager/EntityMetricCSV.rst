
vim.PerformanceManager.EntityMetricCSV
======================================
  This data object type stores metric values for a specific entity in CSV format.
:extends: vim.PerformanceManager.EntityMetricBase_

Attributes:
    sampleInfoCSV (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The `PerfSampleInfo <vim/PerformanceManager/SampleInfo.rst>`_ encoded in the following CSV format: [interval1], [date1], [interval2], [date2], and so on.
    value ([`vim.PerformanceManager.MetricSeriesCSV <vim/PerformanceManager/MetricSeriesCSV.rst>`_], optional):

       Metric values corresponding to the samples collected in this list.
