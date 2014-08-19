
vim.event.ScheduledTaskEmailCompletedEvent
==========================================
  This event records the sending of a notification via email for a scheduled task.
:extends: vim.event.ScheduledTaskEvent_

Attributes:
    to (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The destination email address.
