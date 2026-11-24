# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import auth as auth
from . import fault as fault
from . import vso as vso

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.alarm
import pyVmomi.vim.scheduler
import pyVmomi.vim.vslm
import pyVmomi.vslm.auth
import pyVmomi.vslm.vso



class AboutInfo(pyVmomi.vmodl.DynamicData):
   name: str
   fullName: str
   vendor: str
   apiVersion: str
   instanceUuid: str


class QueryDatastoreInfoResult(pyVmomi.vmodl.DynamicData):
   datacenter: pyVmomi.vim.Datacenter
   datastore: pyVmomi.vim.Datastore


class ServiceInstance(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def content(self) -> ServiceInstanceContent: ...

   def RetrieveContent(self) -> ServiceInstanceContent: ...


class ServiceInstanceContent(pyVmomi.vmodl.DynamicData):
   aboutInfo: AboutInfo
   sessionManager: pyVmomi.vslm.auth.SessionManager
   vStorageObjectManager: pyVmomi.vslm.vso.VStorageObjectManager
   storageLifecycleManager: StorageLifecycleManager


class StorageLifecycleManager(pyVmomi.VmomiSupport.ManagedObject):
   def SyncDatastore(self, datastoreUrl: str, fullSync: bool, fcdId: _typing.Optional[pyVmomi.vim.vslm.ID]) -> None: ...
   def QueryDatastoreInfo(self, datastoreUrl: str) -> list[QueryDatastoreInfoResult]: ...


class Task(pyVmomi.VmomiSupport.ManagedObject):
   def QueryResult(self) -> _typing.Optional[object]: ...
   def QueryInfo(self) -> TaskInfo: ...
   def Cancel(self) -> None: ...


class TaskInfo(pyVmomi.vmodl.DynamicData):
   class State(pyVmomi.VmomiSupport.Enum):
      queued: _typing.ClassVar['State'] = 'queued'
      running: _typing.ClassVar['State'] = 'running'
      success: _typing.ClassVar['State'] = 'success'
      error: _typing.ClassVar['State'] = 'error'

   key: str
   task: Task
   description: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None
   name: _typing.Optional[pyVmomi.VmomiSupport.ManagedMethod] = None
   descriptionId: str
   entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   entityName: _typing.Optional[str] = None
   locked: list[pyVmomi.vim.ManagedEntity] = []
   state: State
   cancelled: bool
   cancelable: bool
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   result: _typing.Optional[object] = None
   progress: _typing.Optional[int] = None
   reason: TaskReason
   queueTime: _datetime.datetime
   startTime: _typing.Optional[_datetime.datetime] = None
   completeTime: _typing.Optional[_datetime.datetime] = None
   eventChainId: int
   changeTag: _typing.Optional[str] = None
   parentTaskKey: _typing.Optional[str] = None
   rootTaskKey: _typing.Optional[str] = None
   activationId: _typing.Optional[str] = None


class TaskReason(pyVmomi.vmodl.DynamicData):
   pass


class TaskReasonAlarm(TaskReason):
   alarmName: str
   alarm: pyVmomi.vim.alarm.Alarm
   entityName: str
   entity: pyVmomi.vim.ManagedEntity


class TaskReasonSchedule(TaskReason):
   name: str
   scheduledTask: pyVmomi.vim.scheduler.ScheduledTask

class TaskReasonSystem(TaskReason):
   pass

class TaskReasonUser(TaskReason):
   userName: str
