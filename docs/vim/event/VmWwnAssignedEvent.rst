
vim.event.VmWwnAssignedEvent
============================
  This event records the assignment of a new WWN (World Wide Name) to a virtual machine.
:extends: vim.event.VmEvent_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    nodeWwns ([`long <https://docs.python.org/2/library/stdtypes.html>`_]):

       The new node WWN.
    portWwns ([`long <https://docs.python.org/2/library/stdtypes.html>`_]):

       The new port WWN.
