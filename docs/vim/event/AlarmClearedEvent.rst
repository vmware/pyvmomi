
vim.event.AlarmClearedEvent
===========================
  This event records the manual clearing of an Alarm
:extends: vim.event.AlarmEvent_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    source (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity that triggered the alarm.
    entity (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity with which the alarm is registered.
    from (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The original alarm status from which it was cleared
