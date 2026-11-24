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
   alarmStatus: _typing.Optional[str] = None
   alarmType: _typing.Optional[str] = None
   entityType: _typing.Optional[str] = None
   entityId: list[object] = []
   pageMarker: _typing.Optional[str] = None


class AlarmResult(pyVmomi.vmodl.DynamicData):
   storageAlarm: list[pyVmomi.sms.storage.StorageAlarm] = []
   pageMarker: _typing.Optional[str] = None


class Provider(pyVmomi.VmomiSupport.ManagedObject):
   def QueryProviderInfo(self) -> ProviderInfo: ...


class ProviderInfo(pyVmomi.vmodl.DynamicData):
   uid: str
   name: str
   description: _typing.Optional[str] = None
   version: _typing.Optional[str] = None


class ProviderSpec(pyVmomi.vmodl.DynamicData):
   name: str
   description: _typing.Optional[str] = None


class VASAProviderUpgradeSpec(pyVmomi.vmodl.DynamicData):
   providerUid: str
   username: str
   password: str


class VasaProvider(Provider):
   def Sync(self, arrayId: _typing.Optional[str]) -> pyVmomi.vim.Task: ...
   def RefreshCertificate(self) -> pyVmomi.vim.Task: ...
   def RevokeCertificate(self) -> pyVmomi.vim.Task: ...
   def Reconnect(self) -> pyVmomi.vim.Task: ...
   def QueryReplicationPeer(self, faultDomainId: list[pyVmomi.vim.vm.replication.FaultDomainId]) -> list[pyVmomi.sms.storage.replication.QueryReplicationPeerResult]: ...
   def QueryReplicationGroup(self, groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId]) -> list[pyVmomi.sms.storage.replication.GroupOperationResult]: ...
   def QueryPointInTimeReplica(self, groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId], queryParam: _typing.Optional[pyVmomi.sms.storage.replication.QueryPointInTimeReplicaParam]) -> list[pyVmomi.sms.storage.replication.GroupOperationResult]: ...
   def TestFailoverReplicationGroupStart(self, testFailoverParam: pyVmomi.sms.storage.replication.TestFailoverParam) -> pyVmomi.vim.Task: ...
   def TestFailoverReplicationGroupStop(self, groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId], force: bool) -> pyVmomi.vim.Task: ...
   def PromoteReplicationGroup(self, promoteParam: pyVmomi.sms.storage.replication.PromoteParam) -> pyVmomi.vim.Task: ...
   def SyncReplicationGroup(self, groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId], pitName: str) -> pyVmomi.vim.Task: ...
   def PrepareFailoverReplicationGroup(self, groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId]) -> pyVmomi.vim.Task: ...
   def FailoverReplicationGroup(self, failoverParam: pyVmomi.sms.storage.replication.FailoverParam) -> pyVmomi.vim.Task: ...
   def ReverseReplicateGroup(self, groupId: list[pyVmomi.vim.vm.replication.ReplicationGroupId]) -> pyVmomi.vim.Task: ...
   def QueryActiveAlarm(self, alarmFilter: _typing.Optional[AlarmFilter]) -> _typing.Optional[AlarmResult]: ...


class VasaProviderInfo(ProviderInfo):
   class CertificateStatus(pyVmomi.VmomiSupport.Enum):
      valid: _typing.ClassVar['CertificateStatus'] = 'valid'
      expirySoftLimitReached: _typing.ClassVar['CertificateStatus'] = 'expirySoftLimitReached'
      expiryHardLimitReached: _typing.ClassVar['CertificateStatus'] = 'expiryHardLimitReached'
      expired: _typing.ClassVar['CertificateStatus'] = 'expired'
      invalid: _typing.ClassVar['CertificateStatus'] = 'invalid'

   class RelatedStorageArray(pyVmomi.vmodl.DynamicData):
      arrayId: str
      active: bool
      manageable: bool
      priority: int

   class SupportedVendorModelMapping(pyVmomi.vmodl.DynamicData):
      vendorId: _typing.Optional[str] = None
      modelId: _typing.Optional[str] = None

   class VasaProviderStatus(pyVmomi.VmomiSupport.Enum):
      online: _typing.ClassVar['VasaProviderStatus'] = 'online'
      offline: _typing.ClassVar['VasaProviderStatus'] = 'offline'
      syncError: _typing.ClassVar['VasaProviderStatus'] = 'syncError'
      unknown: _typing.ClassVar['VasaProviderStatus'] = 'unknown'
      connected: _typing.ClassVar['VasaProviderStatus'] = 'connected'
      disconnected: _typing.ClassVar['VasaProviderStatus'] = 'disconnected'

   class VasaProviderProfile(pyVmomi.VmomiSupport.Enum):
      blockDevice: _typing.ClassVar['VasaProviderProfile'] = 'blockDevice'
      fileSystem: _typing.ClassVar['VasaProviderProfile'] = 'fileSystem'
      capability: _typing.ClassVar['VasaProviderProfile'] = 'capability'

   class ProviderProfile(pyVmomi.VmomiSupport.Enum):
      ProfileBasedManagement: _typing.ClassVar['ProviderProfile'] = 'ProfileBasedManagement'
      Replication: _typing.ClassVar['ProviderProfile'] = 'Replication'

   class Type(pyVmomi.VmomiSupport.Enum):
      PERSISTENCE: _typing.ClassVar['Type'] = 'PERSISTENCE'
      DATASERVICE: _typing.ClassVar['Type'] = 'DATASERVICE'
      UNKNOWN: _typing.ClassVar['Type'] = 'UNKNOWN'

   class Category(pyVmomi.VmomiSupport.Enum):
      internal: _typing.ClassVar['Category'] = 'internal'
      external: _typing.ClassVar['Category'] = 'external'

   url: str
   certificate: _typing.Optional[str] = None
   status: _typing.Optional[str] = None
   statusFault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   vasaVersion: _typing.Optional[str] = None
   namespace: _typing.Optional[str] = None
   lastSyncTime: _typing.Optional[str] = None
   supportedVendorModelMapping: list[SupportedVendorModelMapping] = []
   supportedProfile: list[str] = []
   supportedProviderProfile: list[str] = []
   relatedStorageArray: list[RelatedStorageArray] = []
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
   username: str
   password: str
   url: str
   certificate: _typing.Optional[str] = None
