.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmMacAssignedEvent
============================
  This event records the assignment of a new MAC address to a virtual network adapter.
:extends: vim.event.VmEvent_

Attributes:
    adapter (`str`_):

       The name of the virtual adapter.
    mac (`str`_):

       The new MAC address.
