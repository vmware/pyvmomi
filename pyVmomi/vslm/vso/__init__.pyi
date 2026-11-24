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
   """
   DatastoreSyncStatus shows the catalog sync status of a datastore
   and is returned as a result of the VStorageObjectManager
   getGlobalCatalogSyncStatus API.
   
   When syncVClock == objectVClock the global catalog is in sync with the
   local catalog
   
   Attributes:
       datastoreURL: The datastore URL as specified in `pyVmomi.vim.Datastore.Info.url`
       syncTime: The time representing the last successful sync of the datastore.
       numberOfRetries: The number of retries for the Datastore synchronization in failure
           cases.
       error: The fault is set in case of error conditions.
           
           If the fault is set,
           the objectVClock and syncVClock will be set to -1L.
           Possible Faults:
           SyncFault If specified datastoreURL failed to sync.
   """
   datastoreURL: str
   objectVClock: pyVmomi.VmomiSupport.long
   syncVClock: pyVmomi.VmomiSupport.long
   syncTime: _typing.Optional[_datetime.datetime] = None
   numberOfRetries: _typing.Optional[int] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VStorageObjectAssociations(pyVmomi.vmodl.DynamicData):
   """
   This data object is a key-value pair whose key is the virtual storage
   object id, and value is the vm association information.
   
   Attributes:
       id: ID of this virtual storage object.
       vmDiskAssociation: Array of vm associations related to the virtual storage object.
       fault: Received error while generating associations.
   """
   class VmDiskAssociation(pyVmomi.vmodl.DynamicData):
      """
      This data object contains information of a VM Disk association.
      
      Attributes:
          vmId: ID of the virtual machine.
          diskKey: Device key of the disk attached to the VM.
      """
      vmId: str
      diskKey: int

   id: pyVmomi.vim.vslm.ID
   vmDiskAssociation: list[VStorageObjectAssociations.VmDiskAssociation] = []
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VStorageObjectManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   Interface to manage virtual storage object on a vCenter.
   
   VStorageObjectManager and SPBM policy support:
   All of the VStorageObjectManager APIs requiring ESXi host
   uses \"Programmatically selected\" host to perform the actual operation.
   If the selected host is of 6.5 version then policy would not be passed
   down to host. In that case, user operation would succeed but if user checks
   SPBM Entity Compliance, it will show \"Mismatch\" / \"Non Compliant\" as a
   compliance result.
   """
   def CreateDisk(self, spec: pyVmomi.vim.vslm.CreateSpec) -> pyVmomi.vim.Task:
      """
      Create a virtual disk, which is a storage object with
      `disk`
      as consumption type.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual disk object is created.
      
      `pyVmomi.vslm.fault.SyncFault` will set in the task error if the
      createDisk completed successfully in the backed but the datastore
      synchronization or FCD retrieval failed. The sync fault can be ignored
      with the risk of Pandora not recognizing the FCD or Pandora DB
      missing the FCD, consequently, affecting the return of
      `pyVmomi.vslm.vso.VStorageObjectManager.listVStorageObjectsForSpec` and `pyVmomi.vslm.vso.VStorageObjectManager.retrieveVStorageObjects`
      APIs.
      
      Args:
          spec: The specification of the virtual storage object
              to be created.
      
      Returns:
          The new virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs when creating the virtual disk.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RegisterDisk(self, path: str, name: _typing.Optional[str]) -> pyVmomi.vim.vslm.VStorageObject:
      """
      Promote a virtual disk to a First Class Disk.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual disk resides.
      
      Args:
          path: URL path to the virtual disk.
          name: The descriptive name of the disk object. If
              unset the name will be automatically determined
              from the path. @see vim.vslm.BaseConfigInfo.name
      
      Returns:
          The registered virtual storage object for the disk.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while registering the virtual disk.
          pyVmomi.vim.fault.InvalidDatastore: If datastore cannot be found or the operation
              cannot be performed on the datastore.
          pyVmomi.vim.fault.AlreadyExists: If disk is already registered as a
              virtual storage object.
          pyVmomi.vslm.fault.SyncFault: If an error occurs during datastore synchronization,
              implies the registerDisk completed successfully,
              however, there was an exception during datastore
              synchronization.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def ExtendDisk(self, id: pyVmomi.vim.vslm.ID, newCapacityInMB: pyVmomi.VmomiSupport.long) -> pyVmomi.vim.Task:
      """
      Expand the capacity of a virtual disk, which is a storage object with
      `disk`, to the new
      capacity.
      
      If new capacity is smaller than current disk capacity, then
      operation fails due to invalid capacity. If new capacity is greater
      than current disk capacity, then operation proceeds. If new capacity
      is equal to current disk capacity, then operation succeeds without
      any actual extension.
      The extended disk region will be the same as the original disk:
      \\- For a zerothick disk, the extended disk region will be zeroedthick.
      \\- For an eagerzerothick disk, the extended disk region will be
      eagerzeroedthick
      \\- A thin-provisioned disk will always be extended as a thin-provisioned
      disk.
      
      `pyVmomi.vslm.fault.SyncFault` will set in the task error if the
      extendDisk completed successfully but the datastore
      synchronization failed.
      
      Args:
          id: The ID of the virtual disk to be extended.
          newCapacityInMB: The new capacity of the virtual disk in MB.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while extending the virtual disk.
          pyVmomi.vim.fault.NotFound: If the specified virtual storage object cannot be
              found.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
              The disk may be consumed and cannot be extended.
          pyVmomi.vim.fault.TaskInProgress: If the virtual storage object is busy.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def InflateDisk(self, id: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.Task:
      """
      Inflate a sparse or thin-provisioned virtual disk up to the full size.
      
      Additional space allocated to the disk as a result of this operation
      will be filled with zeros.
      
      Currently inflateDisk API only supports the following combinations:
      Valid provisioning type: THIN;
      Valid Datastore: VMFS, NFS.
      Inflating a disk is not applicable for VVol/VSAN datastore.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual disk to be inflated.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while inflating the virtual disk.
          pyVmomi.vim.fault.NotFound: If the specified virtual storage object cannot be
              found.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
              The disk may be consumed and cannot be extended.
          pyVmomi.vim.fault.TaskInProgress: If the virtual storage object is busy.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RenameVStorageObject(self, id: pyVmomi.vim.vslm.ID, name: str) -> None:
      """
      Rename a virtual storage object.
      
      `pyVmomi.vslm.fault.SyncFault` is thrown when
      the underlying rename operation of the FCD succeeded, however, there
      was a issue with syncing the datastore or FCD. Rename operation of the
      FCD is not idempotent, implying, any attempt to rename the FCD with it's
      current name would result in a error. The sync fault can be ignored
      with the risk of Pandora DB having stale name, consequently,
      affecting the return of `pyVmomi.vslm.vso.VStorageObjectManager.listVStorageObjectsForSpec`
      and `pyVmomi.vslm.vso.VStorageObjectManager.retrieveVStorageObjects` APIs.
      
      Args:
          id: The ID of the virtual storage object to be renamed.
          name: The new name for the virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while renaming the virtual storage
              object.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If the specified virtual storage object cannot be
              found.
          pyVmomi.vslm.fault.SyncFault: If an error occurs during datastore synchronization,
              implies the renameVStorageObject completed
              successfully, however, there was an exception during
              datastore synchronization.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def UpdateVStorageObjectPolicy(self, id: pyVmomi.vim.vslm.ID, profile: list[pyVmomi.vim.vm.ProfileSpec]) -> pyVmomi.vim.Task:
      """
      Update the storage policy on a virtual storage object.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object.
          profile: New profile requirement on the virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while updating the virtual storage
              object policy.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If the specified virtual storage object cannot be
              found.
          pyVmomi.vim.fault.TaskInProgress: If the virtual storage object is busy.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def UpdateVStorageObjectCrypto(self, id: pyVmomi.vim.vslm.ID, profile: list[pyVmomi.vim.vm.ProfileSpec], disksCrypto: _typing.Optional[pyVmomi.vim.vslm.DiskCryptoSpec]) -> pyVmomi.vim.Task:
      """
      Update the storage crypto on a virtual storage object.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object.
          profile: New profile requirement on the virtual storage object.
          disksCrypto: The crypto information of each disk on the chain.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while updating the virtual storage
              object policy.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If the specified virtual storage object cannot be
              found.
          pyVmomi.vim.fault.TaskInProgress: If the virtual storage object is busy.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def UpdateVStorageInfrastructureObjectPolicy(self, spec: pyVmomi.vim.vslm.InfrastructureObjectPolicySpec) -> pyVmomi.vim.Task:
      """
      Assigns specified SBPM policy to the given FCD infrastructure object.
      
      Only support VSAN datastore.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage infrastructure object is located.
      
      `pyVmomi.vslm.fault.SyncFault` will set in the task error if the
      updateVStorageInfrastructureObjectPolicy completed successfully
      but the datastore synchronization failed.
      
      Args:
          spec: specification to assign a SPBM policy to FCD infrastructure
              object.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.InvalidState: If there is issue with profile spec.
          pyVmomi.vim.fault.TaskInProgress: The TaskInProgress data object type represents a fault when an operation tries
              to access an entity that already has another (long) operation in progress.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RetrieveVStorageInfrastructureObjectPolicy(self, datastore: pyVmomi.vim.Datastore) -> list[pyVmomi.vim.vslm.InfrastructureObjectPolicy]:
      """
      Retrieve FCD infrastructure object SBPM policy on given datastore.
      
      Only support VSAN datastore.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage infrastructure object is located.
      
      Args:
          datastore: Datastore on which policy needs to be retrieved.
      
      Returns:
          The policy object of virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def DeleteVStorageObject(self, id: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.Task:
      """
      Delete a virtual storage object and its associated backings.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      `pyVmomi.vslm.fault.SyncFault` will set in the task error if the
      delete of the FCD succeeded in the backend, however, there was a
      issue with syncing the datastore. The error can be ignored with
      the anticipation of Pandora resolving this automatically and the
      risk of Pandora DB having stale FCDs consequently affecting the
      return of `pyVmomi.vslm.vso.VStorageObjectManager.listVStorageObjectsForSpec` and
      `pyVmomi.vslm.vso.VStorageObjectManager.retrieveVStorageObjects` APIs.
      Any subsequent operation on the FCD is guaranteed to fail.
      
      Args:
          id: The ID of the virtual storage object to be deleted.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs when deleting the virtual storage
              object.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
              The disk may be consumed and cannot be deleted.
          pyVmomi.vim.fault.NotFound: If the specified virtual storage object cannot be
              found.
          pyVmomi.vim.fault.TaskInProgress: If the virtual storage object is busy.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RetrieveVStorageObject(self, id: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.vslm.VStorageObject:
      """
      Retrieve a virtual storage object.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object to be retrieved.
      
      Returns:
          The required virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs when retrieving the virtual object.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RetrieveVStorageObjectState(self, id: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.vslm.StateInfo:
      """
      Retrieve a virtual storage object state.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object the state to be retrieved.
      
      Returns:
          The required virtual storage object state.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs when retrieving the virtual object
              state.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RetrieveVStorageObjectAssociations(self, ids: list[pyVmomi.vim.vslm.ID]) -> list[VStorageObjectAssociations]:
      """
      Retrieve vm associations for each virtual storage object in the query.
      
      Args:
          ids: The IDs of the virtual storage objects of the query.
      
      Returns:
          The list of VStorageObjectVmAssociations which provides FCD id
          to vm associations mapping.
      """
      ...
   def ListVStorageObjectsForSpec(self, query: list[VStorageObjectQuerySpec], maxResult: int) -> _typing.Optional[VStorageObjectQueryResult]:
      """
      List virtual storage objects matching all the
      `pyVmomi.vslm.vso.VStorageObjectQuerySpec`.
      
      The results are determined
      by ANDing the `pyVmomi.vslm.vso.VStorageObjectQuerySpec` while ORing each
      of the values specified as a part of the
      `pyVmomi.vslm.vso.VStorageObjectQuerySpec.queryValue` field. Currently,
      only a single value in `pyVmomi.vslm.vso.VStorageObjectQuerySpec.queryValue`
      is supported.
      Expect that not all results will be returned. If all results are not
      returned, `pyVmomi.vslm.vso.VStorageObjectQueryResult.allRecordsReturned`
      flag will be set to false. Results will be returned in
      `pyVmomi.vslm.vso.VStorageObjectQueryResult.id` order. To query for additional
      objects, \"add ID > last ID returned\" to the query and call
      `pyVmomi.vslm.vso.VStorageObjectManager.listVStorageObjectsForSpec` again.
      
      Args:
          query: Query defined using array of
              `pyVmomi.vslm.vso.VStorageObjectQuerySpec` objects.
          maxResult: Maximum number of virtual storage object IDs to return.
      
      Returns:
          `pyVmomi.vslm.vso.VStorageObjectQueryResult` array containing the
          list of IDs of the virtual storage objects sorted in ascending
          order and matching the query.
      """
      ...
   def CloneVStorageObject(self, id: pyVmomi.vim.vslm.ID, spec: pyVmomi.vim.vslm.CloneSpec) -> pyVmomi.vim.Task:
      """
      Clone a virtual storage object.
      
      Requires Datastore.FileManagement privilege on both source and
      destination datastore.
      
      `pyVmomi.vslm.fault.SyncFault` will set in the task error if the
      cloneVStorageObject completed successfully but the datastore
      synchronization failed.
      
      Args:
          id: The ID of the virtual storage object.
          spec: The specification for cloning the virtual storage
              object.
      
      Returns:
          The cloned virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while cloning the virtual
              storage object.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be
              found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RelocateVStorageObject(self, id: pyVmomi.vim.vslm.ID, spec: pyVmomi.vim.vslm.RelocateSpec) -> pyVmomi.vim.Task:
      """
      Relocate a virtual storage object.
      
      Requires Datastore.FileManagement privilege on both source and
      destination datastore.
      
      `pyVmomi.vslm.fault.SyncFault` will set in the task error if the
      relocateVStorageObject completed successfully but the datastore
      synchronization failed.
      
      Args:
          id: The ID of the virtual storage object.
          spec: The specification for relocation of the virtual
              storage object.
      
      Returns:
          The relocated virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while relocating the virtual
              storage object.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
              The disk may be consumed and cannot be relocated.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot
              be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def SetVStorageObjectControlFlags(self, id: pyVmomi.vim.vslm.ID, controlFlags: list[str]) -> None:
      """
      Set control flags on VStorageObject.
      
      The control flags are defined in
      `pyVmomi.vim.vslm.VStorageObjectControlFlag`.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object.
          controlFlags: control flags enum array to be set on the
              VStorageObject. All control flags not included
              in the array remain intact.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on
              the datastore.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
              The disk may be consumed.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot
              be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def ClearVStorageObjectControlFlags(self, id: pyVmomi.vim.vslm.ID, controlFlags: list[str]) -> None:
      """
      Clear control flags on VStorageObject.
      
      The control flags are defined in
      `pyVmomi.vim.vslm.VStorageObjectControlFlag`.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object.
          controlFlags: control flags enum array to be cleared on the
              VStorageObject. All control flags not included
              in the array remain intact.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on
              the datastore.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
              The disk may be consumed.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot
              be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def AttachTagToVStorageObject(self, id: pyVmomi.vim.vslm.ID, category: str, tag: str) -> None:
      """
      Attach a tag to a virtual storage object.
      
      Requires privilege InventoryService.Tagging.AttachTag on root folder
      
      Args:
          id: The identifier(ID) of the virtual storage object.
          category: The category to which the tag belongs.
          tag: The tag which has to be associated with the virtual storage
              object.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If the specified category or tag cannot be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def DetachTagFromVStorageObject(self, id: pyVmomi.vim.vslm.ID, category: str, tag: str) -> None:
      """
      Detach a tag from a virtual storage object.
      
      Requires privilege InventoryService.Tagging.AttachTag on root folder
      
      Args:
          id: The identifier(ID) of the virtual storage object.
          category: The category to which the tag belongs.
          tag: The tag which has to be disassociated with the virtual storage
              object.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If the specified category or tag cannot be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def ListVStorageObjectsAttachedToTag(self, category: str, tag: str) -> list[pyVmomi.vim.vslm.ID]:
      """
      Lists all virtual storage objects attached to the tag.
      
      Args:
          category: The category to which the tag belongs.
          tag: The tag to be queried.
      
      Returns:
          The list of IDs of the virtual storage objects.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If the specified category or tag cannot be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def ListTagsAttachedToVStorageObject(self, id: pyVmomi.vim.vslm.ID) -> list[pyVmomi.vim.vslm.TagEntry]:
      """
      Lists all tags attached to virtual storage object.
      
      Args:
          id: The ID of the virtual storage object.
      
      Returns:
          The list of Tag-association tuples associated with the
          virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If the specified category or tag cannot be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def ReconcileDatastoreInventory(self, datastore: pyVmomi.vim.Datastore) -> pyVmomi.vim.Task:
      """
      Reconcile the datastore inventory info of virtual storage objects.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          datastore: The datastore that needs to be reconciled.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on
              the datastore.
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def ScheduleReconcileDatastoreInventory(self, datastore: pyVmomi.vim.Datastore) -> None:
      """
      Schedules reconcile of the inventory info of virtual storage objects on
      one of the hosts that is connected with the datastore.
      
      This method just
      schedules the reconcile operation for the nearby future and returns. Note
      that since the reconcile operation will be executed after this method
      already returns the success of this method should not be considered as
      success of the actual reconcile operation.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          datastore: The datastore that needs to be reconciled.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on
              the datastore.
          pyVmomi.vim.fault.NotFound: A NotFound error occurs when a referenced component of a managed
              object cannot be found.
              
              The referenced component can be a data
              object type (such as a role or permission) or a primitive
              (such as a string).
              
              For example, if the missing referenced component is a data object, such as
              VirtualSwitch, the NotFound error is
              thrown. The NotFound error is also thrown if the data object is found, but the referenced name
              (for example, \"vswitch0\") is not.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def CreateSnapshot(self, id: pyVmomi.vim.vslm.ID, description: str) -> pyVmomi.vim.Task:
      """
      Creates a snapshot of a given VStorageObject.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          id: The ID of the virtual storage object.
          description: A short description to be associated with the snapshot.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def DeleteSnapshot(self, id: pyVmomi.vim.vslm.ID, snapshotId: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.Task:
      """
      Deletes a given snapshot of a VStorageObject.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          id: The ID of the virtual storage object.
          snapshotId: The ID of the snapshot of a virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RetrieveSnapshotInfo(self, id: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.vslm.VStorageObjectSnapshotInfo:
      """
      Retrieves snapshot information of a given VStorageObject.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          id: The ID of the virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def CreateDiskFromSnapshot(self, id: pyVmomi.vim.vslm.ID, snapshotId: pyVmomi.vim.vslm.ID, name: str, profile: list[pyVmomi.vim.vm.ProfileSpec], crypto: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec], path: _typing.Optional[str]) -> pyVmomi.vim.Task:
      """
      Creates a new Disk from given snapshot of a VStorageObject.
      
      Requires Datastore.FileManagement and Cryptographer.Decrypt privilege.
      
      `pyVmomi.vslm.fault.SyncFault` will set in the task error if the
      createDiskFromSnapshot completed successfully but the datastore
      synchronization failed.
      
      Args:
          id: The ID of the virtual storage object.
          snapshotId: The ID of the snapshot of the virtual storage object.
          name: A user friendly name to be associated with the new disk.
          profile: SPBM Profile requirement on the new virtual storage object.
              If not specified datastore default policy would be
              assigned.
          crypto: Crypto information of the new disk.
          path: Relative location in the specified datastore where disk needs
              to be created. If not specified disk gets created at the
              default VStorageObject location on the specified datastore.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RevertVStorageObject(self, id: pyVmomi.vim.vslm.ID, snapshotId: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.Task:
      """
      Reverts to a given snapshot of a VStorageObject.
      
      This operation is supported on detached VirtualDisks
      During revert all the snapshots which were taken after the specified
      snapshot would get deleted.
      
      E.g. Consider Disk with 4 snapshots
      
      BaseDisk -$gt; Snap-2 -$gt; Snap-3 -$gt; Snap-4 -$gt; Running-Point
      
      If user chooses to revert to snap-2 then snap-4 and snap-3 would also
      be deleted. After revert operation disk would have below configuration:
      
      BaseDisk -$gt; Snap-2 -$gt; Running-Point
      
      Requires Datastore.FileManagement privilege.
      
      `pyVmomi.vslm.fault.SyncFault` will set in the task error if the
      revertVStorageObject completed successfully but the datastore
      synchronization failed.
      
      Args:
          id: The ID of the virtual storage object.
          snapshotId: The ID of the snapshot of a virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RetrieveSnapshotDetails(self, id: pyVmomi.vim.vslm.ID, snapshotId: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.vslm.VStorageObjectSnapshotDetails:
      """
      Retrieves snapshot disk details of a given snapshot.
      
      Args:
          id: The ID of the virtual storage object.
          snapshotId: The ID of the snapshot of a virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def QueryChangedDiskAreas(self, id: pyVmomi.vim.vslm.ID, snapshotId: pyVmomi.vim.vslm.ID, startOffset: pyVmomi.VmomiSupport.long, changeId: str) -> pyVmomi.vim.VirtualMachine.DiskChangeInfo:
      """
      Get a list of areas of a virtual disk that have been modified since a
      well-defined point in the past.
      
      The beginning of the change interval is
      identified by \"changeId\", while the end of the change interval is implied
      by the snapshot ID passed in.
      
      Note that the result of this function may contain \"false positives\"
      (i.e: flag areas of the disk as modified that are not). However, it is
      guaranteed that no changes will be missed.
      
      Args:
          id: The ID of the virtual storage object.
          snapshotId: The ID of the snapshot of a virtual storage object for
              which changes that have been made since \"changeId\"
              should be computed.
          startOffset: Start Offset in bytes at which to start computing
              changes. Typically, callers will make multiple calls
              to this function, starting with startOffset 0 and then
              examine the \"length\" property in the returned
              DiskChangeInfo structure, repeatedly calling
              queryChangedDiskAreas until a map for the entire
              virtual disk has been obtained.
          changeId: Identifier referring to a point in the past that should
              be used as the point in time at which to begin including
              changes to the disk in the result. A typical use case
              would be a backup application obtaining a changeId from
              a virtual disk's backing info when performing a backup.
              When a subsequent incremental backup is to be performed,
              this change Id can be used to obtain a list of changed
              areas on disk.
      
      Returns:
          Returns a data structure specifying extents of the virtual disk
          that have changed since the time the changeId string was
          obtained.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object or snapshot
              cannot be found.
          pyVmomi.vim.fault.FileFault: if the virtual disk files cannot be accessed/queried.
          pyVmomi.vim.fault.InvalidState: if change tracking is not supported for this
              particular disk.
          pyVmomi.vmodl.fault.InvalidArgument: if startOffset is beyond the end of the virtual
              disk or changeId is invalid.
          pyVmomi.vslm.fault.VslmFault: The super class for all VSLM Faults.
      """
      ...
   def QueryGlobalCatalogSyncStatus(self) -> list[DatastoreSyncStatus]:
      """
      Gets the synchronization status of the Global Catalog.
      
      This API returns an
      array of DatastoreSyncStatuses showing the synchronization status for each
      datastore currently being tracked by the Global Catalog. This can be used
      to see if the Global Catalog search results are fully up-to-date and also to
      check if the Global Catalog is making progress on bringing a datastore's
      information up to date.
      """
      ...
   def QueryGlobalCatalogSyncStatusForDatastore(self, datastoreURL: str) -> _typing.Optional[DatastoreSyncStatus]:
      """
      Gets the synchronization state of the Global Catalog for the specified datastore.
      
      Args:
          datastoreURL: URL of the datastore to check synchronization status for
      
      Returns:
          The sync status of the datastore
      
      Raises:
          pyVmomi.vim.fault.NotFound: If the specified datastore cannot be found
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def UpdateVStorageObjectMetadata(self, id: pyVmomi.vim.vslm.ID, metadata: list[pyVmomi.vim.KeyValue], deleteKeys: list[str]) -> pyVmomi.vim.Task:
      """
      Update metadata KV pairs to a virtual storage object.
      
      And this API is by
      design supposed to be used for all of the addition, modification and
      deletion operations of metadata KV pairs.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      `pyVmomi.vslm.fault.SyncFault` will set in the task error if the
      updateVStorageObjectMetadata completed successfully but the datastore
      synchronization or FCD retrieval failed. The sync fault can
      be ignored with the risk of Pandora DB having stale metadata information
      consequently affecting the return of `pyVmomi.vslm.vso.VStorageObjectManager.listVStorageObjectsForSpec`
      and `pyVmomi.vslm.vso.VStorageObjectManager.retrieveVStorageObjects` APIs.
      
      Args:
          id: The ID of the virtual storage object.
          metadata: array of key/value strings. (keys must be unique
              within the list)
          deleteKeys: array of keys need to be deleted
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore, such as datastore cannot be found
              or inaccessible.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RetrieveVStorageObjectMetadata(self, id: pyVmomi.vim.vslm.ID, snapshotId: _typing.Optional[pyVmomi.vim.vslm.ID], prefix: _typing.Optional[str]) -> list[pyVmomi.vim.KeyValue]:
      """
      Retrieve metadata KV pairs from a virtual storage object.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object.
          snapshotId: The ID of the snapshot of virtual storage object.
          prefix: The prefix of the metadata key that needs to be retrieved
      
      Returns:
          returns the array of key value pair
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore, such as datastore cannot be found
              or inaccessible.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RetrieveVStorageObjectMetadataValue(self, id: pyVmomi.vim.vslm.ID, snapshotId: _typing.Optional[pyVmomi.vim.vslm.ID], key: str) -> str:
      """
      Retrieve the metadata value by key from a virtual storage object.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object.
          snapshotId: The ID of the snapshot of virtual storage object.
          key: The key for the virtual storage object
      
      Returns:
          returns the value for the key
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore, such as datastore cannot be found
              or inaccessible.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.KeyNotFound: If specified key cannot be found.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...
   def RetrieveVStorageObjects(self, ids: list[pyVmomi.vim.vslm.ID]) -> list[VStorageObjectResult]:
      """
      Retrieves details of a list of virtual storage objects from cache.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          ids: The array of IDs of the virtual storage object to be
              retrieved.
      
      Returns:
          The array of `pyVmomi.vslm.vso.VStorageObjectResult` virtual
          storage objects corresponding to the input.
      """
      ...
   def AttachDisk(self, id: pyVmomi.vim.vslm.ID, vm: pyVmomi.vim.VirtualMachine, controllerKey: _typing.Optional[int], unitNumber: _typing.Optional[int]) -> pyVmomi.vim.Task:
      """
      Attach an existing disk to this virtual machine.
      
      A minimum virtual machine version of 'vmx-13' is required for this
      operation to succeed. If a compatible VM version is not satisfied,
      a `pyVmomi.vim.fault.DeviceUnsupportedForVmVersion` fault will be thrown.
      
      `pyVmomi.vslm.fault.SyncFault` will set in the task error if the
      FCD was attached successfully in the backend, however, there
      was a failure in syncing the datastore or FCD. The attach disk
      operation is not idempotent, implying, any attempt to re-attach
      the FCD to the same VM would cause an error. The sync fault can
      be ignored safely as Pandora DB does not track FCDs attached
      to VMs as of vSphere 7.0.
      
      Args:
          id: The ID of the virtual disk to be operated. See
              `pyVmomi.vim.vslm.ID`
          vm: The virtual machine where the virtual disk is to be attached.
          controllerKey: Key of the controller the disk will connect to.
              It can be unset if there is only one controller
              (SCSI or SATA) with the available slot in the
              virtual machine. If there are multiple SCSI or
              SATA controllers available, user must specify
              the controller; if there is no available
              controllers, a `pyVmomi.vim.fault.MissingController`
              fault will be thrown.
          unitNumber: The unit number of the attached disk on its controller.
              If unset, the next available slot on the specified
              controller or the only available controller will be
              assigned to the attached disk.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the disk object cannot be found.
          pyVmomi.vim.fault.VmConfigFault: if the virtual machine's configuration is invalid.
          pyVmomi.vim.fault.FileFault: if there is a problem creating or accessing the virtual
              machine's files for this operation.
          pyVmomi.vim.fault.InvalidState: if the operation cannot be performed in the current
              state of the virtual machine. For example, because the virtual
              machine's configuration is not available.
          pyVmomi.vim.fault.InvalidDatastore: If the datastore cannot be found or inaccessible.
          pyVmomi.vim.fault.InvalidController: If the specified controller cannot be found or
              the specified unitNumber is already taken, or
              the controller has no free slots.
          pyVmomi.vim.fault.MissingController: If the virtual machine has no or more than one
              available controllers when controllerKey is
              unset.
          pyVmomi.vim.fault.DeviceUnsupportedForVmVersion: If the virtual machine's version is
              incompatible for the given device.
          pyVmomi.vslm.fault.VslmFault: If a VSLM internal server error occurred.
      """
      ...


class VStorageObjectQueryResult(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vslm.vso.VStorageObjectQueryResult` contains the result of
   `pyVmomi.vslm.vso.VStorageObjectManager.listVStorageObjectsForSpec` API.
   
   Attributes:
       allRecordsReturned: If set to false, more results were found than could be returned (either
           limited by maxResult input argument in the
           `pyVmomi.vslm.vso.VStorageObjectManager.listVStorageObjectsForSpec` API or
           truncated because the number of results exceeded the internal limit).
       id: IDs of the VStorageObjects matching the query criteria
           NOTE: This field will be removed once the dev/qe code is refactored.
           
           IDs will be returned in ascending order. If
           `pyVmomi.vslm.vso.VStorageObjectQueryResult.allRecordsReturned` is set to false,
           to get the additional results, repeat the query with ID > last ID as
           part of the query spec `pyVmomi.vslm.vso.VStorageObjectQuerySpec`.
       queryResults: Results of the query criteria.
           
           `pyVmomi.vslm.vso.VStorageObjectResult.id` will be returned in
           ascending order. If `pyVmomi.vslm.vso.VStorageObjectQueryResult.allRecordsReturned`
           is set to false,then, to get the additional results, repeat the query
           with ID > last ID as part of the query spec
           `pyVmomi.vslm.vso.VStorageObjectQuerySpec`.
   """
   allRecordsReturned: bool
   id: list[pyVmomi.vim.vslm.ID] = []
   queryResults: list[VStorageObjectResult] = []


class VStorageObjectQuerySpec(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vslm.vso.VStorageObjectQuerySpec` describes the criteria to query
   VStorageObject from global catalog.
   
   `pyVmomi.vslm.vso.VStorageObjectQuerySpec` is sent as input to
   `pyVmomi.vslm.vso.VStorageObjectManager.listVStorageObjectsForSpec` API.
   
   Attributes:
       queryField: This field specifies the searchable field.
           
           This can be one of the values from
           `pyVmomi.vslm.vso.VStorageObjectQuerySpec.QueryFieldEnum`.
       queryOperator: This field specifies the operator to compare the searchable field
           `pyVmomi.vslm.vso.VStorageObjectQuerySpec.queryField` with the specified
           value `pyVmomi.vslm.vso.VStorageObjectQuerySpec.queryValue`.
           
           This can be one of the values from `pyVmomi.vslm.vso.VStorageObjectQuerySpec.QueryOperatorEnum`.
       queryValue: This field specifies the value to be compared with the searchable field.
   """
   class QueryOperatorEnum(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.vslm.vso.VStorageObjectQuerySpec.QueryOperatorEnum` enumerated
      type defines the operators to use for constructing the query criteria.
      """
      equals: _typing.ClassVar['VStorageObjectQuerySpec.QueryOperatorEnum'] = 'equals'
      notEquals: _typing.ClassVar['VStorageObjectQuerySpec.QueryOperatorEnum'] = 'notEquals'
      lessThan: _typing.ClassVar['VStorageObjectQuerySpec.QueryOperatorEnum'] = 'lessThan'
      greaterThan: _typing.ClassVar['VStorageObjectQuerySpec.QueryOperatorEnum'] = 'greaterThan'
      lessThanOrEqual: _typing.ClassVar['VStorageObjectQuerySpec.QueryOperatorEnum'] = 'lessThanOrEqual'
      greaterThanOrEqual: _typing.ClassVar['VStorageObjectQuerySpec.QueryOperatorEnum'] = 'greaterThanOrEqual'
      contains: _typing.ClassVar['VStorageObjectQuerySpec.QueryOperatorEnum'] = 'contains'
      startsWith: _typing.ClassVar['VStorageObjectQuerySpec.QueryOperatorEnum'] = 'startsWith'
      endsWith: _typing.ClassVar['VStorageObjectQuerySpec.QueryOperatorEnum'] = 'endsWith'

   class QueryFieldEnum(pyVmomi.VmomiSupport.Enum):
      """
      The `pyVmomi.vslm.vso.VStorageObjectQuerySpec.QueryFieldEnum` enumerated
      type defines the searchable fields.
      
      Attributes:
          id: Indicates `pyVmomi.vim.vslm.BaseConfigInfo.id` as the searchable field.
          name: Indicates `pyVmomi.vim.vslm.BaseConfigInfo.name` as the searchable
              field.
          capacity: Indicates `pyVmomi.vim.vslm.VStorageObject.ConfigInfo.capacityInMB` as the
              searchable field.
          createTime: Indicates `pyVmomi.vim.vslm.BaseConfigInfo.createTime` as the searchable
              field.
          backingObjectId: Indicates
              `pyVmomi.vim.vslm.BaseConfigInfo.FileBackingInfo.backingObjectId` as the
              searchable field.
          datastoreMoId: Indicates `pyVmomi.vim.vslm.BaseConfigInfo.BackingInfo.datastore` as the
              searchable field.
          metadataKey: Indicates it as the searchable field.
          metadataValue: Indicates it as the searchable field.
      """
      id: _typing.ClassVar['VStorageObjectQuerySpec.QueryFieldEnum'] = 'id'
      name: _typing.ClassVar['VStorageObjectQuerySpec.QueryFieldEnum'] = 'name'
      capacity: _typing.ClassVar['VStorageObjectQuerySpec.QueryFieldEnum'] = 'capacity'
      createTime: _typing.ClassVar['VStorageObjectQuerySpec.QueryFieldEnum'] = 'createTime'
      backingObjectId: _typing.ClassVar['VStorageObjectQuerySpec.QueryFieldEnum'] = 'backingObjectId'
      datastoreMoId: _typing.ClassVar['VStorageObjectQuerySpec.QueryFieldEnum'] = 'datastoreMoId'
      metadataKey: _typing.ClassVar['VStorageObjectQuerySpec.QueryFieldEnum'] = 'metadataKey'
      metadataValue: _typing.ClassVar['VStorageObjectQuerySpec.QueryFieldEnum'] = 'metadataValue'

   queryField: str
   queryOperator: str
   queryValue: list[str] = []


class VStorageObjectResult(pyVmomi.vmodl.DynamicData):
   """
   The `pyVmomi.vslm.vso.VStorageObjectResult` contains the result objects of
   `pyVmomi.vslm.vso.VStorageObjectQueryResult` which is returned as a result of
   `pyVmomi.vslm.vso.VStorageObjectManager.listVStorageObjectsForSpec` and
   `pyVmomi.vslm.vso.VStorageObjectManager.retrieveVStorageObjects` APIs.
   
   Attributes:
       id: The ID of the virtual storage object.
       name: Name of FCD.
       capacityInMB: The size in MB of this object.
           
           If the faults are set,
           then the capacityInMB will be -1
       createTime: The create time information of the FCD.
       datastoreUrl: The Datastore URL containing the FCD.
       diskPath: The disk path of the FCD.
       usedCapacityInMB: The rolled up used capacity of the FCD and it's snapshots.
           
           Returns -1L if the space information is currently unavailable.
       backingObjectId: The ID of the backing object of the virtual storage object.
       snapshotInfo: VStorageObjectSnapshotResult array containing information about all the
           snapshots of the virtual storage object.
       metadata: Metadata array of key/value strings.
       error: The fault is set in case of error conditions and this property will
           have the reason.
           
           Possible Faults:
           NotFound If specified virtual storage object cannot be found.
   """
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
   """
   The `pyVmomi.vslm.vso.VStorageObjectSnapshotResult` contains brief information about a
   snapshot of the object `pyVmomi.vslm.vso.VStorageObjectResult` which is returned as a
   result of `pyVmomi.vslm.vso.VStorageObjectManager.retrieveVStorageObjects` API.
   
   Attributes:
       backingObjectId: The ID of the vsan object backing a snapshot of the virtual storage
           object.
       description: The description user passed in when creating this snapshot.
       snapshotId: The ID of this snapshot, created and used in fcd layer.
       diskPath: The file path of this snapshot.
   """
   backingObjectId: pyVmomi.vim.vslm.ID
   description: _typing.Optional[str] = None
   snapshotId: _typing.Optional[pyVmomi.vim.vslm.ID] = None
   diskPath: _typing.Optional[str] = None
