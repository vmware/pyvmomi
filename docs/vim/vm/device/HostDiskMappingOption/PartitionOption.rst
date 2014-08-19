
vim.vm.device.HostDiskMappingOption.PartitionOption
===================================================
  The PhysicalPartitionOption data class contains the options for a partition on a physical disk.
:extends: vmodl.DynamicData_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Partition name.
    fileSystem (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       File system, if the partition is formatted.
    capacityInKb (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Partition capacity, in KB.
