.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.LocalFileSystemVolume.Specification
============================================
  The specification for creating a new local file system volume.
:extends: vmodl.DynamicData_

Attributes:
    device (`str`_):

       The device of the local file system.
    localPath (`str`_):

       The file path on the host where the file system is mounted.
