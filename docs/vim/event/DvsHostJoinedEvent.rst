
vim.event.DvsHostJoinedEvent
============================
  A host joined the distributed virtual switch.
:extends: vim.event.DvsEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    hostJoined (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The host that joined DVS.
