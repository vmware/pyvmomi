.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmDasUpdateErrorEvent
===============================
  The event records that an error occurred when updating the HA agents with the current state of the virtual machine. If this occurs during a powerOn operation, the virtual machine will not be failed over in the event of a host failure. If it occurs during a powerOff, the virtual machine will be automatically powered on if the host it was last running on crashes.
:extends: vim.event.VmEvent_

Attributes:
