
vim.event.PermissionAddedEvent
==============================
  This event records the creation of a permission.
:extends: vim.event.PermissionEvent_

Attributes:
    role (`vim.event.RoleEventArgument <vim/event/RoleEventArgument.rst>`_):

       The associated role.
    propagate (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether or not the permission applies to sub-entities.
