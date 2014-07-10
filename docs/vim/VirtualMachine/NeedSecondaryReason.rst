.. _vim.VirtualMachine: ../../vim/VirtualMachine.rst

.. _vim.VirtualMachine.NeedSecondaryReason: ../../vim/VirtualMachine/NeedSecondaryReason.rst

vim.VirtualMachine.NeedSecondaryReason
======================================
  The NeedSecondaryReason type defines all reasons a virtual machine is in the needSecondary Fault Tolerance state following a failure.
  :contained by: `vim.VirtualMachine`_

  :type: `vim.VirtualMachine.NeedSecondaryReason`_

  :name: other

values:
--------

userAction
   Terminated by user

lostConnection
   Lose connection to secondary

divergence
   Divergence

partialHardwareFailure
   Partial hardware failure

other
   All other reasons

initializing
   Initializing FT
