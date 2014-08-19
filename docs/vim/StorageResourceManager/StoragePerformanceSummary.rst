
vim.StorageResourceManager.StoragePerformanceSummary
====================================================
  Summary statistics for datastore performance The statistics are reported in aggregated quantiles over a time period
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    interval (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Time period over which statistics are aggregated The reported time unit is in seconds
    percentile ([`int <https://docs.python.org/2/library/stdtypes.html>`_]):

       Metric percentile specification. A percentile is a value between 1 and 100. The metric value reported in the aggregated statistics corresponds with the percentile values in this field. For example, if the value of percentile[0] is P, and the value of the datastoreReadLatency[0] is L, then P% of all the read IOs performed during observation interval is less than L milliseconds.
    datastoreReadLatency ([`double <https://docs.python.org/2/library/stdtypes.html>`_]):

       Aggregated datastore latency in milliseconds for read operations
    datastoreWriteLatency ([`double <https://docs.python.org/2/library/stdtypes.html>`_]):

       Aggregated datastore latency in milliseconds for write operations
    datastoreVmLatency ([`double <https://docs.python.org/2/library/stdtypes.html>`_]):

       Aggregated datastore latency as observed by Vms using the datastore The reported latency is in milliseconds.
    datastoreReadIops ([`double <https://docs.python.org/2/library/stdtypes.html>`_]):

       Aggregated datastore Read IO rate (Reads/second)
    datastoreWriteIops ([`double <https://docs.python.org/2/library/stdtypes.html>`_]):

       Aggregated datastore Write IO rate (Writes/second)
    siocActivityDuration (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Cumulative SIOC activity to satisfy SIOC latency threshold setting. This metric indicates the total time that SIOC is actively throttling IO requests. The SIOC throttling activity occurs whenever the datastore latency exceeds the SIOC latency threshold. If SIOC is not enabled on the datastore, the metric indicates the total time that SIOC would have been active. The unit of reporting is in milliseconds.
