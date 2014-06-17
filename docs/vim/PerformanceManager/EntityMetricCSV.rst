.. _str: https://docs.python.org/2/library/stdtypes.html

.. _PerfSampleInfo: ../../vim/PerformanceManager/SampleInfo.rst

.. _vim.PerformanceManager.MetricSeriesCSV: ../../vim/PerformanceManager/MetricSeriesCSV.rst

.. _vim.PerformanceManager.EntityMetricBase: ../../vim/PerformanceManager/EntityMetricBase.rst


vim.PerformanceManager.EntityMetricCSV
======================================
  This data object type stores metric values for a specific entity in CSV format.
:extends: vim.PerformanceManager.EntityMetricBase_

Attributes:
    sampleInfoCSV (`str`_):

       The `PerfSampleInfo`_ encoded in the following CSV format: [interval1], [date1], [interval2], [date2], and so on.
    value (`vim.PerformanceManager.MetricSeriesCSV`_, optional):

       Metric values corresponding to the samples collected in this list.
