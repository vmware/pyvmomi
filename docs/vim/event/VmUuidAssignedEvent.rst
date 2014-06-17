.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmUuidAssignedEvent
=============================
  This event records the assignment of a new BIOS UUID to a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    uuid (`str`_):

       The new BIOS UUID.
