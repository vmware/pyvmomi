.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst


vim.event.HostCnxFailedAlreadyManagedEvent
==========================================
  This event records a failure to connect to a host due to the host being managed by a different VirtualCenter server.
:extends: vim.event.HostEvent_

Attributes:
    serverName (`str`_):

       The name of the VirtualCenter server that manages the host.
