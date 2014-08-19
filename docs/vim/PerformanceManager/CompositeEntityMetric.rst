
vim.PerformanceManager.CompositeEntityMetric
============================================
   `PerfCompositeMetric <vim/PerformanceManager/CompositeEntityMetric.rst>`_ includes an optional aggregated entity performance statistics and a list of composite entities performance statisticsThe aggregated entity statistics are optional because some entities, such as folders, do not have their own statistics
:extends: vmodl.DynamicData_

Attributes:
    entity (`vim.PerformanceManager.EntityMetricBase <vim/PerformanceManager/EntityMetricBase.rst>`_, optional):

       The aggregated entity performance metrics. If it exists, the `PerfSampleInfo <vim/PerformanceManager/SampleInfo.rst>`_ list of the aggregate entity is a complete list of `PerfSampleInfo <vim/PerformanceManager/SampleInfo.rst>`_ that could be contained in `PerfSampleInfo <vim/PerformanceManager/SampleInfo.rst>`_ lists of child entities.
    childEntity ([`vim.PerformanceManager.EntityMetricBase <vim/PerformanceManager/EntityMetricBase.rst>`_], optional):

       A list of `metrics <vim/PerformanceManager/EntityMetric.rst>`_ of performance providers that comprise the aggregated entity. For example, Host is an aggregated entity for virtual machines and virtual machine Folders. ResourcePools are aggregate entities for virtual machines. Host, Folder, and Cluster are aggregate entities for hosts in the cluster or folder.
