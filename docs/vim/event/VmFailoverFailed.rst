.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.event.VmFailoverFailed
==========================
  This event records when a virtual machine failover was unsuccessful.
:extends: vim.event.VmEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault`_, optional):

       The reason for the failure
