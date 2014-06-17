.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.event.VmFailedToPowerOffEvent
=================================
  This event records a failure to power off a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault`_):

       The reason for the failure.
