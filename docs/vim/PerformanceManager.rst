
vim.PerformanceManager
======================
  This managed object type provides the service interface for obtaining statistical data about various aspects of system performance, as generated and maintained by the system's performance providers. A "performance provider" ( `PerfProviderSummary <vim/PerformanceManager/ProviderSummary.rst>`_ ) is any managed object that generates utilization or other performance metrics. Performance providers include `managed entities <vim/ManagedEntity.rst>`_ , such as `hosts <vim/HostSystem.rst>`_ , `virtual machines <vim/VirtualMachine.rst>`_ , `compute resources <vim/ComputeResource.rst>`_ , `resource pools <vim/ResourcePool.rst>`_ , `datastores <vim/Datastore.rst>`_ , and `networks <vim/Network.rst>`_ . Performance providers also include physical or virtual devices associated with these objects, such as virtual host-bus adapters and network-interface controllers (NICs)Performance CountersEach performance providerthe instrumented device or entityhas its own set of `counters <vim/PerformanceManager/CounterInfo.rst>`_ that provides metadata about its available `metrics <vim/PerformanceManager/EntityMetric.rst>`_ . Each counter has a unique `key <vim/PerformanceManager/CounterInfo.rst#key>`_ , referred to as the counterId. The actual performance metrics generated at runtime are identified by this `counterId <vim/PerformanceManager/MetricId.rst#counterId>`_ . Counters are organized by `groups <vim/PerformanceManager/CounterInfo.rst#groupInfo>`_ of finite system resources, such as `memory <memory_counters.rst>`_ , `CPU <cpu_counters.rst>`_ , `disk <disk_counters.rst>`_ , and so on. The links in this list contain documentation for performance counters, by `group <vim/PerformanceManager/CounterInfo.rst#groupInfo>`_ . Each page contains a table that includes data extracted from instances of the `PerfCounterInfo <vim/PerformanceManager/CounterInfo.rst>`_ data object, including the counter name, its Label, Unit, StatsType, RollupType, and Level:
   * 
   * `Cluster Services <cluster_services_counters.rst>`_ ` <cluster_services_counters.rst>`_ 
   * ` <cluster_services_counters.rst>`_
   * `CPU <cpu_counters.rst>`_
   * 
   * `Host-Based Replication <hbr_counters.rst>`_
   * 
   * `Management Agent <mgmt_agent_counters.rst>`_
   * 
   * `Memory <memory_counters.rst>`_
   * 
   * `Network <network_counters.rst>`_
   * 
   * `Power <power_counters.rst>`_
   * 
   * `Resource Scheduler <resource_scheduler_counters.rst>`_
   * Storage Capacity:
   * 
   * 
   * `Datastore / Virtual Machine <disk_storutil_counters.rst>`_
   * Storage I/O:
   * 
   * 
   * `Datastore <datastore_counters.rst>`_
   * 
   * `Disk <disk_counters.rst>`_
   * 
   * `Virtual Disk <virtual_disk_counters.rst>`_
   * 
   * `Storage Adapter <storage_adapter_counters.rst>`_
   * 
   * `Storage Path <storage_path_counters.rst>`_
   * `System <system_counters.rst>`_
   * `vCenter Resource <vcres_counters.rst>`_
   * `Virtual Machine Operations <vmop_counters.rst>`_Other performance-counter groups, in addition to those listed here, exist on the system. However, only the counter groups listed are considered of possible interest to third-party developers.Obtaining Metadata and MetricsThis interface provides these query operations:
   * 
   * `QueryPerfProviderSummary <vim/PerformanceManager.rst#queryProviderSummary>`_
   * , for obtaining metatdata about
   * `performance providers <vim/PerformanceManager/ProviderSummary.rst>`_
   * 
   * `QueryPerfCounter <vim/PerformanceManager.rst#queryCounter>`_
   * and
   * `QueryPerfCounterByLevel <vim/PerformanceManager.rst#queryCounterByLevel>`_
   * for obtaining metadata about supported counters.
   * 
   * `QueryPerf <vim/PerformanceManager.rst#queryStats>`_
   * ,
   * `QueryAvailablePerfMetric <vim/PerformanceManager.rst#queryAvailableMetric>`_
   * , and
   * `QueryPerfComposite <vim/PerformanceManager.rst#queryCompositeStats>`_
   * for obtaining statistics for one or more entities:
   * 
   * Use
   * `QueryPerf <vim/PerformanceManager.rst#queryStats>`_
   * to obtain metrics for multiple entities in a single call
   * Use
   * `QueryPerfComposite <vim/PerformanceManager.rst#queryCompositeStats>`_
   * to obtain statistics for a single entity with its descendent objects
   * statistics for a
   * `host <vim/HostSystem.rst>`_
   * and all its
   * `virtual machines <vim/VirtualMachine.rst>`_
   * , for example.Product and Version SpecificsSome differences between ESX and vCenter Server implementations of this interface include:
   * For ESX systems, this interface provides access to real-time data, and to real-time data that has been rolled up into "PastDay" statistics (if applicable for the specific counter).
   * For vCenter Server systems, this interface provides access to real-time and historical data. vCenter Server collects statistics on a regular basis from all ESX systems that it manages, and aggregates the results based on the level settings for the server.
   * Default sampling interval is product- and version-specific:
   * 
   * ESX 3
   * x (and subsequent) systems: 20 second interval
   * ESX 2
   * x systems: 60 second interval
   * VirtualCenter Server 2
   * 5 (and subsequent vCenter Server) systems initially collect statistics data 10 minutes after system startup, and then hourly thereafterSee the Programming Guide for more information about using `PerformanceManager <vim/PerformanceManager.rst>`_ 




Attributes
----------
    description (`vim.PerformanceDescription <vim/PerformanceDescription.rst>`_):
      privilege: System.View
       The static description strings.
    historicalInterval ([`vim.HistoricalInterval <vim/HistoricalInterval.rst>`_]):
      privilege: System.View
       A list of `intervals <vim/HistoricalInterval.rst>`_ configured on the system.
    perfCounter ([`vim.PerformanceManager.CounterInfo <vim/PerformanceManager/CounterInfo.rst>`_]):
      privilege: System.View
       A list of all supported performance counters in the system.


Methods
-------


QueryPerfProviderSummary(entity):
   Retrieves the `PerfProviderSummary <vim/PerformanceManager/ProviderSummary.rst>`_ data object that defines the capabilities of the specified managed object with respect to statistics, such as whether it supports current or summary statistics


  Privilege:
               System.Read



  Args:
    entity (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_):
       Reference to a managed object that provides performance data. If the entity specified by managed object reference is not a performance provider, an "InvalidArgument" exception is thrown.




  Returns:
    `vim.PerformanceManager.ProviderSummary <vim/PerformanceManager/ProviderSummary.rst>`_:
         A data object containing metadata about the entity as a performance provider, such as the type of metrics (real-time, summary, or both) it generates and the `refreshRate <vim/PerformanceManager/ProviderSummary.rst#refreshRate>`_ .


QueryAvailablePerfMetric(entity, beginTime, endTime, intervalId):
   Retrieves all performance counters for the specified `managed object <vim/ExtensibleManagedObject.rst>`_ generated during a specified period of time. The time period can be specified using beginTime, endTime, or by interval ID.


  Privilege:
               System.Read



  Args:
    entity (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_):
       The `managed object <vim/PerformanceManager/ProviderSummary.rst#entity>`_ that provides performance metrics.


    beginTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       Starting time (server time) for a period of time from which to return available metrics. If not specified, defaults to oldest available metric for the specified entity.


    endTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       Ending time (server time) for a period of time from which to return available performance metrics. If not specified, defaults to the most recently generated metric for the specified entity.


    intervalId (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):
       Period of time from which to retrieve metrics, defined by intervalId (rather than beginTime or endTime). Valid intervalIds include:
        * For real-time counters, the
        * `refreshRate <vim/PerformanceManager/ProviderSummary.rst#refreshRate>`_
        * of the
        * `performance provider <vim/PerformanceManager/ProviderSummary.rst>`_
        * .
        * For historical counters, the
        * `samplingPeriod <vim/HistoricalInterval.rst#samplingPeriod>`_
        * of the
        * `historical interval <vim/HistoricalInterval.rst>`_
        * .If this parameter is not specified, the system returns available metrics for historical statistics




  Returns:
    [`vim.PerformanceManager.MetricId <vim/PerformanceManager/MetricId.rst>`_]:
         An array of metrics, each of which comprises a `counterId <vim/PerformanceManager/MetricId.rst#counterId>`_ and an `name <vim/PerformanceManager/MetricId.rst#instance>`_ .

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the set of arguments passed to the function is not specified correctly.


QueryPerfCounter(counterId):
   Retrieves counter information for the specified list of counter IDs.


  Privilege:
               System.View



  Args:
    counterId (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       An array of one or more `counterIds <vim/PerformanceManager/MetricId.rst#counterId>`_ representing performance counters for which information is being retrieved.




  Returns:
    [`vim.PerformanceManager.CounterInfo <vim/PerformanceManager/CounterInfo.rst>`_]:
         An array consisting of performance counter information for the specified counterIds.

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the set of arguments passed to the function is not specified correctly.


QueryPerfCounterByLevel(level):
   Retrieves the set of counters that are available at a specified collection `level <vim/HistoricalInterval.rst#level>`_ . The collection level determines the statistics that get stored in VirtualCenter. See `PerfInterval <vim/HistoricalInterval.rst>`_ for more information about VirtualCenter Server historical statistics collection.
  since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_


  Privilege:
               System.View



  Args:
    level (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       A number between 1 and 4 that specifies the collection level.




  Returns:
    [`vim.PerformanceManager.CounterInfo <vim/PerformanceManager/CounterInfo.rst>`_]:
         An array of `PerfCounterInfo <vim/PerformanceManager/CounterInfo.rst>`_ objects that define the set of counters having the specified level number available for the entity.

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if an invalid level is specified.


QueryPerf(querySpec):
   Retrieves the performance metrics for the specified entity (or entities) based on the properties specified in the `PerfQuerySpec <vim/PerformanceManager/QuerySpec.rst>`_ data object.Query Performance for VirtualCenter Server


  Privilege:
               System.View



  Args:
    querySpec (`vim.PerformanceManager.QuerySpec <vim/PerformanceManager/QuerySpec.rst>`_):
       An array of `PerfQuerySpec <vim/PerformanceManager/QuerySpec.rst>`_ objects. Each `PerfQuerySpec <vim/PerformanceManager/QuerySpec.rst>`_ object specifies a managed object reference for an entity, plus optional criteria for filtering results. Only metrics for entities that can be resolved and that are valid `performance providers <vim/PerformanceManager/ProviderSummary.rst>`_ are returned in any result.Each `PerfQuerySpec <vim/PerformanceManager/QuerySpec.rst>`_ object in the array submitted in this operation can query for different metrics. Or, select all types of statistics for a single managed entity.Raw data feed workaround: Normally, QueryPerf will return performance statistics stored in the VirtualCenter database. However this may not be suitable for certain applications. For example, applications that treat VirtualCenter as a raw data source, query for performance statistics regularly (say every 5 minutes) and extract the data for external archival and reporting. Such applications need better query performance. These applications should query statistics using QueryPerf for the base historical interval (5 minutes by default) having a start and end time range within 30 minutes from the current VirtualCenter server system time. These QueryPerf calls will have better performance than other QueryPerf calls.




  Returns:
    [`vim.PerformanceManager.EntityMetricBase <vim/PerformanceManager/EntityMetricBase.rst>`_]:
         The metric values for the specified entity or entities.

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the set of arguments passed to the function is not specified correctly.


QueryPerfComposite(querySpec):
   Retrieves a `PerfCompositeMetric <vim/PerformanceManager/CompositeEntityMetric.rst>`_ data object that comprises statistics for the specified entity and its children entities. Only metrics for the first level of descendents are included in the `PerfCompositeMetric <vim/PerformanceManager/CompositeEntityMetric.rst>`_ object.Use this operation to obtain statistics for a `host <vim/HostSystem.rst>`_ and its associated `virtual machines <vim/VirtualMachine.rst>`_ , for example.Requiressystem.readprivilege for every virtual machine on the target host, or the query fails with theNoPermissionfault. Suported for `HostSystem <vim/HostSystem.rst>`_ managed entities only.


  Privilege:
               System.View



  Args:
    querySpec (`vim.PerformanceManager.QuerySpec <vim/PerformanceManager/QuerySpec.rst>`_):
       A `PerfQuerySpec <vim/PerformanceManager/QuerySpec.rst>`_ object specifying the query parameters. This `PerfQuerySpec <vim/PerformanceManager/QuerySpec.rst>`_ object specifies a managed object for which composite statistics should be retrieved, with specific optional criteria for filtering the results.This `PerfQuerySpec <vim/PerformanceManager/QuerySpec.rst>`_ requires a valid `metricId <vim/PerformanceManager/QuerySpec.rst#metricId>`_ property that specifies a metric that is available, in common, to the entity and its children. If the specified metricId is not available to the entity and its children, it is ignored.




  Returns:
    `vim.PerformanceManager.CompositeEntityMetric <vim/PerformanceManager/CompositeEntityMetric.rst>`_:
         The metric values for the specified entity and its associated entities for a single interval.

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the set of arguments passed to the function is not specified correctly.


CreatePerfInterval(intervalId):
   Adds a new historical interval. Sampling period for new interval must be a multiple of an existing interval; must comprise a longer period of time; and must be uniquely named.


  Privilege:
               Performance.ModifyIntervals



  Args:
    intervalId (`vim.HistoricalInterval <vim/HistoricalInterval.rst>`_):
       A custom interval, specified as the number of seconds to hold data in the database, a user-specified unique name, and a sampling period (in seconds).




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the set of arguments passed to the function is not specified correctly.


RemovePerfInterval(samplePeriod):
   Removes an interval from the list.


  Privilege:
               Performance.ModifyIntervals



  Args:
    samplePeriod (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       The sampling period, in seconds, for the specified interval being removed.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the set of arguments passed to the function is not specified correctly.


UpdatePerfInterval(interval):
   Modifies VirtualCenter Server's built-in `historical intervals <vim/HistoricalInterval.rst>`_ , within certain limits.Supported ModificationskeysamplingPeriodlengthnamelevel [1]enabled [2]1300 [3]86400 [4]Pastday1true21800604800Pastweek1true372002592000Pastmonth1true46640031536000 [5]Pastyear1true[1]The collection level for the `historical intervals <vim/HistoricalInterval.rst>`_ can be changed. However, the level specified for a lower-numbered interval cannot be smaller than that of a larger interval.[2]An interval can be disabled. By default, all four intervals are enabled. Disabling an interval disables all higher intervals. For example, disabling interval 3 (Past month) also disables interval 4 (Past year).[3]Can reduce this intervals `samplingPeriod <vim/HistoricalInterval.rst#samplingPeriod>`_ from 5 minutes to 1, 2, or 3 minutes.[4]Can increase this intervals `length <vim/HistoricalInterval.rst#length>`_ from 1 day to 2 or 3 days.[5]Can increase intervals `length <vim/HistoricalInterval.rst#length>`_ from 1 year to 2 or 3 years.See `PerfInterval <vim/HistoricalInterval.rst>`_ for information about the four default intervals for VirtualCenter Server.


  Privilege:
               Performance.ModifyIntervals



  Args:
    interval (`vim.HistoricalInterval <vim/HistoricalInterval.rst>`_):
       The `historical interval <vim/HistoricalInterval.rst>`_ being modified, a complete data object comprising values for `enabled <vim/HistoricalInterval.rst#enabled>`_ , `interval ID <vim/HistoricalInterval.rst#key>`_ , `length <vim/HistoricalInterval.rst#length>`_ of time to maintain statistics for this interval in the database, `level <vim/HistoricalInterval.rst#level>`_ , `name <vim/HistoricalInterval.rst#name>`_ , and `samplingPeriod <vim/HistoricalInterval.rst#samplingPeriod>`_ properties.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       if the set of arguments passed to the function is not specified correctly or if the update does not conform to the rules mentioned above.


UpdateCounterLevelMapping(counterLevelMap):
   Changes the level of data collection for a set of performance counters. See the `performance counter tables <#counterTables>`_ for the default collection level for individual counters.Important:Consider the performance and storage consequences of using this method. You may cause a significant increase in data collection and storage, along with a corresponding decrease in performance. vCenter Server performance and database storage requirements depend on the collection levels defined for the performance intervals (PerformanceManager. `historicalInterval <vim/PerformanceManager.rst#historicalInterval>`_ ) and the collection levels specified for individual performance counters ( `PerfCounterInfo <vim/PerformanceManager/CounterInfo.rst>`_ . `level <vim/PerformanceManager/CounterInfo.rst#level>`_ ).Performance Counter Data CollectionvSphere defines four levels of data collection for performance counters. Each performance counter specifies a level for collection. The historical performance intervals (PerformanceManager. `historicalInterval <vim/PerformanceManager.rst#historicalInterval>`_ ) define the sampling period and length for a particular collection level.The amount of data collected for a performance counter depends on the performance interval and on the type of entity for which the counter is defined. For example, a datastore counter such as datastoreIops (the aggregate number of IO operations on the datastore) will generate a data set that corresponds to the number of datastores on a host. If a vCenter Server manages a large number of hosts with a large number of datastores, the Server will collect a large amount of data.There are other counters for which the vCenter Server collects a relatively smaller amount of data. For example, memory counters are collected as a single counter per virtual machine and a single counter per host.Performance Counter Data StorageThe performance interval collection `level <vim/PerformanceManager/CounterInfo.rst#level>`_ defines the set of counters for which the vCenter Server stores performance data. The Server will store data for counters at the specified level and for counters at all lower levels.By default, all the performance intervals specify collection level one. Using these defaults, the vCenter Server stores performance counter data in the vCenter database for all counters that specify collection level one. It does not store data for counters that specify collection levels two through four.Performance Manager Method InteractionYou can use the UpdateCounterLevelMapping method to change the collection level for individual counters. You can also use the `UpdatePerfInterval <vim/PerformanceManager.rst#updateHistoricalInterval>`_ method to change the collection level for the system-defined performance intervals. These methods can cause a significant increase in the amount of data collected and stored in the vCenter database.You may cause a significant increase in data collection and storage along with a corresponding decrease in performance under the following conditions:
    * By default the system-defined performance intervals use collection level one, storing data for all counters that specify collection level one. If you use the UpdateCounterLevelMapping method to change the collection level of performance counters to level one, you will increase the amount of stored performance data.
    * If you use the
    * `UpdatePerfInterval <vim/PerformanceManager.rst#updateHistoricalInterval>`_
    * method to increase the collection level for the system-defined performance intervals, you will increase the amount of stored performance data.To restore counter levels to default settings use the `ResetCounterLevelMapping <vim/PerformanceManager.rst#resetCounterLevelMapping>`_ method.
  since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_


  Privilege:
               Performance.ModifyIntervals



  Args:
    counterLevelMap (`vim.PerformanceManager.CounterLevelMapping <vim/PerformanceManager/CounterLevelMapping.rst>`_):
       An array of `PerformanceManagerCounterLevelMapping <vim/PerformanceManager/CounterLevelMapping.rst>`_ objects. The levels for the counters passed in are changed to the passed in values. If the optional aggregateLevel field is left unset then only the perDeviceLevel is configured. If the optional perDeviceLevel is left unset then only the aggregateLevel is configured. If there are multiple entries in the passed in array for the same counterId being updated then the last entry containing the counterId takes effect.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If the passed in counterId is invalid or if both the aggregateLevel and perDeviceLevel are unset or if the aggregateLevel field is not between 1-4 (valid values).

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       If called directly on a host.


ResetCounterLevelMapping(counters):
   Restores a set of performance counters to the default level of data collection. See the `performance counter tables <#counterTables>`_ for the default collection level for individual counters.
  since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_


  Privilege:
               Performance.ModifyIntervals



  Args:
    counters (`int <https://docs.python.org/2/library/stdtypes.html>`_):
       An array of counter ids.




  Returns:
    None
         

  Raises:

    `vmodl.fault.InvalidArgument <vmodl/fault/InvalidArgument.rst>`_: 
       If the passed in counterId is invalid.

    `vmodl.fault.NotSupported <vmodl/fault/NotSupported.rst>`_: 
       If called directly on a host.


