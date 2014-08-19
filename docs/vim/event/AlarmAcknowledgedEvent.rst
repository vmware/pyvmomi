
vim.event.AlarmAcknowledgedEvent
================================
  This event records the acknowledgement of an Alarm
:extends: vim.event.AlarmEvent_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    source (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity that triggered the alarm.
    entity (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity with which the alarm is registered.
