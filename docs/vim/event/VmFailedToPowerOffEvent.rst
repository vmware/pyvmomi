
vim.event.VmFailedToPowerOffEvent
=================================
  This event records a failure to power off a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The reason for the failure.
