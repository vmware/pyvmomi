.. _int: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.DiskDimensions.Lba
===========================
  This data object type describes the logical block addressing system that uses block numbers and block sizes to refer to a block. This scheme is employed by SCSI. If a SCSI disk is not involved, then blockSize is 512 bytes.
:extends: vmodl.DynamicData_

Attributes:
    blockSize (`int`_):

       The size of the blocks.
    block (`long`_):

       The number of blocks.
