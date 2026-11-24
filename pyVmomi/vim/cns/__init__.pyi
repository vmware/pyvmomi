# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.encryption
import pyVmomi.vim.vm
import pyVmomi.vim.vsan
import pyVmomi.vim.vslm



class AccessControlSpec(pyVmomi.vmodl.DynamicData):
   pass


class AsyncQueryResult(VolumeOperationResult):
   queryResult: _typing.Optional[QueryResult] = None


class BackingObjectDetails(pyVmomi.vmodl.DynamicData):
   capacityInMb: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class BaseCreateSpec(pyVmomi.vmodl.DynamicData):
   pass


class BlockBackingDetails(BackingObjectDetails):
   backingDiskId: _typing.Optional[str] = None
   backingDiskUrlPath: _typing.Optional[str] = None
   backingDiskPath: _typing.Optional[str] = None
   backingDiskObjectId: _typing.Optional[str] = None
   usedCapacityInMb: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   aggregatedSnapshotCapacityInMb: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class BlockCreateSpec(BaseCreateSpec):
   cryptoSpec: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None

class BlockVolumeRelocateSpec(VolumeRelocateSpec):
   pass


class CloneVolumeSource(VolumeSource):
   volumeId: VolumeId
   keepAfterDeleteVm: _typing.Optional[bool] = None

class ClusterFlavor:
   pass

class ClusterType:
   pass


class ContainerCluster(pyVmomi.vmodl.DynamicData):
   clusterType: str
   clusterId: str
   vSphereUser: str
   clusterFlavor: _typing.Optional[str] = None
   clusterDistribution: _typing.Optional[str] = None
   delete: _typing.Optional[bool] = None


class Cursor(pyVmomi.vmodl.DynamicData):
   offset: pyVmomi.VmomiSupport.long
   limit: pyVmomi.VmomiSupport.long
   totalRecords: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class EntityMetadata(pyVmomi.vmodl.DynamicData):
   entityName: str
   labels: list[pyVmomi.vim.KeyValue] = []
   delete: _typing.Optional[bool] = None
   clusterId: _typing.Optional[str] = None


class FileBackingDetails(BackingObjectDetails):
   backingFileId: _typing.Optional[str] = None

class FileCreateSpec(BaseCreateSpec):
   pass


class KubernetesEntityMetadata(EntityMetadata):
   entityType: str
   namespace: _typing.Optional[str] = None
   referredEntity: list[KubernetesEntityReference] = []


class KubernetesEntityReference(pyVmomi.vmodl.DynamicData):
   entityType: str
   entityName: str
   namespace: _typing.Optional[str] = None
   clusterId: _typing.Optional[str] = None

class KubernetesEntityType:
   pass


class KubernetesQueryFilter(QueryFilter):
   namespaces: list[str] = []
   podNames: list[str] = []
   pvcNames: list[str] = []
   pvNames: list[str] = []

class MetricFormat:
   pass

class MetricType:
   pass


class NFSAccessControlSpec(AccessControlSpec):
   netPermission: pyVmomi.vim.vsan.FileShareNetPermission
   delete: _typing.Optional[bool] = None


class PlacementResult(pyVmomi.vmodl.DynamicData):
   datastore: pyVmomi.vim.Datastore
   placementFaults: list[pyVmomi.vmodl.MethodFault] = []
   clusters: list[pyVmomi.vim.ClusterComputeResource] = []


class QueryFilter(pyVmomi.vmodl.DynamicData):
   volumeIds: list[VolumeId] = []
   names: list[str] = []
   containerClusterIds: list[str] = []
   storagePolicyId: _typing.Optional[str] = None
   datastores: list[pyVmomi.vim.Datastore] = []
   labels: list[pyVmomi.vim.KeyValue] = []
   complianceStatus: _typing.Optional[str] = None
   datastoreAccessibilityStatus: _typing.Optional[str] = None
   cursor: _typing.Optional[Cursor] = None
   healthStatus: _typing.Optional[str] = None


class QueryResult(pyVmomi.vmodl.DynamicData):
   volumes: list[Volume] = []
   cursor: Cursor


class QuerySelection(pyVmomi.vmodl.DynamicData):
   names: list[str] = []

class QuerySelectionNameType:
   pass


class SnapshotCreateSpec(pyVmomi.vmodl.DynamicData):
   volumeId: VolumeId
   description: str
   snapshotId: _typing.Optional[SnapshotId] = None


class SnapshotDeleteSpec(pyVmomi.vmodl.DynamicData):
   volumeId: VolumeId
   snapshotId: SnapshotId


class SnapshotId(pyVmomi.vmodl.DynamicData):
   id: str


class SnapshotVolumeSource(VolumeSource):
   volumeId: _typing.Optional[VolumeId] = None
   snapshotId: _typing.Optional[SnapshotId] = None
   linkedClone: _typing.Optional[bool] = None

class SyncVolumeMode:
   pass


class SyncVolumeSpec(pyVmomi.vmodl.DynamicData):
   volumeId: VolumeId
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None
   syncMode: list[str] = []

class UnregisterTargetVolumeType:
   pass


class UnregisterVolumeSpec(pyVmomi.vmodl.DynamicData):
   volumeId: VolumeId
   targetVolumeType: str


class VSANFileCreateSpec(FileCreateSpec):
   softQuotaInMb: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   permission: list[pyVmomi.vim.vsan.FileShareNetPermission] = []


class Volume(pyVmomi.vmodl.DynamicData):
   volumeId: VolumeId
   datastoreUrl: _typing.Optional[str] = None
   name: _typing.Optional[str] = None
   volumeType: _typing.Optional[str] = None
   storagePolicyId: _typing.Optional[str] = None
   metadata: _typing.Optional[VolumeMetadata] = None
   backingObjectDetails: _typing.Optional[BackingObjectDetails] = None
   complianceStatus: _typing.Optional[str] = None
   datastoreAccessibilityStatus: _typing.Optional[str] = None
   healthStatus: _typing.Optional[str] = None


class VolumeACLConfigureSpec(pyVmomi.vmodl.DynamicData):
   volumeId: VolumeId
   accessControlSpecList: list[AccessControlSpec] = []


class VolumeAttachDetachSpec(pyVmomi.vmodl.DynamicData):
   volumeId: VolumeId
   vm: pyVmomi.vim.VirtualMachine
   diskMode: _typing.Optional[str] = None
   sharing: _typing.Optional[str] = None
   controllerKey: _typing.Optional[int] = None
   unitNumber: _typing.Optional[int] = None
   backingTypeName: _typing.Optional[str] = None
   volumeEncrypted: _typing.Optional[bool] = None


class VolumeAttachResult(VolumeOperationResult):
   diskUUID: _typing.Optional[str] = None

class VolumeBackingType:
   pass


class VolumeCreateResult(VolumeOperationResult):
   name: _typing.Optional[str] = None
   placementResults: list[PlacementResult] = []


class VolumeCreateSpec(pyVmomi.vmodl.DynamicData):
   name: str
   volumeType: str
   volumeId: _typing.Optional[VolumeId] = None
   datastores: list[pyVmomi.vim.Datastore] = []
   metadata: _typing.Optional[VolumeMetadata] = None
   backingObjectDetails: BackingObjectDetails
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []
   activeClusters: list[pyVmomi.vim.ClusterComputeResource] = []
   createSpec: _typing.Optional[BaseCreateSpec] = None
   volumeSource: _typing.Optional[VolumeSource] = None


class VolumeCryptoUpdateSpec(pyVmomi.vmodl.DynamicData):
   volumeId: VolumeId
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []
   disksCrypto: _typing.Optional[pyVmomi.vim.vslm.DiskCryptoSpec] = None


class VolumeExtendSpec(pyVmomi.vmodl.DynamicData):
   volumeId: VolumeId
   capacityInMb: pyVmomi.VmomiSupport.long


class VolumeId(pyVmomi.vmodl.DynamicData):
   id: str


class VolumeManager(pyVmomi.VmomiSupport.ManagedObject):
   def Create(self, createSpecs: list[VolumeCreateSpec]) -> pyVmomi.vim.Task: ...
   def UpdateVolumeMetadata(self, updateSpecs: list[VolumeMetadataUpdateSpec]) -> pyVmomi.vim.Task: ...
   def Delete(self, volumeIds: list[VolumeId], deleteDisk: bool) -> pyVmomi.vim.Task: ...
   def Attach(self, attachSpecs: list[VolumeAttachDetachSpec]) -> pyVmomi.vim.Task: ...
   def Detach(self, detachSpecs: list[VolumeAttachDetachSpec]) -> pyVmomi.vim.Task: ...
   def QueryAsync(self, filter: QueryFilter, selection: _typing.Optional[QuerySelection]) -> pyVmomi.vim.Task: ...
   def Query(self, filter: QueryFilter, selection: _typing.Optional[QuerySelection]) -> QueryResult: ...
   def ConfigureVolumeACLs(self, ACLConfigSpecs: list[VolumeACLConfigureSpec]) -> pyVmomi.vim.Task: ...
   def Extend(self, extendSpecs: list[VolumeExtendSpec]) -> pyVmomi.vim.Task: ...
   def CreateSnapshots(self, snapshotSpecs: list[SnapshotCreateSpec]) -> pyVmomi.vim.Task: ...
   def DeleteSnapshots(self, snapshotDeleteSpecs: list[SnapshotDeleteSpec]) -> pyVmomi.vim.Task: ...
   def Relocate(self, relocateSpecs: list[VolumeRelocateSpec]) -> pyVmomi.vim.Task: ...
   def ReconfigPolicy(self, volumePolicyReconfigSpecs: list[VolumePolicyReconfigSpec]) -> pyVmomi.vim.Task: ...
   def UpdateVolumeCrypto(self, updateSpecs: list[VolumeCryptoUpdateSpec]) -> pyVmomi.vim.Task: ...
   def UnregisterVolume(self, unregisterSpec: list[UnregisterVolumeSpec]) -> pyVmomi.vim.Task: ...
   def SyncVolume(self, syncSpecs: list[SyncVolumeSpec]) -> pyVmomi.vim.Task: ...


class VolumeMetadata(pyVmomi.vmodl.DynamicData):
   containerCluster: ContainerCluster
   entityMetadata: list[EntityMetadata] = []
   containerClusterArray: list[ContainerCluster] = []


class VolumeMetadataUpdateSpec(pyVmomi.vmodl.DynamicData):
   volumeId: VolumeId
   metadata: VolumeMetadata


class VolumeOperationBatchResult(pyVmomi.vmodl.DynamicData):
   volumeResults: list[VolumeOperationResult] = []


class VolumeOperationResult(pyVmomi.vmodl.DynamicData):
   volumeId: _typing.Optional[VolumeId] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VolumePolicyReconfigSpec(pyVmomi.vmodl.DynamicData):
   volumeId: VolumeId
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []


class VolumeRelocateSpec(pyVmomi.vmodl.DynamicData):
   volumeId: VolumeId
   datastore: pyVmomi.vim.Datastore
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []


class VolumeSource(pyVmomi.vmodl.DynamicData):
   pass

class VolumeType:
   pass


class VsanFileShareBackingDetails(FileBackingDetails):
   name: _typing.Optional[str] = None
   accessPoints: list[pyVmomi.vim.KeyValue] = []
   permission: list[pyVmomi.vim.vsan.FileShareNetPermission] = []
