# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import auth as auth
from . import fault as fault
from . import provider as provider
from . import storage as storage

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.sms.auth
import pyVmomi.sms.provider
import pyVmomi.sms.storage
import pyVmomi.sms.storage.replication
import pyVmomi.vim.vm.replication



class AboutInfo(pyVmomi.vmodl.DynamicData):
   name: str
   fullName: str
   vendor: str
   apiVersion: str
   instanceUuid: str
   vasaApiVersion: _typing.Optional[str] = None


class EntityReference(pyVmomi.vmodl.DynamicData):
   class EntityType(pyVmomi.VmomiSupport.Enum):
      datacenter: _typing.ClassVar['EntityType'] = 'datacenter'
      resourcePool: _typing.ClassVar['EntityType'] = 'resourcePool'
      storagePod: _typing.ClassVar['EntityType'] = 'storagePod'
      cluster: _typing.ClassVar['EntityType'] = 'cluster'
      vm: _typing.ClassVar['EntityType'] = 'vm'
      datastore: _typing.ClassVar['EntityType'] = 'datastore'
      host: _typing.ClassVar['EntityType'] = 'host'
      vmFile: _typing.ClassVar['EntityType'] = 'vmFile'
      scsiPath: _typing.ClassVar['EntityType'] = 'scsiPath'
      scsiTarget: _typing.ClassVar['EntityType'] = 'scsiTarget'
      scsiVolume: _typing.ClassVar['EntityType'] = 'scsiVolume'
      scsiAdapter: _typing.ClassVar['EntityType'] = 'scsiAdapter'
      nasMount: _typing.ClassVar['EntityType'] = 'nasMount'

   id: str
   type: _typing.Optional[EntityType] = None


class FaultDomainFilter(pyVmomi.vmodl.DynamicData):
   providerId: _typing.Optional[str] = None


class ReplicationGroupFilter(pyVmomi.vmodl.DynamicData):
   groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId] = []


class ServiceInstance(pyVmomi.VmomiSupport.ManagedObject):
   def QueryStorageManager(self) -> StorageManager: ...
   def QuerySessionManager(self) -> pyVmomi.sms.auth.SessionManager: ...
   def QueryAboutInfo(self) -> AboutInfo: ...


class StorageManager(pyVmomi.VmomiSupport.ManagedObject):
   def RegisterProvider(self, providerSpec: pyVmomi.sms.provider.ProviderSpec) -> pyVmomi.vim.Task: ...
   def UnregisterProvider(self, providerId: str) -> pyVmomi.vim.Task: ...
   def QueryProvider(self) -> list[pyVmomi.sms.provider.Provider]: ...
   def QueryArray(self, providerId: list[str]) -> list[pyVmomi.sms.storage.StorageArray]: ...
   def QueryProcessorAssociatedWithArray(self, arrayId: str) -> list[pyVmomi.sms.storage.StorageProcessor]: ...
   def QueryPortAssociatedWithArray(self, arrayId: str) -> list[pyVmomi.sms.storage.StoragePort]: ...
   def QueryPortAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> _typing.Optional[pyVmomi.sms.storage.StoragePort]: ...
   def QueryLunAssociatedWithPort(self, portId: str, arrayId: str) -> list[pyVmomi.sms.storage.StorageLun]: ...
   def QueryArrayAssociatedWithLun(self, canonicalName: str) -> _typing.Optional[pyVmomi.sms.storage.StorageArray]: ...
   def QueryPortAssociatedWithProcessor(self, processorId: str, arrayId: str) -> list[pyVmomi.sms.storage.StoragePort]: ...
   def QueryLunAssociatedWithArray(self, arrayId: str) -> list[pyVmomi.sms.storage.StorageLun]: ...
   def QueryFileSystemAssociatedWithArray(self, arrayId: str) -> list[pyVmomi.sms.storage.StorageFileSystem]: ...
   def QueryDatastoreCapability(self, datastore: pyVmomi.vim.Datastore) -> _typing.Optional[pyVmomi.sms.storage.StorageCapability]: ...
   def QueryHostAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> list[pyVmomi.vim.HostSystem]: ...
   def QueryVmfsDatastoreAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> _typing.Optional[pyVmomi.vim.Datastore]: ...
   def QueryNfsDatastoreAssociatedWithFileSystem(self, fileSystemId: str, arrayId: str) -> _typing.Optional[pyVmomi.vim.Datastore]: ...
   def QueryDrsMigrationCapabilityForPerformance(self, srcDatastore: pyVmomi.vim.Datastore, dstDatastore: pyVmomi.vim.Datastore) -> bool: ...
   def QueryDrsMigrationCapabilityForPerformanceEx(self, datastore: list[pyVmomi.vim.Datastore]) -> pyVmomi.sms.storage.DrsMigrationCapabilityResult: ...
   def QueryStorageContainer(self, containerSpec: _typing.Optional[pyVmomi.sms.storage.StorageContainerSpec]) -> _typing.Optional[pyVmomi.sms.storage.StorageContainerResult]: ...
   def QueryAssociatedBackingStoragePool(self, entityId: _typing.Optional[str], entityType: _typing.Optional[str]) -> list[pyVmomi.sms.storage.BackingStoragePool]: ...
   def QueryDatastoreBackingPoolMapping(self, datastore: list[pyVmomi.vim.Datastore]) -> list[pyVmomi.sms.storage.DatastoreBackingPoolMapping]: ...
   def RefreshCACertificatesAndCRLs(self, providerId: list[str]) -> pyVmomi.vim.Task: ...
   def QueryFaultDomain(self, filter: _typing.Optional[FaultDomainFilter]) -> list[pyVmomi.vim.vm.replication.FaultDomainId]: ...
   def QueryReplicationGroupInfo(self, rgFilter: ReplicationGroupFilter) -> list[pyVmomi.sms.storage.replication.GroupOperationResult]: ...
   def UpgradeVASAProvider(self, upgradeSpec: pyVmomi.sms.provider.VASAProviderUpgradeSpec) -> pyVmomi.vim.Task: ...


class Task(pyVmomi.VmomiSupport.ManagedObject):
   def QueryResult(self) -> _typing.Optional[object]: ...
   def QueryInfo(self) -> TaskInfo: ...


class TaskInfo(pyVmomi.vmodl.DynamicData):
   class State(pyVmomi.VmomiSupport.Enum):
      queued: _typing.ClassVar['State'] = 'queued'
      running: _typing.ClassVar['State'] = 'running'
      success: _typing.ClassVar['State'] = 'success'
      error: _typing.ClassVar['State'] = 'error'

   key: str
   task: Task
   object: _typing.Optional[pyVmomi.VmomiSupport.ManagedObject] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   result: _typing.Optional[object] = None
   startTime: _typing.Optional[_datetime.datetime] = None
   completionTime: _typing.Optional[_datetime.datetime] = None
   state: str
   progress: _typing.Optional[int] = None
