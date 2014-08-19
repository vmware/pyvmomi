
vim.event.DrsResourceConfigureFailedEvent
=========================================
  This event records when resource configuration specification synchronization fails on a host.
:extends: vim.event.HostEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The reason for the failure.
