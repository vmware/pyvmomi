.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.AuthorizationEvent: ../../vim/event/AuthorizationEvent.rst

.. _vim.event.ManagedEntityEventArgument: ../../vim/event/ManagedEntityEventArgument.rst


vim.event.PermissionEvent
=========================
  This event records a permission operation.
:extends: vim.event.AuthorizationEvent_

Attributes:
    entity (`vim.event.ManagedEntityEventArgument`_):

       The entity to which the permission applied.
    principal (`str`_):

       The user name or group to which the permission was granted.
    group (`bool`_):

       Whether or not the principal was a group.
