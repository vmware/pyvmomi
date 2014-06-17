.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _WeeklyTaskScheduler: ../../vim/scheduler/WeeklyTaskScheduler.rst

.. _vim.scheduler.DailyTaskScheduler: ../../vim/scheduler/DailyTaskScheduler.rst


vim.scheduler.WeeklyTaskScheduler
=================================
  The `WeeklyTaskScheduler`_ data object sets the time for weekly task execution. You can set the schedule for task execution on one or more days during the week, and you complete the schedule by setting the inherited properties for the hour and minute.By default the scheduler executes the task according to the specified day(s) every week. If you set the interval to a value greater than 1, the task will execute at the specified weekly interval. (For example, an interval of 2 will cause the task to execute on the specified days every 2 weeks.)
:extends: vim.scheduler.DailyTaskScheduler_

Attributes:
    sunday (`bool`_):

       The day or days of the week when the scheduled task will run. At least one of the days must be true.
    monday (`bool`_):

    tuesday (`bool`_):

    wednesday (`bool`_):

    thursday (`bool`_):

    friday (`bool`_):

    saturday (`bool`_):

