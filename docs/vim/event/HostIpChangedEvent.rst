.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst


vim.event.HostIpChangedEvent
============================
  This event records a change in host IP address.
:extends: vim.event.HostEvent_
:since: `VI API 2.5`_

Attributes:
    oldIP (`str`_):

       Old IP address of the host.
    newIP (`str`_):

       New IP address of the host.
