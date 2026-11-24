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
   """This class defines general access control list spec."""
   pass


class VolumeOperationResult(pyVmomi.vmodl.DynamicData):
   """
   Base class for returning result of operation invoked on a specific volume.
   
     
   Operations that require some additional fields in their result can extend this
   class. E.g. result classes for create and attach operations extend this class to
   add additional fields.
     
   If an operation allows batch input, then the output should contain same number
   of result objects. One object corresponding to each input entry.
     
   Since every result object will have its own fault, that fault will be limited to the
   corresponding input object and should not be used for overall operation failure.
   
   Attributes:
       volumeId: Unique identifier and datastore information for the volume.
           
             
           Result object for all operations, other than create, will get volumeId as
           part of its input parameter and should always have this field set. For the
           result of create operation, this field will not be set. Please see
           `pyVmomi.vim.cns.VolumeCreateResult` for details.
       fault: Fault, if any, corresponding to the specified volume ID that caused operation
           to fail.
           
           Absence of fault will indicate successful result.
             
           For create operation, volumeId field will not be set. Instead, volume name
           will be set, to associated fault with appropriate request. Please see
           `pyVmomi.vim.cns.VolumeCreateResult` for details.
   """
   volumeId: _typing.Optional[VolumeId] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class AsyncQueryResult(VolumeOperationResult):
   """
   Data object for returning result of asynchronous query/queryAll operation.
   
   Attributes:
       queryResult: Query result object.
   """
   queryResult: _typing.Optional[QueryResult] = None


class BackingObjectDetails(pyVmomi.vmodl.DynamicData):
   """
   Base class for providing additional option for creating backing for a
   container volume.
   
     
   The child-classes of this class will be used at the time
   of volume creation to specify options that should be used to create volume,
   and will also be returned as part of query result to give more information
   about the volume, `pyVmomi.vim.cns.Volume`. Type of child-class will also serve
   as the volume type specification during creation.
     
   Backing type specific fields would be there in the respective child classes.
     
   E.g. BlockBackingDetails class will have details related to block type of
   backing object. One example of such property is ID of the block disk that
   backs the volume.
   
   Attributes:
       capacityInMb: During creation this field specifies desired container volume capacity in MB.
           
             
           In case of block and file volumes, when an existing volume is specified
           then this field will be ignored.
             
           At the time of query, when available, this field will tell the actual
           capacity of volume that backs the container volume. Else it will be set
           to -1, to indicate that the capacity of the volume is unknown at the moment.
           This can happen due to some internal system errors or due to the underlying
           platform that's eventually consistent.
   """
   capacityInMb: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class BaseCreateSpec(pyVmomi.vmodl.DynamicData):
   """Base specification for volume creation."""
   pass


class BlockBackingDetails(BackingObjectDetails):
   """
   Details for a block type backing for container volume.
   
     
   This class will be used as input at the time of volume creation and will also
   be returned as part of query result to give more information about a container volume.
     
   Note: In future, for block volumes the disk format, like thin, lazy-zeroed-
   thick, eager-zeroed-thick, will be made a part of storage policy. Until then,
   for block volumes, only the thin type of provisioning will be supported.
   
   Attributes:
       backingDiskId: At the time of creation this field would identify the existing disk
           that should be used to back the container volume.
           
             
           This field is optional and when this and backingDiskPath are not specified,
           a new disk will be created to back the volume.
             
           When this field is present, capacityInMb and storage policy fields
           will be ignored.
       backingDiskUrlPath: At the time of creation this field would identify the URL path to an
           existing disk that should be used to back the container volume.
           
           This field should be set in create request when the client wants to
           register an existing disk as a CNS block volume. If this disk is already
           registered as CNS block volume, then the server will throw
           `pyVmomi.vim.fault.CnsAlreadyRegisteredFault` CNS fault with the CNS volume ID set.
             
           This field is optional and when this and backingDiskId are not specified,
           a new disk will be created to back the volume.
             
           When this field is present, capacityInMb and storage policy fields
           will be ignored.
             
           Note that this field will not be set in the query API result. But in
           future release of CNS, it may be set.
             
           This field must be in the following format:
           Format:
           https://<vc_ip>/folder/<vm_vmdk_path>?dcPath=<datacenterPath>& dsName=<datastoreName>
             
           Ex: https://10.192.255.221/folder/34a9c05d-5f03-e254-e692-02004479cb91/ vm2_1.vmdk?dcPath=/Folder-1/Datacenter-1&dsName=vsanDatastore
             
           This is for a 34a9c05d-5f03-e254-e692-02004479cb91/vm2_1.vmdk file under
           datacenter \"Datacenter-1\" with path \"/Folder-1/Datacenter-1\" and datastore
           \"vsanDatastore\".
       backingDiskPath: This is file path of the volume.
           
           It's different from backingDiskUrlPath.
           backingDiskUrlPath is accessible from a web browser, while
           backingDiskPath is accessible by the file system.
             
           This field is set only in result of query.
       backingDiskObjectId: This is the id generated by underlying object storage, such as vsan/vvol.
           
             
           This field is set only in result of query.
       usedCapacityInMb: This is the rolled up used capacity of the FCD and its snapshots.
           
           Set to -1 if unknown.
       aggregatedSnapshotCapacityInMb: This is the rolled up allocated space of the volume's snapshots.
           
           Set to -1 if unknown.
   """
   backingDiskId: _typing.Optional[str] = None
   backingDiskUrlPath: _typing.Optional[str] = None
   backingDiskPath: _typing.Optional[str] = None
   backingDiskObjectId: _typing.Optional[str] = None
   usedCapacityInMb: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   aggregatedSnapshotCapacityInMb: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class BlockCreateSpec(BaseCreateSpec):
   """
   Specification for block volume creation.
   
   Attributes:
       cryptoSpec: Crypto to use on the volume to be created.
           
           Works with block volume only currently.
           See `pyVmomi.vim.vslm.vcenter.VStorageObjectManager.createDiskFromSnapshot` for more detail
   """
   cryptoSpec: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None


class VolumeRelocateSpec(pyVmomi.vmodl.DynamicData):
   """
   Base class for the volume relocation spec.
   
   Attributes:
       volumeId: Unique identifier for the volume.
       datastore: The destination datastore that the volume is relocated to.
       profile: Volume relocation profile requirement.
           
             
           While relocating the volume, the default policy of the destination
           datastore is applied if this is unset.
   """
   volumeId: VolumeId
   datastore: pyVmomi.vim.Datastore
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []

class BlockVolumeRelocateSpec(VolumeRelocateSpec):
   """Data object for block volume relocation spec."""
   pass


class VolumeSource(pyVmomi.vmodl.DynamicData):
   """
   Base class for the source of volumes creation.
   
   The source can be a volume snapshot or a volume.
   """
   pass


class CloneVolumeSource(VolumeSource):
   """
   Data object representing volume cloning
   
   Attributes:
       volumeId: Identifier of the volume.
       keepAfterDeleteVm: Choosing if volume should stay after VM deletion.
           
           If not set, the default value is false.
   """
   volumeId: VolumeId
   keepAfterDeleteVm: _typing.Optional[bool] = None

class ClusterFlavor:
   """
   Enumerates flavors of container orchestrator cluster for which
   volume operations are being performed.
   """
   pass

class ClusterType:
   """
   Enumerates types of container orchestrator cluster for which volume operations
   are being performed.
   
     
   This is a list of supported container orchestrator cluster types. Also the
   ClusterType value can be used to list all the volumes that exist for the
   specified type of container orchestrator.
   """
   pass


class ContainerCluster(pyVmomi.vmodl.DynamicData):
   """
   Data object to identify a container orchestrator cluster uniquely.
   
     
   This data object is aimed to link the container volumes with their
   corresponding container orchestrator clusters.
     
   One example of container orchestrator cluster is Kubernetes. Kubernetes
   cluster deployed on vSphere would consist of virtual machines on which cloud
   native application can be deployed using Kubernetes constructs.
   
   Attributes:
       clusterType: Type of this container orchestrator cluster.
           
           See `pyVmomi.vim.cns.ClusterType`
           for supported types and valid values for this field.
       clusterId: Cluster ID, provided by CNS client.
           
             
           E.g.: vSphere volume plugin for Kubernetes cluster will be responsible for
           passing this container ID to CNS. This ID will get used to link a cluster
           with its container volumes, for filtering read operations.
             
           CNS will not try to enforce uniqueness of this ID and will rely
           on clients to ensure uniqueness. Duplicate cluster ID will not cause any
           problem in provisioning workflow. But it will make cluster ID based filtering
           of volume less useful for end user.
             
           For VANILLA flavor of Kubernetes, this field must be set to a unique ID.
           For example, a combination of name and UUID.
             
           For WORKLOAD flavor of Kubernetes, this field will be set to the
           Virtual Center cluster managed object ID that has supervisor cluster enabled.
           The associated Kubernetes entity metadata for a CNS volume like namespace, PVC,
           PV and Pods will refer to corresponding entities in supervisor cluster.
             
           For GUEST_CLUSTER flavor of Kubernetes, this field will be set to the
           sub resource pool managed object ID where the guest cluster is deployed.
       vSphereUser: vSphere user corresponding to container orchestrator cluster user.
           
             
           This property is aimed to help associate container volumes with the vSphere
           user, responsible for managing lifecycle of those volumes. vSphere user
           management, like keeping track that which vSphere user is responsible for
           which all container orchestrator clusters, needs to happen out-of-band and
           is out of the scope for CNS.
             
           This information will not be used for authorization. It's for association
           purpose only.
       clusterFlavor: Flavor of this container orchestrator cluster.
           
           See `pyVmomi.vim.cns.ClusterFlavor` for supported types
           and valid values for this field. If not set, the server
           will assume VANILLA cluster flavor.
       clusterDistribution: Distribution name of this container cluster.
           
           The distribution name length is limited to 128 bytes.
       delete: Default value is False if not set.
           
           If True, the ContainerCluster should be deleted in VolumeManager.Update API
           call. But if any EntityMetadata is associating with this ContainerCluster,
           CNS Fault will be thrown. So to delete the ContainerCluster,
           user must also delete the EntityMetadata associate with this
           ContainerCluster.
           If False, the ContainerCluster should be added in VolumeManager.Update
           API call.
           This field will be ignored in VolumeManager.Create API call.
   """
   clusterType: str
   clusterId: str
   vSphereUser: str
   clusterFlavor: _typing.Optional[str] = None
   clusterDistribution: _typing.Optional[str] = None
   delete: _typing.Optional[bool] = None


class Cursor(pyVmomi.vmodl.DynamicData):
   """
   Cursor object to facilitate pagination of multi-value result for an operation,
   such as querying volumes.
   
     
   Usage: Client can set desired values of offset and limit in the first request.
   Cursor will also be returned as part of result, pointing to next set of values.
   Client can simply put the cursor object from result back in the next request.
     
   If client does not set cursor object for the request, default offset 0
   and default limit 100 will be used. The returned cursor object will set
   offset to next offset and limit to the default limit.
   
   Attributes:
       offset: Offset value.
           
           These many results will be skipped and not included in result.
       limit: Limit value sets upper cap for maximum number of values to be included in
           result.
           
           Default value for limit is 100 and maximum is 1000 (implementation
           dependent. Subject to change).
             
           If a value higher than maximum allowed is set in input, it will be limited
           to the maximum.
       totalRecords: This is the total number of records for given input parameters.
           
             
           This value should be used by client to decide if there is a need to make
           further calls to server. Client request with offset greater than total number
           of records would have empty result.
   """
   offset: pyVmomi.VmomiSupport.long
   limit: pyVmomi.VmomiSupport.long
   totalRecords: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class EntityMetadata(pyVmomi.vmodl.DynamicData):
   """
   Base data object that represents the metadata associated with an entity
   in container orchestrators like Kubernetes, Docker swarm etc.
   
   Attributes:
       entityName: Represents the name of entity.
       labels: Labels for this entity.
           
             
           Labels are opaque to CNS and it will neither try to parse the key nor the value.
           A maximum of 32 labels will be supported for each entity. Label key should be
           less than 320 bytes and value should be less than 64 bytes.
             
           If the constraints are not honored, then `pyVmomi.vmodl.fault.InvalidArgument` will be thrown.
       delete: If not set, False is assumed.
           - True indicates that the EntityMetadata should be deleted in
             VolumeManager.Update API.
           - False indicates that the EntityMetadata should be added or replaced
             in VolumeManager.Create, VolumeManager.Update APIs.
       clusterId: Represents the container orchestrator cluster the entity belongs to.
           
           This is a mandatory field as the VolumeMetadata.containerCluster
           is deprecated.
             
           This field points to a cluster in
           `pyVmomi.vim.cns.VolumeMetadata.containerClusterArray`
   """
   entityName: str
   labels: list[pyVmomi.vim.KeyValue] = []
   delete: _typing.Optional[bool] = None
   clusterId: _typing.Optional[str] = None


class FileBackingDetails(BackingObjectDetails):
   """
   Details for a file type backing for container volume.
   
     
   This class will be used as input at the time of volume creation and will also
   be returned as part of query result to give more information about a
   container volume.
   
   Attributes:
       backingFileId: At the time of creation this field would identify the existing file share
           that should be used to back the container volume.
           
             
           This field is optional and when not specified, a new file share will be
           created to back the volume.
             
           When this field is present, capacityInMb and storage policy fields
           will be ignored.
   """
   backingFileId: _typing.Optional[str] = None

class FileCreateSpec(BaseCreateSpec):
   """
   Specification for file volume creation.
   
   The file volume could be
   NFS or SMB file share. Currently, only NFS file shares provisioned by
   vSAN file service will be supported. CNS may support non NFS,
   non vSAN file service based file shares in future.
   """
   pass


class KubernetesEntityMetadata(EntityMetadata):
   """
   Data object that represents metadata associated with an entity
   in Kubernetes.
   
     
   For Kubernetes, CNS caches Kubernetes metadata like labels, persistent volume
   name, persistent volume claim name, pod name, namespace(if applicable) etc.
   Labels are captured only for persistent volume and persistent volume claim
   entities only.
     
   For WORKLOAD cluster flavor, KubernetesEntityMetadata can be mapped to
   entities in supervisor cluster as follows:
   - Namespace in this object will represent the namespace in
     supervisor cluster.
   - PV, PVC names in this object represents the PV and PVC names
     in supervisor cluster.
   - Pod name represents the pod VM name under the specific
     namespace/workload in supervisor cluster.
   
   Attributes:
       entityType: Represents the type of entity in Kubernetes.
           
           See `pyVmomi.vim.cns.KubernetesEntityType`
           for supported types.
       namespace: Namespace in Kubernetes the entity belongs to, if applicable.
           
             
           Namespace must not be set for entity of type persistent volume and must be
           set for entities of type persistent volume claim and pod.
       referredEntity: The Kubernetes entity it is referring to.
           
           For example, a PVC refers to a PV, a Pod refers to one or more
           PVCs etc. If is perfectly fine for an entity to not refer to
           anything, example, a PV does not refer to a PVC etc.
   """
   entityType: str
   namespace: _typing.Optional[str] = None
   referredEntity: list[KubernetesEntityReference] = []


class KubernetesEntityReference(pyVmomi.vmodl.DynamicData):
   """
   Data object that represents a Kubernetes entity reference both
   within the Kubernetes cluster and across nested clusters.
   
     
   Example for within Kubernetes cluster - A PVC referring a PV
   within the same kubernetes cluster.
   Example for across nested cluster - A PVC in supervisor cluster
   used by a PV in guest cluster.
   
   Attributes:
       entityType: Represents the type of entity in Kubernetes.
           
           See `pyVmomi.vim.cns.KubernetesEntityType`
           for supported types.
       entityName: Represents the name of entity.
       namespace: Namespace in Kubernetes the entity belongs to, if applicable.
           
             
           Namespace must not be set for entity of type persistent volume and must be
           set for entities of type persistent volume claim and pod.
       clusterId: Represents the Kubernetes cluster the entity belongs to.
           
           If unset, the server will interpret that this referred entity is in the
           same Kubernetes cluster as the `pyVmomi.vim.cns.KubernetesEntityMetadata.entityType`.
             
           The clusterId should be one of the cluster in
           `pyVmomi.vim.cns.VolumeMetadata.containerClusterArray`
   """
   entityType: str
   entityName: str
   namespace: _typing.Optional[str] = None
   clusterId: _typing.Optional[str] = None

class KubernetesEntityType:
   """Enumerates types of Kubernetes entities for which CNS would be storing metadata for."""
   pass


class QueryFilter(pyVmomi.vmodl.DynamicData):
   """
   Filter object to query matching volumes.
   
     
   Every property criteria that is specified through array, like labels, datastores
   and so on will add complexity in retrieving the query result, and it should be
   minimal (preferrably less than or equal to 10). The query may be slow or fail
   if this guideline is not honored. All string matchings will be absolute, unless
   specified.
   
   Attributes:
       volumeIds: Volume identifiers to be queried.
           
             
           A maximum of 1000 volume ids can be provided.
       names: Volume names to be queried.
           
             
           Currently only full string match will be supported. No regex or substring matching will be done.
       containerClusterIds: Container orchestrator cluster identifiers.
       storagePolicyId: Storage policy id associated with volume.
           
             
           This will be matched to the actual storage policy attached with the volume.
       datastores: Volumes located on this Datastore will be returned.
       labels: Labels to be matched for this volume.
           
             
           Label key and value should be an exact match. All volumes that match
           any of the labels will be returned in the result.
       complianceStatus: Storage policy compliance status of the volume.
           
             
           This must be one of the compliance status exposed by SPBM. See `pyVmomi.vim.vsan.host.ComplianceStatus`.
       datastoreAccessibilityStatus: Datastore accessibility status of the volume.
           
             
           This must be one of the datastore accessibility status exposed by SPBM.
           See `pyVmomi.pbm.compliance.EntityHealthStatus.DatastoreAccessibilityStatus`.
       cursor: Cursor object, pointing to desired range of results.
       healthStatus: Health status of the volume.
           
             
           This will be one of the health status exposed by SPBM.
           See `pyVmomi.pbm.compliance.EntityHealthStatus.healthStatus`.
       relocationStatus: Relocation status of the volume.
           
             
           See `pyVmomi.vim.cns.VolumeRelocationStatus` for supported values.
       attachmentStatus: Attachment status of the volume, indicating whether it is currently
           attached to a VM.
           
             
           See `pyVmomi.vim.cns.VolumeAttachmentStatus` for supported values.
   """
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
   relocationStatus: _typing.Optional[str] = None
   attachmentStatus: _typing.Optional[str] = None


class KubernetesQueryFilter(QueryFilter):
   """
   Attributes:
       namespaces: Associated Kubernetes namespaces.
       podNames: Associated Pod names.
       pvcNames: Associated PVC names.
       pvNames: Associated PV names.
   """
   namespaces: list[str] = []
   podNames: list[str] = []
   pvcNames: list[str] = []
   pvNames: list[str] = []

class MetricFormat:
   """Enumerates the metrics output format."""
   pass

class MetricType:
   """Enumerates types of metrics for 8.x and previous releases."""
   pass


class NFSAccessControlSpec(AccessControlSpec):
   """
   This class defines vSAN NFS file volume specific access control list spec.
   
     
   The access contorl spec will be treated as the delta to be added to/removed
   from the existing access control list.
   
   Attributes:
       netPermission: The permission settings of users based on the network information.
           
           This
           setting should include the IP information of the users, permission assigned
           and the user squash information.
           The accepted IP formats are:
           1\\) Single IP address, e.g., 123.23.23.123;
           2\\) IP addresses with subnet mask, e.g., 123.23.23.0/8;
           3\\) IP address ranges specified with '-', e.g., 123.23.23.123-123.23.23.128;
           4\\) The string '*' implies all clients.
           Please see `pyVmomi.vim.vsan.FileShareNetPermission`.
             
           Note that the `pyVmomi.vim.vsan.FileShareNetPermission.permissions` will
           be ignored if the delete flag is set.
       delete: Whether to delete the access control rules.
           
           If set to true, existing rules
           whose IP is matched will be deleted. If this is not set or set to false,
           the net permissions will be added to the existing permission list.
             
           Note that 1) To delete rules from the NFS, the input IP has to exactly
           match the existing rules' IP in string. Otherwise, it will be ignored;
           2\\) If there are no rules left after rules being deleted, CNS will add the
           permission {*, NO_ACCESS} as the default rule.
   """
   netPermission: pyVmomi.vim.vsan.FileShareNetPermission
   delete: _typing.Optional[bool] = None


class PlacementResult(pyVmomi.vmodl.DynamicData):
   """
   This class defines placement result for volume create operation.
   
   Attributes:
       datastore: Placement result for the datastore.
       placementFaults: Placement faults if any for the datastore.
           
           This field will be set with
           appropriate `pyVmomi.vim.fault.CnsPlacementFault` only.
             
           The selected datastore will not have any fault set.
       clusters: Clusters where the datastore is mounted on all the hosts.
           
           This field is
           populated only when the datastore is selected based on policy and
           active clusters.
   """
   datastore: pyVmomi.vim.Datastore
   placementFaults: list[pyVmomi.vmodl.MethodFault] = []
   clusters: list[pyVmomi.vim.ClusterComputeResource] = []


class QueryResult(pyVmomi.vmodl.DynamicData):
   """
   Result object for query operation.
   
   Attributes:
       volumes: Volumes that matched query criteria.
       cursor: Cursor object, pointing to next set of results, if any.
   """
   volumes: list[Volume] = []
   cursor: Cursor


class QuerySelection(pyVmomi.vmodl.DynamicData):
   """
   Query selection spec.
   
   Attributes:
       names: Selection names
             
           The property name of the volume object to return.
           
           For example,
           to get volume attributes volumeType and backingObjectDetails, pass in
           [\"volumeType\", \"backingObjectDetails\"]. See
           `pyVmomi.vim.cns.QuerySelectionNameType` for a list of enums.
             
           Given volumeId is the index, it will be selected implicitly.
             
           Not set / empty array => select volumeId only.
   """
   names: list[str] = []

class QuerySelectionNameType:
   """
   Enumerates types of query selection name.
   
   This is a reflection of the
   attributes in `pyVmomi.vim.cns.Volume`.
   """
   pass


class SnapshotCreateSpec(pyVmomi.vmodl.DynamicData):
   """
   Specifications for snapshot creation operation.
   
     
   Create snapshot with given description.
   
   Attributes:
       volumeId: Unique identifier for the volume.
       description: User description of this snapshot.
           
           CNS server does not enforce uniqueness of snapshot description
       snapshotId: CSI-provided id of the snapshot
   """
   volumeId: VolumeId
   description: str
   snapshotId: _typing.Optional[SnapshotId] = None


class SnapshotDeleteSpec(pyVmomi.vmodl.DynamicData):
   """
   Specifications for snapshot delete operation.
   
     
   Delete the snapshot with given volumeId and snapshotId.
   
   Attributes:
       volumeId: Unique identifier for the volume.
       snapshotId: Unique identifier for the snapshot.
   """
   volumeId: VolumeId
   snapshotId: SnapshotId


class SnapshotId(pyVmomi.vmodl.DynamicData):
   """
   Data object to uniquely identify a snapshot.
   
   Attributes:
       id: Unique identifier of the snapshot.
   """
   id: str


class SnapshotVolumeSource(VolumeSource):
   """
   Data object representing volume creation from a volume snapshot.
   
   Attributes:
       volumeId: Identifier of the volume.
       snapshotId: Snapshot ID of the volume.
       linkedClone: Whether linked clone operation is desired, false by default
   """
   volumeId: _typing.Optional[VolumeId] = None
   snapshotId: _typing.Optional[SnapshotId] = None
   linkedClone: _typing.Optional[bool] = None

class SyncVolumeMode:
   """
   Enumerates different modes of volume synchronization.
   
   This enumeration is used within `pyVmomi.vim.cns.SyncVolumeSpec` to specify
   the scope of a synchronization operation, allowing for partial or full updates
   of volume information. Enumerations represent non-overlapping and mutually
   exclusive set of attributes, which would be synced.
   """
   pass


class SyncVolumeSpec(pyVmomi.vmodl.DynamicData):
   """
   This class `pyVmomi.vim.cns.SyncVolumeSpec` is used to encapsulate the parameters required
   to synchronize a CNS volume.
   
   It identifies the volume to be synchronized and can optionally specify
   if only certain attribute needs to be synchronized.
   
   Attributes:
       volumeId: Unique identifier for the volume.
       datastore: Optional Datastore object where the volume belongs.
           
           This field identifies the datastore associated with the volume that needs
           to be synchronized. This field is useful when CNS does not have information
           about datastore or to optimize additional synchronization process by directing
           it to a specific datastore.
       syncMode: Array of supported synchronization mode specifying what information to be synchronize.
           
           This field provides more control over the synchronisation process. For instance, if
           configured to synchronise only space usage, the operation will update only those
           details, not all volume properties. One or more such modes can be passed.
           If none are passed, it will be a full synchronisation.
           The possible values for this field are enumerated in
           `pyVmomi.vim.cns.SyncVolumeMode`.
   """
   volumeId: VolumeId
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None
   syncMode: list[str] = []

class UnregisterTargetVolumeType:
   """Enumerates possible target volume type for unregister volume operation."""
   pass


class UnregisterVolumeSpec(pyVmomi.vmodl.DynamicData):
   """
   Specifies the parameters required to unregister a volume from the vSphere environment.
   
     
   Depending on the `pyVmomi.vim.cns.UnregisterTargetVolumeType` specified, the
   unregistration process would also optionally demote the volume to VMDK.
   
   Attributes:
       volumeId: The unique identifier of the volume to be unregistered.
       targetVolumeType: Specifies the final desired volume type after the unregistration operation.
           
           This parameter dictates how the underlying storage volume should be treated
           or converted once its CNS metadata is removed.
           
           Unregistering a block volume might convert it into a legacy VMDK or FCD
           The possible values for this field are enumerated in
           `pyVmomi.vim.cns.UnregisterTargetVolumeType`.
   """
   volumeId: VolumeId
   targetVolumeType: str


class VSANFileCreateSpec(FileCreateSpec):
   """
   Specification for vSAN file volume creation.
   
   Attributes:
       softQuotaInMb: During creation this field specifies desired soft quota for file volume
           in MB.
           
           When an existing file share is specified then this field will
           be ignored.
       permission: The permission parameters set for this file share.
           
           If this field is not set,
           then no user can access this file share.
   """
   softQuotaInMb: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   permission: list[pyVmomi.vim.vsan.FileShareNetPermission] = []


class Volume(pyVmomi.vmodl.DynamicData):
   """
   Data object captures all details about container volume.
   
     
   This is used strictly for Query `pyVmomi.vim.cns.VolumeManager.query` /
   QueryAll `pyVmomi.vim.cns.VolumeManager.queryAll` result.
   
   Attributes:
       volumeId: Unique identifier and datastore information for the volume.
       datastoreUrl: URL for datastore where the volume resides.
           
             
           This is the URL from `pyVmomi.vim.Datastore.summary`.
       name: Name of the volume.
           
             
           Name size is limited to 80 bytes. CNS will not try to
           enforce uniqueness for volume name. Different container orchestrator clusters
           can create volumes with same name. Uniqueness within a container orchestrator
           cluster, if needed, should be enforced by the cluster orchestrator during
           volume creation.
       volumeType: Type of this volume.
           
             
           See `pyVmomi.vim.cns.VolumeType` for all supported types and valid values for this field.
       storagePolicyId: Storage policy associated with the container volume.
       metadata: Metadata for this volume.
       backingObjectDetails: Additional information about the backing object for this volume, specific
           to volume type.
           
             
           See `pyVmomi.vim.cns.BackingObjectDetails` and its child-classes for more information.
       complianceStatus: Storage policy compliance status of the volume.
           
             
           This will be one of the compliance status exposed by SPBM.
           See `pyVmomi.pbm.compliance.ComplianceResult.ComplianceStatus`.
       datastoreAccessibilityStatus: Datastore accessibility status of the volume.
           
             
           This will be one of the datastore accessibility status exposed by SPBM.
           See `pyVmomi.pbm.compliance.EntityHealthStatus.DatastoreAccessibilityStatus`.
       healthStatus: Health status of the volume.
           
             
           This will be one of the health status exposed by SPBM.
           See `pyVmomi.pbm.compliance.EntityHealthStatus.healthStatus`.
       relocationStatus: Relocation status of the volume.
           
             
           See `pyVmomi.vim.cns.VolumeRelocationStatus` for supported values.
       attachmentStatus: Attachment status of the volume, indicating whether it is currently
           attached to a VM.
           
             
           See `pyVmomi.vim.cns.VolumeAttachmentStatus` for supported values.
   """
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
   relocationStatus: _typing.Optional[str] = None
   attachmentStatus: _typing.Optional[str] = None


class VolumeACLConfigureSpec(pyVmomi.vmodl.DynamicData):
   """
   Specifications for volume ACL reconfigure operation.
   
   Attributes:
       volumeId: Unique identifier for the volume.
       accessControlSpecList: List of the permission settings of users based on the network information.
           
             
           Note that only `pyVmomi.vim.cns.NFSAccessControlSpec` is supported.
   """
   volumeId: VolumeId
   accessControlSpecList: list[AccessControlSpec] = []


class VolumeAttachDetachSpec(pyVmomi.vmodl.DynamicData):
   """
   Data object for specifications for volume attach/detach operations.
   
   Attributes:
       volumeId: Unique identifier and datastore information for the volume.
       vm: VirtualMachine to which this volume needs to be attached to.
       diskMode: The disk persistence mode.
           
           Valid modes are
           vim.vm.device.VirtualDiskOption.DiskMode#persistent
           vim.vm.device.VirtualDiskOption.DiskMode#independent_persistent
           vim.vm.device.VirtualDiskOption.DiskMode#independent_nonpersistent
           vim.vm.device.VirtualDiskOption.DiskMode#nonpersistent
           vim.vm.device.VirtualDiskOption.DiskMode#undoable
           vim.vm.device.VirtualDiskOption.DiskMode#append
           When unset, default mode is persistent(that also means
           dependant persistent to CNS)
           see `pyVmomi.vim.vm.device.VirtualDiskOption.DiskMode`
       sharing: The sharing mode of the virtual disk.
           
           Valid values are
           vim.vm.device.VirtualDisk.Sharing#sharingNone
           vim.vm.device.VirtualDisk.Sharing#sharingMultiWriter
           When unset, default value is sharingNone
           See `pyVmomi.vim.vm.device.VirtualDisk.Sharing`
       controllerKey: Key of the controller the disk will connect to.
           
           It can be unset if there is only one controller
           (SCSI/SATA/NVME) with the available slot in the
           virtual machine. If there are multiple SCSI/SATA/NVME
           controllers available, user must specify
           the controller; if there is no available
           controllers, a `pyVmomi.vim.fault.MissingController`
           fault will be thrown.
       unitNumber: The unit number of the disk to be attached on its
           controller.
           
           If unset, the next free slot on the specified
           controller or on the only available controller will be
           assigned to the attached disk.
       backingTypeName: Specifies the file backing type for the volume.
           
           Valid values are defined in `pyVmomi.vim.cns.VolumeBackingType`
           
           For dynamically provisioned volumes:
           - If not provided, defaults to `pyVmomi.vim.vm.device.VirtualDisk.FlatVer2BackingInfo`
           - If provided, the specified backing type will be used.
             
           For statically provisioned volumes:
           - This field is required. If not provided, a `pyVmomi.vim.fault.CnsFault` will be thrown.
       volumeEncrypted: Indicates whether the volume is encrypted.
           
           When set to true, the volume is encrypted and vpxd API
           `pyVmomi.vim.VirtualMachine.attachVStorageObject` will be called
           for cryptographic key handling during batch attach operations.
           When set to false, the volume is not encrypted and vpxd API
           `pyVmomi.vim.VirtualMachine.attachVStorageObject` call
           will be skipped.
           When unset, regardless of the volume encryption status,
           vpxd API `pyVmomi.vim.VirtualMachine.attachVStorageObject` will be
           called to determine the volume encryption status and perform
           cryptographic key handling if the volume is encrypted.
           Note: `pyVmomi.vim.VirtualMachine.attachVStorageObject` call might
           impact performance.
   """
   volumeId: VolumeId
   vm: pyVmomi.vim.VirtualMachine
   diskMode: _typing.Optional[str] = None
   sharing: _typing.Optional[str] = None
   controllerKey: _typing.Optional[int] = None
   unitNumber: _typing.Optional[int] = None
   backingTypeName: _typing.Optional[str] = None
   volumeEncrypted: _typing.Optional[bool] = None


class VolumeAttachResult(VolumeOperationResult):
   """
   Data object for returning result of attach operation.
   
   Attributes:
       diskUUID: UUID for disk, coming via SCSI vital product data (VPD) page 0x83 for the block
           backing of this volume.
           
             
           This UUID can be used to identify this disk on the VM, e.g. for mounting purpose.
           This field will be set in case of a successful attach operation. When fault field is set,
           this value will not be set and should be ignored.
   """
   diskUUID: _typing.Optional[str] = None

class VolumeAttachmentStatus:
   """Enumerates whether a container volume is attached to a VM."""
   pass

class VolumeBackingType:
   """
   Enumerates types of backing for batch attach operations.
   
   These values correspond to VirtualDevice.FileBackingInfo subclasses.
   Note: RawDiskMappingVer2BackingInfo and PartitionedRawDiskMappingVer2BackingInfo
   are not included because they are only supported for VMware server.
   """
   pass


class VolumeCreateResult(VolumeOperationResult):
   """
   This class defines result for volume create operation.
   
   Attributes:
       name: Client specified volume name in input.
           
             
           This field will be set along with fault field because if volume creation fails,
           then there won't be any volumeId to be set in the result.CNS API will not try to
           enforce any uniqueness for volume name.
             
           But it is highly recommended to not to have duplicate volume names,
           especially for a single invocation of the create operation.
       placementResults: Placement result for every datastore in the dynamic volume
           provisioning/create request.
           
             
           The size of this array will be equal to the size of
           `pyVmomi.vim.cns.VolumeCreateSpec.datastores`.
             
           This is an optional field and will not be set for static volume
           provisioning and register volume operations.
   """
   name: _typing.Optional[str] = None
   placementResults: list[PlacementResult] = []


class VolumeCreateSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for a container volume creation.
   
   Attributes:
       name: Name of the volume.
           
             
           Name size is limited to 80 bytes. CNS will not try to
           enforce uniqueness for volume name. Different container orchestrator clusters
           can create volumes with the same name. Uniqueness within a container orchestrator
           cluster, if needed, should be enforced by the cluster orchestrator.
       volumeType: Type of the volume.
           
           See `pyVmomi.vim.cns.VolumeType`.
       volumeId: ID of the volume.
           
             
           CNS will ensure no 2 volumes have the same id.
           This field should only be used for block volumes.
       datastores: Datastores to be considered for volume placement.
           
             
           For block volume type:
           - If backing disk is not specified in backingObjectDetails,
             then this is a mandatory field. In case of multiple placement
             candidate datastores, the server would select one datastore
             (subject to change) based on various factors like available
             free space.
           - If an existing backing disk has been specified in
             backingObjectDetails, then this datastores array should not be set.
             
           For file volume type:
           - If backing file volume is not specified in backingObjectDetails,
             then this is a mandatory field. In case of multiple placement
             candidate datastores, the server would select one datastore
             (subject to change) based on various factors like available
             free space.
           - If an existing backing disk has been specified in
             backingObjectDetails, then this datastores array should not be set.
       metadata: Metadata for the container volume.
       backingObjectDetails: Additional details for the backing object for this volume.
           
             
           The details would be specific to the type of the volume. E.g. a block volume
           can have details like ID of existing disk that should back the volume. See
           `pyVmomi.vim.cns.BackingObjectDetails` and its child-classes, specific to
           volume type, for more.
       profile: Storage Profile for the container volume.
           
             
           ProfileSpec size is limited to 1. See `pyVmomi.vim.vm.ProfileSpec` and its child-classes.
           - If DefinedProfileSpec is specified, then the volume is created on the
             most free datastore compatible with the given storage policy.
           - If DefaultProfileSpec or EmptyProfileSpec is specified, then the volume is
             created on the most free datastore with that profile spec.
             
           While creating a block volume with an existing disk, the policy would be
           applied to the existing disk no matter the disk is attached to VM or detached.
           While creating a file volume with an existing file share, this field will be
           ignored.
       activeClusters: Active clusters of vSphere zones in a namespace.
           
           This list of active clusters of zones in a namespace along with Storage Profile
           is used to identify compatible datastores for volume creation.
       createSpec: Volume type specific requirements for the volume.
       volumeSource: Specification for the source of the volume creation.
           
           If set to null, a new empty volume is created.
   """
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
   """
   Specifications for volume crypto update operation.
   
   Attributes:
       volumeId: Unique identifier for the volume.
       profile: Target volume policy.
       disksCrypto: Target volume crypto.
   """
   volumeId: VolumeId
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []
   disksCrypto: _typing.Optional[pyVmomi.vim.vslm.DiskCryptoSpec] = None


class VolumeExtendSpec(pyVmomi.vmodl.DynamicData):
   """
   Specifications for volume extend operation.
   
     
   Extend operation is called to extend volume's capacity. The new
   non-negative capacity should be specified in MB.
     
   Extend operation should be called by providing at least one ExtendSpec.
   If an array of empty spec is passed, the operation will fail.
   
   Attributes:
       volumeId: Unique identifier for the volume.
       capacityInMb: New capacityInMb for the volume.
   """
   volumeId: VolumeId
   capacityInMb: pyVmomi.VmomiSupport.long


class VolumeId(pyVmomi.vmodl.DynamicData):
   """
   Data object to uniquely identify a volume.
   
   Attributes:
       id: Unique identifier of the volume.
           
           The identifier is generated by the system
           and the client cannot generate/specify an identifier for a volume.
   """
   id: str


class VolumeManager(pyVmomi.VmomiSupport.ManagedObject):
   """
   This is the interface for managing the lifecycle of volumes that are consumed
   by containers or pods, in case of Kubernetes.
   
   This managed interface can be
   accessed through MOID of cns-volume-manager, through vSAN service in vCenter.
     
   Lifecycle of a container volume includes creation, update, query, attach,
   detach and delete operations. This interface and its related classes are the entry
   point for Cloud Native Storage (abbreviated to CNS) service.
     
   These requests could come from different container orchestrator clusters running
   on same vSphere as associated with this VolumeManager. VolumeManager is not
   aware of presence and topology of container orchestrator clusters, except
   for the weak association via `pyVmomi.vim.cns.ContainerCluster`. This is a weak
   association because it's client's responsibility to provide unique identity
   for this container orchestrator cluster. VolumeManager will not impose any
   uniqueness verification on cluster identification.
     
   Provisioning APIs of this interface return vim.Task which is vCenter Task
   object to track the progress of operation. In case of either partial or
   complete success, the state of the task would be set to success. In case
   of complete failure of the task when the individual specs couldn't be scheduled,
   the task status would be set to error. The corresponding fault, if any, will be
   set in the fault field. For a successfully scheduled task, result of this
   operation will be a list of `pyVmomi.vim.cns.VolumeOperationResult` instances.
   The client needs to go through the result and check the successful and failed
   instances.
     
   The Task returned by provisioning APIs is a vim.Task object. Client needs to
   connect to vim endpoint on vCenter using the latest VSAN VMODL version
   (not latest VIM version) to monitor task status. After the task is complete,
   clients can refer to `pyVmomi.vim.cns.VolumeOperationResult` set as result field in
   task's `pyVmomi.vim.TaskInfo` field.
     
   Please refer to the required privileges in the individual API documentation and ignore
   the Required Privileges section which is not used.
   """
   def Create(self, createSpecs: list[VolumeCreateSpec]) -> pyVmomi.vim.Task:
      """
      Creates container volume with given specifications.
      
        
      Following privileges will be required on specified entities, to perform
      this operation. For dynamic provisioning, the datastores that does not
      have the necessary privileges will be ignored and other datastores that
      have the necessary privileges will be considered for volume placement.
      - Datastore.FileManagement on datastores specified in input, required for
        block volume only
      - Host.Config.Storage on vSAN file service enabled vSAN cluster,
        required for file volume only
      - StorageProfile.View on RootFolder to access storage policy specified in input
        
      Faults that can be set in individual result entry, corresponding to each
      VolumeCreateSpec instance in input:
      - vmodl.fault.InvalidArgument set in case of invalid input arguments,
        invalid formats, invalid combination of
        inputs.
      - vim.fault.NotFound set in case the existing disk that should
        be used to back the container volume cannot be found.
      - vim.fault.CnsFault set in case of any other failure scenario.
      - vim.fault.CnsVolumeAlreadyExistsFault
        set in case volume already exists on a different datastore.
      
      Args:
          createSpecs: Specifications for volumes to be created.
      
      Returns:
          `pyVmomi.vim.Task` to track the progress and overall state of this
          operation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: For block volume, if the input spec is invalid like
              createSpecs size is not equal to 1, backing disk ID
              in backing object details is empty and datastores is
              empty, volume metadata in input spec is invalid,
              backing disk ID in backing object details is not
              present, datastore is invalid, entityMetadata
              containing duplicate entity types, profile size
              is not equal to 1 etc.
                
              For file volume, if the input spec is invalid like
              createSpecs size is not equal to 1, volume metadata
              in input spec is invalid, backing disk ID in backing
              object details is not present, entityMetadata
              containing duplicate entity types, profile size
              is not equal to 1 etc.
          pyVmomi.vim.fault.NotFound: if the volume can not be found.
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenario.
      """
      ...
   def UpdateVolumeMetadata(self, updateSpecs: list[VolumeMetadataUpdateSpec]) -> pyVmomi.vim.Task:
      """
      Updates volume metadata, namely labels and container cluster information for the
      container volumes.
      
        
      Following privileges will be required on specified entities, to perform
      this operation:
      - Datastore.FileManagement on datastores specified in input, required for
        block volume only
      - Host.Config.Storage on vSAN file service enabled vSAN cluster, required
        for file volume only
        
      Faults that can be set in individual result entry, corresponding to each
      VolumeMetadataUpdateSpec instance in input:
      - vmodl.fault.InvalidArgument set in case of invalid but non-empty
        volume id.
      - vim.fault.NotFound set in case of the volume can not be found.
      - vim.fault.CnsFault set in case of any other failure scenario.
      
      Args:
          updateSpecs: Specifications for volumes to be updated.
      
      Returns:
          `pyVmomi.vim.Task` vCenter Task to track the progress and overall state
          of this operation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if:
              - Input size is not equal to 1
              - Volume id in input spec is empty.
              - Volume metadata in input spec has empty
                cluster info.
              - Entity objects in volume metadata has empty or
                invalid attributes.
              - EntityMetadata in volume metadata contains
                duplicate entity types.
          pyVmomi.vim.fault.NotFound: if the volume can not be found.
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenario.
      """
      ...
   def Delete(self, volumeIds: list[VolumeId], deleteDisk: bool) -> pyVmomi.vim.Task:
      """
      Deletes given container volumes.
      
        
      Multiple requests for a volume, when deletion is already in progress, will
      not return any fault. This operation will make the volume unavailable for
      any attach, update and query operation.
        
      Following privileges will be required on specified entities, to perform
      this operation:
      - Datastore.FileManagement on all involved Datastores, required for block
        volume only
      - Host.Config.Storage on vSAN file service enabled vSAN cluster,
        required for file volume only
        
      Faults that can be set in individual result entry, corresponding to each
      volume ID instance in input:
      - vmodl.fault.InvalidArgument set in case of empty volume ID
      - vim.fault.NotFound set in case of the volume can not be found.
      - vim.fault.ResourceInUse set when volume has been attached to a VM
        and is in use, client needs to first detach
        the volume from that VM and then retry this
        operation.
      - vim.fault.CnsFault set in case of any other failure scenario.
      
      Args:
          volumeIds: List of `pyVmomi.vim.cns.VolumeId` for the volumes to be
              deleted.
          deleteDisk: Disk is the backing object for each container volume
              specified in volumeIds list. If set to true, the backing
              objects specified in volumeIds list will be deleted. If
              set to false, the backing objects specified in volumeIds
              list will not be deleted but will no longer be a
              container volume.
      
      Returns:
          `pyVmomi.vim.Task` to track the progress and overall state of this
          operation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: This API supports input size of 1 only. If
              more or less than one entries are passed as
              input, this exception will be thrown and
              operation will fail.  
              This exception will be thrown when invalid
              format for VolumeId `pyVmomi.vim.cns.VolumeId.id`
              is passed, or volume IDs are empty.
          pyVmomi.vim.fault.NotFound: if the volume can not be found.
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenario.
          pyVmomi.vim.fault.ResourceInUse: if the volume has been attached to a VM and is in
              use, client needs to first detach the volume
              from that VM and then retry this operation.
      """
      ...
   def Attach(self, attachSpecs: list[VolumeAttachDetachSpec]) -> pyVmomi.vim.Task:
      """
      Attaches volumes(block volumes only) to specified VM instances, to make
      volumes ready for mount and consumption by respective containers.
      
        
      For each volume in input, this API will attach block backing for this volume
      to the VirtualMachine specified in input, via one of the available slots on
      SCSI controller. This API will transparently add new SCSI controller to the
      VirtualMachine, if needed.
        
      Following privileges will be required on specified entities, to perform
      this operation:
      - Datastore.FileManagement on datastores specified in input, required for
        block volume only
      - VirtualMachine.Config.AddExistingDisk on VM specified in the input
      - VirtualMachine.Config.AddRemoveDevice on VM specified in the input
        
      Faults that can be set in individual result entry, corresponding to each
      VolumeAttachDetachSpec instance in input:
      - vmodl.fault.InvalidArgument set in case of invalid input arguments, like
        empty strings, invalid formats, invalid
        combination of inputs.
      - vmodl.fault.ManagedObjectNotFound set in case of the VM can not be
        found.
      - vim.fault.NotFound set in case of the volume can not be
        found.
      - vim.fault.ResourceInUse set when volume has been attached to a VM
        and is in use, client needs to first detach
        the volume from that VM and then retry this
        operation.
      - vim.fault.CnsMissingControllerFault set if the virtual machine has no
        available controller when controllerKey is
        unset, it is inherited from
        vim.fault.CnsFault.
      - vim.fault.CnsFault set in case of any other failure
        scenario.
      
      Args:
          attachSpecs: Specification for attach operation
      
      Returns:
          `pyVmomi.vim.Task` to track the progress and overall state of this
          operation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: This API supports input size of 1 only. If
              more or less than one entries are passed as
              input, this exception will be thrown and
              operation will fail. This fault will occur in
              cases where the volume ID is empty, VM
              is not present, volume type is FILE etc.
          pyVmomi.vmodl.fault.ManagedObjectNotFound: if the VM can not be found.
          pyVmomi.vim.fault.ResourceInUse: if the volume has been attached a VM and is in
              use, client needs to first detach the volume
              from that VM and then retry this operation.
          pyVmomi.vim.fault.NotFound: if the volume can not be found.
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenario.
      """
      ...
   def Detach(self, detachSpecs: list[VolumeAttachDetachSpec]) -> pyVmomi.vim.Task:
      """
      Detaches volumes(block volumes only) and makes those volumes unavailable
      for consumption.
      
      If a volume is already detached, this operation will pass,
      without any failure for that volume.
        
      Following privileges will be required on specified entities, to perform
      this operation:
      - Datastore.FileManagement on datastores specified in input, required for
        block volume only
      - VirtualMachine.Config.RemoveDisk on VM specified in the input
        
      Faults that can be set in individual result entry, corresponding to each
      VolumeAttachDetachSpec instance in input:
      - vmodl.fault.InvalidArgument set in case of invalid input arguments, like
        empty strings, invalid formats, invalid
        combination of inputs, such as the volume is
        not attached to any VM, or the volume is not
        attached to the VM specified, volume type if
        FILE etc.
      - vmodl.fault.ManagedObjectNotFound set in case of the VM can not be
        found.
      - vim.fault.NotFound set in case of the volume can not be found.
      - vim.fault.CnsFault set in case of any other failure scenario.
      
      Args:
          detachSpecs: Specification for detach operation
      
      Returns:
          `pyVmomi.vim.Task` to track the progress and overall state of this
          operation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: This API supports input size of 1 only. If
              more or less than one entries are passed as
              input, this exception will be thrown and
              operation will fail. This fault will occur
              when the volume is not attached to any VM or
              the volume is not attached to the VM specified
              or the volume ID is empty etc.
          pyVmomi.vmodl.fault.ManagedObjectNotFound: if the VM can not be found.
          pyVmomi.vim.fault.NotFound: if the volume can not be found.
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenario.
      """
      ...
   def QueryAsync(self, filter: QueryFilter, selection: _typing.Optional[QuerySelection]) -> pyVmomi.vim.Task:
      """
      Returns container volumes matching criteria set in the filter.
      
        
      This API will return partial results even when some of the volume IDs
      are invalid or non-existent. Invalid inputs, like empty volume ID or
      unknown volume ID, will be excluded from the results. For valid inputs,
      if the output doesn't contain information for that volume that would
      mean that CNS is not aware of the existence of that volume. Note that
      there could be duplicate volumes or missing volumes across multiple
      pages returned by this API when there are parallel volume provisioning
      operations like create, delete are in progress.
        
      Following privileges will be required on specified entities, to perform
      this operation:
      - Cns.Searchable on RootFolder to search over all container volumes
      
      Args:
          filter: All container volumes matching the criteria set in the filter
              will be returned. A maximum of 1000 volume ids can be provided.
              See `pyVmomi.vim.cns.QueryFilter`
          selection: Selection spec for the query entities to return.
              This is an optional parameter. All volume fields would be returned
              if the parameter is not specified. See `pyVmomi.vim.cns.QuerySelection`
      
      Returns:
          `pyVmomi.vim.Task` to track the progress and result of this operation.
          For result type in task, see `pyVmomi.vim.cns.AsyncQueryResult`
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: Thrown in case of invalid input arguments, like empty
              strings, invalid formats, invalid combination of
              inputs
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenarios
      """
      ...
   def Query(self, filter: QueryFilter, selection: _typing.Optional[QuerySelection]) -> QueryResult:
      """
      Returns container volumes matching criteria set in the filter.
      
        
      This API will return partial results even when some of the volume IDs
      are invalid or non-existent. Invalid inputs, like empty volume ID or
      unknown volume ID, will be excluded from the results. For valid inputs,
      if the output doesn't contain information for that volume that would
      mean that CNS is not aware of the existence of that volume. Note that
      there could be duplicate volumes or missing volumes across multiple
      pages returned by this API when there are parallel volume provisioning
      operations like create, delete are in
      progress.
        
      Following privileges will be required on specified entities, to perform
      this operation:
      - Cns.Searchable on RootFolder to search over all container volumes
      
      Args:
          filter: All container volumes matching the criteria set in the filter
              will be returned. A maximum of 1000 volume ids can be provided.
              See `pyVmomi.vim.cns.QueryFilter`
          selection: Selection spec for the query entities to return.
              This is an optional parameter. All volume fields would be returned
              if the parameter is not specified. See `pyVmomi.vim.cns.QuerySelection`
      
      Returns:
          array of `pyVmomi.vim.cns.Volume` matching the input criteria
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: Thrown in case of invalid input arguments, like empty
              strings, invalid formats, invalid combination of
              inputs
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenarios
      """
      ...
   def ConfigureVolumeACLs(self, ACLConfigSpecs: list[VolumeACLConfigureSpec]) -> pyVmomi.vim.Task:
      """
      Modify the ACL configurations for existing volumes.
      
      Multiple requests
      configuring the same volume at the same time will be serialized in CNS.
        
      Note that this API is currently supported for file volumes only.
        
      Following privileges will be required on file volumes, to perform
      this operation:
      - Host.Config.Storage on vSAN file service enabled vSAN cluster,
        required for file volume only
        
      Faults that can be set in individual result entry, corresponding to each
      `pyVmomi.vim.cns.VolumeACLConfigureSpec` instance in input:
      - vmodl.fault.InvalidArgument Set if the input spec has invalid field.
      - vim.fault.NotFound Set in case of the volume can not be found.
      - vim.fault.CnsFault Set in case of any other failure scenarios.
      
      Args:
          ACLConfigSpecs: Specifications for volumes ACL configuration.
      
      Returns:
          `pyVmomi.vim.Task` to track the progress and overall state of this
          operation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: Thrown if: 1) two or more ACLConfigSpec instances
              are passed; 2) the volume ID is empty; 3) file
              service reports the invalid inputs.
          pyVmomi.vim.fault.NotFound: Thrown if the volume or cluster can not be found
              by CNS.
          pyVmomi.vim.fault.CnsFault: Thrown for any other authorization failure scenrios.
      """
      ...
   def Extend(self, extendSpecs: list[VolumeExtendSpec]) -> pyVmomi.vim.Task:
      """
      Extend the capacity for the container volumes.
      
        
      Following privileges will be required on specified entities, to perform
      this operation:
      - Datastore.FileManagement on datastore where the volume is placed,
        required for block volume only
      - Host.Config.Storage on vSAN file service enabled vSAN cluster,
        required for file volume only
        
      Faults that can be set in individual result entry, corresponding to each
      VolumeExtendSpec instance in input:
      - vmodl.fault.InvalidArgument set in case of invalid input arguments,
        like empty strings, invalid formats,
        invalid combination of inputs.
      - vim.fault.NotFound set in case of the volume can not be found.
      - vim.fault.CnsFault set in case of any other failure scenario.
      
      Args:
          extendSpecs: Specifications for volumes to be extended.
      
      Returns:
          `pyVmomi.vim.Task` to track the progress and overall state of this
          operation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: This API supports input size of 1 only. If
              more or less than one entries are passed as
              input, this exception will be thrown and
              operation will fail.
              This API requires the new capacity of the
              volume specified in ExtendSpec is bigger
              than 0, this exception will be thrown and
              operation will fail.
          pyVmomi.vim.fault.NotFound: if the volume can not be found.
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenario.
      """
      ...
   def CreateSnapshots(self, snapshotSpecs: list[SnapshotCreateSpec]) -> pyVmomi.vim.Task:
      """
      Create snapshots of given volumes
        
      A volume with snapshot created on it, is considered in use
      and cannot be deleted.
      
      Create snapshot operation should be called by providing at least one SnapshotCreateSpec.
      If an array of empty spec is passed, the operation will fail.
      Return a task that tracks the status and result of snapshot
      operation.
      Following privileges will be required on specified entities, to perform
      this operation:
      - Datastore.FileManagement on all involved Datastores
      
      Returns:
          `pyVmomi.vim.Task` to track the progress and result
          of this operation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: This API supports input size of 1 only. If
              more or less than one entries are passed as
              input, this exception will be thrown and
              operation will fail.
              This exception will be thrown when invalid
              format for VolumeId `pyVmomi.vim.cns.VolumeId.id`
              is passed, or volume IDs are empty etc.
          pyVmomi.vim.fault.NotFound: if the volume can not be found.
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenario.
      """
      ...
   def DeleteSnapshots(self, snapshotDeleteSpecs: list[SnapshotDeleteSpec]) -> pyVmomi.vim.Task:
      """
      Delete snapshots with given volumeIds and snapshotIds.
      
        
      Delete snapshot operation should be called by providing at least one SnapshotDeleteSpec
      If an array of empty spec is passed, the operation will fail.
      Return a task that tracks the status and result of delete operation
      per given volume.
      Following privileges will be required on specified entities, to perform
      this operation:
      - Datastore.FileManagement on all involved Datastores
      
      Returns:
          `pyVmomi.vim.Task` to track the progress and result
          of this operation.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the volume or snapshot can not be found.
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenario.
      """
      ...
   def Relocate(self, relocateSpecs: list[VolumeRelocateSpec]) -> pyVmomi.vim.Task:
      """
      Relocate container volume from the current source datastore to another
      destination datastore.
      
      Currently, it supports for a single block volume only.
        
      This API comes with the following limitations:
      - Any CNS control operations like attach, detach, update, expand, etc on a
        volume being relocated or any other volume attached
        to the same VM as the volume being relocated will
        fail with CnsFault, see `pyVmomi.vim.fault.CnsFault`.
      - VMC is not fully supported for this API.
      - Please see guidelines and
        limitations of CNS relocate on vSphere.
        
        
      If an array of empty spec is passed or the size of the input spec is not
      equal to 1, the operation will fail.
        
      Following privileges will be required on specified entities, to perform
      this operation.
      - Datastore.FileManagement on both the source datastore, and the
        destination datastore specified in input,
        which is required for block volume only
      - Resource.ColdMigrate on the virtual machine that volume is attached to,
        which is required for attached block volume only.
      - Datastore.AllocateSpace on the target datastore
      - Resource.HotMigrate on the virtual machine that volume is attached to,
        if the vm is powered on, which is required for
        attached block volume only
        
      Faults that can be set in individual result entry, corresponding to each
      VolumeRelocateSpec instance in input:
      - vmodl.fault.InvalidArgument set in case of invalid input arguments,
        invalid formats.
      - vim.fault.NotFound set in case the volume or datastore in the spec
        can not be found.
      - vim.fault.CnsFault set in case of any other failure scenarios.
      
      Args:
          relocateSpecs: Specifications for volumes to be relocated. Block volume
              relocation should use the child class spec, see
              `pyVmomi.vim.cns.BlockVolumeRelocateSpec`.
      
      Returns:
          `pyVmomi.vim.Task` to track the progress and overall state of this
          operation.
      
      Raises:
          pyVmomi.vim.fault.AlreadyExists: Thrown in case volume is already migrated to the
              specified destination datastore.
          pyVmomi.vmodl.fault.InvalidArgument: Thrown in case of invalid input arguments, such as
              invalid volume or datastore format, or empty volume
              IDs
          pyVmomi.vim.fault.NotFound: if the volume or datastore can not be found.
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenario.
      """
      ...
   def ReconfigPolicy(self, volumePolicyReconfigSpecs: list[VolumePolicyReconfigSpec]) -> pyVmomi.vim.Task:
      """
      Reconfigures the volume with the storage policy.
      
      Currently the API is supported for only block volumes and only supports applying
      the currently associated policy.
        
      Following privileges will be required on specified entities, to perform
      this operation:
      - Datastore.FileManagement on datastores specified in input, required for
        block volume only
      - StoragePolicy.View on policy in the spec
      
      Args:
          volumePolicyReconfigSpecs: An array of spec ,
              currently only array of size 1 is supported.
      
      Returns:
          `pyVmomi.vim.Task` vCenter Task to track the progress and overall state
          of this operation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if:
              - Input size is not equal to 1
              - Volume id in input spec is empty.
              - Policy string is empty.
          pyVmomi.vim.fault.NotFound: if the volume can not be found.
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenario.
      """
      ...
   def UpdateVolumeCrypto(self, updateSpecs: list[VolumeCryptoUpdateSpec]) -> pyVmomi.vim.Task:
      """
      Updates volume crypto, namely encrypt, deep recrypt, shallow recrypt,
      and decrypt for the container block volumes and all the disks in the chain.
      
        
      Following privileges will be required on specified entities, to perform
      this operation:
      - Datastore.FileManagement on all involved datastores, required for
        block volumes only
      - Cryptographer.Encrypt on all involved datastores and on the virtual machines volumes
        are attached to, required for block volumes update encrypt
      - Cryptographer.Recrypt on all involved datastores and on the virtual machines volumes
        are attached to, required for block volumes update deep or shallow recrypt
      - Cryptographer.Decrypt on all involved datastores and on the virtual machines volumes
        are attached to, required for block volumes update decrypt
        
      Faults that can be set in individual result entry, corresponding to each
      VolumeCryptoUpdateSpec instance in input:
      - vmodl.fault.InvalidArgument set in case of invalid but non-empty
        volume id.
      - vim.fault.NotFound set in case of the volume can not be found.
      - vim.fault.CnsFault set in case of any other failure scenario.
      
      Args:
          updateSpecs: Specifications for volumes to be crypted.
      
      Returns:
          `pyVmomi.vim.Task` vCenter Task to track the progress and overall state
          of this operation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if:
              - Input size is not equal to 1
              - Volume id in input spec is empty.
              - `VolumeCryptoUpdateSpec.disksCrypto.crypto`
                is unset.
              - `VolumeCryptoUpdateSpec.disksCrypto.parent`
                is set.
          pyVmomi.vim.fault.NotFound: if the volume can not be found.
          pyVmomi.vim.fault.CnsFault: Thrown for all other failure scenario.
          pyVmomi.vim.fault.CnsNotRegisteredFault: if the volume exists in VC but not registered as CNS
              volume.
      """
      ...
   def UnregisterVolume(self, unregisterSpec: list[UnregisterVolumeSpec]) -> pyVmomi.vim.Task:
      """
      Initiates an asynchronous operation to unregister volume.
      
        
      Unregistration removes the CNS metadata associated with the specified volumes,
      it also optionally converts to a targer volume type as specified in the
      `pyVmomi.vim.cns.UnregisterVolumeSpec.targetVolumeType`. This API is only
      supported for the block volume.
        
      This is an asynchronous operation, it returns a `pyVmomi.vim.Task` object
      which can be used to monitor the progress and completion status of the
      unregistration process.
      
      Args:
          unregisterSpec: An array of `pyVmomi.vim.cns.UnregisterVolumeSpec` objects,
              each specifying a unique volume or PVC to be unregistered
              along with optional parameters for its post-unregistration
              state. At most one specification is supported for this operation.
      
      Returns:
          `pyVmomi.vim.Task` to track the progress and result of this operation.
          The task's result will indicate the success of the unregistration
          for all specified volumes.
            
          Following privileges will be required on specified entities, to perform
          this operation:
          - Datastore.FileManagement on datastores specified in input, required for
            block volume only
      
      Raises:
          pyVmomi.vim.fault.NotFound: Thrown if any of the `volumeId`s specified in the
              `unregisterSpec` do not correspond to an
              existing PVC in the CNS inventory.
          pyVmomi.vim.fault.InvalidState: Thrown if a volume specified is in a state that prevents
              unregistration.
          pyVmomi.vim.fault.InvalidDatastore: Thrown if the operation cannot be performed on the datastore.
          pyVmomi.vim.fault.TaskInProgress: Thrown if the virtual storage object is busy.
          pyVmomi.vmodl.fault.InvalidArgument: if:
              - This API supports input size of 1 only. If
                more or less than one entries are passed as
                input, this exception will be thrown.
              - This exception will be thrown when invalid
                format for VolumeId `pyVmomi.vim.cns.VolumeId.id`
                is passed, or volume IDs are empty.
              - This exception will be thrown when volume Id does
                not belong to block volume.
          pyVmomi.vim.fault.CnsFault: Thrown if a general CNS-specific error occurs during the
              unregistration process that is not covered by more
              specific faults.
      """
      ...
   def SyncVolume(self, syncSpecs: list[SyncVolumeSpec]) -> pyVmomi.vim.Task:
      """
      Initiates a task to synchronize one or more volumes based on the provided specifications.
      
      This method allows for syncing volume properties for a single volume only.
      The operation is asynchronous and returns a `Task` object that can be used
      to monitor the progress and outcome of the synchronization. This API supported only
      for block volume.
      
      Args:
          syncSpecs: Specification for volume to be synchronized.
              At most one specification is supported for this operation.
      
      Returns:
          `vim.Task` vCenter Task to track the progress and overall state
          of this operation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if:
              - The volume ID in an input spec is empty or malformed
              - This API supports input size of 1 only. If
                more or less than one entries are passed as
                input, this exception will be thrown.
          pyVmomi.vim.fault.NotFound: if a volume specified in `syncSpecs` does not exist on the system.
          pyVmomi.vim.fault.CnsFault: Thrown for all other CNS-related failure scenarios, such as issues
              with the CNS infrastructure or backend storage.
      """
      ...
   def DeleteAllSnapshots(self, volumeId: VolumeId) -> pyVmomi.vim.Task:
      """
      This api allows user to delete all snapshots of a particular block volume.
      
      It returns a task
      whose result type is `pyVmomi.vim.cns.SnapshotDeleteAllResult`
      
      Args:
          volumeId: target volume where user wants to delete all its snapshots.
      
      Returns:
          `pyVmomi.vim.Task` to track the progress and overall state of this
          operation.
      
      Raises:
          pyVmomi.vmodl.fault.InvalidArgument: if:
              - The volume ID in the input spec is empty or malformed
              - The volume specified is not a block volume.
          pyVmomi.vim.fault.NotFound: if the volume specified does not exist on the system.
          pyVmomi.vim.fault.CnsFault: for all other failure scenarios.
                
              Following privileges will be required on specified entities, to perform
              this operation:
              - Datastore.FileManagement on the volume's datastore
      """
      ...


class VolumeMetadata(pyVmomi.vmodl.DynamicData):
   """
   Data object that represents metadata associated with a container volume.
   
   Attributes:
       containerCluster: Represents the container orchestrator cluster where the volume
           is used.
           
             
           Volume metadata will be associated with the container volume
           for this container cluster during volume create and update
           operations. In case the block container volume is created in
           one container cluster but used in a different container cluster
           (static volume provisioning use case), an update volume operation
           with a new container cluster will replace the old entry.
       entityMetadata: All the entity metadata associated with the container volume within a
           container orchestrator like Kubernetes.
       containerClusterArray: Represents list of all container orchestrator clusters
           where the volume is used.
           
           This field is mandatory in versions
           that support it.
   """
   containerCluster: ContainerCluster
   entityMetadata: list[EntityMetadata] = []
   containerClusterArray: list[ContainerCluster] = []


class VolumeMetadataUpdateSpec(pyVmomi.vmodl.DynamicData):
   """
   Specifications for volume metadata update operation.
   
   The update is performed based on the specified entity metadata
   in volume metadata.
     
   For metadata add/update - if CNS already had entity metadata associated,
   then this update will replace it. Else, it will associate the entity metadata
   with the volume.
     
   For metadata deletion - CNS will delete the speficied entity metadata.
     
   Update operation should be called for at least one update. If an empty spec
   is passed without any volume properties to be updated, the operation will fail.
   
   Attributes:
       volumeId: Unique identifier for the volume.
       metadata: Metadata for the container volume.
   """
   volumeId: VolumeId
   metadata: VolumeMetadata


class VolumeOperationBatchResult(pyVmomi.vmodl.DynamicData):
   """
   Wrapper class to pass array of `pyVmomi.vim.cns.VolumeOperationResult` as
   `pyVmomi.vim.Task` result field, which can only be set to a single object
   otherwise.
   
   Attributes:
       volumeResults: Result for volume operation, performed for multiple input entries.
           
             
           This is a mandatory field and should be set to non-empty array. For create operation,
           all objects in this array would be of type `pyVmomi.vim.cns.VolumeCreateResult`.
           For attach operation, all objects in this array would be of type
           `pyVmomi.vim.cns.VolumeAttachResult`.
   """
   volumeResults: list[VolumeOperationResult] = []


class VolumePolicyReconfigSpec(pyVmomi.vmodl.DynamicData):
   """
   Specifications for volume policy update.
   
   Attributes:
       volumeId: Unique identifier for the volume.
       profile: Target volume policy.
           
           Currently user need to use only DefinedProfileSpec. i.e. EmptyProfileSpec
           and DefaultProfileSpec are not supported.
   """
   volumeId: VolumeId
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []


class VolumeRelocateResult(VolumeOperationResult):
   """
   Data object for returning result of relocate operation.
   
   Attributes:
       profile: Storage policy associated with the volume after relocation.
           
             
           ProfileSpec size is limited to 1. See `pyVmomi.vim.vm.ProfileSpec` and its child-classes.
           ProfileSpec is a generic vSphere SPBM construct that allows multiple
           solution-specific profiles to be attached to a single entity; CNS only
           integrates with the storage policy solution, so only one element is
           ever meaningful here.
             
           This is set only if the volume's storage policy changed as a result of
           the relocation, for example when `pyVmomi.vim.cns.VolumeRelocateSpec.profile`
           was unset and the destination datastore's default policy was applied
           instead of the volume's current policy.
           This field will be set only in case of a successful relocate operation.
           When fault field is set, this value will not be set and should be ignored.
   """
   profile: list[pyVmomi.vim.vm.ProfileSpec] = []

class VolumeRelocationStatus:
   """Enumerates relocation status for a container volume."""
   pass

class VolumeType:
   """
   Enumerate types of container volume based on the type of backing for the
   volume.
   """
   pass


class VsanFileShareBackingDetails(FileBackingDetails):
   """
   Details for a vSAN file share backing for container volume.
   
   Attributes:
       name: vSAN file share name.
           
             
           This field is ignored while creating the volume. However, this field
           is populated with the name of the vSAN file share while returning
           it in Query APIs.
       accessPoints: A key-value pair indicating the access points for the file share.
           
           The key of
           an access point is the type of the protocol, and the value of the access
           point is the connection string for accessing the file share.
             
           The supported type of protocol string is NFSv4.1/NFSv3.
             
           This field is ignored while creating the volume. However, this field
           is populated with the access points of the file share while returning
           it in Query APIs.
       permission: The permission parameters set for this file share.
           
           If this field is not set,
           for NFS then no user can access this file share.
             
           This field is ignored from `pyVmomi.vim.cns.VolumeCreateSpec` while creating
           the volume. However, this field is set in the query APIs.
   """
   name: _typing.Optional[str] = None
   accessPoints: list[pyVmomi.vim.KeyValue] = []
   permission: list[pyVmomi.vim.vsan.FileShareNetPermission] = []
