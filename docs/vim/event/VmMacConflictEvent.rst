
vim.event.VmMacConflictEvent
============================
  This event records a MAC address conflict for a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    conflictedVm (`vim.event.VmEventArgument <vim/event/VmEventArgument.rst>`_):

       The virtual machine whose MAC address conflicts with the current virtual machine's address.
    mac (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The MAC address that is in conflict.
