
vim.StorageResourceManager.IORMConfigSpec
=========================================
  Configuration settings used for creating or reconfiguring storage I/O resource management.All fields are defined as optional. If a field is unset, the property is not changed.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether or not the service is enabled.
    congestionThresholdMode (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Mode of congestion threshold specification For more information, see `StorageIORMThresholdMode <vim/StorageResourceManager/CongestionThresholdMode.rst>`_ 
    congestionThreshold (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The latency beyond which the storage array is considered congested.For more information, see `congestionThreshold <vim/StorageResourceManager/IORMConfigInfo.rst#congestionThreshold>`_ 
    percentOfPeakThroughput (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The percentage of peak throughput to be used for setting threshold latency of a datastore. Valid values are between 50 to 100.For more information, see `congestionThreshold <vim/StorageResourceManager/IORMConfigInfo.rst#congestionThreshold>`_ 
    statsCollectionEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether the service is enabled in stats collection mode.
    statsAggregationDisabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether stats aggregation is disabled.
