.. _int: https://docs.python.org/2/library/stdtypes.html

.. _MonthlyByDayTaskScheduler: ../../vim/scheduler/MonthlyByDayTaskScheduler.rst

.. _vim.scheduler.MonthlyTaskScheduler: ../../vim/scheduler/MonthlyTaskScheduler.rst


vim.scheduler.MonthlyByDayTaskScheduler
=======================================
  The `MonthlyByDayTaskScheduler`_ data object sets the time for monthly task execution. You can set the schedule for task execution on one day during the month, and you complete the schedule by setting the inherited properties for the hour and minute.By default the scheduler executes the task on the specified day every month. If you set the interval to a value greater than 1, the task will execute at the specified monthly interval. (For example, an interval of 2 will cause the task to execute on the specified day, hour, and minute every 2 months.)
:extends: vim.scheduler.MonthlyTaskScheduler_

Attributes:
    day (`int`_):

       The day in every month to run the scheduled task. Valid values are 1 to 31.In any month where the value of "day" exceeds the total number of days in the month, the scheduled task will run on the last day of the month.
