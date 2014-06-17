.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmRequirementsExceedCurrentEVCModeEvent
=================================================
  The virtual machine is using features that exceed what the host is capable of providing. This may occur when joining an EVC cluster while the virtual machine is powered on. The most common resolution is to power cycle the virtual machine.
:extends: vim.event.VmEvent_
:since: `vSphere API 5.1`_

Attributes:
