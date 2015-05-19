.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _DatastoreInfo: ../../vim/Datastore/Info.rst

.. _HostNasVolume: ../../vim/host/NasVolume.rst

.. _HostVffsVolume: ../../vim/host/VffsVolume.rst

.. _HostVmfsVolume: ../../vim/host/VmfsVolume.rst

.. _HostVfatVolume: ../../vim/host/VfatVolume.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _HostLocalFileSystemVolume: ../../vim/host/LocalFileSystemVolume.rst


vim.host.FileSystemVolume
=========================
  Detailed information about a file system. This is a base type for derived types that have more specific details about specific filesystem types.Typically a FileSystem is exposed as a datatoreSee `DatastoreInfo`_ See `HostVmfsVolume`_ See `HostNasVolume`_ See `HostVffsVolume`_ See `HostLocalFileSystemVolume`_ See `HostVfatVolume`_ 
:extends: vmodl.DynamicData_

Attributes:
    type (`str`_):

       Type of file system volume.The following values are defined:VMFSVMware File System (ESX Server only). If this is set, the type of the file system volume is VMFS.NFSNetwork file system v3 and below (Linux and ESX Server only). If this is set, the type of the file system volume is NetworkFileSystem.NFSV41Network file system version v4.1 or later (Linux only and ESX Server only). If this is set, the type of the file system volume is NetworkFileSystem41.CIFSCommon Internet file system (Windows only). If this is set, the type of the file system volume is CIFS.VFATVirtual FAT (ESX Server only). If this is set, the type of the file system volume is VFAT.vsanVSAN (ESX Server only). If this is set, the type of the file system volume is VSAN.VFFSvFlash File System (ESX Server only). If this is set, the type of the file system volume is VFFS.
    name (`str`_):

       Name of the file system volume.
    capacity (`long`_):

       The capacity of the file system volume, in bytes.
