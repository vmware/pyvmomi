
vim.event.HostExtraNetworksEvent
================================
  This event records the fact that a host has extra networks not used by other hosts for HA communication
:extends: vim.event.HostDasEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_
**deprecated**


Attributes:
    ips (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The comma-separated list of extra networks
