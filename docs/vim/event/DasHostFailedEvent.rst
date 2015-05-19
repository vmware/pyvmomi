.. _vim.event.ClusterEvent: ../../vim/event/ClusterEvent.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst


vim.event.DasHostFailedEvent
============================
  This event records when a host failure has been detected by HA.
:extends: vim.event.ClusterEvent_

Attributes:
    failedHost (`vim.event.HostEventArgument`_):

       The host that failed.
