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
   """This data object type describes system information."""
   name: str
   fullName: str
   vendor: str
   apiVersion: str
   instanceUuid: str


class QueryDatastoreInfoResult(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vslm.QueryDatastoreInfoResult` provides mapping information
   between `pyVmomi.vim.Datacenter` and `pyVmomi.vim.Datastore`.
   
   This API is returned as a result of
   `pyVmomi.vslm.StorageLifecycleManager.queryDatastoreInfo` invocation.
   
   Attributes:
       datacenter: Indicates the datacenter containing the
           `pyVmomi.vslm.QueryDatastoreInfoResult.datastore`.
       datastore: Indicates the datastore which is contained within the
           `pyVmomi.vslm.QueryDatastoreInfoResult.datacenter`.
   """
   datacenter: pyVmomi.vim.Datacenter
   datastore: pyVmomi.vim.Datastore


class ServiceInstance(pyVmomi.VmomiSupport.ManagedObject):
   """
   The `pyVmomi.vslm.ServiceInstance` managed object is the root object of the
   vSphere Storage Lifecycle Management(VSLM) service.
   
   After you connect to
   VSLM Server, you create a reference to the `pyVmomi.vslm.ServiceInstance`, and use
   that reference to retrieve the `pyVmomi.vslm.ServiceInstanceContent` data
   object. The `pyVmomi.vslm.ServiceInstanceContent` object provides access to
   VSLM managed objects.
   """
   @property
   def content(self) -> ServiceInstanceContent:
      """Contains references to Storage Lifecycle Management managed objects."""
      ...

   def RetrieveContent(self) -> ServiceInstanceContent:
      """
      Retrieves the properties of the Storage Lifecycle Management service
      instance.
      
      Returns:
          Service instance properties that provide access to
          Storage Lifecycle Management managed objects.
      """
      ...


class ServiceInstanceContent(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vslm.ServiceInstanceContent` data object defines properties for the
   `pyVmomi.vslm.ServiceInstance` managed object.
   
   Attributes:
       aboutInfo: Contains information that identifies the Storage Lifecycle Management
           service.
       sessionManager: `pyVmomi.vslm.auth.SessionManager` contains login APIs to connect to VSLM
           service.
       vStorageObjectManager: `pyVmomi.vslm.vso.VStorageObjectManager` contains virtual storage object
           APIs.
       storageLifecycleManager: `pyVmomi.vslm.StorageLifecycleManager` contains callback APIs to VSLM
           service.
   """
   aboutInfo: AboutInfo
   sessionManager: pyVmomi.vslm.auth.SessionManager
   vStorageObjectManager: pyVmomi.vslm.vso.VStorageObjectManager
   storageLifecycleManager: StorageLifecycleManager


class StorageLifecycleManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   Interface to manage storage inventory in VSLM service.
   
   VSLM maintains inventory of VStorageObjects present on all the datastores
   connected to VC. If there is a change in datastore membership in VC that has
   to be updated in VSLM as well.
   APIs in this class are called as callback functions when Datastore
   membership in VC changes.
   """
   def SyncDatastore(self, datastoreUrl: str, fullSync: bool, fcdId: _typing.Optional[pyVmomi.vim.vslm.ID]) -> None:
      """
      Sync the FCD info on the passed in datastore.
      
      Args:
          datastoreUrl: The datastore URL as specified in
              `pyVmomi.vim.Datastore.Info.url`
          fullSync: If this is set to true, all information for this datastore
              will be discarded from the catalog and reloaded from the
              datastore's catalog
          fcdId: If set, this call blocks until fcdId is persisted into db
              if this fcdId is not found in queue, assume persisted and return
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If matching datastore could not be found for the given
              datastoreMoId.
          pyVmomi.vslm.fault.SyncFault: If an exception occurred during datastore sync.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def QueryDatastoreInfo(self, datastoreUrl: str) -> list[QueryDatastoreInfoResult]:
      """
      Query the mapping of `pyVmomi.vim.Datacenter` and `pyVmomi.vim.Datastore`
      for a specified datastore url.
      
      Args:
          datastoreUrl: The datastore URL as specified in
              `pyVmomi.vim.Datastore.Info.url`
      
      Returns:
          Returns array of `pyVmomi.vslm.QueryDatastoreInfoResult`
          representing the mapping between datastores and datacenters.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If the specified datastoreUrl cannot be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...


class Task(pyVmomi.VmomiSupport.ManagedObject):
   """A task is used to monitor long running operations."""
   def QueryResult(self) -> _typing.Optional[object]:
      """Get the result of the task."""
      ...
   def QueryInfo(self) -> TaskInfo:
      """
      Get detailed information about this task.
      
      Returns:
          TaskInfo
      """
      ...
   def Cancel(self) -> None:
      """
      Cancel a running or queued task.
      
      A task may only be canceled if it is
      cancelable. Multiple cancel requests will be treated as a single
      cancellation request. Canceling a completed task will throw an
      InvalidState exception.
      
      If a task is canceled, its runtime state will be set to
      `error` and the `pyVmomi.vslm.TaskInfo.cancelled` flag will
      be set to true.
      
      A cancel operation is asynchronous. The operation may return before the
      task is canceled.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: \\- if the task is already canceled or completed.
      """
      ...


class TaskInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object type contains all information about a VSLM task.
   
   A task represents an operation performed by VirtualCenter or ESX.
   
   Attributes:
       key: The unique key for the task.
       task: The managed object that represents this task.
       description: The description field of the task describes the current phase of
           operation of the task.
           
           For a task that does a single monolithic
           activity, this will be fixed and unchanging.
           For tasks that have various substeps, this field will change
           as the task progresses from one phase to another.
       name: The name of the operation that created the task.
           
           This is not set
           for internal tasks.
       descriptionId: An identifier for this operation.
           
           This includes publicly visible
           internal tasks and is a lookup in the TaskDescription methodInfo
           data object.
       entity: Managed entity to which the operation applies.
       entityName: The name of the managed entity, locale-specific, retained for the
           history collector database.
       locked: If the state of the task is \"running\", then this property is a list of
           managed entities that the operation has locked, with a shared lock.
       state: Runtime status of the task.
       cancelled: Flag to indicate whether or not the client requested
           cancellation of the task.
       cancelable: Flag to indicate whether or not the cancel task operation is supported.
       error: If the task state is \"error\", then this property contains the fault code.
       result: If the task state is \"success\", then this property may be used
           to hold a return value.
       progress: If the task state is \"running\", then this property contains a
           progress measurement, expressed as percentage completed, from 0 to 100.
           
           If this property is not set, then the command does not report progress.
       reason: Kind of entity responsible for creating this task.
       queueTime: Time stamp when the task was created.
       startTime: Time stamp when the task started running.
       completeTime: Time stamp when the task was completed (whether success or failure).
       eventChainId: Event chain ID that leads to the corresponding events.
       changeTag: The user entered tag to identify the operations and their side effects
       parentTaskKey: Tasks can be created by another task.
           
           This shows `pyVmomi.vslm.TaskInfo.key` of the task spun off this task. This is to
           track causality between tasks.
       rootTaskKey: Tasks can be created by another task and such creation can go on for
           multiple levels.
           
           This is the `pyVmomi.vslm.TaskInfo.key` of the task
           that started the chain of tasks.
       activationId: The activation Id is a client-provided token to link an API call with a task.
   """
   class State(pyVmomi.VmomiSupport.Enum):
      """
      List of possible states of a task.
      
      Attributes:
          queued: When there are too many tasks for threads to handle.
          running: When the busy thread is freed from its current task by
              finishing the task, it picks a queued task to run.
              
              Then the queued tasks are marked as running.
          success: When a running task has completed.
          error: When a running task has encountered an error.
      """
      queued: _typing.ClassVar['TaskInfo.State'] = 'queued'
      running: _typing.ClassVar['TaskInfo.State'] = 'running'
      success: _typing.ClassVar['TaskInfo.State'] = 'success'
      error: _typing.ClassVar['TaskInfo.State'] = 'error'

   key: str
   task: Task
   description: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None
   name: _typing.Optional[pyVmomi.VmomiSupport.ManagedMethod] = None
   descriptionId: str
   entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   entityName: _typing.Optional[str] = None
   locked: list[pyVmomi.vim.ManagedEntity] = []
   state: TaskInfo.State
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
   """
   Base type for all task reasons.
   
   Task reasons represent the kind of entity responsible for a task's creation.
   """
   pass


class TaskReasonAlarm(TaskReason):
   """
   Indicates that the task was queued by an alarm.
   
   Attributes:
       alarmName: The name of the alarm that queued the task, retained in the history
           collector database.
       alarm: The alarm object that queued the task.
       entityName: The name of the managed entity on which the alarm is triggered,
           retained in the history collector database.
       entity: The managed entity object on which the alarm is triggered.
   """
   alarmName: str
   alarm: pyVmomi.vim.alarm.Alarm
   entityName: str
   entity: pyVmomi.vim.ManagedEntity


class TaskReasonSchedule(TaskReason):
   """
   Indicates that the task was queued by a scheduled task.
   
   Attributes:
       name: The name of the scheduled task that queued this task.
       scheduledTask: The scheduledTask object that queued this task.
   """
   name: str
   scheduledTask: pyVmomi.vim.scheduler.ScheduledTask

class TaskReasonSystem(TaskReason):
   """Indicates that the task was started by the system (a default task)."""
   pass

class TaskReasonUser(TaskReason):
   """
   Indicates that the task was queued by a specific user.
   
   Attributes:
       userName: Name of the user that queued the task.
   """
   userName: str
