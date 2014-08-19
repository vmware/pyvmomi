
vim.event.VmNoCompatibleHostForSecondaryEvent
=============================================
  This event records that no compatible host was found to place a secondary VM. A default alarm will be triggered upon this event, which by default would trigger a SNMP trap.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
