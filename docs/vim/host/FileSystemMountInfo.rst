
vim.host.FileSystemMountInfo
============================
  The `HostFileSystemMountInfo <vim/host/FileSystemMountInfo.rst>`_ data object describes a host mount point for a file system.
:extends: vmodl.DynamicData_

Attributes:
    mountInfo (`vim.host.MountInfo <vim/host/MountInfo.rst>`_):

       Information about the mount point.
    volume (`vim.host.FileSystemVolume <vim/host/FileSystemVolume.rst>`_):

       Information about the mounted volume.
    vStorageSupport (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       vStorage hardware acceleration support status. This property represents the volume's capability for storage acceleration. See `FileSystemMountInfoVStorageSupportStatus <vim/host/FileSystemMountInfo/VStorageSupportStatus.rst>`_ for valid values.If the ESX Server supports hardware acceleration, the Server can offload specific virtual machine management operations to a storage device with the hardware acceleration feature. With hardware assistance, the host performs storage operations faster and consumes less CPU, memory, and storage fabric bandwidth.For vSphere 4.0 or earlier hosts, this value will be unset.
