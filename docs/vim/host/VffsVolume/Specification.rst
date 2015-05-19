.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _devicePath: ../../../vim/host/ScsiDisk.rst#devicePath

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.DiskPartitionInfo.Specification: ../../../vim/host/DiskPartitionInfo/Specification.rst


vim.host.VffsVolume.Specification
=================================
  This data object type describes the VFFS creation specification.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.5`_

Attributes:
    devicePath (`str`_):

       The device path of the SSD disk.See `devicePath`_ 
    partition (`vim.host.DiskPartitionInfo.Specification`_, optional):

       Partition specification of the SSD disk. If this property is not provided, partition information will be computed and generated.
    majorVersion (`int`_):

       Major version number of VFFS. This can be changed if the VFFS is upgraded, but this is an irreversible change.
    volumeName (`str`_):

       Volume name of VFFS.
