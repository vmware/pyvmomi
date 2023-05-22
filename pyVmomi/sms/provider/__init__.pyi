from typing import List
from enum import Enum
from pyVmomi import sms, vim, vmodl
from pyVmomi.VmomiSupport import ManagedObject, long


class Provider(ManagedObject):
    def QueryProviderInfo(self) -> ProviderInfo: ...


class VasaProvider(Provider):
    def Sync(self, arrayId: str) -> sms.Task: ...
    def RefreshCertificate(self) -> sms.Task: ...
    def RevokeCertificate(self) -> sms.Task: ...
    def Reconnect(self) -> sms.Task: ...
    def QueryReplicationPeer(self, faultDomainId: List[vim.vm.replication.FaultDomainId]) -> List[sms.storage.replication.QueryReplicationPeerResult]: ...
    def QueryReplicationGroup(self, groupId: List[vim.vm.replication.ReplicationGroupId]) -> List[sms.storage.replication.GroupOperationResult]: ...
    def QueryPointInTimeReplica(self, groupId: List[vim.vm.replication.ReplicationGroupId], queryParam: sms.storage.replication.QueryPointInTimeReplicaParam) -> List[sms.storage.replication.GroupOperationResult]: ...
    def TestFailoverReplicationGroupStart(self, testFailoverParam: sms.storage.replication.TestFailoverParam) -> sms.Task: ...
    def TestFailoverReplicationGroupStop(self, groupId: List[vim.vm.replication.ReplicationGroupId], force: bool) -> sms.Task: ...
    def PromoteReplicationGroup(self, promoteParam: sms.storage.replication.PromoteParam) -> sms.Task: ...
    def SyncReplicationGroup(self, groupId: List[vim.vm.replication.ReplicationGroupId], pitName: str) -> sms.Task: ...
    def PrepareFailoverReplicationGroup(self, groupId: List[vim.vm.replication.ReplicationGroupId]) -> sms.Task: ...
    def FailoverReplicationGroup(self, failoverParam: sms.storage.replication.FailoverParam) -> sms.Task: ...
    def ReverseReplicateGroup(self, groupId: List[vim.vm.replication.ReplicationGroupId]) -> sms.Task: ...
    def QueryActiveAlarm(self, alarmFilter: AlarmFilter) -> AlarmResult: ...


class AlarmFilter(vmodl.DynamicData):
    @property
    def alarmStatus(self) -> str: ...
    @alarmStatus.setter
    def alarmStatus(self, value: str):
        self._alarmStatus = value
    @property
    def alarmType(self) -> str: ...
    @alarmType.setter
    def alarmType(self, value: str):
        self._alarmType = value
    @property
    def entityType(self) -> str: ...
    @entityType.setter
    def entityType(self, value: str):
        self._entityType = value
    @property
    def entityId(self) -> List[object]: ...
    @entityId.setter
    def entityId(self, value: List[object]):
        self._entityId = value
    @property
    def pageMarker(self) -> str: ...
    @pageMarker.setter
    def pageMarker(self, value: str):
        self._pageMarker = value


class AlarmResult(vmodl.DynamicData):
    @property
    def storageAlarm(self) -> List[sms.storage.StorageAlarm]: ...
    @storageAlarm.setter
    def storageAlarm(self, value: List[sms.storage.StorageAlarm]):
        self._storageAlarm = value
    @property
    def pageMarker(self) -> str: ...
    @pageMarker.setter
    def pageMarker(self, value: str):
        self._pageMarker = value


class ProviderInfo(vmodl.DynamicData):
    @property
    def uid(self) -> str: ...
    @uid.setter
    def uid(self, value: str):
        self._uid = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value


class ProviderSpec(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value


class VasaProviderInfo(ProviderInfo):
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, value: str):
        self._url = value
    @property
    def certificate(self) -> str: ...
    @certificate.setter
    def certificate(self, value: str):
        self._certificate = value
    @property
    def status(self) -> str: ...
    @status.setter
    def status(self, value: str):
        self._status = value
    @property
    def statusFault(self) -> vmodl.MethodFault: ...
    @statusFault.setter
    def statusFault(self, value: vmodl.MethodFault):
        self._statusFault = value
    @property
    def vasaVersion(self) -> str: ...
    @vasaVersion.setter
    def vasaVersion(self, value: str):
        self._vasaVersion = value
    @property
    def namespace(self) -> str: ...
    @namespace.setter
    def namespace(self, value: str):
        self._namespace = value
    @property
    def lastSyncTime(self) -> str: ...
    @lastSyncTime.setter
    def lastSyncTime(self, value: str):
        self._lastSyncTime = value
    @property
    def supportedVendorModelMapping(self) -> List[VasaProviderInfo.SupportedVendorModelMapping]: ...
    @supportedVendorModelMapping.setter
    def supportedVendorModelMapping(self, value: List[VasaProviderInfo.SupportedVendorModelMapping]):
        self._supportedVendorModelMapping = value
    @property
    def supportedProfile(self) -> List[str]: ...
    @supportedProfile.setter
    def supportedProfile(self, value: List[str]):
        self._supportedProfile = value
    @property
    def supportedProviderProfile(self) -> List[str]: ...
    @supportedProviderProfile.setter
    def supportedProviderProfile(self, value: List[str]):
        self._supportedProviderProfile = value
    @property
    def relatedStorageArray(self) -> List[VasaProviderInfo.RelatedStorageArray]: ...
    @relatedStorageArray.setter
    def relatedStorageArray(self, value: List[VasaProviderInfo.RelatedStorageArray]):
        self._relatedStorageArray = value
    @property
    def providerId(self) -> str: ...
    @providerId.setter
    def providerId(self, value: str):
        self._providerId = value
    @property
    def certificateExpiryDate(self) -> str: ...
    @certificateExpiryDate.setter
    def certificateExpiryDate(self, value: str):
        self._certificateExpiryDate = value
    @property
    def certificateStatus(self) -> str: ...
    @certificateStatus.setter
    def certificateStatus(self, value: str):
        self._certificateStatus = value
    @property
    def serviceLocation(self) -> str: ...
    @serviceLocation.setter
    def serviceLocation(self, value: str):
        self._serviceLocation = value
    @property
    def needsExplicitActivation(self) -> bool: ...
    @needsExplicitActivation.setter
    def needsExplicitActivation(self, value: bool):
        self._needsExplicitActivation = value
    @property
    def maxBatchSize(self) -> long: ...
    @maxBatchSize.setter
    def maxBatchSize(self, value: long):
        self._maxBatchSize = value
    @property
    def retainVasaProviderCertificate(self) -> bool: ...
    @retainVasaProviderCertificate.setter
    def retainVasaProviderCertificate(self, value: bool):
        self._retainVasaProviderCertificate = value
    @property
    def arrayIndependentProvider(self) -> bool: ...
    @arrayIndependentProvider.setter
    def arrayIndependentProvider(self, value: bool):
        self._arrayIndependentProvider = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def category(self) -> str: ...
    @category.setter
    def category(self, value: str):
        self._category = value
    @property
    def priority(self) -> int: ...
    @priority.setter
    def priority(self, value: int):
        self._priority = value
    @property
    def failoverGroupId(self) -> str: ...
    @failoverGroupId.setter
    def failoverGroupId(self, value: str):
        self._failoverGroupId = value


    class RelatedStorageArray(vmodl.DynamicData):
        @property
        def arrayId(self) -> str: ...
        @arrayId.setter
        def arrayId(self, value: str):
            self._arrayId = value
        @property
        def active(self) -> bool: ...
        @active.setter
        def active(self, value: bool):
            self._active = value
        @property
        def manageable(self) -> bool: ...
        @manageable.setter
        def manageable(self, value: bool):
            self._manageable = value
        @property
        def priority(self) -> int: ...
        @priority.setter
        def priority(self, value: int):
            self._priority = value


    class SupportedVendorModelMapping(vmodl.DynamicData):
        @property
        def vendorId(self) -> str: ...
        @vendorId.setter
        def vendorId(self, value: str):
            self._vendorId = value
        @property
        def modelId(self) -> str: ...
        @modelId.setter
        def modelId(self, value: str):
            self._modelId = value


    class Category(Enum):
        internal = "internal"
        external = "external"


    class CertificateStatus(Enum):
        valid = "valid"
        expirySoftLimitReached = "expirySoftLimitReached"
        expiryHardLimitReached = "expiryHardLimitReached"
        expired = "expired"
        invalid = "invalid"


    class ProviderProfile(Enum):
        ProfileBasedManagement = "ProfileBasedManagement"
        Replication = "Replication"


    class Type(Enum):
        PERSISTENCE = "PERSISTENCE"
        DATASERVICE = "DATASERVICE"
        UNKNOWN = "UNKNOWN"


    class VasaProviderProfile(Enum):
        blockDevice = "blockDevice"
        fileSystem = "fileSystem"
        capability = "capability"


    class VasaProviderStatus(Enum):
        online = "online"
        offline = "offline"
        syncError = "syncError"
        unknown = "unknown"
        connected = "connected"
        disconnected = "disconnected"


class VasaProviderSpec(ProviderSpec):
    @property
    def username(self) -> str: ...
    @username.setter
    def username(self, value: str):
        self._username = value
    @property
    def password(self) -> str: ...
    @password.setter
    def password(self, value: str):
        self._password = value
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, value: str):
        self._url = value
    @property
    def certificate(self) -> str: ...
    @certificate.setter
    def certificate(self, value: str):
        self._certificate = value


class VmodlVasaProviderSpec():


    class AuthenticationType(Enum):
        LoginByToken = "LoginByToken"
        UseSessionId = "UseSessionId"