.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.DiskDimensions.Chs: ../../../vim/host/DiskDimensions/Chs.rst

.. _vim.host.DiskPartitionInfo.Partition: ../../../vim/host/DiskPartitionInfo/Partition.rst


vim.host.DiskPartitionInfo.Specification
========================================
  This data object type describes the disk partition table specification used to configure the partitions on a disk. This data object represents the fundamental data needed to specify a partition table.
:extends: vmodl.DynamicData_

Attributes:
    partitionFormat (`str`_, optional):

       Partition format type on the disk.
    chs (`vim.host.DiskDimensions.Chs`_, optional):

       Disk dimensions expressed as cylinder, head, sector (CHS) coordinates.
    totalSectors (`long`_, optional):

       Disk dimensions expressed in total number of 512-byte sectors.
    partition (`vim.host.DiskPartitionInfo.Partition`_, optional):

       List of partitions on the disk.
