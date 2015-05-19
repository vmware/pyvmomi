.. _int: https://docs.python.org/2/library/stdtypes.html

.. _HourlyTaskScheduler: ../../vim/scheduler/HourlyTaskScheduler.rst

.. _RecurrentTaskScheduler: ../../vim/scheduler/RecurrentTaskScheduler.rst

.. _vim.scheduler.TaskScheduler: ../../vim/scheduler/TaskScheduler.rst


vim.scheduler.RecurrentTaskScheduler
====================================
  The `RecurrentTaskScheduler`_ data object is the base type for the hierarchy that includes hourly, daily, weekly, and monthly task schedulers.
:extends: vim.scheduler.TaskScheduler_

Attributes:
    interval (`int`_):

       How often to run the scheduled task. The value must be greater than or equal to 1 and less than 1000. The default value is 1. The interval acts as a multiplier for the unit of time associated with a particular scheduler (hours, days, weeks, or months). For example, setting the `HourlyTaskScheduler`_ interval to 4 causes the task to run every 4 hours.
