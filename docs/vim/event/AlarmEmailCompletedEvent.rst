
vim.event.AlarmEmailCompletedEvent
==================================
  This event records the completion of an alarm email notification.
:extends: vim.event.AlarmEvent_

Attributes:
    entity (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity with which the alarm is registered.
    to (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The destination email address.
