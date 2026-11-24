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
   pass

class CertificateAuthorityFault(ProviderRegistrationFault):
   faultCode: int

class CertificateNotImported(ProviderRegistrationFault):
   pass

class CertificateNotTrusted(ProviderRegistrationFault):
   certificate: str


class CertificateRefreshFailed(pyVmomi.vmodl.MethodFault):
   providerId: list[str] = []


class CertificateRevocationFailed(pyVmomi.vmodl.MethodFault):
   pass


class DuplicateEntry(pyVmomi.vmodl.MethodFault):
   pass


class InactiveProvider(pyVmomi.vmodl.MethodFault):
   mapping: list[pyVmomi.sms.storage.FaultDomainProviderMapping] = []

class IncorrectUsernamePassword(ProviderRegistrationFault):
   pass

class InvalidCertificate(ProviderRegistrationFault):
   certificate: str


class InvalidLogin(pyVmomi.vmodl.MethodFault):
   pass


class InvalidProfile(pyVmomi.vmodl.MethodFault):
   pass


class InvalidSession(pyVmomi.vim.fault.NoPermission):
   sessionCookie: str

class InvalidUrl(ProviderRegistrationFault):
   url: str


class MultipleSortSpecsNotSupported(pyVmomi.vmodl.fault.InvalidArgument):
   pass

class NoCommonProviderForAllBackings(QueryExecutionFault):
   pass


class NotSupportedByProvider(pyVmomi.vmodl.MethodFault):
   pass


class ProviderBusy(pyVmomi.vmodl.MethodFault):
   pass


class ProviderConnectionFailed(pyVmomi.vmodl.RuntimeFault):
   pass

class ProviderNotFound(QueryExecutionFault):
   pass


class ProviderOutOfProvisioningResource(pyVmomi.vmodl.MethodFault):
   provisioningResourceId: str
   availableBefore: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   availableAfter: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   total: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   isTransient: _typing.Optional[bool] = None


class ProviderOutOfResource(pyVmomi.vmodl.MethodFault):
   pass


class ProviderRegistrationFault(pyVmomi.vmodl.MethodFault):
   pass


class ProviderSyncFailed(pyVmomi.vmodl.MethodFault):
   pass


class ProviderUnavailable(pyVmomi.vmodl.MethodFault):
   pass


class ProviderUnregistrationFault(pyVmomi.vmodl.MethodFault):
   pass


class ProxyRegistrationFailed(pyVmomi.vmodl.RuntimeFault):
   pass


class QueryExecutionFault(pyVmomi.vmodl.MethodFault):
   pass


class QueryNotSupported(pyVmomi.vmodl.fault.InvalidArgument):
   entityType: _typing.Optional[pyVmomi.sms.EntityReference.EntityType] = None
   relatedEntityType: pyVmomi.sms.EntityReference.EntityType


class ResourceInUse(pyVmomi.vim.fault.ResourceInUse):
   deviceIds: list[pyVmomi.sms.storage.replication.DeviceId] = []


class ServiceNotInitialized(pyVmomi.vmodl.RuntimeFault):
   pass


class SmsFault(pyVmomi.vmodl.MethodFault):
   pass

class SyncInProgress(ProviderSyncFailed):
   pass


class TooMany(pyVmomi.vmodl.MethodFault):
   maxBatchSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
