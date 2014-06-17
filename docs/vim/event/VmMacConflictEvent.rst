.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vim.event.VmEventArgument: ../../vim/event/VmEventArgument.rst


vim.event.VmMacConflictEvent
============================
  This event records a MAC address conflict for a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    conflictedVm (`vim.event.VmEventArgument`_):

       The virtual machine whose MAC address conflicts with the current virtual machine's address.
    mac (`str`_):

       The MAC address that is in conflict.
