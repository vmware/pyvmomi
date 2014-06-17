.. _int: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.HbrManager.ReplicationVmInfo.ProgressInfo
=============================================
  A set of statistics related to the progress of the current operation (full sync or lwd).
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    progress (`int`_):

       An estimation of the operation progress as a percentage completed, from 0 to 100.
    bytesTransferred (`long`_):

       Number of bytes transferred so far.For sync operations, this value includes (i.e. counts multiple times) areas that were transferred multiple times (due to stopping and continuing the operation, or for some errors).
    bytesToTransfer (`long`_):

       The total number of bytes to be transferred.For lwd operations, this is the total size of the disk images that are transferring. This is known from the start and will not change during a lwd operation.For sync operations, this is the total size of the blocks that have been found not to match between the primary and secondary (by comparing checksums). It starts from 0 and grows as the checksum operations advance. The value includes (i.e. counts multiple times) areas that will end up being transferred more than once (due to stopping and continuing the operation, or for some errors).
    checksumTotalBytes (`long`_, optional):

       The total number of bytes to be checksummed, only present for sync tasks. This is the total size of all disks.
    checksumComparedBytes (`long`_, optional):

       The total number of bytes that were checksummed, only present for sync tasks.
