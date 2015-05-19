.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _OnceTaskScheduler: ../../vim/scheduler/OnceTaskScheduler.rst

.. _vim.scheduler.TaskScheduler: ../../vim/scheduler/TaskScheduler.rst


vim.scheduler.OnceTaskScheduler
===============================
  The `OnceTaskScheduler`_ data object establishes the time for running a scheduled task only once.
:extends: vim.scheduler.TaskScheduler_

Attributes:
    runAt (`datetime`_, optional):

       The time a task will run. If you do not set the time, it executes immediately.
