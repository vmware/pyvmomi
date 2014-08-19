
vim.StoragePod.Summary
======================
  The `StoragePodSummary <vim/StoragePod/Summary.rst>`_ data object encapsulates runtime properties of a `StoragePod <vim/StoragePod.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the storage pod.
    capacity (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Total capacity of this storage pod, in bytes. This value is the sum of the capacity of all datastores that are part of this storage pod, and is updated periodically by the server.
    freeSpace (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Total free space on this storage pod, in bytes. This value is the sum of the free space on all datastores that are part of this storage pod, and is updated periodically by the server.
