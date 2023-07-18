from typing import List, Literal
from enum import Enum
from pyVmomi import vim, vmodl, vslm
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedMethod, ManagedObject, NoneType
from . import auth as auth
from . import event as event
from . import fault as fault
from . import vso as vso


class ServiceInstance(ManagedObject):
    @property
    def content(self) -> ServiceInstanceContent: ...
    def RetrieveContent(self) -> ServiceInstanceContent: ...


class StorageLifecycleManager(ManagedObject):
    def SyncDatastore(self, datastoreUrl: str, fullSync: bool, fcdId: vim.vslm.ID) -> NoneType: ...
    def QueryDatastoreInfo(self, datastoreUrl: str) -> List[QueryDatastoreInfoResult]: ...


class Task(ManagedObject):
    def QueryResult(self) -> object: ...
    def QueryInfo(self) -> TaskInfo: ...
    def Cancel(self) -> NoneType: ...


class AboutInfo(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def fullName(self) -> str: ...
    @fullName.setter
    def fullName(self, value: str):
        self._fullName = value
    @property
    def vendor(self) -> str: ...
    @vendor.setter
    def vendor(self, value: str):
        self._vendor = value
    @property
    def apiVersion(self) -> str: ...
    @apiVersion.setter
    def apiVersion(self, value: str):
        self._apiVersion = value
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value


class QueryDatastoreInfoResult(vmodl.DynamicData):
    @property
    def datacenter(self) -> vim.Datacenter: ...
    @datacenter.setter
    def datacenter(self, value: vim.Datacenter):
        self._datacenter = value
    @property
    def datastore(self) -> vim.Datastore: ...
    @datastore.setter
    def datastore(self, value: vim.Datastore):
        self._datastore = value


class ServiceInstanceContent(vmodl.DynamicData):
    @property
    def aboutInfo(self) -> AboutInfo: ...
    @aboutInfo.setter
    def aboutInfo(self, value: AboutInfo):
        self._aboutInfo = value
    @property
    def sessionManager(self) -> vslm.auth.SessionManager: ...
    @sessionManager.setter
    def sessionManager(self, value: vslm.auth.SessionManager):
        self._sessionManager = value
    @property
    def vStorageObjectManager(self) -> vslm.vso.VStorageObjectManager: ...
    @vStorageObjectManager.setter
    def vStorageObjectManager(self, value: vslm.vso.VStorageObjectManager):
        self._vStorageObjectManager = value
    @property
    def storageLifecycleManager(self) -> StorageLifecycleManager: ...
    @storageLifecycleManager.setter
    def storageLifecycleManager(self, value: StorageLifecycleManager):
        self._storageLifecycleManager = value


class TaskInfo(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def task(self) -> Task: ...
    @task.setter
    def task(self, value: Task):
        self._task = value
    @property
    def description(self) -> vmodl.LocalizableMessage: ...
    @description.setter
    def description(self, value: vmodl.LocalizableMessage):
        self._description = value
    @property
    def name(self) -> ManagedMethod: ...
    @name.setter
    def name(self, value: ManagedMethod):
        self._name = value
    @property
    def descriptionId(self) -> str: ...
    @descriptionId.setter
    def descriptionId(self, value: str):
        self._descriptionId = value
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @entity.setter
    def entity(self, value: vim.ManagedEntity):
        self._entity = value
    @property
    def entityName(self) -> str: ...
    @entityName.setter
    def entityName(self, value: str):
        self._entityName = value
    @property
    def locked(self) -> List[vim.ManagedEntity]: ...
    @locked.setter
    def locked(self, value: List[vim.ManagedEntity]):
        self._locked = value
    @property
    def state(self) -> TaskInfo.State | Literal['queued', 'running', 'success', 'error']: ...
    @state.setter
    def state(self, value: TaskInfo.State | Literal['queued', 'running', 'success', 'error']):
        self._state = value
    @property
    def cancelled(self) -> bool: ...
    @cancelled.setter
    def cancelled(self, value: bool):
        self._cancelled = value
    @property
    def cancelable(self) -> bool: ...
    @cancelable.setter
    def cancelable(self, value: bool):
        self._cancelable = value
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
    def reason(self) -> TaskReason: ...
    @reason.setter
    def reason(self, value: TaskReason):
        self._reason = value
    @property
    def queueTime(self) -> datetime: ...
    @queueTime.setter
    def queueTime(self, value: datetime):
        self._queueTime = value
    @property
    def startTime(self) -> datetime: ...
    @startTime.setter
    def startTime(self, value: datetime):
        self._startTime = value
    @property
    def completeTime(self) -> datetime: ...
    @completeTime.setter
    def completeTime(self, value: datetime):
        self._completeTime = value
    @property
    def eventChainId(self) -> int: ...
    @eventChainId.setter
    def eventChainId(self, value: int):
        self._eventChainId = value
    @property
    def changeTag(self) -> str: ...
    @changeTag.setter
    def changeTag(self, value: str):
        self._changeTag = value
    @property
    def parentTaskKey(self) -> str: ...
    @parentTaskKey.setter
    def parentTaskKey(self, value: str):
        self._parentTaskKey = value
    @property
    def rootTaskKey(self) -> str: ...
    @rootTaskKey.setter
    def rootTaskKey(self, value: str):
        self._rootTaskKey = value
    @property
    def activationId(self) -> str: ...
    @activationId.setter
    def activationId(self, value: str):
        self._activationId = value


    class State(Enum):
        queued = "queued"
        running = "running"
        success = "success"
        error = "error"


class TaskReason(vmodl.DynamicData): ...


class TaskReasonAlarm(TaskReason):
    @property
    def alarmName(self) -> str: ...
    @alarmName.setter
    def alarmName(self, value: str):
        self._alarmName = value
    @property
    def alarm(self) -> vim.alarm.Alarm: ...
    @alarm.setter
    def alarm(self, value: vim.alarm.Alarm):
        self._alarm = value
    @property
    def entityName(self) -> str: ...
    @entityName.setter
    def entityName(self, value: str):
        self._entityName = value
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @entity.setter
    def entity(self, value: vim.ManagedEntity):
        self._entity = value


class TaskReasonSchedule(TaskReason):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def scheduledTask(self) -> vim.scheduler.ScheduledTask: ...
    @scheduledTask.setter
    def scheduledTask(self, value: vim.scheduler.ScheduledTask):
        self._scheduledTask = value


class TaskReasonSystem(TaskReason): ...


class TaskReasonUser(TaskReason):
    @property
    def userName(self) -> str: ...
    @userName.setter
    def userName(self, value: str):
        self._userName = value