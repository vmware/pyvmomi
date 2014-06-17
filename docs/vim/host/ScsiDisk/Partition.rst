.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _HostScsiDisk: ../../../vim/host/ScsiDisk.rst

.. _canonicalName: ../../../vim/host/ScsiLun.rst#canonicalName

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.ScsiDisk.Partition
===========================
  This data object type describes the specification of a Disk partition.
:extends: vmodl.DynamicData_

Attributes:
    diskName (`str`_):

       The SCSI disk device on which a VMware File System (VMFS) extent resides.See `HostScsiDisk`_ See `canonicalName`_ 
    partition (`int`_):

       The partition number of the partition on the ScsiDisk.
