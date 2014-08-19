
vim.event.VmResourcePoolMovedEvent
==================================
  This event records when a virtual machine is moved from one resource pool to another.
:extends: vim.event.VmEvent_

Attributes:
    oldParent (`vim.event.ResourcePoolEventArgument <vim/event/ResourcePoolEventArgument.rst>`_):

       The old parent resourcePool of the moved virtual machine.
    newParent (`vim.event.ResourcePoolEventArgument <vim/event/ResourcePoolEventArgument.rst>`_):

       The new parent resourcePool of the moved virtual machine.
