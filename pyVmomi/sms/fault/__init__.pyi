from typing import List
from pyVmomi import sms, vim, vmodl
from pyVmomi.VmomiSupport import long


class AuthConnectionFailed(NoPermission): ...


class CertificateAuthorityFault(ProviderRegistrationFault):
    @property
    def faultCode(self) -> int: ...


class CertificateNotImported(ProviderRegistrationFault): ...


class CertificateNotTrusted(ProviderRegistrationFault):
    @property
    def certificate(self) -> str: ...


class CertificateRefreshFailed(vmodl.MethodFault):
    @property
    def providerId(self) -> List[str]: ...


class CertificateRevocationFailed(vmodl.MethodFault): ...


class DuplicateEntry(vmodl.MethodFault): ...


class InactiveProvider(vmodl.MethodFault):
    @property
    def mapping(self) -> List[sms.storage.FaultDomainProviderMapping]: ...


class IncorrectUsernamePassword(ProviderRegistrationFault): ...


class InvalidCertificate(ProviderRegistrationFault):
    @property
    def certificate(self) -> str: ...


class InvalidLogin(vmodl.MethodFault): ...


class InvalidProfile(vmodl.MethodFault): ...


class InvalidSession(NoPermission):
    @property
    def sessionCookie(self) -> str: ...


class InvalidUrl(ProviderRegistrationFault):
    @property
    def url(self) -> str: ...


class MultipleSortSpecsNotSupported(InvalidArgument): ...


class NoCommonProviderForAllBackings(QueryExecutionFault): ...


class NotSupportedByProvider(vmodl.MethodFault): ...


class ProviderBusy(vmodl.MethodFault): ...


class ProviderConnectionFailed(vmodl.RuntimeFault): ...


class ProviderNotFound(QueryExecutionFault): ...


class ProviderOutOfProvisioningResource(vmodl.MethodFault):
    @property
    def provisioningResourceId(self) -> str: ...
    @property
    def availableBefore(self) -> long: ...
    @property
    def availableAfter(self) -> long: ...
    @property
    def total(self) -> long: ...
    @property
    def isTransient(self) -> bool: ...


class ProviderOutOfResource(vmodl.MethodFault): ...


class ProviderRegistrationFault(vmodl.MethodFault): ...


class ProviderSyncFailed(vmodl.MethodFault): ...


class ProviderUnavailable(vmodl.MethodFault): ...


class ProviderUnregistrationFault(vmodl.MethodFault): ...


class ProxyRegistrationFailed(vmodl.RuntimeFault): ...


class QueryExecutionFault(vmodl.MethodFault): ...


class QueryNotSupported(InvalidArgument):
    @property
    def entityType(self) -> sms.EntityReference.EntityType: ...
    @property
    def relatedEntityType(self) -> sms.EntityReference.EntityType: ...


class ResourceInUse(ResourceInUse):
    @property
    def deviceIds(self) -> List[sms.storage.replication.DeviceId]: ...


class ServiceNotInitialized(vmodl.RuntimeFault): ...


class SyncInProgress(ProviderSyncFailed): ...


class TooMany(vmodl.MethodFault):
    @property
    def maxBatchSize(self) -> long: ...