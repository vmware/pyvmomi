.. _vim.PerformanceManager.SampleInfo: ../../vim/PerformanceManager/SampleInfo.rst

.. _vim.PerformanceManager.MetricSeries: ../../vim/PerformanceManager/MetricSeries.rst

.. _vim.PerformanceManager.EntityMetricBase: ../../vim/PerformanceManager/EntityMetricBase.rst


vim.PerformanceManager.EntityMetric
===================================
  This data object type stores values and metadata for metrics associated with a specific entity, in 'normal' format.
:extends: vim.PerformanceManager.EntityMetricBase_

Attributes:
    sampleInfo (`vim.PerformanceManager.SampleInfo`_, optional):

       A list of objects containing information (an interval and a timestamp) about the samples collected.
    value (`vim.PerformanceManager.MetricSeries`_, optional):

       A list of values that corresponds to the samples collected.
