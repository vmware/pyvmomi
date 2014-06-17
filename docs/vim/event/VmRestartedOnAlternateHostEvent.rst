.. _vim.event.VmPoweredOnEvent: ../../vim/event/VmPoweredOnEvent.rst

.. _vim.event.HostEventArgument: ../../vim/event/HostEventArgument.rst


vim.event.VmRestartedOnAlternateHostEvent
=========================================
  This event records that the virtual machine was restarted on a host, since its original host had failed.
:extends: vim.event.VmPoweredOnEvent_
**deprecated**


Attributes:
    sourceHost (`vim.event.HostEventArgument`_):

       The host that failed.
