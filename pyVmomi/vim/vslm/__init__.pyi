# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import host as host
from . import vcenter as vcenter

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.encryption
import pyVmomi.vim.vm



class BaseConfigInfo(pyVmomi.vmodl.DynamicData):
   class BackingInfo(pyVmomi.vmodl.DynamicData):
      datastore: pyVmomi.vim.Datastore

   class FileBackingInfo(BackingInfo):
      filePath: str
      backingObjectId: _typing.Optional[str] = None
      parent: _typing.Optional[FileBackingInfo] = None
      deltaSizeInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None
      sharedFileBacking: _typing.Optional[bool] = None

   class DiskFileBackingInfo(FileBackingInfo):
      class ProvisioningType(pyVmomi.VmomiSupport.Enum):
         thin: _typing.ClassVar['ProvisioningType'] = 'thin'
         eagerZeroedThick: _typing.ClassVar['ProvisioningType'] = 'eagerZeroedThick'
         lazyZeroedThick: _typing.ClassVar['ProvisioningType'] = 'lazyZeroedThick'

      provisioningType: str

   class RawDiskMappingBackingInfo(FileBackingInfo):
      lunUuid: str
      compatibilityMode: str

   id: ID
   name: str
   createTime: _datetime.datetime
   keepAfterDeleteVm: _typing.Optional[bool] = None
   relocationDisabled: _typing.Optional[bool] = None
   nativeSnapshotSupported: _typing.Optional[bool] = None
   changedBlockTrackingEnabled: _typing.Optional[bool] = None
   backing: BackingInfo
   metadata: list[pyVmomi.vim.KeyValue] = []
   vclock: _typing.Optional[VClockInfo] = None
   iofilter: list[str] = []


class CloneSpec(MigrateSpec):
   name: str
   keepAfterDeleteVm: _typing.Optional[bool] = None
   metadata: list[pyVmomi.vim.KeyValue] = []


class CreateSpec(pyVmomi.vmodl.DynamicData):
   class BackingSpec(pyVmomi.vmodl.DynamicData):
      datastore: pyVmomi.vim.Datastore
      path: _typing.Optional[str] = None

   class DiskFileBackingSpec(BackingSpec):
      provisioningType: _typing.Optional[str] = None

   class RawDiskMappingBackingSpec(BackingSpec):
      lunUuid: str
      compatibilityMode: str

   id: _typing.Optional[ID] = None
   name: str
   keepAfterDeleteVm: _typing.Optional[bool] = None
   backingSpec: BackingSpec
   capacityInMB: pyVmomi.VmomiSupport.long
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []
   crypto: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None
   metadata: list[pyVmomi.vim.KeyValue] = []


class DiskCryptoSpec(pyVmomi.vmodl.DynamicData):
   parent: _typing.Optional[DiskCryptoSpec] = None
   crypto: pyVmomi.vim.encryption.CryptoSpec

class DiskInfoFlag:
   pass


class ID(pyVmomi.vmodl.DynamicData):
   id: str


class InfrastructureObjectPolicy(pyVmomi.vmodl.DynamicData):
   name: str
   backingObjectId: str
   profileId: str
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class InfrastructureObjectPolicySpec(pyVmomi.vmodl.DynamicData):
   datastore: pyVmomi.vim.Datastore
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []


class MigrateSpec(pyVmomi.vmodl.DynamicData):
   backingSpec: CreateSpec.BackingSpec
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []
   consolidate: _typing.Optional[bool] = None
   disksCrypto: _typing.Optional[DiskCryptoSpec] = None
   service: _typing.Optional[pyVmomi.vim.ServiceLocator] = None


class ReconcileResult(pyVmomi.vmodl.DynamicData):
   class InvalidDiskPath(pyVmomi.vmodl.DynamicData):
      path: str
      reason: str

   class ReconcileDetail(pyVmomi.vmodl.DynamicData):
      hostName: _typing.Optional[str] = None
      reconcileReportPath: _typing.Optional[str] = None
      isReconciled: _typing.Optional[bool] = None
      isDeepScanned: _typing.Optional[bool] = None
      numberOfReconcileIssues: _typing.Optional[int] = None
      numberOfFcdsBeforeReconcile: _typing.Optional[int] = None
      numberOfFcdsAfterReconcile: _typing.Optional[int] = None
      invalidDiskPaths: list[InvalidDiskPath] = []

   reconcileDetails: list[ReconcileDetail] = []


class ReconcileSpec(pyVmomi.vmodl.DynamicData):
   datastore: pyVmomi.vim.Datastore
   includeDiskPaths: list[str] = []
   excludeDiskPaths: list[str] = []
   deepScan: _typing.Optional[bool] = None
   dryRun: _typing.Optional[bool] = None
   generateReport: _typing.Optional[int] = None

class RelocateSpec(MigrateSpec):
   pass


class StateInfo(pyVmomi.vmodl.DynamicData):
   tentative: _typing.Optional[bool] = None


class TagEntry(pyVmomi.vmodl.DynamicData):
   tagName: str
   parentCategoryName: str


class VClockInfo(pyVmomi.vmodl.DynamicData):
   vClockTime: pyVmomi.VmomiSupport.long


class VStorageObject(pyVmomi.vmodl.DynamicData):
   class ConsumptionType(pyVmomi.VmomiSupport.Enum):
      disk: _typing.ClassVar['ConsumptionType'] = 'disk'

   class ConfigInfo(BaseConfigInfo):
      descriptorVersion: _typing.Optional[int] = None
      capacityInMB: pyVmomi.VmomiSupport.long
      consumptionType: list[str] = []
      consumerId: list[ID] = []
      virtualDiskFormat: _typing.Optional[str] = None
      linkedCloneBasePath: _typing.Optional[str] = None
      linkedCloneParentId: _typing.Optional[ID] = None

   config: ConfigInfo


class VStorageObjectAttachResult(pyVmomi.vmodl.DynamicData):
   volumeId: ID
   diskUUID: _typing.Optional[str] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VStorageObjectAttachSpec(pyVmomi.vmodl.DynamicData):
   volumeId: ID
   datastore: pyVmomi.vim.Datastore
   diskMode: _typing.Optional[str] = None
   sharing: _typing.Optional[str] = None
   controllerKey: _typing.Optional[int] = None
   unitNumber: _typing.Optional[int] = None

class VStorageObjectControlFlag:
   pass


class VStorageObjectManagerBase(pyVmomi.VmomiSupport.ManagedObject):
   def ExtendDiskEx(self, id: ID, datastore: pyVmomi.vim.Datastore, newCapacityInMB: pyVmomi.VmomiSupport.long) -> pyVmomi.vim.Task: ...
   def RenameVStorageObjectEx(self, id: ID, datastore: pyVmomi.vim.Datastore, name: str) -> VClockInfo: ...
   def CreateSnapshotEx(self, id: ID, datastore: pyVmomi.vim.Datastore, description: str, snapshotId: _typing.Optional[ID]) -> pyVmomi.vim.Task: ...
   def DeleteSnapshotEx(self, id: ID, datastore: pyVmomi.vim.Datastore, snapshotId: ID) -> pyVmomi.vim.Task: ...
   def DeleteSnapshotEx2(self, id: ID, datastore: pyVmomi.vim.Datastore, snapshotId: ID) -> pyVmomi.vim.Task: ...
   def RevertVStorageObjectEx(self, id: ID, datastore: pyVmomi.vim.Datastore, snapshotId: ID) -> pyVmomi.vim.Task: ...
   def RepairDiskChain(self, id: ID, datastore: pyVmomi.vim.Datastore) -> pyVmomi.vim.Task: ...
   def UnregisterDisk(self, id: ID, datastore: pyVmomi.vim.Datastore) -> pyVmomi.vim.Task: ...


class VStorageObjectSnapshot(pyVmomi.vmodl.DynamicData):
   id: ID
   vclock: VClockInfo
   usedCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VStorageObjectSnapshotDetails(pyVmomi.vmodl.DynamicData):
   path: _typing.Optional[str] = None
   changedBlockTrackingId: _typing.Optional[str] = None


class VStorageObjectSnapshotInfo(pyVmomi.vmodl.DynamicData):
   class VStorageObjectSnapshot(pyVmomi.vmodl.DynamicData):
      id: _typing.Optional[ID] = None
      backingObjectId: _typing.Optional[str] = None
      createTime: _datetime.datetime
      description: str

   snapshots: list[VStorageObjectSnapshot] = []
