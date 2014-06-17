.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst


vim.event.RollbackEvent
=======================
  This event is generated when network configuration rollback occurs on a host due configuration change that disconnected the host from vSphere server
:extends: vim.event.DvsEvent_
:since: `vSphere API 5.1`_

Attributes:
    hostName (`str`_):

       The host on which rollback happened
    methodName (`str`_, optional):

       The API method that was rolled back
