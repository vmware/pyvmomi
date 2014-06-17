.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.PermissionEvent: ../../vim/event/PermissionEvent.rst

.. _vim.event.RoleEventArgument: ../../vim/event/RoleEventArgument.rst


vim.event.PermissionAddedEvent
==============================
  This event records the creation of a permission.
:extends: vim.event.PermissionEvent_

Attributes:
    role (`vim.event.RoleEventArgument`_):

       The associated role.
    propagate (`bool`_):

       Whether or not the permission applies to sub-entities.
