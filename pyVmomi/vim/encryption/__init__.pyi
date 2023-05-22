from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType


class CryptoManager(ManagedObject):
    @property
    def enabled(self) -> bool: ...
    def AddKey(self, key: CryptoKeyPlain) -> NoneType: ...
    def AddKeys(self, keys: List[CryptoKeyPlain]) -> List[CryptoKeyResult]: ...
    def RemoveKey(self, key: CryptoKeyId, force: bool) -> NoneType: ...
    def RemoveKeys(self, keys: List[CryptoKeyId], force: bool) -> List[CryptoKeyResult]: ...
    def ListKeys(self, limit: int) -> List[CryptoKeyId]: ...


class CryptoManagerHost(CryptoManager):
    def Prepare(self) -> NoneType: ...
    def Enable(self, initialKey: CryptoKeyPlain) -> NoneType: ...
    def ChangeKey(self, newKey: CryptoKeyPlain) -> vim.Task: ...
    def Disable(self) -> NoneType: ...
    def GetCryptoKeyStatus(self, keys: List[CryptoKeyId]) -> List[CryptoManagerHost.KeyStatus]: ...


    class KeyStatus(vmodl.DynamicData):
        @property
        def keyId(self) -> CryptoKeyId: ...
        @keyId.setter
        def keyId(self, value: CryptoKeyId):
            self._keyId = value
        @property
        def present(self) -> bool: ...
        @present.setter
        def present(self, value: bool):
            self._present = value
        @property
        def managementType(self) -> str: ...
        @managementType.setter
        def managementType(self, value: str):
            self._managementType = value


    class KeyManagementType(Enum):
        unknown = "unknown"
        internal = "internal"
        external = "external"


class CryptoManagerHostKMS(CryptoManagerHost): ...


class CryptoManagerKmip(CryptoManager):
    @property
    def kmipServers(self) -> List[KmipClusterInfo]: ...
    def RegisterKmipServer(self, server: KmipServerSpec) -> NoneType: ...
    def MarkDefault(self, clusterId: KeyProviderId) -> NoneType: ...
    def UpdateKmipServer(self, server: KmipServerSpec) -> NoneType: ...
    def RemoveKmipServer(self, clusterId: KeyProviderId, serverName: str) -> NoneType: ...
    def ListKmipServers(self, limit: int) -> List[KmipClusterInfo]: ...
    def RetrieveKmipServersStatus(self, clusters: List[KmipClusterInfo]) -> vim.Task: ...
    def GenerateKey(self, keyProvider: KeyProviderId, spec: CryptoManagerKmip.CustomAttributeSpec) -> CryptoKeyResult: ...
    def RetrieveKmipServerCert(self, keyProvider: KeyProviderId, server: KmipServerInfo) -> CryptoManagerKmip.ServerCertInfo: ...
    def UploadKmipServerCert(self, cluster: KeyProviderId, certificate: str) -> NoneType: ...
    def GenerateSelfSignedClientCert(self, cluster: KeyProviderId, request: CryptoManagerKmip.CertSignRequest) -> str: ...
    def GenerateClientCsr(self, cluster: KeyProviderId, request: CryptoManagerKmip.CertSignRequest) -> str: ...
    def RetrieveSelfSignedClientCert(self, cluster: KeyProviderId) -> str: ...
    def RetrieveClientCsr(self, cluster: KeyProviderId) -> str: ...
    def RetrieveClientCert(self, cluster: KeyProviderId) -> str: ...
    def UpdateSelfSignedClientCert(self, cluster: KeyProviderId, certificate: str) -> NoneType: ...
    def UpdateKmsSignedCsrClientCert(self, cluster: KeyProviderId, certificate: str) -> NoneType: ...
    def UploadClientCert(self, cluster: KeyProviderId, certificate: str, privateKey: str) -> NoneType: ...
    def IsKmsClusterActive(self, cluster: KeyProviderId) -> bool: ...
    def SetDefaultKmsCluster(self, entity: vim.ManagedEntity, clusterId: KeyProviderId) -> NoneType: ...
    def GetDefaultKmsCluster(self, entity: vim.ManagedEntity, defaultsToParent: bool) -> KeyProviderId: ...
    def QueryCryptoKeyStatus(self, keyIds: List[CryptoKeyId], checkKeyBitMap: int) -> List[CryptoManagerKmip.CryptoKeyStatus]: ...
    def RegisterKmsCluster(self, clusterId: KeyProviderId, managementType: str) -> NoneType: ...
    def UnregisterKmsCluster(self, clusterId: KeyProviderId) -> NoneType: ...
    def ListKmsClusters(self, includeKmsServers: bool, managementTypeFilter: int, statusFilter: int) -> List[KmipClusterInfo]: ...
    def SetKeyCustomAttributes(self, keyId: CryptoKeyId, spec: CryptoManagerKmip.CustomAttributeSpec) -> CryptoKeyResult: ...


    class CertSignRequest(vmodl.DynamicData):
        @property
        def commonName(self) -> str: ...
        @commonName.setter
        def commonName(self, value: str):
            self._commonName = value
        @property
        def organization(self) -> str: ...
        @organization.setter
        def organization(self, value: str):
            self._organization = value
        @property
        def organizationUnit(self) -> str: ...
        @organizationUnit.setter
        def organizationUnit(self, value: str):
            self._organizationUnit = value
        @property
        def locality(self) -> str: ...
        @locality.setter
        def locality(self, value: str):
            self._locality = value
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value
        @property
        def country(self) -> str: ...
        @country.setter
        def country(self, value: str):
            self._country = value
        @property
        def email(self) -> str: ...
        @email.setter
        def email(self, value: str):
            self._email = value


    class CertificateInfo(vmodl.DynamicData):
        @property
        def subject(self) -> str: ...
        @subject.setter
        def subject(self, value: str):
            self._subject = value
        @property
        def issuer(self) -> str: ...
        @issuer.setter
        def issuer(self, value: str):
            self._issuer = value
        @property
        def serialNumber(self) -> str: ...
        @serialNumber.setter
        def serialNumber(self, value: str):
            self._serialNumber = value
        @property
        def notBefore(self) -> datetime: ...
        @notBefore.setter
        def notBefore(self, value: datetime):
            self._notBefore = value
        @property
        def notAfter(self) -> datetime: ...
        @notAfter.setter
        def notAfter(self, value: datetime):
            self._notAfter = value
        @property
        def fingerprint(self) -> str: ...
        @fingerprint.setter
        def fingerprint(self, value: str):
            self._fingerprint = value
        @property
        def checkTime(self) -> datetime: ...
        @checkTime.setter
        def checkTime(self, value: datetime):
            self._checkTime = value
        @property
        def secondsSinceValid(self) -> int: ...
        @secondsSinceValid.setter
        def secondsSinceValid(self, value: int):
            self._secondsSinceValid = value
        @property
        def secondsBeforeExpire(self) -> int: ...
        @secondsBeforeExpire.setter
        def secondsBeforeExpire(self, value: int):
            self._secondsBeforeExpire = value


    class ClusterStatus(vmodl.DynamicData):
        @property
        def clusterId(self) -> KeyProviderId: ...
        @clusterId.setter
        def clusterId(self, value: KeyProviderId):
            self._clusterId = value
        @property
        def overallStatus(self) -> vim.ManagedEntity.Status: ...
        @overallStatus.setter
        def overallStatus(self, value: vim.ManagedEntity.Status):
            self._overallStatus = value
        @property
        def managementType(self) -> str: ...
        @managementType.setter
        def managementType(self, value: str):
            self._managementType = value
        @property
        def servers(self) -> List[CryptoManagerKmip.ServerStatus]: ...
        @servers.setter
        def servers(self, value: List[CryptoManagerKmip.ServerStatus]):
            self._servers = value
        @property
        def clientCertInfo(self) -> CryptoManagerKmip.CertificateInfo: ...
        @clientCertInfo.setter
        def clientCertInfo(self, value: CryptoManagerKmip.CertificateInfo):
            self._clientCertInfo = value


    class CryptoKeyStatus(vmodl.DynamicData):
        @property
        def keyId(self) -> CryptoKeyId: ...
        @keyId.setter
        def keyId(self, value: CryptoKeyId):
            self._keyId = value
        @property
        def keyAvailable(self) -> bool: ...
        @keyAvailable.setter
        def keyAvailable(self, value: bool):
            self._keyAvailable = value
        @property
        def reason(self) -> str: ...
        @reason.setter
        def reason(self, value: str):
            self._reason = value
        @property
        def encryptedVMs(self) -> List[vim.VirtualMachine]: ...
        @encryptedVMs.setter
        def encryptedVMs(self, value: List[vim.VirtualMachine]):
            self._encryptedVMs = value
        @property
        def affectedHosts(self) -> List[vim.HostSystem]: ...
        @affectedHosts.setter
        def affectedHosts(self, value: List[vim.HostSystem]):
            self._affectedHosts = value
        @property
        def referencedByTags(self) -> List[str]: ...
        @referencedByTags.setter
        def referencedByTags(self, value: List[str]):
            self._referencedByTags = value


        class KeyUnavailableReason(Enum):
            KeyStateMissingInCache = "KeyStateMissingInCache"
            KeyStateClusterInvalid = "KeyStateClusterInvalid"
            KeyStateClusterUnreachable = "KeyStateClusterUnreachable"
            KeyStateMissingInKMS = "KeyStateMissingInKMS"
            KeyStateNotActiveOrEnabled = "KeyStateNotActiveOrEnabled"
            KeyStateManagedByTrustAuthority = "KeyStateManagedByTrustAuthority"
            KeyStateManagedByNKP = "KeyStateManagedByNKP"


    class CustomAttributeSpec(vmodl.DynamicData):
        @property
        def attributes(self) -> List[vim.KeyValue]: ...
        @attributes.setter
        def attributes(self, value: List[vim.KeyValue]):
            self._attributes = value


    class ServerCertInfo(vmodl.DynamicData):
        @property
        def certificate(self) -> str: ...
        @certificate.setter
        def certificate(self, value: str):
            self._certificate = value
        @property
        def certInfo(self) -> CryptoManagerKmip.CertificateInfo: ...
        @certInfo.setter
        def certInfo(self, value: CryptoManagerKmip.CertificateInfo):
            self._certInfo = value
        @property
        def clientTrustServer(self) -> bool: ...
        @clientTrustServer.setter
        def clientTrustServer(self, value: bool):
            self._clientTrustServer = value


    class ServerStatus(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def status(self) -> vim.ManagedEntity.Status: ...
        @status.setter
        def status(self, value: vim.ManagedEntity.Status):
            self._status = value
        @property
        def connectionStatus(self) -> str: ...
        @connectionStatus.setter
        def connectionStatus(self, value: str):
            self._connectionStatus = value
        @property
        def certInfo(self) -> CryptoManagerKmip.CertificateInfo: ...
        @certInfo.setter
        def certInfo(self, value: CryptoManagerKmip.CertificateInfo):
            self._certInfo = value
        @property
        def clientTrustServer(self) -> bool: ...
        @clientTrustServer.setter
        def clientTrustServer(self, value: bool):
            self._clientTrustServer = value
        @property
        def serverTrustClient(self) -> bool: ...
        @serverTrustClient.setter
        def serverTrustClient(self, value: bool):
            self._serverTrustClient = value


class CryptoKeyId(vmodl.DynamicData):
    @property
    def keyId(self) -> str: ...
    @keyId.setter
    def keyId(self, value: str):
        self._keyId = value
    @property
    def providerId(self) -> KeyProviderId: ...
    @providerId.setter
    def providerId(self, value: KeyProviderId):
        self._providerId = value


class CryptoKeyPlain(vmodl.DynamicData):
    @property
    def keyId(self) -> CryptoKeyId: ...
    @keyId.setter
    def keyId(self, value: CryptoKeyId):
        self._keyId = value
    @property
    def algorithm(self) -> str: ...
    @algorithm.setter
    def algorithm(self, value: str):
        self._algorithm = value
    @property
    def keyData(self) -> str: ...
    @keyData.setter
    def keyData(self, value: str):
        self._keyData = value


class CryptoKeyResult(vmodl.DynamicData):
    @property
    def keyId(self) -> CryptoKeyId: ...
    @keyId.setter
    def keyId(self, value: CryptoKeyId):
        self._keyId = value
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool):
        self._success = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class CryptoSpec(vmodl.DynamicData): ...


class CryptoSpecDecrypt(CryptoSpec): ...


class CryptoSpecDeepRecrypt(CryptoSpec):
    @property
    def newKeyId(self) -> CryptoKeyId: ...
    @newKeyId.setter
    def newKeyId(self, value: CryptoKeyId):
        self._newKeyId = value


class CryptoSpecEncrypt(CryptoSpec):
    @property
    def cryptoKeyId(self) -> CryptoKeyId: ...
    @cryptoKeyId.setter
    def cryptoKeyId(self, value: CryptoKeyId):
        self._cryptoKeyId = value


class CryptoSpecNoOp(CryptoSpec): ...


class CryptoSpecRegister(CryptoSpecNoOp):
    @property
    def cryptoKeyId(self) -> CryptoKeyId: ...
    @cryptoKeyId.setter
    def cryptoKeyId(self, value: CryptoKeyId):
        self._cryptoKeyId = value


class CryptoSpecShallowRecrypt(CryptoSpec):
    @property
    def newKeyId(self) -> CryptoKeyId: ...
    @newKeyId.setter
    def newKeyId(self, value: CryptoKeyId):
        self._newKeyId = value


class KeyProviderId(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value


class KmipClusterInfo(vmodl.DynamicData):
    @property
    def clusterId(self) -> KeyProviderId: ...
    @clusterId.setter
    def clusterId(self, value: KeyProviderId):
        self._clusterId = value
    @property
    def servers(self) -> List[KmipServerInfo]: ...
    @servers.setter
    def servers(self, value: List[KmipServerInfo]):
        self._servers = value
    @property
    def useAsDefault(self) -> bool: ...
    @useAsDefault.setter
    def useAsDefault(self, value: bool):
        self._useAsDefault = value
    @property
    def managementType(self) -> str: ...
    @managementType.setter
    def managementType(self, value: str):
        self._managementType = value
    @property
    def useAsEntityDefault(self) -> List[vim.ManagedEntity]: ...
    @useAsEntityDefault.setter
    def useAsEntityDefault(self, value: List[vim.ManagedEntity]):
        self._useAsEntityDefault = value
    @property
    def hasBackup(self) -> bool: ...
    @hasBackup.setter
    def hasBackup(self, value: bool):
        self._hasBackup = value
    @property
    def tpmRequired(self) -> bool: ...
    @tpmRequired.setter
    def tpmRequired(self, value: bool):
        self._tpmRequired = value
    @property
    def keyId(self) -> str: ...
    @keyId.setter
    def keyId(self, value: str):
        self._keyId = value


    class KmsManagementType(Enum):
        unknown = "unknown"
        vCenter = "vCenter"
        trustAuthority = "trustAuthority"
        nativeProvider = "nativeProvider"


class KmipServerInfo(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def address(self) -> str: ...
    @address.setter
    def address(self, value: str):
        self._address = value
    @property
    def port(self) -> int: ...
    @port.setter
    def port(self, value: int):
        self._port = value
    @property
    def proxyAddress(self) -> str: ...
    @proxyAddress.setter
    def proxyAddress(self, value: str):
        self._proxyAddress = value
    @property
    def proxyPort(self) -> int: ...
    @proxyPort.setter
    def proxyPort(self, value: int):
        self._proxyPort = value
    @property
    def reconnect(self) -> int: ...
    @reconnect.setter
    def reconnect(self, value: int):
        self._reconnect = value
    @property
    def protocol(self) -> str: ...
    @protocol.setter
    def protocol(self, value: str):
        self._protocol = value
    @property
    def nbio(self) -> int: ...
    @nbio.setter
    def nbio(self, value: int):
        self._nbio = value
    @property
    def timeout(self) -> int: ...
    @timeout.setter
    def timeout(self, value: int):
        self._timeout = value
    @property
    def userName(self) -> str: ...
    @userName.setter
    def userName(self, value: str):
        self._userName = value


class KmipServerSpec(vmodl.DynamicData):
    @property
    def clusterId(self) -> KeyProviderId: ...
    @clusterId.setter
    def clusterId(self, value: KeyProviderId):
        self._clusterId = value
    @property
    def info(self) -> KmipServerInfo: ...
    @info.setter
    def info(self, value: KmipServerInfo):
        self._info = value
    @property
    def password(self) -> str: ...
    @password.setter
    def password(self, value: str):
        self._password = value


class KmipServerStatus(vmodl.DynamicData):
    @property
    def clusterId(self) -> KeyProviderId: ...
    @clusterId.setter
    def clusterId(self, value: KeyProviderId):
        self._clusterId = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def status(self) -> vim.ManagedEntity.Status: ...
    @status.setter
    def status(self, value: vim.ManagedEntity.Status):
        self._status = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value