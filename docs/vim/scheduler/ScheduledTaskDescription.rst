.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.TypeDescription: ../../vim/TypeDescription.rst

.. _TaskInfo State enum: ../../vim/TaskInfo/State.rst

.. _vim.ElementDescription: ../../vim/ElementDescription.rst

.. _vim.scheduler.ScheduledTaskDescription.SchedulerDetail: ../../vim/scheduler/ScheduledTaskDescription/SchedulerDetail.rst

.. _MonthlyByWeekdayTaskScheduler Days of the week enum description: ../../vim/scheduler/MonthlyByWeekdayTaskScheduler/DayOfWeek.rst

.. _MonthlyByWeekdayTaskScheduler Week of the month enum description: ../../vim/scheduler/MonthlyByWeekdayTaskScheduler/WeekOfMonth.rst


vim.scheduler.ScheduledTaskDescription
======================================
  Static strings for scheduled tasks. These strings are locale-specific.
:extends: vmodl.DynamicData_

Attributes:
    action ([`vim.TypeDescription`_]):

       Action class descriptions for a scheduled task.
    schedulerInfo ([`vim.scheduler.ScheduledTaskDescription.SchedulerDetail`_]):

       Scheduler class description details.
    state ([`vim.ElementDescription`_]):

        `TaskInfo State enum`_ 
    dayOfWeek ([`vim.ElementDescription`_]):

        `MonthlyByWeekdayTaskScheduler Days of the week enum description`_ 
    weekOfMonth ([`vim.ElementDescription`_]):

        `MonthlyByWeekdayTaskScheduler Week of the month enum description`_ 
