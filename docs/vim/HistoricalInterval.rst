
vim.HistoricalInterval
======================
  This data object type contains metadata about a performance interval.
   * For VirtualCenter Server systems, instances of this data object are referred to as
   * historical intervals
   * because they control how data collected from the ESX systems will be aggregated and stored in the database.
   * For ESX system, this data object is typically referred to simply as the
   * interval
   * or
   * performance interval
   * because ESX does not aggregate statistical data.For ESX systems, a single instance of this data object exists. It cannot be modified. It has these properties:keysamplingPeriodlengthnamelevelenabled1300129600PastDaynulltrueVirtualCenter Server system provides four instances of this data object by default, that apply globally to all system entities.Example Collection LevelsVirtualCenter Server uses the specifications configured in its historical intervals to collect metrics from the ESX systems that it manages. The quantity of data collected depends on the level settings for the server, and the level associated with a specific counter. Both factors may change from one version of the products to the next. In general, the lower the number, the smaller the amount of data collected. For VirtualCenter Server 2.5, for example, the levels 1 through 4 collected data as follows:
   * Basic counters defined with "average"
   * `rollup type <vim/PerformanceManager/CounterInfo/RollupType.rst>`_
   * for CPU, Memory, Disk, and Network; plus counters for System Uptime, System Heartbeat, and DRS (Distributed Resource Scheduler, tracked in the "clusterServices" group). Does not include counters for devices.
   * Counters defined with "average," "summation," and "latest"
   * `rollup types <vim/PerformanceManager/CounterInfo/RollupType.rst>`_
   * for CPU, Memory, Disk, and Network; plus counters for System Uptime, System Heartbeat, and DRS (clusterServices). Does not include counters for devices.
   * Counters defined with "average," "summmation," and "latest"
   * `rollup types <vim/PerformanceManager/CounterInfo/RollupType.rst>`_
   * for CPU, Memory, Disk, Network, and all devices; plus counters for System Uptime, System Heartbeat, and DRS (clusterServices).
   * All counters defined for all entities and devices, for every
   * `rollup type <vim/PerformanceManager/CounterInfo/RollupType.rst>`_
   * , including
   * minimum
   * and
   * maximum
   * Default properties for the four built-in historical intervals include:keysamplingPeriodlengthnamelevelenabled130086400Pastday1true21800604800Pastweek1true372002592000Pastmonth1true46640031536000Pastyear1trueAll values are in seconds. The default setting for vCenter Server is level 1, which retains sampled statistical data as follows:
   * 5-minute samples for the past day
   * 30-minute samples for the past week
   * 2-hour samples for the past month
   * 1-day samples for the past yearData older than a year is purged from the vCenter Server database.Prior to version 25 of the API, this data object could be used in conjunction with the `CreatePerfInterval <vim/PerformanceManager.rst#createHistoricalInterval>`_ operation, to define new, custom historical intervals. That operation has been deprecated: Adding and deleting objects of this type is no longer supported. However, the default historical intervals can be enabled or disabled, and can be modified within certain limits (with the `UpdatePerfInterval <vim/PerformanceManager.rst#updateHistoricalInterval>`_ operation)
:extends: vmodl.DynamicData_

Attributes:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       A unique identifier for the interval.
    samplingPeriod (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of seconds that data is sampled for this interval. The real-time samplingPeriod is 20 seconds.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the historical interval. A localized string that provides a name for the interval. Names include:
        * "Past Day"
        * "Past Week"
        * "Past Month"
        * "Past Year"The name is not meaningful in terms of system behavior. That is, the interval namedPast Weekworks as it does because of its length, level, and so on, not because of the value of this string.
    length (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Number of seconds that the statistics corresponding to this interval are kept on the system.
    level (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Statistics collection level for this historical interval. vCenter Server will aggregate only those statistics that match the value of this property for this historical interval. For ESX, the value of this property is null. For vCenter Server, the value will be a number from 1 to 4.
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates whether the interval is enabled (true) or disabled (false). Disabling a historical interval prevents vCenter Server from collecting metrics for that interval and all higher (longer) intervals.For example, disabling the "Past Month" interval disables both "Past Month" and "Past Year" intervals. The system will aggregate and retain performance data using the "Past Day" and "Past Week" intervals only.
