# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.action



class TaskScheduler(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vim.scheduler.TaskScheduler` data object is the base type for the scheduler objects.
   
   The hierarchy of scheduler objects is as follows:
   
           TaskScheduler
               `pyVmomi.vim.scheduler.AfterStartupTaskScheduler`
               `pyVmomi.vim.scheduler.OnceTaskScheduler`
               `pyVmomi.vim.scheduler.RecurrentTaskScheduler`
                   `pyVmomi.vim.scheduler.HourlyTaskScheduler`
                       `pyVmomi.vim.scheduler.DailyTaskScheduler`
                           `pyVmomi.vim.scheduler.WeeklyTaskScheduler`
                           `pyVmomi.vim.scheduler.MonthlyTaskScheduler`
                               `pyVmomi.vim.scheduler.MonthlyByDayTaskScheduler`
                               `pyVmomi.vim.scheduler.MonthlyByWeekdayTaskScheduler`
   
   Use a scheduler object to set the time(s) for task execution.
   You can use two scheduling modes - single execution or
   recurring execution:
   - Use the `pyVmomi.vim.scheduler.AfterStartupTaskScheduler` or the `pyVmomi.vim.scheduler.OnceTaskScheduler`
     to schedule a single instance of task execution.
   - Use one of the recurrent task schedulers to schedule
     hourly, daily, weekly, or monthly task execution.
     
   After you have established the task timing, use the scheduler
   object for the `pyVmomi.vim.scheduler.ScheduledTaskSpec`
   `pyVmomi.vim.scheduler.ScheduledTaskSpec.scheduler` property value.
   
   Attributes:
       activeTime: The time that the schedule for the task takes effect.
           
           Task activation is distinct from task execution.
           When you activate a task, its schedule starts,
           and when the next execution time occurs, the task will run.
           If you do not set activeTime, the activation time defaults to
           the time that you create the scheduled task.
       expireTime: The time the schedule for the task expires.
           
           If you do not set expireTime, the schedule does not expire.
   """
   activeTime: _typing.Optional[_datetime.datetime] = None
   expireTime: _typing.Optional[_datetime.datetime] = None

class AfterStartupTaskScheduler(TaskScheduler):
   """
   The `pyVmomi.vim.scheduler.AfterStartupTaskScheduler` data object establishes the time
   that a scheduled task will run after the vCenter server restarts.
   
   Attributes:
       minute: The delay in minutes after vCenter server is restarted.
           
           The value must be greater than or equal to 0.
   """
   minute: int

class RecurrentTaskScheduler(TaskScheduler):
   """
   The `pyVmomi.vim.scheduler.RecurrentTaskScheduler` data object is the base type for
   the hierarchy that includes hourly, daily, weekly, and monthly task schedulers.
   
   Attributes:
       interval: How often to run the scheduled task.
           
           The value must be greater than
           or equal to 1 and less than 1000. The default value is 1.
           The interval acts as a multiplier for the unit of time associated
           with a particular scheduler (hours, days, weeks, or months).
           For example, setting the `pyVmomi.vim.scheduler.HourlyTaskScheduler` interval
           to 4 causes the task to run every 4 hours.
   """
   interval: int

class HourlyTaskScheduler(RecurrentTaskScheduler):
   """
   The `pyVmomi.vim.scheduler.HourlyTaskScheduler` data object sets the time for hourly
   task execution.
   
   By default, the scheduled task will run once every hour,
   at the specified minute.
   
   If you set the interval to a value greater than 1, the task will
   execute at the specified hourly interval. (For example, an interval
   of 2 will cause the task to execute at the specified minute every 2 hours.)
   
   Attributes:
       minute: The minute at which the `pyVmomi.vim.scheduler.RecurrentTaskScheduler` runs
           the task.
           
           Specify the minute value as a UTC (Coordinated Universal Time)
           value in the range 0 to 59.
           
           For vCenter 2.x and prior releases, use the server's local time.
           For example, use Australia Northern Territory (UTC +9:30) or Indian (UTC +5:30)
           time values, rather than a UTC value.
   """
   minute: int

class DailyTaskScheduler(HourlyTaskScheduler):
   """
   The `pyVmomi.vim.scheduler.DailyTaskScheduler` data object sets the time for daily
   task execution.
   
   You set the hour and the inherited minute
   property to complete the schedule. By default, the scheduled task
   will run once every day at the specified hour and minute.
   
   If you set the interval to a value greater than 1, the task will
   execute at the specified daily interval. (For example, an interval
   of 2 will cause the task to execute at the specified hour and minute
   every 2 days.)
   
   Attributes:
       hour: The hour at which the `pyVmomi.vim.scheduler.RecurrentTaskScheduler` runs the task.
           
           Use UTC (Coordinated Universal Time) values in the range
           0 to 23, where 0 = 12:00 a.m. (UTC) and 12 = 12:00 p.m. (UTC).
           
           For vCenter 2.x and prior releases, use the server's local time.
           For example, use Eastern Standard Time (EST) or Pacific Daylight Time (PDT),
           rather than UTC.
   """
   hour: int

class MonthlyTaskScheduler(DailyTaskScheduler):
   """
   The `pyVmomi.vim.scheduler.MonthlyTaskScheduler` data object is the base type for
   the monthly schedulers (`pyVmomi.vim.scheduler.MonthlyByDayTaskScheduler` and
   `pyVmomi.vim.scheduler.MonthlyByWeekdayTaskScheduler`).
   """
   pass

class MonthlyByDayTaskScheduler(MonthlyTaskScheduler):
   """
   The `pyVmomi.vim.scheduler.MonthlyByDayTaskScheduler` data object sets the time for monthly
   task execution.
   
   You can set the schedule for task execution
   on one day during the month, and you complete the schedule by
   setting the inherited properties for the hour and minute.
   
   By default the scheduler executes the task on the specified day
   every month. If you set the interval to a value greater than 1,
   the task will execute at the specified monthly interval.
   (For example, an interval of 2 will cause the task to execute
   on the specified day, hour, and minute every 2 months.)
   
   Attributes:
       day: The day in every month to run the scheduled task.
           
           Valid values are 1 to 31.
           
           In any month where the value of \"day\" exceeds the total number of days
           in the month, the scheduled task will run on the last day of the month.
   """
   day: int


class MonthlyByWeekdayTaskScheduler(MonthlyTaskScheduler):
   """
   The `pyVmomi.vim.scheduler.MonthlyByWeekdayTaskScheduler` data object sets the time for
   monthly task execution.
   
   You identify a single day for task execution
   by specifying the week of the month and day of the week, and you
   complete the schedule by setting the inherited properties for the
   hour and minute.
   
   By default, the scheduler executes the task on the specified day
   every month. If you set the interval to a value greater than 1,
   the task will execute at the specified monthly interval. (For example,
   an interval of 2 will cause the task to execute on the specified
   day, hour, and minute every 2 months.)
   
   Attributes:
       offset: The week in the month during which the scheduled task is to run.
       weekday: The day in the week when the scheduled task is to run.
   """
   class DayOfWeek(pyVmomi.VmomiSupport.Enum):
      sunday: _typing.ClassVar['MonthlyByWeekdayTaskScheduler.DayOfWeek'] = 'sunday'
      monday: _typing.ClassVar['MonthlyByWeekdayTaskScheduler.DayOfWeek'] = 'monday'
      tuesday: _typing.ClassVar['MonthlyByWeekdayTaskScheduler.DayOfWeek'] = 'tuesday'
      wednesday: _typing.ClassVar['MonthlyByWeekdayTaskScheduler.DayOfWeek'] = 'wednesday'
      thursday: _typing.ClassVar['MonthlyByWeekdayTaskScheduler.DayOfWeek'] = 'thursday'
      friday: _typing.ClassVar['MonthlyByWeekdayTaskScheduler.DayOfWeek'] = 'friday'
      saturday: _typing.ClassVar['MonthlyByWeekdayTaskScheduler.DayOfWeek'] = 'saturday'

   class WeekOfMonth(pyVmomi.VmomiSupport.Enum):
      first: _typing.ClassVar['MonthlyByWeekdayTaskScheduler.WeekOfMonth'] = 'first'
      second: _typing.ClassVar['MonthlyByWeekdayTaskScheduler.WeekOfMonth'] = 'second'
      third: _typing.ClassVar['MonthlyByWeekdayTaskScheduler.WeekOfMonth'] = 'third'
      fourth: _typing.ClassVar['MonthlyByWeekdayTaskScheduler.WeekOfMonth'] = 'fourth'
      last: _typing.ClassVar['MonthlyByWeekdayTaskScheduler.WeekOfMonth'] = 'last'

   offset: MonthlyByWeekdayTaskScheduler.WeekOfMonth
   weekday: MonthlyByWeekdayTaskScheduler.DayOfWeek


class OnceTaskScheduler(TaskScheduler):
   """
   The `pyVmomi.vim.scheduler.OnceTaskScheduler` data object establishes the time for running
   a scheduled task only once.
   
   Attributes:
       runAt: The time a task will run.
           
           If you do not set the time, it executes immediately.
   """
   runAt: _typing.Optional[_datetime.datetime] = None


class ScheduledTask(pyVmomi.vim.ExtensibleManagedObject):
   """The scheduled task object."""
   @property
   def info(self) -> ScheduledTaskInfo:
      """Information about the current scheduled task."""
      ...

   def Remove(self) -> None:
      """
      Removes the scheduled task.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: if the scheduled task is running.
      """
      ...
   def Reconfigure(self, spec: ScheduledTaskSpec) -> None:
      """
      Reconfigures the scheduled task properties.
      
      Args:
          spec: The new specification for the scheduled task.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: if the scheduled task is running.
          pyVmomi.vim.fault.InvalidName: if the scheduled task name is empty or too long.
          pyVmomi.vim.fault.DuplicateName: if a scheduled task with the name already exists.
      """
      ...
   def Run(self) -> None:
      """
      Runs the scheduled task immediately.
      
      The schedule for future runs remains in effect.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: if the scheduled task is running already.
      """
      ...


class ScheduledTaskDescription(pyVmomi.vmodl.DynamicData):
   """
   Static strings for scheduled tasks.
   
   These strings are locale-specific.
   
   Attributes:
       action: Action class descriptions for a scheduled task.
       schedulerInfo: Scheduler class description details.
       state: `pyVmomi.vim.TaskInfo.State`
       dayOfWeek: `pyVmomi.vim.scheduler.MonthlyByWeekdayTaskScheduler.DayOfWeek`
       weekOfMonth: `pyVmomi.vim.scheduler.MonthlyByWeekdayTaskScheduler.WeekOfMonth`
   """
   class SchedulerDetail(pyVmomi.vim.TypeDescription):
      """
      Descriptive detail for each scheduler type.
      
      Attributes:
          frequency: Scheduler frequency description.
      """
      frequency: str

   action: list[pyVmomi.vim.TypeDescription] = []
   schedulerInfo: list[ScheduledTaskDescription.SchedulerDetail] = []
   state: list[pyVmomi.vim.ElementDescription] = []
   dayOfWeek: list[pyVmomi.vim.ElementDescription] = []
   weekOfMonth: list[pyVmomi.vim.ElementDescription] = []


class ScheduledTaskSpec(pyVmomi.vmodl.DynamicData):
   """
   Parameters for scheduled task creation.
   
   Attributes:
       name: Name of the scheduled task.
       description: Description of the scheduled task.
       enabled: Flag to indicate whether the scheduled task is enabled or disabled.
       scheduler: The time scheduler that determines when the scheduled task runs.
       action: The action of the scheduled task, to be done when the scheduled task runs.
       notification: The email notification.
           
           If not set, this property is set to empty string, indicating no notification.
   """
   name: str
   description: str
   enabled: bool
   scheduler: TaskScheduler
   action: pyVmomi.vim.action.Action
   notification: _typing.Optional[str] = None


class ScheduledTaskInfo(ScheduledTaskSpec):
   """
   The scheduled task details.
   
   Attributes:
       scheduledTask: Scheduled task object.
       entity: The entity on which related events will be logged.
           
           If the task is scheduled on a ManagedEntity, this
           field will also reflect the same ManagedEntity.
           If task is scheduled on a ManagedObject, this field
           will have information about the entity on which
           the events will be logged on behalf of the ManagedObject.
           ManagedObject itself will be denoted by `pyVmomi.vim.scheduler.ScheduledTaskInfo.taskObject`
       lastModifiedTime: The time the scheduled task is created or modified.
       lastModifiedUser: Last user that modified the scheduled task.
       nextRunTime: The next time the scheduled task will run.
       prevRunTime: The last time the scheduled task ran.
       state: Scheduled task state.
       error: The fault code when the scheduled task state is \"error\".
       result: The operation result when the scheduled task state is \"success\".
       progress: The task progress when the scheduled task state is \"running\".
       activeTask: The running task instance when the scheduled task state is \"running\".
       taskObject: The object on which the scheduled task is defined.
           
           This field will have information about either the
           ManagedEntity or the ManagedObject on which the scheduled
           task is defined.
   """
   scheduledTask: ScheduledTask
   entity: pyVmomi.vim.ManagedEntity
   lastModifiedTime: _datetime.datetime
   lastModifiedUser: str
   nextRunTime: _typing.Optional[_datetime.datetime] = None
   prevRunTime: _typing.Optional[_datetime.datetime] = None
   state: pyVmomi.vim.TaskInfo.State
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   result: _typing.Optional[object] = None
   progress: _typing.Optional[int] = None
   activeTask: _typing.Optional[pyVmomi.vim.Task] = None
   taskObject: pyVmomi.VmomiSupport.ManagedObject


class ScheduledTaskManager(pyVmomi.VmomiSupport.ManagedObject):
   """Object manager for scheduled tasks."""
   @property
   def scheduledTask(self) -> list[ScheduledTask]:
      """All available scheduled tasks."""
      ...
   @property
   def description(self) -> ScheduledTaskDescription:
      """Static descriptive strings used in scheduled tasks."""
      ...

   def Create(self, entity: pyVmomi.vim.ManagedEntity, spec: ScheduledTaskSpec) -> ScheduledTask:
      """
      Creates a scheduled task.
      
      Args:
          entity: The managed entity (or entities) for which the
              scheduled task triggers an action. You can
              schedule tasks on any managed entity. If the
              scheduled task is associated with a leaf node in
              the inventory tree, it applies only to a single
              entity (virtual machine or host). If the
              task is associated with a folder, a datacenter, a
              compute resource, or a resource pool, it applies to
              the virtual machine or host descendants of the entity.
          spec: The specification for the new scheduled task.
      
      Returns:
          The scheduled task created by the operation.
      
      Raises:
          pyVmomi.vim.fault.InvalidName: if the scheduled task name is empty or too long.
          pyVmomi.vim.fault.DuplicateName: if a scheduled task with the name already exists.
      """
      ...
   def RetrieveEntityScheduledTask(self, entity: _typing.Optional[pyVmomi.vim.ManagedEntity]) -> list[ScheduledTask]:
      """
      Available scheduled tasks defined on the entity.
      
      Args:
          entity: The entity. If null, all scheduled tasks are returned
              for visible entities.
      
      Returns:
          The scheduled tasks.
      """
      ...
   def CreateObjectScheduledTask(self, obj: pyVmomi.VmomiSupport.ManagedObject, spec: ScheduledTaskSpec) -> ScheduledTask:
      """
      Creates a scheduled task.
      
      Args:
          obj: The managed object for which the
              scheduled task triggers an action. You can
              schedule tasks on any managed object.
          spec: The specification for the new scheduled task.
      
      Returns:
          The scheduled task created by the operation.
      
      Raises:
          pyVmomi.vim.fault.InvalidName: if the scheduled task name is empty or too long.
          pyVmomi.vim.fault.DuplicateName: if a scheduled task with the name already exists.
      """
      ...
   def RetrieveObjectScheduledTask(self, obj: _typing.Optional[pyVmomi.VmomiSupport.ManagedObject]) -> list[ScheduledTask]:
      """
      Available scheduled tasks defined on the object.
      
      Args:
          obj: The object. If not specified, all scheduled tasks are returned
              for visible entities and visible ManagedObjects.
      
      Returns:
          The scheduled tasks.
      """
      ...

class WeeklyTaskScheduler(DailyTaskScheduler):
   """
   The `pyVmomi.vim.scheduler.WeeklyTaskScheduler` data object sets the time for weekly
   task execution.
   
   You can set the schedule for task execution
   on one or more days during the week, and you complete the schedule
   by setting the inherited properties for the hour and minute.
   
   By default the scheduler executes the task according to the
   specified day(s) every week.
   If you set the interval to a value greater than 1, the task will
   execute at the specified weekly interval. (For example, an interval
   of 2 will cause the task to execute on the specified days every 2 weeks.)
   
   Attributes:
       sunday: The day or days of the week when the scheduled task will run.
           
           At least one of the days must be true.
   """
   sunday: bool
   monday: bool
   tuesday: bool
   wednesday: bool
   thursday: bool
   friday: bool
   saturday: bool
