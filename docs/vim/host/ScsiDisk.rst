
vim.host.ScsiDisk
=================
  This data object type describes a SCSI disk. A SCSI disk contains a partition table which can be changed. To change a SCSI disk, use the device name and the partition specification.See `RetrieveDiskPartitionInfo <vim/host/StorageSystem.rst#retrieveDiskPartitionInfo>`_ See `UpdateDiskPartitions <vim/host/StorageSystem.rst#updateDiskPartitions>`_ 
:extends: vim.host.ScsiLun_

Attributes:
    capacity (`vim.host.DiskDimensions.Lba <vim/host/DiskDimensions/Lba.rst>`_):

       The size of SCSI disk using the Logical Block Addressing scheme.
    devicePath (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The device path of the ScsiDisk. This device path is a file path that can be opened to create partitions on the disk.See `RetrieveDiskPartitionInfo <vim/host/StorageSystem.rst#retrieveDiskPartitionInfo>`_ See `UpdateDiskPartitions <vim/host/StorageSystem.rst#updateDiskPartitions>`_ 
    ssd (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether the ScsiDisk is SSD backed. If unset, the information whether the ScsiDisk is SSD backed is unknown.
