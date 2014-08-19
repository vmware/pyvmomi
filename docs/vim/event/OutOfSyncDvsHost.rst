
vim.event.OutOfSyncDvsHost
==========================
  The list of hosts that have the DVS configuration on the host diverged from that of the Virtual Center Server.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    hostOutOfSync ([`vim.event.DvsOutOfSyncHostArgument <vim/event/DvsOutOfSyncHostArgument.rst>`_]):

       The host that went out of sync.
