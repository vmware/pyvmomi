
vim.host.FileSystemVolumeInfo
=============================
  The `HostFileSystemVolumeInfo <vim/host/FileSystemVolumeInfo.rst>`_ data object describes the file system volume information for the host.A file system volume refers to a storage abstraction that allows files to be created and organized. A host can have multiple file system volumes. File system volumes are typically mounted into a file namespace that allows all files in mounted file systems to be addressable from the host.A file system volume is backed by disk storage. It could span one or more disks but need not use an entire disk.A file system volume by definition must be mounted on the file system in order to exist.
:extends: vmodl.DynamicData_

Attributes:
    volumeTypeList ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The list of supported file system volume types.
    mountInfo ([`vim.host.FileSystemMountInfo <vim/host/FileSystemMountInfo.rst>`_], optional):

       The list of file system volumes mounted on the host.
