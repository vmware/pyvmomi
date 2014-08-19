
vim.event.AlarmActionTriggeredEvent
===================================
  This event records that an alarm was triggered.
:extends: vim.event.AlarmEvent_

Attributes:
    source (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity that triggered the alarm.
    entity (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity with which the alarm is registered.
