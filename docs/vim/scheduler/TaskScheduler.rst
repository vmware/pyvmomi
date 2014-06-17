.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _scheduler: ../../vim/scheduler/ScheduledTaskSpec.rst#scheduler

.. _TaskScheduler: ../../vim/scheduler/TaskScheduler.rst

.. _OnceTaskScheduler: ../../vim/scheduler/OnceTaskScheduler.rst

.. _ScheduledTaskSpec: ../../vim/scheduler/ScheduledTaskSpec.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _DailyTaskScheduler: ../../vim/scheduler/DailyTaskScheduler.rst

.. _HourlyTaskScheduler: ../../vim/scheduler/HourlyTaskScheduler.rst

.. _WeeklyTaskScheduler: ../../vim/scheduler/WeeklyTaskScheduler.rst

.. _MonthlyTaskScheduler: ../../vim/scheduler/MonthlyTaskScheduler.rst

.. _RecurrentTaskScheduler: ../../vim/scheduler/RecurrentTaskScheduler.rst

.. _MonthlyByDayTaskScheduler: ../../vim/scheduler/MonthlyByDayTaskScheduler.rst

.. _AfterStartupTaskScheduler: ../../vim/scheduler/AfterStartupTaskScheduler.rst

.. _MonthlyByWeekdayTaskScheduler: ../../vim/scheduler/MonthlyByWeekdayTaskScheduler.rst


vim.scheduler.TaskScheduler
===========================
  The `TaskScheduler`_ data object is the base type for the scheduler objects. The hierarchy of scheduler objects is as follows:TaskScheduler `AfterStartupTaskScheduler`_  `OnceTaskScheduler`_  `RecurrentTaskScheduler`_  `HourlyTaskScheduler`_  `DailyTaskScheduler`_  `WeeklyTaskScheduler`_  `MonthlyTaskScheduler`_  `MonthlyByDayTaskScheduler`_  `MonthlyByWeekdayTaskScheduler`_ Use a scheduler object to set the time(s) for task execution. You can use two scheduling modes - single execution or recurring execution:
   * Use the
   * `AfterStartupTaskScheduler`_
   * or the
   * `OnceTaskScheduler`_
   * to schedule a single instance of task execution.
   * Use one of the recurrent task schedulers to schedule hourly, daily, weekly, or monthly task execution.
   * 
   * After you have established the task timing, use the scheduler object for the
   * `ScheduledTaskSpec`_
   * 
   * `scheduler`_
   * property value.
:extends: vmodl.DynamicData_

Attributes:
    activeTime (`datetime`_, optional):

       The time that the schedule for the task takes effect. Task activation is distinct from task execution. When you activate a task, its schedule starts, and when the next execution time occurs, the task will run. If you do not set activeTime, the activation time defaults to the time that you create the scheduled task.
    expireTime (`datetime`_, optional):

       The time the schedule for the task expires. If you do not set expireTime, the schedule does not expire.
