.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.HostDasEvent: ../../vim/event/HostDasEvent.rst


vim.event.HostIsolationIpPingFailedEvent
========================================
  This event records that the isolation address could not be pinged. The default isolation address is the service console's default gateway.
:extends: vim.event.HostDasEvent_
:since: `VI API 2.5`_

Attributes:
    isolationIp (`str`_):

