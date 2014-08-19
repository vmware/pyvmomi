
vim.host.ScsiDisk.Partition
===========================
  This data object type describes the specification of a Disk partition.
:extends: vmodl.DynamicData_

Attributes:
    diskName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The SCSI disk device on which a VMware File System (VMFS) extent resides.See `HostScsiDisk <vim/host/ScsiDisk.rst>`_ See `canonicalName <vim/host/ScsiLun.rst#canonicalName>`_ 
    partition (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The partition number of the partition on the ScsiDisk.
