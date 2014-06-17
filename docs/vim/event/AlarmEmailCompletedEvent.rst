.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.event.AlarmEvent: ../../vim/event/AlarmEvent.rst

.. _vim.event.ManagedEntityEventArgument: ../../vim/event/ManagedEntityEventArgument.rst


vim.event.AlarmEmailCompletedEvent
==================================
  This event records the completion of an alarm email notification.
:extends: vim.event.AlarmEvent_

Attributes:
    entity (`vim.event.ManagedEntityEventArgument`_):

       The entity with which the alarm is registered.
    to (`str`_):

       The destination email address.
