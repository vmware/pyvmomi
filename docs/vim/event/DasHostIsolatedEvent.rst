.. _vim.event.ClusterEvent: ../../vim/event/ClusterEvent.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst


vim.event.DasHostIsolatedEvent
==============================
  This event records that a host has been isolated from the network in a HA cluster. Since an isolated host cannot be distinguished from a failed host except by the isolated host itself, this event is logged when the isolated host regains network connectivity.
:extends: vim.event.ClusterEvent_

Attributes:
    isolatedHost (`vim.event.HostEventArgument`_):

       The host that was isolated.
