
vim.event.VmTimedoutStartingSecondaryEvent
==========================================
  This event records timeout when starting a secondary VM. A default alarm will be triggered upon this event, which by default would trigger a SNMP trap.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    timeout (`long <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The duration of the timeout in milliseconds.
