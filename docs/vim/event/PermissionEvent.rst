
vim.event.PermissionEvent
=========================
  This event records a permission operation.
:extends: vim.event.AuthorizationEvent_

Attributes:
    entity (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity to which the permission applied.
    principal (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The user name or group to which the permission was granted.
    group (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether or not the principal was a group.
