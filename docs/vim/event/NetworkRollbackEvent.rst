
vim.event.NetworkRollbackEvent
==============================
  This event records when networking configuration on the host is rolled back as it disconnects the host from vCenter server.
:extends: vim.event.Event_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    methodName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Method name which caused the disconnect
    transactionId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Transaction ID for the method call that caused the disconnect
