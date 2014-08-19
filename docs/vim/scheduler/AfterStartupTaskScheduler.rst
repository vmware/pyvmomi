
vim.scheduler.AfterStartupTaskScheduler
=======================================
  The `AfterStartupTaskScheduler <vim/scheduler/AfterStartupTaskScheduler.rst>`_ data object establishes the time that a scheduled task will run after the vCenter server restarts.
:extends: vim.scheduler.TaskScheduler_

Attributes:
    minute (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The delay in minutes after vCenter server is restarted. The value must be greater than or equal to 0.
