.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _EntityImportType: ../../vim/dvs/EntityBackup/ImportType.rst

.. _vim.event.DVPortgroupEvent: ../../vim/event/DVPortgroupEvent.rst


vim.event.DvpgImportEvent
=========================
  This event is generated when an import operation is performed on a distributed virtual portgroup
:extends: vim.event.DVPortgroupEvent_
:since: `vSphere API 5.1`_

Attributes:
    importType (`str`_):

       The type of restore operation. See `EntityImportType`_ for valid values
