.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.host.ScsiLun: ../../vim/host/ScsiLun.rst

.. _UpdateDiskPartitions: ../../vim/host/StorageSystem.rst#updateDiskPartitions

.. _RetrieveDiskPartitionInfo: ../../vim/host/StorageSystem.rst#retrieveDiskPartitionInfo

.. _vim.host.DiskDimensions.Lba: ../../vim/host/DiskDimensions/Lba.rst


vim.host.ScsiDisk
=================
  This data object type describes a SCSI disk. A SCSI disk contains a partition table which can be changed. To change a SCSI disk, use the device name and the partition specification.See `RetrieveDiskPartitionInfo`_ See `UpdateDiskPartitions`_ 
:extends: vim.host.ScsiLun_

Attributes:
    capacity (`vim.host.DiskDimensions.Lba`_):

       The size of SCSI disk using the Logical Block Addressing scheme.
    devicePath (`str`_):

       The device path of the ScsiDisk. This device path is a file path that can be opened to create partitions on the disk.See `RetrieveDiskPartitionInfo`_ See `UpdateDiskPartitions`_ 
    ssd (`bool`_, optional):

       Indicates whether the ScsiDisk is SSD backed. If unset, the information whether the ScsiDisk is SSD backed is unknown.
