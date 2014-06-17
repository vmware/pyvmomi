.. _str: https://docs.python.org/2/library/stdtypes.html

.. _long: https://docs.python.org/2/library/stdtypes.html

.. _StoragePod: ../../vim/StoragePod.rst

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _StoragePodSummary: ../../vim/StoragePod/Summary.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.StoragePod.Summary
======================
  The `StoragePodSummary`_ data object encapsulates runtime properties of a `StoragePod`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    name (`str`_):

       The name of the storage pod.
    capacity (`long`_):

       Total capacity of this storage pod, in bytes. This value is the sum of the capacity of all datastores that are part of this storage pod, and is updated periodically by the server.
    freeSpace (`long`_):

       Total free space on this storage pod, in bytes. This value is the sum of the free space on all datastores that are part of this storage pod, and is updated periodically by the server.
