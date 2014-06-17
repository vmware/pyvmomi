.. _long: https://docs.python.org/2/library/stdtypes.html

.. _sampleInfo: ../../vim/PerformanceManager/EntityMetric.rst#sampleInfo

.. _PerfSampleInfo: ../../vim/PerformanceManager/SampleInfo.rst

.. _PerfEntityMetric: ../../vim/PerformanceManager/EntityMetric.rst

.. _vim.PerformanceManager.MetricSeries: ../../vim/PerformanceManager/MetricSeries.rst


vim.PerformanceManager.IntSeries
================================
  This data object type describes integer metric values. The size of the array must match the size of `sampleInfo`_ property in the `PerfEntityMetric`_ that contains this series.
:extends: vim.PerformanceManager.MetricSeries_

Attributes:
    value (`long`_, optional):

       An array of 64-bit integer values. The size of the array matches the size as the `PerfSampleInfo`_ , because the values can only be interpreted in the context of the sample that generated the value.
