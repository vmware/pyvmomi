
vim.event.DuplicateIpDetectedEvent
==================================
  This event records that a duplicate IP address has been observed in conflict with the vmotion or IP storage interface configured on the host.
:extends: vim.event.HostEvent_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    duplicateIP (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The Duplicate IP address detected.
    macAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The MAC associated with duplicate IP.
