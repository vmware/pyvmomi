.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmRenamedEvent
========================
  This event records the renaming of a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    oldName (`str`_):

       The old name of the virtual machine.
    newName (`str`_):

       The new name of the virtual machine.
