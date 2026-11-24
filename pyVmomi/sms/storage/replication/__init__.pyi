# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.sms.provider
import pyVmomi.vim.vm.replication



class DeviceId(pyVmomi.vmodl.DynamicData):
   """Base class that represents a replicated device."""
   pass


class FailoverParam(pyVmomi.vmodl.DynamicData):
   """
   Input to the failover or testFailover methods.
   
   Attributes:
       isPlanned: Whether the failover is a planned failover or not.
           
           Note that testFailover
           can also be executed in an unplanned mode. When this flag is
           set to false, the recovery VASA provider must not try to connect
           to the primary VASA provider during the failover.
       checkOnly: Do not execute the (test) failover but check if the configuration
           is correct to execute the (test) failover.
           
           If set to `true`, the (test)failover result is an array where
           each element is either `pyVmomi.sms.storage.replication.GroupOperationResult` or `pyVmomi.sms.storage.replication.GroupErrorResult`.
           
           If set to `false`, the (test)failover result is an array where
           each element is either `pyVmomi.sms.storage.replication.FailoverSuccessResult` or `pyVmomi.sms.storage.replication.GroupErrorResult`.
       replicationGroupsToFailover: The replication groups to failover.
           
           It is OK for the VASA
           provider to successfully failover only some groups. The
           groups that did not complete will be retried.
       policyAssociations: Storage policies for the devices after (test)failover.
           
           Failover should be done even if policies cannot be associated.
           Test failover, however, should fail if policies cannot be associated.
           
           If policies cannot be associated, VASA provider can notify the client by
           doing either or both of these:
           1\\. Set the warning in the result for a replication group to indicate
           such a failure to set the policy.
           2\\. Raise a compliance alarm after the failover is done.
           
           If not specified, the default policies are used. Callers may reassign
           policy later.
   """
   class ReplicationGroupData(pyVmomi.vmodl.DynamicData):
      """
      Describes one Replication Group's data.
      
      Attributes:
          groupId: Replication group to failover.
          pitId: The PIT that should be used for (test)Failover.
              
              Use the latest if not specified.
      """
      groupId: pyVmomi.vim.vm.replication.ReplicationGroupId
      pitId: _typing.Optional[PointInTimeReplicaId] = None

   class PolicyAssociation(pyVmomi.vmodl.DynamicData):
      """
      Describes the policy association object.
      
      Attributes:
          id: The source device id.
              
              The corresponding recovered device
              gets the specified `policyId`.
          policyId: Policy id.
          datastore: Datastore object.
      """
      id: DeviceId
      policyId: str
      datastore: pyVmomi.vim.Datastore

   isPlanned: bool
   checkOnly: bool
   replicationGroupsToFailover: list[FailoverParam.ReplicationGroupData] = []
   policyAssociations: list[FailoverParam.PolicyAssociation] = []


class GroupOperationResult(pyVmomi.vmodl.DynamicData):
   """
   The base class for any operation on a replication group.
   
   Usually, there is an
   operation specific <Operation>SuccessResult
   
   Attributes:
       groupId: Replication group Id.
   """
   groupId: pyVmomi.vim.vm.replication.ReplicationGroupId
   warning: list[pyVmomi.vmodl.MethodFault] = []


class FailoverSuccessResult(GroupOperationResult):
   """
   Results of a successful failover operation.
   
   The target fault domain Id, and the device group id are inherited.
   
   Attributes:
       newState: Some replicators may automatically reverse replication on failover.
           
           Such
           replicators must move the replication status to
           `SOURCE`
           In other cases, it can remain as `FAILEDOVER`.
       pitId: Id of the Point in Time snapshot used during failover.
           
           If not present,
           latest PIT was used.
       pitIdBeforeFailover: Optional id of the Point in Time snapshot that was automatically created before
           failing over.
           
           This is recommended so users can revert back to this
           snapshot to avoid data loss. This can be removed after the reverse
           replication call succeeds.
       recoveredDeviceInfo: Recovered Devices.
           
           This is optional because in some corner cases the
           replication groups on the target site may not have any virtual volumes.
       timeStamp: Time stamp of recovery.
   """
   class RecoveredDiskInfo(pyVmomi.vmodl.DynamicData):
      """
      Describes the recovered disks for a given virtual machine.
      
      Only applicable for VAIO based replicators. Upon recovery,
      all the replicated disks must be attached to the virtual machine,
      i.e. the VMX file must refer to the correct file paths. Device
      keys must be preserved and non-replicated disks can refer to
      non-existent file names.
      Array based replicators can ignore this class.
      
      Attributes:
          deviceKey: Virtual disk key.
              
              Note that disk device
              keys must not change after recovery - in other words, the device
              key is the same on both the source and target sites.
              
              For example, if a VMDK d1 is being replicated to d1', and d1 is attached as device
              2001 to the source VM, the recovered VM should have d1' attached
              as 2001.
          dsUrl: URL of the datastore that disk was recovered to.
          diskPath: Full pathname of the disk.
      """
      deviceKey: int
      dsUrl: str
      diskPath: str

   class RecoveredDevice(pyVmomi.vmodl.DynamicData):
      """
      Represents the device after the failover.
      
      Even though many of the fields in this structure are
      marked optional, it is important for VASA provider to
      make sure that the recovery of the entire ReplicationGroup succeeds
      atomically. The only valid scenario when there is a device specific
      recovery failure is when there is no valid replica for the Virtual Volume
      (e.g. Virtual Volume was just added to the ReplicationGroup).
      
      Attributes:
          targetDeviceId: Identifier of the device which was the target of replication before
              failover.
          recoveredDeviceId: Identifier of the target device after test or failover.
          sourceDeviceId: Identifier of the source of the replication data before the failover
              stopped the replication.
          info: Informational messages.
          datastore: Datastore for the newly surfaced device.
          recoveredDiskInfo: Only to be filled in if the `pyVmomi.sms.storage.replication.FailoverSuccessResult.RecoveredDevice.recoveredDeviceId` is `pyVmomi.sms.storage.replication.VirtualMachineId`.
          error: Virtual Volume specific recovery error.
              
              This should be rare.
          warnings: Warnings.
      """
      targetDeviceId: _typing.Optional[ReplicaId] = None
      recoveredDeviceId: _typing.Optional[DeviceId] = None
      sourceDeviceId: DeviceId
      info: list[str] = []
      datastore: pyVmomi.vim.Datastore
      recoveredDiskInfo: list[FailoverSuccessResult.RecoveredDiskInfo] = []
      error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
      warnings: list[pyVmomi.vmodl.MethodFault] = []

   newState: str
   pitId: _typing.Optional[PointInTimeReplicaId] = None
   pitIdBeforeFailover: _typing.Optional[PointInTimeReplicaId] = None
   recoveredDeviceInfo: list[FailoverSuccessResult.RecoveredDevice] = []
   timeStamp: _typing.Optional[_datetime.datetime] = None


class FaultDomainInfo(pyVmomi.vim.vm.replication.FaultDomainId):
   """
   Information about a Fault Domain.
   
   Attributes:
       name: Name of the fault domain, if not specified, the id will be used in place
           of the name.
           
           Name need not be unique.
       description: Description - could be a localized string.
       storageArrayId: Identifier of the Storage Array that this Fault Domain belongs to.
           
           A Fault
           Domain and all its children should report same `pyVmomi.sms.storage.replication.FaultDomainInfo.storageArrayId`. It
           can be left unspecified. If not specified, vSphere will not support High
           Availability feature for this Fault Domain. When specified, vSphere will
           treat the the currently active VASA provider for `pyVmomi.sms.storage.StorageArray` as
           the active VASA provider for this Fault Domain and its children.
           Changing High Availability support choice for a Fault Domain
           intermittently, by sometimes specifying the storageArrayId and sometimes
           not, will cause unexpected result and might cause VP to be in 'syncError'
           state in vSphere.
       children: List of children, the entries in the array should always be
           `pyVmomi.vim.vm.replication.FaultDomainId` and not `pyVmomi.sms.storage.replication.FaultDomainInfo`.
           
           The 2016 vSphere release will not support nested Fault Domains. The field
           FaultDomainInfo#children is ignored by vSphere 2016 release.
       provider: VASA provider that is actively managing this fault domain
   """
   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   storageArrayId: _typing.Optional[str] = None
   children: list[pyVmomi.vim.vm.replication.FaultDomainId] = []
   provider: _typing.Optional[pyVmomi.sms.provider.Provider] = None


class GroupErrorResult(GroupOperationResult):
   """
   Error result.
   
   Attributes:
       error: Error array, must contain at least one entry.
   """
   error: list[pyVmomi.vmodl.MethodFault] = []


class GroupInfo(pyVmomi.vmodl.DynamicData):
   """
   Replication group information.
   
   May be either a `pyVmomi.sms.storage.replication.SourceGroupInfo` or
   `pyVmomi.sms.storage.replication.TargetGroupInfo`.
   
   Attributes:
       groupId: Identifier of the group + fault domain id.
   """
   groupId: pyVmomi.vim.vm.replication.ReplicationGroupId


class PointInTimeReplicaId(pyVmomi.vmodl.DynamicData):
   """
   Identity of the Point in Time Replica object.
   
   Attributes:
       id: ID of the Point In Time replica.
   """
   id: str


class PromoteParam(pyVmomi.vmodl.DynamicData):
   """
   Input to the promoteReplicationGroup method.
   
   Attributes:
       isPlanned: Specifies whether the promote operation is a planned one.
           
           When this flag is set to false, the recovery VASA provider must not
           try to connect to the primary VASA provider during promote.
       replicationGroupsToPromote: The replication groups to promote.
           
           It is legal for the VASA
           provider to successfully promote only some groups. The
           groups that did not succeed will be retried.
           
           The identifiers of the Virtual Volumes do not change after the
           promote operation.
   """
   isPlanned: bool
   replicationGroupsToPromote: list[pyVmomi.vim.vm.replication.ReplicationGroupId] = []


class QueryPointInTimeReplicaParam(pyVmomi.vmodl.DynamicData):
   """
   Describes the search criteria for the PiT query.
   
   If none of the fields
   is set, or if the number of PiT replicas is too large, VASA provider can
   return `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaSummaryResult`.
   
   Attributes:
       replicaTimeQueryParam: Specifies the replica time span that vSphere is interested in.
       pitName: Only the replicas that match the given name are requested.
           
           A regexp according to http://www.w3.org/TR/xmlschema-2/#regexs.
       tags: Only the replicas with tags that match the given tag(s) are requested.
           
           Each entry may be a regexp according to http://www.w3.org/TR/xmlschema-2/#regexs.
       preferDetails: This field is hint for the preferred type of return results.
           
           It can be either true for `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaSuccessResult` or
           false for `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaSummaryResult`.
           If not set, VP may choose the appropriate type, as described in
           `ReplicaQueryIntervalParam`.
   """
   class ReplicaQueryIntervalParam(pyVmomi.vmodl.DynamicData):
      """
      Defines the parameters for a Point In Time replica (PiT) query.
      
      vSphere will not set all the three fields.
      
      In other words, the following combinations of fields are allowed:
      - All the three fields are omitted.
      - `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaParam.ReplicaQueryIntervalParam.fromDate` and `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaParam.ReplicaQueryIntervalParam.toDate` are set.
      - `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaParam.ReplicaQueryIntervalParam.fromDate` and `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaParam.ReplicaQueryIntervalParam.number` are set.
      - `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaParam.ReplicaQueryIntervalParam.toDate` and `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaParam.ReplicaQueryIntervalParam.number` are set.
        
      When all the fields are omitted, VASA provider should return
      `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaSummaryResult`.
      But, returned result can be either `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaSuccessResult`
      or `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaSummaryResult` based on value i.e true or false
      respectively for field `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaParam.preferDetails`.
      
      Attributes:
          fromDate: Return all PiTs including and later than `fromDate`.
          toDate: Return all PiTs earlier than `toDate`.
          number: Return information for only `number` entries.
      """
      fromDate: _typing.Optional[_datetime.datetime] = None
      toDate: _typing.Optional[_datetime.datetime] = None
      number: _typing.Optional[int] = None

   replicaTimeQueryParam: _typing.Optional[QueryPointInTimeReplicaParam.ReplicaQueryIntervalParam] = None
   pitName: _typing.Optional[str] = None
   tags: list[str] = []
   preferDetails: _typing.Optional[bool] = None


class QueryPointInTimeReplicaSuccessResult(GroupOperationResult):
   """
   Return type for successful
   `pyVmomi.sms.provider.VasaProvider.queryPointInTimeReplica`
   operation.
   
   If the VASA provider decides that there are too many to return,
   it could set the result of some of the groups to `pyVmomi.sms.fault.TooMany`
   fault or `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaSummaryResult`.
   
   vSphere will then query for these groups separately.
   
   Attributes:
       replicaInfo: Information about the available replicas.
   """
   class PointInTimeReplicaInfo(pyVmomi.vmodl.DynamicData):
      """
      Attributes:
          id: Id of the PIT replica.
              
              Note that this id is always used
              in combination with the `pyVmomi.vim.vm.replication.ReplicationGroupId`, hence must be
              unique to the `pyVmomi.vim.vm.replication.ReplicationGroupId`.
          pitName: Name of the PIT replica.
              
              This may be a localized string
              in a language as chosen by the VASA provider.
          timeStamp: Time when the snapshot was taken.
              
              Time stamps are maintained by
              the Replication provider, note that this carries time zone information
              as well.
          tags: VASA provider managed tags associated with the replica.
      """
      id: PointInTimeReplicaId
      pitName: str
      timeStamp: _datetime.datetime
      tags: list[str] = []

   replicaInfo: list[QueryPointInTimeReplicaSuccessResult.PointInTimeReplicaInfo] = []


class QueryPointInTimeReplicaSummaryResult(GroupOperationResult):
   """
   Summary of the available replicas.
   
   Mostly useful for CDP type replicators.
   
   Attributes:
       intervalResults: A series of query results.
           
           No special ordering is assumed by vSphere.
   """
   class ReplicaIntervalQueryResult(pyVmomi.vmodl.DynamicData):
      """
      Summarizes the collection of replicas in one time interval.
      
      Attributes:
          fromDate: Beginning of interval (inclusive).
          toDate: End of interval (exclusive).
          number: Number of Point in Time replicas available for recovery.
              
              TODO: Do we want to have also ask for number of 'special'
              PiTs e.g. those that are consistent?
      """
      fromDate: _datetime.datetime
      toDate: _datetime.datetime
      number: int

   intervalResults: list[QueryPointInTimeReplicaSummaryResult.ReplicaIntervalQueryResult] = []

class QueryReplicationGroupSuccessResult(GroupOperationResult):
   """
   Information about the replication groups.
   
   Information about both the source
   groups and the target groups is returned.
   
   Attributes:
       rgInfo: Information about the replication group.
           
           May be either
           `pyVmomi.sms.storage.replication.SourceGroupInfo` or `pyVmomi.sms.storage.replication.TargetGroupInfo`.
   """
   rgInfo: GroupInfo


class QueryReplicationPeerResult(pyVmomi.vmodl.DynamicData):
   """
   Information about the replication peers of a VASA provider.
   
   Attributes:
       sourceDomain: Source fault domain id, must correspond to an id from the input.
       targetDomain: Target fault domains for the given source, fault domain ID's are globally
           unique.
           
           There can be one or more target domains for a given source.
       error: Error must be set when targetDomain field is not set.
       warning: Optional warning messages.
   """
   sourceDomain: pyVmomi.vim.vm.replication.FaultDomainId
   targetDomain: list[pyVmomi.vim.vm.replication.FaultDomainId] = []
   error: list[pyVmomi.vmodl.MethodFault] = []
   warning: list[pyVmomi.vmodl.MethodFault] = []


class TargetGroupMemberInfo(pyVmomi.vmodl.DynamicData):
   """
   Information about member virtual volumes in a ReplicationGroup
   on the target when the state is `TARGET`.
   
   This need not include information about all the snapshots in
   the ReplicationGroup.
   
   Attributes:
       replicaId: Identifier of the replica device.
       sourceId: Source device, since the device id can be the same in all the domains,
           this needs to supplemented with the domain id to identify the device.
       targetDatastore: Datastore of the target device.
           
           This may be used by CAM/SRM
           to notify the administrators to setup access paths for the hosts
           to access the recovered devices.
   """
   replicaId: ReplicaId
   sourceId: DeviceId
   targetDatastore: pyVmomi.vim.Datastore


class RecoveredTargetGroupMemberInfo(TargetGroupMemberInfo):
   """
   Information about member virtual volumes in a ReplicationGroup
   on the target after failover or testFailoverStart.
   
   This must include information about all the vSphere managed snapshots in
   the ReplicationGroup.
   
   Attributes:
       recoveredDeviceId: Identifier of the target device after test or failover.
   """
   recoveredDeviceId: _typing.Optional[DeviceId] = None


class ReplicaId(pyVmomi.vmodl.DynamicData):
   """
   Identifier of the replication target device.
   
   For Virtual Volumes, this could be the same as a Virtual Volume
   Id, for VMDK's this could be an FCD uuid, or some other ID
   made up by the replicator. This identifier is opaque to vSphere and
   hence does not have any distinguishing type. This can be used
   to identify the replica without the accompanying source device id
   (though there are no such uses in the current API).
   
   Since this an opaque type, the recovered device id at
   `pyVmomi.sms.storage.replication.RecoveredTargetGroupMemberInfo.recoveredDeviceId`
   should be filled in even if the values are the same.
   """
   id: str

class ReplicationState:
   """
   State of the replication group at the site of the query.
   
   A replication group
   may be in different states at the source site and each of the target sites.
   Note that this state does not capture the health of the replication link. If
   necessary, that can be an additional attribute.
   """
   pass


class ReverseReplicationSuccessResult(GroupOperationResult):
   """
   Represents the result of a successful reverse replication action.
   
   The newly
   established replication relation might have a different source group ID and
   different set of target group IDs. This means that the replication topology
   will need to be discovered again by the DR orchestration programs (SRM/CAM).
   However, we assume that after the reverse replication, the new source fault
   domain id remains the same as the old (i.e. before failover) fault domain id.
   
   Attributes:
       newGroupId: The replication group ID of the newly created source group.
           
           FaultDomainId
           must remain the same.
   """
   newGroupId: pyVmomi.vim.vm.replication.DeviceGroupId


class SourceGroupInfo(GroupInfo):
   """
   Replication group details on the source.
   
   We do not assume the same
   Replication Group id on all the sites. This is returned as answer to
   queryReplicationGroup.
   
   Attributes:
       name: Name of the replication group, may be edited after creating the
           Replication Group, not unique.
           
           May be a localized string. Some vendors may
           choose to use name as the group id, to support this, vSphere will not
           allow the name to be modified - even if vSphere creates/manages the
           Replication Group.
       description: Description the Replication Group, may be edited after creating the
           Replication Group.
           
           May be a localized string.
       state: State of the replication group on the source.
       replica: Information about the target Replication Groups.
       memberInfo: Information about the member virtual volumes and their replicas.
   """
   class ReplicationTargetInfo(pyVmomi.vmodl.DynamicData):
      """
      Information about each replication target.
      
      Attributes:
          targetGroupId: Id of the target replication group (including the fault domain ID).
          replicationAgreementDescription: Description of the replication agreement.
              
              This could be used to describe the characteristics of the replication
              relationship between the source and the target (e.g. RPO, Replication
              Mode, and other such properties). It is expected that VASA provider
              will localize the string before sending to vSphere.
      """
      targetGroupId: pyVmomi.vim.vm.replication.ReplicationGroupId
      replicationAgreementDescription: _typing.Optional[str] = None

   name: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   state: str
   replica: list[SourceGroupInfo.ReplicationTargetInfo] = []
   memberInfo: list[SourceGroupMemberInfo] = []


class SourceGroupMemberInfo(pyVmomi.vmodl.DynamicData):
   """
   Represents a member virtual volume of a replication group on the source end
   of the replication arrow.
   
   Attributes:
       deviceId: Identifier of the source device.
           
           May be a Virtual Volume, a Virtual Disk or a Virtual Machine
       targetId: Target devices, key'ed by the fault domain id.
           
           TODO: It is not clear if we
           really need this information, since the target side query can return the
           target -> source relation information.
   """
   class TargetDeviceId(pyVmomi.vmodl.DynamicData):
      """
      Represents a replication target device, since the replication group id can
      be the same in all the domains, this is keyed by the fault domain id.
      
      Attributes:
          domainId: ID of the fault domain.
          deviceId: ID of the target device.
      """
      domainId: pyVmomi.vim.vm.replication.FaultDomainId
      deviceId: ReplicaId

   deviceId: DeviceId
   targetId: list[SourceGroupMemberInfo.TargetDeviceId] = []


class SyncReplicationGroupSuccessResult(GroupOperationResult):
   """
   Result object for a replication group that was successfully synchronized.
   
   Attributes:
       timeStamp: Creation time of the PIT
       pitId: PIT id.
           
           If the VASA provider does not support PIT, this can be
           left unset.
           
           A PIT created as a result of the `syncReplicationGroup`
           may or may not have the same retention policy as other PITs. A VASA provider
           can choose to delete such a PIT after a successful `testFailoverStop`
   """
   timeStamp: _datetime.datetime
   pitId: _typing.Optional[PointInTimeReplicaId] = None
   pitName: _typing.Optional[str] = None


class TargetGroupInfo(GroupInfo):
   """
   Information about the replication target group.
   
   This is returned as answer
   to queryReplicationGroup before failover or testFailoverStart.
   
   This does not have to include the
   snapshot objects in the ReplicationGroup, however, see also
   `pyVmomi.sms.storage.replication.RecoveredTargetGroupMemberInfo`.
   
   Attributes:
       sourceInfo: Replication source information.
       state: Replication state of the group on the replication target.
       devices: Member device information.
           
           When the ReplicationGroup is either in `FAILEDOVER`
           or `INTEST`, this
           should be `pyVmomi.sms.storage.replication.RecoveredTargetGroupMemberInfo`.
           Otherwise, this should be `pyVmomi.sms.storage.replication.TargetGroupMemberInfo`
       isPromoteCapable: Whether the VASA provider is capable of executing
           `pyVmomi.sms.provider.VasaProvider.promoteReplicationGroup` for this
           ReplicationGroup.
           
           False if not set. Note that this setting is per
           ReplicationGroup per Target domain.
       name: Name of Replication Group.
   """
   class TargetToSourceInfo(pyVmomi.vmodl.DynamicData):
      """
      Information about each replication target.
      
      Attributes:
          sourceGroupId: Id of the source CG id (including the fault domain ID).
          replicationAgreementDescription: Description of the replication agreement.
              
              This could be used to describe the characteristics of the replication
              relationship between the source and the target (e.g. RPO, Replication
              Mode, and other such properties). It is expected that VASA provider
              will localize the string before sending to vSphere.
      """
      sourceGroupId: pyVmomi.vim.vm.replication.ReplicationGroupId
      replicationAgreementDescription: _typing.Optional[str] = None

   sourceInfo: TargetGroupInfo.TargetToSourceInfo
   state: str
   devices: list[TargetGroupMemberInfo] = []
   isPromoteCapable: _typing.Optional[bool] = None
   name: _typing.Optional[str] = None

class TestFailoverParam(FailoverParam):
   """Input to testFailover method."""
   pass

class VVolId(DeviceId):
   """
   Identity of a virtual volume for policy API purposes.
   
   For the sake of
   brevity, let us use VVolId. This works because the class is defined as a part
   of the policy package.
   
   WSDL names do not have this feature, but WSDL names are usually prefixed with
   the package name any way.
   """
   id: str

class VirtualDiskId(DeviceId):
   """
   Represents a virtual disk with a UUID (aka FCD).
   
   Virtual Volume VASA providers can ignore this class.
   
   Attributes:
       diskId: See VIM documentation for more details on first class storage - which is
           new in 2016.
   """
   diskId: str

class VirtualDiskKey(DeviceId):
   """
   Represents a virtual disk.
   
   Ideally a UUID, since we do not yet have an FCD,
   let us use VM's UUID + diskKey.
   Virtual Volume VASA providers can ignore this class.
   
   Attributes:
       vmInstanceUUID: The vmInstanceUUID is unique to a VM.
           
           See
           http://pubs.vmware.com/vsphere-60/index.jsp?topic=%2Fcom.vmware.wssdk.apiref.doc%2Fvim.vm.ConfigInfo.html
   """
   vmInstanceUUID: str
   deviceKey: int


class VirtualDiskMoId(DeviceId):
   """
   Identifies a VirtualDisk uniquely using the disk key, vCenter managed object id of the VM it
   belongs to and the corresponding vCenter UUID.
   
   Attributes:
       vcUuid: The vCenter UUID - this is informational only, and may not always be set.
       vmMoid: The managed object id that corresponds to vCenter's ManagedObjectReference#key for this VM.
       diskKey: The disk key that corresponds to the VirtualDevice#key in vCenter.
   """
   vcUuid: _typing.Optional[str] = None
   vmMoid: str
   diskKey: str

class VirtualMachineId(DeviceId):
   """Abstracts the identity of a virtual machine."""
   pass


class VirtualMachineFilePath(VirtualMachineId):
   """
   Identifies a virtual machine by its VMX file path.
   
   Attributes:
       vcUuid: The vCenter UUID - this is informational only,
           and may not always be set.
       dsUrl: Datastore URL, which is globally unique (name is not).
       vmxPath: Full path name from the URL onwards.
           
           When the vmxPath is returned after failover, the VMX file
           should be fixed up to contain correct target filenames for all replicated
           disks. For non-replicated disks, the target filenames can contain
           any arbitrary path. For better security, it is recommended to
           set these disks pointed to a random string (e.g. UUID).
   """
   vcUuid: _typing.Optional[str] = None
   dsUrl: str
   vmxPath: str


class VirtualMachineMoId(VirtualMachineId):
   """
   Identifies a VirtualMachine uniquely using its vCenter managed object id and the corresponding
   vCenter UUID
   
   Attributes:
       vcUuid: The vCenter UUID - this is informational only, and may not always be set.
       vmMoid: The managed object id that corresponds to vCenter's ManagedObjectReference#key for this VM.
   """
   vcUuid: _typing.Optional[str] = None
   vmMoid: str

class VirtualMachineUUID(VirtualMachineId):
   """
   Identifies a virtual machine by its vmInstanceUUID
   
   Attributes:
       vmInstanceUUID: The vmInstanceUUID is unique to a VM.
           
           See
           http://pubs.vmware.com/vsphere-60/index.jsp?topic=%2Fcom.vmware.wssdk.apiref.doc%2Fvim.vm.ConfigInfo.html
   """
   vmInstanceUUID: str
