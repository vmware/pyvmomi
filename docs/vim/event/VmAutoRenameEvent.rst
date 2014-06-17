.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst


vim.event.VmAutoRenameEvent
===========================
  This event records that a virtual machine was automatically renamed because of a name conflict.
:extends: vim.event.VmEvent_

Attributes:
    oldName (`str`_):

       The name of the virtual machine before renaming.
    newName (`str`_):

       The name of the virtual machine after renaming.
