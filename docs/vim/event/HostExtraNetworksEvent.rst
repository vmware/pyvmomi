.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.HostDasEvent: ../../vim/event/HostDasEvent.rst


vim.event.HostExtraNetworksEvent
================================
  This event records the fact that a host has extra networks not used by other hosts for HA communication
:extends: vim.event.HostDasEvent_
:since: `vSphere API 4.0`_
**deprecated**


Attributes:
    ips (`str`_, optional):

       The comma-separated list of extra networks
