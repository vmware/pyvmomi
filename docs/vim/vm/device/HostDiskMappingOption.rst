.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.vm.device.HostDiskMappingOption.PartitionOption: ../../../vim/vm/device/HostDiskMappingOption/PartitionOption.rst


vim.vm.device.HostDiskMappingOption
===================================
  The HostDiskMappingOption data object type describes the options for a virtual disk mapping to a host disk.
:extends: vmodl.DynamicData_

Attributes:
    physicalPartition (`vim.vm.device.HostDiskMappingOption.PartitionOption`_, optional):

       Array of valid partitions on this physical disk. There is no default for this array.
    name (`str`_):

       Host resource name.
