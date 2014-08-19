
vim.event.ScheduledTaskFailedEvent
==================================
  This event records the failure of a scheduled task.
:extends: vim.event.ScheduledTaskEvent_

Attributes:
    reason (`vmodl.LocalizedMethodFault <vmodl/LocalizedMethodFault.rst>`_):

       The reason for the failure.
