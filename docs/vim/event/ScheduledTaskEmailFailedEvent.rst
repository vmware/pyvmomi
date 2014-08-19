
vim.event.ScheduledTaskEmailFailedEvent
=======================================
  This event records the failure of an attempt to send a notification via email for a scheduled task.
:extends: vim.event.ScheduledTaskEvent_

Attributes:
    to (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The destination email address.
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The reason for the failure.
