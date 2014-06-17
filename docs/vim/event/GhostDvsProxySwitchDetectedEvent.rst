.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst


vim.event.GhostDvsProxySwitchDetectedEvent
==========================================
  This event records when Virtual Center server found DVS proxy switches on the host that don't match any DVS defined in Virtual Center.
:extends: vim.event.HostEvent_
:since: `vSphere API 4.0`_

Attributes:
    switchUuid (`str`_):

       The list of ghost DVS proxy switch uuids that were found.
