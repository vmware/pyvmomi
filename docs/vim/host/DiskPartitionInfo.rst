
vim.host.DiskPartitionInfo
==========================
  Information about the partitions on a disk. A DiskPartitionInfo object provides two different views into the partitions on a disk:
   * A detailed specification that is used to create the partition table.
   * A convenient view that shows the allocations of blocks as a contiguous sequence of block ranges.
   * See
   * `RetrieveDiskPartitionInfo <vim/host/StorageSystem.rst#retrieveDiskPartitionInfo>`_
   * See
   * `ComputeDiskPartitionInfo <vim/host/StorageSystem.rst#computeDiskPartitionInfo>`_
   * See
   * `UpdateDiskPartitions <vim/host/StorageSystem.rst#updateDiskPartitions>`_
   * 
:extends: vmodl.DynamicData_

Attributes:
    deviceName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The device name of the disk to which this partition information corresponds.
    spec (`vim.host.DiskPartitionInfo.Specification <vim/host/DiskPartitionInfo/Specification.rst>`_):

       The detailed disk partition specification. Use this specification for manipulating the file system.See `RetrieveDiskPartitionInfo <vim/host/StorageSystem.rst#retrieveDiskPartitionInfo>`_ See `UpdateDiskPartitions <vim/host/StorageSystem.rst#updateDiskPartitions>`_ 
    layout (`vim.host.DiskPartitionInfo.Layout <vim/host/DiskPartitionInfo/Layout.rst>`_):

       A convenient format for describing disk layout. This layout specification can be converted to a Specification object.See `ComputeDiskPartitionInfo <vim/host/StorageSystem.rst#computeDiskPartitionInfo>`_ 
