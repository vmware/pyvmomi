
vim.event.AlarmStatusChangedEvent
=================================
  This event records a status change for an alarm.
:extends: vim.event.AlarmEvent_

Attributes:
    source (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity for which the alarm status has been changed.
    entity (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity with which the alarm is registered.
    from (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The original alarm status.
    to (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The new alarm status.
