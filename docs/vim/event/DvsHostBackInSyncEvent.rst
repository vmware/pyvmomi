
vim.event.DvsHostBackInSyncEvent
================================
  The DVS configuration on the host was synchronized with that of the Virtual Center Server and the configuration is the same on the host and Virtual Center Server.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    hostBackInSync (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The host that was synchronized.
