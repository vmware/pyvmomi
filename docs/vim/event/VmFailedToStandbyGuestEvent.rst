
vim.event.VmFailedToStandbyGuestEvent
=====================================
  This event records a failure to set the guest on a virtual machine to a standby state.
:extends: vim.event.VmEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The reason for the failure.
