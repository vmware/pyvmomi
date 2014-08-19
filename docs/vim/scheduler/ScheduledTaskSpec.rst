
vim.scheduler.ScheduledTaskSpec
===============================
  Parameters for scheduled task creation.
:extends: vmodl.DynamicData_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the scheduled task.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Description of the scheduled task.
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether the scheduled task is enabled or disabled.
    scheduler (`vim.scheduler.TaskScheduler <vim/scheduler/TaskScheduler.rst>`_):

       The time scheduler that determines when the scheduled task runs.
    action (`vim.action.Action <vim/action/Action.rst>`_):

       The action of the scheduled task, to be done when the scheduled task runs.
    notification (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The email notification. If not set, this property is set to empty string, indicating no notification.
