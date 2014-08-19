
vim.scheduler.ScheduledTaskDescription
======================================
  Static strings for scheduled tasks. These strings are locale-specific.
:extends: vmodl.DynamicData_

Attributes:
    action ([`vim.TypeDescription <vim/TypeDescription.rst>`_]):

       Action class descriptions for a scheduled task.
    schedulerInfo ([`vim.scheduler.ScheduledTaskDescription.SchedulerDetail <vim/scheduler/ScheduledTaskDescription/SchedulerDetail.rst>`_]):

       Scheduler class description details.
    state ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `TaskInfo State enum <vim/TaskInfo/State.rst>`_ 
    dayOfWeek ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `MonthlyByWeekdayTaskScheduler Days of the week enum description <vim/scheduler/MonthlyByWeekdayTaskScheduler/DayOfWeek.rst>`_ 
    weekOfMonth ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `MonthlyByWeekdayTaskScheduler Week of the month enum description <vim/scheduler/MonthlyByWeekdayTaskScheduler/WeekOfMonth.rst>`_ 
