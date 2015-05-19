.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmUuidChangedEvent
============================
  This event records a change in a virtual machine's BIOS UUID.
:extends: vim.event.VmEvent_

Attributes:
    oldUuid (`str`_):

       The old BIOS UUID.
    newUuid (`str`_):

       The new BIOS UUID.
