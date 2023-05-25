from typing import List, Literal
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType


class ScheduledTask(vim.ExtensibleManagedObject):
    @property
    def info(self) -> ScheduledTaskInfo: ...
    def Remove(self) -> NoneType: ...
    def Reconfigure(self, spec: ScheduledTaskSpec) -> NoneType: ...
    def Run(self) -> NoneType: ...


class ScheduledTaskManager(ManagedObject):
    @property
    def scheduledTask(self) -> List[ScheduledTask]: ...
    @property
    def description(self) -> ScheduledTaskDescription: ...
    def Create(self, entity: vim.ManagedEntity, spec: ScheduledTaskSpec) -> ScheduledTask: ...
    def RetrieveEntityScheduledTask(self, entity: vim.ManagedEntity) -> List[ScheduledTask]: ...
    def CreateObjectScheduledTask(self, obj: ManagedObject, spec: ScheduledTaskSpec) -> ScheduledTask: ...
    def RetrieveObjectScheduledTask(self, obj: ManagedObject) -> List[ScheduledTask]: ...


class AfterStartupTaskScheduler(TaskScheduler):
    @property
    def minute(self) -> int: ...
    @minute.setter
    def minute(self, value: int):
        self._minute = value


class DailyTaskScheduler(HourlyTaskScheduler):
    @property
    def hour(self) -> int: ...
    @hour.setter
    def hour(self, value: int):
        self._hour = value


class HourlyTaskScheduler(RecurrentTaskScheduler):
    @property
    def minute(self) -> int: ...
    @minute.setter
    def minute(self, value: int):
        self._minute = value


class MonthlyByDayTaskScheduler(MonthlyTaskScheduler):
    @property
    def day(self) -> int: ...
    @day.setter
    def day(self, value: int):
        self._day = value


class MonthlyByWeekdayTaskScheduler(MonthlyTaskScheduler):
    @property
    def offset(self) -> MonthlyByWeekdayTaskScheduler.WeekOfMonth | Literal['first', 'second', 'third', 'fourth', 'last']: ...
    @offset.setter
    def offset(self, value: MonthlyByWeekdayTaskScheduler.WeekOfMonth | Literal['first', 'second', 'third', 'fourth', 'last']):
        self._offset = value
    @property
    def weekday(self) -> MonthlyByWeekdayTaskScheduler.DayOfWeek | Literal['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']: ...
    @weekday.setter
    def weekday(self, value: MonthlyByWeekdayTaskScheduler.DayOfWeek | Literal['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']):
        self._weekday = value


    class DayOfWeek(Enum):
        sunday = "sunday"
        monday = "monday"
        tuesday = "tuesday"
        wednesday = "wednesday"
        thursday = "thursday"
        friday = "friday"
        saturday = "saturday"


    class WeekOfMonth(Enum):
        first = "first"
        second = "second"
        third = "third"
        fourth = "fourth"
        last = "last"


class MonthlyTaskScheduler(DailyTaskScheduler): ...


class OnceTaskScheduler(TaskScheduler):
    @property
    def runAt(self) -> datetime: ...
    @runAt.setter
    def runAt(self, value: datetime):
        self._runAt = value


class RecurrentTaskScheduler(TaskScheduler):
    @property
    def interval(self) -> int: ...
    @interval.setter
    def interval(self, value: int):
        self._interval = value


class ScheduledTaskDescription(vmodl.DynamicData):
    @property
    def action(self) -> List[vim.TypeDescription]: ...
    @action.setter
    def action(self, value: List[vim.TypeDescription]):
        self._action = value
    @property
    def schedulerInfo(self) -> List[ScheduledTaskDescription.SchedulerDetail]: ...
    @schedulerInfo.setter
    def schedulerInfo(self, value: List[ScheduledTaskDescription.SchedulerDetail]):
        self._schedulerInfo = value
    @property
    def state(self) -> List[vim.ElementDescription]: ...
    @state.setter
    def state(self, value: List[vim.ElementDescription]):
        self._state = value
    @property
    def dayOfWeek(self) -> List[vim.ElementDescription]: ...
    @dayOfWeek.setter
    def dayOfWeek(self, value: List[vim.ElementDescription]):
        self._dayOfWeek = value
    @property
    def weekOfMonth(self) -> List[vim.ElementDescription]: ...
    @weekOfMonth.setter
    def weekOfMonth(self, value: List[vim.ElementDescription]):
        self._weekOfMonth = value


    class SchedulerDetail(vim.TypeDescription):
        @property
        def frequency(self) -> str: ...
        @frequency.setter
        def frequency(self, value: str):
            self._frequency = value


class ScheduledTaskInfo(ScheduledTaskSpec):
    @property
    def scheduledTask(self) -> ScheduledTask: ...
    @scheduledTask.setter
    def scheduledTask(self, value: ScheduledTask):
        self._scheduledTask = value
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @entity.setter
    def entity(self, value: vim.ManagedEntity):
        self._entity = value
    @property
    def lastModifiedTime(self) -> datetime: ...
    @lastModifiedTime.setter
    def lastModifiedTime(self, value: datetime):
        self._lastModifiedTime = value
    @property
    def lastModifiedUser(self) -> str: ...
    @lastModifiedUser.setter
    def lastModifiedUser(self, value: str):
        self._lastModifiedUser = value
    @property
    def nextRunTime(self) -> datetime: ...
    @nextRunTime.setter
    def nextRunTime(self, value: datetime):
        self._nextRunTime = value
    @property
    def prevRunTime(self) -> datetime: ...
    @prevRunTime.setter
    def prevRunTime(self, value: datetime):
        self._prevRunTime = value
    @property
    def state(self) -> vim.TaskInfo.State | Literal['queued', 'running', 'success', 'error']: ...
    @state.setter
    def state(self, value: vim.TaskInfo.State | Literal['queued', 'running', 'success', 'error']):
        self._state = value
    @property
    def error(self) -> vmodl.MethodFault: ...
    @error.setter
    def error(self, value: vmodl.MethodFault):
        self._error = value
    @property
    def result(self) -> object: ...
    @result.setter
    def result(self, value: object):
        self._result = value
    @property
    def progress(self) -> int: ...
    @progress.setter
    def progress(self, value: int):
        self._progress = value
    @property
    def activeTask(self) -> vim.Task: ...
    @activeTask.setter
    def activeTask(self, value: vim.Task):
        self._activeTask = value
    @property
    def taskObject(self) -> ManagedObject: ...
    @taskObject.setter
    def taskObject(self, value: ManagedObject):
        self._taskObject = value


class ScheduledTaskSpec(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def scheduler(self) -> TaskScheduler: ...
    @scheduler.setter
    def scheduler(self, value: TaskScheduler):
        self._scheduler = value
    @property
    def action(self) -> vim.action.Action: ...
    @action.setter
    def action(self, value: vim.action.Action):
        self._action = value
    @property
    def notification(self) -> str: ...
    @notification.setter
    def notification(self, value: str):
        self._notification = value


class TaskScheduler(vmodl.DynamicData):
    @property
    def activeTime(self) -> datetime: ...
    @activeTime.setter
    def activeTime(self, value: datetime):
        self._activeTime = value
    @property
    def expireTime(self) -> datetime: ...
    @expireTime.setter
    def expireTime(self, value: datetime):
        self._expireTime = value


class WeeklyTaskScheduler(DailyTaskScheduler):
    @property
    def sunday(self) -> bool: ...
    @sunday.setter
    def sunday(self, value: bool):
        self._sunday = value
    @property
    def monday(self) -> bool: ...
    @monday.setter
    def monday(self, value: bool):
        self._monday = value
    @property
    def tuesday(self) -> bool: ...
    @tuesday.setter
    def tuesday(self, value: bool):
        self._tuesday = value
    @property
    def wednesday(self) -> bool: ...
    @wednesday.setter
    def wednesday(self, value: bool):
        self._wednesday = value
    @property
    def thursday(self) -> bool: ...
    @thursday.setter
    def thursday(self, value: bool):
        self._thursday = value
    @property
    def friday(self) -> bool: ...
    @friday.setter
    def friday(self, value: bool):
        self._friday = value
    @property
    def saturday(self) -> bool: ...
    @saturday.setter
    def saturday(self, value: bool):
        self._saturday = value