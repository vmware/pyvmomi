.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vim.event.HostEvent: ../../vim/event/HostEvent.rst

.. _vim.event.VnicPortArgument: ../../vim/event/VnicPortArgument.rst


vim.event.HostVnicConnectedToCustomizedDVPortEvent
==================================================
  This event records when some host Virtual NICs were reconfigured to use DVPorts with port level configuration, which might be different from the DVportgroup.
:extends: vim.event.HostEvent_
:since: `vSphere API 4.0`_

Attributes:
    vnic (`vim.event.VnicPortArgument`_):

       Information about the Virtual NIC that is using the DVport.
