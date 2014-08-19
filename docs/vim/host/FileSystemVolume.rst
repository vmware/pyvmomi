
vim.host.FileSystemVolume
=========================
  Detailed information about a file system. This is a base type for derived types that have more specific details about specific filesystem types.Typically a FileSystem is exposed as a datatoreSee `DatastoreInfo <vim/Datastore/Info.rst>`_ See `HostVmfsVolume <vim/host/VmfsVolume.rst>`_ See `HostNasVolume <vim/host/NasVolume.rst>`_ See `HostVffsVolume <vim/host/VffsVolume.rst>`_ See `HostLocalFileSystemVolume <vim/host/LocalFileSystemVolume.rst>`_ See `HostVfatVolume <vim/host/VfatVolume.rst>`_ 
:extends: vmodl.DynamicData_

Attributes:
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Type of file system volume.The following values are defined:VMFSVMware File System (ESX Server only). If this is set, the type of the file system volume is VMFS.NFSNetwork file system v3 and below (Linux and ESX Server only). If this is set, the type of the file system volume is NetworkFileSystem.NFSV41Network file system version v4.1 or later (Linux only and ESX Server only). If this is set, the type of the file system volume is NetworkFileSystem41.CIFSCommon Internet file system (Windows only). If this is set, the type of the file system volume is CIFS.VFATVirtual FAT (ESX Server only). If this is set, the type of the file system volume is VFAT.vsanVSAN (ESX Server only). If this is set, the type of the file system volume is VSAN.VFFSvFlash File System (ESX Server only). If this is set, the type of the file system volume is VFFS.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the file system volume.
    capacity (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       The capacity of the file system volume, in bytes.
