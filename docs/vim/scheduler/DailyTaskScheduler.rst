.. _int: https://docs.python.org/2/library/stdtypes.html

.. _DailyTaskScheduler: ../../vim/scheduler/DailyTaskScheduler.rst

.. _RecurrentTaskScheduler: ../../vim/scheduler/RecurrentTaskScheduler.rst

.. _vim.scheduler.HourlyTaskScheduler: ../../vim/scheduler/HourlyTaskScheduler.rst


vim.scheduler.DailyTaskScheduler
================================
  The `DailyTaskScheduler`_ data object sets the time for daily task execution. You set the hour and the inherited minute property to complete the schedule. By default, the scheduled task will run once every day at the specified hour and minute.If you set the interval to a value greater than 1, the task will execute at the specified daily interval. (For example, an interval of 2 will cause the task to execute at the specified hour and minute every 2 days.)
:extends: vim.scheduler.HourlyTaskScheduler_

Attributes:
    hour (`int`_):

       The hour at which the `RecurrentTaskScheduler`_ runs the task. Use UTC (Coordinated Universal Time) values in the range 0 to 23, where 0 = 12:00 a.m. (UTC) and 12 = 12:00 p.m. (UTC).For vCenter 2.x and prior releases, use the server's local time. For example, use Eastern Standard Time (EST) or Pacific Daylight Time (PDT), rather than UTC.
