
vim.scheduler.TaskScheduler
===========================
  The `TaskScheduler <vim/scheduler/TaskScheduler.rst>`_ data object is the base type for the scheduler objects. The hierarchy of scheduler objects is as follows:TaskScheduler `AfterStartupTaskScheduler <vim/scheduler/AfterStartupTaskScheduler.rst>`_  `OnceTaskScheduler <vim/scheduler/OnceTaskScheduler.rst>`_  `RecurrentTaskScheduler <vim/scheduler/RecurrentTaskScheduler.rst>`_  `HourlyTaskScheduler <vim/scheduler/HourlyTaskScheduler.rst>`_  `DailyTaskScheduler <vim/scheduler/DailyTaskScheduler.rst>`_  `WeeklyTaskScheduler <vim/scheduler/WeeklyTaskScheduler.rst>`_  `MonthlyTaskScheduler <vim/scheduler/MonthlyTaskScheduler.rst>`_  `MonthlyByDayTaskScheduler <vim/scheduler/MonthlyByDayTaskScheduler.rst>`_  `MonthlyByWeekdayTaskScheduler <vim/scheduler/MonthlyByWeekdayTaskScheduler.rst>`_ Use a scheduler object to set the time(s) for task execution. You can use two scheduling modes - single execution or recurring execution:
   * Use the
   * `AfterStartupTaskScheduler <vim/scheduler/AfterStartupTaskScheduler.rst>`_
   * or the
   * `OnceTaskScheduler <vim/scheduler/OnceTaskScheduler.rst>`_
   * to schedule a single instance of task execution.
   * Use one of the recurrent task schedulers to schedule hourly, daily, weekly, or monthly task execution.
   * 
   * After you have established the task timing, use the scheduler object for the
   * `ScheduledTaskSpec <vim/scheduler/ScheduledTaskSpec.rst>`_
   * 
   * `scheduler <vim/scheduler/ScheduledTaskSpec.rst#scheduler>`_
   * property value.
:extends: vmodl.DynamicData_

Attributes:
    activeTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The time that the schedule for the task takes effect. Task activation is distinct from task execution. When you activate a task, its schedule starts, and when the next execution time occurs, the task will run. If you do not set activeTime, the activation time defaults to the time that you create the scheduled task.
    expireTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The time the schedule for the task expires. If you do not set expireTime, the schedule does not expire.
