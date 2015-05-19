.. _str: https://docs.python.org/2/library/stdtypes.html

.. _info: ../../vim/HttpNfcLease.rst#info

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.HttpNfcLease.ManifestEntry
==============================
  Provides a manifest for downloaded (exported) files and disks.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    key (`str`_):

       Key used to match this entry with the corresponding DeviceUrl entry in `info`_ .
    sha1 (`str`_):

       SHA-1 checksum of the data stream sent from the server. This can be used to verify that the bytes received by the client match those sent by the HttpNfc server.
    size (`long`_):

       Size of the downloaded file.
    disk (`bool`_):

       True if the downloaded file is a virtual disk backing.
    capacity (`long`_, optional):

       The capacity of the disk, if the file is a virtual disk backing.
    populatedSize (`long`_, optional):

       The populated size of the disk, if the file is a virtual disk backing.
