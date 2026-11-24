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
   """
   This data object type contains the basic configuration for
   a virtual storage object or a virtual storage object snapshot.
   
   Attributes:
       id: ID of this object.
       name: Descriptive name of this object.
       createTime: The date and time this object was created.
       keepAfterDeleteVm: Choice of the deletion behavior of this virtual storage object.
           
           If not set, the default value is false.
       relocationDisabled: Is virtual storage object relocation disabled.
           
           If not set, the default value is false.
       nativeSnapshotSupported: Is virtual storage object supports native snapshot.
           
           If not set, the default value is false.
       changedBlockTrackingEnabled: If Virtual storage object has changed block tracking enabled.
           
           If not set, the default value is false.
       backing: Backing of this object.
       metadata: Metadata associated with the FCD if available.
           
           Since: vSphere API Release 7.0.2.0
       vclock: VClock associated with the fcd when the operation completed.
           
           The files is unset if the operation is a retrieve.
           
           Since: vSphere API Release 7.0.2.0
       iofilter: IDs of the IO Filters associated with the virtual disk.
           
           See `pyVmomi.vim.IoFilterManager.IoFilterInfo.id`.
           The client cannot modify this information on a virtual machine.
   """
   class BackingInfo(pyVmomi.vmodl.DynamicData):
      """
      The data object type is a base type of backing of a virtual
      storage object.
      
      Attributes:
          datastore: The datastore managed object where this backing is located.
      """
      datastore: pyVmomi.vim.Datastore

   class FileBackingInfo(BaseConfigInfo.BackingInfo):
      """
      Information for file backing of a virtual storage
      object.
      
      File backing is mainly used for virtual disks.
      
      Attributes:
          filePath: Full file path for the host file used in this backing.
          backingObjectId: Id refers to the backed storage object where the virtual storage object
              is backed on.
          parent: The parent of this virtual disk file, if this is a delta disk backing.
              
              This will be unset if this is the root disk backing.
              
              Note that the type of the backing is consistent throughout the chain;
              any new delta disk backing which is added is of the same type as the
              original disk. Also note that since the parent backing is not being
              written to, it is possible that the parent backing may be shared among
              multiple disks.
              
              Only raw disk mappings in
              `virtualMode` can have parents.
          deltaSizeInMB: Size allocated by the FS for this file/chain/link/extent only.
              
              This property is used only for a delta disk whose
              `pyVmomi.vim.vslm.BaseConfigInfo.FileBackingInfo.parent` is set.
          keyId: key id used to encrypt the backing disk.
          sharedFileBacking: Flag indicates whether the file backing is shared across
              multiple fcd disk chains.
              
              This flag is intended for internal use only and is
              primarily used in the relocation and deletion workflow.
              
              Since: vSphere API Release 9.1.0.0
      """
      filePath: str
      backingObjectId: _typing.Optional[str] = None
      parent: _typing.Optional[BaseConfigInfo.FileBackingInfo] = None
      deltaSizeInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None
      sharedFileBacking: _typing.Optional[bool] = None

   class DiskFileBackingInfo(BaseConfigInfo.FileBackingInfo):
      """
      The data object type for disk file backing of a virtual storage
      object.
      
      Disk file backing provides full virtualization of the backend
      storage.
      
      Attributes:
          provisioningType: Provisioning type.
              
              See `pyVmomi.vim.vslm.BaseConfigInfo.DiskFileBackingInfo.ProvisioningType` for the
              supported types.
      """
      class ProvisioningType(pyVmomi.VmomiSupport.Enum):
         """
         Provisioning type constants.
         
         Attributes:
             thin: Space required for thin-provisioned virtual disk is allocated
                 and zeroed on demand as the space is used.
             eagerZeroedThick: An eager zeroed thick virtual disk has all space allocated and
                 wiped clean of any previous contents on the physical media at
                 creation time.
                 
                 Such virtual disk may take longer time
                 during creation compared to other provisioning formats.
             lazyZeroedThick: A thick virtual disk has all space allocated at creation time.
                 
                 This space may contain stale data on the physical media.
         """
         thin: _typing.ClassVar['BaseConfigInfo.DiskFileBackingInfo.ProvisioningType'] = 'thin'
         eagerZeroedThick: _typing.ClassVar['BaseConfigInfo.DiskFileBackingInfo.ProvisioningType'] = 'eagerZeroedThick'
         lazyZeroedThick: _typing.ClassVar['BaseConfigInfo.DiskFileBackingInfo.ProvisioningType'] = 'lazyZeroedThick'

      provisioningType: str

   class RawDiskMappingBackingInfo(BaseConfigInfo.FileBackingInfo):
      """
      This data object type contains information about raw device mapping.
      
      Attributes:
          lunUuid: Unique identifier of the LUN accessed by the raw disk mapping.
          compatibilityMode: The compatibility mode of the raw disk mapping (RDM).
              
              This must be
              specified when a new virtual disk with an RDM backing is created.
      """
      lunUuid: str
      compatibilityMode: str

   id: ID
   name: str
   createTime: _datetime.datetime
   keepAfterDeleteVm: _typing.Optional[bool] = None
   relocationDisabled: _typing.Optional[bool] = None
   nativeSnapshotSupported: _typing.Optional[bool] = None
   changedBlockTrackingEnabled: _typing.Optional[bool] = None
   backing: BaseConfigInfo.BackingInfo
   metadata: list[pyVmomi.vim.KeyValue] = []
   vclock: _typing.Optional[VClockInfo] = None
   iofilter: list[str] = []


class MigrateSpec(pyVmomi.vmodl.DynamicData):
   """
   Base specification of moving or copying a virtual storage object.
   
   Attributes:
       backingSpec: Specification of the backings of the target virtual storage object.
       profile: Virtual storage object Profile requirement.
           
           If unset,
           the default behavior will apply.
       consolidate: Flag indicates any delta disk backings will be consolidated
           during clone/migration.
           
           Cloning of linked clone disks always require consolidation.
       disksCrypto: Disk chain crypto information.
           
           If unset and if `pyVmomi.vim.vslm.MigrateSpec.profile` contains an encryption iofilter and if
           source VStorageObject is unencrypted, then disksCrypto will be of type
           CryptoSpecEncrypt, and filled with keyId that is automatically generated
           and keyProviderId that is the default kms cluster. During the migration,
           the object will be encrypted.
           If unset and if `pyVmomi.vim.vslm.MigrateSpec.profile` is a default policy and if source
           VStorageObject is unenrypted, then disksCrypto is treated as
           CryptoSpecNoOp. During migration, no cryptographic change.
           If unset and if `pyVmomi.vim.vslm.MigrateSpec.profile` contains an encryption iofilter and if
           source VStorageObject is encrypted, then disksCrypto is treated as
           CryptoSpecNoOp. During migration, no cryptographic change.
           If unset and if `pyVmomi.vim.vslm.MigrateSpec.profile` is a default policy and if
           source VStorageObject is encrypted, then disksCrypto is treated as
           CryptoSpecDecrypt, during migration, the object will be decrypted.
           To recrypt the disk during migration, disksCrypto has to be present.
       service: The service endpoint of vCenter where the FCD should be located.
           
           If
           not specified the current vCenter service is used.
           
           Since: vSphere API Release 8.0.3.0
   """
   backingSpec: CreateSpec.BackingSpec
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []
   consolidate: _typing.Optional[bool] = None
   disksCrypto: _typing.Optional[DiskCryptoSpec] = None
   service: _typing.Optional[pyVmomi.vim.ServiceLocator] = None


class CloneSpec(MigrateSpec):
   """
   Specification of cloning a virtual storage object.
   
   Attributes:
       name: Descriptive name of the cloned virtual storage object.
       keepAfterDeleteVm: Choice of the deletion behavior of this virtual storage object.
           
           If not set, the default value is false.
       metadata: The metadata KV pairs that are supposed to be updated on the destination
           virtual storage object.
           
           The clone task is atomic by design. That being
           said, failing to update the specified metadata pairs leads to the failure
           of the clone task. If unset, no metadata will be updated. An empty string
           value is indicative of a vcenter tag.
   """
   name: str
   keepAfterDeleteVm: _typing.Optional[bool] = None
   metadata: list[pyVmomi.vim.KeyValue] = []


class CreateSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification to create a virtual storage object.
   
   Attributes:
       id: The ID of the virtual storage object.
           
           If specified, the id will be used as an identifier for the created virtual
           storage object.
           For each new request, the ID should be a unique ID complying to RFC4122V4
           (generated randomly).
           For retry requests with the same ID, all the other input parameters in
           the spec are expected to remain same.
           If not specified, a system generated ID will be used as identifier for
           the virtual storage object.
           
           Since: vSphere API Release 9.1.0.0
       name: Descriptive name of this virtual storage object.
       keepAfterDeleteVm: Choice of the deletion behavior of this virtual storage object.
           
           If not set, the default value is true.
       backingSpec: Specification of the backings of the virtual storage object.
       capacityInMB: Size in MB of the virtual storage object.
       profile: Virtual storage object Profile requirement.
           
           If unset,
           the default behavior will apply.
       crypto: Crypto operation of the disk.
           
           If unset and if `pyVmomi.vim.vslm.CreateSpec.profile` contains an encryption iofilter,
           then crypto will be of type CryptoSpecEncrypt, and filled with
           keyId that is automatically generated and keyProviderId that is the
           default kms cluster.
       metadata: The metadata KV pairs that are supposed to be created on the newly created
           virtual storage object.
           
           The create task is atomic by design. That being
           said, failing to add the specified metadata pairs leads to the failure
           of the create task. If unset, no metadata will be added. An empty string
           value is indicative of a vcenter tag.
   """
   class BackingSpec(pyVmomi.vmodl.DynamicData):
      """
      Specification of the backing of a virtual
      storage object.
      
      Attributes:
          datastore: The datastore managed object where this backing is located.
          path: Relative location in the specified datastore where disk needs to be
              created.
              
              If not specified disk gets created at the default
              VStorageObject location on the specified datastore.
      """
      datastore: pyVmomi.vim.Datastore
      path: _typing.Optional[str] = None

   class DiskFileBackingSpec(CreateSpec.BackingSpec):
      """
      Specification of the disk file backing of a virtual
      storage object.
      
      Attributes:
          provisioningType: Provisioning type.
      """
      provisioningType: _typing.Optional[str] = None

   class RawDiskMappingBackingSpec(CreateSpec.BackingSpec):
      """
      Specification of the rdm backing of a virtual
      storage object.
      
      Attributes:
          lunUuid: Unique identifier of the LUN accessed by the raw disk mapping.
          compatibilityMode: The compatibility mode of the raw disk mapping (RDM).
              
              This must be specified
              when a new virtual disk with an RDM backing is created.
      """
      lunUuid: str
      compatibilityMode: str

   id: _typing.Optional[ID] = None
   name: str
   keepAfterDeleteVm: _typing.Optional[bool] = None
   backingSpec: CreateSpec.BackingSpec
   capacityInMB: pyVmomi.VmomiSupport.long
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []
   crypto: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None
   metadata: list[pyVmomi.vim.KeyValue] = []


class DeleteAllSnapshotsResult(pyVmomi.vmodl.DynamicData):
   """
   This data object type defines the result of
   `pyVmomi.vim.vslm.VStorageObjectManagerBase.deleteAllSnapshots` task.
   
   Attributes:
       vstorageObject: Source VStorageObject object whose snapshots deletion are done.
       usedCapacity: Storage space utilization of snapshots in MB excluding the running point
       isConsolidated: This flag will be set to true in case we have consolidated
           the whole snapshot disk chain.
   
   Since: vSphere API Release 9.1.2.0
   """
   vstorageObject: VStorageObject
   usedCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   isConsolidated: _typing.Optional[bool] = None


class DiskCryptoSpec(pyVmomi.vmodl.DynamicData):
   """
   This data object type contains the crypto information of all disks along
   the chain
   
   Attributes:
       parent: The parent in the chain.
       crypto: Crypto information of the current disk.
   """
   parent: _typing.Optional[DiskCryptoSpec] = None
   crypto: pyVmomi.vim.encryption.CryptoSpec

class DiskInfoFlag:
   """
   Flags representing the different information of a disk.
   
   Since: vSphere API Release 8.0.0.1
   """
   pass


class ID(pyVmomi.vmodl.DynamicData):
   """
   This data object type describes an identifier class which
   is globally unique to identify the associated object.
   
   Attributes:
       id: Id string which is globally unique to identify
           an object.
   """
   id: str


class InfrastructureObjectPolicy(pyVmomi.vmodl.DynamicData):
   """
   The data object type describes improved virtual disk infrastructure namespace
   storage policy details.
   """
   name: str
   backingObjectId: str
   profileId: str
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class InfrastructureObjectPolicySpec(pyVmomi.vmodl.DynamicData):
   """
   Specification to assign a SPBM policy to FCD infrastructure object
   (namespace).
   
   This is used in object-based storage.
   
   Attributes:
       datastore: Datastore on which datastore policy needs to be assigned.
       profile: SPBM Profile to associate.
   """
   datastore: pyVmomi.vim.Datastore
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []


class ReconcileResult(pyVmomi.vmodl.DynamicData):
   """
   Contains result to be returned for
   `pyVmomi.vim.vslm.vcenter.VStorageObjectManager.reconcileDatastoreInventoryEx` task.
   
   Since: vSphere API Release 9.0.0.0
   """
   class InvalidDiskPath(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          path: invalid disk path for reconcile.
          reason: Reason for invalid disk path
      
      Since: vSphere API Release 9.0.0.0
      """
      path: str
      reason: str

   class ReconcileDetail(pyVmomi.vmodl.DynamicData):
      """
      Contains information related to the performed reconcile operation.
      
      Attributes:
          hostName: Host name where reconcile operation was performed.
              
              This will have the either VC name or the host name based on
              where the details were captured.
              In case we do not get the hostName for the system it would be
              empty string.
          reconcileReportPath: Reconcile report path in host.
          isReconciled: Set to true if reconcile was done from host, false otherwise
              for host.
              
              This will be unset for the vcenter part of result.
          isDeepScanned: If deepScan was done from host, false otherwise for host.
              
              This will be unset for vcenter part of result.
          numberOfReconcileIssues: Number of reconcile issues found
          numberOfFcdsBeforeReconcile: Number of fcds before reconcile operation
              This will be unset for vcenter part of result.
          numberOfFcdsAfterReconcile: Number of fcds after reconcile operation.
              
              This will be unset for vcenter part of result.
          invalidDiskPaths: reconcile invalid disk paths
      
      Since: vSphere API Release 9.0.0.0
      """
      hostName: _typing.Optional[str] = None
      reconcileReportPath: _typing.Optional[str] = None
      isReconciled: _typing.Optional[bool] = None
      isDeepScanned: _typing.Optional[bool] = None
      numberOfReconcileIssues: _typing.Optional[int] = None
      numberOfFcdsBeforeReconcile: _typing.Optional[int] = None
      numberOfFcdsAfterReconcile: _typing.Optional[int] = None
      invalidDiskPaths: list[ReconcileResult.InvalidDiskPath] = []

   reconcileDetails: list[ReconcileResult.ReconcileDetail] = []


class ReconcileSpec(pyVmomi.vmodl.DynamicData):
   """
   Contains specification to reconcile a datastore
   
   Attributes:
       datastore: The datastore managed object that is to be reconciled/scanned.
       includeDiskPaths: List of paths of the disk descriptor files which are to be reconciled
           or scanned.
           
           This is an optional parameter and if specified, the reconciliation will
           scan only these disk paths and reconcile the catalog.
           This will save time and avoid scanning all the vmdk files.
           The disk paths should belong to the same datastore.
           The field should adhere to the following format:
           /vmfs/volume/<datastore-uuid>/.../<disk-name>.vmdk .
           Please note, either this field or `pyVmomi.vim.vslm.ReconcileSpec.excludeDiskPaths`
           should be specified in `pyVmomi.vim.vslm.ReconcileSpec` and not both.
       excludeDiskPaths: List of paths of the disk descriptor files which are excluded for reconcile
           or scan operation.
           
           This is an optional parameter and if specified, the reconciliation will
           skip these disk paths.
           This will be useful in a case when user wants to reconcile complete datastore
           and skip few set of the FCD's which are present in same datastore.
           The disk paths should belong to the same datastore.
           The field should adhere to the following format:
           /vmfs/volume/<datastore-uuid>/.../<disk-name>.vmdk
           Please note, either `pyVmomi.vim.vslm.ReconcileSpec.includeDiskPaths` or this field
           should be specified in `pyVmomi.vim.vslm.ReconcileSpec` and not both.
       deepScan: If true - Checks extent files and disk descriptor file contents
           Also evaluates and corrects the `ddb.fcd.useCount` values on relevant VMDKs,
           if it is incorrectly set.
           
           `ddb.fcd.useCount` correction only happens
           when reconciling the entire datastore with `pyVmomi.vim.vslm.ReconcileSpec.deepScan` set to true.
           If either `pyVmomi.vim.vslm.ReconcileSpec.includeDiskPaths` or `pyVmomi.vim.vslm.ReconcileSpec.excludeDiskPaths` are specified,
           `ddb.fcd.useCount` evaluation will not be performed.
           Note that this is a time consuming process.
       dryRun: If true - Does not reconcile but only scans the datastore.
       generateReport: If set to 1, generate report for
           `pyVmomi.vim.vslm.host.VStorageObjectManager.reconcileDatastoreInventoryEx` task.
           
           If set to 0 or unset, do not generate report
           Partner apps can use 0 and 1 as values.
           Other values are reserved for future and internal use.
   
   Since: vSphere API Release 9.0.0.0
   """
   datastore: pyVmomi.vim.Datastore
   includeDiskPaths: list[str] = []
   excludeDiskPaths: list[str] = []
   deepScan: _typing.Optional[bool] = None
   dryRun: _typing.Optional[bool] = None
   generateReport: _typing.Optional[int] = None

class RelocateSpec(MigrateSpec):
   """Specification for relocating a virtual storage object."""
   pass


class StateInfo(pyVmomi.vmodl.DynamicData):
   """
   Contains information of a virtual storage object state.
   
   NOTE: The information obtained with this object is dynamic and it could
   change during the lifetime of the object. For performance purposes some
   of the data may not reflect the immediate state of the object, also there
   is not guarantee that it will be provided.
   
   Attributes:
       tentative: If set this flag indicates that the object currently is part of
           provisioning operation or the last operation has not finished gracefully.
           
           There are maintenance procedures that are working on resolving that
           tentative state. Note that this might result in the object to be removed.
   """
   tentative: _typing.Optional[bool] = None


class TagEntry(pyVmomi.vmodl.DynamicData):
   """
   Specification of the Tag-Association tuple of Dataservice Tagging package.
   
   This class is a subset of the class dataservice.taggging.TaggingEntry.
   
   Attributes:
       tagName: Associated tag name of the Tag-Association tuple
       parentCategoryName: Associated parent category name of the Tag-Association tuple
   """
   tagName: str
   parentCategoryName: str


class VClockInfo(pyVmomi.vmodl.DynamicData):
   """
   Virtual clock info of VStorageObject catalog.
   
   Attributes:
       vClockTime: Virtual clock time of VStorageObject catalog.
           
           It is an epoch or
           generation ID assigned to each VStorageObject operation on a datastore.
   """
   vClockTime: pyVmomi.VmomiSupport.long


class VStorageObject(pyVmomi.vmodl.DynamicData):
   """
   This data object type describes a virtual storage object.
   
   Attributes:
       config: Virtual storage object configuration
   """
   class ConsumptionType(pyVmomi.VmomiSupport.Enum):
      """
      Consumption type constants.
      
      Consumption type describes how the virtual storage object is connected and
      consumed for data by the clients.
      
      Attributes:
          disk: Disk type.
      """
      disk: _typing.ClassVar['VStorageObject.ConsumptionType'] = 'disk'

   class ConfigInfo(BaseConfigInfo):
      """
      Data object specifies Virtual storage object configuration
      
      Attributes:
          descriptorVersion: The descriptor version of this object
              
              Since: vSphere API Release 8.0.1.0
          capacityInMB: The size in MB of this object.
          consumptionType: Consumption type of this object.
          consumerId: IDs of the consumer objects which consume this vstorage object.
              
              For a virtual disk, this can be VM ID(s).
          virtualDiskFormat: The type of VirtualDisk for 4k native disk/array support.
              
              See `pyVmomi.vim.Datastore.SectorFormat` for definitions of
              supported types. If not set, the default value is
              `native_512`.
              
              Since: vSphere API Release 9.0.0.0
          linkedCloneBasePath: Base disk path of a linked clone disk.
              
              Unset, if the virtual storage object is not a linked clone.
              
              Since: vSphere API Release 9.1.0.0
          linkedCloneParentId: The ID of the parent virtual storage object this linked clone virtual
              storage object.
              
              Unset, if the virtual storage object is not a linked clone or if the
              parent of the linked clone is a vanilla disk
              
              Since: vSphere API Release 9.1.0.0
      """
      descriptorVersion: _typing.Optional[int] = None
      capacityInMB: pyVmomi.VmomiSupport.long
      consumptionType: list[str] = []
      consumerId: list[ID] = []
      virtualDiskFormat: _typing.Optional[str] = None
      linkedCloneBasePath: _typing.Optional[str] = None
      linkedCloneParentId: _typing.Optional[ID] = None

   config: VStorageObject.ConfigInfo


class VStorageObjectAttachResult(pyVmomi.vmodl.DynamicData):
   """
   This data type defines the result of
   attaching a vStorage object to VM
   
   Attributes:
       volumeId: The ID of the operated volume See `pyVmomi.vim.vslm.ID`
       diskUUID: UUID for disk, value is obtained from vm config and can be used during mounting.
           
           This field will be set in case of a successful attach operation. When fault field is set,
           this value will not be set and should be ignored.
       fault: Fault, if any, corresponding to the specified volume ID that caused operation
           to fail.
           
           Absence of fault will indicate successful result.
   
   Since: vSphere API Release 9.1.0.0
   """
   volumeId: ID
   diskUUID: _typing.Optional[str] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VStorageObjectAttachSpec(pyVmomi.vmodl.DynamicData):
   """
   This data type defines the specification for one volume to
   be attached to virtual machine.
   
   Attributes:
       volumeId: The ID of the virtual disk to be operated.
           
           See `pyVmomi.vim.vslm.ID`
       datastore: datastore where the volume is located.
       diskMode: The disk persistence mode.
           
           Supported modes are listed in `pyVmomi.vim.vm.device.VirtualDiskOption.DiskMode`
           When unset, default mode is `vim.vm.device.VirtualDiskOption.persistent`
           (that also means dependent persistent to CNS)
           see `pyVmomi.vim.vm.device.VirtualDiskOption.DiskMode`
       sharing: The sharing mode of the virtual disk.
           
           Supported modes are listed in `pyVmomi.vim.vm.device.VirtualDisk.Sharing`
           When unset, default value is `sharingNone`
           See `pyVmomi.vim.vm.device.VirtualDisk.Sharing`
       controllerKey: Key of the controller the disk will connect to.
           
           It can be unset if there is only one controller
           (SCSI/SATA/NVMe) with the available slot in the
           virtual machine. If there are multiple SCSI/SATA/NVMe
           controllers available, user must specify
           the controller; if there is no available
           controllers, a `pyVmomi.vim.fault.MissingController`
           fault will be thrown.
       unitNumber: The unit number of the disk to be attached on its
           controller.
           
           If unset, the next free slot on the specified
           controller or on the only available controller will be
           assigned to the attached disk.
   
   Since: vSphere API Release 9.1.0.0
   """
   volumeId: ID
   datastore: pyVmomi.vim.Datastore
   diskMode: _typing.Optional[str] = None
   sharing: _typing.Optional[str] = None
   controllerKey: _typing.Optional[int] = None
   unitNumber: _typing.Optional[int] = None

class VStorageObjectControlFlag:
   pass


class VStorageObjectManagerBase(pyVmomi.VmomiSupport.ManagedObject):
   """Base interface to manage virtual storage object."""
   def ExtendDiskEx(self, id: ID, datastore: pyVmomi.vim.Datastore, newCapacityInMB: pyVmomi.VmomiSupport.long) -> pyVmomi.vim.Task:
      """
      Expand the capacity of a virtual disk, which is a storage object with
      `disk`, to the new
      capacity.
      
      If new capacity is smaller than current disk capacity, then
      operation fails due to invalid capacity. If new capacity is greater
      than current disk capacity, then operation proceeds. If new capacity
      is equal to current disk ccapcity, then operation succeeds without
      any actual extension.
      The extended disk region will be the same as the original disk:
      \\- For a zerothick disk, the extended disk region will be zeroedthick.
      \\- For an eagerzerothick disk, the extended disk region will be
      eagerzeroedthick
      \\- A thin-provisioned disk will always be extended as a thin-provisioned
      disk.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          id: The ID of the virtual disk to be extended.
          datastore: The datastore where the virtual disk is located.
          newCapacityInMB: The new capacity of the virtual disk in MB.
      
      Returns:
          The vclock info of this operation
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while extending the virtual disk.
          pyVmomi.vim.fault.NotFound: If the specified virtual storage object cannot be
              found.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
              The disk may be consumed and cannot be extended.
          pyVmomi.vim.fault.TaskInProgress: If the virtual storage object is busy.
      
      Since: vSphere API Release 8.0.2.0
      """
      ...
   def RenameVStorageObjectEx(self, id: ID, datastore: pyVmomi.vim.Datastore, name: str) -> VClockInfo:
      """
      Rename a virtual storage object.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          id: The ID of the virtual storage object to be renamed.
          datastore: The datastore where the virtual storage object is
              located.
          name: The new name for the virtual storage object.
      
      Returns:
          The vclock info of this operation
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while renaming the virtual storage
              object.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If the specified virtual storage object cannot be
              found.
      
      Since: vSphere API Release 8.0.2.0
      """
      ...
   def CreateSnapshotEx(self, id: ID, datastore: pyVmomi.vim.Datastore, description: str, snapshotId: _typing.Optional[ID]) -> pyVmomi.vim.Task:
      """
      Creates a snapshot of a given VStorageObject.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage object
              is located.
          description: A short description to be associated with the snapshot.
          snapshotId: The ID of the snapshot of the virtual storage object,
              For each new request, the ID should be a unique ID
              complying to RFC4122V4 (generated randomly).
              For retry requests with the same ID, all the other input
              parameters are expected to remain same.
              If not specified, a random system generated snapshot ID
              will be assigned to the snapshot.
              
              Since: vSphere API Release 9.1.0.0
      
      Returns:
          The vStorageObjectSnapshot info.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
      
      Since: vSphere API Release 8.0.2.0
      """
      ...
   def DeleteSnapshotEx(self, id: ID, datastore: pyVmomi.vim.Datastore, snapshotId: ID) -> pyVmomi.vim.Task:
      """
      Deletes a given snapshot of a VStorageObject.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage object
              is located.
          snapshotId: The ID of the snapshot of a virtual storage object.
      
      Returns:
          The vclock info of this operation
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
      
      Since: vSphere API Release 8.0.2.0
      """
      ...
   def DeleteSnapshotEx2(self, id: ID, datastore: pyVmomi.vim.Datastore, snapshotId: ID) -> pyVmomi.vim.Task:
      """
      Deletes a given snapshot of a VStorageObject.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage object
              is located.
          snapshotId: The ID of the snapshot of a virtual storage object.
      
      Returns:
          The vStorageObjectSnapshot info.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object or snapshot cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
      
      Since: vSphere API Release 9.0.0.0
      """
      ...
   def RevertVStorageObjectEx(self, id: ID, datastore: pyVmomi.vim.Datastore, snapshotId: ID) -> pyVmomi.vim.Task:
      """
      Reverts to a given snapshot of a VStorageObject.
      
      This operation is supported on detached VirtualDisks
      During revert all the snapshots which were taken after the specified
      snapshot would get deleted.
      
      E.g. Consider Disk with 4 snapshots
      
      BaseDisk -> Snap-2 -> Snap-3 -> Snap-4 -> Running-Point
      
      If user chooses to revert to snap-2 then snap-4 and snap-3 would also
      be deleted. After revert operation disk would have below configuration:
      
      BaseDisk -> Snap-2 -> Running-Point
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage object
              is located.
          snapshotId: The ID of the snapshot of a virtual storage object.
      
      Returns:
          The vclock info of this operation
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
      
      Since: vSphere API Release 8.0.2.0
      """
      ...
   def RepairDiskChain(self, id: ID, datastore: pyVmomi.vim.Datastore) -> pyVmomi.vim.Task:
      """
      Repair a virtual disk having broken chain.
      
      Requires Datastore.FileManagement privilege on the datastore where each
      virtual disk resides.
      
      Args:
          id: The ID of the virtual disk to be repaired.
          datastore: The datastore where the virtual disk is located.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while repairing the virtual disk.
          pyVmomi.vim.fault.NotFound: If the specified virtual storage object cannot be found.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.TaskInProgress: If the virtual storage object is busy.
      
      Since: vSphere API Release 9.1.0.0
      """
      ...
   def UnregisterDisk(self, id: ID, datastore: pyVmomi.vim.Datastore) -> pyVmomi.vim.Task:
      """
      Convert FCD disk to legacy disk.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          id: The ID of the virtual storage object which
              needs to be unregistered.
          datastore: The datastore where the virtual storage object is
              located.
      
      Raises:
          pyVmomi.vim.fault.InvalidState: If unregister disk operation could not be performed.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the datastore.
          pyVmomi.vim.fault.NotFound: If a given vstorage object id was not found.
          pyVmomi.vim.fault.TaskInProgress: If the virtual storage object is busy.
      
      Since: vSphere API Release 9.1.0.0
      """
      ...
   def DeleteAllSnapshots(self, id: ID, datastore: pyVmomi.vim.Datastore, deleteOnlyVanillaDisks: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      Delete all snapshots of a VStorageObject.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the virtual storage object is
              located.
          deleteOnlyVanillaDisks: If set to true, then deleteAllSnapshots task will
              try to consolidate only vanilla disk chain.
      
      Returns:
          Returns `pyVmomi.vim.vslm.DeleteAllSnapshotsResult` as result.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              specified datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while deleting any snapshot of the
              virtual storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
      
      Since: vSphere API Release 9.1.2.0
      """
      ...


class VStorageObjectSnapshot(pyVmomi.vmodl.DynamicData):
   """
   This data object type contains ID and VClock details of a virtual disk snapshot.
   
   Attributes:
       id: ID of this snapshot object.
       vclock: VClock associated with the FCD when the operation completes.
       usedCapacity: Storage space utilization of snapshots in MB excluding the running point
           
           Since: vSphere API Release 9.0.0.0
   
   Since: vSphere API Release 8.0.2.0
   """
   id: ID
   vclock: VClockInfo
   usedCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VStorageObjectSnapshotDetails(pyVmomi.vmodl.DynamicData):
   """
   This data object type provides details of a vstorage object snapshot
   
   Attributes:
       path: Path of the snapshot object
       changedBlockTrackingId: Changed block tracking ID of the snapshot
   """
   path: _typing.Optional[str] = None
   changedBlockTrackingId: _typing.Optional[str] = None


class VStorageObjectSnapshotInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object type contains the brief information of a
   virtual storage snapshot.
   
   Attributes:
       snapshots: An array of snapshots
   """
   class VStorageObjectSnapshot(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          id: ID of the snapshot object.
          backingObjectId: Backing object ID
          createTime: The date and time this object was created.
          description: Short description of the snapshot
      """
      id: _typing.Optional[ID] = None
      backingObjectId: _typing.Optional[str] = None
      createTime: _datetime.datetime
      description: str

   snapshots: list[VStorageObjectSnapshotInfo.VStorageObjectSnapshot] = []
