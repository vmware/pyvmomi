
vim.fault.ImportOperationBulkFault.FaultOnImport
================================================
  The fault occurred on the entity during an import operation.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    entityType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The entity type on which import failed. See `EntityType <vim/dvs/EntityBackup/EntityType.rst>`_ for valid values
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The key on which import failed
    fault (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The fault that occurred.
