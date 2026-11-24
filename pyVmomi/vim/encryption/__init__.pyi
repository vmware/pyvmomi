# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl



class CryptoKeyId(pyVmomi.vmodl.DynamicData):
   keyId: str
   providerId: _typing.Optional[KeyProviderId] = None


class CryptoKeyPlain(pyVmomi.vmodl.DynamicData):
   keyId: CryptoKeyId
   algorithm: str
   keyData: str


class CryptoKeyResult(pyVmomi.vmodl.DynamicData):
   keyId: CryptoKeyId
   success: bool
   reason: _typing.Optional[str] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class CryptoManager(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def enabled(self) -> bool: ...

   def AddKey(self, key: CryptoKeyPlain) -> None: ...
   def AddKeys(self, keys: list[CryptoKeyPlain]) -> list[CryptoKeyResult]: ...
   def RemoveKey(self, key: CryptoKeyId, force: bool) -> None: ...
   def RemoveKeys(self, keys: list[CryptoKeyId], force: bool) -> list[CryptoKeyResult]: ...
   def ListKeys(self, limit: _typing.Optional[int]) -> list[CryptoKeyId]: ...


class CryptoManagerHost(CryptoManager):
   class KeyManagementType(pyVmomi.VmomiSupport.Enum):
      unknown: _typing.ClassVar['KeyManagementType'] = 'unknown'
      internal: _typing.ClassVar['KeyManagementType'] = 'internal'
      external: _typing.ClassVar['KeyManagementType'] = 'external'

   class KeyStatus(pyVmomi.vmodl.DynamicData):
      keyId: CryptoKeyId
      present: bool
      managementType: _typing.Optional[str] = None
      accessGranted: _typing.Optional[bool] = None

   def Prepare(self) -> None: ...
   def Enable(self, initialKey: CryptoKeyPlain) -> None: ...
   def ChangeKey(self, newKey: CryptoKeyPlain) -> pyVmomi.vim.Task: ...
   def Disable(self) -> None: ...
   def GetCryptoKeyStatus(self, keys: list[CryptoKeyId]) -> list[KeyStatus]: ...

class CryptoManagerHostKMS(CryptoManagerHost):
   pass


class CryptoManagerKmip(CryptoManager):
   class CertificateInfo(pyVmomi.vmodl.DynamicData):
      subject: str
      issuer: str
      serialNumber: str
      notBefore: _datetime.datetime
      notAfter: _datetime.datetime
      fingerprint: str
      checkTime: _datetime.datetime
      secondsSinceValid: _typing.Optional[int] = None
      secondsBeforeExpire: _typing.Optional[int] = None

   class ServerStatus(pyVmomi.vmodl.DynamicData):
      name: str
      status: pyVmomi.vim.ManagedEntity.Status
      connectionStatus: str
      certInfo: _typing.Optional[CertificateInfo] = None
      clientTrustServer: _typing.Optional[bool] = None
      serverTrustClient: _typing.Optional[bool] = None

   class ClusterStatus(pyVmomi.vmodl.DynamicData):
      clusterId: KeyProviderId
      overallStatus: _typing.Optional[pyVmomi.vim.ManagedEntity.Status] = None
      managementType: _typing.Optional[str] = None
      servers: list[ServerStatus] = []
      clientCertInfo: _typing.Optional[CertificateInfo] = None

   class GenerateKeySpec(pyVmomi.vmodl.DynamicData):
      keyType: _typing.Optional[str] = None

   class ServerCertInfo(pyVmomi.vmodl.DynamicData):
      certificate: str
      certInfo: _typing.Optional[CertificateInfo] = None
      clientTrustServer: _typing.Optional[bool] = None

   class CertSignRequest(pyVmomi.vmodl.DynamicData):
      commonName: _typing.Optional[str] = None
      organization: _typing.Optional[str] = None
      organizationUnit: _typing.Optional[str] = None
      locality: _typing.Optional[str] = None
      state: _typing.Optional[str] = None
      country: _typing.Optional[str] = None
      email: _typing.Optional[str] = None

   class CryptoKeyStatus(pyVmomi.vmodl.DynamicData):
      class KeyUnavailableReason(pyVmomi.VmomiSupport.Enum):
         KeyStateMissingInCache: _typing.ClassVar['KeyUnavailableReason'] = 'KeyStateMissingInCache'
         KeyStateClusterInvalid: _typing.ClassVar['KeyUnavailableReason'] = 'KeyStateClusterInvalid'
         KeyStateClusterUnreachable: _typing.ClassVar['KeyUnavailableReason'] = 'KeyStateClusterUnreachable'
         KeyStateMissingInKMS: _typing.ClassVar['KeyUnavailableReason'] = 'KeyStateMissingInKMS'
         KeyStateNotActiveOrEnabled: _typing.ClassVar['KeyUnavailableReason'] = 'KeyStateNotActiveOrEnabled'
         KeyStateManagedByTrustAuthority: _typing.ClassVar['KeyUnavailableReason'] = 'KeyStateManagedByTrustAuthority'
         KeyStateManagedByNKP: _typing.ClassVar['KeyUnavailableReason'] = 'KeyStateManagedByNKP'
         NoPermissionToAccessKeyProvider: _typing.ClassVar['KeyUnavailableReason'] = 'NoPermissionToAccessKeyProvider'
         WrappingKeyMissingInKMS: _typing.ClassVar['KeyUnavailableReason'] = 'WrappingKeyMissingInKMS'
         WrappingKeyNotActiveOrEnabled: _typing.ClassVar['KeyUnavailableReason'] = 'WrappingKeyNotActiveOrEnabled'

      class KeyInfo(pyVmomi.vmodl.DynamicData):
         keyId: str

      class WrappingKeyIdKeyInfo(CryptoKeyStatus.KeyInfo):
         configuredTime: _typing.Optional[_datetime.datetime] = None

      class WrappingRotationIntervalKeyInfo(CryptoKeyStatus.KeyInfo):
         createTime: _typing.Optional[_datetime.datetime] = None
         rotateTime: _typing.Optional[_datetime.datetime] = None

      keyId: CryptoKeyId
      keyAvailable: _typing.Optional[bool] = None
      reason: _typing.Optional[str] = None
      keyInfo: _typing.Optional[KeyInfo] = None
      encryptedVMs: list[pyVmomi.vim.VirtualMachine] = []
      affectedHosts: list[pyVmomi.vim.HostSystem] = []
      referencedByTags: list[str] = []

   class CustomAttributeSpec(pyVmomi.vmodl.DynamicData):
      attributes: list[pyVmomi.vim.KeyValue] = []

   @property
   def kmipServers(self) -> list[KmipClusterInfo]: ...

   def RegisterKmipServer(self, server: KmipServerSpec) -> None: ...
   def MarkDefault(self, clusterId: KeyProviderId) -> None: ...
   def UpdateKmipServer(self, server: KmipServerSpec) -> None: ...
   def RemoveKmipServer(self, clusterId: KeyProviderId, serverName: str) -> None: ...
   def ListKmipServers(self, limit: _typing.Optional[int]) -> list[KmipClusterInfo]: ...
   def RetrieveKmipServersStatus(self, clusters: list[KmipClusterInfo]) -> pyVmomi.vim.Task: ...
   def GenerateKey(self, keyProvider: _typing.Optional[KeyProviderId], spec: _typing.Optional[CustomAttributeSpec], keySpec: _typing.Optional[GenerateKeySpec]) -> CryptoKeyResult: ...
   def RetrieveKmipServerCert(self, keyProvider: KeyProviderId, server: KmipServerInfo) -> ServerCertInfo: ...
   def UploadKmipServerCert(self, cluster: KeyProviderId, certificate: str) -> None: ...
   def GenerateSelfSignedClientCert(self, cluster: KeyProviderId, request: _typing.Optional[CertSignRequest]) -> str: ...
   def GenerateClientCsr(self, cluster: KeyProviderId, request: _typing.Optional[CertSignRequest]) -> str: ...
   def RetrieveSelfSignedClientCert(self, cluster: KeyProviderId) -> str: ...
   def RetrieveClientCsr(self, cluster: KeyProviderId) -> str: ...
   def RetrieveClientCert(self, cluster: KeyProviderId) -> str: ...
   def UpdateSelfSignedClientCert(self, cluster: KeyProviderId, certificate: str) -> None: ...
   def UpdateKmsSignedCsrClientCert(self, cluster: KeyProviderId, certificate: str) -> None: ...
   def UploadClientCert(self, cluster: KeyProviderId, certificate: str, privateKey: str) -> None: ...
   def IsKmsClusterActive(self, cluster: _typing.Optional[KeyProviderId]) -> bool: ...
   def SetDefaultKmsCluster(self, entity: _typing.Optional[pyVmomi.vim.ManagedEntity], clusterId: _typing.Optional[KeyProviderId]) -> None: ...
   def GetDefaultKmsCluster(self, entity: _typing.Optional[pyVmomi.vim.ManagedEntity], defaultsToParent: _typing.Optional[bool]) -> _typing.Optional[KeyProviderId]: ...
   def QueryCryptoKeyStatus(self, keyIds: list[CryptoKeyId], checkKeyBitMap: int) -> list[CryptoKeyStatus]: ...
   def RegisterKmsCluster(self, clusterId: KeyProviderId, managementType: _typing.Optional[str]) -> None: ...
   def UnregisterKmsCluster(self, clusterId: KeyProviderId) -> None: ...
   def ListKmsClusters(self, includeKmsServers: _typing.Optional[bool], managementTypeFilter: _typing.Optional[int], statusFilter: _typing.Optional[int]) -> list[KmipClusterInfo]: ...
   def SetKeyCustomAttributes(self, keyId: CryptoKeyId, spec: CustomAttributeSpec) -> CryptoKeyResult: ...


class CryptoSpec(pyVmomi.vmodl.DynamicData):
   pass

class CryptoSpecDecrypt(CryptoSpec):
   pass

class CryptoSpecDeepRecrypt(CryptoSpec):
   newKeyId: CryptoKeyId

class CryptoSpecEncrypt(CryptoSpec):
   cryptoKeyId: CryptoKeyId

class CryptoSpecNoOp(CryptoSpec):
   pass

class CryptoSpecRegister(CryptoSpecNoOp):
   cryptoKeyId: CryptoKeyId

class CryptoSpecShallowRecrypt(CryptoSpec):
   newKeyId: CryptoKeyId


class KeyProviderId(pyVmomi.vmodl.DynamicData):
   id: str


class KmipClusterInfo(pyVmomi.vmodl.DynamicData):
   class KmsManagementType(pyVmomi.VmomiSupport.Enum):
      unknown: _typing.ClassVar['KmsManagementType'] = 'unknown'
      vCenter: _typing.ClassVar['KmsManagementType'] = 'vCenter'
      trustAuthority: _typing.ClassVar['KmsManagementType'] = 'trustAuthority'
      nativeProvider: _typing.ClassVar['KmsManagementType'] = 'nativeProvider'

   class KeyType(pyVmomi.VmomiSupport.Enum):
      rawKey: _typing.ClassVar['KeyType'] = 'rawKey'
      wrappedKey: _typing.ClassVar['KeyType'] = 'wrappedKey'

   class KeyInfo(pyVmomi.vmodl.DynamicData):
      pass

   class WrappingKeyIdKeyInfo(KeyInfo):
      keyId: str
      configuredTime: _datetime.datetime

   class WrappingRotationIntervalKeyInfo(KeyInfo):
      keyId: _typing.Optional[str] = None
      rotationInterval: _typing.Optional[int] = None
      lastRotation: _typing.Optional[_datetime.datetime] = None

   clusterId: KeyProviderId
   servers: list[KmipServerInfo] = []
   useAsDefault: bool
   managementType: _typing.Optional[str] = None
   useAsEntityDefault: list[pyVmomi.vim.ManagedEntity] = []
   hasBackup: _typing.Optional[bool] = None
   tpmRequired: _typing.Optional[bool] = None
   keyId: _typing.Optional[str] = None
   defaultKeyType: _typing.Optional[str] = None
   keyInfo: _typing.Optional[KeyInfo] = None


class KmipServerInfo(pyVmomi.vmodl.DynamicData):
   name: str
   address: str
   port: int
   proxyAddress: _typing.Optional[str] = None
   proxyPort: _typing.Optional[int] = None
   reconnect: _typing.Optional[int] = None
   protocol: _typing.Optional[str] = None
   nbio: _typing.Optional[int] = None
   timeout: _typing.Optional[int] = None
   userName: _typing.Optional[str] = None


class KmipServerSpec(pyVmomi.vmodl.DynamicData):
   class KeySpec(pyVmomi.vmodl.DynamicData):
      pass

   class WrappingKeyIdKeySpec(KeySpec):
      keyId: str

   class WrappingRotationIntervalKeySpec(KeySpec):
      rotationInterval: _typing.Optional[int] = None

   clusterId: KeyProviderId
   info: KmipServerInfo
   password: _typing.Optional[str] = None
   defaultKeyType: _typing.Optional[str] = None
   keySpec: _typing.Optional[KeySpec] = None


class KmipServerStatus(pyVmomi.vmodl.DynamicData):
   clusterId: KeyProviderId
   name: str
   status: pyVmomi.vim.ManagedEntity.Status
   description: str
