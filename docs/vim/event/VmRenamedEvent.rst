
vim.event.VmRenamedEvent
========================
  This event records the renaming of a virtual machine.
:extends: vim.event.VmEvent_

Attributes:
    oldName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The old name of the virtual machine.
    newName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The new name of the virtual machine.
