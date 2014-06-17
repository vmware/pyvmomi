.. _str: https://docs.python.org/2/library/stdtypes.html

.. _int: https://docs.python.org/2/library/stdtypes.html

.. _endTime: ../../vim/PerformanceManager/QuerySpec.rst#endTime

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _startTime: ../../vim/PerformanceManager/QuerySpec.rst#startTime

.. _intervalId: ../../vim/PerformanceManager/QuerySpec.rst#intervalId

.. _PerfFormat: ../../vim/PerformanceManager/Format.rst

.. _refreshRate: ../../vim/PerformanceManager/ProviderSummary.rst#refreshRate

.. _PerfInterval: ../../vim/HistoricalInterval.rst

.. _samplingPeriod: ../../vim/HistoricalInterval.rst#samplingPeriod

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _QueryPerfComposite: ../../vim/PerformanceManager.rst#queryCompositeStats

.. _vmodl.ManagedObject: ../../vim.ExtensibleManagedObject.rst

.. _vim.PerformanceManager.MetricId: ../../vim/PerformanceManager/MetricId.rst


vim.PerformanceManager.QuerySpec
================================
  This data object specifies the query parameters, including the managed object reference to the target entity for statistics retrieval.
   * If the optional
   * `intervalId`_
   * is omitted, the metrics are returned in their originally sampled interval.
   * 
   * When an
   * `intervalId`_
   * is specified, the server tries to summarize the information for the specified
   * `intervalId`_
   * . However, if that interval does not exist or has no data, the server summarizes the information using the best interval available.
   * If the range between
   * `startTime`_
   * and
   * `endTime`_
   * crosses multiple sample interval periods, the result contains data from the longest interval in the period.
:extends: vmodl.DynamicData_

Attributes:
    entity (`vmodl.ManagedObject`_):

       The managed object whose performance statistics are being queried.
    startTime (`datetime`_, optional):

       The server time from which to obtain counters. If not specified, defaults to the first available counter. When a startTime is specified, the returned samples do not include the sample at startTime.
    endTime (`datetime`_, optional):

       The time up to which statistics are retrieved. Corresponds to server time. When endTime is omitted, the returned result includes up to the most recent metric value. When an endTime is specified, the returned samples include the sample at endTime.
    maxSample (`int`_, optional):

       Limits the number of samples returned. Defaults to the most recent sample (or samples), unless a time range is specified. Use this property only in conjunction with the `intervalId`_ to obtain real-time statistics (set the `intervalId`_ to the `refreshRate`_ . This property is ignored for historical statistics, and is not valid for the `QueryPerfComposite`_ operation.
    metricId (`vim.PerformanceManager.MetricId`_, optional):

       The performance metrics to be retrieved. This property is required for the `QueryPerfComposite`_ operation.
    intervalId (`int`_, optional):

       The interval ( `samplingPeriod`_ ), in seconds, for the performance statisticsFor aggregated information, use one of the historical intervals for this property. See `PerfInterval`_ for more information.
        * To obtain the greatest detail, use the provider
        * s
        * `refreshRate`_
        * for this property.
        * 
    format (`str`_, optional):

       The format to be used while returning the statisticsSee `PerfFormat`_ 
