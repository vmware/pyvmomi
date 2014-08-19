
vim.event.HostShortNameInconsistentEvent
========================================
  This event records that host name resolution returned different names on the host. Please check your host's network configuration and your DNS configuration. There may be duplicate entries.
:extends: vim.event.HostDasEvent_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_
**deprecated**


Attributes:
    shortName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

    shortName2 (`str <https://docs.python.org/2/library/stdtypes.html>`_):

