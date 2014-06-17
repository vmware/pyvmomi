.. _int: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _UpdatePerfInterval: ../../vim/PerformanceManager.rst#updateHistoricalInterval


vim.PerformanceManager.SampleInfo
=================================
  This data object type describes information contained in a sample collection, its timestamp, and sampling interval.
:extends: vmodl.DynamicData_

Attributes:
    timestamp (`datetime`_):

       The time at which the sample was collected.
    interval (`int`_):

       The interval in seconds for which performance statistics were collected. This can be the refreshRate of the managed object for which this statistics was collected or one of the intervals for historical statistics configured in the system. See `UpdatePerfInterval`_ for more information about the intervals configured in the system.
