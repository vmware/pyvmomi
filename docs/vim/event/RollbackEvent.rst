
vim.event.RollbackEvent
=======================
  This event is generated when network configuration rollback occurs on a host due configuration change that disconnected the host from vSphere server
:extends: vim.event.DvsEvent_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    hostName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The host on which rollback happened
    methodName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The API method that was rolled back
