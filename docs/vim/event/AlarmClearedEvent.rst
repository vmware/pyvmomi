.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vim.event.AlarmEvent: ../../vim/event/AlarmEvent.rst

.. _vim.event.ManagedEntityEventArgument: ../../vim/event/ManagedEntityEventArgument.rst


vim.event.AlarmClearedEvent
===========================
  This event records the manual clearing of an Alarm
:extends: vim.event.AlarmEvent_
:since: `vSphere API 5.0`_

Attributes:
    source (`vim.event.ManagedEntityEventArgument`_):

       The entity that triggered the alarm.
    entity (`vim.event.ManagedEntityEventArgument`_):

       The entity with which the alarm is registered.
    from (`str`_):

       The original alarm status from which it was cleared
