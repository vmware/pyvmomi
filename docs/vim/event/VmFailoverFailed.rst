
vim.event.VmFailoverFailed
==========================
  This event records when a virtual machine failover was unsuccessful.
:extends: vim.event.VmEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_, optional):

       The reason for the failure
