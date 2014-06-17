.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostDiskPartitionInfoType: ../../../vim/host/DiskPartitionInfo/Type.rst


vim.host.DiskPartitionInfo.Partition
====================================
  Information about a single disk partition. A partition is a contiguous set of blocks on a disk that is marked for use. The typeId identifies the purpose of the data in the partition.
:extends: vmodl.DynamicData_

Attributes:
    partition (`int`_):

       The partition number. Must be a positive integer.
    startSector (`long`_):

       The start sector.
    endSector (`long`_):

       The end sector.
    type (`str`_):

       Type of data in the partition. If it is a well-known partition type, it will be one of the defined types. If it is not, then it will be reported as a hexadecimal number. For example, "none", "vmfs", "linux", and "0x20" are all valid values.See `HostDiskPartitionInfoType`_ 
    guid (`str`_, optional):

       Globally Unique Identifier of the partition, as defined by the GUID Partition Table (GPT) format. This is available only for GPT formatted disks.
    logical (`bool`_):

       The flag to indicate whether or not the partition is logical. If true, the partition number should be greater than 4.
    attributes (`int`_):

       The attributes on the partition.
    partitionAlignment (`long`_, optional):

       Partition alignment in bytes. If unset, partition alignment value is unknown.
