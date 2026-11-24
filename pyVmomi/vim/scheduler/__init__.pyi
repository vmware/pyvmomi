# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.action


class AfterStartupTaskScheduler(TaskScheduler):
   minute: int

class DailyTaskScheduler(HourlyTaskScheduler):
   hour: int

class HourlyTaskScheduler(RecurrentTaskScheduler):
   minute: int

class MonthlyByDayTaskScheduler(MonthlyTaskScheduler):
   day: int


class MonthlyByWeekdayTaskScheduler(MonthlyTaskScheduler):
   class DayOfWeek(pyVmomi.VmomiSupport.Enum):
      sunday: _typing.ClassVar['DayOfWeek'] = 'sunday'
      monday: _typing.ClassVar['DayOfWeek'] = 'monday'
      tuesday: _typing.ClassVar['DayOfWeek'] = 'tuesday'
      wednesday: _typing.ClassVar['DayOfWeek'] = 'wednesday'
      thursday: _typing.ClassVar['DayOfWeek'] = 'thursday'
      friday: _typing.ClassVar['DayOfWeek'] = 'friday'
      saturday: _typing.ClassVar['DayOfWeek'] = 'saturday'

   class WeekOfMonth(pyVmomi.VmomiSupport.Enum):
      first: _typing.ClassVar['WeekOfMonth'] = 'first'
      second: _typing.ClassVar['WeekOfMonth'] = 'second'
      third: _typing.ClassVar['WeekOfMonth'] = 'third'
      fourth: _typing.ClassVar['WeekOfMonth'] = 'fourth'
      last: _typing.ClassVar['WeekOfMonth'] = 'last'

   offset: WeekOfMonth
   weekday: DayOfWeek

class MonthlyTaskScheduler(DailyTaskScheduler):
   pass


class OnceTaskScheduler(TaskScheduler):
   runAt: _typing.Optional[_datetime.datetime] = None

class RecurrentTaskScheduler(TaskScheduler):
   interval: int


class ScheduledTask(pyVmomi.vim.ExtensibleManagedObject):
   @property
   def info(self) -> ScheduledTaskInfo: ...

   def Remove(self) -> None: ...
   def Reconfigure(self, spec: ScheduledTaskSpec) -> None: ...
   def Run(self) -> None: ...


class ScheduledTaskDescription(pyVmomi.vmodl.DynamicData):
   class SchedulerDetail(pyVmomi.vim.TypeDescription):
      frequency: str

   action: list[pyVmomi.vim.TypeDescription] = []
   schedulerInfo: list[SchedulerDetail] = []
   state: list[pyVmomi.vim.ElementDescription] = []
   dayOfWeek: list[pyVmomi.vim.ElementDescription] = []
   weekOfMonth: list[pyVmomi.vim.ElementDescription] = []


class ScheduledTaskInfo(ScheduledTaskSpec):
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
   @property
   def scheduledTask(self) -> list[ScheduledTask]: ...
   @property
   def description(self) -> ScheduledTaskDescription: ...

   def Create(self, entity: pyVmomi.vim.ManagedEntity, spec: ScheduledTaskSpec) -> ScheduledTask: ...
   def RetrieveEntityScheduledTask(self, entity: _typing.Optional[pyVmomi.vim.ManagedEntity]) -> list[ScheduledTask]: ...
   def CreateObjectScheduledTask(self, obj: pyVmomi.VmomiSupport.ManagedObject, spec: ScheduledTaskSpec) -> ScheduledTask: ...
   def RetrieveObjectScheduledTask(self, obj: _typing.Optional[pyVmomi.VmomiSupport.ManagedObject]) -> list[ScheduledTask]: ...


class ScheduledTaskSpec(pyVmomi.vmodl.DynamicData):
   name: str
   description: str
   enabled: bool
   scheduler: TaskScheduler
   action: pyVmomi.vim.action.Action
   notification: _typing.Optional[str] = None


class TaskScheduler(pyVmomi.vmodl.DynamicData):
   activeTime: _typing.Optional[_datetime.datetime] = None
   expireTime: _typing.Optional[_datetime.datetime] = None

class WeeklyTaskScheduler(DailyTaskScheduler):
   sunday: bool
   monday: bool
   tuesday: bool
   wednesday: bool
   thursday: bool
   friday: bool
   saturday: bool
