
vim.event.VmFailedRelayoutEvent
===============================
  This event records a specific failure to relay out a virtual machine, such as a failure to access the disk.
:extends: vim.event.VmEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

