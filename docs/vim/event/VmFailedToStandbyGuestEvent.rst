.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.event.VmFailedToStandbyGuestEvent
=====================================
  This event records a failure to set the guest on a virtual machine to a standby state.
:extends: vim.event.VmEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault`_):

       The reason for the failure.
