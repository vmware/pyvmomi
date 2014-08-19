
vim.TaskReasonSchedule
======================
  Indicates that the task was queued by a scheduled task.
:extends: vim.TaskReason_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the scheduled task that queued this task.
    scheduledTask (`vim.scheduler.ScheduledTask <vim/scheduler/ScheduledTask.rst>`_):

       The scheduledTask object that queued this task.
