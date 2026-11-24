# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vim.encryption
import pyVmomi.vim.vm
import pyVmomi.vim.vslm



class VStorageObjectManager(pyVmomi.vim.vslm.VStorageObjectManagerBase):
   """Interface to manage virtual storage object on an ESXi host."""
   def CreateDisk(self, spec: pyVmomi.vim.vslm.CreateSpec) -> pyVmomi.vim.Task:
      """
      Create a virtual disk, which is a storage object with
      `disk`
      as consumption type.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual disk object is created.
      
      Args:
          spec: The specification of the virtual storage object
              to be created.
              2
      
      Returns:
          The new virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs when creating the virtual disk.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
      """
      ...
   def RegisterDisk(self, path: str, name: _typing.Optional[str], modifyControlFlags: _typing.Optional[bool], id: _typing.Optional[pyVmomi.vim.vslm.ID]) -> pyVmomi.vim.vslm.VStorageObject:
      """
      Promote a virtual disk to a First Class Disk.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual disk resides.
      
      Args:
          path: URL or datastore path to the running point of the virtual disk.
          name: The descriptive name of the disk object. If
              unset the name will be automatically determined
              from the path. @see vim.vslm.BaseConfigInfo#name
          modifyControlFlags: Optional Parameter describing if the control Flags should be changed to default values
              
              Since: vSphere API Release 8.0.2.0
          id: The ID of the newly registered virtual storage object.
              For each new request, the ID should be a unique ID complying
              to RFC4122V4 (generated randomly).
              For retry requests with the same ID, all the other input
              parameters are expected to remain same.
              If not specified, a system generated ID will be assigned.
              
              Since: vSphere API Release 9.1.0.0
      
      Returns:
          The registered virtual storage object for the disk.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while registering the virtual disk.
          pyVmomi.vim.fault.InvalidDatastore: If datastore cannot be found or the operation
              cannot be performed on the datastore.
          pyVmomi.vim.fault.AlreadyExists: If disk is already registered as a
              virtual storage object.
      """
      ...
   def ExtendDisk(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, newCapacityInMB: pyVmomi.VmomiSupport.long) -> pyVmomi.vim.Task:
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
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual disk to be extended.
          datastore: The datastore where the virtual disk is located.
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
      """
      ...
   def InflateDisk(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore) -> pyVmomi.vim.Task:
      """
      Inflate a sparse or thin-provisioned virtual disk up to the full size.
      
      Additional space allocated to the disk as a result of this operation
      will be filled with zeroes.
      
      Currently inflateDisk API only supports the following combinations:
      Valid provisioning type: THIN;
      Valid Datastore: VMFS, NFS.
      Inflating a disk is not applicable for VVol/VSAN datastore.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual disk to be inflated.
          datastore: The datastore where the virtual disk is located.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while inflating the virtual disk.
          pyVmomi.vim.fault.NotFound: If the specified virtual storage object cannot be
              found.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
              The disk may be consumed and cannot be extended.
          pyVmomi.vim.fault.TaskInProgress: If the virtual storage object is busy.
      """
      ...
   def RenameVStorageObject(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, name: str) -> None:
      """
      Rename a virtual storage object.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object to be renamed.
          datastore: The datastore where the virtual storage object is
              located.
          name: The new name for the virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while renaming the virtual storage
              object.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If the specified virtual storage object cannot be
              found.
      """
      ...
   def RetrieveVStorageInfrastructureObjectPolicy(self, datastore: pyVmomi.vim.Datastore) -> list[pyVmomi.vim.vslm.InfrastructureObjectPolicy]:
      """
      Retrieve virtual storage infrastructure object SBPM policy on given
      datastore.
      
      Only support VSAN datastore.
      
      Requires Datastore.FileManagement privilege on the datastore specified.
      
      Args:
          datastore: Datastore on which policy needs to be retrieved.
      
      Returns:
          The policy object of virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
      """
      ...
   def DeleteVStorageObject(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, isLcParentAttached: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      Delete a virtual storage object and its associated backings.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object to be deleted.
          datastore: The datastore where the virtual storage object is
              located.
          isLcParentAttached: Set to true if parent of linked clone is attached
              to VM, set to false if parent of linked clone is
              detached, unset is considered as false.
              
              Since: vSphere API Release 9.1.0.0
      
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
      """
      ...
   def RetrieveVStorageObject(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, diskInfoFlags: list[str]) -> pyVmomi.vim.vslm.VStorageObject:
      """
      Retrieve a virtual storage object.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object to be retrieved.
          datastore: The datastore where the virtual storage object is
              located.
          diskInfoFlags: Flags indicating the FCD information to be
              retrieved. If diskInfoFlags is unset, then all FCD
              information will be retrieved. See
              `pyVmomi.vim.vslm.DiskInfoFlag` for the list of
              supported values.
              
              Since: vSphere API Release 8.0.0.1
      
      Returns:
          The required virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs when retrieving the virtual object.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
      """
      ...
   def RetrieveVStorageObjectState(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore) -> pyVmomi.vim.vslm.StateInfo:
      """
      Retrieve a virtual storage object state.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object the state to be retrieved.
          datastore: The datastore where the virtual storage object is
              located.
      
      Returns:
          The required virtual storage object state.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs when retrieving the virtual object
              state.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
      """
      ...
   def ListVStorageObject(self, datastore: pyVmomi.vim.Datastore) -> list[pyVmomi.vim.vslm.ID]:
      """
      List all virtual storage objects located on a datastore.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          datastore: The datastore to query for the virtual storage objects.
      
      Returns:
          The list of IDs of the virtual storage objects located on the
          datastore.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore, such as datastore cannot be found
              or inaccessible.
      """
      ...
   def CloneVStorageObject(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, spec: pyVmomi.vim.vslm.CloneSpec) -> pyVmomi.vim.Task:
      """
      Clone a virtual storage object.
      
      Requires Datastore.FileManagement privilege on both source and
      destination datastore.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage
              object is located.
          spec: The specification for cloning the virtual storage
              object.
      
      Returns:
          The cloned virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while cloning the virtual
              storage object.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on
              the datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be
              found.
      """
      ...
   def RelocateVStorageObject(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, spec: pyVmomi.vim.vslm.RelocateSpec, isLcParentAttached: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      Relocate a virtual storage object.
      
      Requires Datastore.FileManagement privilege on both source and
      destination datastore.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage
              object is located.
          spec: The specification for relocation of the virtual
              storage object.
          isLcParentAttached: Since: vSphere API Release 9.1.0.0
      
      Returns:
          The relocated virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.FileFault: If an error occurs while relocating the virtual
              storage object.
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on
              the datastore.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
              The disk may be consumed and cannot be relocated.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot
              be found.
      """
      ...
   def SetVStorageObjectControlFlags(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, controlFlags: list[str]) -> None:
      """
      Set control flags on VStorageObject.
      
      The control flags are defined in
      `pyVmomi.vim.vslm.VStorageObjectControlFlag`.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage
              object is located.
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
      """
      ...
   def ClearVStorageObjectControlFlags(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, controlFlags: list[str]) -> None:
      """
      Clear control flags on VStorageObject.
      
      The control flags are defined in
      `pyVmomi.vim.vslm.VStorageObjectControlFlag`.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage
              object is located.
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
      """
      ...
   def ReconcileDatastoreInventory(self, datastore: pyVmomi.vim.Datastore, deepCleansing: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      Reconcile the datastore inventory info of virtual storage objects.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          datastore: The datastore that needs to be reconciled.
          deepCleansing: If set true, the reconcile task will check for the
              extent files and the disk descriptor file content
              as part of reconciliation. Note that this is a time
              consuming process.
              
              Since: vSphere API Release 9.0.0.0
      
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
      """
      ...
   def ScheduleReconcileDatastoreInventory(self, datastore: pyVmomi.vim.Datastore, deepCleansing: _typing.Optional[bool]) -> None:
      """
      Schedules reconcile of the datastore inventory info of virtual storage
      objects.
      
      This method just schedules the reconcile operation for the
      nearby future and returns. Note that since the reconcile operation will
      be executed after this method already returns the success of this method
      should not be considered as success of the actual reconcile operation.
      
      Requires Datastore.FileManagement privilege.
      
      Args:
          datastore: The datastore that needs to be reconciled.
          deepCleansing: If set true, the reconcile task will check for the
              extent files and the disk descriptor file content
              as part of reconciliation. Note that this is a time
              consuming process.
              
              Since: vSphere API Release 9.0.0.0
      
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
      """
      ...
   def CreateSnapshot(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, description: str) -> pyVmomi.vim.Task:
      """
      Creates a snapshot of a given VStorageObject.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage object
              is located.
          description: A short description to be associated with the snapshot.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
      """
      ...
   def DeleteSnapshot(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, snapshotId: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.Task:
      """
      Deletes a given snapshot of a VStorageObject.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage object
              is located.
          snapshotId: The ID of the snapshot of a virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
      """
      ...
   def RetrieveSnapshotInfo(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore) -> pyVmomi.vim.vslm.VStorageObjectSnapshotInfo:
      """
      Retrieves snapshot information of a given VStorageObject.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage object
              is located.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
      """
      ...
   def CreateDiskFromSnapshot(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, snapshotId: pyVmomi.vim.vslm.ID, name: str, profile: list[pyVmomi.vim.vm.ProfileSpec], crypto: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec], path: _typing.Optional[str], provisioningType: _typing.Optional[str], isLinkedClone: _typing.Optional[bool], targetId: _typing.Optional[pyVmomi.vim.vslm.ID], targetDatastore: _typing.Optional[pyVmomi.vim.Datastore]) -> pyVmomi.vim.Task:
      """
      Creates a new Disk from given snapshot of a VStorageObject.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage object
              is located.
          snapshotId: The ID of the snapshot of the virtual storage object.
          name: A user friendly name to be associated with the new disk.
          profile: SPBM Profile requirement on the new virtual storage object.
              If not specified datastore default policy would be
              assigned.
          crypto: Crypto information of the new disk.
          path: Relative location where disk has to be created, used in
              `targetDatastore` and `datastore` parameters.
              If not specified disk gets created at default `pyVmomi.vim.vslm.VStorageObject`
              location of `targetDatastore` or `datastore`.
          provisioningType: Provisioining type of the disk as specified in above
              mentioned profile. The list of supported values can be found in
              `pyVmomi.vim.vslm.BaseConfigInfo.DiskFileBackingInfo.ProvisioningType`
              
              Since: vSphere API Release 8.0.0.1
          isLinkedClone: Indicates whether a linkedClone Disk needs to be created from the snapshot.
              
              Since: vSphere API Release 9.1.0.0
          targetId: The ID of the target virtual storage object.
              For each new request, the ID should be a unique ID
              complying to RFC4122V4 (generated randomly).
              For retry requests with the same ID, all the other input
              parameters are expected to remain same.
              If not specified, a system generated ID will be assigned
              to the newly created virtual storage object.
              
              Since: vSphere API Release 9.1.0.0
          targetDatastore: The target datastore where the new disk needs to be created.
              if not specified, the new disk will be created where
              the source virtual storage object is located.
              
              Since: vSphere API Release 9.1.0.0
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
      """
      ...
   def RevertVStorageObject(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, snapshotId: pyVmomi.vim.vslm.ID) -> pyVmomi.vim.Task:
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
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore where the source virtual storage object
              is located.
          snapshotId: The ID of the snapshot of a virtual storage object.
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.FileFault: If an error occurs while snapshotting the virtual
              storage object.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
      """
      ...
   def UpdateVStorageObjectMetadata(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, metadata: list[pyVmomi.vim.KeyValue], deleteKeys: list[str]) -> pyVmomi.vim.Task:
      """
      Update metadata KV pairs to a virtual storage object.
      
      And this API is by
      design supposed to be used for all of the addition, modification and
      deletion operations of metadata KV pairs.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore to query for the virtual storage objects.
          metadata: array of key/value strings. (keys must be unique
              within the list)
          deleteKeys: array of keys need to be deleted
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore, such as datastore cannot be found
              or inaccessible.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
      """
      ...
   def RetrieveVStorageObjectMetadata(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, snapshotId: _typing.Optional[pyVmomi.vim.vslm.ID], prefix: _typing.Optional[str]) -> list[pyVmomi.vim.KeyValue]:
      """
      Retrieve metadata KV pairs from a virtual storage object.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore to query for the virtual storage objects.
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
      """
      ...
   def RetrieveVStorageObjectMetadataValue(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, snapshotId: _typing.Optional[pyVmomi.vim.vslm.ID], key: str) -> str:
      """
      Retrieve the metadata value by key from a virtual storage object.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore to query for the virtual storage objects.
          snapshotId: The ID of the snapshot of virtual storage object.
          key: The key for the the virtual storage object
      
      Returns:
          returns the value for the key
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore, such as datastore cannot be found
              or inaccessible.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
          pyVmomi.vim.fault.KeyNotFound: If specified key cannot be found.
      """
      ...
   def DeleteVStorageObjectEx(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, isLcParentAttached: _typing.Optional[bool]) -> pyVmomi.vim.Task:
      """
      Delete a virtual storage object and its associated backings.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object to be deleted.
          datastore: The datastore where the virtual storage object is
              located.
          isLcParentAttached: Set to true if parent of linked clone is attached
              to VM, set to false if parent of linked clone is
              detached, unset is considered as false.
              
              Since: vSphere API Release 9.1.0.0
      
      Returns:
          The vclock info of this operation
      
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
      
      Since: vSphere API Release 7.0.2.0
      """
      ...
   def UpdateVStorageObjectMetadataEx(self, id: pyVmomi.vim.vslm.ID, datastore: pyVmomi.vim.Datastore, metadata: list[pyVmomi.vim.KeyValue], deleteKeys: list[str]) -> pyVmomi.vim.Task:
      """
      Update metadata KV pairs to a virtual storage object.
      
      And this API is by
      design supposed to be used for all of the addition, modification and
      deletion operations of metadata KV pairs.
      
      Requires Datastore.FileManagement privilege on the datastore where the
      virtual storage object is located.
      
      Args:
          id: The ID of the virtual storage object.
          datastore: The datastore to query for the virtual storage objects.
          metadata: array of key/value strings. (keys must be unique
              within the list)
          deleteKeys: array of keys need to be deleted
      
      Returns:
          The virtual storage object containing vclock of this operation
      
      Raises:
          pyVmomi.vim.fault.InvalidDatastore: If the operation cannot be performed on the
              datastore, such as datastore cannot be found
              or inaccessible.
          pyVmomi.vim.fault.InvalidState: If the operation cannot be performed on the disk.
          pyVmomi.vim.fault.NotFound: If specified virtual storage object cannot be found.
      
      Since: vSphere API Release 7.0.2.0
      """
      ...
   def SetVirtualDiskUuidEx(self, name: str, uuid: _typing.Optional[str]) -> pyVmomi.vim.Task:
      """
      Set the virtual disk Uuid.
      
      Args:
          name: The name of the disk, either a datastore path or a URL
              referring to the virtual disk whose uuid for the DDB entry needs to be set.
              A URL has the form
              > scheme://authority/folder/path?dsName=dsName
              
              where
              - scheme is `http` or `https`.
              - authority specifies the hostname or IP address of the VirtualCenter or
                ESX server and optionally the port.
              - dsName is the name of the Datastore.
              - path is a slash-delimited path from the root of the datastore.
              
              A datastore path has the form
              > [datastore] path
              
              where
              - datastore is the datastore name.
              - path is a slash-delimited path from the root of the datastore.
              
              An example datastore path is \"[storage] path/to/file.extension\".
          uuid: The hex representation of the unique ID for this virtual disk. If uuid is not set or missing,
              a random UUID is generated and assigned.
      
      Raises:
          pyVmomi.vim.fault.FileFault: if an error occurs updating the virtual disk.
          pyVmomi.vim.fault.InvalidDatastore: if the operation cannot be performed on the datastore.
      
      Since: vSphere API Release 8.0.3.0
      """
      ...
   def QueryVirtualDiskUuidEx(self, name: str) -> str:
      """
      Get the virtual disk UUID.
      
      Args:
          name: The name of the disk, either a datastore path or a URL
              referring to the virtual disk whose uuid for the DDB entry needs to be queried.
              A URL has the form
              > scheme://authority/folder/path?dsName=dsName
              
              where
              - scheme is `http` or `https`.
              - authority specifies the hostname or IP address of the VirtualCenter or
                ESX server and optionally the port.
              - dsName is the name of the Datastore.
              - path is a slash-delimited path from the root of the datastore.
              
              A datastore path has the form
              > [datastore] path
              
              where
              - datastore is the datastore name.
              - path is a slash-delimited path from the root of the datastore.
              
              An example datastore path is \"[storage] path/to/file.extension\".
      
      Returns:
          The hex representation of the unique ID for this virtual disk.
      
      Raises:
          pyVmomi.vim.fault.FileFault: if an error occurs reading the virtual disk.
          pyVmomi.vim.fault.InvalidDatastore: if the operation cannot be performed on the datastore.
      
      Since: vSphere API Release 8.0.3.0
      """
      ...
