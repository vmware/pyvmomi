.. _vim.event.Event: ../../vim/event/Event.rst

.. _vim.event.ScheduledTaskEventArgument: ../../vim/event/ScheduledTaskEventArgument.rst

.. _vim.event.ManagedEntityEventArgument: ../../vim/event/ManagedEntityEventArgument.rst


vim.event.ScheduledTaskEvent
============================
  These events are scheduled task events.
:extends: vim.event.Event_

Attributes:
    scheduledTask (`vim.event.ScheduledTaskEventArgument`_):

       The scheduled task object.
    entity (`vim.event.ManagedEntityEventArgument`_):

       The entity on which the scheduled task registered.
