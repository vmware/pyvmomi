
vim.event.VmSecondaryDisabledBySystemEvent
==========================================
  This event records that a fault tolerance secondary VM has been disabled by vCenter because the VM could not be powered on.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_, optional):

