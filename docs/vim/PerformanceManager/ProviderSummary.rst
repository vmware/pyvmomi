.. _int: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _intervals: ../../vim/HistoricalInterval.rst

.. _QueryPerf: ../../vim/PerformanceManager.rst#queryStats

.. _intervalId: ../../vim/PerformanceManager/QuerySpec.rst#intervalId

.. _refreshRate: ../../vim/PerformanceManager/ProviderSummary.rst#refreshRate

.. _host systems: ../../vim/HostSystem.rst

.. _PerfQuerySpec: ../../vim/PerformanceManager/QuerySpec.rst

.. _managed object: ../../vim/ExtensibleManagedObject.rst

.. _resource pools: ../../vim/ResourcePool.rst

.. _currentSupported: ../../vim/PerformanceManager/ProviderSummary.rst#currentSupported

.. _virtual machines: ../../vim/VirtualMachine.rst

.. _managed entities: ../../vim/ManagedEntity.rst

.. _summarySupported: ../../vim/PerformanceManager/ProviderSummary.rst#summarySupported

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vmodl.ManagedObject: ../../vim.ExtensibleManagedObject.rst


vim.PerformanceManager.ProviderSummary
======================================
  This data object type contains information about a performance provider, the type of statistics it generates, and the `refreshRate`_ for statistics generation. A performance provider is any `managed object`_ that generates real-time or historical statistics (or boththe `currentSupported`_ and `summarySupported`_ properties are not mutually exclusive).
:extends: vmodl.DynamicData_

Attributes:
    entity (`vmodl.ManagedObject`_):

       Reference to the performance provider, the `managed object`_ that provides real-time or historical metrics. The managed objects include but are not limited to `managed entities`_ , such as `host systems`_ , `virtual machines`_ , and `resource pools`_ .
    currentSupported (`bool`_):

       True if this entity supports real-time (current) statistics; false if it does not. If this property is true for an entity, a client application can set the `intervalId`_ of the `PerfQuerySpec`_ (passed to the `QueryPerf`_ operation) to the `refreshRate`_ to obtain the maximum information possible for the entity.
    summarySupported (`bool`_):

       True if this entity supports historical (aggregated) statistics; false if it does not. When this property is true for an entity, a client application can set the `intervalId`_ of `QueryPerf`_ to one of the historical `intervals`_ to obtain historical statistics for this entity.
    refreshRate (`int`_, optional):

       Number of seconds between the generation of each counter. This value applies only to entities that support real-time (current) statistics
