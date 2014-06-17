.. _vim.event.ResourcePoolEvent: ../../vim/event/ResourcePoolEvent.rst

.. _vim.event.ResourcePoolEventArgument: ../../vim/event/ResourcePoolEventArgument.rst


vim.event.ResourcePoolMovedEvent
================================
  This event records when a resource pool is moved.
:extends: vim.event.ResourcePoolEvent_

Attributes:
    oldParent (`vim.event.ResourcePoolEventArgument`_):

       The old parent of the resource Pool.
    newParent (`vim.event.ResourcePoolEventArgument`_):

       The new parent of the resource Pool.
