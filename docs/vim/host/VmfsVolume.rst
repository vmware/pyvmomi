
vim.host.VmfsVolume
===================
  The VMFS file system.
:extends: vim.host.FileSystemVolume_

Attributes:
    blockSizeMb (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Block size of VMFS. Determines maximum file size. The maximum number of blocks is typically fixed with each specific version of VMFS. To increase the maximum size of a VMFS file, increase the block size.The minimum block size is 1MB.
    maxBlocks (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Maximum number of blocks. Determines maximum file size along with blockSize. See information about the blockSize.
    majorVersion (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Major version number of VMFS.
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Version string. Contains major and minor version numbers.
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The universally unique identifier assigned to VMFS.
    extent ([`vim.host.ScsiDisk.Partition <vim/host/ScsiDisk/Partition.rst>`_]):

       The list of partition names that comprise this disk's VMFS extents.This property can be accessed via various enclosing objects. In VirtualCenter, where it can be accessed from multiple hosts, the value of this property may differ according to the context in which it is accessed. When accessed from the `VmfsDatastoreInfo <vim/host/VmfsDatastoreInfo.rst>`_ object, in VirtualCenter, this property reflects the extent information of any one of the hosts visible to the datastore.For a VirtualCenter system which manages ESX Server 2.x and ESX Server 3.x hosts, this extent information is only correlatable across hosts if the extents are exposed on the same adapter on all hosts which can access them. To find the extent names for a specific host, this same property should be accessed via the host's `HostFileSystemVolume <vim/host/FileSystemVolume.rst>`_ object, by correlating the uuid of the VMFS datastore in the VmfsDatastoreInfo object to the uuid in the FileSystemVolume object.For a Virtual Center system which manages only ESX Server hosts with versions 4.0 onwards , this extent information is correlatable across hosts, irrespective of the adapters the extents are exposed on.
    vmfsUpgradable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Can the filesystem be upgraded to a newer version.See `UpgradeVmfs <vim/host/StorageSystem.rst#upgradeVmfs>`_ 
    forceMountedInfo (`vim.host.ForceMountedInfo <vim/host/ForceMountedInfo.rst>`_, optional):

       Information about 'forceMounted' VmfsVolume. When the system detects a copy of a VmfsVolume, it will not be auto-mounted on the host and it will be detected as 'UnresolvedVmfsVolume'. If user decides to 'forceMount' the VmfsVolume on the host, forceMountedInfo will be populated. It will not be set for automounted VMFS volumes.
    ssd (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether the volume is SSD backed. If unset, the information whether the volume is SSD backed is unknown.
    local (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether the volume is backed by local disk. If unset, the information of the volume is local-disk backed is unknown.
