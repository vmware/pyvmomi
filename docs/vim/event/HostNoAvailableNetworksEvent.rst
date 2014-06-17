.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.HostDasEvent: ../../vim/event/HostDasEvent.rst


vim.event.HostNoAvailableNetworksEvent
======================================
  This event records the fact that a host does not have any available networks for HA communication
:extends: vim.event.HostDasEvent_
:since: `vSphere API 4.0`_

Attributes:
    ips (`str`_, optional):

       The comma-separated list of used networks
