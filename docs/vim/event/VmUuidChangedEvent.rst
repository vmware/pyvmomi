
vim.event.VmUuidChangedEvent
============================
  This event records a change in a virtual machine's BIOS UUID.
:extends: vim.event.VmEvent_

Attributes:
    oldUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The old BIOS UUID.
    newUuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The new BIOS UUID.
