
vim.host.LocalFileSystemVolume.Specification
============================================
  The specification for creating a new local file system volume.
:extends: vmodl.DynamicData_

Attributes:
    device (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The device of the local file system.
    localPath (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The file path on the host where the file system is mounted.
