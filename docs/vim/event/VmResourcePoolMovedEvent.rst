.. _vim.event.VmEvent: ../../vim/event/VmEvent.rst

.. _vim.event.ResourcePoolEventArgument: ../../vim/event/ResourcePoolEventArgument.rst


vim.event.VmResourcePoolMovedEvent
==================================
  This event records when a virtual machine is moved from one resource pool to another.
:extends: vim.event.VmEvent_

Attributes:
    oldParent (`vim.event.ResourcePoolEventArgument`_):

       The old parent resourcePool of the moved virtual machine.
    newParent (`vim.event.ResourcePoolEventArgument`_):

       The new parent resourcePool of the moved virtual machine.
