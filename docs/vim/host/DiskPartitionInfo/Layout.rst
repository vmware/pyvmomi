.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.DiskDimensions.Lba: ../../../vim/host/DiskDimensions/Lba.rst

.. _vim.host.DiskPartitionInfo.BlockRange: ../../../vim/host/DiskPartitionInfo/BlockRange.rst


vim.host.DiskPartitionInfo.Layout
=================================
  This data object type describes the disk partition layout specified as a list of ordered BlockRanges. This view of the disk partitions shows the data on the disk as a contiguous set of BlockRanges.
:extends: vmodl.DynamicData_

Attributes:
    total (`vim.host.DiskDimensions.Lba`_, optional):

       Total number of blocks on a disk.
    partition ([`vim.host.DiskPartitionInfo.BlockRange`_]):

       List of block ranges on the disk.
