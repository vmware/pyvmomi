
vim.host.VffsVolume
===================
  vFlash File System Volume.
:extends: vim.host.FileSystemVolume_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    majorVersion (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Major version number of VFFS.
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Version string. Contains major and minor version numbers.
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The universally unique identifier assigned to VFFS.
    extent ([`vim.host.ScsiDisk.Partition <vim/host/ScsiDisk/Partition.rst>`_]):

       The list of partition names that comprise this disk's VFFS extents.
