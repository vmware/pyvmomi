from typing import List
from enum import Enum
from pyVmomi import vim, vmodl, vslm
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType, long


class VStorageObjectManager(ManagedObject):
    def CreateDisk(self, spec: vim.vslm.CreateSpec) -> vslm.Task: ...
    def RegisterDisk(self, path: str, name: str) -> vim.vslm.VStorageObject: ...
    def ExtendDisk(self, id: vim.vslm.ID, newCapacityInMB: long) -> vslm.Task: ...
    def InflateDisk(self, id: vim.vslm.ID) -> vslm.Task: ...
    def RenameVStorageObject(self, id: vim.vslm.ID, name: str) -> NoneType: ...
    def UpdateVStorageObjectPolicy(self, id: vim.vslm.ID, profile: List[vim.vm.ProfileSpec]) -> vslm.Task: ...
    def UpdateVStorageObjectCrypto(self, id: vim.vslm.ID, profile: List[vim.vm.ProfileSpec], disksCrypto: vim.vslm.DiskCryptoSpec) -> vslm.Task: ...
    def UpdateVStorageInfrastructureObjectPolicy(self, spec: vim.vslm.InfrastructureObjectPolicySpec) -> vslm.Task: ...
    def RetrieveVStorageInfrastructureObjectPolicy(self, datastore: vim.Datastore) -> List[vim.vslm.InfrastructureObjectPolicy]: ...
    def DeleteVStorageObject(self, id: vim.vslm.ID) -> vslm.Task: ...
    def RetrieveVStorageObject(self, id: vim.vslm.ID) -> vim.vslm.VStorageObject: ...
    def RetrieveVStorageObjectState(self, id: vim.vslm.ID) -> vim.vslm.StateInfo: ...
    def RetrieveVStorageObjectAssociations(self, ids: List[vim.vslm.ID]) -> List[VStorageObjectAssociations]: ...
    def ListVStorageObjectsForSpec(self, query: List[VStorageObjectQuerySpec], maxResult: int) -> VStorageObjectQueryResult: ...
    def CloneVStorageObject(self, id: vim.vslm.ID, spec: vim.vslm.CloneSpec) -> vslm.Task: ...
    def RelocateVStorageObject(self, id: vim.vslm.ID, spec: vim.vslm.RelocateSpec) -> vslm.Task: ...
    def SetVStorageObjectControlFlags(self, id: vim.vslm.ID, controlFlags: List[str]) -> NoneType: ...
    def ClearVStorageObjectControlFlags(self, id: vim.vslm.ID, controlFlags: List[str]) -> NoneType: ...
    def AttachTagToVStorageObject(self, id: vim.vslm.ID, category: str, tag: str) -> NoneType: ...
    def DetachTagFromVStorageObject(self, id: vim.vslm.ID, category: str, tag: str) -> NoneType: ...
    def ListVStorageObjectsAttachedToTag(self, category: str, tag: str) -> List[vim.vslm.ID]: ...
    def ListTagsAttachedToVStorageObject(self, id: vim.vslm.ID) -> List[vim.vslm.TagEntry]: ...
    def ReconcileDatastoreInventory(self, datastore: vim.Datastore) -> vslm.Task: ...
    def ScheduleReconcileDatastoreInventory(self, datastore: vim.Datastore) -> NoneType: ...
    def CreateSnapshot(self, id: vim.vslm.ID, description: str) -> vslm.Task: ...
    def DeleteSnapshot(self, id: vim.vslm.ID, snapshotId: vim.vslm.ID) -> vslm.Task: ...
    def RetrieveSnapshotInfo(self, id: vim.vslm.ID) -> vim.vslm.VStorageObjectSnapshotInfo: ...
    def CreateDiskFromSnapshot(self, id: vim.vslm.ID, snapshotId: vim.vslm.ID, name: str, profile: List[vim.vm.ProfileSpec], crypto: vim.encryption.CryptoSpec, path: str) -> vslm.Task: ...
    def RevertVStorageObject(self, id: vim.vslm.ID, snapshotId: vim.vslm.ID) -> vslm.Task: ...
    def RetrieveSnapshotDetails(self, id: vim.vslm.ID, snapshotId: vim.vslm.ID) -> vim.vslm.VStorageObjectSnapshotDetails: ...
    def QueryChangedDiskAreas(self, id: vim.vslm.ID, snapshotId: vim.vslm.ID, startOffset: long, changeId: str) -> vim.VirtualMachine.DiskChangeInfo: ...
    def QueryGlobalCatalogSyncStatus(self) -> List[DatastoreSyncStatus]: ...
    def QueryGlobalCatalogSyncStatusForDatastore(self, datastoreURL: str) -> DatastoreSyncStatus: ...
    def UpdateVStorageObjectMetadata(self, id: vim.vslm.ID, metadata: List[vim.KeyValue], deleteKeys: List[str]) -> vslm.Task: ...
    def RetrieveVStorageObjectMetadata(self, id: vim.vslm.ID, snapshotId: vim.vslm.ID, prefix: str) -> List[vim.KeyValue]: ...
    def RetrieveVStorageObjectMetadataValue(self, id: vim.vslm.ID, snapshotId: vim.vslm.ID, key: str) -> str: ...
    def RetrieveVStorageObjects(self, ids: List[vim.vslm.ID]) -> List[VStorageObjectResult]: ...
    def AttachDisk(self, id: vim.vslm.ID, vm: vim.VirtualMachine, controllerKey: int, unitNumber: int) -> vslm.Task: ...


class DatastoreSyncStatus(vmodl.DynamicData):
    @property
    def datastoreURL(self) -> str: ...
    @datastoreURL.setter
    def datastoreURL(self, value: str):
        self._datastoreURL = value
    @property
    def objectVClock(self) -> long: ...
    @objectVClock.setter
    def objectVClock(self, value: long):
        self._objectVClock = value
    @property
    def syncVClock(self) -> long: ...
    @syncVClock.setter
    def syncVClock(self, value: long):
        self._syncVClock = value
    @property
    def syncTime(self) -> datetime: ...
    @syncTime.setter
    def syncTime(self, value: datetime):
        self._syncTime = value
    @property
    def numberOfRetries(self) -> int: ...
    @numberOfRetries.setter
    def numberOfRetries(self, value: int):
        self._numberOfRetries = value
    @property
    def error(self) -> vmodl.MethodFault: ...
    @error.setter
    def error(self, value: vmodl.MethodFault):
        self._error = value


class VStorageObjectAssociations(vmodl.DynamicData):
    @property
    def id(self) -> vim.vslm.ID: ...
    @id.setter
    def id(self, value: vim.vslm.ID):
        self._id = value
    @property
    def vmDiskAssociation(self) -> List[VStorageObjectAssociations.VmDiskAssociation]: ...
    @vmDiskAssociation.setter
    def vmDiskAssociation(self, value: List[VStorageObjectAssociations.VmDiskAssociation]):
        self._vmDiskAssociation = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


    class VmDiskAssociation(vmodl.DynamicData):
        @property
        def vmId(self) -> str: ...
        @vmId.setter
        def vmId(self, value: str):
            self._vmId = value
        @property
        def diskKey(self) -> int: ...
        @diskKey.setter
        def diskKey(self, value: int):
            self._diskKey = value


class VStorageObjectQueryResult(vmodl.DynamicData):
    @property
    def allRecordsReturned(self) -> bool: ...
    @allRecordsReturned.setter
    def allRecordsReturned(self, value: bool):
        self._allRecordsReturned = value
    @property
    def id(self) -> List[vim.vslm.ID]: ...
    @id.setter
    def id(self, value: List[vim.vslm.ID]):
        self._id = value
    @property
    def queryResults(self) -> List[VStorageObjectResult]: ...
    @queryResults.setter
    def queryResults(self, value: List[VStorageObjectResult]):
        self._queryResults = value


class VStorageObjectQuerySpec(vmodl.DynamicData):
    @property
    def queryField(self) -> str: ...
    @queryField.setter
    def queryField(self, value: str):
        self._queryField = value
    @property
    def queryOperator(self) -> str: ...
    @queryOperator.setter
    def queryOperator(self, value: str):
        self._queryOperator = value
    @property
    def queryValue(self) -> List[str]: ...
    @queryValue.setter
    def queryValue(self, value: List[str]):
        self._queryValue = value


    class QueryFieldEnum(Enum):
        id = "id"
        name = "name"
        capacity = "capacity"
        createTime = "createTime"
        backingObjectId = "backingObjectId"
        datastoreMoId = "datastoreMoId"
        metadataKey = "metadataKey"
        metadataValue = "metadataValue"


    class QueryOperatorEnum(Enum):
        equals = "equals"
        notEquals = "notEquals"
        lessThan = "lessThan"
        greaterThan = "greaterThan"
        lessThanOrEqual = "lessThanOrEqual"
        greaterThanOrEqual = "greaterThanOrEqual"
        contains = "contains"
        startsWith = "startsWith"
        endsWith = "endsWith"


class VStorageObjectResult(vmodl.DynamicData):
    @property
    def id(self) -> vim.vslm.ID: ...
    @id.setter
    def id(self, value: vim.vslm.ID):
        self._id = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def capacityInMB(self) -> long: ...
    @capacityInMB.setter
    def capacityInMB(self, value: long):
        self._capacityInMB = value
    @property
    def createTime(self) -> datetime: ...
    @createTime.setter
    def createTime(self, value: datetime):
        self._createTime = value
    @property
    def datastoreUrl(self) -> str: ...
    @datastoreUrl.setter
    def datastoreUrl(self, value: str):
        self._datastoreUrl = value
    @property
    def diskPath(self) -> str: ...
    @diskPath.setter
    def diskPath(self, value: str):
        self._diskPath = value
    @property
    def usedCapacityInMB(self) -> long: ...
    @usedCapacityInMB.setter
    def usedCapacityInMB(self, value: long):
        self._usedCapacityInMB = value
    @property
    def backingObjectId(self) -> vim.vslm.ID: ...
    @backingObjectId.setter
    def backingObjectId(self, value: vim.vslm.ID):
        self._backingObjectId = value
    @property
    def snapshotInfo(self) -> List[VStorageObjectSnapshotResult]: ...
    @snapshotInfo.setter
    def snapshotInfo(self, value: List[VStorageObjectSnapshotResult]):
        self._snapshotInfo = value
    @property
    def metadata(self) -> List[vim.KeyValue]: ...
    @metadata.setter
    def metadata(self, value: List[vim.KeyValue]):
        self._metadata = value
    @property
    def error(self) -> vmodl.MethodFault: ...
    @error.setter
    def error(self, value: vmodl.MethodFault):
        self._error = value


class VStorageObjectSnapshotResult(vmodl.DynamicData):
    @property
    def backingObjectId(self) -> vim.vslm.ID: ...
    @backingObjectId.setter
    def backingObjectId(self, value: vim.vslm.ID):
        self._backingObjectId = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def snapshotId(self) -> vim.vslm.ID: ...
    @snapshotId.setter
    def snapshotId(self, value: vim.vslm.ID):
        self._snapshotId = value
    @property
    def diskPath(self) -> str: ...
    @diskPath.setter
    def diskPath(self, value: str):
        self._diskPath = value