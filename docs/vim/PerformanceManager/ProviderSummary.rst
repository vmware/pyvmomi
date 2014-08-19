
vim.PerformanceManager.ProviderSummary
======================================
  This data object type contains information about a performance provider, the type of statistics it generates, and the `refreshRate <vim/PerformanceManager/ProviderSummary.rst#refreshRate>`_ for statistics generation. A performance provider is any `managed object <vim/ExtensibleManagedObject.rst>`_ that generates real-time or historical statistics (or boththe `currentSupported <vim/PerformanceManager/ProviderSummary.rst#currentSupported>`_ and `summarySupported <vim/PerformanceManager/ProviderSummary.rst#summarySupported>`_ properties are not mutually exclusive).
:extends: vmodl.DynamicData_

Attributes:
    entity (`vmodl.ManagedObject <vim.ExtensibleManagedObject.rst>`_):

       Reference to the performance provider, the `managed object <vim/ExtensibleManagedObject.rst>`_ that provides real-time or historical metrics. The managed objects include but are not limited to `managed entities <vim/ManagedEntity.rst>`_ , such as `host systems <vim/HostSystem.rst>`_ , `virtual machines <vim/VirtualMachine.rst>`_ , and `resource pools <vim/ResourcePool.rst>`_ .
    currentSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if this entity supports real-time (current) statistics; false if it does not. If this property is true for an entity, a client application can set the `intervalId <vim/PerformanceManager/QuerySpec.rst#intervalId>`_ of the `PerfQuerySpec <vim/PerformanceManager/QuerySpec.rst>`_ (passed to the `QueryPerf <vim/PerformanceManager.rst#queryStats>`_ operation) to the `refreshRate <vim/PerformanceManager/ProviderSummary.rst#refreshRate>`_ to obtain the maximum information possible for the entity.
    summarySupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if this entity supports historical (aggregated) statistics; false if it does not. When this property is true for an entity, a client application can set the `intervalId <vim/PerformanceManager/QuerySpec.rst#intervalId>`_ of `QueryPerf <vim/PerformanceManager.rst#queryStats>`_ to one of the historical `intervals <vim/HistoricalInterval.rst>`_ to obtain historical statistics for this entity.
    refreshRate (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Number of seconds between the generation of each counter. This value applies only to entities that support real-time (current) statistics
