# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.encryption
import pyVmomi.vim.vm
import pyVmomi.vim.vslm



class DatastoreSyncStatus(pyVmomi.vmodl.DynamicData):
   datastoreURL: str
   objectVClock: pyVmomi.VmomiSupport.long
   syncVClock: pyVmomi.VmomiSupport.long
   syncTime: _typing.Optional[_datetime.datetime] = None
   numberOfRetries: _typing.Optional[int] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VStorageObjectAssociations(pyVmomi.vmodl.DynamicData):
   class VmDiskAssociation(pyVmomi.vmodl.DynamicData):
      vmId: str
      diskKey: int

   id: pyVmomi.vim.vslm.ID
   vmDiskAssociation: list[VmDiskAssociation] = []
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VStorageObjectManager(pyVmomi.VmomiSupport.ManagedObject):
   def CreateDisk(self, spec: pyVmomi.vim.vslm.CreateSpec) -> pyVmomi.vim.Task: ...
   def RegisterDisk(self, path: str, name: _typing.Optional[str]) -> pyVmomi.vim.vslm.VStorageObject: ...
   def ExtendDisk(self, id: pyVmomi.vim.vslm.ID, newCapacityInMB: pyVmomi.VmomiSupport.long) -> pyVmomi.vim.Task: ...
   def InflateDisk(self, id: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.Task: ...
   def RenameVStorageObject(self, id: pyVmomi.vim.vslm.ID, name: str) -> None: ...
   def UpdateVStorageObjectPolicy(self, id: pyVmomi.vim.vslm.ID, profile: list[pyVmomi.vim.vm.ProfileSpec]) -> pyVmomi.vim.Task: ...
   def UpdateVStorageObjectCrypto(self, id: pyVmomi.vim.vslm.ID, profile: list[pyVmomi.vim.vm.ProfileSpec], disksCrypto: _typing.Optional[pyVmomi.vim.vslm.DiskCryptoSpec]) -> pyVmomi.vim.Task: ...
   def UpdateVStorageInfrastructureObjectPolicy(self, spec: pyVmomi.vim.vslm.InfrastructureObjectPolicySpec) -> pyVmomi.vim.Task: ...
   def RetrieveVStorageInfrastructureObjectPolicy(self, datastore: pyVmomi.vim.Datastore) -> list[pyVmomi.vim.vslm.InfrastructureObjectPolicy]: ...
   def DeleteVStorageObject(self, id: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.Task: ...
   def RetrieveVStorageObject(self, id: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.vslm.VStorageObject: ...
   def RetrieveVStorageObjectState(self, id: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.vslm.StateInfo: ...
   def RetrieveVStorageObjectAssociations(self, ids: list[pyVmomi.vim.vslm.ID]) -> list[VStorageObjectAssociations]: ...
   def ListVStorageObjectsForSpec(self, query: list[VStorageObjectQuerySpec], maxResult: int) -> _typing.Optional[VStorageObjectQueryResult]: ...
   def CloneVStorageObject(self, id: pyVmomi.vim.vslm.ID, spec: pyVmomi.vim.vslm.CloneSpec) -> pyVmomi.vim.Task: ...
   def RelocateVStorageObject(self, id: pyVmomi.vim.vslm.ID, spec: pyVmomi.vim.vslm.RelocateSpec) -> pyVmomi.vim.Task: ...
   def SetVStorageObjectControlFlags(self, id: pyVmomi.vim.vslm.ID, controlFlags: list[str]) -> None: ...
   def ClearVStorageObjectControlFlags(self, id: pyVmomi.vim.vslm.ID, controlFlags: list[str]) -> None: ...
   def AttachTagToVStorageObject(self, id: pyVmomi.vim.vslm.ID, category: str, tag: str) -> None: ...
   def DetachTagFromVStorageObject(self, id: pyVmomi.vim.vslm.ID, category: str, tag: str) -> None: ...
   def ListVStorageObjectsAttachedToTag(self, category: str, tag: str) -> list[pyVmomi.vim.vslm.ID]: ...
   def ListTagsAttachedToVStorageObject(self, id: pyVmomi.vim.vslm.ID) -> list[pyVmomi.vim.vslm.TagEntry]: ...
   def ReconcileDatastoreInventory(self, datastore: pyVmomi.vim.Datastore) -> pyVmomi.vim.Task: ...
   def ScheduleReconcileDatastoreInventory(self, datastore: pyVmomi.vim.Datastore) -> None: ...
   def CreateSnapshot(self, id: pyVmomi.vim.vslm.ID, description: str) -> pyVmomi.vim.Task: ...
   def DeleteSnapshot(self, id: pyVmomi.vim.vslm.ID, snapshotId: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.Task: ...
   def RetrieveSnapshotInfo(self, id: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.vslm.VStorageObjectSnapshotInfo: ...
   def CreateDiskFromSnapshot(self, id: pyVmomi.vim.vslm.ID, snapshotId: pyVmomi.vim.vslm.ID, name: str, profile: list[pyVmomi.vim.vm.ProfileSpec], crypto: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec], path: _typing.Optional[str]) -> pyVmomi.vim.Task: ...
   def RevertVStorageObject(self, id: pyVmomi.vim.vslm.ID, snapshotId: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.Task: ...
   def RetrieveSnapshotDetails(self, id: pyVmomi.vim.vslm.ID, snapshotId: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.vslm.VStorageObjectSnapshotDetails: ...
   def QueryChangedDiskAreas(self, id: pyVmomi.vim.vslm.ID, snapshotId: pyVmomi.vim.vslm.ID, startOffset: pyVmomi.VmomiSupport.long, changeId: str) -> pyVmomi.vim.VirtualMachine.DiskChangeInfo: ...
   def QueryGlobalCatalogSyncStatus(self) -> list[DatastoreSyncStatus]: ...
   def QueryGlobalCatalogSyncStatusForDatastore(self, datastoreURL: str) -> _typing.Optional[DatastoreSyncStatus]: ...
   def UpdateVStorageObjectMetadata(self, id: pyVmomi.vim.vslm.ID, metadata: list[pyVmomi.vim.KeyValue], deleteKeys: list[str]) -> pyVmomi.vim.Task: ...
   def RetrieveVStorageObjectMetadata(self, id: pyVmomi.vim.vslm.ID, snapshotId: _typing.Optional[pyVmomi.vim.vslm.ID], prefix: _typing.Optional[str]) -> list[pyVmomi.vim.KeyValue]: ...
   def RetrieveVStorageObjectMetadataValue(self, id: pyVmomi.vim.vslm.ID, snapshotId: _typing.Optional[pyVmomi.vim.vslm.ID], key: str) -> str: ...
   def RetrieveVStorageObjects(self, ids: list[pyVmomi.vim.vslm.ID]) -> list[VStorageObjectResult]: ...
   def AttachDisk(self, id: pyVmomi.vim.vslm.ID, vm: pyVmomi.vim.VirtualMachine, controllerKey: _typing.Optional[int], unitNumber: _typing.Optional[int]) -> pyVmomi.vim.Task: ...


class VStorageObjectQueryResult(pyVmomi.vmodl.DynamicData):
   allRecordsReturned: bool
   id: list[pyVmomi.vim.vslm.ID] = []
   queryResults: list[VStorageObjectResult] = []


class VStorageObjectQuerySpec(pyVmomi.vmodl.DynamicData):
   class QueryOperatorEnum(pyVmomi.VmomiSupport.Enum):
      equals: _typing.ClassVar['QueryOperatorEnum'] = 'equals'
      notEquals: _typing.ClassVar['QueryOperatorEnum'] = 'notEquals'
      lessThan: _typing.ClassVar['QueryOperatorEnum'] = 'lessThan'
      greaterThan: _typing.ClassVar['QueryOperatorEnum'] = 'greaterThan'
      lessThanOrEqual: _typing.ClassVar['QueryOperatorEnum'] = 'lessThanOrEqual'
      greaterThanOrEqual: _typing.ClassVar['QueryOperatorEnum'] = 'greaterThanOrEqual'
      contains: _typing.ClassVar['QueryOperatorEnum'] = 'contains'
      startsWith: _typing.ClassVar['QueryOperatorEnum'] = 'startsWith'
      endsWith: _typing.ClassVar['QueryOperatorEnum'] = 'endsWith'

   class QueryFieldEnum(pyVmomi.VmomiSupport.Enum):
      id: _typing.ClassVar['QueryFieldEnum'] = 'id'
      name: _typing.ClassVar['QueryFieldEnum'] = 'name'
      capacity: _typing.ClassVar['QueryFieldEnum'] = 'capacity'
      createTime: _typing.ClassVar['QueryFieldEnum'] = 'createTime'
      backingObjectId: _typing.ClassVar['QueryFieldEnum'] = 'backingObjectId'
      datastoreMoId: _typing.ClassVar['QueryFieldEnum'] = 'datastoreMoId'
      metadataKey: _typing.ClassVar['QueryFieldEnum'] = 'metadataKey'
      metadataValue: _typing.ClassVar['QueryFieldEnum'] = 'metadataValue'

   queryField: str
   queryOperator: str
   queryValue: list[str] = []


class VStorageObjectResult(pyVmomi.vmodl.DynamicData):
   id: pyVmomi.vim.vslm.ID
   name: _typing.Optional[str] = None
   capacityInMB: pyVmomi.VmomiSupport.long
   createTime: _typing.Optional[_datetime.datetime] = None
   datastoreUrl: _typing.Optional[str] = None
   diskPath: _typing.Optional[str] = None
   usedCapacityInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   backingObjectId: _typing.Optional[pyVmomi.vim.vslm.ID] = None
   snapshotInfo: list[VStorageObjectSnapshotResult] = []
   metadata: list[pyVmomi.vim.KeyValue] = []
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VStorageObjectSnapshotResult(pyVmomi.vmodl.DynamicData):
   backingObjectId: pyVmomi.vim.vslm.ID
   description: _typing.Optional[str] = None
   snapshotId: _typing.Optional[pyVmomi.vim.vslm.ID] = None
   diskPath: _typing.Optional[str] = None
