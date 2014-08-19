
vim.event.AlarmScriptCompleteEvent
==================================
  This event records the completion of an alarm-triggered script.
:extends: vim.event.AlarmEvent_

Attributes:
    entity (`vim.event.ManagedEntityEventArgument <vim/event/ManagedEntityEventArgument.rst>`_):

       The entity with which the alarm is registered.
    script (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The script triggered by the alarm.
