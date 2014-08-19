
vim.event.VmMacAssignedEvent
============================
  This event records the assignment of a new MAC address to a virtual network adapter.
:extends: vim.event.VmEvent_

Attributes:
    adapter (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the virtual adapter.
    mac (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The new MAC address.
