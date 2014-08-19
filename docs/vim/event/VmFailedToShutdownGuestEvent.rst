
vim.event.VmFailedToShutdownGuestEvent
======================================
  This event records a failure to shut down the guest on a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The reason for the failure.
