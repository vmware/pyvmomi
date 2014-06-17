.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst


vim.event.VmNoNetworkAccessEvent
================================
  This event records a migration failure when the destination host is not on the same network as the source host.
:extends: vim.event.VmEvent_

Attributes:
    destHost (`vim.event.HostEventArgument`_):

       The destination host.
