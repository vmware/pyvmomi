
vim.VirtualMachine.StorageRequirement
=====================================
  Describes the storage requirment to perform a consolidation operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    datastore (`vim.Datastore <vim/Datastore.rst>`_):

       The datastore.
    freeSpaceRequiredInKb (`long <https://docs.python.org/2/library/stdtypes.html>`_):

       Space required.
