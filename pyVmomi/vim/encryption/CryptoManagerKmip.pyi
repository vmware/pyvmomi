# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.KeyValue import KeyValue

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.Task import Task

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.encryption.CryptoKeyId import CryptoKeyId

from pyVmomi.vim.encryption.CryptoKeyResult import CryptoKeyResult

from pyVmomi.vim.encryption.CryptoManager import CryptoManager

from pyVmomi.vim.encryption.KeyProviderId import KeyProviderId

from pyVmomi.vim.encryption.KmipClusterInfo import KmipClusterInfo

from pyVmomi.vim.encryption.KmipServerInfo import KmipServerInfo

from pyVmomi.vim.encryption.KmipServerSpec import KmipServerSpec

class CryptoManagerKmip(CryptoManager):
   class CertificateInfo(DynamicData):
      subject: str
      issuer: str
      serialNumber: str
      notBefore: datetime
      notAfter: datetime
      fingerprint: str
      checkTime: datetime
      secondsSinceValid: Optional[int] = None
      secondsBeforeExpire: Optional[int] = None

   class ServerStatus(DynamicData):
      name: str
      status: ManagedEntity.Status
      connectionStatus: str
      certInfo: Optional[CertificateInfo] = None
      clientTrustServer: Optional[bool] = None
      serverTrustClient: Optional[bool] = None

   class ClusterStatus(DynamicData):
      clusterId: KeyProviderId
      overallStatus: Optional[ManagedEntity.Status] = None
      managementType: Optional[str] = None
      servers: list[ServerStatus] = []
      clientCertInfo: Optional[CertificateInfo] = None

   class GenerateKeySpec(DynamicData):
      keyType: Optional[str] = None

   class ServerCertInfo(DynamicData):
      certificate: str
      certInfo: Optional[CertificateInfo] = None
      clientTrustServer: Optional[bool] = None

   class CertSignRequest(DynamicData):
      commonName: Optional[str] = None
      organization: Optional[str] = None
      organizationUnit: Optional[str] = None
      locality: Optional[str] = None
      state: Optional[str] = None
      country: Optional[str] = None
      email: Optional[str] = None

   class CryptoKeyStatus(DynamicData):
      class KeyUnavailableReason(Enum):
         KeyStateMissingInCache: ClassVar['KeyUnavailableReason'] = 'KeyStateMissingInCache'
         KeyStateClusterInvalid: ClassVar['KeyUnavailableReason'] = 'KeyStateClusterInvalid'
         KeyStateClusterUnreachable: ClassVar['KeyUnavailableReason'] = 'KeyStateClusterUnreachable'
         KeyStateMissingInKMS: ClassVar['KeyUnavailableReason'] = 'KeyStateMissingInKMS'
         KeyStateNotActiveOrEnabled: ClassVar['KeyUnavailableReason'] = 'KeyStateNotActiveOrEnabled'
         KeyStateManagedByTrustAuthority: ClassVar['KeyUnavailableReason'] = 'KeyStateManagedByTrustAuthority'
         KeyStateManagedByNKP: ClassVar['KeyUnavailableReason'] = 'KeyStateManagedByNKP'
         NoPermissionToAccessKeyProvider: ClassVar['KeyUnavailableReason'] = 'NoPermissionToAccessKeyProvider'
         WrappingKeyMissingInKMS: ClassVar['KeyUnavailableReason'] = 'WrappingKeyMissingInKMS'
         WrappingKeyNotActiveOrEnabled: ClassVar['KeyUnavailableReason'] = 'WrappingKeyNotActiveOrEnabled'

      class KeyInfo(DynamicData):
         keyId: str

      class WrappingKeyIdKeyInfo(CryptoKeyStatus.KeyInfo):
         configuredTime: Optional[datetime] = None

      class WrappingRotationIntervalKeyInfo(CryptoKeyStatus.KeyInfo):
         createTime: Optional[datetime] = None
         rotateTime: Optional[datetime] = None

      keyId: CryptoKeyId
      keyAvailable: Optional[bool] = None
      reason: Optional[str] = None
      keyInfo: Optional[KeyInfo] = None
      encryptedVMs: list[VirtualMachine] = []
      affectedHosts: list[HostSystem] = []
      referencedByTags: list[str] = []

   class CustomAttributeSpec(DynamicData):
      attributes: list[KeyValue] = []

   @property
   def kmipServers(self) -> list[KmipClusterInfo]: ...

   def RegisterKmipServer(self, server: KmipServerSpec) -> None: ...
   def MarkDefault(self, clusterId: KeyProviderId) -> None: ...
   def UpdateKmipServer(self, server: KmipServerSpec) -> None: ...
   def RemoveKmipServer(self, clusterId: KeyProviderId, serverName: str) -> None: ...
   def ListKmipServers(self, limit: Optional[int]) -> list[KmipClusterInfo]: ...
   def RetrieveKmipServersStatus(self, clusters: list[KmipClusterInfo]) -> Task: ...
   def GenerateKey(self, keyProvider: Optional[KeyProviderId], spec: Optional[CustomAttributeSpec], keySpec: Optional[GenerateKeySpec]) -> CryptoKeyResult: ...
   def RetrieveKmipServerCert(self, keyProvider: KeyProviderId, server: KmipServerInfo) -> ServerCertInfo: ...
   def UploadKmipServerCert(self, cluster: KeyProviderId, certificate: str) -> None: ...
   def GenerateSelfSignedClientCert(self, cluster: KeyProviderId, request: Optional[CertSignRequest]) -> str: ...
   def GenerateClientCsr(self, cluster: KeyProviderId, request: Optional[CertSignRequest]) -> str: ...
   def RetrieveSelfSignedClientCert(self, cluster: KeyProviderId) -> str: ...
   def RetrieveClientCsr(self, cluster: KeyProviderId) -> str: ...
   def RetrieveClientCert(self, cluster: KeyProviderId) -> str: ...
   def UpdateSelfSignedClientCert(self, cluster: KeyProviderId, certificate: str) -> None: ...
   def UpdateKmsSignedCsrClientCert(self, cluster: KeyProviderId, certificate: str) -> None: ...
   def UploadClientCert(self, cluster: KeyProviderId, certificate: str, privateKey: str) -> None: ...
   def IsKmsClusterActive(self, cluster: Optional[KeyProviderId]) -> bool: ...
   def SetDefaultKmsCluster(self, entity: Optional[ManagedEntity], clusterId: Optional[KeyProviderId]) -> None: ...
   def GetDefaultKmsCluster(self, entity: Optional[ManagedEntity], defaultsToParent: Optional[bool]) -> Optional[KeyProviderId]: ...
   def QueryCryptoKeyStatus(self, keyIds: list[CryptoKeyId], checkKeyBitMap: int) -> list[CryptoKeyStatus]: ...
   def RegisterKmsCluster(self, clusterId: KeyProviderId, managementType: Optional[str]) -> None: ...
   def UnregisterKmsCluster(self, clusterId: KeyProviderId) -> None: ...
   def ListKmsClusters(self, includeKmsServers: Optional[bool], managementTypeFilter: Optional[int], statusFilter: Optional[int]) -> list[KmipClusterInfo]: ...
   def SetKeyCustomAttributes(self, keyId: CryptoKeyId, spec: CustomAttributeSpec) -> CryptoKeyResult: ...
