
vim.event.DvsImportEvent
========================
  This event is generated when a import operation is performed on a distributed virtual switch
:extends: vim.event.DvsEvent_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    importType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The type of restore operation. See `EntityImportType <vim/dvs/EntityBackup/ImportType.rst>`_ for valid values
