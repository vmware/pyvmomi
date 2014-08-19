
vim.event.GhostDvsProxySwitchRemovedEvent
=========================================
  This event records when the ghost DVS proxy switches (a.k.a host proxy switches that don't match any DVS defined in Virtual Center) were removed on the host.
:extends: vim.event.HostEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    switchUuid ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       The list of ghost DVS proxy switch uuid that were removed.
