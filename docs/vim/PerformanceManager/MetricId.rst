.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _metricId: ../../vim/PerformanceManager/QuerySpec.rst#metricId

.. _instance: ../../vim/PerformanceManager/MetricId.rst#instance

.. _counterId: ../../vim/PerformanceManager/MetricId.rst#counterId

.. _PerfQuerySpec: ../../vim/PerformanceManager/QuerySpec.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _PerformanceManager: ../../vim/PerformanceManager.rst


vim.PerformanceManager.MetricId
===============================
  This data object type contains information that associates a performance counter with a performance metric. When constructing this data object for the `metricId`_ property of the `PerfQuerySpec`_ to submit to one of the `PerformanceManager`_ query operations, the `instance`_ property supports these special characters:
   * An asterisk (*) to specify all instances of the metric for the specified
   * `counterId`_
   * 
   * Double-quotes ("") to specify aggregated statistics
:extends: vmodl.DynamicData_

Attributes:
    counterId (`int`_):

       The `ID`_ of the counter for the metric.
    instance (`str`_):

       An identifier that is derived from configuration names for the device associated with the metric. It identifies the instance of the metric with its source. This property may be empty.
        * For memory and aggregated statistics, this property is empty.
        * For host and virtual machine devices, this property contains the name of the device, such as the name of the host-bus adapter or the name of the virtual Ethernet adapter. For example,
        * mpx
        * vmhba33
        * C0
        * T0
        * L0
        * or
        * vmnic0
        * 
        * For a CPU, this property identifies the numeric position within the CPU core, such as 0, 1, 2, 3.
        * For a virtual disk, this property identifies the file type:
        * 
        * DISKFILE, for virtual machine base-disk files
        * SWAPFILE, for virtual machine swap files
        * DELTAFILE, for virtual machine snapshot overhead files
        * OTHERFILE, for all other files of a virtual machine
