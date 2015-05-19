.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.host.FileSystemVolume: ../../vim/host/FileSystemVolume.rst


vim.host.NasVolume
==================
  This data object type describes the NAS volume. Applies to both NFS and CIFS.
:extends: vim.host.FileSystemVolume_

Attributes:
    remoteHost (`str`_):

       The host that runs the NFS/CIFS server. Clients must plan to use remoteHostNames for both NFS v3 as well as NFS v4.1 because this field remoteHost may be deprecated in future.
    remotePath (`str`_):

       The remote path of NFS/CIFS mount point.
    userName (`str`_, optional):

       In case of CIFS, the user name used while connecting to the server.
