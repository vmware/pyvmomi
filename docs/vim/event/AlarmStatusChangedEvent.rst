.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.AlarmEvent: ../../vim/event/AlarmEvent.rst

.. _vim.event.ManagedEntityEventArgument: ../../vim/event/ManagedEntityEventArgument.rst


vim.event.AlarmStatusChangedEvent
=================================
  This event records a status change for an alarm.
:extends: vim.event.AlarmEvent_

Attributes:
    source (`vim.event.ManagedEntityEventArgument`_):

       The entity for which the alarm status has been changed.
    entity (`vim.event.ManagedEntityEventArgument`_):

       The entity with which the alarm is registered.
    from (`str`_):

       The original alarm status.
    to (`str`_):

       The new alarm status.
