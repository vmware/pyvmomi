.. _metrics: ../../vim/PerformanceManager/EntityMetric.rst

.. _PerfSampleInfo: ../../vim/PerformanceManager/SampleInfo.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _PerfCompositeMetric: ../../vim/PerformanceManager/CompositeEntityMetric.rst

.. _vim.PerformanceManager.EntityMetricBase: ../../vim/PerformanceManager/EntityMetricBase.rst


vim.PerformanceManager.CompositeEntityMetric
============================================
   `PerfCompositeMetric`_ includes an optional aggregated entity performance statistics and a list of composite entities performance statisticsThe aggregated entity statistics are optional because some entities, such as folders, do not have their own statistics
:extends: vmodl.DynamicData_

Attributes:
    entity (`vim.PerformanceManager.EntityMetricBase`_, optional):

       The aggregated entity performance metrics. If it exists, the `PerfSampleInfo`_ list of the aggregate entity is a complete list of `PerfSampleInfo`_ that could be contained in `PerfSampleInfo`_ lists of child entities.
    childEntity ([`vim.PerformanceManager.EntityMetricBase`_], optional):

       A list of `metrics`_ of performance providers that comprise the aggregated entity. For example, Host is an aggregated entity for virtual machines and virtual machine Folders. ResourcePools are aggregate entities for virtual machines. Host, Folder, and Cluster are aggregate entities for hosts in the cluster or folder.
