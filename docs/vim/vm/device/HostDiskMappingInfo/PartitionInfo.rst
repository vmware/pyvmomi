.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst


vim.vm.device.HostDiskMappingInfo.PartitionInfo
===============================================
  The PhysicalPartitionInfo data class.
:extends: vmodl.DynamicData_

Attributes:
    name (`str`_):

       Partition name.
    fileSystem (`str`_):

       Filesystem, if the partition is formatted.
    capacityInKb (`long`_):

       Partition capacity, in KB.
