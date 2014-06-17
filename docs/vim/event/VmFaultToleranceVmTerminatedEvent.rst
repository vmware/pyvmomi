.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmFaultToleranceVmTerminatedEvent
===========================================
  This event records a secondary or primary VM is terminated. The reason could be : divergence, lost connection to secondary, partial hardware failure of secondary, or by user.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0`_

Attributes:
    reason (`str`_, optional):

