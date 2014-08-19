
vim.vm.Summary.StorageSummary
=============================
  A subset of the storage information of this virtual machine.See `VirtualMachineStorageInfo <vim/vm/StorageInfo.rst>`_ for a detailed storage break-up.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    committed (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Total storage space, in bytes, committed to this virtual machine across all datastores.Essentially an aggregate of the property `committed <vim/vm/StorageInfo/UsageOnDatastore.rst#committed>`_ across all datastores that this virtual machine is located on.
    uncommitted (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Additional storage space, in bytes, potentially used by this virtual machine on all datastores.Essentially an aggregate of the property `uncommitted <vim/vm/StorageInfo/UsageOnDatastore.rst#uncommitted>`_ across all datastores that this virtual machine is located on.
    unshared (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Total storage space, in bytes, occupied by the virtual machine across all datastores, that is not shared with any other virtual machine.
    timestamp (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       Time when values in this structure were last updated.
