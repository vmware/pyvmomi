.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.AlarmEvent: ../../vim/event/AlarmEvent.rst

.. _vim.event.ManagedEntityEventArgument: ../../vim/event/ManagedEntityEventArgument.rst


vim.event.AlarmScriptCompleteEvent
==================================
  This event records the completion of an alarm-triggered script.
:extends: vim.event.AlarmEvent_

Attributes:
    entity (`vim.event.ManagedEntityEventArgument`_):

       The entity with which the alarm is registered.
    script (`str`_):

       The script triggered by the alarm.
