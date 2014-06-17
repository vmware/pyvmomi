.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vim.event.AlarmEvent: ../../vim/event/AlarmEvent.rst

.. _vim.event.ManagedEntityEventArgument: ../../vim/event/ManagedEntityEventArgument.rst


vim.event.AlarmAcknowledgedEvent
================================
  This event records the acknowledgement of an Alarm
:extends: vim.event.AlarmEvent_
:since: `vSphere API 5.0`_

Attributes:
    source (`vim.event.ManagedEntityEventArgument`_):

       The entity that triggered the alarm.
    entity (`vim.event.ManagedEntityEventArgument`_):

       The entity with which the alarm is registered.
