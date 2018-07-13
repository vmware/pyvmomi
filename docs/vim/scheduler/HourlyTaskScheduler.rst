.. _int: https://docs.python.org/2/library/stdtypes.html

.. _HourlyTaskScheduler: ../../vim/scheduler/HourlyTaskScheduler.rst

.. _RecurrentTaskScheduler: ../../vim/scheduler/RecurrentTaskScheduler.rst

.. _vim.scheduler.RecurrentTaskScheduler: ../../vim/scheduler/RecurrentTaskScheduler.rst


vim.scheduler.HourlyTaskScheduler
=================================
  The `HourlyTaskScheduler`_ data object sets the time for hourly task execution. By default, the scheduled task will run once every hour, at the specified minute.If you set the interval to a value greater than 1, the task will execute at the specified hourly interval. (For example, an interval of 2 will cause the task to execute at the specified minute every 2 hours.)
:extends: vim.scheduler.RecurrentTaskScheduler_

Attributes:
    minute (`int`_):

       The minute at which the `RecurrentTaskScheduler`_ runs the task. Specify the minute value as a UTC (Coordinated Universal Time) value in the range 0 to 59.For vCenter 2.x and prior releases, use the server's local time. For example, use Australia Northern Territory (UTC +9:30) or Indian (UTC +5:30) time values, rather than a UTC value.
