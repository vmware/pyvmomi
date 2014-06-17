.. _long: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmWwnAssignedEvent
============================
  This event records the assignment of a new WWN (World Wide Name) to a virtual machine.
:extends: vim.event.VmEvent_
:since: `VI API 2.5`_

Attributes:
    nodeWwns (`long`_):

       The new node WWN.
    portWwns (`long`_):

       The new port WWN.
