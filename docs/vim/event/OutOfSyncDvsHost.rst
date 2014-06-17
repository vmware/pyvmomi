.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.DvsEvent: ../../vim/event/DvsEvent.rst

.. _vim.event.DvsOutOfSyncHostArgument: ../../vim/event/DvsOutOfSyncHostArgument.rst


vim.event.OutOfSyncDvsHost
==========================
  The list of hosts that have the DVS configuration on the host diverged from that of the Virtual Center Server.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0`_

Attributes:
    hostOutOfSync (`vim.event.DvsOutOfSyncHostArgument`_):

       The host that went out of sync.
