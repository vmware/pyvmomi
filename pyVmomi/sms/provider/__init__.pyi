# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.sms.storage
import pyVmomi.sms.storage.replication
import pyVmomi.vim.vm.replication



class AlarmFilter(pyVmomi.vmodl.DynamicData):
   """
   This spec contains information needed for queryActiveAlarm API to filter the result.
   
   Attributes:
       alarmStatus: The status of the alarm to search for.
           
           Should be one of
           `pyVmomi.sms.storage.AlarmStatus`. If not specified, all status values
           should be considered.
       alarmType: The status of the alarm to search for.
           
           Should be one of
           `pyVmomi.sms.storage.AlarmType`. If not specified, all alarm types
           should be considered.
       entityType: The entityType of interest, VASA provider should
           return all active alarms of this type when `pyVmomi.sms.provider.AlarmFilter.entityId`
           is not set.
           
           See `pyVmomi.sms.storage.EntityType`.
       entityId: The identifiers of the entities of interest.
           
           If set, all entities must be
           of the same `pyVmomi.sms.storage.EntityType` and it should be set in
           `pyVmomi.sms.provider.AlarmFilter.entityType`. VASA provider can skip listing the missing entities.
       pageMarker: The page marker used for query pagination.
           
           This is an opaque string that
           will be set based on the value returned by the VASA provider - see
           `pyVmomi.sms.provider.AlarmResult.pageMarker`. For initial request this should be set to
           null, indicating request for the first page.
   """
   alarmStatus: _typing.Optional[str] = None
   alarmType: _typing.Optional[str] = None
   entityType: _typing.Optional[str] = None
   entityId: list[object] = []
   pageMarker: _typing.Optional[str] = None


class AlarmResult(pyVmomi.vmodl.DynamicData):
   """
   Contains result for queryActiveAlarm API.
   
   Attributes:
       storageAlarm: Resulting storage alarms.
       pageMarker: The page marker used for query pagination.
           
           This is an opaque string that
           will be set by the VASA provider. The client will set the same value in
           `pyVmomi.sms.provider.AlarmFilter.pageMarker` to query the next page. VP should unset
           this value to indicate the end of page.
   """
   storageAlarm: list[pyVmomi.sms.storage.StorageAlarm] = []
   pageMarker: _typing.Optional[str] = None


class Provider(pyVmomi.VmomiSupport.ManagedObject):
   """Provider interface for Storage Monitoring Service (SMS)."""
   def QueryProviderInfo(self) -> ProviderInfo:
      """Get provider information."""
      ...


class ProviderInfo(pyVmomi.vmodl.DynamicData):
   """
   Information about Storage Monitoring Service (SMS)
   providers.
   
   Attributes:
       uid: Unique identifier
       name: Name
       description: Description of the provider
       version: Version of the provider
   """
   uid: str
   name: str
   description: _typing.Optional[str] = None
   version: _typing.Optional[str] = None


class ProviderSpec(pyVmomi.vmodl.DynamicData):
   """
   Specification for Storage Monitoring Service (SMS)
   providers.
   
   Attributes:
       name: Name
           The maximum length of the name is 275 characters.
       description: Description of the provider
   """
   name: str
   description: _typing.Optional[str] = None


class VASAProviderUpgradeSpec(pyVmomi.vmodl.DynamicData):
   """
   VASA Provider Specification for upgrade.
   
   Attributes:
       providerUid: `pyVmomi.sms.provider.ProviderInfo.uid` for the provider
       username: VASA Provider username
       password: VASA Provider password
   """
   providerUid: str
   username: str
   password: str


class VasaProvider(Provider):
   """
   VASA(vStorage APIs for Storage Awareness) provider
   definition.
   """
   def Sync(self, arrayId: _typing.Optional[str]) -> pyVmomi.vim.Task:
      """
      Issue a sync for the given Storage Array.
      
      Raises:
          pyVmomi.sms.fault.ProviderSyncFailed: if an error is encountered while
              executing sync operation for the
              provider.
      """
      ...
   def RefreshCertificate(self) -> pyVmomi.vim.Task:
      """
      Refresh a CA signed certificate for the provider.
      
      This API will be used when provider
      certificate is about to expire, but still within soft or hard limit window. If the
      provider is in \"disconnected\" state, this operation will be a no-op.
      Note: This API works only for non-IOFilter and non-VSAN providers that support VASA 2.0 and onwards.
      
      Raises:
          pyVmomi.sms.fault.CertificateRefreshFailed: if an error is encountered while refreshing
              CA signed certificate for the provider.
      """
      ...
   def RevokeCertificate(self) -> pyVmomi.vim.Task:
      """
      Revoke CA signed certificate of the provider.
      
      This API will unregister the
      provider automatically.
      Note: This API works only for non-IOFilter and non-VSAN providers that support VASA 2.0 and onwards.
      
      Raises:
          pyVmomi.sms.fault.CertificateRevocationFailed: if an error is encountered while revoking CA signed
              certificate of the provider.
      """
      ...
   def Reconnect(self) -> pyVmomi.vim.Task:
      """
      Reconnect to the provider.
      
      This API will be used to reconnect to a provider that
      is in \"disconnected\" state. If reconnecting fails due to InvalidCertificate exception,
      that means the current provider certificate is expired or corrupted. Then user has to
      recover the provider following these steps:
      1\\. Unregister the provider using `pyVmomi.sms.StorageManager.unregisterProvider`
      2\\. Provision a new self signed certificate for the provider
      3\\. Register the provider using `pyVmomi.sms.StorageManager.registerProvider`
      If the provider is not in \"disconnected\" state, this operation will be a no-op.
      Note: This API works only for providers that support VASA 2.0 and onwards.
      
      Raises:
          pyVmomi.sms.fault.InvalidCertificate: if the provider certificate is invalid
          pyVmomi.sms.fault.ProviderConnectionFailed: if an error is encountered while reconnecting to
              the provider.
      """
      ...
   def QueryReplicationPeer(self, faultDomainId: list[pyVmomi.vim.vm.replication.FaultDomainId]) -> list[pyVmomi.sms.storage.replication.QueryReplicationPeerResult]:
      """
      Query for the replication peer fault domains.
      
      Args:
          faultDomainId: An optional list of source fault domain ID.
      
      Returns:
          An array of `pyVmomi.sms.storage.replication.QueryReplicationPeerResult`.
          
          If the input array is null or empty, VASA provider needs to return
          result for all available source FaultDomain(s). If the input array is
          not empty, VASA Provider needs to return one entry in result for each
          entry in the input. The length of the input and result arrays must be
          same in that case.
          
          The fault in the result entry can be set to:
          - `pyVmomi.vim.fault.NotFound` if the fault domain identifier is not present.
          - `pyVmomi.sms.fault.DuplicateEntry` if the fault domain identifier is duplicate.
          - `pyVmomi.sms.fault.TooMany` if the number of entries is too large to be returned in one call.
          - `pyVmomi.sms.fault.QueryExecutionFault` for any other error.
      
      Raises:
          pyVmomi.sms.fault.ProviderUnavailable: if the provider is temporarily unavailable.
          pyVmomi.sms.fault.InactiveProvider: if the provider is inactive for the specified
              fault domains.
          pyVmomi.sms.fault.ProviderBusy: if the provider is busy and cannot process the request.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while processing
              the query request.
      """
      ...
   def QueryReplicationGroup(self, groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId]) -> list[pyVmomi.sms.storage.replication.GroupOperationResult]:
      """
      Query for the replication group details.
      
      Args:
          groupId: List of replication group IDs.
      
      Returns:
          An array of `pyVmomi.sms.storage.replication.GroupOperationResult` elements.
          
          If the input array is null or empty, VASA Provider needs to return all
          available replication groups. Depending on the number of replication
          groups to be returned, VASA Provider can return either a list of
          `pyVmomi.sms.storage.replication.GroupOperationResult` or a list of
          `pyVmomi.sms.storage.replication.QueryReplicationGroupSuccessResult`. However, VASA
          Provider should not return a hybrid result.
          
          If the input array is not empty, VASA Provider needs to return an array
          of results, one for each entry in the input. Each entry in the returned
          array is either a `pyVmomi.sms.storage.replication.QueryReplicationGroupSuccessResult`
          (for success), or a `pyVmomi.sms.storage.replication.GroupErrorResult` (for failure).
          The length of the result arrays must be the same as the input.
          
          The fault in the result entry can be set to:
          - `pyVmomi.vim.fault.NotFound` if the replication group identifier is not present.
          - `pyVmomi.sms.fault.DuplicateEntry` if the replication group identifier is duplicate.
          - `pyVmomi.sms.fault.TooMany` if the number of entries is too large to be returned in one call.
          - `pyVmomi.sms.fault.QueryExecutionFault` for any other error.
      
      Raises:
          pyVmomi.sms.fault.ProviderUnavailable: if the provider is temporarily unavailable.
          pyVmomi.sms.fault.InactiveProvider: if the provider is inactive for the specified
              replication groups.
          pyVmomi.sms.fault.ProviderBusy: if the provider is busy and cannot process the request.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while processing
              the query request.
      """
      ...
   def QueryPointInTimeReplica(self, groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId], queryParam: _typing.Optional[pyVmomi.sms.storage.replication.QueryPointInTimeReplicaParam]) -> list[pyVmomi.sms.storage.replication.GroupOperationResult]:
      """
      Query for the point-in-time replicas available at the target location.
      
      Args:
          groupId: List of replication group IDs.
          queryParam: Search criteria specification for all the groups.
      
      Returns:
          An array of GroupOperationResult elements.
          
          Each of these elements is either `pyVmomi.sms.storage.replication.GroupErrorResult` or
          `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaSuccessResult` or
          `pyVmomi.sms.storage.replication.QueryPointInTimeReplicaSummaryResult` for CDP capable replicators.
          
          The fault in the result entry can be set to:
          - `pyVmomi.vim.fault.NotFound` if the replication group identifier is not present.
          - `pyVmomi.sms.fault.DuplicateEntry` if the replication group identifier is duplicate.
          - `pyVmomi.sms.fault.TooMany` if the number of entries is too large to be returned in one call.
          - `pyVmomi.sms.fault.QueryExecutionFault` for any other error.
      
      Raises:
          pyVmomi.sms.fault.ProviderUnavailable: if the provider is temporarily unavailable.
          pyVmomi.sms.fault.InactiveProvider: if the provider is inactive for the specified
              replication groups.
          pyVmomi.sms.fault.ProviderBusy: if the provider is busy and cannot process the request.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while processing
              the query request.
      """
      ...
   def TestFailoverReplicationGroupStart(self, testFailoverParam: pyVmomi.sms.storage.replication.TestFailoverParam) -> pyVmomi.vim.Task:
      """
      Start a test failover for the specified replication groups.
      
      This
      function will always be called at the replication target location.
      
      Args:
          testFailoverParam: Settings for the failover.
      
      Returns:
          An array of GroupOperationResult elements.
          
          Each of the elements is either a `pyVmomi.sms.storage.replication.GroupErrorResult` or `pyVmomi.sms.storage.replication.FailoverSuccessResult`
          
          The fault in the result entry can be set to:
          - `pyVmomi.vim.fault.NotFound` if the replication group id is not present.
          - `pyVmomi.sms.fault.DuplicateEntry` if the replication group id in the failover parameter is duplicate.
          - `pyVmomi.sms.fault.ProviderOutOfResource` if it is not possible to perform the operation due to lack of resources.
          - `pyVmomi.sms.fault.replication.InvalidFunctionTarget` if the call is made on the VP owning source end of the replication.
          - `pyVmomi.sms.fault.replication.InvalidReplicationState` if the group is in an incompatible state.
          - `pyVmomi.sms.fault.replication.PeerNotReachable` if the replication peer is not reachable.
          - `pyVmomi.sms.fault.replication.ReplicationFault` for any other error.
      
      Raises:
          pyVmomi.sms.fault.ProviderUnavailable: if the provider is temporarily unavailable.
          pyVmomi.sms.fault.ProviderOutOfResource: if it is not possible to perform the operation
              due to lack of resources.
          pyVmomi.sms.fault.InactiveProvider: if the provider is inactive for the specified entity.
          pyVmomi.sms.fault.TooMany: Thrown if the Provider is unable to handle the given set of
              replication groups in one call. The client needs to call this method based
              on the maxBatchSize specified in the TooMany fault. If the maxBatchSize is
              not specified, the client is expected to call the function for each group
              individually (i.e. maxBatchSize = 1).
          pyVmomi.sms.fault.ProviderBusy: if the provider is busy and cannot process the request.
          pyVmomi.sms.fault.replication.ReplicationFault: if an error is encountered while processing the request.
      """
      ...
   def TestFailoverReplicationGroupStop(self, groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId], force: bool) -> pyVmomi.vim.Task:
      """
      Stop the ongoing test failover.
      
      This function will always be called at
      the replication target location.
      
      Args:
          groupId: Array of replication groups that need to stop test.
          force: \\- if true, VP should force-unbind all Virtual Volumes
              and move the RG from INTEST to TARGET state. If false, VP will report all the
              Virtual Volumes which need to be cleaned up before a failover operation
              can be triggered. The default value will be false.
      
      Returns:
          An array of GroupOperationResult elements.
          
          Each of the elements is either `pyVmomi.sms.storage.replication.GroupErrorResult` for error or
          `pyVmomi.sms.storage.replication.GroupOperationResult` for success.
          
          The fault in the result entry can be set to:
          `pyVmomi.vim.fault.NotFound` if the replication group id is not present.
          `pyVmomi.sms.fault.DuplicateEntry` if the replication group id is duplicate.
          `ResourceInUse` if the related resources cannot be cleaned up because they are still being used.
          `pyVmomi.sms.fault.ProviderOutOfResource` if it is not possible to perform the operation due to lack of resources.
          `pyVmomi.sms.fault.replication.InvalidFunctionTarget` if the call is made on the VP owning source end of the replication.
          `pyVmomi.sms.fault.replication.PeerNotReachable` if the replication peer is not reachable.
          `pyVmomi.sms.fault.replication.InvalidReplicationState` if the group is in an incompatible state.
          `pyVmomi.sms.fault.replication.ReplicationFault` for any other error.
      
      Raises:
          pyVmomi.sms.fault.ProviderUnavailable: if the provider is temporarily unavailable.
          pyVmomi.sms.fault.ProviderOutOfResource: if it is not possible to perform the operation
              due to lack of resources.
          pyVmomi.sms.fault.InactiveProvider: if the provider is inactive for the specified
              replication groups.
          pyVmomi.sms.fault.TooMany: Thrown if the Provider is unable to handle the given set of
              replication groups in one call. The client needs to call this method based
              on the maxBatchSize specified in the TooMany fault. If the maxBatchSize is
              not specified, the client is expected to call the function for each group
              individually (i.e. maxBatchSize = 1).
          pyVmomi.sms.fault.ProviderBusy: if the provider is busy and cannot process the request.
          pyVmomi.sms.fault.replication.ReplicationFault: if an error is encountered while processing the request.
          pyVmomi.sms.fault.NotSupportedByProvider: if the provider does not support force operation.
      """
      ...
   def PromoteReplicationGroup(self, promoteParam: pyVmomi.sms.storage.replication.PromoteParam) -> pyVmomi.vim.Task:
      """
      Promotes the replication groups currently `INTEST`
      to `FAILEDOVER`.
      
      This
      function must be called at the replication target location.
      
      Args:
          promoteParam: Specifies an array of replication group IDs whose
              in-test devices (`INTEST`) need to be
              promoted to failover `FAILEDOVER` state.
      
      Returns:
          An array of GroupOperationResult elements.
          
          Each of the elements is either `pyVmomi.sms.storage.replication.GroupErrorResult` for error or
          `pyVmomi.sms.storage.replication.GroupOperationResult` for success.
          
          The fault in the result entry can be set to:
          `pyVmomi.vim.fault.NotFound` if the replication group id is not present.
          `pyVmomi.sms.fault.DuplicateEntry` if the replication group id in the promote parameter is duplicate.
          `pyVmomi.sms.fault.NotSupportedByProvider` if the replication group does not support promote operation.
          `pyVmomi.sms.fault.ProviderOutOfResource` if it is not possible to perform the operation due to lack of resources.
          `pyVmomi.sms.fault.replication.InvalidFunctionTarget` if the call is made on the VP owning source end of the replication.
          `pyVmomi.sms.fault.replication.PeerNotReachable` if the replication peer is not reachable.
          `pyVmomi.sms.fault.replication.InvalidReplicationState` if the group is in an incompatible state.
          `pyVmomi.sms.fault.replication.ReplicationFault` for any other error.
      
      Raises:
          pyVmomi.sms.fault.ProviderUnavailable: if the provider is temporarily unavailable.
          pyVmomi.sms.fault.ProviderOutOfResource: if it is not possible to perform the operation
              due to lack of resources.
          pyVmomi.sms.fault.InactiveProvider: if the provider is inactive for the specified entity.
          pyVmomi.sms.fault.TooMany: Thrown if the Provider is unable to handle the given set of
              replication groups in one call. The client needs to call this method based
              on the maxBatchSize specified in the TooMany fault. If the maxBatchSize is
              not specified, the client is expected to call the function for each group
              individually (i.e. maxBatchSize = 1).
          pyVmomi.sms.fault.ProviderBusy: if the provider is busy and cannot process the request.
          pyVmomi.sms.fault.replication.ReplicationFault: if an error is encountered while processing the request.
      """
      ...
   def SyncReplicationGroup(self, groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId], pitName: str) -> pyVmomi.vim.Task:
      """
      Synchronize the data between source and replica for the specified
      replication group.
      
      This function will always be called at the replication
      target location.
      
      Args:
          groupId: List of replication group IDs.
          pitName: Localized name for the point-in-time snapshot created.
      
      Returns:
          An array of GroupOperationResult elements.
          Each of the elements is either a `pyVmomi.sms.storage.replication.GroupErrorResult` or
          `pyVmomi.sms.storage.replication.SyncReplicationGroupSuccessResult`.
          
          If a Sync is ongoing for a given replication group, the corresponding fault must be
          `pyVmomi.sms.fault.replication.SyncOngoing` (which includes the sync task that can be tracked). Different
          replication groups can have different sync tasks associated with them and each needs
          to be tracked independently. If SMS fails to create task for the ongoing sync in VASA
          provider, `pyVmomi.sms.storage.replication.GroupErrorResult` will contain `pyVmomi.sms.fault.replication.ReplicationFault`, instead of
          `pyVmomi.sms.fault.replication.SyncOngoing`. In that case ongoing sync will not be trackable and a fresh
          sync operation can be retried after some time.
          
          The fault in the result entry can be set to:
          `pyVmomi.vim.fault.NotFound` if the replication group id is not present.
          `pyVmomi.sms.fault.DuplicateEntry` if the replication group identifier is duplicate.
          `pyVmomi.sms.fault.ProviderOutOfResource` if it is not possible to perform the operation due to lack of resources.
          `pyVmomi.sms.fault.replication.SyncOngoing` if synchronization ongoing, in this case payload must include the ongoing taskId.
          `pyVmomi.sms.fault.replication.InvalidFunctionTarget` if the call is made on the VP owning source end of the replication.
          `pyVmomi.sms.fault.replication.PeerNotReachable` if the replication peer is not reachable.
          `pyVmomi.sms.fault.replication.ReplicationFault` for any other error.
      
      Raises:
          pyVmomi.sms.fault.ProviderUnavailable: if the provider is temporarily unavailable.
          pyVmomi.sms.fault.ProviderOutOfResource: if it is not possible to perform the operation
              due to lack of resources.
          pyVmomi.sms.fault.InactiveProvider: if the provider is inactive for the specified entity.
          pyVmomi.sms.fault.ProviderBusy: if the provider is busy and cannot process the request.
          pyVmomi.sms.fault.replication.ReplicationFault: if an error is encountered while processing the request.
          pyVmomi.sms.fault.TooMany: Thrown if the Provider is unable to handle the given set of
              replication groups in one call. The client needs to call this method based
              on the maxBatchSize specified in the TooMany fault. If the maxBatchSize is
              not specified, the client is expected to call the function for each group
              individually (i.e. maxBatchSize = 1).
      """
      ...
   def PrepareFailoverReplicationGroup(self, groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId]) -> pyVmomi.vim.Task:
      """
      Prepare to fail over the specified replication groups.
      
      This function is always
      called at the replication source location.
      
      Args:
          groupId: List of replication group IDs.
      
      Returns:
          An array of GroupOperationResult elements.
          
          Each of the elements is either `pyVmomi.sms.storage.replication.GroupErrorResult` for error or
          `pyVmomi.sms.storage.replication.GroupOperationResult` for success.
          
          The fault in the result entry can be set to:
          `pyVmomi.vim.fault.NotFound` if the replication group id is not present.
          `pyVmomi.sms.fault.DuplicateEntry` if the replication group id is duplicate.
          `pyVmomi.sms.fault.ProviderOutOfResource` if it is not possible to perform the operation due to lack of resources.
          `pyVmomi.sms.fault.replication.InvalidFunctionTarget` if the call is made on the VP owning source end of the replication.
          `pyVmomi.sms.fault.replication.PeerNotReachable` if the replication peer is not reachable.
          `pyVmomi.sms.fault.replication.InvalidReplicationState` if the group is in an incompatible state.
          `pyVmomi.sms.fault.replication.ReplicationFault` for any other error.
      
      Raises:
          pyVmomi.sms.fault.ProviderUnavailable: if the provider is temporarily unavailable.
          pyVmomi.sms.fault.ProviderOutOfResource: if it is not possible to perform the operation
              due to lack of resources.
          pyVmomi.sms.fault.InactiveProvider: if the provider is inactive for the specified entity.
          pyVmomi.sms.fault.TooMany: Thrown if the Provider is unable to handle the given set of
              replication groups in one call. The client needs to call this method based
              on the maxBatchSize specified in the TooMany fault. If the maxBatchSize is
              not specified, the client is expected to call the function for each group
              individually (i.e. maxBatchSize = 1).
          pyVmomi.sms.fault.ProviderBusy: if the provider is busy and cannot process the request.
          pyVmomi.sms.fault.replication.ReplicationFault: if an error is encountered while processing the request.
      """
      ...
   def FailoverReplicationGroup(self, failoverParam: pyVmomi.sms.storage.replication.FailoverParam) -> pyVmomi.vim.Task:
      """
      Failover the specified device groups.
      
      This function will always be called
      at the replication target location.
      
      Args:
          failoverParam: Settings for the failover.
      
      Returns:
          An array of GroupOperationResult elements.
          
          Each of the elements is either a `pyVmomi.sms.storage.replication.GroupErrorResult` for error or
          `pyVmomi.sms.storage.replication.FailoverSuccessResult` for success.
          
          The fault in the result entry can be set to:
          `pyVmomi.vim.fault.NotFound` if the replication group id is not present.
          `pyVmomi.sms.fault.DuplicateEntry` if the replication group id in the failover parameter is duplicate.
          `pyVmomi.sms.fault.ProviderOutOfResource` if it is not possible to perform the operation due to lack of resources.
          `pyVmomi.sms.fault.replication.InvalidFunctionTarget` if the call is made on the VP owning source end of the replication.
          `pyVmomi.sms.fault.replication.PeerNotReachable` if the replication peer is not reachable.
          `pyVmomi.sms.fault.replication.InvalidReplicationState` if the group is in an incompatible state.
          `pyVmomi.sms.fault.replication.ReplicationFault` for any other error.
      
      Raises:
          pyVmomi.sms.fault.ProviderUnavailable: if the provider is temporarily unavailable.
          pyVmomi.sms.fault.ProviderOutOfResource: if it is not possible to perform the operation
              due to lack of resources.
          pyVmomi.sms.fault.InactiveProvider: if the provider is inactive for the specified entity.
          pyVmomi.sms.fault.TooMany: Thrown if the Provider is unable to handle the given set of
              replication groups in one call. The client needs to call this method based
              on the maxBatchSize specified in the TooMany fault. If the maxBatchSize is
              not specified, the client is expected to call the function for each group
              individually (i.e. maxBatchSize = 1).
          pyVmomi.sms.fault.ProviderBusy: if the provider is busy and cannot process the request.
          pyVmomi.sms.fault.replication.ReplicationFault: if an error is encountered while processing the request.
      """
      ...
   def ReverseReplicateGroup(self, groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId]) -> pyVmomi.vim.Task:
      """
      Initiate replication in the reverse way, making the currently
      `FAILEDOVER` devices as sources.
      
      Args:
          groupId: Array of replication groups (currently in
              `FAILEDOVER` state) that need to be reversed.
      
      Returns:
          An array of GroupOperationResult elements.
          
          Each of the elements is either `pyVmomi.sms.storage.replication.GroupErrorResult` for error or
          `pyVmomi.sms.storage.replication.ReverseReplicationSuccessResult` for success.
          
          The fault in the result entry can be set to:
          `pyVmomi.vim.fault.NotFound` if the replication group id is not present.
          `pyVmomi.sms.fault.DuplicateEntry` if the replication group id is duplicate.
          `pyVmomi.sms.fault.ProviderOutOfResource` if it is not possible to perform the operation due to lack of resources.
          `pyVmomi.sms.fault.replication.InvalidFunctionTarget` if the call is made on the VP owning source end of the replication.
          `pyVmomi.sms.fault.replication.PeerNotReachable` if the replication peer is not reachable.
          `pyVmomi.sms.fault.replication.NoReplicationTarget` If the replication target is not yet available.
          `pyVmomi.sms.fault.replication.InvalidReplicationState` if the group is in an incompatible state.
          `pyVmomi.sms.fault.replication.ReplicationFault` for any other error.
      
      Raises:
          pyVmomi.sms.fault.ProviderUnavailable: if the provider is temporarily unavailable.
          pyVmomi.sms.fault.ProviderOutOfResource: if it is not possible to perform the operation
              due to lack of resources.
          pyVmomi.sms.fault.InactiveProvider: if the provider is inactive for the specified entity.
          pyVmomi.sms.fault.TooMany: Thrown if the Provider is unable to handle the given set of
              replication groups in one call. The client needs to call this method based
              on the maxBatchSize specified in the TooMany fault. If the maxBatchSize is
              not specified, the client is expected to call the function for each group
              individually (i.e. maxBatchSize = 1).
          pyVmomi.sms.fault.ProviderBusy: if the provider is busy and cannot process the request.
          pyVmomi.sms.fault.replication.ReplicationFault: if an error is encountered while processing the request.
      """
      ...
   def QueryActiveAlarm(self, alarmFilter: _typing.Optional[AlarmFilter]) -> _typing.Optional[AlarmResult]:
      """
      Query for the currently active alarms known to this VASA provider.
      
      Provider is expected to return Red and Yellow types of alarms only.
      No Green alarms should be included in the result for this API.
      
      Args:
          alarmFilter: Filter criteria for the alarm state.
      
      Returns:
          `pyVmomi.sms.provider.AlarmResult` containing all (or requested) active alarm objects owned
          by the VASA provider.
      
      Raises:
          pyVmomi.vim.fault.NotFound: if the specified entity does not exist.
          pyVmomi.sms.fault.ProviderBusy: if the provider is busy and cannot process the request.
          pyVmomi.sms.fault.InactiveProvider: if the provider is inactive for the specified entity.
          pyVmomi.sms.fault.ProviderUnavailable: if the provider is temporarily unavailable.
          pyVmomi.sms.fault.QueryExecutionFault: if an error is encountered while processing the
              query request.
      """
      ...


class VasaProviderInfo(ProviderInfo):
   """
   Information about VASA (vStorage APIs for Storage Awareness) providers.
   
   Attributes:
       url: Provider URL
       certificate: Provider certificate
       status: The operational state of VASA Provider.
       statusFault: A fault that describes the cause of the current operational status.
       vasaVersion: Supported VASA(vStorage APIs for Storage Awareness) version
       namespace: Namespace to categorize storage capabilities provided by
           arrays managed by the provider
       lastSyncTime: Time stamp to indicate when last sync operation was completed
           successfully.
       supportedVendorModelMapping: List containing mapping between the supported vendorID and
           corresponding modelID
       supportedProfile: List of supported profiles
       supportedProviderProfile: List of supported profiles at provider level.
           
           Must be one of the string
           values from `pyVmomi.sms.provider.VasaProviderInfo.ProviderProfile`.
       relatedStorageArray: List containing mapping between storage arrays reported by the provider
           and information such as whether the provider is considered active for them.
       providerId: Provider identifier reported by the provider which is unique within
           the provider namespace.
       certificateExpiryDate: Provider certificate expiry date.
       certificateStatus: Provider certificate status
           This field holds values from `pyVmomi.sms.provider.VasaProviderInfo.CertificateStatus`
       serviceLocation: Service location for the VASA endpoint that SMS is using
           to communicate with the provider.
       needsExplicitActivation: Indicates the type of deployment supported by the provider.
           
           If true, it is an active/passive deployment and the provider needs to be
           activated explicitly using activateProviderEx() VASA API.
           If false, it is an active/active deployment and provider does not need any
           explicit activation to respond to VASA calls.
       maxBatchSize: Maximum number of elements in batch APIs that the VASA Provider can support.
           
           This value is common to all batch APIs supported by the provider. However,
           for each specific API, the provider may still throw or return `pyVmomi.sms.fault.TooMany`
           fault in which a different value of maxBatchSize can be specified.
           If the value is not specified (zero) or invalid (negative), client will
           assume there's no common limit for the number of elements that can be
           handled in all batch APIs.
       retainVasaProviderCertificate: Indicate whether the provider wants to retain its certificate after bootstrapping.
           
           If true, SMS will not provision a VMCA signed certificate for the provider
           and all certificate life cycle management workflows are disabled for this provider certificate.
           If false, SMS will provision a VMCA signed certificate for the provider and
           all certificate life cycle management workflows are enabled for this provider certificate.
       arrayIndependentProvider: Indicates if this provider is independent of arrays.
           
           Default value for this flag is false, which means this provider supports
           arrays. Arrays will be queried for this provider during sync. If this flag
           is set to true, arrays will not be synced for this provider and array
           related API will not be invoked on this provider.
       type: Type of this VASA provider.
           
           This field will be equal to one of the values of `pyVmomi.sms.provider.VasaProviderInfo.Type`.
       category: This field indicates the category of the provider and will be equal to one of the values of
           `pyVmomi.sms.provider.VasaProviderInfo.Category`.
       priority: Priority level of the provider within a VASA HA group.
           
           For a stand-alone
           provider which does not participate in VASA HA, this field will be ignored.
           
           The priority value is an integer with valid range from 0 to 255.
       failoverGroupId: Unique identifier of a VASA HA group.
           
           Providers should report this
           identifier to utilize HA feature supported by vSphere. Different providers
           reporting the same `failoverGroupId` will be treated as an HA
           group. Failover/failback will be done within one group.
   """
   class CertificateStatus(pyVmomi.VmomiSupport.Enum):
      """
      The status of the provider certificate
      
      Attributes:
          valid: Provider certificate is valid.
          expirySoftLimitReached: Provider certificate is within the soft limit threshold.
          expiryHardLimitReached: Provider certificate is within the hard limit threshold.
          expired: Provider certificate has expired.
          invalid: Provider certificate is revoked, malformed or missing.
      """
      valid: _typing.ClassVar['VasaProviderInfo.CertificateStatus'] = 'valid'
      expirySoftLimitReached: _typing.ClassVar['VasaProviderInfo.CertificateStatus'] = 'expirySoftLimitReached'
      expiryHardLimitReached: _typing.ClassVar['VasaProviderInfo.CertificateStatus'] = 'expiryHardLimitReached'
      expired: _typing.ClassVar['VasaProviderInfo.CertificateStatus'] = 'expired'
      invalid: _typing.ClassVar['VasaProviderInfo.CertificateStatus'] = 'invalid'

   class RelatedStorageArray(pyVmomi.vmodl.DynamicData):
      """
      Indicates whether the provider has been marked as active for the given array
      for the session context.
      
      SMS uses `pyVmomi.sms.storage.StorageArray.priority` value to mark a provider
      as active among the ones that are registered with SMS and manage this array.
      
      Attributes:
          arrayId: `pyVmomi.sms.storage.StorageArray.uuid` of StorageArray
          active: This field indicates whether the provider is currently serving data for the StorageArray
          manageable: Manageability status of StorageArray on VASA provider, if true it is manageable.
          priority: `pyVmomi.sms.storage.StorageArray.priority` of StorageArray
              For VASA 1.0 providers, this field is set to -1.
      """
      arrayId: str
      active: bool
      manageable: bool
      priority: int

   class SupportedVendorModelMapping(pyVmomi.vmodl.DynamicData):
      """
      Mapping between the supported vendorID and corresponding
      modelID
      
      Attributes:
          vendorId: SCSI Vendor ID
          modelId: SCSI Model ID
      """
      vendorId: _typing.Optional[str] = None
      modelId: _typing.Optional[str] = None

   class VasaProviderStatus(pyVmomi.VmomiSupport.Enum):
      """
      The operational state of VASA Provider.
      
      Attributes:
          online: VASA Provider is operating correctly.
          offline: VASA Provider is not responding, e.g.
              
              communication error due to temporary
              network outage. SMS keeps polling the provider in this state.
          syncError: VASA Provider is connected, but sync operation failed.
          unknown: VASA Provider is unreachable.
          connected: VASA Provider is connected, but has not triggered sync operation.
          disconnected: VASA Provider is disconnected, e.g.
              
              failed to establish a valid
              SSL connection to the provider. SMS stops communication with the
              provider in this state. The user can reconnect to the provider by invoking
              `pyVmomi.sms.provider.VasaProvider.reconnect`.
      """
      online: _typing.ClassVar['VasaProviderInfo.VasaProviderStatus'] = 'online'
      offline: _typing.ClassVar['VasaProviderInfo.VasaProviderStatus'] = 'offline'
      syncError: _typing.ClassVar['VasaProviderInfo.VasaProviderStatus'] = 'syncError'
      unknown: _typing.ClassVar['VasaProviderInfo.VasaProviderStatus'] = 'unknown'
      connected: _typing.ClassVar['VasaProviderInfo.VasaProviderStatus'] = 'connected'
      disconnected: _typing.ClassVar['VasaProviderInfo.VasaProviderStatus'] = 'disconnected'

   class VasaProviderProfile(pyVmomi.VmomiSupport.Enum):
      """
      Deprecated: As of SMS API 3.0, use `pyVmomi.sms.storage.StorageArray.VasaProfile`Profiles supported by VASA Provider.
      
      Attributes:
          blockDevice: Block device profile
          fileSystem: File system profile
          capability: Storage capability profile
      """
      blockDevice: _typing.ClassVar['VasaProviderInfo.VasaProviderProfile'] = 'blockDevice'
      fileSystem: _typing.ClassVar['VasaProviderInfo.VasaProviderProfile'] = 'fileSystem'
      capability: _typing.ClassVar['VasaProviderInfo.VasaProviderProfile'] = 'capability'

   class ProviderProfile(pyVmomi.VmomiSupport.Enum):
      """
      Profiles supported by VASA Provider.
      
      Attributes:
          ProfileBasedManagement: PBM profile
          Replication: Replication profile
      """
      ProfileBasedManagement: _typing.ClassVar['VasaProviderInfo.ProviderProfile'] = 'ProfileBasedManagement'
      Replication: _typing.ClassVar['VasaProviderInfo.ProviderProfile'] = 'Replication'

   class Type(pyVmomi.VmomiSupport.Enum):
      """
      VASA Provider type.
      
      Attributes:
          PERSISTENCE: Persistence provider.
          DATASERVICE: DataService provider.
              
              No storage supported for this type of provider.
          UNKNOWN: Type is unknown.
              
              VASA provider type can be UNKNOWN when it is undergoing sync operation.
      """
      PERSISTENCE: _typing.ClassVar['VasaProviderInfo.Type'] = 'PERSISTENCE'
      DATASERVICE: _typing.ClassVar['VasaProviderInfo.Type'] = 'DATASERVICE'
      UNKNOWN: _typing.ClassVar['VasaProviderInfo.Type'] = 'UNKNOWN'

   class Category(pyVmomi.VmomiSupport.Enum):
      """
      A Category to indicate whether provider is of internal or external category.
      
      This classification can help selectively enable few administrative functions
      such as say unregistration of a provider.
      
      Attributes:
          internal: An internal provider category indicates the set of providers such as IOFILTERS and VSAN.
          external: An external provider category indicates the set of providers are external and not belong
              to say either of IOFILTERS or VSAN category.
      """
      internal: _typing.ClassVar['VasaProviderInfo.Category'] = 'internal'
      external: _typing.ClassVar['VasaProviderInfo.Category'] = 'external'

   url: str
   certificate: _typing.Optional[str] = None
   status: _typing.Optional[str] = None
   statusFault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   vasaVersion: _typing.Optional[str] = None
   namespace: _typing.Optional[str] = None
   lastSyncTime: _typing.Optional[str] = None
   supportedVendorModelMapping: list[VasaProviderInfo.SupportedVendorModelMapping] = []
   supportedProfile: list[str] = []
   supportedProviderProfile: list[str] = []
   relatedStorageArray: list[VasaProviderInfo.RelatedStorageArray] = []
   providerId: _typing.Optional[str] = None
   certificateExpiryDate: _typing.Optional[str] = None
   certificateStatus: _typing.Optional[str] = None
   serviceLocation: _typing.Optional[str] = None
   needsExplicitActivation: _typing.Optional[bool] = None
   maxBatchSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   retainVasaProviderCertificate: _typing.Optional[bool] = None
   arrayIndependentProvider: _typing.Optional[bool] = None
   type: _typing.Optional[str] = None
   category: _typing.Optional[str] = None
   priority: _typing.Optional[int] = None
   failoverGroupId: _typing.Optional[str] = None


class VasaProviderSpec(ProviderSpec):
   """
   VASA(vStorage APIs for Storage Awareness) provider
   specification
   
   Attributes:
       username: Username
           The maximum length of the username is 255 characters.
       password: Password
           The maximum length of the password is 255 characters.
       url: URL
       certificate: Certificate
   """
   username: str
   password: str
   url: str
   certificate: _typing.Optional[str] = None
