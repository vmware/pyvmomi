
vim.event.DvpgImportEvent
=========================
  This event is generated when an import operation is performed on a distributed virtual portgroup
:extends: vim.event.DVPortgroupEvent_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    importType (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The type of restore operation. See `EntityImportType <vim/dvs/EntityBackup/ImportType.rst>`_ for valid values
