.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vim.vm.device.VirtualDisk.RawDiskVer2BackingInfo: ../../../../vim/vm/device/VirtualDisk/RawDiskVer2BackingInfo.rst


vim.vm.device.VirtualDisk.PartitionedRawDiskVer2BackingInfo
===========================================================
  This data object type contains information about backing a virtual disk using one or more partitions on a physical disk device. This type of backing is supported for VMware Server.
:extends: vim.vm.device.VirtualDisk.RawDiskVer2BackingInfo_

Attributes:
    partition (`int`_):

       Array of partition indexes. This array identifies the partitions that are used on the physical disk drive.
