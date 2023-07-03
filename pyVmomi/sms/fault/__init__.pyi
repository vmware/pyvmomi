from typing import List, Literal
from pyVmomi import sms, vim, vmodl
from pyVmomi.VmomiSupport import long
from . import replication as replication


class AuthConnectionFailed(vim.fault.NoPermission): ...


class CertificateAuthorityFault(ProviderRegistrationFault):
    @property
    def faultCode(self) -> int: ...
    @faultCode.setter
    def faultCode(self, value: int):
        self._faultCode = value


class CertificateNotImported(ProviderRegistrationFault): ...


class CertificateNotTrusted(ProviderRegistrationFault):
    @property
    def certificate(self) -> str: ...
    @certificate.setter
    def certificate(self, value: str):
        self._certificate = value


class CertificateRefreshFailed(vmodl.MethodFault):
    @property
    def providerId(self) -> List[str]: ...
    @providerId.setter
    def providerId(self, value: List[str]):
        self._providerId = value


class CertificateRevocationFailed(vmodl.MethodFault): ...


class DuplicateEntry(vmodl.MethodFault): ...


class InactiveProvider(vmodl.MethodFault):
    @property
    def mapping(self) -> List[sms.storage.FaultDomainProviderMapping]: ...
    @mapping.setter
    def mapping(self, value: List[sms.storage.FaultDomainProviderMapping]):
        self._mapping = value


class IncorrectUsernamePassword(ProviderRegistrationFault): ...


class InvalidCertificate(ProviderRegistrationFault):
    @property
    def certificate(self) -> str: ...
    @certificate.setter
    def certificate(self, value: str):
        self._certificate = value


class InvalidLogin(vmodl.MethodFault): ...


class InvalidProfile(vmodl.MethodFault): ...


class InvalidSession(vim.fault.NoPermission):
    @property
    def sessionCookie(self) -> str: ...
    @sessionCookie.setter
    def sessionCookie(self, value: str):
        self._sessionCookie = value


class InvalidUrl(ProviderRegistrationFault):
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, value: str):
        self._url = value


class MultipleSortSpecsNotSupported(vmodl.fault.InvalidArgument): ...


class NoCommonProviderForAllBackings(QueryExecutionFault): ...


class NotSupportedByProvider(vmodl.MethodFault): ...


class ProviderBusy(vmodl.MethodFault): ...


class ProviderConnectionFailed(vmodl.RuntimeFault): ...


class ProviderNotFound(QueryExecutionFault): ...


class ProviderOutOfProvisioningResource(vmodl.MethodFault):
    @property
    def provisioningResourceId(self) -> str: ...
    @provisioningResourceId.setter
    def provisioningResourceId(self, value: str):
        self._provisioningResourceId = value
    @property
    def availableBefore(self) -> long: ...
    @availableBefore.setter
    def availableBefore(self, value: long):
        self._availableBefore = value
    @property
    def availableAfter(self) -> long: ...
    @availableAfter.setter
    def availableAfter(self, value: long):
        self._availableAfter = value
    @property
    def total(self) -> long: ...
    @total.setter
    def total(self, value: long):
        self._total = value
    @property
    def isTransient(self) -> bool: ...
    @isTransient.setter
    def isTransient(self, value: bool):
        self._isTransient = value


class ProviderOutOfResource(vmodl.MethodFault): ...


class ProviderRegistrationFault(vmodl.MethodFault): ...


class ProviderSyncFailed(vmodl.MethodFault): ...


class ProviderUnavailable(vmodl.MethodFault): ...


class ProviderUnregistrationFault(vmodl.MethodFault): ...


class ProxyRegistrationFailed(vmodl.RuntimeFault): ...


class QueryExecutionFault(vmodl.MethodFault): ...


class QueryNotSupported(vmodl.fault.InvalidArgument):
    @property
    def entityType(self) -> sms.EntityReference.EntityType | Literal['datacenter', 'resourcePool', 'storagePod', 'cluster', 'vm', 'datastore', 'host', 'vmFile', 'scsiPath', 'scsiTarget', 'scsiVolume', 'scsiAdapter', 'nasMount']: ...
    @entityType.setter
    def entityType(self, value: sms.EntityReference.EntityType | Literal['datacenter', 'resourcePool', 'storagePod', 'cluster', 'vm', 'datastore', 'host', 'vmFile', 'scsiPath', 'scsiTarget', 'scsiVolume', 'scsiAdapter', 'nasMount']):
        self._entityType = value
    @property
    def relatedEntityType(self) -> sms.EntityReference.EntityType | Literal['datacenter', 'resourcePool', 'storagePod', 'cluster', 'vm', 'datastore', 'host', 'vmFile', 'scsiPath', 'scsiTarget', 'scsiVolume', 'scsiAdapter', 'nasMount']: ...
    @relatedEntityType.setter
    def relatedEntityType(self, value: sms.EntityReference.EntityType | Literal['datacenter', 'resourcePool', 'storagePod', 'cluster', 'vm', 'datastore', 'host', 'vmFile', 'scsiPath', 'scsiTarget', 'scsiVolume', 'scsiAdapter', 'nasMount']):
        self._relatedEntityType = value


class ResourceInUse(vim.fault.ResourceInUse):
    @property
    def deviceIds(self) -> List[sms.storage.replication.DeviceId]: ...
    @deviceIds.setter
    def deviceIds(self, value: List[sms.storage.replication.DeviceId]):
        self._deviceIds = value


class ServiceNotInitialized(vmodl.RuntimeFault): ...


class SyncInProgress(ProviderSyncFailed): ...


class TooMany(vmodl.MethodFault):
    @property
    def maxBatchSize(self) -> long: ...
    @maxBatchSize.setter
    def maxBatchSize(self, value: long):
        self._maxBatchSize = value