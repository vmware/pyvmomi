.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vim.event.VmEventArgument: ../../vim/event/VmEventArgument.rst


vim.event.VmUuidConflictEvent
=============================
  This event records a conflict of virtual machine BIOS UUIDs.
:extends: vim.event.VmEvent_

Attributes:
    conflictedVm (`vim.event.VmEventArgument`_):

       The virtual machine whose UUID conflicts with the current virtual machine's UUID.
    uuid (`str`_):

       The BIOS UUID in conflict.
