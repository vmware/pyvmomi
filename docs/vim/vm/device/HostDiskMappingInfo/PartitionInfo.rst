
vim.vm.device.HostDiskMappingInfo.PartitionInfo
===============================================
  The PhysicalPartitionInfo data class.
:extends: vmodl.DynamicData_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Partition name.
    fileSystem (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Filesystem, if the partition is formatted.
    capacityInKb (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Partition capacity, in KB.
