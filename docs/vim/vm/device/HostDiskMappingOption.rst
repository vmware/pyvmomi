
vim.vm.device.HostDiskMappingOption
===================================
  The HostDiskMappingOption data object type describes the options for a virtual disk mapping to a host disk.
:extends: vmodl.DynamicData_

Attributes:
    physicalPartition ([`vim.vm.device.HostDiskMappingOption.PartitionOption <vim/vm/device/HostDiskMappingOption/PartitionOption.rst>`_], optional):

       Array of valid partitions on this physical disk. There is no default for this array.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Host resource name.
