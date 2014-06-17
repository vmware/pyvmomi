.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmMacChangedEvent
===========================
  This event records a change in a virtual machine's MAC address.
:extends: vim.event.VmEvent_

Attributes:
    adapter (`str`_):

       The name of the virtual network adapter.
    oldMac (`str`_):

       The old MAC address.
    newMac (`str`_):

       The new MAC address.
