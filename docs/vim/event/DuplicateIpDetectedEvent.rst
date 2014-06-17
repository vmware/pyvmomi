.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst


vim.event.DuplicateIpDetectedEvent
==================================
  This event records that a duplicate IP address has been observed in conflict with the vmotion or IP storage interface configured on the host.
:extends: vim.event.HostEvent_
:since: `VI API 2.5`_

Attributes:
    duplicateIP (`str`_):

       The Duplicate IP address detected.
    macAddress (`str`_):

       The MAC associated with duplicate IP.
