
vim.event.VmUuidConflictEvent
=============================
  This event records a conflict of virtual machine BIOS UUIDs.
:extends: vim.event.VmEvent_

Attributes:
    conflictedVm (`vim.event.VmEventArgument <vim/event/VmEventArgument.rst>`_):

       The virtual machine whose UUID conflicts with the current virtual machine's UUID.
    uuid (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The BIOS UUID in conflict.
