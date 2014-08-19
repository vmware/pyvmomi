
vim.event.VmFailedToSuspendEvent
================================
  This event records a failure to suspend a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The reason for the failure.
