.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vmodl.LocalizedMethodFault: ../../vmodl/LocalizedMethodFault.rst


vim.event.VmSecondaryDisabledBySystemEvent
==========================================
  This event records that a fault tolerance secondary VM has been disabled by vCenter because the VM could not be powered on.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0`_

Attributes:
    reason (`vmodl.LocalizedMethodFault`_, optional):

