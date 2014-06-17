.. _int: https://docs.python.org/2/library/stdtypes.html

.. _AfterStartupTaskScheduler: ../../vim/scheduler/AfterStartupTaskScheduler.rst

.. _vim.scheduler.TaskScheduler: ../../vim/scheduler/TaskScheduler.rst


vim.scheduler.AfterStartupTaskScheduler
=======================================
  The `AfterStartupTaskScheduler`_ data object establishes the time that a scheduled task will run after the vCenter server restarts.
:extends: vim.scheduler.TaskScheduler_

Attributes:
    minute (`int`_):

       The delay in minutes after vCenter server is restarted. The value must be greater than or equal to 0.
