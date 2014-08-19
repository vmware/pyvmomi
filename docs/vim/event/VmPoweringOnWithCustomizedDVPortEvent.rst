
vim.event.VmPoweringOnWithCustomizedDVPortEvent
===============================================
  This event records when a virtual machine was powering on using DVPorts with port level configuration, which might be different from the DVportgroup.
:extends: vim.event.VmEvent_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    vnic ([`vim.event.VnicPortArgument <vim/event/VnicPortArgument.rst>`_]):

       The list of Virtual NIC that were using the DVports.
