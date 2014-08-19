
vim.host.DiskPartitionInfo.BlockRange
=====================================
  A BlockRange data object type describes a contiguous set of blocks on a disk. A BlockRange may describe either a partition or unpartitioned (primordial) blocks on the disk.
:extends: vmodl.DynamicData_

Attributes:
    partition (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Partition number. This number is a hint from the server indicating what the partition number for this block range is if the range corresponds to a partition. The partition number should correlate to the one in the partition specification. If sent back to the server, this property is ignored.
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The type of data in the partition.See `type <vim/host/DiskPartitionInfo/Partition.rst#type>`_ 
    start (`vim.host.DiskDimensions.Lba <vim/host/DiskDimensions/Lba.rst>`_):

       The starting block address of the disk range. The block numbers start from zero. The range is inclusive of the end address.
    end (`vim.host.DiskDimensions.Lba <vim/host/DiskDimensions/Lba.rst>`_):

       The end block address of the disk range. The block numbers start from zero. The range is inclusive of the end address.
