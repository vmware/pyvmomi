.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.event.VmFailedToShutdownGuestEvent
======================================
  This event records a failure to shut down the guest on a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault`_):

       The reason for the failure.
