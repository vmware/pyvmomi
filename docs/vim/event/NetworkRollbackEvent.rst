.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.Event: ../../vim/event/Event.rst

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8


vim.event.NetworkRollbackEvent
==============================
  This event records when networking configuration on the host is rolled back as it disconnects the host from vCenter server.
:extends: vim.event.Event_
:since: `vSphere API 5.1`_

Attributes:
    methodName (`str`_):

       Method name which caused the disconnect
    transactionId (`str`_):

       Transaction ID for the method call that caused the disconnect
