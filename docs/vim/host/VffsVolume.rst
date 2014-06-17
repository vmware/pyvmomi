.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../vim/version.rst#vimversionversion9

.. _vim.host.FileSystemVolume: ../../vim/host/FileSystemVolume.rst

.. _vim.host.ScsiDisk.Partition: ../../vim/host/ScsiDisk/Partition.rst


vim.host.VffsVolume
===================
  vFlash File System Volume.
:extends: vim.host.FileSystemVolume_
:since: `vSphere API 5.5`_

Attributes:
    majorVersion (`int`_):

       Major version number of VFFS.
    version (`str`_):

       Version string. Contains major and minor version numbers.
    uuid (`str`_):

       The universally unique identifier assigned to VFFS.
    extent (`vim.host.ScsiDisk.Partition`_):

       The list of partition names that comprise this disk's VFFS extents.
