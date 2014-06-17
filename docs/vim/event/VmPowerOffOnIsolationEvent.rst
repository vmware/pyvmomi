.. _vim.event.VmPoweredOffEvent: ../../vim/event/VmPoweredOffEvent.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst


vim.event.VmPowerOffOnIsolationEvent
====================================
  This event records when a virtual machine has been powered off on an isolated host in a HA cluster.
:extends: vim.event.VmPoweredOffEvent_

Attributes:
    isolatedHost (`vim.event.HostEventArgument`_):

       The isolated host on which a virtual machine is powered off.
