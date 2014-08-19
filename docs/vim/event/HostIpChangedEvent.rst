
vim.event.HostIpChangedEvent
============================
  This event records a change in host IP address.
:extends: vim.event.HostEvent_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    oldIP (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Old IP address of the host.
    newIP (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       New IP address of the host.
