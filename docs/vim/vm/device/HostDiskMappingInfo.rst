.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.vm.device.HostDiskMappingInfo.PartitionInfo: ../../../vim/vm/device/HostDiskMappingInfo/PartitionInfo.rst


vim.vm.device.HostDiskMappingInfo
=================================
  The HostDiskMappingInfo data object type describes a virtual disk mapping to a host disk.
:extends: vmodl.DynamicData_

Attributes:
    physicalPartition (`vim.vm.device.HostDiskMappingInfo.PartitionInfo`_, optional):

       The partition used on the host, if not mapping to a full disk device.
    name (`str`_):

       Host resource name.
    exclusive (`bool`_, optional):

       Flag to indicate whether or not the virtual machine has exclusive access to the host device.
