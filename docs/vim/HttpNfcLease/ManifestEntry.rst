
vim.HttpNfcLease.ManifestEntry
==============================
  Provides a manifest for downloaded (exported) files and disks.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Key used to match this entry with the corresponding DeviceUrl entry in `info <vim/HttpNfcLease.rst#info>`_ .
    sha1 (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       SHA-1 checksum of the data stream sent from the server. This can be used to verify that the bytes received by the client match those sent by the HttpNfc server.
    size (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Size of the downloaded file.
    disk (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if the downloaded file is a virtual disk backing.
    capacity (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The capacity of the disk, if the file is a virtual disk backing.
    populatedSize (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The populated size of the disk, if the file is a virtual disk backing.
