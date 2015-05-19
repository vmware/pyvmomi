.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _congestionThreshold: ../../vim/StorageResourceManager/IORMConfigInfo.rst#congestionThreshold

.. _StorageIORMThresholdMode: ../../vim/StorageResourceManager/CongestionThresholdMode.rst


vim.StorageResourceManager.IORMConfigSpec
=========================================
  Configuration settings used for creating or reconfiguring storage I/O resource management.All fields are defined as optional. If a field is unset, the property is not changed.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    enabled (`bool`_, optional):

       Flag indicating whether or not the service is enabled.
    congestionThresholdMode (`str`_, optional):

       Mode of congestion threshold specification For more information, see `StorageIORMThresholdMode`_ 
    congestionThreshold (`int`_, optional):

       The latency beyond which the storage array is considered congested.For more information, see `congestionThreshold`_ 
    percentOfPeakThroughput (`int`_, optional):

       The percentage of peak throughput to be used for setting threshold latency of a datastore. Valid values are between 50 to 100.For more information, see `congestionThreshold`_ 
    statsCollectionEnabled (`bool`_, optional):

       Flag indicating whether the service is enabled in stats collection mode.
    statsAggregationDisabled (`bool`_, optional):

       Flag indicating whether stats aggregation is disabled.
