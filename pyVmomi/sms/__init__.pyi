from typing import List
from enum import Enum
from pyVmomi import auth, vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject
from . import provider, storage


class ServiceInstance(ManagedObject):
    def QueryStorageManager(self) -> StorageManager: ...
    def QuerySessionManager(self) -> auth.SessionManager: ...
    def QueryAboutInfo(self) -> AboutInfo: ...


class StorageManager(ManagedObject):
    def RegisterProvider(self, providerSpec: provider.ProviderSpec) -> Task: ...
    def UnregisterProvider(self, providerId: str) -> Task: ...
    def QueryProvider(self) -> List[provider.Provider]: ...
    def QueryArray(self, providerId: List[str]) -> List[storage.StorageArray]: ...
    def QueryProcessorAssociatedWithArray(self, arrayId: str) -> List[storage.StorageProcessor]: ...
    def QueryPortAssociatedWithArray(self, arrayId: str) -> List[storage.StoragePort]: ...
    def QueryPortAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> storage.StoragePort: ...
    def QueryLunAssociatedWithPort(self, portId: str, arrayId: str) -> List[storage.StorageLun]: ...
    def QueryArrayAssociatedWithLun(self, canonicalName: str) -> storage.StorageArray: ...
    def QueryPortAssociatedWithProcessor(self, processorId: str, arrayId: str) -> List[storage.StoragePort]: ...
    def QueryLunAssociatedWithArray(self, arrayId: str) -> List[storage.StorageLun]: ...
    def QueryFileSystemAssociatedWithArray(self, arrayId: str) -> List[storage.StorageFileSystem]: ...
    def QueryDatastoreCapability(self, datastore: vim.Datastore) -> storage.StorageCapability: ...
    def QueryHostAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> List[vim.HostSystem]: ...
    def QueryVmfsDatastoreAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> vim.Datastore: ...
    def QueryNfsDatastoreAssociatedWithFileSystem(self, fileSystemId: str, arrayId: str) -> vim.Datastore: ...
    def QueryDrsMigrationCapabilityForPerformance(self, srcDatastore: vim.Datastore, dstDatastore: vim.Datastore) -> bool: ...
    def QueryDrsMigrationCapabilityForPerformanceEx(self, datastore: List[vim.Datastore]) -> storage.DrsMigrationCapabilityResult: ...
    def QueryStorageContainer(self, containerSpec: storage.StorageContainerSpec) -> storage.StorageContainerResult: ...
    def QueryAssociatedBackingStoragePool(self, entityId: str, entityType: str) -> List[storage.BackingStoragePool]: ...
    def QueryDatastoreBackingPoolMapping(self, datastore: List[vim.Datastore]) -> List[storage.DatastoreBackingPoolMapping]: ...
    def RefreshCACertificatesAndCRLs(self, providerId: List[str]) -> Task: ...
    def QueryFaultDomain(self, filter: FaultDomainFilter) -> List[vim.vm.replication.FaultDomainId]: ...
    def QueryReplicationGroupInfo(self, rgFilter: ReplicationGroupFilter) -> List[storage.replication.GroupOperationResult]: ...


class Task(ManagedObject):
    def QueryResult(self) -> object: ...
    def QueryInfo(self) -> TaskInfo: ...


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
    @property
    def vasaApiVersion(self) -> str: ...
    @vasaApiVersion.setter
    def vasaApiVersion(self, value: str):
        self._vasaApiVersion = value


class EntityReference(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def type(self) -> EntityReference.EntityType: ...
    @type.setter
    def type(self, value: EntityReference.EntityType):
        self._type = value


    class EntityType(Enum):
        datacenter = "datacenter"
        resourcePool = "resourcePool"
        storagePod = "storagePod"
        cluster = "cluster"
        vm = "vm"
        datastore = "datastore"
        host = "host"
        vmFile = "vmFile"
        scsiPath = "scsiPath"
        scsiTarget = "scsiTarget"
        scsiVolume = "scsiVolume"
        scsiAdapter = "scsiAdapter"
        nasMount = "nasMount"


class FaultDomainFilter(vmodl.DynamicData):
    @property
    def providerId(self) -> str: ...
    @providerId.setter
    def providerId(self, value: str):
        self._providerId = value


class ReplicationGroupFilter(vmodl.DynamicData):
    @property
    def groupId(self) -> List[vim.vm.replication.ReplicationGroupId]: ...
    @groupId.setter
    def groupId(self, value: List[vim.vm.replication.ReplicationGroupId]):
        self._groupId = value


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
    def object(self) -> ManagedObject: ...
    @object.setter
    def object(self, value: ManagedObject):
        self._object = value
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
    def startTime(self) -> datetime: ...
    @startTime.setter
    def startTime(self, value: datetime):
        self._startTime = value
    @property
    def completionTime(self) -> datetime: ...
    @completionTime.setter
    def completionTime(self, value: datetime):
        self._completionTime = value
    @property
    def state(self) -> str: ...
    @state.setter
    def state(self, value: str):
        self._state = value
    @property
    def progress(self) -> int: ...
    @progress.setter
    def progress(self, value: int):
        self._progress = value


    class State(Enum):
        queued = "queued"
        running = "running"
        success = "success"
        error = "error"