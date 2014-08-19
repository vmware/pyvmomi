
vim.event.DasHostFailedEvent
============================
  This event records when a host failure has been detected by HA.
:extends: vim.event.ClusterEvent_

Attributes:
    failedHost (`vim.event.HostEventArgument <vim/event/HostEventArgument.rst>`_):

       The host that failed.
