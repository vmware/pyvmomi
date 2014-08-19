
vim.vm.StorageInfo
==================
  Information about the amount of storage used by a virtual machine across datastores that it is located on.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    perDatastoreUsage ([`vim.vm.StorageInfo.UsageOnDatastore <vim/vm/StorageInfo/UsageOnDatastore.rst>`_], optional):

       Storage space used by this virtual machine on all datastores that it is located on.Total storage space committed to this virtual machine across all datastores is simply an aggregate of the property `committed <vim/vm/StorageInfo/UsageOnDatastore.rst#committed>`_ .See `committed <vim/vm/Summary/StorageSummary.rst#committed>`_ 
    timestamp (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       Time when values in this structure were last updated.
