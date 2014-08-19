
vim.vm.device.HostDiskMappingInfo
=================================
  The HostDiskMappingInfo data object type describes a virtual disk mapping to a host disk.
:extends: vmodl.DynamicData_

Attributes:
    physicalPartition (`vim.vm.device.HostDiskMappingInfo.PartitionInfo <vim/vm/device/HostDiskMappingInfo/PartitionInfo.rst>`_, optional):

       The partition used on the host, if not mapping to a full disk device.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Host resource name.
    exclusive (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether or not the virtual machine has exclusive access to the host device.
