
vim.StorageResourceManager.IORMConfigInfo
=========================================
  Configuration of storage I/O resource management.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether or not the service is enabled.
    congestionThresholdMode (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Mode of congestion threshold specification For more information, see `StorageIORMThresholdMode <vim/StorageResourceManager/CongestionThresholdMode.rst>`_ 
    congestionThreshold (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The latency beyond which the storage array is considered congested.If storage I/O resource management is enabled on a datastore, the algorithm tries to maintain the latency to be below or close to this value. The unit is millisecond. The range of this value is between 5 to 100 milliseconds.
    percentOfPeakThroughput (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The percentage of peak throughput to be used for setting congestion threshold of a datastore. Valid values are between 50 to 100. Default value is 90%For more information, see `congestionThreshold <vim/StorageResourceManager/IORMConfigInfo.rst#congestionThreshold>`_ 
    statsCollectionEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether service is running in stats collection mode.
    statsAggregationDisabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag indicating whether stats aggregation is disabled.
