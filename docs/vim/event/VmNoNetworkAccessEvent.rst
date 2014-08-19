
vim.event.VmNoNetworkAccessEvent
================================
  This event records a migration failure when the destination host is not on the same network as the source host.
:extends: vim.event.VmEvent_

Attributes:
    destHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The destination host.
