.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vim.event.VmEventArgument: ../../vim/event/VmEventArgument.rst


vim.event.VmStaticMacConflictEvent
==================================
  This event records a static MAC address conflict for a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    conflictedVm (`vim.event.VmEventArgument`_):

       The virtual machine whose static MAC address conflicts with the current virtual machine's address.
    mac (`str`_):

       The static MAC address that is in conflict.
