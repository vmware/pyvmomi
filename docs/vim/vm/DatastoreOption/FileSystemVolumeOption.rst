.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostFileSystemVolumeInfo: ../../../vim/host/FileSystemVolumeInfo.rst


vim.vm.DatastoreOption.FileSystemVolumeOption
=============================================
  This data object type describes a file system volume option for this virtual machine.
:extends: vmodl.DynamicData_

Attributes:
    fileSystemType (`str`_):

       The type name of the file system volume information object for this option.See `HostFileSystemVolumeInfo`_ 
    majorVersion (`int`_, optional):

       The major version of the file system volume information for this option. If not specified, all versions of this file system are included in this option. Currently, this value is set only for VMFS volumes.
