
vim.PerformanceManager.IntSeries
================================
  This data object type describes integer metric values. The size of the array must match the size of `sampleInfo <vim/PerformanceManager/EntityMetric.rst#sampleInfo>`_ property in the `PerfEntityMetric <vim/PerformanceManager/EntityMetric.rst>`_ that contains this series.
:extends: vim.PerformanceManager.MetricSeries_

Attributes:
    value ([`long <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       An array of 64-bit integer values. The size of the array matches the size as the `PerfSampleInfo <vim/PerformanceManager/SampleInfo.rst>`_ , because the values can only be interpreted in the context of the sample that generated the value.
