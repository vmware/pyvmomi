
vim.host.DiskPartitionInfo.Specification
========================================
  This data object type describes the disk partition table specification used to configure the partitions on a disk. This data object represents the fundamental data needed to specify a partition table.
:extends: vmodl.DynamicData_

Attributes:
    partitionFormat (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Partition format type on the disk.
    chs (`vim.host.DiskDimensions.Chs <vim/host/DiskDimensions/Chs.rst>`_, optional):

       Disk dimensions expressed as cylinder, head, sector (CHS) coordinates.
    totalSectors (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Disk dimensions expressed in total number of 512-byte sectors.
    partition ([`vim.host.DiskPartitionInfo.Partition <vim/host/DiskPartitionInfo/Partition.rst>`_], optional):

       List of partitions on the disk.
