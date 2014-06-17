.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst


vim.vm.device.HostDiskMappingOption.PartitionOption
===================================================
  The PhysicalPartitionOption data class contains the options for a partition on a physical disk.
:extends: vmodl.DynamicData_

Attributes:
    name (`str`_):

       Partition name.
    fileSystem (`str`_):

       File system, if the partition is formatted.
    capacityInKb (`long`_):

       Partition capacity, in KB.
