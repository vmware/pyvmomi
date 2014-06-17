.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _UpdateDiskPartitions: ../../vim/host/StorageSystem.rst#updateDiskPartitions

.. _ComputeDiskPartitionInfo: ../../vim/host/StorageSystem.rst#computeDiskPartitionInfo

.. _RetrieveDiskPartitionInfo: ../../vim/host/StorageSystem.rst#retrieveDiskPartitionInfo

.. _vim.host.DiskPartitionInfo.Layout: ../../vim/host/DiskPartitionInfo/Layout.rst

.. _vim.host.DiskPartitionInfo.Specification: ../../vim/host/DiskPartitionInfo/Specification.rst


vim.host.DiskPartitionInfo
==========================
  Information about the partitions on a disk. A DiskPartitionInfo object provides two different views into the partitions on a disk:
   * A detailed specification that is used to create the partition table.
   * A convenient view that shows the allocations of blocks as a contiguous sequence of block ranges.
   * See
   * `RetrieveDiskPartitionInfo`_
   * See
   * `ComputeDiskPartitionInfo`_
   * See
   * `UpdateDiskPartitions`_
   * 
:extends: vmodl.DynamicData_

Attributes:
    deviceName (`str`_):

       The device name of the disk to which this partition information corresponds.
    spec (`vim.host.DiskPartitionInfo.Specification`_):

       The detailed disk partition specification. Use this specification for manipulating the file system.See `RetrieveDiskPartitionInfo`_ See `UpdateDiskPartitions`_ 
    layout (`vim.host.DiskPartitionInfo.Layout`_):

       A convenient format for describing disk layout. This layout specification can be converted to a Specification object.See `ComputeDiskPartitionInfo`_ 
