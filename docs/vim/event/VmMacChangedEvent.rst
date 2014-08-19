
vim.event.VmMacChangedEvent
===========================
  This event records a change in a virtual machine's MAC address.
:extends: vim.event.VmEvent_

Attributes:
    adapter (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the virtual network adapter.
    oldMac (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The old MAC address.
    newMac (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The new MAC address.
