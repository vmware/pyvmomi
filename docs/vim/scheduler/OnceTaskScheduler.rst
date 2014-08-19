
vim.scheduler.OnceTaskScheduler
===============================
  The `OnceTaskScheduler <vim/scheduler/OnceTaskScheduler.rst>`_ data object establishes the time for running a scheduled task only once.
:extends: vim.scheduler.TaskScheduler_

Attributes:
    runAt (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The time a task will run. If you do not set the time, it executes immediately.
