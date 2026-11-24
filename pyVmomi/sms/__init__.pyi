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
   """This data object type describes system information."""
   name: str
   fullName: str
   vendor: str
   apiVersion: str
   instanceUuid: str
   vasaApiVersion: _typing.Optional[str] = None


class EntityReference(pyVmomi.vmodl.DynamicData):
   """
   Deprecated: As of SMS API 4.0Unique identifier of a given entity with the storage
   management service.
   
   It is similar to the VirtualCenter
   ManagedObjectReference but also identifies certain
   non-managed objects.
   
   Attributes:
       id: Unique identifier for the entity of a given type in the
           system.
           
           A VirtualCenter managed object ID can be supplied
           here, in which case the type may be unset. Otherwise, the
           type must be set.
       type: Type of the entity.
   """
   class EntityType(pyVmomi.VmomiSupport.Enum):
      """Types of entities supported by the service."""
      datacenter: _typing.ClassVar['EntityReference.EntityType'] = 'datacenter'
      resourcePool: _typing.ClassVar['EntityReference.EntityType'] = 'resourcePool'
      storagePod: _typing.ClassVar['EntityReference.EntityType'] = 'storagePod'
      cluster: _typing.ClassVar['EntityReference.EntityType'] = 'cluster'
      vm: _typing.ClassVar['EntityReference.EntityType'] = 'vm'
      datastore: _typing.ClassVar['EntityReference.EntityType'] = 'datastore'
      host: _typing.ClassVar['EntityReference.EntityType'] = 'host'
      vmFile: _typing.ClassVar['EntityReference.EntityType'] = 'vmFile'
      scsiPath: _typing.ClassVar['EntityReference.EntityType'] = 'scsiPath'
      scsiTarget: _typing.ClassVar['EntityReference.EntityType'] = 'scsiTarget'
      scsiVolume: _typing.ClassVar['EntityReference.EntityType'] = 'scsiVolume'
      scsiAdapter: _typing.ClassVar['EntityReference.EntityType'] = 'scsiAdapter'
      nasMount: _typing.ClassVar['EntityReference.EntityType'] = 'nasMount'

   id: str
   type: _typing.Optional[EntityReference.EntityType] = None


class FaultDomainFilter(pyVmomi.vmodl.DynamicData):
   """
   This spec contains information needed for `pyVmomi.sms.StorageManager.queryFaultDomain`
   API to filter the result.
   
   Attributes:
       providerId: If specified, query for this specific provider only; else query for all
           providers.
   """
   providerId: _typing.Optional[str] = None


class ReplicationGroupFilter(pyVmomi.vmodl.DynamicData):
   """
   This spec contains information needed for `pyVmomi.sms.StorageManager.queryReplicationGroupInfo`
   API to filter the result.
   
   Attributes:
       groupId: Query for the given replication groups from their associated providers.
           
           The groupId cannot be null or empty.
   """
   groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId] = []


class ServiceInstance(pyVmomi.VmomiSupport.ManagedObject):
   """Service interface for the Storage Monitoring Service."""
   def QueryStorageManager(self) -> StorageManager:
      """
      Retrieves Storage Manager managed object.
      
      Returns:
          A managed object `pyVmomi.sms.StorageManager` reference.
      """
      ...
   def QuerySessionManager(self) -> pyVmomi.sms.auth.SessionManager:
      """
      Retrieves SMS Session Manager managed object.
      
      Returns:
          A managed object `pyVmomi.sms.auth.SessionManager` reference.
      """
      ...
   def QueryAboutInfo(self) -> AboutInfo:
      """
      Retrieves information about the service.
      
      Returns:
          AboutInfo information about the system
      """
      ...


class StorageManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   The `pyVmomi.sms.StorageManager` managed object (SMS) provides methods to retrieve
   information about available storage topology, capabilities, and state.
   
   SMS establishes and maintains connections with VASA providers. SMS retrieves
   information about storage availability from the providers, and clients can use
   the SMS API to perform the following operations.
   - Identify VASA providers.
   - Retrieve information about storage arrays.
   - Identify vSphere inventory entities (hosts and datastores)
     which are associated with external storage entities on the storage arrays.
   """
   def RegisterProvider(self, providerSpec: pyVmomi.sms.provider.ProviderSpec) -> pyVmomi.vim.Task:
      """
      Register the provider and issue a sync operation on it.
      
      Args:
          providerSpec: `pyVmomi.sms.provider.ProviderSpec`
              containing parameters needed to register the
              provider
      
      Raises:
          pyVmomi.vim.fault.AlreadyExists: if the provider already exists.
          pyVmomi.sms.fault.ProviderRegistrationFault: if an error is encountered during the
              registration operation. For instance, `pyVmomi.sms.fault.IncorrectUsernamePassword`
              is thrown if the login credentials are incorrect. `pyVmomi.sms.fault.CertificateNotTrusted`
              is thrown if the provider identifies itself with an untrusted certificate.
      """
      ...
   def UnregisterProvider(self, providerId: str) -> pyVmomi.vim.Task:
      """
      Unregister the provider.
      
      Args:
          providerId: `pyVmomi.sms.provider.ProviderInfo.uid` for
              the provider
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.ProviderUnregistrationFault: if provider service is not available or
              any exception is thrown by the VASA provider
              during unregister provider.
      """
      ...
   def QueryProvider(self) -> list[pyVmomi.sms.provider.Provider]:
      """
      Get the list of Providers that are currently registered
      with StorageManager.
      
      Returns:
          List of Providers.
      
      Raises:
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while processing the
              query request.
      """
      ...
   def QueryArray(self, providerId: list[str]) -> list[pyVmomi.sms.storage.StorageArray]:
      """
      Get the list of storage arrays managed by all the registered VASA providers.
      
      Args:
          providerId: List of `pyVmomi.sms.provider.ProviderInfo.uid` for the VASA
              provider objects.
      
      Returns:
          List of data objects containing information about
          StorageArray.
      
      Raises:
          pyVmomi.vim.fault.NotFound: If the given providerId does not have any
              reference.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryProcessorAssociatedWithArray(self, arrayId: str) -> list[pyVmomi.sms.storage.StorageProcessor]:
      """
      Get the StorageProcessor data objects that are associated with Array.
      
      Args:
          arrayId: `pyVmomi.sms.storage.StorageArray.uuid` for the StorageArray
              object.
      
      Returns:
          List of data objects containing information about
          StorageProcessor.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryPortAssociatedWithArray(self, arrayId: str) -> list[pyVmomi.sms.storage.StoragePort]:
      """
      Get the StoragePort data objects that are associated with Array.
      
      Args:
          arrayId: `pyVmomi.sms.storage.StorageArray.uuid` for the StorageArray
              object.
      
      Returns:
          List of data objects containing information about
          StoragePort.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryPortAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> _typing.Optional[pyVmomi.sms.storage.StoragePort]:
      """
      Get the StoragePort data object that is associated with LUN.
      
      Args:
          scsi3Id: `pyVmomi.sms.storage.StorageLun.uuid` for the StorageLun
              object.
          arrayId: `pyVmomi.sms.storage.StorageArray.uuid` for the StorageArray
              object.
      
      Returns:
          A data object containing information about StoragePort.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryLunAssociatedWithPort(self, portId: str, arrayId: str) -> list[pyVmomi.sms.storage.StorageLun]:
      """
      Get the StorageLun data objects that are associated with StoragePort.
      
      Args:
          portId: `pyVmomi.sms.storage.StoragePort.uuid` for the StoragePort
              object.
          arrayId: `pyVmomi.sms.storage.StorageArray.uuid` for the StorageArray
              object.
      
      Returns:
          List of data objects containing information about
          StorageLun.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryArrayAssociatedWithLun(self, canonicalName: str) -> _typing.Optional[pyVmomi.sms.storage.StorageArray]:
      """
      Get the StorageArray object that is associated with the
      ScsiLun.
      
      Args:
          canonicalName: `pyVmomi.vim.host.ScsiLun.canonicalName`
              of ScsiLun
      
      Returns:
          StorageArray for the for the ScsiLun.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryPortAssociatedWithProcessor(self, processorId: str, arrayId: str) -> list[pyVmomi.sms.storage.StoragePort]:
      """
      Get the StoragePort data objects that are associated with Processor.
      
      Args:
          processorId: `pyVmomi.sms.storage.StorageProcessor.uuid` for the
              StorageProcessor object.
          arrayId: `pyVmomi.sms.storage.StorageArray.uuid` for the StorageArray
              object.
      
      Returns:
          List of data objects containing information about
          StoragePort.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryLunAssociatedWithArray(self, arrayId: str) -> list[pyVmomi.sms.storage.StorageLun]:
      """
      Get the list of StorageLun data objects that for the Array.
      
      Args:
          arrayId: `pyVmomi.sms.storage.StorageArray.uuid` for the StorageArray
              object.
      
      Returns:
          List of data object containing information about
          StorageLun.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryFileSystemAssociatedWithArray(self, arrayId: str) -> list[pyVmomi.sms.storage.StorageFileSystem]:
      """
      Get the StorageFileSystem data objects for the Array.
      
      Args:
          arrayId: `pyVmomi.sms.storage.StorageArray.uuid` for the StorageArray
              object.
      
      Returns:
          List of data objects containing information about
          StorageFileSystem.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryDatastoreCapability(self, datastore: pyVmomi.vim.Datastore) -> _typing.Optional[pyVmomi.sms.storage.StorageCapability]:
      """
      Get the capability for the given datastore.
      
      Args:
          datastore: reference to `pyVmomi.vim.Datastore`
      
      Returns:
          A data object containing information about StorageCapability.
          If the VMFS datastore have heterogeneous Luns (in case of VMFS extends),
          `pyVmomi.sms.storage.StorageCapability.description` will be empty.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryHostAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> list[pyVmomi.vim.HostSystem]:
      """
      Get HostSystem managed entities that share the StorageLun.
      
      Args:
          scsi3Id: `pyVmomi.sms.storage.StorageLun.uuid` for the StorageLun
              object.
          arrayId: `pyVmomi.sms.storage.StorageArray.uuid` for the StorageArray
              object.
      
      Returns:
          List of HostSystems.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryVmfsDatastoreAssociatedWithLun(self, scsi3Id: str, arrayId: str) -> _typing.Optional[pyVmomi.vim.Datastore]:
      """
      Get VMFS Datastore managed entity that are associated with
      StorageLun.
      
      Args:
          scsi3Id: `pyVmomi.sms.storage.StorageLun.uuid` for the StorageLun object
          arrayId: `pyVmomi.sms.storage.StorageArray.uuid` for the StorageArray
              object.
      
      Returns:
          Vmfs datastore for the file system id.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryNfsDatastoreAssociatedWithFileSystem(self, fileSystemId: str, arrayId: str) -> _typing.Optional[pyVmomi.vim.Datastore]:
      """
      Get NFS datastore managed entity that are associated with
      StorageFileSystem.
      
      Args:
          fileSystemId: `pyVmomi.sms.storage.StorageFileSystem.uuid` for the
              StorageFileSystem object
          arrayId: `pyVmomi.sms.storage.StorageArray.uuid` for the StorageArray
              object.
      
      Returns:
          Nas datastore for the storage file system id.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryDrsMigrationCapabilityForPerformance(self, srcDatastore: pyVmomi.vim.Datastore, dstDatastore: pyVmomi.vim.Datastore) -> bool:
      """
      Deprecated: As of SMS API 3.0, use `pyVmomi.sms.StorageManager.queryDrsMigrationCapabilityForPerformanceEx`Query the provider to figure out whether Storage DRS should
      migrate VMDKs between the two given datastores.
      
      Args:
          srcDatastore: Reference to the source `pyVmomi.vim.Datastore`
          dstDatastore: Reference to the destination `pyVmomi.vim.Datastore`
      
      Returns:
          true if VM migration is recommended from srcDatastore
          to dstDatastore.
          false if VM migration is not recommended from
          srcDatastore to dstDatastore.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while
              processing the query request.
      """
      ...
   def QueryDrsMigrationCapabilityForPerformanceEx(self, datastore: list[pyVmomi.vim.Datastore]) -> pyVmomi.sms.storage.DrsMigrationCapabilityResult:
      """
      Deprecated: As of SMS API 5.0Query available VASA providers for I/O performance based migration recommendations
      for all pair combinations of the given set of datastores.
      
      Datastore pairs for which
      a recommendation cannot be obtained are not included in the result.
      
      Args:
          datastore: Array containing references to `pyVmomi.vim.Datastore` objects.
      
      Returns:
          `pyVmomi.sms.storage.DrsMigrationCapabilityResult`
      
      Raises:
          pyVmomi.vim.fault.NotFound: if any `pyVmomi.vim.Datastore` in the specified input array does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while processing the query request.
      """
      ...
   def QueryStorageContainer(self, containerSpec: _typing.Optional[pyVmomi.sms.storage.StorageContainerSpec]) -> _typing.Optional[pyVmomi.sms.storage.StorageContainerResult]:
      """
      Query storage containers that are retrieved from VASA providers.
      
      Stretched container with
      UNREPORTED sync status is not included in returned result.
      
      Args:
          containerSpec: `pyVmomi.sms.storage.StorageContainerSpec`
      
      Returns:
          `pyVmomi.sms.storage.StorageContainerResult`
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the input provided as part of `pyVmomi.sms.storage.StorageContainerSpec` is not found.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while processing the query request.
      """
      ...
   def QueryAssociatedBackingStoragePool(self, entityId: _typing.Optional[str], entityType: _typing.Optional[str]) -> list[pyVmomi.sms.storage.BackingStoragePool]:
      """
      Query Backing Storage Pools for StorageLun or StorageFileSystem.
      
      Args:
          entityId: Unique identifier of a StorageLun or StorageFileSystem.
          entityType: Entity type of the entity specified using entityId. This can be either
              StorageLun or StorageFileSystem.
      
      Returns:
          Array of BackingStoragePool`pyVmomi.sms.storage.BackingStoragePool` associated with specified StorageLun or StorageFileSystem.
          If entityId is null then API returns all the BackingStoragePools of the specified type.
          If both entityId and entityType are not specified then API returns all the BackingStoragePools available.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entityId does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while processing the query request.
      """
      ...
   def QueryDatastoreBackingPoolMapping(self, datastore: list[pyVmomi.vim.Datastore]) -> list[pyVmomi.sms.storage.DatastoreBackingPoolMapping]:
      """
      Query BackingStoragePools for the given set of datastores.
      
      Available information for all types of BackingStoragePools`pyVmomi.sms.storage.BackingStoragePool.BackingStoragePoolType`
      for every input datastore is returned as part of the result.
      More than one datastore can map to same set of BackingStoragePools.
      
      Args:
          datastore: Array containing references to `pyVmomi.vim.Datastore` objects.
      
      Returns:
          `pyVmomi.sms.storage.DatastoreBackingPoolMapping`
      
      Raises:
          pyVmomi.vim.fault.NotFound: if any `pyVmomi.vim.Datastore` in the specified input array does not exist.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while processing the query request.
      """
      ...
   def RefreshCACertificatesAndCRLs(self, providerId: list[str]) -> pyVmomi.vim.Task:
      """
      SMS pushes the latest CA root certificates and CRLs to all registered VASA providers.
      
      Args:
          providerId: `pyVmomi.sms.provider.ProviderInfo.uid` for providers
      
      Raises:
          pyVmomi.vim.fault.NotFound: if there exists no provider for a `pyVmomi.sms.provider.ProviderInfo.uid` in providerId
          pyVmomi.sms.fault.CertificateRefreshFailed: if an error is encountered while refreshing
              root certificates and CRLs for any provider.
      """
      ...
   def QueryFaultDomain(self, filter: _typing.Optional[FaultDomainFilter]) -> list[pyVmomi.vim.vm.replication.FaultDomainId]:
      """
      Query for fault domains based on the query spec.
      
      If spec is null, SMS
      will return all the root fault domains only.
      
      Args:
          filter: spec for the query operation.
      
      Returns:
          all the fault domains based on the query spec.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified providerId in the spec does not exist
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while processing the
              query request.
      """
      ...
   def QueryReplicationGroupInfo(self, rgFilter: ReplicationGroupFilter) -> list[pyVmomi.sms.storage.replication.GroupOperationResult]:
      """
      Query for replication group details based on the query filter spec.
      
      The replication
      group id list in the filter spec cannot be null or empty.
      
      Returns:
          An array of `pyVmomi.sms.storage.replication.GroupOperationResult` elements.
          The length of the result array must be the same as the input.
          In the result array, each entry is either a
          `pyVmomi.sms.storage.replication.QueryReplicationGroupSuccessResult` (for success), or a
          `pyVmomi.sms.storage.replication.GroupErrorResult` (for failure).
          
          The following fault may be set in error result entry:
          - `pyVmomi.vim.fault.NotFound` if the replication group cannot be found.
          - `pyVmomi.sms.fault.ProviderUnavailable` if the provider for the entity is temporarily unavailable.
          - `pyVmomi.sms.fault.InactiveProvider` if the provider for the entity is not active.
          - `pyVmomi.sms.fault.ProviderBusy` if the provider for the entity is busy.
          - `pyVmomi.vmodl.fault.NotImplemented` if the provider does not implement this function.
      
      Raises:
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while processing the query request.
      """
      ...
   def UpgradeVASAProvider(self, upgradeSpec: pyVmomi.sms.provider.VASAProviderUpgradeSpec) -> pyVmomi.vim.Task:
      """
      Upgrade VASA Provider registered to vCenter/SMS to maximum common version supported by both
      VASA Provider and SMS.
      
      Args:
          upgradeSpec: `pyVmomi.sms.provider.VASAProviderUpgradeSpec` containing parameter to upgrade the
              VASA Provider. If spec is for non VVOL VASA Provider, then exception is thrown.
      
      Returns:
          Upgraded VASA Provider
      
      Raises:
          pyVmomi.sms.fault.SmsFault: If there is any error encountered while processing request
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


class TaskInfo(pyVmomi.vmodl.DynamicData):
   """
   This data object type contains all information about a task.
   
   Attributes:
       key: The unique key for the task.
       task: The managed object that represents this task.
       object: Managed Object to which the operation applies.
       error: If the task state is \"error\", then this property contains the fault code.
       result: If the task state is \"success\", then this property may be used
           to hold a return value.
       startTime: Time stamp when the task started running.
       completionTime: Time stamp when the task was completed (whether success or failure).
       state: Runtime status of the task.
           
           Possible values are `pyVmomi.sms.TaskInfo.State`
       progress: If the task state is \"running\", then this property contains a
           progress measurement, expressed as percentage completed, from 0 to 100.
           
           If this property is not set, then the command does not report progress.
   """
   class State(pyVmomi.VmomiSupport.Enum):
      """
      List of possible states of a task.
      
      Attributes:
          queued: Task is put in the queue.
          running: Task is currently running.
          success: Task has completed.
          error: Task has encountered an error or has been canceled.
      """
      queued: _typing.ClassVar['TaskInfo.State'] = 'queued'
      running: _typing.ClassVar['TaskInfo.State'] = 'running'
      success: _typing.ClassVar['TaskInfo.State'] = 'success'
      error: _typing.ClassVar['TaskInfo.State'] = 'error'

   key: str
   task: Task
   object: _typing.Optional[pyVmomi.VmomiSupport.ManagedObject] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   result: _typing.Optional[object] = None
   startTime: _typing.Optional[_datetime.datetime] = None
   completionTime: _typing.Optional[_datetime.datetime] = None
   state: str
   progress: _typing.Optional[int] = None
