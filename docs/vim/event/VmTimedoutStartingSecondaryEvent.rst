.. _long: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmTimedoutStartingSecondaryEvent
==========================================
  This event records timeout when starting a secondary VM. A default alarm will be triggered upon this event, which by default would trigger a SNMP trap.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0`_

Attributes:
    timeout (`long`_, optional):

       The duration of the timeout in milliseconds.
