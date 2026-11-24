# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import replication as replication

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.sms
import pyVmomi.vmodl
import pyVmomi.sms.storage
import pyVmomi.vim.fault
import pyVmomi.vmodl.fault
import pyVmomi.sms.storage.replication



class AuthConnectionFailed(pyVmomi.vim.fault.NoPermission):
   """
   This exception is thrown when an error occurs while
   connecting to the vpxd service to validate the user
   credentials
   """
   pass


class ProviderRegistrationFault(pyVmomi.vmodl.MethodFault):
   """
   This fault is thrown if failed to register provider to storage
   management service.
   """
   pass

class CertificateAuthorityFault(ProviderRegistrationFault):
   """
   This exception is thrown if there is a problem with calls to the
   CertificateAuthority.
   
   Attributes:
       faultCode: Fault code returned by certificate authority.
   """
   faultCode: int

class CertificateNotImported(ProviderRegistrationFault):
   """
   This exception is thrown if `pyVmomi.sms.provider.VasaProviderInfo.retainVasaProviderCertificate`
   is true and the provider uses a certificate issued by a Certificate Authority,
   but the root certificate of the Certificate Authority is not imported to VECS truststore
   before attempting the provider registration.
   """
   pass

class CertificateNotTrusted(ProviderRegistrationFault):
   """
   This exception is thrown if the certificate provided by the
   provider is not trusted.
   
   Attributes:
       certificate: Certificate
   """
   certificate: str


class CertificateRefreshFailed(pyVmomi.vmodl.MethodFault):
   """
   This exception is thrown if SMS failed to
   refresh a CA signed certificate for the provider (or)
   push the latest CA root certificates and CRLs to the provider.
   """
   providerId: list[str] = []


class CertificateRevocationFailed(pyVmomi.vmodl.MethodFault):
   """This exception is thrown if SMS failed to revoke CA signed certificate of the provider."""
   pass


class DuplicateEntry(pyVmomi.vmodl.MethodFault):
   """This exception indicates there are duplicate entries in the input argument."""
   pass


class InactiveProvider(pyVmomi.vmodl.MethodFault):
   """
   Thrown if the VASA Provider on which the call is made is currently not
   active.
   
   If the client maintains a cache of the topology of fault domains
   and replication groups, it's expected to update the cache based on the
   mapping information set in this fault.
   
   Attributes:
       mapping: Mapping between VASA provider and the fault domains
   """
   mapping: list[pyVmomi.sms.storage.FaultDomainProviderMapping] = []

class IncorrectUsernamePassword(ProviderRegistrationFault):
   """This fault is thrown if failed to register provider due to incorrect credentials."""
   pass

class InvalidCertificate(ProviderRegistrationFault):
   """
   This exception is thrown if the provider certificate is empty, malformed,
   expired, not yet valid, revoked or fails host name verification.
   
   Attributes:
       certificate: Provider certificate
   """
   certificate: str


class InvalidLogin(pyVmomi.vmodl.MethodFault):
   """
   Thrown when login fails due to token not provided or token could not be
   validated.
   """
   pass


class InvalidProfile(pyVmomi.vmodl.MethodFault):
   """This exception is thrown if the specified storage profile is invalid."""
   pass


class InvalidSession(pyVmomi.vim.fault.NoPermission):
   """
   This exception is thrown if a specified session is invalid.
   
   This can occur if the VirtualCenter session referred to by
   the cookie has timed out or has been closed.
   
   Attributes:
       sessionCookie: VirtualCenter session cookie that is invalid.
   """
   sessionCookie: str

class InvalidUrl(ProviderRegistrationFault):
   """
   This exception is thrown if `pyVmomi.sms.provider.VasaProviderSpec.url` is malformed.
   
   Attributes:
       url: Provider `pyVmomi.sms.provider.VasaProviderSpec.url`
   """
   url: str


class MultipleSortSpecsNotSupported(pyVmomi.vmodl.fault.InvalidArgument):
   """
   This exception is thrown if more than one sort spec is
   specified in a list query.
   """
   pass


class QueryExecutionFault(pyVmomi.vmodl.MethodFault):
   """
   This exception is thrown if a failure occurs while
   processing a query request.
   """
   pass

class NoCommonProviderForAllBackings(QueryExecutionFault):
   """
   This fault is thrown when backings (@link
   sms.storage.StorageLun/ @link sms.storage.StorageFileSystem)
   of the specified datastores refer to different
   VASA providers.
   """
   pass


class NotSupportedByProvider(pyVmomi.vmodl.MethodFault):
   """
   This exception is thrown if the VASA Provider on which the call is made
   does not support this operation.
   """
   pass


class ProviderBusy(pyVmomi.vmodl.MethodFault):
   """
   This exception is thrown if the VASA Provider on which the call is made
   is currently busy.
   """
   pass


class ProviderConnectionFailed(pyVmomi.vmodl.RuntimeFault):
   """This fault is thrown if the Storage Monitoring Service failed to connect to the VASA provider."""
   pass

class ProviderNotFound(QueryExecutionFault):
   """
   This fault is thrown when a VASA provider cannot be found for the specified
   entities.
   """
   pass


class ProviderOutOfProvisioningResource(pyVmomi.vmodl.MethodFault):
   """
   This exception is thrown if the VASA Provider is out of resource to satisfy
   a provisioning request.
   
   Attributes:
       provisioningResourceId: Identifier of the provisioning resource.
       availableBefore: Currently available.
       availableAfter: Necessary for provisioning.
       total: Total amount (free + used).
       isTransient: This resource limitation is transient, i.e.
           
           the resource
           will be available after some time.
   """
   provisioningResourceId: str
   availableBefore: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   availableAfter: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   total: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   isTransient: _typing.Optional[bool] = None


class ProviderOutOfResource(pyVmomi.vmodl.MethodFault):
   """
   This exception is thrown if the VASA Provider on which the call is made
   is out of resource.
   """
   pass


class ProviderSyncFailed(pyVmomi.vmodl.MethodFault):
   """
   Thrown if a failure occurs when synchronizing the service
   cache with provider information.
   """
   pass


class ProviderUnavailable(pyVmomi.vmodl.MethodFault):
   """
   This exception is thrown if the VASA Provider on which the call is made is
   currently not available, e.g.
   
   VASA Provider is in offline state. This error
   usually means the provider is temporarily unavailable due to network outage, etc.
   The client is expected to wait for some time and retry the same call.
   """
   pass


class ProviderUnregistrationFault(pyVmomi.vmodl.MethodFault):
   """
   This fault is thrown if failed to unregister provider from storage
   management service.
   """
   pass


class ProxyRegistrationFailed(pyVmomi.vmodl.RuntimeFault):
   """
   This exception is thrown if the storage management service
   fails to register with the VirtualCenter proxy during
   initialization.
   """
   pass


class QueryNotSupported(pyVmomi.vmodl.fault.InvalidArgument):
   """
   This exception is thrown if the specified entity and related
   entity type combination for a list query is not supported.
   
   Attributes:
       entityType: Entity type.
       relatedEntityType: Related entity type.
   """
   entityType: _typing.Optional[pyVmomi.sms.EntityReference.EntityType] = None
   relatedEntityType: pyVmomi.sms.EntityReference.EntityType


class ResourceInUse(pyVmomi.vim.fault.ResourceInUse):
   """
   A ResourceInUse fault indicating that some error has occurred because
   some resources are in use.
   
   Information about the devices that are in
   use may be supplied.
   
   Attributes:
       deviceIds: The list of device Ids that are in use.
   """
   deviceIds: list[pyVmomi.sms.storage.replication.DeviceId] = []


class ServiceNotInitialized(pyVmomi.vmodl.RuntimeFault):
   """
   This exception is thrown if the storage management service
   has not yet been initialized successfully and therefore is
   not ready to process requests.
   """
   pass


class SmsFault(pyVmomi.vmodl.MethodFault):
   """The common base type for all SMS faults."""
   pass

class SyncInProgress(ProviderSyncFailed):
   """
   This exception is thrown if a sync operation is invoked
   while another sync invocation is in progress.
   """
   pass


class TooMany(pyVmomi.vmodl.MethodFault):
   """
   This exception is thrown if the request exceeds the maximum number of
   elements in batch that the VASA Provider can support for the specific API.
   
   Attributes:
       maxBatchSize: Maximum number of elements in batch that the VASA Provider can support
           for the specific API.
           
           If the value is not specified (zero) or invalid
           (negative), client will assume the default value is 1.
   """
   maxBatchSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
