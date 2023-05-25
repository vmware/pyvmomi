from typing import List, Literal
from enum import Enum
from pyVmomi import ClusterStatus, DecommissionMode, DiskMapping, DiskResult, VsanDiskInfo, VsanRuntimeInfo, vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import Link, ManagedObject, NoneType, binary, byte, long, short


class ActiveDirectoryAuthentication(DirectoryStore):
    def JoinDomain(self, domainName: str, userName: str, password: str) -> vim.Task: ...
    def JoinDomainWithCAM(self, domainName: str, camServer: str) -> vim.Task: ...
    def ImportCertificateForCAM(self, certPath: str, camServer: str) -> vim.Task: ...
    def LeaveCurrentDomain(self, force: bool) -> vim.Task: ...
    def EnableSmartCardAuthentication(self) -> NoneType: ...
    def InstallSmartCardTrustAnchor(self, cert: str) -> NoneType: ...
    def ReplaceSmartCardTrustAnchors(self, certs: List[str]) -> NoneType: ...
    def RemoveSmartCardTrustAnchor(self, issuer: str, serial: str) -> NoneType: ...
    def RemoveSmartCardTrustAnchorByFingerprint(self, fingerprint: str, digest: str) -> NoneType: ...
    def ListSmartCardTrustAnchors(self) -> List[str]: ...
    def DisableSmartCardAuthentication(self) -> NoneType: ...


    class CertificateDigest(Enum):
        SHA1 = "SHA1"


class AssignableHardwareManager(ManagedObject):
    @property
    def binding(self) -> List[AssignableHardwareBinding]: ...
    @property
    def config(self) -> AssignableHardwareConfig: ...
    def DownloadDescriptionTree(self) -> binary: ...
    def RetrieveDynamicPassthroughInfo(self) -> List[vim.vm.DynamicPassthroughInfo]: ...
    def RetrieveVendorDeviceGroupInfo(self) -> List[vim.vm.VendorDeviceGroupInfo]: ...
    def UpdateConfig(self, config: AssignableHardwareConfig) -> NoneType: ...


class AuthenticationManager(ManagedObject):
    @property
    def info(self) -> AuthenticationManagerInfo: ...
    @property
    def supportedStore(self) -> List[AuthenticationStore]: ...


class AuthenticationStore(ManagedObject):
    @property
    def info(self) -> AuthenticationStoreInfo: ...


class AutoStartManager(ManagedObject):
    @property
    def config(self) -> AutoStartManager.Config: ...
    def Reconfigure(self, spec: AutoStartManager.Config) -> NoneType: ...
    def AutoPowerOn(self) -> NoneType: ...
    def AutoPowerOff(self) -> NoneType: ...


    class AutoPowerInfo(vmodl.DynamicData):
        @property
        def key(self) -> vim.VirtualMachine: ...
        @key.setter
        def key(self, value: vim.VirtualMachine):
            self._key = value
        @property
        def startOrder(self) -> int: ...
        @startOrder.setter
        def startOrder(self, value: int):
            self._startOrder = value
        @property
        def startDelay(self) -> int: ...
        @startDelay.setter
        def startDelay(self, value: int):
            self._startDelay = value
        @property
        def waitForHeartbeat(self) -> AutoStartManager.AutoPowerInfo.WaitHeartbeatSetting | Literal['yes', 'no', 'systemDefault']: ...
        @waitForHeartbeat.setter
        def waitForHeartbeat(self, value: AutoStartManager.AutoPowerInfo.WaitHeartbeatSetting | Literal['yes', 'no', 'systemDefault']):
            self._waitForHeartbeat = value
        @property
        def startAction(self) -> str: ...
        @startAction.setter
        def startAction(self, value: str):
            self._startAction = value
        @property
        def stopDelay(self) -> int: ...
        @stopDelay.setter
        def stopDelay(self, value: int):
            self._stopDelay = value
        @property
        def stopAction(self) -> str: ...
        @stopAction.setter
        def stopAction(self, value: str):
            self._stopAction = value


        class WaitHeartbeatSetting(Enum):
            yes = "yes"
            no = "no"
            systemDefault = "systemDefault"


    class Config(vmodl.DynamicData):
        @property
        def defaults(self) -> AutoStartManager.SystemDefaults: ...
        @defaults.setter
        def defaults(self, value: AutoStartManager.SystemDefaults):
            self._defaults = value
        @property
        def powerInfo(self) -> List[AutoStartManager.AutoPowerInfo]: ...
        @powerInfo.setter
        def powerInfo(self, value: List[AutoStartManager.AutoPowerInfo]):
            self._powerInfo = value


    class SystemDefaults(vmodl.DynamicData):
        @property
        def enabled(self) -> bool: ...
        @enabled.setter
        def enabled(self, value: bool):
            self._enabled = value
        @property
        def startDelay(self) -> int: ...
        @startDelay.setter
        def startDelay(self, value: int):
            self._startDelay = value
        @property
        def stopDelay(self) -> int: ...
        @stopDelay.setter
        def stopDelay(self, value: int):
            self._stopDelay = value
        @property
        def waitForHeartbeat(self) -> bool: ...
        @waitForHeartbeat.setter
        def waitForHeartbeat(self, value: bool):
            self._waitForHeartbeat = value
        @property
        def stopAction(self) -> str: ...
        @stopAction.setter
        def stopAction(self, value: str):
            self._stopAction = value


    class Action(Enum):
        none = "none"
        systemDefault = "systemDefault"
        powerOn = "powerOn"
        powerOff = "powerOff"
        guestShutdown = "guestShutdown"
        suspend = "suspend"


class BootDeviceSystem(ManagedObject):
    def QueryBootDevices(self) -> BootDeviceInfo: ...
    def UpdateBootDevice(self, key: str) -> NoneType: ...


    class BootDevice(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value


class CacheConfigurationManager(ManagedObject):
    @property
    def cacheConfigurationInfo(self) -> List[CacheConfigurationManager.CacheConfigurationInfo]: ...
    def ConfigureCache(self, spec: CacheConfigurationManager.CacheConfigurationSpec) -> vim.Task: ...


    class CacheConfigurationInfo(vmodl.DynamicData):
        @property
        def key(self) -> vim.Datastore: ...
        @key.setter
        def key(self, value: vim.Datastore):
            self._key = value
        @property
        def swapSize(self) -> long: ...
        @swapSize.setter
        def swapSize(self, value: long):
            self._swapSize = value


    class CacheConfigurationSpec(vmodl.DynamicData):
        @property
        def datastore(self) -> vim.Datastore: ...
        @datastore.setter
        def datastore(self, value: vim.Datastore):
            self._datastore = value
        @property
        def swapSize(self) -> long: ...
        @swapSize.setter
        def swapSize(self, value: long):
            self._swapSize = value


class CertificateManager(ManagedObject):
    @property
    def certificateInfo(self) -> CertificateManager.CertificateInfo: ...
    def RetrieveCertificateInfoList(self) -> List[CertificateManager.CertificateInfo]: ...
    def GenerateCertificateSigningRequest(self, useIpAddressAsCommonName: bool, spec: CertificateManager.CertificateSpec) -> str: ...
    def GenerateCertificateSigningRequestByDn(self, distinguishedName: str, spec: CertificateManager.CertificateSpec) -> str: ...
    def InstallServerCertificate(self, cert: str) -> NoneType: ...
    def ReplaceCACertificatesAndCRLs(self, caCert: List[str], caCrl: List[str]) -> NoneType: ...
    def ListCACertificates(self) -> List[str]: ...
    def ListCACertificateRevocationLists(self) -> List[str]: ...


    class CertificateInfo(vmodl.DynamicData):
        @property
        def kind(self) -> str: ...
        @kind.setter
        def kind(self, value: str):
            self._kind = value
        @property
        def issuer(self) -> str: ...
        @issuer.setter
        def issuer(self, value: str):
            self._issuer = value
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
        def subject(self) -> str: ...
        @subject.setter
        def subject(self, value: str):
            self._subject = value
        @property
        def status(self) -> str: ...
        @status.setter
        def status(self, value: str):
            self._status = value


        class CertificateStatus(Enum):
            unknown = "unknown"
            expired = "expired"
            expiring = "expiring"
            expiringShortly = "expiringShortly"
            expirationImminent = "expirationImminent"
            good = "good"
            revoked = "revoked"


    class CertificateSpec(vmodl.DynamicData):
        @property
        def kind(self) -> str: ...
        @kind.setter
        def kind(self, value: str):
            self._kind = value


    class CertificateKind(Enum):
        Machine = "Machine"
        VASAClient = "VASAClient"


class CpuSchedulerSystem(vim.ExtensibleManagedObject):
    @property
    def hyperthreadInfo(self) -> CpuSchedulerSystem.HyperThreadScheduleInfo: ...
    def EnableHyperThreading(self) -> NoneType: ...
    def DisableHyperThreading(self) -> NoneType: ...


    class HyperThreadScheduleInfo(vmodl.DynamicData):
        @property
        def available(self) -> bool: ...
        @available.setter
        def available(self, value: bool):
            self._available = value
        @property
        def active(self) -> bool: ...
        @active.setter
        def active(self, value: bool):
            self._active = value
        @property
        def config(self) -> bool: ...
        @config.setter
        def config(self, value: bool):
            self._config = value


class DatastoreBrowser(ManagedObject):
    @property
    def datastore(self) -> List[vim.Datastore]: ...
    @property
    def supportedType(self) -> List[DatastoreBrowser.Query]: ...
    def Search(self, datastorePath: str, searchSpec: DatastoreBrowser.SearchSpec) -> vim.Task: ...
    def SearchSubFolders(self, datastorePath: str, searchSpec: DatastoreBrowser.SearchSpec) -> vim.Task: ...
    def DeleteFile(self, datastorePath: str) -> NoneType: ...


    class FileInfo(vmodl.DynamicData):
        @property
        def path(self) -> str: ...
        @path.setter
        def path(self, value: str):
            self._path = value
        @property
        def friendlyName(self) -> str: ...
        @friendlyName.setter
        def friendlyName(self, value: str):
            self._friendlyName = value
        @property
        def fileSize(self) -> long: ...
        @fileSize.setter
        def fileSize(self, value: long):
            self._fileSize = value
        @property
        def modification(self) -> datetime: ...
        @modification.setter
        def modification(self, value: datetime):
            self._modification = value
        @property
        def owner(self) -> str: ...
        @owner.setter
        def owner(self, value: str):
            self._owner = value


        class Details(vmodl.DynamicData):
            @property
            def fileType(self) -> bool: ...
            @fileType.setter
            def fileType(self, value: bool):
                self._fileType = value
            @property
            def fileSize(self) -> bool: ...
            @fileSize.setter
            def fileSize(self, value: bool):
                self._fileSize = value
            @property
            def modification(self) -> bool: ...
            @modification.setter
            def modification(self, value: bool):
                self._modification = value
            @property
            def fileOwner(self) -> bool: ...
            @fileOwner.setter
            def fileOwner(self, value: bool):
                self._fileOwner = value


    class FloppyImageInfo(DatastoreBrowser.FileInfo): ...


    class FloppyImageQuery(DatastoreBrowser.Query): ...


    class FolderInfo(DatastoreBrowser.FileInfo): ...


    class FolderQuery(DatastoreBrowser.Query): ...


    class IsoImageInfo(DatastoreBrowser.FileInfo): ...


    class IsoImageQuery(DatastoreBrowser.Query): ...


    class Query(vmodl.DynamicData): ...


    class SearchResults(vmodl.DynamicData):
        @property
        def datastore(self) -> vim.Datastore: ...
        @datastore.setter
        def datastore(self, value: vim.Datastore):
            self._datastore = value
        @property
        def folderPath(self) -> str: ...
        @folderPath.setter
        def folderPath(self, value: str):
            self._folderPath = value
        @property
        def file(self) -> List[DatastoreBrowser.FileInfo]: ...
        @file.setter
        def file(self, value: List[DatastoreBrowser.FileInfo]):
            self._file = value


    class SearchSpec(vmodl.DynamicData):
        @property
        def query(self) -> List[DatastoreBrowser.Query]: ...
        @query.setter
        def query(self, value: List[DatastoreBrowser.Query]):
            self._query = value
        @property
        def details(self) -> DatastoreBrowser.FileInfo.Details: ...
        @details.setter
        def details(self, value: DatastoreBrowser.FileInfo.Details):
            self._details = value
        @property
        def searchCaseInsensitive(self) -> bool: ...
        @searchCaseInsensitive.setter
        def searchCaseInsensitive(self, value: bool):
            self._searchCaseInsensitive = value
        @property
        def matchPattern(self) -> List[str]: ...
        @matchPattern.setter
        def matchPattern(self, value: List[str]):
            self._matchPattern = value
        @property
        def sortFoldersFirst(self) -> bool: ...
        @sortFoldersFirst.setter
        def sortFoldersFirst(self, value: bool):
            self._sortFoldersFirst = value


    class TemplateVmConfigInfo(DatastoreBrowser.VmConfigInfo): ...


    class TemplateVmConfigQuery(DatastoreBrowser.VmConfigQuery): ...


    class VmConfigInfo(DatastoreBrowser.FileInfo):
        @property
        def configVersion(self) -> int: ...
        @configVersion.setter
        def configVersion(self, value: int):
            self._configVersion = value
        @property
        def encryption(self) -> DatastoreBrowser.VmConfigInfo.VmConfigEncryptionInfo: ...
        @encryption.setter
        def encryption(self, value: DatastoreBrowser.VmConfigInfo.VmConfigEncryptionInfo):
            self._encryption = value


        class VmConfigEncryptionInfo(vmodl.DynamicData):
            @property
            def keyId(self) -> vim.encryption.CryptoKeyId: ...
            @keyId.setter
            def keyId(self, value: vim.encryption.CryptoKeyId):
                self._keyId = value


    class VmConfigQuery(DatastoreBrowser.Query):
        @property
        def filter(self) -> DatastoreBrowser.VmConfigQuery.Filter: ...
        @filter.setter
        def filter(self, value: DatastoreBrowser.VmConfigQuery.Filter):
            self._filter = value
        @property
        def details(self) -> DatastoreBrowser.VmConfigQuery.Details: ...
        @details.setter
        def details(self, value: DatastoreBrowser.VmConfigQuery.Details):
            self._details = value


        class Details(vmodl.DynamicData):
            @property
            def configVersion(self) -> bool: ...
            @configVersion.setter
            def configVersion(self, value: bool):
                self._configVersion = value
            @property
            def encryption(self) -> bool: ...
            @encryption.setter
            def encryption(self, value: bool):
                self._encryption = value


        class Filter(vmodl.DynamicData):
            @property
            def matchConfigVersion(self) -> List[int]: ...
            @matchConfigVersion.setter
            def matchConfigVersion(self, value: List[int]):
                self._matchConfigVersion = value
            @property
            def encrypted(self) -> bool: ...
            @encrypted.setter
            def encrypted(self, value: bool):
                self._encrypted = value


    class VmDiskInfo(DatastoreBrowser.FileInfo):
        @property
        def diskType(self) -> type: ...
        @diskType.setter
        def diskType(self, value: type):
            self._diskType = value
        @property
        def capacityKb(self) -> long: ...
        @capacityKb.setter
        def capacityKb(self, value: long):
            self._capacityKb = value
        @property
        def hardwareVersion(self) -> int: ...
        @hardwareVersion.setter
        def hardwareVersion(self, value: int):
            self._hardwareVersion = value
        @property
        def controllerType(self) -> type: ...
        @controllerType.setter
        def controllerType(self, value: type):
            self._controllerType = value
        @property
        def diskExtents(self) -> List[str]: ...
        @diskExtents.setter
        def diskExtents(self, value: List[str]):
            self._diskExtents = value
        @property
        def thin(self) -> bool: ...
        @thin.setter
        def thin(self, value: bool):
            self._thin = value
        @property
        def encryption(self) -> DatastoreBrowser.VmDiskInfo.VmDiskEncryptionInfo: ...
        @encryption.setter
        def encryption(self, value: DatastoreBrowser.VmDiskInfo.VmDiskEncryptionInfo):
            self._encryption = value


        class VmDiskEncryptionInfo(vmodl.DynamicData):
            @property
            def keyId(self) -> vim.encryption.CryptoKeyId: ...
            @keyId.setter
            def keyId(self, value: vim.encryption.CryptoKeyId):
                self._keyId = value


    class VmDiskQuery(DatastoreBrowser.Query):
        @property
        def filter(self) -> DatastoreBrowser.VmDiskQuery.Filter: ...
        @filter.setter
        def filter(self, value: DatastoreBrowser.VmDiskQuery.Filter):
            self._filter = value
        @property
        def details(self) -> DatastoreBrowser.VmDiskQuery.Details: ...
        @details.setter
        def details(self, value: DatastoreBrowser.VmDiskQuery.Details):
            self._details = value


        class Details(vmodl.DynamicData):
            @property
            def diskType(self) -> bool: ...
            @diskType.setter
            def diskType(self, value: bool):
                self._diskType = value
            @property
            def capacityKb(self) -> bool: ...
            @capacityKb.setter
            def capacityKb(self, value: bool):
                self._capacityKb = value
            @property
            def hardwareVersion(self) -> bool: ...
            @hardwareVersion.setter
            def hardwareVersion(self, value: bool):
                self._hardwareVersion = value
            @property
            def controllerType(self) -> bool: ...
            @controllerType.setter
            def controllerType(self, value: bool):
                self._controllerType = value
            @property
            def diskExtents(self) -> bool: ...
            @diskExtents.setter
            def diskExtents(self, value: bool):
                self._diskExtents = value
            @property
            def thin(self) -> bool: ...
            @thin.setter
            def thin(self, value: bool):
                self._thin = value
            @property
            def encryption(self) -> bool: ...
            @encryption.setter
            def encryption(self, value: bool):
                self._encryption = value


        class Filter(vmodl.DynamicData):
            @property
            def diskType(self) -> List[type]: ...
            @diskType.setter
            def diskType(self, value: List[type]):
                self._diskType = value
            @property
            def matchHardwareVersion(self) -> List[int]: ...
            @matchHardwareVersion.setter
            def matchHardwareVersion(self, value: List[int]):
                self._matchHardwareVersion = value
            @property
            def controllerType(self) -> List[type]: ...
            @controllerType.setter
            def controllerType(self, value: List[type]):
                self._controllerType = value
            @property
            def thin(self) -> bool: ...
            @thin.setter
            def thin(self, value: bool):
                self._thin = value
            @property
            def encrypted(self) -> bool: ...
            @encrypted.setter
            def encrypted(self, value: bool):
                self._encrypted = value


    class VmLogInfo(DatastoreBrowser.FileInfo): ...


    class VmLogQuery(DatastoreBrowser.Query): ...


    class VmNvramInfo(DatastoreBrowser.FileInfo): ...


    class VmNvramQuery(DatastoreBrowser.Query): ...


    class VmSnapshotInfo(DatastoreBrowser.FileInfo): ...


    class VmSnapshotQuery(DatastoreBrowser.Query): ...


class DatastoreSystem(ManagedObject):
    @property
    def datastore(self) -> List[vim.Datastore]: ...
    @property
    def capabilities(self) -> DatastoreSystem.Capabilities: ...
    def UpdateLocalSwapDatastore(self, datastore: vim.Datastore) -> NoneType: ...
    def QueryAvailableDisksForVmfs(self, datastore: vim.Datastore) -> List[ScsiDisk]: ...
    def QueryVmfsDatastoreCreateOptions(self, devicePath: str, vmfsMajorVersion: int) -> List[VmfsDatastoreOption]: ...
    def CreateVmfsDatastore(self, spec: VmfsDatastoreCreateSpec) -> vim.Datastore: ...
    def QueryVmfsDatastoreExtendOptions(self, datastore: vim.Datastore, devicePath: str, suppressExpandCandidates: bool) -> List[VmfsDatastoreOption]: ...
    def QueryVmfsDatastoreExpandOptions(self, datastore: vim.Datastore) -> List[VmfsDatastoreOption]: ...
    def ExtendVmfsDatastore(self, datastore: vim.Datastore, spec: VmfsDatastoreExtendSpec) -> vim.Datastore: ...
    def EnableClusteredVmdkSupport(self, datastore: vim.Datastore) -> NoneType: ...
    def DisableClusteredVmdkSupport(self, datastore: vim.Datastore) -> NoneType: ...
    def ExpandVmfsDatastore(self, datastore: vim.Datastore, spec: VmfsDatastoreExpandSpec) -> vim.Datastore: ...
    def CreateNasDatastore(self, spec: NasVolume.Specification) -> vim.Datastore: ...
    def CreateLocalDatastore(self, name: str, path: str) -> vim.Datastore: ...
    def CreateVvolDatastore(self, spec: DatastoreSystem.VvolDatastoreSpec) -> vim.Datastore: ...
    def RemoveDatastore(self, datastore: vim.Datastore) -> NoneType: ...
    def SetMaxQueueDepth(self, datastore: vim.Datastore, maxQdepth: long) -> NoneType: ...
    def QueryMaxQueueDepth(self, datastore: vim.Datastore) -> long: ...
    def RemoveDatastoreEx(self, datastore: List[vim.Datastore]) -> vim.Task: ...
    def ConfigureDatastorePrincipal(self, userName: str, password: str) -> NoneType: ...
    def QueryUnresolvedVmfsVolumes(self) -> List[UnresolvedVmfsVolume]: ...
    def ResignatureUnresolvedVmfsVolume(self, resolutionSpec: UnresolvedVmfsResignatureSpec) -> vim.Task: ...


    class Capabilities(vmodl.DynamicData):
        @property
        def nfsMountCreationRequired(self) -> bool: ...
        @nfsMountCreationRequired.setter
        def nfsMountCreationRequired(self, value: bool):
            self._nfsMountCreationRequired = value
        @property
        def nfsMountCreationSupported(self) -> bool: ...
        @nfsMountCreationSupported.setter
        def nfsMountCreationSupported(self, value: bool):
            self._nfsMountCreationSupported = value
        @property
        def localDatastoreSupported(self) -> bool: ...
        @localDatastoreSupported.setter
        def localDatastoreSupported(self, value: bool):
            self._localDatastoreSupported = value
        @property
        def vmfsExtentExpansionSupported(self) -> bool: ...
        @vmfsExtentExpansionSupported.setter
        def vmfsExtentExpansionSupported(self, value: bool):
            self._vmfsExtentExpansionSupported = value


    class DatastoreResult(vmodl.DynamicData):
        @property
        def key(self) -> vim.Datastore: ...
        @key.setter
        def key(self, value: vim.Datastore):
            self._key = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


    class VvolDatastoreSpec(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def scId(self) -> str: ...
        @scId.setter
        def scId(self, value: str):
            self._scId = value


class DateTimeSystem(ManagedObject):
    @property
    def dateTimeInfo(self) -> DateTimeInfo: ...
    def UpdateConfig(self, config: DateTimeConfig) -> NoneType: ...
    def QueryAvailableTimeZones(self) -> List[DateTimeSystem.TimeZone]: ...
    def QueryDateTime(self) -> datetime: ...
    def UpdateDateTime(self, dateTime: datetime) -> NoneType: ...
    def Refresh(self) -> NoneType: ...
    def TestTimeService(self) -> DateTimeSystem.ServiceTestResult: ...


    class ServiceTestResult(vmodl.DynamicData):
        @property
        def workingNormally(self) -> bool: ...
        @workingNormally.setter
        def workingNormally(self, value: bool):
            self._workingNormally = value
        @property
        def report(self) -> List[str]: ...
        @report.setter
        def report(self, value: List[str]):
            self._report = value


    class TimeZone(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
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
        def gmtOffset(self) -> int: ...
        @gmtOffset.setter
        def gmtOffset(self, value: int):
            self._gmtOffset = value


class DiagnosticSystem(ManagedObject):
    @property
    def activePartition(self) -> DiagnosticPartition: ...
    def QueryAvailablePartition(self) -> List[DiagnosticPartition]: ...
    def SelectActivePartition(self, partition: ScsiDisk.Partition) -> NoneType: ...
    def QueryPartitionCreateOptions(self, storageType: str, diagnosticType: str) -> List[DiagnosticPartition.CreateOption]: ...
    def QueryPartitionCreateDesc(self, diskUuid: str, diagnosticType: str) -> DiagnosticPartition.CreateDescription: ...
    def CreateDiagnosticPartition(self, spec: DiagnosticPartition.CreateSpec) -> NoneType: ...


class DirectoryStore(AuthenticationStore): ...


class EsxAgentHostManager(ManagedObject):
    @property
    def configInfo(self) -> EsxAgentHostManager.ConfigInfo: ...
    def UpdateConfig(self, configInfo: EsxAgentHostManager.ConfigInfo) -> NoneType: ...


    class ConfigInfo(vmodl.DynamicData):
        @property
        def agentVmDatastore(self) -> vim.Datastore: ...
        @agentVmDatastore.setter
        def agentVmDatastore(self, value: vim.Datastore):
            self._agentVmDatastore = value
        @property
        def agentVmNetwork(self) -> vim.Network: ...
        @agentVmNetwork.setter
        def agentVmNetwork(self, value: vim.Network):
            self._agentVmNetwork = value


class FirewallSystem(vim.ExtensibleManagedObject):
    @property
    def firewallInfo(self) -> FirewallInfo: ...
    def UpdateDefaultPolicy(self, defaultPolicy: FirewallInfo.DefaultPolicy) -> NoneType: ...
    def EnableRuleset(self, id: str) -> NoneType: ...
    def DisableRuleset(self, id: str) -> NoneType: ...
    def UpdateRuleset(self, id: str, spec: Ruleset.RulesetSpec) -> NoneType: ...
    def Refresh(self) -> NoneType: ...


class FirmwareSystem(ManagedObject):
    def ResetToFactoryDefaults(self) -> NoneType: ...
    def BackupConfiguration(self) -> str: ...
    def QueryConfigUploadURL(self) -> str: ...
    def RestoreConfiguration(self, force: bool) -> NoneType: ...


class GraphicsManager(vim.ExtensibleManagedObject):
    @property
    def graphicsInfo(self) -> List[GraphicsInfo]: ...
    @property
    def graphicsConfig(self) -> GraphicsConfig: ...
    @property
    def sharedPassthruGpuTypes(self) -> List[str]: ...
    @property
    def sharedGpuCapabilities(self) -> List[SharedGpuCapabilities]: ...
    def RetrieveVgpuDeviceInfo(self) -> List[vim.vm.VgpuDeviceInfo]: ...
    def RetrieveVgpuProfileInfo(self) -> List[vim.vm.VgpuProfileInfo]: ...
    def Refresh(self) -> NoneType: ...
    def IsSharedGraphicsActive(self) -> bool: ...
    def UpdateGraphicsConfig(self, config: GraphicsConfig) -> NoneType: ...


class HealthStatusSystem(ManagedObject):
    @property
    def runtime(self) -> HealthStatusSystem.Runtime: ...
    def Refresh(self) -> NoneType: ...
    def ResetSystemHealthInfo(self) -> NoneType: ...
    def ClearSystemEventLog(self) -> NoneType: ...
    def FetchSystemEventLog(self) -> List[SystemEventInfo]: ...


    class Runtime(vmodl.DynamicData):
        @property
        def systemHealthInfo(self) -> SystemHealthInfo: ...
        @systemHealthInfo.setter
        def systemHealthInfo(self, value: SystemHealthInfo):
            self._systemHealthInfo = value
        @property
        def hardwareStatusInfo(self) -> HardwareStatusInfo: ...
        @hardwareStatusInfo.setter
        def hardwareStatusInfo(self, value: HardwareStatusInfo):
            self._hardwareStatusInfo = value


class HostAccessManager(ManagedObject):
    @property
    def lockdownMode(self) -> HostAccessManager.LockdownMode | Literal['lockdownDisabled', 'lockdownNormal', 'lockdownStrict']: ...
    def RetrieveAccessEntries(self) -> List[HostAccessManager.AccessEntry]: ...
    def ChangeAccessMode(self, principal: str, isGroup: bool, accessMode: HostAccessManager.AccessMode | Literal['accessNone', 'accessAdmin', 'accessNoAccess', 'accessReadOnly', 'accessOther']) -> NoneType: ...
    def QuerySystemUsers(self) -> List[str]: ...
    def UpdateSystemUsers(self, users: List[str]) -> NoneType: ...
    def QueryLockdownExceptions(self) -> List[str]: ...
    def UpdateLockdownExceptions(self, users: List[str]) -> NoneType: ...
    def ChangeLockdownMode(self, mode: HostAccessManager.LockdownMode | Literal['lockdownDisabled', 'lockdownNormal', 'lockdownStrict']) -> NoneType: ...


    class AccessEntry(vmodl.DynamicData):
        @property
        def principal(self) -> str: ...
        @principal.setter
        def principal(self, value: str):
            self._principal = value
        @property
        def group(self) -> bool: ...
        @group.setter
        def group(self, value: bool):
            self._group = value
        @property
        def accessMode(self) -> HostAccessManager.AccessMode | Literal['accessNone', 'accessAdmin', 'accessNoAccess', 'accessReadOnly', 'accessOther']: ...
        @accessMode.setter
        def accessMode(self, value: HostAccessManager.AccessMode | Literal['accessNone', 'accessAdmin', 'accessNoAccess', 'accessReadOnly', 'accessOther']):
            self._accessMode = value


    class AccessMode(Enum):
        accessNone = "accessNone"
        accessAdmin = "accessAdmin"
        accessNoAccess = "accessNoAccess"
        accessReadOnly = "accessReadOnly"
        accessOther = "accessOther"


    class LockdownMode(Enum):
        lockdownDisabled = "lockdownDisabled"
        lockdownNormal = "lockdownNormal"
        lockdownStrict = "lockdownStrict"


class ImageConfigManager(ManagedObject):
    def QueryHostAcceptanceLevel(self) -> str: ...
    def QueryHostImageProfile(self) -> ImageConfigManager.ImageProfileSummary: ...
    def UpdateAcceptanceLevel(self, newAcceptanceLevel: str) -> NoneType: ...
    def FetchSoftwarePackages(self) -> List[SoftwarePackage]: ...
    def InstallDate(self) -> datetime: ...


    class ImageProfileSummary(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def vendor(self) -> str: ...
        @vendor.setter
        def vendor(self, value: str):
            self._vendor = value


    class AcceptanceLevel(Enum):
        vmware_certified = "vmware_certified"
        vmware_accepted = "vmware_accepted"
        partner = "partner"
        community = "community"


class IscsiManager(ManagedObject):
    def QueryVnicStatus(self, vnicDevice: str) -> IscsiManager.IscsiStatus: ...
    def QueryPnicStatus(self, pnicDevice: str) -> IscsiManager.IscsiStatus: ...
    def QueryBoundVnics(self, iScsiHbaName: str) -> List[IscsiManager.IscsiPortInfo]: ...
    def QueryCandidateNics(self, iScsiHbaName: str) -> List[IscsiManager.IscsiPortInfo]: ...
    def BindVnic(self, iScsiHbaName: str, vnicDevice: str) -> NoneType: ...
    def UnbindVnic(self, iScsiHbaName: str, vnicDevice: str, force: bool) -> NoneType: ...
    def QueryMigrationDependencies(self, pnicDevice: List[str]) -> IscsiManager.IscsiMigrationDependency: ...


    class IscsiDependencyEntity(vmodl.DynamicData):
        @property
        def pnicDevice(self) -> str: ...
        @pnicDevice.setter
        def pnicDevice(self, value: str):
            self._pnicDevice = value
        @property
        def vnicDevice(self) -> str: ...
        @vnicDevice.setter
        def vnicDevice(self, value: str):
            self._vnicDevice = value
        @property
        def vmhbaName(self) -> str: ...
        @vmhbaName.setter
        def vmhbaName(self, value: str):
            self._vmhbaName = value


    class IscsiMigrationDependency(vmodl.DynamicData):
        @property
        def migrationAllowed(self) -> bool: ...
        @migrationAllowed.setter
        def migrationAllowed(self, value: bool):
            self._migrationAllowed = value
        @property
        def disallowReason(self) -> IscsiManager.IscsiStatus: ...
        @disallowReason.setter
        def disallowReason(self, value: IscsiManager.IscsiStatus):
            self._disallowReason = value
        @property
        def dependency(self) -> List[IscsiManager.IscsiDependencyEntity]: ...
        @dependency.setter
        def dependency(self, value: List[IscsiManager.IscsiDependencyEntity]):
            self._dependency = value


    class IscsiPortInfo(vmodl.DynamicData):
        @property
        def vnicDevice(self) -> str: ...
        @vnicDevice.setter
        def vnicDevice(self, value: str):
            self._vnicDevice = value
        @property
        def vnic(self) -> VirtualNic: ...
        @vnic.setter
        def vnic(self, value: VirtualNic):
            self._vnic = value
        @property
        def pnicDevice(self) -> str: ...
        @pnicDevice.setter
        def pnicDevice(self, value: str):
            self._pnicDevice = value
        @property
        def pnic(self) -> PhysicalNic: ...
        @pnic.setter
        def pnic(self, value: PhysicalNic):
            self._pnic = value
        @property
        def switchName(self) -> str: ...
        @switchName.setter
        def switchName(self, value: str):
            self._switchName = value
        @property
        def switchUuid(self) -> str: ...
        @switchUuid.setter
        def switchUuid(self, value: str):
            self._switchUuid = value
        @property
        def portgroupName(self) -> str: ...
        @portgroupName.setter
        def portgroupName(self, value: str):
            self._portgroupName = value
        @property
        def portgroupKey(self) -> str: ...
        @portgroupKey.setter
        def portgroupKey(self, value: str):
            self._portgroupKey = value
        @property
        def portKey(self) -> str: ...
        @portKey.setter
        def portKey(self, value: str):
            self._portKey = value
        @property
        def opaqueNetworkId(self) -> str: ...
        @opaqueNetworkId.setter
        def opaqueNetworkId(self, value: str):
            self._opaqueNetworkId = value
        @property
        def opaqueNetworkType(self) -> str: ...
        @opaqueNetworkType.setter
        def opaqueNetworkType(self, value: str):
            self._opaqueNetworkType = value
        @property
        def opaqueNetworkName(self) -> str: ...
        @opaqueNetworkName.setter
        def opaqueNetworkName(self, value: str):
            self._opaqueNetworkName = value
        @property
        def externalId(self) -> str: ...
        @externalId.setter
        def externalId(self, value: str):
            self._externalId = value
        @property
        def complianceStatus(self) -> IscsiManager.IscsiStatus: ...
        @complianceStatus.setter
        def complianceStatus(self, value: IscsiManager.IscsiStatus):
            self._complianceStatus = value
        @property
        def pathStatus(self) -> str: ...
        @pathStatus.setter
        def pathStatus(self, value: str):
            self._pathStatus = value


        class PathStatus(Enum):
            notUsed = "notUsed"
            active = "active"
            standBy = "standBy"
            lastActive = "lastActive"


    class IscsiStatus(vmodl.DynamicData):
        @property
        def reason(self) -> List[vmodl.MethodFault]: ...
        @reason.setter
        def reason(self, value: List[vmodl.MethodFault]):
            self._reason = value


class KernelModuleSystem(ManagedObject):
    def QueryModules(self) -> List[KernelModuleSystem.ModuleInfo]: ...
    def UpdateModuleOptionString(self, name: str, options: str) -> NoneType: ...
    def QueryConfiguredModuleOptionString(self, name: str) -> str: ...


    class ModuleInfo(vmodl.DynamicData):
        @property
        def id(self) -> int: ...
        @id.setter
        def id(self, value: int):
            self._id = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def version(self) -> str: ...
        @version.setter
        def version(self, value: str):
            self._version = value
        @property
        def filename(self) -> str: ...
        @filename.setter
        def filename(self, value: str):
            self._filename = value
        @property
        def optionString(self) -> str: ...
        @optionString.setter
        def optionString(self, value: str):
            self._optionString = value
        @property
        def loaded(self) -> bool: ...
        @loaded.setter
        def loaded(self, value: bool):
            self._loaded = value
        @property
        def enabled(self) -> bool: ...
        @enabled.setter
        def enabled(self, value: bool):
            self._enabled = value
        @property
        def useCount(self) -> int: ...
        @useCount.setter
        def useCount(self, value: int):
            self._useCount = value
        @property
        def readOnlySection(self) -> KernelModuleSystem.ModuleInfo.SectionInfo: ...
        @readOnlySection.setter
        def readOnlySection(self, value: KernelModuleSystem.ModuleInfo.SectionInfo):
            self._readOnlySection = value
        @property
        def writableSection(self) -> KernelModuleSystem.ModuleInfo.SectionInfo: ...
        @writableSection.setter
        def writableSection(self, value: KernelModuleSystem.ModuleInfo.SectionInfo):
            self._writableSection = value
        @property
        def textSection(self) -> KernelModuleSystem.ModuleInfo.SectionInfo: ...
        @textSection.setter
        def textSection(self, value: KernelModuleSystem.ModuleInfo.SectionInfo):
            self._textSection = value
        @property
        def dataSection(self) -> KernelModuleSystem.ModuleInfo.SectionInfo: ...
        @dataSection.setter
        def dataSection(self, value: KernelModuleSystem.ModuleInfo.SectionInfo):
            self._dataSection = value
        @property
        def bssSection(self) -> KernelModuleSystem.ModuleInfo.SectionInfo: ...
        @bssSection.setter
        def bssSection(self, value: KernelModuleSystem.ModuleInfo.SectionInfo):
            self._bssSection = value


        class SectionInfo(vmodl.DynamicData):
            @property
            def address(self) -> long: ...
            @address.setter
            def address(self, value: long):
                self._address = value
            @property
            def length(self) -> int: ...
            @length.setter
            def length(self, value: int):
                self._length = value


class LocalAccountManager(ManagedObject):
    def CreateUser(self, user: LocalAccountManager.AccountSpecification) -> NoneType: ...
    def UpdateUser(self, user: LocalAccountManager.AccountSpecification) -> NoneType: ...
    def CreateGroup(self, group: LocalAccountManager.AccountSpecification) -> NoneType: ...
    def RemoveUser(self, userName: str) -> NoneType: ...
    def RemoveGroup(self, groupName: str) -> NoneType: ...
    def AssignUserToGroup(self, user: str, group: str) -> NoneType: ...
    def UnassignUserFromGroup(self, user: str, group: str) -> NoneType: ...
    def ChangePassword(self, user: str, oldPassword: str, newPassword: str) -> NoneType: ...


    class AccountSpecification(vmodl.DynamicData):
        @property
        def id(self) -> str: ...
        @id.setter
        def id(self, value: str):
            self._id = value
        @property
        def password(self) -> str: ...
        @password.setter
        def password(self, value: str):
            self._password = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value


    class PosixAccountSpecification(LocalAccountManager.AccountSpecification):
        @property
        def posixId(self) -> int: ...
        @posixId.setter
        def posixId(self, value: int):
            self._posixId = value
        @property
        def shellAccess(self) -> bool: ...
        @shellAccess.setter
        def shellAccess(self, value: bool):
            self._shellAccess = value


class LocalAuthentication(AuthenticationStore): ...


class MemoryManagerSystem(vim.ExtensibleManagedObject):
    @property
    def consoleReservationInfo(self) -> MemoryManagerSystem.ServiceConsoleReservationInfo: ...
    @property
    def virtualMachineReservationInfo(self) -> MemoryManagerSystem.VirtualMachineReservationInfo: ...
    def ReconfigureServiceConsoleReservation(self, cfgBytes: long) -> NoneType: ...
    def ReconfigureVirtualMachineReservation(self, spec: MemoryManagerSystem.VirtualMachineReservationSpec) -> NoneType: ...


    class ServiceConsoleReservationInfo(vmodl.DynamicData):
        @property
        def serviceConsoleReservedCfg(self) -> long: ...
        @serviceConsoleReservedCfg.setter
        def serviceConsoleReservedCfg(self, value: long):
            self._serviceConsoleReservedCfg = value
        @property
        def serviceConsoleReserved(self) -> long: ...
        @serviceConsoleReserved.setter
        def serviceConsoleReserved(self, value: long):
            self._serviceConsoleReserved = value
        @property
        def unreserved(self) -> long: ...
        @unreserved.setter
        def unreserved(self, value: long):
            self._unreserved = value


    class VirtualMachineReservationInfo(vmodl.DynamicData):
        @property
        def virtualMachineMin(self) -> long: ...
        @virtualMachineMin.setter
        def virtualMachineMin(self, value: long):
            self._virtualMachineMin = value
        @property
        def virtualMachineMax(self) -> long: ...
        @virtualMachineMax.setter
        def virtualMachineMax(self, value: long):
            self._virtualMachineMax = value
        @property
        def virtualMachineReserved(self) -> long: ...
        @virtualMachineReserved.setter
        def virtualMachineReserved(self, value: long):
            self._virtualMachineReserved = value
        @property
        def allocationPolicy(self) -> str: ...
        @allocationPolicy.setter
        def allocationPolicy(self, value: str):
            self._allocationPolicy = value


        class AllocationPolicy(Enum):
            swapNone = "swapNone"
            swapSome = "swapSome"
            swapMost = "swapMost"


    class VirtualMachineReservationSpec(vmodl.DynamicData):
        @property
        def virtualMachineReserved(self) -> long: ...
        @virtualMachineReserved.setter
        def virtualMachineReserved(self, value: long):
            self._virtualMachineReserved = value
        @property
        def allocationPolicy(self) -> str: ...
        @allocationPolicy.setter
        def allocationPolicy(self, value: str):
            self._allocationPolicy = value


class MessageBusProxy(ManagedObject): ...


class NetworkSystem(vim.ExtensibleManagedObject):
    @property
    def capabilities(self) -> NetCapabilities: ...
    @property
    def networkInfo(self) -> NetworkInfo: ...
    @property
    def offloadCapabilities(self) -> NetOffloadCapabilities: ...
    @property
    def networkConfig(self) -> NetworkConfig: ...
    @property
    def dnsConfig(self) -> DnsConfig: ...
    @property
    def ipRouteConfig(self) -> IpRouteConfig: ...
    @property
    def consoleIpRouteConfig(self) -> IpRouteConfig: ...
    def UpdateNetworkConfig(self, config: NetworkConfig, changeMode: str) -> NetworkConfig.Result: ...
    def UpdateDnsConfig(self, config: DnsConfig) -> NoneType: ...
    def UpdateIpRouteConfig(self, config: IpRouteConfig) -> NoneType: ...
    def UpdateConsoleIpRouteConfig(self, config: IpRouteConfig) -> NoneType: ...
    def UpdateIpRouteTableConfig(self, config: IpRouteTableConfig) -> NoneType: ...
    def AddVirtualSwitch(self, vswitchName: str, spec: VirtualSwitch.Specification) -> NoneType: ...
    def RemoveVirtualSwitch(self, vswitchName: str) -> NoneType: ...
    def UpdateVirtualSwitch(self, vswitchName: str, spec: VirtualSwitch.Specification) -> NoneType: ...
    def AddPortGroup(self, portgrp: PortGroup.Specification) -> NoneType: ...
    def RemovePortGroup(self, pgName: str) -> NoneType: ...
    def UpdatePortGroup(self, pgName: str, portgrp: PortGroup.Specification) -> NoneType: ...
    def UpdatePhysicalNicLinkSpeed(self, device: str, linkSpeed: PhysicalNic.LinkSpeedDuplex) -> NoneType: ...
    def QueryNetworkHint(self, device: List[str]) -> List[PhysicalNic.NetworkHint]: ...
    def AddVirtualNic(self, portgroup: str, nic: VirtualNic.Specification) -> str: ...
    def RemoveVirtualNic(self, device: str) -> NoneType: ...
    def UpdateVirtualNic(self, device: str, nic: VirtualNic.Specification) -> NoneType: ...
    def AddServiceConsoleVirtualNic(self, portgroup: str, nic: VirtualNic.Specification) -> str: ...
    def RemoveServiceConsoleVirtualNic(self, device: str) -> NoneType: ...
    def UpdateServiceConsoleVirtualNic(self, device: str, nic: VirtualNic.Specification) -> NoneType: ...
    def RestartServiceConsoleVirtualNic(self, device: str) -> NoneType: ...
    def Refresh(self) -> NoneType: ...


class NvdimmSystem(ManagedObject):
    @property
    def nvdimmSystemInfo(self) -> NvdimmSystem.NvdimmSystemInfo: ...
    def CreateNamespace(self, createSpec: NvdimmSystem.NamespaceCreateSpec) -> vim.Task: ...
    def CreatePMemNamespace(self, createSpec: NvdimmSystem.PMemNamespaceCreateSpec) -> vim.Task: ...
    def DeleteNamespace(self, deleteSpec: NvdimmSystem.NamespaceDeleteSpec) -> vim.Task: ...
    def DeleteBlockNamespaces(self) -> vim.Task: ...


    class DimmInfo(vmodl.DynamicData):
        @property
        def dimmHandle(self) -> int: ...
        @dimmHandle.setter
        def dimmHandle(self, value: int):
            self._dimmHandle = value
        @property
        def healthInfo(self) -> NvdimmSystem.HealthInfo: ...
        @healthInfo.setter
        def healthInfo(self, value: NvdimmSystem.HealthInfo):
            self._healthInfo = value
        @property
        def totalCapacity(self) -> long: ...
        @totalCapacity.setter
        def totalCapacity(self, value: long):
            self._totalCapacity = value
        @property
        def persistentCapacity(self) -> long: ...
        @persistentCapacity.setter
        def persistentCapacity(self, value: long):
            self._persistentCapacity = value
        @property
        def availablePersistentCapacity(self) -> long: ...
        @availablePersistentCapacity.setter
        def availablePersistentCapacity(self, value: long):
            self._availablePersistentCapacity = value
        @property
        def volatileCapacity(self) -> long: ...
        @volatileCapacity.setter
        def volatileCapacity(self, value: long):
            self._volatileCapacity = value
        @property
        def availableVolatileCapacity(self) -> long: ...
        @availableVolatileCapacity.setter
        def availableVolatileCapacity(self, value: long):
            self._availableVolatileCapacity = value
        @property
        def blockCapacity(self) -> long: ...
        @blockCapacity.setter
        def blockCapacity(self, value: long):
            self._blockCapacity = value
        @property
        def regionInfo(self) -> List[NvdimmSystem.RegionInfo]: ...
        @regionInfo.setter
        def regionInfo(self, value: List[NvdimmSystem.RegionInfo]):
            self._regionInfo = value
        @property
        def representationString(self) -> str: ...
        @representationString.setter
        def representationString(self, value: str):
            self._representationString = value


    class Guid(vmodl.DynamicData):
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value


    class HealthInfo(vmodl.DynamicData):
        @property
        def healthStatus(self) -> str: ...
        @healthStatus.setter
        def healthStatus(self, value: str):
            self._healthStatus = value
        @property
        def healthInformation(self) -> str: ...
        @healthInformation.setter
        def healthInformation(self, value: str):
            self._healthInformation = value
        @property
        def stateFlagInfo(self) -> List[str]: ...
        @stateFlagInfo.setter
        def stateFlagInfo(self, value: List[str]):
            self._stateFlagInfo = value
        @property
        def dimmTemperature(self) -> int: ...
        @dimmTemperature.setter
        def dimmTemperature(self, value: int):
            self._dimmTemperature = value
        @property
        def dimmTemperatureThreshold(self) -> int: ...
        @dimmTemperatureThreshold.setter
        def dimmTemperatureThreshold(self, value: int):
            self._dimmTemperatureThreshold = value
        @property
        def spareBlocksPercentage(self) -> int: ...
        @spareBlocksPercentage.setter
        def spareBlocksPercentage(self, value: int):
            self._spareBlocksPercentage = value
        @property
        def spareBlockThreshold(self) -> int: ...
        @spareBlockThreshold.setter
        def spareBlockThreshold(self, value: int):
            self._spareBlockThreshold = value
        @property
        def dimmLifespanPercentage(self) -> int: ...
        @dimmLifespanPercentage.setter
        def dimmLifespanPercentage(self, value: int):
            self._dimmLifespanPercentage = value
        @property
        def esTemperature(self) -> int: ...
        @esTemperature.setter
        def esTemperature(self, value: int):
            self._esTemperature = value
        @property
        def esTemperatureThreshold(self) -> int: ...
        @esTemperatureThreshold.setter
        def esTemperatureThreshold(self, value: int):
            self._esTemperatureThreshold = value
        @property
        def esLifespanPercentage(self) -> int: ...
        @esLifespanPercentage.setter
        def esLifespanPercentage(self, value: int):
            self._esLifespanPercentage = value


        class StateFlag(Enum):
            normal = "normal"
            error = "error"


    class InterleaveSetInfo(vmodl.DynamicData):
        @property
        def setId(self) -> int: ...
        @setId.setter
        def setId(self, value: int):
            self._setId = value
        @property
        def rangeType(self) -> str: ...
        @rangeType.setter
        def rangeType(self, value: str):
            self._rangeType = value
        @property
        def baseAddress(self) -> long: ...
        @baseAddress.setter
        def baseAddress(self, value: long):
            self._baseAddress = value
        @property
        def size(self) -> long: ...
        @size.setter
        def size(self, value: long):
            self._size = value
        @property
        def availableSize(self) -> long: ...
        @availableSize.setter
        def availableSize(self, value: long):
            self._availableSize = value
        @property
        def deviceList(self) -> List[int]: ...
        @deviceList.setter
        def deviceList(self, value: List[int]):
            self._deviceList = value
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value


        class InterleaveSetState(Enum):
            invalid = "invalid"
            active = "active"


    class NamespaceCreateSpec(vmodl.DynamicData):
        @property
        def friendlyName(self) -> str: ...
        @friendlyName.setter
        def friendlyName(self, value: str):
            self._friendlyName = value
        @property
        def blockSize(self) -> long: ...
        @blockSize.setter
        def blockSize(self, value: long):
            self._blockSize = value
        @property
        def blockCount(self) -> long: ...
        @blockCount.setter
        def blockCount(self, value: long):
            self._blockCount = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def locationID(self) -> int: ...
        @locationID.setter
        def locationID(self, value: int):
            self._locationID = value


    class NamespaceDeleteSpec(vmodl.DynamicData):
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value


    class NamespaceDetails(vmodl.DynamicData):
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def friendlyName(self) -> str: ...
        @friendlyName.setter
        def friendlyName(self, value: str):
            self._friendlyName = value
        @property
        def size(self) -> long: ...
        @size.setter
        def size(self, value: long):
            self._size = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def namespaceHealthStatus(self) -> str: ...
        @namespaceHealthStatus.setter
        def namespaceHealthStatus(self, value: str):
            self._namespaceHealthStatus = value
        @property
        def interleavesetID(self) -> int: ...
        @interleavesetID.setter
        def interleavesetID(self, value: int):
            self._interleavesetID = value
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value


        class NamespaceHealthStatus(Enum):
            normal = "normal"
            missing = "missing"
            labelMissing = "labelMissing"
            interleaveBroken = "interleaveBroken"
            labelInconsistent = "labelInconsistent"


        class NamespaceState(Enum):
            invalid = "invalid"
            notInUse = "notInUse"
            inUse = "inUse"


    class NamespaceInfo(vmodl.DynamicData):
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def friendlyName(self) -> str: ...
        @friendlyName.setter
        def friendlyName(self, value: str):
            self._friendlyName = value
        @property
        def blockSize(self) -> long: ...
        @blockSize.setter
        def blockSize(self, value: long):
            self._blockSize = value
        @property
        def blockCount(self) -> long: ...
        @blockCount.setter
        def blockCount(self, value: long):
            self._blockCount = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def namespaceHealthStatus(self) -> str: ...
        @namespaceHealthStatus.setter
        def namespaceHealthStatus(self, value: str):
            self._namespaceHealthStatus = value
        @property
        def locationID(self) -> int: ...
        @locationID.setter
        def locationID(self, value: int):
            self._locationID = value
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value


    class NvdimmSystemInfo(vmodl.DynamicData):
        @property
        def summary(self) -> NvdimmSystem.Summary: ...
        @summary.setter
        def summary(self, value: NvdimmSystem.Summary):
            self._summary = value
        @property
        def dimms(self) -> List[int]: ...
        @dimms.setter
        def dimms(self, value: List[int]):
            self._dimms = value
        @property
        def dimmInfo(self) -> List[NvdimmSystem.DimmInfo]: ...
        @dimmInfo.setter
        def dimmInfo(self, value: List[NvdimmSystem.DimmInfo]):
            self._dimmInfo = value
        @property
        def interleaveSet(self) -> List[int]: ...
        @interleaveSet.setter
        def interleaveSet(self, value: List[int]):
            self._interleaveSet = value
        @property
        def iSetInfo(self) -> List[NvdimmSystem.InterleaveSetInfo]: ...
        @iSetInfo.setter
        def iSetInfo(self, value: List[NvdimmSystem.InterleaveSetInfo]):
            self._iSetInfo = value
        @property
        def namespace(self) -> List[NvdimmSystem.Guid]: ...
        @namespace.setter
        def namespace(self, value: List[NvdimmSystem.Guid]):
            self._namespace = value
        @property
        def nsInfo(self) -> List[NvdimmSystem.NamespaceInfo]: ...
        @nsInfo.setter
        def nsInfo(self, value: List[NvdimmSystem.NamespaceInfo]):
            self._nsInfo = value
        @property
        def nsDetails(self) -> List[NvdimmSystem.NamespaceDetails]: ...
        @nsDetails.setter
        def nsDetails(self, value: List[NvdimmSystem.NamespaceDetails]):
            self._nsDetails = value


    class PMemNamespaceCreateSpec(vmodl.DynamicData):
        @property
        def friendlyName(self) -> str: ...
        @friendlyName.setter
        def friendlyName(self, value: str):
            self._friendlyName = value
        @property
        def size(self) -> long: ...
        @size.setter
        def size(self, value: long):
            self._size = value
        @property
        def interleavesetID(self) -> int: ...
        @interleavesetID.setter
        def interleavesetID(self, value: int):
            self._interleavesetID = value


    class RegionInfo(vmodl.DynamicData):
        @property
        def regionId(self) -> int: ...
        @regionId.setter
        def regionId(self, value: int):
            self._regionId = value
        @property
        def setId(self) -> int: ...
        @setId.setter
        def setId(self, value: int):
            self._setId = value
        @property
        def rangeType(self) -> str: ...
        @rangeType.setter
        def rangeType(self, value: str):
            self._rangeType = value
        @property
        def startAddr(self) -> long: ...
        @startAddr.setter
        def startAddr(self, value: long):
            self._startAddr = value
        @property
        def size(self) -> long: ...
        @size.setter
        def size(self, value: long):
            self._size = value
        @property
        def offset(self) -> long: ...
        @offset.setter
        def offset(self, value: long):
            self._offset = value


    class Summary(vmodl.DynamicData):
        @property
        def numDimms(self) -> int: ...
        @numDimms.setter
        def numDimms(self, value: int):
            self._numDimms = value
        @property
        def healthStatus(self) -> str: ...
        @healthStatus.setter
        def healthStatus(self, value: str):
            self._healthStatus = value
        @property
        def totalCapacity(self) -> long: ...
        @totalCapacity.setter
        def totalCapacity(self, value: long):
            self._totalCapacity = value
        @property
        def persistentCapacity(self) -> long: ...
        @persistentCapacity.setter
        def persistentCapacity(self, value: long):
            self._persistentCapacity = value
        @property
        def blockCapacity(self) -> long: ...
        @blockCapacity.setter
        def blockCapacity(self, value: long):
            self._blockCapacity = value
        @property
        def availableCapacity(self) -> long: ...
        @availableCapacity.setter
        def availableCapacity(self, value: long):
            self._availableCapacity = value
        @property
        def numInterleavesets(self) -> int: ...
        @numInterleavesets.setter
        def numInterleavesets(self, value: int):
            self._numInterleavesets = value
        @property
        def numNamespaces(self) -> int: ...
        @numNamespaces.setter
        def numNamespaces(self, value: int):
            self._numNamespaces = value


    class NamespaceType(Enum):
        blockNamespace = "blockNamespace"
        persistentNamespace = "persistentNamespace"


    class RangeType(Enum):
        volatileRange = "volatileRange"
        persistentRange = "persistentRange"
        controlRange = "controlRange"
        blockRange = "blockRange"
        volatileVirtualDiskRange = "volatileVirtualDiskRange"
        volatileVirtualCDRange = "volatileVirtualCDRange"
        persistentVirtualDiskRange = "persistentVirtualDiskRange"
        persistentVirtualCDRange = "persistentVirtualCDRange"


class PatchManager(ManagedObject):
    def Check(self, metaUrls: List[str], bundleUrls: List[str], spec: PatchManager.PatchManagerOperationSpec) -> vim.Task: ...
    def Scan(self, repository: PatchManager.Locator, updateID: List[str]) -> vim.Task: ...
    def ScanV2(self, metaUrls: List[str], bundleUrls: List[str], spec: PatchManager.PatchManagerOperationSpec) -> vim.Task: ...
    def Stage(self, metaUrls: List[str], bundleUrls: List[str], vibUrls: List[str], spec: PatchManager.PatchManagerOperationSpec) -> vim.Task: ...
    def Install(self, repository: PatchManager.Locator, updateID: str, force: bool) -> vim.Task: ...
    def InstallV2(self, metaUrls: List[str], bundleUrls: List[str], vibUrls: List[str], spec: PatchManager.PatchManagerOperationSpec) -> vim.Task: ...
    def Uninstall(self, bulletinIds: List[str], spec: PatchManager.PatchManagerOperationSpec) -> vim.Task: ...
    def Query(self, spec: PatchManager.PatchManagerOperationSpec) -> vim.Task: ...


    class Locator(vmodl.DynamicData):
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value
        @property
        def proxy(self) -> str: ...
        @proxy.setter
        def proxy(self, value: str):
            self._proxy = value


    class PatchManagerOperationSpec(vmodl.DynamicData):
        @property
        def proxy(self) -> str: ...
        @proxy.setter
        def proxy(self, value: str):
            self._proxy = value
        @property
        def port(self) -> int: ...
        @port.setter
        def port(self, value: int):
            self._port = value
        @property
        def userName(self) -> str: ...
        @userName.setter
        def userName(self, value: str):
            self._userName = value
        @property
        def password(self) -> str: ...
        @password.setter
        def password(self, value: str):
            self._password = value
        @property
        def cmdOption(self) -> str: ...
        @cmdOption.setter
        def cmdOption(self, value: str):
            self._cmdOption = value


    class Result(vmodl.DynamicData):
        @property
        def version(self) -> str: ...
        @version.setter
        def version(self, value: str):
            self._version = value
        @property
        def status(self) -> List[PatchManager.Status]: ...
        @status.setter
        def status(self, value: List[PatchManager.Status]):
            self._status = value
        @property
        def xmlResult(self) -> str: ...
        @xmlResult.setter
        def xmlResult(self, value: str):
            self._xmlResult = value


    class Status(vmodl.DynamicData):
        @property
        def id(self) -> str: ...
        @id.setter
        def id(self, value: str):
            self._id = value
        @property
        def applicable(self) -> bool: ...
        @applicable.setter
        def applicable(self, value: bool):
            self._applicable = value
        @property
        def reason(self) -> List[str]: ...
        @reason.setter
        def reason(self, value: List[str]):
            self._reason = value
        @property
        def integrity(self) -> str: ...
        @integrity.setter
        def integrity(self, value: str):
            self._integrity = value
        @property
        def installed(self) -> bool: ...
        @installed.setter
        def installed(self, value: bool):
            self._installed = value
        @property
        def installState(self) -> List[str]: ...
        @installState.setter
        def installState(self, value: List[str]):
            self._installState = value
        @property
        def prerequisitePatch(self) -> List[PatchManager.Status.PrerequisitePatch]: ...
        @prerequisitePatch.setter
        def prerequisitePatch(self, value: List[PatchManager.Status.PrerequisitePatch]):
            self._prerequisitePatch = value
        @property
        def restartRequired(self) -> bool: ...
        @restartRequired.setter
        def restartRequired(self, value: bool):
            self._restartRequired = value
        @property
        def reconnectRequired(self) -> bool: ...
        @reconnectRequired.setter
        def reconnectRequired(self, value: bool):
            self._reconnectRequired = value
        @property
        def vmOffRequired(self) -> bool: ...
        @vmOffRequired.setter
        def vmOffRequired(self, value: bool):
            self._vmOffRequired = value
        @property
        def supersededPatchIds(self) -> List[str]: ...
        @supersededPatchIds.setter
        def supersededPatchIds(self, value: List[str]):
            self._supersededPatchIds = value


        class PrerequisitePatch(vmodl.DynamicData):
            @property
            def id(self) -> str: ...
            @id.setter
            def id(self, value: str):
                self._id = value
            @property
            def installState(self) -> List[str]: ...
            @installState.setter
            def installState(self, value: List[str]):
                self._installState = value


        class InstallState(Enum):
            hostRestarted = "hostRestarted"
            imageActive = "imageActive"


        class Integrity(Enum):
            validated = "validated"
            keyNotFound = "keyNotFound"
            keyRevoked = "keyRevoked"
            keyExpired = "keyExpired"
            digestMismatch = "digestMismatch"
            notEnoughSignatures = "notEnoughSignatures"
            validationError = "validationError"


        class Reason(Enum):
            obsoleted = "obsoleted"
            missingPatch = "missingPatch"
            missingLib = "missingLib"
            hasDependentPatch = "hasDependentPatch"
            conflictPatch = "conflictPatch"
            conflictLib = "conflictLib"


class PciPassthruSystem(vim.ExtensibleManagedObject):
    @property
    def pciPassthruInfo(self) -> List[PciPassthruInfo]: ...
    @property
    def sriovDevicePoolInfo(self) -> List[SriovDevicePoolInfo]: ...
    def Refresh(self) -> NoneType: ...
    def UpdatePassthruConfig(self, config: List[PciPassthruConfig]) -> NoneType: ...


class PowerSystem(ManagedObject):
    @property
    def capability(self) -> PowerSystem.Capability: ...
    @property
    def info(self) -> PowerSystem.Info: ...
    def ConfigurePolicy(self, key: int) -> NoneType: ...


    class Capability(vmodl.DynamicData):
        @property
        def availablePolicy(self) -> List[PowerSystem.PowerPolicy]: ...
        @availablePolicy.setter
        def availablePolicy(self, value: List[PowerSystem.PowerPolicy]):
            self._availablePolicy = value


    class Info(vmodl.DynamicData):
        @property
        def currentPolicy(self) -> PowerSystem.PowerPolicy: ...
        @currentPolicy.setter
        def currentPolicy(self, value: PowerSystem.PowerPolicy):
            self._currentPolicy = value


    class PowerPolicy(vmodl.DynamicData):
        @property
        def key(self) -> int: ...
        @key.setter
        def key(self, value: int):
            self._key = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def shortName(self) -> str: ...
        @shortName.setter
        def shortName(self, value: str):
            self._shortName = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value


class ServiceSystem(vim.ExtensibleManagedObject):
    @property
    def serviceInfo(self) -> ServiceInfo: ...
    def UpdatePolicy(self, id: str, policy: str) -> NoneType: ...
    def Start(self, id: str) -> NoneType: ...
    def Stop(self, id: str) -> NoneType: ...
    def Restart(self, id: str) -> NoneType: ...
    def Uninstall(self, id: str) -> NoneType: ...
    def Refresh(self) -> NoneType: ...


class SnmpSystem(ManagedObject):
    @property
    def configuration(self) -> SnmpSystem.SnmpConfigSpec: ...
    @property
    def limits(self) -> SnmpSystem.AgentLimits: ...
    def ReconfigureSnmpAgent(self, spec: SnmpSystem.SnmpConfigSpec) -> NoneType: ...
    def SendTestNotification(self) -> NoneType: ...


    class AgentLimits(vmodl.DynamicData):
        @property
        def maxReadOnlyCommunities(self) -> int: ...
        @maxReadOnlyCommunities.setter
        def maxReadOnlyCommunities(self, value: int):
            self._maxReadOnlyCommunities = value
        @property
        def maxTrapDestinations(self) -> int: ...
        @maxTrapDestinations.setter
        def maxTrapDestinations(self, value: int):
            self._maxTrapDestinations = value
        @property
        def maxCommunityLength(self) -> int: ...
        @maxCommunityLength.setter
        def maxCommunityLength(self, value: int):
            self._maxCommunityLength = value
        @property
        def maxBufferSize(self) -> int: ...
        @maxBufferSize.setter
        def maxBufferSize(self, value: int):
            self._maxBufferSize = value
        @property
        def capability(self) -> SnmpSystem.AgentLimits.Capability | Literal['COMPLETE', 'DIAGNOSTICS', 'CONFIGURATION']: ...
        @capability.setter
        def capability(self, value: SnmpSystem.AgentLimits.Capability | Literal['COMPLETE', 'DIAGNOSTICS', 'CONFIGURATION']):
            self._capability = value


        class Capability(Enum):
            COMPLETE = "COMPLETE"
            DIAGNOSTICS = "DIAGNOSTICS"
            CONFIGURATION = "CONFIGURATION"


    class SnmpConfigSpec(vmodl.DynamicData):
        @property
        def enabled(self) -> bool: ...
        @enabled.setter
        def enabled(self, value: bool):
            self._enabled = value
        @property
        def port(self) -> int: ...
        @port.setter
        def port(self, value: int):
            self._port = value
        @property
        def readOnlyCommunities(self) -> List[str]: ...
        @readOnlyCommunities.setter
        def readOnlyCommunities(self, value: List[str]):
            self._readOnlyCommunities = value
        @property
        def trapTargets(self) -> List[SnmpSystem.SnmpConfigSpec.Destination]: ...
        @trapTargets.setter
        def trapTargets(self, value: List[SnmpSystem.SnmpConfigSpec.Destination]):
            self._trapTargets = value
        @property
        def option(self) -> List[vim.KeyValue]: ...
        @option.setter
        def option(self, value: List[vim.KeyValue]):
            self._option = value


        class Destination(vmodl.DynamicData):
            @property
            def hostName(self) -> str: ...
            @hostName.setter
            def hostName(self, value: str):
                self._hostName = value
            @property
            def port(self) -> int: ...
            @port.setter
            def port(self, value: int):
                self._port = value
            @property
            def community(self) -> str: ...
            @community.setter
            def community(self, value: str):
                self._community = value


class StorageSystem(vim.ExtensibleManagedObject):
    @property
    def storageDeviceInfo(self) -> StorageDeviceInfo: ...
    @property
    def fileSystemVolumeInfo(self) -> FileSystemVolumeInfo: ...
    @property
    def systemFile(self) -> List[str]: ...
    @property
    def multipathStateInfo(self) -> MultipathStateInfo: ...
    def RetrieveDiskPartitionInfo(self, devicePath: List[str]) -> List[DiskPartitionInfo]: ...
    def ComputeDiskPartitionInfo(self, devicePath: str, layout: DiskPartitionInfo.Layout, partitionFormat: str) -> DiskPartitionInfo: ...
    def ComputeDiskPartitionInfoForResize(self, partition: ScsiDisk.Partition, blockRange: DiskPartitionInfo.BlockRange, partitionFormat: str) -> DiskPartitionInfo: ...
    def UpdateDiskPartitions(self, devicePath: str, spec: DiskPartitionInfo.Specification) -> NoneType: ...
    def FormatVmfs(self, createSpec: VmfsVolume.Specification) -> VmfsVolume: ...
    def MountVmfsVolume(self, vmfsUuid: str) -> NoneType: ...
    def UnmountVmfsVolume(self, vmfsUuid: str) -> NoneType: ...
    def UnmountVmfsVolumeEx(self, vmfsUuid: List[str]) -> vim.Task: ...
    def MountVmfsVolumeEx(self, vmfsUuid: List[str]) -> vim.Task: ...
    def UnmapVmfsVolumeEx(self, vmfsUuid: List[str]) -> vim.Task: ...
    def DeleteVmfsVolumeState(self, vmfsUuid: str) -> NoneType: ...
    def RescanVmfs(self) -> NoneType: ...
    def AttachVmfsExtent(self, vmfsPath: str, extent: ScsiDisk.Partition) -> NoneType: ...
    def ExpandVmfsExtent(self, vmfsPath: str, extent: ScsiDisk.Partition) -> NoneType: ...
    def UpgradeVmfs(self, vmfsPath: str) -> NoneType: ...
    def UpgradeVmLayout(self) -> NoneType: ...
    def QueryUnresolvedVmfsVolume(self) -> List[UnresolvedVmfsVolume]: ...
    def ResolveMultipleUnresolvedVmfsVolumes(self, resolutionSpec: List[UnresolvedVmfsResolutionSpec]) -> List[UnresolvedVmfsResolutionResult]: ...
    def ResolveMultipleUnresolvedVmfsVolumesEx(self, resolutionSpec: List[UnresolvedVmfsResolutionSpec]) -> vim.Task: ...
    def UnmountForceMountedVmfsVolume(self, vmfsUuid: str) -> NoneType: ...
    def RescanHba(self, hbaDevice: str) -> NoneType: ...
    def RescanAllHba(self) -> NoneType: ...
    def UpdateSoftwareInternetScsiEnabled(self, enabled: bool) -> NoneType: ...
    def UpdateInternetScsiDiscoveryProperties(self, iScsiHbaDevice: str, discoveryProperties: InternetScsiHba.DiscoveryProperties) -> NoneType: ...
    def UpdateInternetScsiAuthenticationProperties(self, iScsiHbaDevice: str, authenticationProperties: InternetScsiHba.AuthenticationProperties, targetSet: InternetScsiHba.TargetSet) -> NoneType: ...
    def UpdateInternetScsiDigestProperties(self, iScsiHbaDevice: str, targetSet: InternetScsiHba.TargetSet, digestProperties: InternetScsiHba.DigestProperties) -> NoneType: ...
    def UpdateInternetScsiAdvancedOptions(self, iScsiHbaDevice: str, targetSet: InternetScsiHba.TargetSet, options: List[InternetScsiHba.ParamValue]) -> NoneType: ...
    def UpdateInternetScsiIPProperties(self, iScsiHbaDevice: str, ipProperties: InternetScsiHba.IPProperties) -> NoneType: ...
    def UpdateInternetScsiName(self, iScsiHbaDevice: str, iScsiName: str) -> NoneType: ...
    def UpdateInternetScsiAlias(self, iScsiHbaDevice: str, iScsiAlias: str) -> NoneType: ...
    def AddInternetScsiSendTargets(self, iScsiHbaDevice: str, targets: List[InternetScsiHba.SendTarget]) -> NoneType: ...
    def RemoveInternetScsiSendTargets(self, iScsiHbaDevice: str, targets: List[InternetScsiHba.SendTarget], force: bool) -> NoneType: ...
    def AddInternetScsiStaticTargets(self, iScsiHbaDevice: str, targets: List[InternetScsiHba.StaticTarget]) -> NoneType: ...
    def RemoveInternetScsiStaticTargets(self, iScsiHbaDevice: str, targets: List[InternetScsiHba.StaticTarget]) -> NoneType: ...
    def EnableMultipathPath(self, pathName: str) -> NoneType: ...
    def DisableMultipathPath(self, pathName: str) -> NoneType: ...
    def SetMultipathLunPolicy(self, lunId: str, policy: MultipathInfo.LogicalUnitPolicy) -> NoneType: ...
    def UpdateHppMultipathLunPolicy(self, lunId: str, policy: MultipathInfo.HppLogicalUnitPolicy) -> NoneType: ...
    def QueryPathSelectionPolicyOptions(self) -> List[PathSelectionPolicyOption]: ...
    def QueryStorageArrayTypePolicyOptions(self) -> List[StorageArrayTypePolicyOption]: ...
    def UpdateScsiLunDisplayName(self, lunUuid: str, displayName: str) -> NoneType: ...
    def DetachScsiLun(self, lunUuid: str) -> NoneType: ...
    def DetachScsiLunEx(self, lunUuid: List[str]) -> vim.Task: ...
    def DeleteScsiLunState(self, lunCanonicalName: str) -> NoneType: ...
    def AttachScsiLun(self, lunUuid: str) -> NoneType: ...
    def AttachScsiLunEx(self, lunUuid: List[str]) -> vim.Task: ...
    def Refresh(self) -> NoneType: ...
    def DiscoverFcoeHbas(self, fcoeSpec: FcoeConfig.FcoeSpecification) -> NoneType: ...
    def MarkForRemoval(self, hbaName: str, remove: bool) -> NoneType: ...
    def FormatVffs(self, createSpec: VffsVolume.Specification) -> VffsVolume: ...
    def ExtendVffs(self, vffsPath: str, devicePath: str, spec: DiskPartitionInfo.Specification) -> NoneType: ...
    def DestroyVffs(self, vffsPath: str) -> NoneType: ...
    def MountVffsVolume(self, vffsUuid: str) -> NoneType: ...
    def UnmountVffsVolume(self, vffsUuid: str) -> NoneType: ...
    def DeleteVffsVolumeState(self, vffsUuid: str) -> NoneType: ...
    def RescanVffs(self) -> NoneType: ...
    def QueryAvailableSsds(self, vffsPath: str) -> List[ScsiDisk]: ...
    def SetNFSUser(self, user: str, password: str) -> NoneType: ...
    def ChangeNFSUserPassword(self, password: str) -> NoneType: ...
    def QueryNFSUser(self) -> NasVolume.UserInfo: ...
    def ClearNFSUser(self) -> NoneType: ...
    def TurnDiskLocatorLedOn(self, scsiDiskUuids: List[str]) -> vim.Task: ...
    def TurnDiskLocatorLedOff(self, scsiDiskUuids: List[str]) -> vim.Task: ...
    def MarkAsSsd(self, scsiDiskUuid: str) -> vim.Task: ...
    def MarkAsNonSsd(self, scsiDiskUuid: str) -> vim.Task: ...
    def MarkAsLocal(self, scsiDiskUuid: str) -> vim.Task: ...
    def MarkAsNonLocal(self, scsiDiskUuid: str) -> vim.Task: ...
    def UpdateVmfsUnmapPriority(self, vmfsUuid: str, unmapPriority: str) -> NoneType: ...
    def UpdateVmfsUnmapBandwidth(self, vmfsUuid: str, unmapBandwidthSpec: VmfsVolume.UnmapBandwidthSpec) -> NoneType: ...
    def QueryVmfsConfigOption(self) -> List[VmfsVolume.ConfigOption]: ...
    def MarkPerenniallyReserved(self, lunUuid: str, state: bool) -> NoneType: ...
    def MarkPerenniallyReservedEx(self, lunUuid: List[str], state: bool) -> vim.Task: ...
    def CreateNvmeOverRdmaAdapter(self, rdmaDeviceName: str) -> NoneType: ...
    def RemoveNvmeOverRdmaAdapter(self, hbaDeviceName: str) -> NoneType: ...
    def CreateSoftwareAdapter(self, spec: HbaCreateSpec) -> NoneType: ...
    def RemoveSoftwareAdapter(self, hbaDeviceName: str) -> NoneType: ...
    def DiscoverNvmeControllers(self, discoverSpec: NvmeDiscoverSpec) -> NvmeDiscoveryLog: ...
    def ConnectNvmeController(self, connectSpec: NvmeConnectSpec) -> NoneType: ...
    def DisconnectNvmeController(self, disconnectSpec: NvmeDisconnectSpec) -> NoneType: ...
    def ConnectNvmeControllerEx(self, connectSpec: List[NvmeConnectSpec]) -> vim.Task: ...
    def DisconnectNvmeControllerEx(self, disconnectSpec: List[NvmeDisconnectSpec]) -> vim.Task: ...


    class DiskLocatorLedResult(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


    class ScsiLunResult(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


    class VmfsVolumeResult(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


class VFlashManager(ManagedObject):
    @property
    def vFlashConfigInfo(self) -> VFlashManager.VFlashConfigInfo: ...
    def ConfigureVFlashResourceEx(self, devicePath: List[str]) -> vim.Task: ...
    def ConfigureVFlashResource(self, spec: VFlashManager.VFlashResourceConfigSpec) -> NoneType: ...
    def RemoveVFlashResource(self) -> NoneType: ...
    def ConfigureHostVFlashCache(self, spec: VFlashManager.VFlashCacheConfigSpec) -> NoneType: ...
    def GetVFlashModuleDefaultConfig(self, vFlashModule: str) -> vim.vm.device.VirtualDisk.VFlashCacheConfigInfo: ...


    class VFlashCacheConfigInfo(vmodl.DynamicData):
        @property
        def vFlashModuleConfigOption(self) -> List[VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption]: ...
        @vFlashModuleConfigOption.setter
        def vFlashModuleConfigOption(self, value: List[VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption]):
            self._vFlashModuleConfigOption = value
        @property
        def defaultVFlashModule(self) -> str: ...
        @defaultVFlashModule.setter
        def defaultVFlashModule(self, value: str):
            self._defaultVFlashModule = value
        @property
        def swapCacheReservationInGB(self) -> long: ...
        @swapCacheReservationInGB.setter
        def swapCacheReservationInGB(self, value: long):
            self._swapCacheReservationInGB = value


        class VFlashModuleConfigOption(vmodl.DynamicData):
            @property
            def vFlashModule(self) -> str: ...
            @vFlashModule.setter
            def vFlashModule(self, value: str):
                self._vFlashModule = value
            @property
            def vFlashModuleVersion(self) -> str: ...
            @vFlashModuleVersion.setter
            def vFlashModuleVersion(self, value: str):
                self._vFlashModuleVersion = value
            @property
            def minSupportedModuleVersion(self) -> str: ...
            @minSupportedModuleVersion.setter
            def minSupportedModuleVersion(self, value: str):
                self._minSupportedModuleVersion = value
            @property
            def cacheConsistencyType(self) -> vim.option.ChoiceOption: ...
            @cacheConsistencyType.setter
            def cacheConsistencyType(self, value: vim.option.ChoiceOption):
                self._cacheConsistencyType = value
            @property
            def cacheMode(self) -> vim.option.ChoiceOption: ...
            @cacheMode.setter
            def cacheMode(self, value: vim.option.ChoiceOption):
                self._cacheMode = value
            @property
            def blockSizeInKBOption(self) -> vim.option.LongOption: ...
            @blockSizeInKBOption.setter
            def blockSizeInKBOption(self, value: vim.option.LongOption):
                self._blockSizeInKBOption = value
            @property
            def reservationInMBOption(self) -> vim.option.LongOption: ...
            @reservationInMBOption.setter
            def reservationInMBOption(self, value: vim.option.LongOption):
                self._reservationInMBOption = value
            @property
            def maxDiskSizeInKB(self) -> long: ...
            @maxDiskSizeInKB.setter
            def maxDiskSizeInKB(self, value: long):
                self._maxDiskSizeInKB = value


    class VFlashCacheConfigSpec(vmodl.DynamicData):
        @property
        def defaultVFlashModule(self) -> str: ...
        @defaultVFlashModule.setter
        def defaultVFlashModule(self, value: str):
            self._defaultVFlashModule = value
        @property
        def swapCacheReservationInGB(self) -> long: ...
        @swapCacheReservationInGB.setter
        def swapCacheReservationInGB(self, value: long):
            self._swapCacheReservationInGB = value


    class VFlashConfigInfo(vmodl.DynamicData):
        @property
        def vFlashResourceConfigInfo(self) -> VFlashManager.VFlashResourceConfigInfo: ...
        @vFlashResourceConfigInfo.setter
        def vFlashResourceConfigInfo(self, value: VFlashManager.VFlashResourceConfigInfo):
            self._vFlashResourceConfigInfo = value
        @property
        def vFlashCacheConfigInfo(self) -> VFlashManager.VFlashCacheConfigInfo: ...
        @vFlashCacheConfigInfo.setter
        def vFlashCacheConfigInfo(self, value: VFlashManager.VFlashCacheConfigInfo):
            self._vFlashCacheConfigInfo = value


    class VFlashResourceConfigInfo(vmodl.DynamicData):
        @property
        def vffs(self) -> VffsVolume: ...
        @vffs.setter
        def vffs(self, value: VffsVolume):
            self._vffs = value
        @property
        def capacity(self) -> long: ...
        @capacity.setter
        def capacity(self, value: long):
            self._capacity = value


    class VFlashResourceConfigSpec(vmodl.DynamicData):
        @property
        def vffsUuid(self) -> str: ...
        @vffsUuid.setter
        def vffsUuid(self, value: str):
            self._vffsUuid = value


    class VFlashResourceRunTimeInfo(vmodl.DynamicData):
        @property
        def usage(self) -> long: ...
        @usage.setter
        def usage(self, value: long):
            self._usage = value
        @property
        def capacity(self) -> long: ...
        @capacity.setter
        def capacity(self, value: long):
            self._capacity = value
        @property
        def accessible(self) -> bool: ...
        @accessible.setter
        def accessible(self, value: bool):
            self._accessible = value
        @property
        def capacityForVmCache(self) -> long: ...
        @capacityForVmCache.setter
        def capacityForVmCache(self, value: long):
            self._capacityForVmCache = value
        @property
        def freeForVmCache(self) -> long: ...
        @freeForVmCache.setter
        def freeForVmCache(self, value: long):
            self._freeForVmCache = value


class VMotionSystem(vim.ExtensibleManagedObject):
    @property
    def netConfig(self) -> VMotionSystem.NetConfig: ...
    @property
    def ipConfig(self) -> IpConfig: ...
    def UpdateIpConfig(self, ipConfig: IpConfig) -> NoneType: ...
    def SelectVnic(self, device: str) -> NoneType: ...
    def DeselectVnic(self) -> NoneType: ...


    class NetConfig(vmodl.DynamicData):
        @property
        def candidateVnic(self) -> List[VirtualNic]: ...
        @candidateVnic.setter
        def candidateVnic(self, value: List[VirtualNic]):
            self._candidateVnic = value
        @property
        def selectedVnic(self) -> Link: ...
        @selectedVnic.setter
        def selectedVnic(self, value: Link):
            self._selectedVnic = value


class VirtualNicManager(vim.ExtensibleManagedObject):
    @property
    def info(self) -> VirtualNicManagerInfo: ...
    def QueryNetConfig(self, nicType: str) -> VirtualNicManager.NetConfig: ...
    def SelectVnic(self, nicType: str, device: str) -> NoneType: ...
    def DeselectVnic(self, nicType: str, device: str) -> NoneType: ...


    class NetConfig(vmodl.DynamicData):
        @property
        def nicType(self) -> str: ...
        @nicType.setter
        def nicType(self, value: str):
            self._nicType = value
        @property
        def multiSelectAllowed(self) -> bool: ...
        @multiSelectAllowed.setter
        def multiSelectAllowed(self, value: bool):
            self._multiSelectAllowed = value
        @property
        def candidateVnic(self) -> List[VirtualNic]: ...
        @candidateVnic.setter
        def candidateVnic(self, value: List[VirtualNic]):
            self._candidateVnic = value
        @property
        def selectedVnic(self) -> List[Link]: ...
        @selectedVnic.setter
        def selectedVnic(self, value: List[Link]):
            self._selectedVnic = value


    class NicTypeSelection(vmodl.DynamicData):
        @property
        def vnic(self) -> VirtualNicConnection: ...
        @vnic.setter
        def vnic(self, value: VirtualNicConnection):
            self._vnic = value
        @property
        def nicType(self) -> List[str]: ...
        @nicType.setter
        def nicType(self, value: List[str]):
            self._nicType = value


    class NicType(Enum):
        vmotion = "vmotion"
        faultToleranceLogging = "faultToleranceLogging"
        vSphereReplication = "vSphereReplication"
        vSphereReplicationNFC = "vSphereReplicationNFC"
        management = "management"
        vsan = "vsan"
        vSphereProvisioning = "vSphereProvisioning"
        vsanWitness = "vsanWitness"
        vSphereBackupNFC = "vSphereBackupNFC"
        ptp = "ptp"
        vsanReplication = "vsanReplication"
        nvmeTcp = "nvmeTcp"
        nvmeRdma = "nvmeRdma"


class VsanInternalSystem(ManagedObject):
    def QueryCmmds(self, queries: List[VsanInternalSystem.CmmdsQuery]) -> str: ...
    def QueryPhysicalVsanDisks(self, props: List[str]) -> str: ...
    def QueryVsanObjects(self, uuids: List[str]) -> str: ...
    def QueryObjectsOnPhysicalVsanDisk(self, disks: List[str]) -> str: ...
    def AbdicateDomOwnership(self, uuids: List[str]) -> List[str]: ...
    def QueryVsanStatistics(self, labels: List[str]) -> str: ...
    def ReconfigureDomObject(self, uuid: str, policy: str) -> NoneType: ...
    def QuerySyncingVsanObjects(self, uuids: List[str]) -> str: ...
    def RunVsanPhysicalDiskDiagnostics(self, disks: List[str]) -> List[VsanInternalSystem.VsanPhysicalDiskDiagnosticsResult]: ...
    def GetVsanObjExtAttrs(self, uuids: List[str]) -> str: ...
    def ReconfigurationSatisfiable(self, pcbs: List[VsanInternalSystem.PolicyChangeBatch], ignoreSatisfiability: bool) -> List[VsanInternalSystem.PolicySatisfiability]: ...
    def CanProvisionObjects(self, npbs: List[VsanInternalSystem.NewPolicyBatch], ignoreSatisfiability: bool) -> List[VsanInternalSystem.PolicySatisfiability]: ...
    def DeleteVsanObjects(self, uuids: List[str], force: bool) -> List[VsanInternalSystem.DeleteVsanObjectsResult]: ...
    def UpgradeVsanObjects(self, uuids: List[str], newVersion: int) -> List[VsanInternalSystem.VsanObjectOperationResult]: ...
    def QueryVsanObjectUuidsByFilter(self, uuids: List[str], limit: int, version: int) -> List[str]: ...


    class CmmdsQuery(vmodl.DynamicData):
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def owner(self) -> str: ...
        @owner.setter
        def owner(self, value: str):
            self._owner = value


    class DeleteVsanObjectsResult(vmodl.DynamicData):
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def success(self) -> bool: ...
        @success.setter
        def success(self, value: bool):
            self._success = value
        @property
        def failureReason(self) -> List[vmodl.LocalizableMessage]: ...
        @failureReason.setter
        def failureReason(self, value: List[vmodl.LocalizableMessage]):
            self._failureReason = value


    class NewPolicyBatch(vmodl.DynamicData):
        @property
        def size(self) -> List[long]: ...
        @size.setter
        def size(self, value: List[long]):
            self._size = value
        @property
        def policy(self) -> str: ...
        @policy.setter
        def policy(self, value: str):
            self._policy = value


    class PolicyChangeBatch(vmodl.DynamicData):
        @property
        def uuid(self) -> List[str]: ...
        @uuid.setter
        def uuid(self, value: List[str]):
            self._uuid = value
        @property
        def policy(self) -> str: ...
        @policy.setter
        def policy(self, value: str):
            self._policy = value


    class PolicyCost(vmodl.DynamicData):
        @property
        def changeDataSize(self) -> long: ...
        @changeDataSize.setter
        def changeDataSize(self, value: long):
            self._changeDataSize = value
        @property
        def currentDataSize(self) -> long: ...
        @currentDataSize.setter
        def currentDataSize(self, value: long):
            self._currentDataSize = value
        @property
        def tempDataSize(self) -> long: ...
        @tempDataSize.setter
        def tempDataSize(self, value: long):
            self._tempDataSize = value
        @property
        def copyDataSize(self) -> long: ...
        @copyDataSize.setter
        def copyDataSize(self, value: long):
            self._copyDataSize = value
        @property
        def changeFlashReadCacheSize(self) -> long: ...
        @changeFlashReadCacheSize.setter
        def changeFlashReadCacheSize(self, value: long):
            self._changeFlashReadCacheSize = value
        @property
        def currentFlashReadCacheSize(self) -> long: ...
        @currentFlashReadCacheSize.setter
        def currentFlashReadCacheSize(self, value: long):
            self._currentFlashReadCacheSize = value
        @property
        def currentDiskSpaceToAddressSpaceRatio(self) -> float: ...
        @currentDiskSpaceToAddressSpaceRatio.setter
        def currentDiskSpaceToAddressSpaceRatio(self, value: float):
            self._currentDiskSpaceToAddressSpaceRatio = value
        @property
        def diskSpaceToAddressSpaceRatio(self) -> float: ...
        @diskSpaceToAddressSpaceRatio.setter
        def diskSpaceToAddressSpaceRatio(self, value: float):
            self._diskSpaceToAddressSpaceRatio = value


    class PolicySatisfiability(vmodl.DynamicData):
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def isSatisfiable(self) -> bool: ...
        @isSatisfiable.setter
        def isSatisfiable(self, value: bool):
            self._isSatisfiable = value
        @property
        def reason(self) -> vmodl.LocalizableMessage: ...
        @reason.setter
        def reason(self, value: vmodl.LocalizableMessage):
            self._reason = value
        @property
        def cost(self) -> VsanInternalSystem.PolicyCost: ...
        @cost.setter
        def cost(self, value: VsanInternalSystem.PolicyCost):
            self._cost = value


    class VsanObjectOperationResult(vmodl.DynamicData):
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def failureReason(self) -> List[vmodl.LocalizableMessage]: ...
        @failureReason.setter
        def failureReason(self, value: List[vmodl.LocalizableMessage]):
            self._failureReason = value


    class VsanPhysicalDiskDiagnosticsResult(vmodl.DynamicData):
        @property
        def diskUuid(self) -> str: ...
        @diskUuid.setter
        def diskUuid(self, value: str):
            self._diskUuid = value
        @property
        def success(self) -> bool: ...
        @success.setter
        def success(self, value: bool):
            self._success = value
        @property
        def failureReason(self) -> str: ...
        @failureReason.setter
        def failureReason(self, value: str):
            self._failureReason = value


class VsanSystem(ManagedObject):
    @property
    def config(self) -> ConfigInfo: ...
    def QueryDisksForVsan(self, canonicalName: List[str]) -> List[DiskResult]: ...
    def AddDisks(self, disk: List[ScsiDisk]) -> vim.Task: ...
    def InitializeDisks(self, mapping: List[DiskMapping]) -> vim.Task: ...
    def RemoveDisk(self, disk: List[ScsiDisk], maintenanceSpec: MaintenanceSpec, timeout: int) -> vim.Task: ...
    def RemoveDiskMapping(self, mapping: List[DiskMapping], maintenanceSpec: MaintenanceSpec, timeout: int) -> vim.Task: ...
    def UnmountDiskMapping(self, mapping: List[DiskMapping]) -> vim.Task: ...
    def Update(self, config: ConfigInfo) -> vim.Task: ...
    def QueryHostStatus(self) -> ClusterStatus: ...
    def EvacuateNode(self, maintenanceSpec: MaintenanceSpec, timeout: int) -> vim.Task: ...
    def RecommissionNode(self) -> vim.Task: ...


class ActiveDirectoryInfo(DirectoryStoreInfo):
    @property
    def joinedDomain(self) -> str: ...
    @joinedDomain.setter
    def joinedDomain(self, value: str):
        self._joinedDomain = value
    @property
    def trustedDomain(self) -> List[str]: ...
    @trustedDomain.setter
    def trustedDomain(self, value: List[str]):
        self._trustedDomain = value
    @property
    def domainMembershipStatus(self) -> str: ...
    @domainMembershipStatus.setter
    def domainMembershipStatus(self, value: str):
        self._domainMembershipStatus = value
    @property
    def smartCardAuthenticationEnabled(self) -> bool: ...
    @smartCardAuthenticationEnabled.setter
    def smartCardAuthenticationEnabled(self, value: bool):
        self._smartCardAuthenticationEnabled = value


    class DomainMembershipStatus(Enum):
        unknown = "unknown"
        ok = "ok"
        noServers = "noServers"
        clientTrustBroken = "clientTrustBroken"
        serverTrustBroken = "serverTrustBroken"
        inconsistentTrust = "inconsistentTrust"
        otherProblem = "otherProblem"


class ActiveDirectorySpec(vmodl.DynamicData):
    @property
    def changeOperation(self) -> str: ...
    @changeOperation.setter
    def changeOperation(self, value: str):
        self._changeOperation = value
    @property
    def spec(self) -> ActiveDirectorySpec.Specification: ...
    @spec.setter
    def spec(self, value: ActiveDirectorySpec.Specification):
        self._spec = value


    class Specification(vmodl.DynamicData):
        @property
        def domainName(self) -> str: ...
        @domainName.setter
        def domainName(self, value: str):
            self._domainName = value
        @property
        def userName(self) -> str: ...
        @userName.setter
        def userName(self, value: str):
            self._userName = value
        @property
        def password(self) -> str: ...
        @password.setter
        def password(self, value: str):
            self._password = value
        @property
        def camServer(self) -> str: ...
        @camServer.setter
        def camServer(self, value: str):
            self._camServer = value
        @property
        def thumbprint(self) -> str: ...
        @thumbprint.setter
        def thumbprint(self, value: str):
            self._thumbprint = value
        @property
        def smartCardAuthenticationEnabled(self) -> bool: ...
        @smartCardAuthenticationEnabled.setter
        def smartCardAuthenticationEnabled(self, value: bool):
            self._smartCardAuthenticationEnabled = value
        @property
        def smartCardTrustAnchors(self) -> List[str]: ...
        @smartCardTrustAnchors.setter
        def smartCardTrustAnchors(self, value: List[str]):
            self._smartCardTrustAnchors = value


class AssignableHardwareBinding(vmodl.DynamicData):
    @property
    def instanceId(self) -> str: ...
    @instanceId.setter
    def instanceId(self, value: str):
        self._instanceId = value
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value


class AssignableHardwareConfig(vmodl.DynamicData):
    @property
    def attributeOverride(self) -> List[AssignableHardwareConfig.AttributeOverride]: ...
    @attributeOverride.setter
    def attributeOverride(self, value: List[AssignableHardwareConfig.AttributeOverride]):
        self._attributeOverride = value


    class AttributeOverride(vmodl.DynamicData):
        @property
        def instanceId(self) -> str: ...
        @instanceId.setter
        def instanceId(self, value: str):
            self._instanceId = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def value(self) -> object: ...
        @value.setter
        def value(self, value: object):
            self._value = value


class AuthenticationManagerInfo(vmodl.DynamicData):
    @property
    def authConfig(self) -> List[AuthenticationStoreInfo]: ...
    @authConfig.setter
    def authConfig(self, value: List[AuthenticationStoreInfo]):
        self._authConfig = value


class AuthenticationStoreInfo(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value


class BIOSInfo(vmodl.DynamicData):
    @property
    def biosVersion(self) -> str: ...
    @biosVersion.setter
    def biosVersion(self, value: str):
        self._biosVersion = value
    @property
    def releaseDate(self) -> datetime: ...
    @releaseDate.setter
    def releaseDate(self, value: datetime):
        self._releaseDate = value
    @property
    def vendor(self) -> str: ...
    @vendor.setter
    def vendor(self, value: str):
        self._vendor = value
    @property
    def majorRelease(self) -> int: ...
    @majorRelease.setter
    def majorRelease(self, value: int):
        self._majorRelease = value
    @property
    def minorRelease(self) -> int: ...
    @minorRelease.setter
    def minorRelease(self, value: int):
        self._minorRelease = value
    @property
    def firmwareMajorRelease(self) -> int: ...
    @firmwareMajorRelease.setter
    def firmwareMajorRelease(self, value: int):
        self._firmwareMajorRelease = value
    @property
    def firmwareMinorRelease(self) -> int: ...
    @firmwareMinorRelease.setter
    def firmwareMinorRelease(self, value: int):
        self._firmwareMinorRelease = value


class BlockAdapterTargetTransport(TargetTransport): ...


class BlockHba(HostBusAdapter): ...


class BootDeviceInfo(vmodl.DynamicData):
    @property
    def bootDevices(self) -> List[BootDeviceSystem.BootDevice]: ...
    @bootDevices.setter
    def bootDevices(self, value: List[BootDeviceSystem.BootDevice]):
        self._bootDevices = value
    @property
    def currentBootDeviceKey(self) -> str: ...
    @currentBootDeviceKey.setter
    def currentBootDeviceKey(self, value: str):
        self._currentBootDeviceKey = value


class Capability(vmodl.DynamicData):
    @property
    def recursiveResourcePoolsSupported(self) -> bool: ...
    @recursiveResourcePoolsSupported.setter
    def recursiveResourcePoolsSupported(self, value: bool):
        self._recursiveResourcePoolsSupported = value
    @property
    def cpuMemoryResourceConfigurationSupported(self) -> bool: ...
    @cpuMemoryResourceConfigurationSupported.setter
    def cpuMemoryResourceConfigurationSupported(self, value: bool):
        self._cpuMemoryResourceConfigurationSupported = value
    @property
    def rebootSupported(self) -> bool: ...
    @rebootSupported.setter
    def rebootSupported(self, value: bool):
        self._rebootSupported = value
    @property
    def shutdownSupported(self) -> bool: ...
    @shutdownSupported.setter
    def shutdownSupported(self, value: bool):
        self._shutdownSupported = value
    @property
    def vmotionSupported(self) -> bool: ...
    @vmotionSupported.setter
    def vmotionSupported(self, value: bool):
        self._vmotionSupported = value
    @property
    def standbySupported(self) -> bool: ...
    @standbySupported.setter
    def standbySupported(self, value: bool):
        self._standbySupported = value
    @property
    def ipmiSupported(self) -> bool: ...
    @ipmiSupported.setter
    def ipmiSupported(self, value: bool):
        self._ipmiSupported = value
    @property
    def maxSupportedVMs(self) -> int: ...
    @maxSupportedVMs.setter
    def maxSupportedVMs(self, value: int):
        self._maxSupportedVMs = value
    @property
    def maxRunningVMs(self) -> int: ...
    @maxRunningVMs.setter
    def maxRunningVMs(self, value: int):
        self._maxRunningVMs = value
    @property
    def maxSupportedVcpus(self) -> int: ...
    @maxSupportedVcpus.setter
    def maxSupportedVcpus(self, value: int):
        self._maxSupportedVcpus = value
    @property
    def maxRegisteredVMs(self) -> int: ...
    @maxRegisteredVMs.setter
    def maxRegisteredVMs(self, value: int):
        self._maxRegisteredVMs = value
    @property
    def datastorePrincipalSupported(self) -> bool: ...
    @datastorePrincipalSupported.setter
    def datastorePrincipalSupported(self, value: bool):
        self._datastorePrincipalSupported = value
    @property
    def sanSupported(self) -> bool: ...
    @sanSupported.setter
    def sanSupported(self, value: bool):
        self._sanSupported = value
    @property
    def nfsSupported(self) -> bool: ...
    @nfsSupported.setter
    def nfsSupported(self, value: bool):
        self._nfsSupported = value
    @property
    def iscsiSupported(self) -> bool: ...
    @iscsiSupported.setter
    def iscsiSupported(self, value: bool):
        self._iscsiSupported = value
    @property
    def vlanTaggingSupported(self) -> bool: ...
    @vlanTaggingSupported.setter
    def vlanTaggingSupported(self, value: bool):
        self._vlanTaggingSupported = value
    @property
    def nicTeamingSupported(self) -> bool: ...
    @nicTeamingSupported.setter
    def nicTeamingSupported(self, value: bool):
        self._nicTeamingSupported = value
    @property
    def highGuestMemSupported(self) -> bool: ...
    @highGuestMemSupported.setter
    def highGuestMemSupported(self, value: bool):
        self._highGuestMemSupported = value
    @property
    def maintenanceModeSupported(self) -> bool: ...
    @maintenanceModeSupported.setter
    def maintenanceModeSupported(self, value: bool):
        self._maintenanceModeSupported = value
    @property
    def suspendedRelocateSupported(self) -> bool: ...
    @suspendedRelocateSupported.setter
    def suspendedRelocateSupported(self, value: bool):
        self._suspendedRelocateSupported = value
    @property
    def restrictedSnapshotRelocateSupported(self) -> bool: ...
    @restrictedSnapshotRelocateSupported.setter
    def restrictedSnapshotRelocateSupported(self, value: bool):
        self._restrictedSnapshotRelocateSupported = value
    @property
    def perVmSwapFiles(self) -> bool: ...
    @perVmSwapFiles.setter
    def perVmSwapFiles(self, value: bool):
        self._perVmSwapFiles = value
    @property
    def localSwapDatastoreSupported(self) -> bool: ...
    @localSwapDatastoreSupported.setter
    def localSwapDatastoreSupported(self, value: bool):
        self._localSwapDatastoreSupported = value
    @property
    def unsharedSwapVMotionSupported(self) -> bool: ...
    @unsharedSwapVMotionSupported.setter
    def unsharedSwapVMotionSupported(self, value: bool):
        self._unsharedSwapVMotionSupported = value
    @property
    def backgroundSnapshotsSupported(self) -> bool: ...
    @backgroundSnapshotsSupported.setter
    def backgroundSnapshotsSupported(self, value: bool):
        self._backgroundSnapshotsSupported = value
    @property
    def preAssignedPCIUnitNumbersSupported(self) -> bool: ...
    @preAssignedPCIUnitNumbersSupported.setter
    def preAssignedPCIUnitNumbersSupported(self, value: bool):
        self._preAssignedPCIUnitNumbersSupported = value
    @property
    def screenshotSupported(self) -> bool: ...
    @screenshotSupported.setter
    def screenshotSupported(self, value: bool):
        self._screenshotSupported = value
    @property
    def scaledScreenshotSupported(self) -> bool: ...
    @scaledScreenshotSupported.setter
    def scaledScreenshotSupported(self, value: bool):
        self._scaledScreenshotSupported = value
    @property
    def storageVMotionSupported(self) -> bool: ...
    @storageVMotionSupported.setter
    def storageVMotionSupported(self, value: bool):
        self._storageVMotionSupported = value
    @property
    def vmotionWithStorageVMotionSupported(self) -> bool: ...
    @vmotionWithStorageVMotionSupported.setter
    def vmotionWithStorageVMotionSupported(self, value: bool):
        self._vmotionWithStorageVMotionSupported = value
    @property
    def vmotionAcrossNetworkSupported(self) -> bool: ...
    @vmotionAcrossNetworkSupported.setter
    def vmotionAcrossNetworkSupported(self, value: bool):
        self._vmotionAcrossNetworkSupported = value
    @property
    def maxNumDisksSVMotion(self) -> int: ...
    @maxNumDisksSVMotion.setter
    def maxNumDisksSVMotion(self, value: int):
        self._maxNumDisksSVMotion = value
    @property
    def maxVirtualDiskDescVersionSupported(self) -> int: ...
    @maxVirtualDiskDescVersionSupported.setter
    def maxVirtualDiskDescVersionSupported(self, value: int):
        self._maxVirtualDiskDescVersionSupported = value
    @property
    def hbrNicSelectionSupported(self) -> bool: ...
    @hbrNicSelectionSupported.setter
    def hbrNicSelectionSupported(self, value: bool):
        self._hbrNicSelectionSupported = value
    @property
    def vrNfcNicSelectionSupported(self) -> bool: ...
    @vrNfcNicSelectionSupported.setter
    def vrNfcNicSelectionSupported(self, value: bool):
        self._vrNfcNicSelectionSupported = value
    @property
    def recordReplaySupported(self) -> bool: ...
    @recordReplaySupported.setter
    def recordReplaySupported(self, value: bool):
        self._recordReplaySupported = value
    @property
    def ftSupported(self) -> bool: ...
    @ftSupported.setter
    def ftSupported(self, value: bool):
        self._ftSupported = value
    @property
    def replayUnsupportedReason(self) -> str: ...
    @replayUnsupportedReason.setter
    def replayUnsupportedReason(self, value: str):
        self._replayUnsupportedReason = value
    @property
    def replayCompatibilityIssues(self) -> List[str]: ...
    @replayCompatibilityIssues.setter
    def replayCompatibilityIssues(self, value: List[str]):
        self._replayCompatibilityIssues = value
    @property
    def smpFtSupported(self) -> bool: ...
    @smpFtSupported.setter
    def smpFtSupported(self, value: bool):
        self._smpFtSupported = value
    @property
    def ftCompatibilityIssues(self) -> List[str]: ...
    @ftCompatibilityIssues.setter
    def ftCompatibilityIssues(self, value: List[str]):
        self._ftCompatibilityIssues = value
    @property
    def smpFtCompatibilityIssues(self) -> List[str]: ...
    @smpFtCompatibilityIssues.setter
    def smpFtCompatibilityIssues(self, value: List[str]):
        self._smpFtCompatibilityIssues = value
    @property
    def maxVcpusPerFtVm(self) -> int: ...
    @maxVcpusPerFtVm.setter
    def maxVcpusPerFtVm(self, value: int):
        self._maxVcpusPerFtVm = value
    @property
    def loginBySSLThumbprintSupported(self) -> bool: ...
    @loginBySSLThumbprintSupported.setter
    def loginBySSLThumbprintSupported(self, value: bool):
        self._loginBySSLThumbprintSupported = value
    @property
    def cloneFromSnapshotSupported(self) -> bool: ...
    @cloneFromSnapshotSupported.setter
    def cloneFromSnapshotSupported(self, value: bool):
        self._cloneFromSnapshotSupported = value
    @property
    def deltaDiskBackingsSupported(self) -> bool: ...
    @deltaDiskBackingsSupported.setter
    def deltaDiskBackingsSupported(self, value: bool):
        self._deltaDiskBackingsSupported = value
    @property
    def perVMNetworkTrafficShapingSupported(self) -> bool: ...
    @perVMNetworkTrafficShapingSupported.setter
    def perVMNetworkTrafficShapingSupported(self, value: bool):
        self._perVMNetworkTrafficShapingSupported = value
    @property
    def tpmSupported(self) -> bool: ...
    @tpmSupported.setter
    def tpmSupported(self, value: bool):
        self._tpmSupported = value
    @property
    def tpmVersion(self) -> str: ...
    @tpmVersion.setter
    def tpmVersion(self, value: str):
        self._tpmVersion = value
    @property
    def txtEnabled(self) -> bool: ...
    @txtEnabled.setter
    def txtEnabled(self, value: bool):
        self._txtEnabled = value
    @property
    def supportedCpuFeature(self) -> List[CpuIdInfo]: ...
    @supportedCpuFeature.setter
    def supportedCpuFeature(self, value: List[CpuIdInfo]):
        self._supportedCpuFeature = value
    @property
    def virtualExecUsageSupported(self) -> bool: ...
    @virtualExecUsageSupported.setter
    def virtualExecUsageSupported(self, value: bool):
        self._virtualExecUsageSupported = value
    @property
    def storageIORMSupported(self) -> bool: ...
    @storageIORMSupported.setter
    def storageIORMSupported(self, value: bool):
        self._storageIORMSupported = value
    @property
    def vmDirectPathGen2Supported(self) -> bool: ...
    @vmDirectPathGen2Supported.setter
    def vmDirectPathGen2Supported(self, value: bool):
        self._vmDirectPathGen2Supported = value
    @property
    def vmDirectPathGen2UnsupportedReason(self) -> List[str]: ...
    @vmDirectPathGen2UnsupportedReason.setter
    def vmDirectPathGen2UnsupportedReason(self, value: List[str]):
        self._vmDirectPathGen2UnsupportedReason = value
    @property
    def vmDirectPathGen2UnsupportedReasonExtended(self) -> str: ...
    @vmDirectPathGen2UnsupportedReasonExtended.setter
    def vmDirectPathGen2UnsupportedReasonExtended(self, value: str):
        self._vmDirectPathGen2UnsupportedReasonExtended = value
    @property
    def supportedVmfsMajorVersion(self) -> List[int]: ...
    @supportedVmfsMajorVersion.setter
    def supportedVmfsMajorVersion(self, value: List[int]):
        self._supportedVmfsMajorVersion = value
    @property
    def vStorageCapable(self) -> bool: ...
    @vStorageCapable.setter
    def vStorageCapable(self, value: bool):
        self._vStorageCapable = value
    @property
    def snapshotRelayoutSupported(self) -> bool: ...
    @snapshotRelayoutSupported.setter
    def snapshotRelayoutSupported(self, value: bool):
        self._snapshotRelayoutSupported = value
    @property
    def firewallIpRulesSupported(self) -> bool: ...
    @firewallIpRulesSupported.setter
    def firewallIpRulesSupported(self, value: bool):
        self._firewallIpRulesSupported = value
    @property
    def servicePackageInfoSupported(self) -> bool: ...
    @servicePackageInfoSupported.setter
    def servicePackageInfoSupported(self, value: bool):
        self._servicePackageInfoSupported = value
    @property
    def maxHostRunningVms(self) -> int: ...
    @maxHostRunningVms.setter
    def maxHostRunningVms(self, value: int):
        self._maxHostRunningVms = value
    @property
    def maxHostSupportedVcpus(self) -> int: ...
    @maxHostSupportedVcpus.setter
    def maxHostSupportedVcpus(self, value: int):
        self._maxHostSupportedVcpus = value
    @property
    def vmfsDatastoreMountCapable(self) -> bool: ...
    @vmfsDatastoreMountCapable.setter
    def vmfsDatastoreMountCapable(self, value: bool):
        self._vmfsDatastoreMountCapable = value
    @property
    def eightPlusHostVmfsSharedAccessSupported(self) -> bool: ...
    @eightPlusHostVmfsSharedAccessSupported.setter
    def eightPlusHostVmfsSharedAccessSupported(self, value: bool):
        self._eightPlusHostVmfsSharedAccessSupported = value
    @property
    def nestedHVSupported(self) -> bool: ...
    @nestedHVSupported.setter
    def nestedHVSupported(self, value: bool):
        self._nestedHVSupported = value
    @property
    def vPMCSupported(self) -> bool: ...
    @vPMCSupported.setter
    def vPMCSupported(self, value: bool):
        self._vPMCSupported = value
    @property
    def interVMCommunicationThroughVMCISupported(self) -> bool: ...
    @interVMCommunicationThroughVMCISupported.setter
    def interVMCommunicationThroughVMCISupported(self, value: bool):
        self._interVMCommunicationThroughVMCISupported = value
    @property
    def scheduledHardwareUpgradeSupported(self) -> bool: ...
    @scheduledHardwareUpgradeSupported.setter
    def scheduledHardwareUpgradeSupported(self, value: bool):
        self._scheduledHardwareUpgradeSupported = value
    @property
    def featureCapabilitiesSupported(self) -> bool: ...
    @featureCapabilitiesSupported.setter
    def featureCapabilitiesSupported(self, value: bool):
        self._featureCapabilitiesSupported = value
    @property
    def latencySensitivitySupported(self) -> bool: ...
    @latencySensitivitySupported.setter
    def latencySensitivitySupported(self, value: bool):
        self._latencySensitivitySupported = value
    @property
    def storagePolicySupported(self) -> bool: ...
    @storagePolicySupported.setter
    def storagePolicySupported(self, value: bool):
        self._storagePolicySupported = value
    @property
    def accel3dSupported(self) -> bool: ...
    @accel3dSupported.setter
    def accel3dSupported(self, value: bool):
        self._accel3dSupported = value
    @property
    def reliableMemoryAware(self) -> bool: ...
    @reliableMemoryAware.setter
    def reliableMemoryAware(self, value: bool):
        self._reliableMemoryAware = value
    @property
    def multipleNetworkStackInstanceSupported(self) -> bool: ...
    @multipleNetworkStackInstanceSupported.setter
    def multipleNetworkStackInstanceSupported(self, value: bool):
        self._multipleNetworkStackInstanceSupported = value
    @property
    def messageBusProxySupported(self) -> bool: ...
    @messageBusProxySupported.setter
    def messageBusProxySupported(self, value: bool):
        self._messageBusProxySupported = value
    @property
    def vsanSupported(self) -> bool: ...
    @vsanSupported.setter
    def vsanSupported(self, value: bool):
        self._vsanSupported = value
    @property
    def vFlashSupported(self) -> bool: ...
    @vFlashSupported.setter
    def vFlashSupported(self, value: bool):
        self._vFlashSupported = value
    @property
    def hostAccessManagerSupported(self) -> bool: ...
    @hostAccessManagerSupported.setter
    def hostAccessManagerSupported(self, value: bool):
        self._hostAccessManagerSupported = value
    @property
    def provisioningNicSelectionSupported(self) -> bool: ...
    @provisioningNicSelectionSupported.setter
    def provisioningNicSelectionSupported(self, value: bool):
        self._provisioningNicSelectionSupported = value
    @property
    def nfs41Supported(self) -> bool: ...
    @nfs41Supported.setter
    def nfs41Supported(self, value: bool):
        self._nfs41Supported = value
    @property
    def nfs41Krb5iSupported(self) -> bool: ...
    @nfs41Krb5iSupported.setter
    def nfs41Krb5iSupported(self, value: bool):
        self._nfs41Krb5iSupported = value
    @property
    def turnDiskLocatorLedSupported(self) -> bool: ...
    @turnDiskLocatorLedSupported.setter
    def turnDiskLocatorLedSupported(self, value: bool):
        self._turnDiskLocatorLedSupported = value
    @property
    def virtualVolumeDatastoreSupported(self) -> bool: ...
    @virtualVolumeDatastoreSupported.setter
    def virtualVolumeDatastoreSupported(self, value: bool):
        self._virtualVolumeDatastoreSupported = value
    @property
    def markAsSsdSupported(self) -> bool: ...
    @markAsSsdSupported.setter
    def markAsSsdSupported(self, value: bool):
        self._markAsSsdSupported = value
    @property
    def markAsLocalSupported(self) -> bool: ...
    @markAsLocalSupported.setter
    def markAsLocalSupported(self, value: bool):
        self._markAsLocalSupported = value
    @property
    def smartCardAuthenticationSupported(self) -> bool: ...
    @smartCardAuthenticationSupported.setter
    def smartCardAuthenticationSupported(self, value: bool):
        self._smartCardAuthenticationSupported = value
    @property
    def pMemSupported(self) -> bool: ...
    @pMemSupported.setter
    def pMemSupported(self, value: bool):
        self._pMemSupported = value
    @property
    def pMemSnapshotSupported(self) -> bool: ...
    @pMemSnapshotSupported.setter
    def pMemSnapshotSupported(self, value: bool):
        self._pMemSnapshotSupported = value
    @property
    def cryptoSupported(self) -> bool: ...
    @cryptoSupported.setter
    def cryptoSupported(self, value: bool):
        self._cryptoSupported = value
    @property
    def oneKVolumeAPIsSupported(self) -> bool: ...
    @oneKVolumeAPIsSupported.setter
    def oneKVolumeAPIsSupported(self, value: bool):
        self._oneKVolumeAPIsSupported = value
    @property
    def gatewayOnNicSupported(self) -> bool: ...
    @gatewayOnNicSupported.setter
    def gatewayOnNicSupported(self, value: bool):
        self._gatewayOnNicSupported = value
    @property
    def upitSupported(self) -> bool: ...
    @upitSupported.setter
    def upitSupported(self, value: bool):
        self._upitSupported = value
    @property
    def cpuHwMmuSupported(self) -> bool: ...
    @cpuHwMmuSupported.setter
    def cpuHwMmuSupported(self, value: bool):
        self._cpuHwMmuSupported = value
    @property
    def encryptedVMotionSupported(self) -> bool: ...
    @encryptedVMotionSupported.setter
    def encryptedVMotionSupported(self, value: bool):
        self._encryptedVMotionSupported = value
    @property
    def encryptionChangeOnAddRemoveSupported(self) -> bool: ...
    @encryptionChangeOnAddRemoveSupported.setter
    def encryptionChangeOnAddRemoveSupported(self, value: bool):
        self._encryptionChangeOnAddRemoveSupported = value
    @property
    def encryptionHotOperationSupported(self) -> bool: ...
    @encryptionHotOperationSupported.setter
    def encryptionHotOperationSupported(self, value: bool):
        self._encryptionHotOperationSupported = value
    @property
    def encryptionWithSnapshotsSupported(self) -> bool: ...
    @encryptionWithSnapshotsSupported.setter
    def encryptionWithSnapshotsSupported(self, value: bool):
        self._encryptionWithSnapshotsSupported = value
    @property
    def encryptionFaultToleranceSupported(self) -> bool: ...
    @encryptionFaultToleranceSupported.setter
    def encryptionFaultToleranceSupported(self, value: bool):
        self._encryptionFaultToleranceSupported = value
    @property
    def encryptionMemorySaveSupported(self) -> bool: ...
    @encryptionMemorySaveSupported.setter
    def encryptionMemorySaveSupported(self, value: bool):
        self._encryptionMemorySaveSupported = value
    @property
    def encryptionRDMSupported(self) -> bool: ...
    @encryptionRDMSupported.setter
    def encryptionRDMSupported(self, value: bool):
        self._encryptionRDMSupported = value
    @property
    def encryptionVFlashSupported(self) -> bool: ...
    @encryptionVFlashSupported.setter
    def encryptionVFlashSupported(self, value: bool):
        self._encryptionVFlashSupported = value
    @property
    def encryptionCBRCSupported(self) -> bool: ...
    @encryptionCBRCSupported.setter
    def encryptionCBRCSupported(self, value: bool):
        self._encryptionCBRCSupported = value
    @property
    def encryptionHBRSupported(self) -> bool: ...
    @encryptionHBRSupported.setter
    def encryptionHBRSupported(self, value: bool):
        self._encryptionHBRSupported = value
    @property
    def ftEfiSupported(self) -> bool: ...
    @ftEfiSupported.setter
    def ftEfiSupported(self, value: bool):
        self._ftEfiSupported = value
    @property
    def unmapMethodSupported(self) -> str: ...
    @unmapMethodSupported.setter
    def unmapMethodSupported(self, value: str):
        self._unmapMethodSupported = value
    @property
    def maxMemMBPerFtVm(self) -> int: ...
    @maxMemMBPerFtVm.setter
    def maxMemMBPerFtVm(self, value: int):
        self._maxMemMBPerFtVm = value
    @property
    def virtualMmuUsageIgnored(self) -> bool: ...
    @virtualMmuUsageIgnored.setter
    def virtualMmuUsageIgnored(self, value: bool):
        self._virtualMmuUsageIgnored = value
    @property
    def virtualExecUsageIgnored(self) -> bool: ...
    @virtualExecUsageIgnored.setter
    def virtualExecUsageIgnored(self, value: bool):
        self._virtualExecUsageIgnored = value
    @property
    def vmCreateDateSupported(self) -> bool: ...
    @vmCreateDateSupported.setter
    def vmCreateDateSupported(self, value: bool):
        self._vmCreateDateSupported = value
    @property
    def vmfs3EOLSupported(self) -> bool: ...
    @vmfs3EOLSupported.setter
    def vmfs3EOLSupported(self, value: bool):
        self._vmfs3EOLSupported = value
    @property
    def ftVmcpSupported(self) -> bool: ...
    @ftVmcpSupported.setter
    def ftVmcpSupported(self, value: bool):
        self._ftVmcpSupported = value
    @property
    def quickBootSupported(self) -> bool: ...
    @quickBootSupported.setter
    def quickBootSupported(self, value: bool):
        self._quickBootSupported = value
    @property
    def encryptedFtSupported(self) -> bool: ...
    @encryptedFtSupported.setter
    def encryptedFtSupported(self, value: bool):
        self._encryptedFtSupported = value
    @property
    def assignableHardwareSupported(self) -> bool: ...
    @assignableHardwareSupported.setter
    def assignableHardwareSupported(self, value: bool):
        self._assignableHardwareSupported = value
    @property
    def suspendToMemorySupported(self) -> bool: ...
    @suspendToMemorySupported.setter
    def suspendToMemorySupported(self, value: bool):
        self._suspendToMemorySupported = value
    @property
    def useFeatureReqsForOldHWv(self) -> bool: ...
    @useFeatureReqsForOldHWv.setter
    def useFeatureReqsForOldHWv(self, value: bool):
        self._useFeatureReqsForOldHWv = value
    @property
    def markPerenniallyReservedSupported(self) -> bool: ...
    @markPerenniallyReservedSupported.setter
    def markPerenniallyReservedSupported(self, value: bool):
        self._markPerenniallyReservedSupported = value
    @property
    def hppPspSupported(self) -> bool: ...
    @hppPspSupported.setter
    def hppPspSupported(self, value: bool):
        self._hppPspSupported = value
    @property
    def deviceRebindWithoutRebootSupported(self) -> bool: ...
    @deviceRebindWithoutRebootSupported.setter
    def deviceRebindWithoutRebootSupported(self, value: bool):
        self._deviceRebindWithoutRebootSupported = value
    @property
    def storagePolicyChangeSupported(self) -> bool: ...
    @storagePolicyChangeSupported.setter
    def storagePolicyChangeSupported(self, value: bool):
        self._storagePolicyChangeSupported = value
    @property
    def precisionTimeProtocolSupported(self) -> bool: ...
    @precisionTimeProtocolSupported.setter
    def precisionTimeProtocolSupported(self, value: bool):
        self._precisionTimeProtocolSupported = value
    @property
    def remoteDeviceVMotionSupported(self) -> bool: ...
    @remoteDeviceVMotionSupported.setter
    def remoteDeviceVMotionSupported(self, value: bool):
        self._remoteDeviceVMotionSupported = value
    @property
    def maxSupportedVmMemory(self) -> int: ...
    @maxSupportedVmMemory.setter
    def maxSupportedVmMemory(self, value: int):
        self._maxSupportedVmMemory = value
    @property
    def ahDeviceHintsSupported(self) -> bool: ...
    @ahDeviceHintsSupported.setter
    def ahDeviceHintsSupported(self, value: bool):
        self._ahDeviceHintsSupported = value
    @property
    def nvmeOverTcpSupported(self) -> bool: ...
    @nvmeOverTcpSupported.setter
    def nvmeOverTcpSupported(self, value: bool):
        self._nvmeOverTcpSupported = value
    @property
    def nvmeStorageFabricServicesSupported(self) -> bool: ...
    @nvmeStorageFabricServicesSupported.setter
    def nvmeStorageFabricServicesSupported(self, value: bool):
        self._nvmeStorageFabricServicesSupported = value
    @property
    def assignHwPciConfigSupported(self) -> bool: ...
    @assignHwPciConfigSupported.setter
    def assignHwPciConfigSupported(self, value: bool):
        self._assignHwPciConfigSupported = value
    @property
    def timeConfigSupported(self) -> bool: ...
    @timeConfigSupported.setter
    def timeConfigSupported(self, value: bool):
        self._timeConfigSupported = value
    @property
    def nvmeBatchOperationsSupported(self) -> bool: ...
    @nvmeBatchOperationsSupported.setter
    def nvmeBatchOperationsSupported(self, value: bool):
        self._nvmeBatchOperationsSupported = value
    @property
    def pMemFailoverSupported(self) -> bool: ...
    @pMemFailoverSupported.setter
    def pMemFailoverSupported(self, value: bool):
        self._pMemFailoverSupported = value
    @property
    def hostConfigEncryptionSupported(self) -> bool: ...
    @hostConfigEncryptionSupported.setter
    def hostConfigEncryptionSupported(self, value: bool):
        self._hostConfigEncryptionSupported = value
    @property
    def maxSupportedSimultaneousThreads(self) -> int: ...
    @maxSupportedSimultaneousThreads.setter
    def maxSupportedSimultaneousThreads(self, value: int):
        self._maxSupportedSimultaneousThreads = value
    @property
    def ptpConfigSupported(self) -> bool: ...
    @ptpConfigSupported.setter
    def ptpConfigSupported(self, value: bool):
        self._ptpConfigSupported = value
    @property
    def maxSupportedPtpPorts(self) -> int: ...
    @maxSupportedPtpPorts.setter
    def maxSupportedPtpPorts(self, value: int):
        self._maxSupportedPtpPorts = value
    @property
    def sgxRegistrationSupported(self) -> bool: ...
    @sgxRegistrationSupported.setter
    def sgxRegistrationSupported(self, value: bool):
        self._sgxRegistrationSupported = value
    @property
    def pMemIndependentSnapshotSupported(self) -> bool: ...
    @pMemIndependentSnapshotSupported.setter
    def pMemIndependentSnapshotSupported(self, value: bool):
        self._pMemIndependentSnapshotSupported = value
    @property
    def iommuSLDirtyCapable(self) -> bool: ...
    @iommuSLDirtyCapable.setter
    def iommuSLDirtyCapable(self, value: bool):
        self._iommuSLDirtyCapable = value
    @property
    def vmknicBindingSupported(self) -> bool: ...
    @vmknicBindingSupported.setter
    def vmknicBindingSupported(self, value: bool):
        self._vmknicBindingSupported = value
    @property
    def ultralowFixedUnmapSupported(self) -> bool: ...
    @ultralowFixedUnmapSupported.setter
    def ultralowFixedUnmapSupported(self, value: bool):
        self._ultralowFixedUnmapSupported = value
    @property
    def nvmeVvolSupported(self) -> bool: ...
    @nvmeVvolSupported.setter
    def nvmeVvolSupported(self, value: bool):
        self._nvmeVvolSupported = value
    @property
    def fptHotplugSupported(self) -> bool: ...
    @fptHotplugSupported.setter
    def fptHotplugSupported(self, value: bool):
        self._fptHotplugSupported = value
    @property
    def mconnectSupported(self) -> bool: ...
    @mconnectSupported.setter
    def mconnectSupported(self, value: bool):
        self._mconnectSupported = value


    class FtUnsupportedReason(Enum):
        vMotionNotLicensed = "vMotionNotLicensed"
        missingVMotionNic = "missingVMotionNic"
        missingFTLoggingNic = "missingFTLoggingNic"
        ftNotLicensed = "ftNotLicensed"
        haAgentIssue = "haAgentIssue"
        unsupportedProduct = "unsupportedProduct"
        cpuHvUnsupported = "cpuHvUnsupported"
        cpuHwmmuUnsupported = "cpuHwmmuUnsupported"
        cpuHvDisabled = "cpuHvDisabled"


    class ReplayUnsupportedReason(Enum):
        incompatibleProduct = "incompatibleProduct"
        incompatibleCpu = "incompatibleCpu"
        hvDisabled = "hvDisabled"
        cpuidLimitSet = "cpuidLimitSet"
        oldBIOS = "oldBIOS"
        unknown = "unknown"


    class UnmapMethodSupported(Enum):
        priority = "priority"
        fixed = "fixed"
        dynamic = "dynamic"


    class VmDirectPathGen2UnsupportedReason(Enum):
        hostNptIncompatibleProduct = "hostNptIncompatibleProduct"
        hostNptIncompatibleHardware = "hostNptIncompatibleHardware"
        hostNptDisabled = "hostNptDisabled"


class ConfigChange(vmodl.DynamicData):


    class Mode(Enum):
        modify = "modify"
        replace = "replace"


    class Operation(Enum):
        add = "add"
        remove = "remove"
        edit = "edit"
        ignore = "ignore"


class ConfigInfo(vmodl.DynamicData):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def product(self) -> vim.AboutInfo: ...
    @product.setter
    def product(self, value: vim.AboutInfo):
        self._product = value
    @property
    def deploymentInfo(self) -> DeploymentInfo: ...
    @deploymentInfo.setter
    def deploymentInfo(self, value: DeploymentInfo):
        self._deploymentInfo = value
    @property
    def hyperThread(self) -> CpuSchedulerSystem.HyperThreadScheduleInfo: ...
    @hyperThread.setter
    def hyperThread(self, value: CpuSchedulerSystem.HyperThreadScheduleInfo):
        self._hyperThread = value
    @property
    def consoleReservation(self) -> MemoryManagerSystem.ServiceConsoleReservationInfo: ...
    @consoleReservation.setter
    def consoleReservation(self, value: MemoryManagerSystem.ServiceConsoleReservationInfo):
        self._consoleReservation = value
    @property
    def virtualMachineReservation(self) -> MemoryManagerSystem.VirtualMachineReservationInfo: ...
    @virtualMachineReservation.setter
    def virtualMachineReservation(self, value: MemoryManagerSystem.VirtualMachineReservationInfo):
        self._virtualMachineReservation = value
    @property
    def storageDevice(self) -> StorageDeviceInfo: ...
    @storageDevice.setter
    def storageDevice(self, value: StorageDeviceInfo):
        self._storageDevice = value
    @property
    def multipathState(self) -> MultipathStateInfo: ...
    @multipathState.setter
    def multipathState(self, value: MultipathStateInfo):
        self._multipathState = value
    @property
    def fileSystemVolume(self) -> FileSystemVolumeInfo: ...
    @fileSystemVolume.setter
    def fileSystemVolume(self, value: FileSystemVolumeInfo):
        self._fileSystemVolume = value
    @property
    def systemFile(self) -> List[str]: ...
    @systemFile.setter
    def systemFile(self, value: List[str]):
        self._systemFile = value
    @property
    def network(self) -> NetworkInfo: ...
    @network.setter
    def network(self, value: NetworkInfo):
        self._network = value
    @property
    def vmotion(self) -> VMotionInfo: ...
    @vmotion.setter
    def vmotion(self, value: VMotionInfo):
        self._vmotion = value
    @property
    def virtualNicManagerInfo(self) -> VirtualNicManagerInfo: ...
    @virtualNicManagerInfo.setter
    def virtualNicManagerInfo(self, value: VirtualNicManagerInfo):
        self._virtualNicManagerInfo = value
    @property
    def capabilities(self) -> NetCapabilities: ...
    @capabilities.setter
    def capabilities(self, value: NetCapabilities):
        self._capabilities = value
    @property
    def datastoreCapabilities(self) -> DatastoreSystem.Capabilities: ...
    @datastoreCapabilities.setter
    def datastoreCapabilities(self, value: DatastoreSystem.Capabilities):
        self._datastoreCapabilities = value
    @property
    def offloadCapabilities(self) -> NetOffloadCapabilities: ...
    @offloadCapabilities.setter
    def offloadCapabilities(self, value: NetOffloadCapabilities):
        self._offloadCapabilities = value
    @property
    def service(self) -> ServiceInfo: ...
    @service.setter
    def service(self, value: ServiceInfo):
        self._service = value
    @property
    def firewall(self) -> FirewallInfo: ...
    @firewall.setter
    def firewall(self, value: FirewallInfo):
        self._firewall = value
    @property
    def autoStart(self) -> AutoStartManager.Config: ...
    @autoStart.setter
    def autoStart(self, value: AutoStartManager.Config):
        self._autoStart = value
    @property
    def activeDiagnosticPartition(self) -> DiagnosticPartition: ...
    @activeDiagnosticPartition.setter
    def activeDiagnosticPartition(self, value: DiagnosticPartition):
        self._activeDiagnosticPartition = value
    @property
    def option(self) -> List[vim.option.OptionValue]: ...
    @option.setter
    def option(self, value: List[vim.option.OptionValue]):
        self._option = value
    @property
    def optionDef(self) -> List[vim.option.OptionDef]: ...
    @optionDef.setter
    def optionDef(self, value: List[vim.option.OptionDef]):
        self._optionDef = value
    @property
    def datastorePrincipal(self) -> str: ...
    @datastorePrincipal.setter
    def datastorePrincipal(self, value: str):
        self._datastorePrincipal = value
    @property
    def localSwapDatastore(self) -> vim.Datastore: ...
    @localSwapDatastore.setter
    def localSwapDatastore(self, value: vim.Datastore):
        self._localSwapDatastore = value
    @property
    def systemSwapConfiguration(self) -> SystemSwapConfiguration: ...
    @systemSwapConfiguration.setter
    def systemSwapConfiguration(self, value: SystemSwapConfiguration):
        self._systemSwapConfiguration = value
    @property
    def systemResources(self) -> SystemResourceInfo: ...
    @systemResources.setter
    def systemResources(self, value: SystemResourceInfo):
        self._systemResources = value
    @property
    def dateTimeInfo(self) -> DateTimeInfo: ...
    @dateTimeInfo.setter
    def dateTimeInfo(self, value: DateTimeInfo):
        self._dateTimeInfo = value
    @property
    def flags(self) -> FlagInfo: ...
    @flags.setter
    def flags(self, value: FlagInfo):
        self._flags = value
    @property
    def adminDisabled(self) -> bool: ...
    @adminDisabled.setter
    def adminDisabled(self, value: bool):
        self._adminDisabled = value
    @property
    def lockdownMode(self) -> HostAccessManager.LockdownMode | Literal['lockdownDisabled', 'lockdownNormal', 'lockdownStrict']: ...
    @lockdownMode.setter
    def lockdownMode(self, value: HostAccessManager.LockdownMode | Literal['lockdownDisabled', 'lockdownNormal', 'lockdownStrict']):
        self._lockdownMode = value
    @property
    def ipmi(self) -> IpmiInfo: ...
    @ipmi.setter
    def ipmi(self, value: IpmiInfo):
        self._ipmi = value
    @property
    def sslThumbprintInfo(self) -> SslThumbprintInfo: ...
    @sslThumbprintInfo.setter
    def sslThumbprintInfo(self, value: SslThumbprintInfo):
        self._sslThumbprintInfo = value
    @property
    def sslThumbprintData(self) -> List[SslThumbprintInfo]: ...
    @sslThumbprintData.setter
    def sslThumbprintData(self, value: List[SslThumbprintInfo]):
        self._sslThumbprintData = value
    @property
    def certificate(self) -> List[byte]: ...
    @certificate.setter
    def certificate(self, value: List[byte]):
        self._certificate = value
    @property
    def pciPassthruInfo(self) -> List[PciPassthruInfo]: ...
    @pciPassthruInfo.setter
    def pciPassthruInfo(self, value: List[PciPassthruInfo]):
        self._pciPassthruInfo = value
    @property
    def authenticationManagerInfo(self) -> AuthenticationManagerInfo: ...
    @authenticationManagerInfo.setter
    def authenticationManagerInfo(self, value: AuthenticationManagerInfo):
        self._authenticationManagerInfo = value
    @property
    def featureVersion(self) -> List[FeatureVersionInfo]: ...
    @featureVersion.setter
    def featureVersion(self, value: List[FeatureVersionInfo]):
        self._featureVersion = value
    @property
    def powerSystemCapability(self) -> PowerSystem.Capability: ...
    @powerSystemCapability.setter
    def powerSystemCapability(self, value: PowerSystem.Capability):
        self._powerSystemCapability = value
    @property
    def powerSystemInfo(self) -> PowerSystem.Info: ...
    @powerSystemInfo.setter
    def powerSystemInfo(self, value: PowerSystem.Info):
        self._powerSystemInfo = value
    @property
    def cacheConfigurationInfo(self) -> List[CacheConfigurationManager.CacheConfigurationInfo]: ...
    @cacheConfigurationInfo.setter
    def cacheConfigurationInfo(self, value: List[CacheConfigurationManager.CacheConfigurationInfo]):
        self._cacheConfigurationInfo = value
    @property
    def wakeOnLanCapable(self) -> bool: ...
    @wakeOnLanCapable.setter
    def wakeOnLanCapable(self, value: bool):
        self._wakeOnLanCapable = value
    @property
    def featureCapability(self) -> List[FeatureCapability]: ...
    @featureCapability.setter
    def featureCapability(self, value: List[FeatureCapability]):
        self._featureCapability = value
    @property
    def maskedFeatureCapability(self) -> List[FeatureCapability]: ...
    @maskedFeatureCapability.setter
    def maskedFeatureCapability(self, value: List[FeatureCapability]):
        self._maskedFeatureCapability = value
    @property
    def vFlashConfigInfo(self) -> VFlashManager.VFlashConfigInfo: ...
    @vFlashConfigInfo.setter
    def vFlashConfigInfo(self, value: VFlashManager.VFlashConfigInfo):
        self._vFlashConfigInfo = value
    @property
    def vsanHostConfig(self) -> ConfigInfo: ...
    @vsanHostConfig.setter
    def vsanHostConfig(self, value: ConfigInfo):
        self._vsanHostConfig = value
    @property
    def domainList(self) -> List[str]: ...
    @domainList.setter
    def domainList(self, value: List[str]):
        self._domainList = value
    @property
    def scriptCheckSum(self) -> binary: ...
    @scriptCheckSum.setter
    def scriptCheckSum(self, value: binary):
        self._scriptCheckSum = value
    @property
    def hostConfigCheckSum(self) -> binary: ...
    @hostConfigCheckSum.setter
    def hostConfigCheckSum(self, value: binary):
        self._hostConfigCheckSum = value
    @property
    def descriptionTreeCheckSum(self) -> binary: ...
    @descriptionTreeCheckSum.setter
    def descriptionTreeCheckSum(self, value: binary):
        self._descriptionTreeCheckSum = value
    @property
    def graphicsInfo(self) -> List[GraphicsInfo]: ...
    @graphicsInfo.setter
    def graphicsInfo(self, value: List[GraphicsInfo]):
        self._graphicsInfo = value
    @property
    def sharedPassthruGpuTypes(self) -> List[str]: ...
    @sharedPassthruGpuTypes.setter
    def sharedPassthruGpuTypes(self, value: List[str]):
        self._sharedPassthruGpuTypes = value
    @property
    def graphicsConfig(self) -> GraphicsConfig: ...
    @graphicsConfig.setter
    def graphicsConfig(self, value: GraphicsConfig):
        self._graphicsConfig = value
    @property
    def sharedGpuCapabilities(self) -> List[SharedGpuCapabilities]: ...
    @sharedGpuCapabilities.setter
    def sharedGpuCapabilities(self, value: List[SharedGpuCapabilities]):
        self._sharedGpuCapabilities = value
    @property
    def ioFilterInfo(self) -> List[vim.IoFilterManager.HostIoFilterInfo]: ...
    @ioFilterInfo.setter
    def ioFilterInfo(self, value: List[vim.IoFilterManager.HostIoFilterInfo]):
        self._ioFilterInfo = value
    @property
    def sriovDevicePool(self) -> List[SriovDevicePoolInfo]: ...
    @sriovDevicePool.setter
    def sriovDevicePool(self, value: List[SriovDevicePoolInfo]):
        self._sriovDevicePool = value
    @property
    def assignableHardwareBinding(self) -> List[AssignableHardwareBinding]: ...
    @assignableHardwareBinding.setter
    def assignableHardwareBinding(self, value: List[AssignableHardwareBinding]):
        self._assignableHardwareBinding = value
    @property
    def assignableHardwareConfig(self) -> AssignableHardwareConfig: ...
    @assignableHardwareConfig.setter
    def assignableHardwareConfig(self, value: AssignableHardwareConfig):
        self._assignableHardwareConfig = value


class ConfigManager(vmodl.DynamicData):
    @property
    def cpuScheduler(self) -> CpuSchedulerSystem: ...
    @cpuScheduler.setter
    def cpuScheduler(self, value: CpuSchedulerSystem):
        self._cpuScheduler = value
    @property
    def datastoreSystem(self) -> DatastoreSystem: ...
    @datastoreSystem.setter
    def datastoreSystem(self, value: DatastoreSystem):
        self._datastoreSystem = value
    @property
    def memoryManager(self) -> MemoryManagerSystem: ...
    @memoryManager.setter
    def memoryManager(self, value: MemoryManagerSystem):
        self._memoryManager = value
    @property
    def storageSystem(self) -> StorageSystem: ...
    @storageSystem.setter
    def storageSystem(self, value: StorageSystem):
        self._storageSystem = value
    @property
    def networkSystem(self) -> NetworkSystem: ...
    @networkSystem.setter
    def networkSystem(self, value: NetworkSystem):
        self._networkSystem = value
    @property
    def vmotionSystem(self) -> VMotionSystem: ...
    @vmotionSystem.setter
    def vmotionSystem(self, value: VMotionSystem):
        self._vmotionSystem = value
    @property
    def virtualNicManager(self) -> VirtualNicManager: ...
    @virtualNicManager.setter
    def virtualNicManager(self, value: VirtualNicManager):
        self._virtualNicManager = value
    @property
    def serviceSystem(self) -> ServiceSystem: ...
    @serviceSystem.setter
    def serviceSystem(self, value: ServiceSystem):
        self._serviceSystem = value
    @property
    def firewallSystem(self) -> FirewallSystem: ...
    @firewallSystem.setter
    def firewallSystem(self, value: FirewallSystem):
        self._firewallSystem = value
    @property
    def advancedOption(self) -> vim.option.OptionManager: ...
    @advancedOption.setter
    def advancedOption(self, value: vim.option.OptionManager):
        self._advancedOption = value
    @property
    def diagnosticSystem(self) -> DiagnosticSystem: ...
    @diagnosticSystem.setter
    def diagnosticSystem(self, value: DiagnosticSystem):
        self._diagnosticSystem = value
    @property
    def autoStartManager(self) -> AutoStartManager: ...
    @autoStartManager.setter
    def autoStartManager(self, value: AutoStartManager):
        self._autoStartManager = value
    @property
    def snmpSystem(self) -> SnmpSystem: ...
    @snmpSystem.setter
    def snmpSystem(self, value: SnmpSystem):
        self._snmpSystem = value
    @property
    def dateTimeSystem(self) -> DateTimeSystem: ...
    @dateTimeSystem.setter
    def dateTimeSystem(self, value: DateTimeSystem):
        self._dateTimeSystem = value
    @property
    def patchManager(self) -> PatchManager: ...
    @patchManager.setter
    def patchManager(self, value: PatchManager):
        self._patchManager = value
    @property
    def imageConfigManager(self) -> ImageConfigManager: ...
    @imageConfigManager.setter
    def imageConfigManager(self, value: ImageConfigManager):
        self._imageConfigManager = value
    @property
    def bootDeviceSystem(self) -> BootDeviceSystem: ...
    @bootDeviceSystem.setter
    def bootDeviceSystem(self, value: BootDeviceSystem):
        self._bootDeviceSystem = value
    @property
    def firmwareSystem(self) -> FirmwareSystem: ...
    @firmwareSystem.setter
    def firmwareSystem(self, value: FirmwareSystem):
        self._firmwareSystem = value
    @property
    def healthStatusSystem(self) -> HealthStatusSystem: ...
    @healthStatusSystem.setter
    def healthStatusSystem(self, value: HealthStatusSystem):
        self._healthStatusSystem = value
    @property
    def pciPassthruSystem(self) -> PciPassthruSystem: ...
    @pciPassthruSystem.setter
    def pciPassthruSystem(self, value: PciPassthruSystem):
        self._pciPassthruSystem = value
    @property
    def licenseManager(self) -> vim.LicenseManager: ...
    @licenseManager.setter
    def licenseManager(self, value: vim.LicenseManager):
        self._licenseManager = value
    @property
    def kernelModuleSystem(self) -> KernelModuleSystem: ...
    @kernelModuleSystem.setter
    def kernelModuleSystem(self, value: KernelModuleSystem):
        self._kernelModuleSystem = value
    @property
    def authenticationManager(self) -> AuthenticationManager: ...
    @authenticationManager.setter
    def authenticationManager(self, value: AuthenticationManager):
        self._authenticationManager = value
    @property
    def powerSystem(self) -> PowerSystem: ...
    @powerSystem.setter
    def powerSystem(self, value: PowerSystem):
        self._powerSystem = value
    @property
    def cacheConfigurationManager(self) -> CacheConfigurationManager: ...
    @cacheConfigurationManager.setter
    def cacheConfigurationManager(self, value: CacheConfigurationManager):
        self._cacheConfigurationManager = value
    @property
    def esxAgentHostManager(self) -> EsxAgentHostManager: ...
    @esxAgentHostManager.setter
    def esxAgentHostManager(self, value: EsxAgentHostManager):
        self._esxAgentHostManager = value
    @property
    def iscsiManager(self) -> IscsiManager: ...
    @iscsiManager.setter
    def iscsiManager(self, value: IscsiManager):
        self._iscsiManager = value
    @property
    def vFlashManager(self) -> VFlashManager: ...
    @vFlashManager.setter
    def vFlashManager(self, value: VFlashManager):
        self._vFlashManager = value
    @property
    def vsanSystem(self) -> VsanSystem: ...
    @vsanSystem.setter
    def vsanSystem(self, value: VsanSystem):
        self._vsanSystem = value
    @property
    def messageBusProxy(self) -> MessageBusProxy: ...
    @messageBusProxy.setter
    def messageBusProxy(self, value: MessageBusProxy):
        self._messageBusProxy = value
    @property
    def userDirectory(self) -> vim.UserDirectory: ...
    @userDirectory.setter
    def userDirectory(self, value: vim.UserDirectory):
        self._userDirectory = value
    @property
    def accountManager(self) -> LocalAccountManager: ...
    @accountManager.setter
    def accountManager(self, value: LocalAccountManager):
        self._accountManager = value
    @property
    def hostAccessManager(self) -> HostAccessManager: ...
    @hostAccessManager.setter
    def hostAccessManager(self, value: HostAccessManager):
        self._hostAccessManager = value
    @property
    def graphicsManager(self) -> GraphicsManager: ...
    @graphicsManager.setter
    def graphicsManager(self, value: GraphicsManager):
        self._graphicsManager = value
    @property
    def vsanInternalSystem(self) -> VsanInternalSystem: ...
    @vsanInternalSystem.setter
    def vsanInternalSystem(self, value: VsanInternalSystem):
        self._vsanInternalSystem = value
    @property
    def certificateManager(self) -> CertificateManager: ...
    @certificateManager.setter
    def certificateManager(self, value: CertificateManager):
        self._certificateManager = value
    @property
    def cryptoManager(self) -> vim.encryption.CryptoManager: ...
    @cryptoManager.setter
    def cryptoManager(self, value: vim.encryption.CryptoManager):
        self._cryptoManager = value
    @property
    def nvdimmSystem(self) -> NvdimmSystem: ...
    @nvdimmSystem.setter
    def nvdimmSystem(self, value: NvdimmSystem):
        self._nvdimmSystem = value
    @property
    def assignableHardwareManager(self) -> AssignableHardwareManager: ...
    @assignableHardwareManager.setter
    def assignableHardwareManager(self, value: AssignableHardwareManager):
        self._assignableHardwareManager = value


class ConfigSpec(vmodl.DynamicData):
    @property
    def nasDatastore(self) -> List[NasVolume.Config]: ...
    @nasDatastore.setter
    def nasDatastore(self, value: List[NasVolume.Config]):
        self._nasDatastore = value
    @property
    def network(self) -> NetworkConfig: ...
    @network.setter
    def network(self, value: NetworkConfig):
        self._network = value
    @property
    def nicTypeSelection(self) -> List[VirtualNicManager.NicTypeSelection]: ...
    @nicTypeSelection.setter
    def nicTypeSelection(self, value: List[VirtualNicManager.NicTypeSelection]):
        self._nicTypeSelection = value
    @property
    def service(self) -> List[ServiceConfig]: ...
    @service.setter
    def service(self, value: List[ServiceConfig]):
        self._service = value
    @property
    def firewall(self) -> FirewallConfig: ...
    @firewall.setter
    def firewall(self, value: FirewallConfig):
        self._firewall = value
    @property
    def option(self) -> List[vim.option.OptionValue]: ...
    @option.setter
    def option(self, value: List[vim.option.OptionValue]):
        self._option = value
    @property
    def datastorePrincipal(self) -> str: ...
    @datastorePrincipal.setter
    def datastorePrincipal(self, value: str):
        self._datastorePrincipal = value
    @property
    def datastorePrincipalPasswd(self) -> str: ...
    @datastorePrincipalPasswd.setter
    def datastorePrincipalPasswd(self, value: str):
        self._datastorePrincipalPasswd = value
    @property
    def datetime(self) -> DateTimeConfig: ...
    @datetime.setter
    def datetime(self, value: DateTimeConfig):
        self._datetime = value
    @property
    def storageDevice(self) -> StorageDeviceInfo: ...
    @storageDevice.setter
    def storageDevice(self, value: StorageDeviceInfo):
        self._storageDevice = value
    @property
    def license(self) -> LicenseSpec: ...
    @license.setter
    def license(self, value: LicenseSpec):
        self._license = value
    @property
    def security(self) -> SecuritySpec: ...
    @security.setter
    def security(self, value: SecuritySpec):
        self._security = value
    @property
    def userAccount(self) -> List[LocalAccountManager.AccountSpecification]: ...
    @userAccount.setter
    def userAccount(self, value: List[LocalAccountManager.AccountSpecification]):
        self._userAccount = value
    @property
    def usergroupAccount(self) -> List[LocalAccountManager.AccountSpecification]: ...
    @usergroupAccount.setter
    def usergroupAccount(self, value: List[LocalAccountManager.AccountSpecification]):
        self._usergroupAccount = value
    @property
    def memory(self) -> MemorySpec: ...
    @memory.setter
    def memory(self, value: MemorySpec):
        self._memory = value
    @property
    def activeDirectory(self) -> List[ActiveDirectorySpec]: ...
    @activeDirectory.setter
    def activeDirectory(self, value: List[ActiveDirectorySpec]):
        self._activeDirectory = value
    @property
    def genericConfig(self) -> List[vmodl.KeyAnyValue]: ...
    @genericConfig.setter
    def genericConfig(self, value: List[vmodl.KeyAnyValue]):
        self._genericConfig = value
    @property
    def graphicsConfig(self) -> GraphicsConfig: ...
    @graphicsConfig.setter
    def graphicsConfig(self, value: GraphicsConfig):
        self._graphicsConfig = value
    @property
    def assignableHardwareConfig(self) -> AssignableHardwareConfig: ...
    @assignableHardwareConfig.setter
    def assignableHardwareConfig(self, value: AssignableHardwareConfig):
        self._assignableHardwareConfig = value


class ConnectInfo(vmodl.DynamicData):
    @property
    def serverIp(self) -> str: ...
    @serverIp.setter
    def serverIp(self, value: str):
        self._serverIp = value
    @property
    def inDasCluster(self) -> bool: ...
    @inDasCluster.setter
    def inDasCluster(self, value: bool):
        self._inDasCluster = value
    @property
    def host(self) -> Summary: ...
    @host.setter
    def host(self, value: Summary):
        self._host = value
    @property
    def vm(self) -> List[vim.vm.Summary]: ...
    @vm.setter
    def vm(self, value: List[vim.vm.Summary]):
        self._vm = value
    @property
    def vimAccountNameRequired(self) -> bool: ...
    @vimAccountNameRequired.setter
    def vimAccountNameRequired(self, value: bool):
        self._vimAccountNameRequired = value
    @property
    def clusterSupported(self) -> bool: ...
    @clusterSupported.setter
    def clusterSupported(self, value: bool):
        self._clusterSupported = value
    @property
    def network(self) -> List[ConnectInfo.NetworkInfo]: ...
    @network.setter
    def network(self, value: List[ConnectInfo.NetworkInfo]):
        self._network = value
    @property
    def datastore(self) -> List[ConnectInfo.DatastoreInfo]: ...
    @datastore.setter
    def datastore(self, value: List[ConnectInfo.DatastoreInfo]):
        self._datastore = value
    @property
    def license(self) -> ConnectInfo.LicenseInfo: ...
    @license.setter
    def license(self, value: ConnectInfo.LicenseInfo):
        self._license = value
    @property
    def capability(self) -> Capability: ...
    @capability.setter
    def capability(self, value: Capability):
        self._capability = value


    class DatastoreExistsInfo(ConnectInfo.DatastoreInfo):
        @property
        def newDatastoreName(self) -> str: ...
        @newDatastoreName.setter
        def newDatastoreName(self, value: str):
            self._newDatastoreName = value


    class DatastoreInfo(vmodl.DynamicData):
        @property
        def summary(self) -> vim.Datastore.Summary: ...
        @summary.setter
        def summary(self, value: vim.Datastore.Summary):
            self._summary = value


    class DatastoreNameConflictInfo(ConnectInfo.DatastoreInfo):
        @property
        def newDatastoreName(self) -> str: ...
        @newDatastoreName.setter
        def newDatastoreName(self, value: str):
            self._newDatastoreName = value


    class LicenseInfo(vmodl.DynamicData):
        @property
        def license(self) -> vim.LicenseManager.LicenseInfo: ...
        @license.setter
        def license(self, value: vim.LicenseManager.LicenseInfo):
            self._license = value
        @property
        def evaluation(self) -> vim.LicenseManager.EvaluationInfo: ...
        @evaluation.setter
        def evaluation(self, value: vim.LicenseManager.EvaluationInfo):
            self._evaluation = value
        @property
        def resource(self) -> vim.LicenseManager.LicensableResourceInfo: ...
        @resource.setter
        def resource(self, value: vim.LicenseManager.LicensableResourceInfo):
            self._resource = value


    class NetworkInfo(vmodl.DynamicData):
        @property
        def summary(self) -> vim.Network.Summary: ...
        @summary.setter
        def summary(self, value: vim.Network.Summary):
            self._summary = value


    class NewNetworkInfo(ConnectInfo.NetworkInfo): ...


class ConnectSpec(vmodl.DynamicData):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def port(self) -> int: ...
    @port.setter
    def port(self, value: int):
        self._port = value
    @property
    def sslThumbprint(self) -> str: ...
    @sslThumbprint.setter
    def sslThumbprint(self, value: str):
        self._sslThumbprint = value
    @property
    def userName(self) -> str: ...
    @userName.setter
    def userName(self, value: str):
        self._userName = value
    @property
    def password(self) -> str: ...
    @password.setter
    def password(self, value: str):
        self._password = value
    @property
    def vmFolder(self) -> vim.Folder: ...
    @vmFolder.setter
    def vmFolder(self, value: vim.Folder):
        self._vmFolder = value
    @property
    def force(self) -> bool: ...
    @force.setter
    def force(self, value: bool):
        self._force = value
    @property
    def vimAccountName(self) -> str: ...
    @vimAccountName.setter
    def vimAccountName(self, value: str):
        self._vimAccountName = value
    @property
    def vimAccountPassword(self) -> str: ...
    @vimAccountPassword.setter
    def vimAccountPassword(self, value: str):
        self._vimAccountPassword = value
    @property
    def managementIp(self) -> str: ...
    @managementIp.setter
    def managementIp(self, value: str):
        self._managementIp = value
    @property
    def lockdownMode(self) -> HostAccessManager.LockdownMode | Literal['lockdownDisabled', 'lockdownNormal', 'lockdownStrict']: ...
    @lockdownMode.setter
    def lockdownMode(self, value: HostAccessManager.LockdownMode | Literal['lockdownDisabled', 'lockdownNormal', 'lockdownStrict']):
        self._lockdownMode = value
    @property
    def hostGateway(self) -> GatewaySpec: ...
    @hostGateway.setter
    def hostGateway(self, value: GatewaySpec):
        self._hostGateway = value


class CpuIdInfo(vmodl.DynamicData):
    @property
    def level(self) -> int: ...
    @level.setter
    def level(self, value: int):
        self._level = value
    @property
    def vendor(self) -> str: ...
    @vendor.setter
    def vendor(self, value: str):
        self._vendor = value
    @property
    def eax(self) -> str: ...
    @eax.setter
    def eax(self, value: str):
        self._eax = value
    @property
    def ebx(self) -> str: ...
    @ebx.setter
    def ebx(self, value: str):
        self._ebx = value
    @property
    def ecx(self) -> str: ...
    @ecx.setter
    def ecx(self, value: str):
        self._ecx = value
    @property
    def edx(self) -> str: ...
    @edx.setter
    def edx(self, value: str):
        self._edx = value


class CpuInfo(vmodl.DynamicData):
    @property
    def numCpuPackages(self) -> short: ...
    @numCpuPackages.setter
    def numCpuPackages(self, value: short):
        self._numCpuPackages = value
    @property
    def numCpuCores(self) -> short: ...
    @numCpuCores.setter
    def numCpuCores(self, value: short):
        self._numCpuCores = value
    @property
    def numCpuThreads(self) -> short: ...
    @numCpuThreads.setter
    def numCpuThreads(self, value: short):
        self._numCpuThreads = value
    @property
    def hz(self) -> long: ...
    @hz.setter
    def hz(self, value: long):
        self._hz = value


class CpuPackage(vmodl.DynamicData):
    @property
    def index(self) -> short: ...
    @index.setter
    def index(self, value: short):
        self._index = value
    @property
    def vendor(self) -> str: ...
    @vendor.setter
    def vendor(self, value: str):
        self._vendor = value
    @property
    def hz(self) -> long: ...
    @hz.setter
    def hz(self, value: long):
        self._hz = value
    @property
    def busHz(self) -> long: ...
    @busHz.setter
    def busHz(self, value: long):
        self._busHz = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def threadId(self) -> List[short]: ...
    @threadId.setter
    def threadId(self, value: List[short]):
        self._threadId = value
    @property
    def cpuFeature(self) -> List[CpuIdInfo]: ...
    @cpuFeature.setter
    def cpuFeature(self, value: List[CpuIdInfo]):
        self._cpuFeature = value


    class Vendor(Enum):
        unknown = "unknown"
        intel = "intel"
        amd = "amd"
        hygon = "hygon"
        arm = "arm"


class CpuPowerManagementInfo(vmodl.DynamicData):
    @property
    def currentPolicy(self) -> str: ...
    @currentPolicy.setter
    def currentPolicy(self, value: str):
        self._currentPolicy = value
    @property
    def hardwareSupport(self) -> str: ...
    @hardwareSupport.setter
    def hardwareSupport(self, value: str):
        self._hardwareSupport = value


    class PolicyType(Enum):
        off = "off"
        staticPolicy = "staticPolicy"
        dynamicPolicy = "dynamicPolicy"


class DataTransportConnectionInfo(vmodl.DynamicData):
    @property
    def staticMemoryConsumed(self) -> long: ...
    @staticMemoryConsumed.setter
    def staticMemoryConsumed(self, value: long):
        self._staticMemoryConsumed = value


class DateTimeConfig(vmodl.DynamicData):
    @property
    def timeZone(self) -> str: ...
    @timeZone.setter
    def timeZone(self, value: str):
        self._timeZone = value
    @property
    def ntpConfig(self) -> NtpConfig: ...
    @ntpConfig.setter
    def ntpConfig(self, value: NtpConfig):
        self._ntpConfig = value
    @property
    def ptpConfig(self) -> PtpConfig: ...
    @ptpConfig.setter
    def ptpConfig(self, value: PtpConfig):
        self._ptpConfig = value
    @property
    def protocol(self) -> str: ...
    @protocol.setter
    def protocol(self, value: str):
        self._protocol = value
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def disableEvents(self) -> bool: ...
    @disableEvents.setter
    def disableEvents(self, value: bool):
        self._disableEvents = value
    @property
    def disableFallback(self) -> bool: ...
    @disableFallback.setter
    def disableFallback(self, value: bool):
        self._disableFallback = value
    @property
    def resetToFactoryDefaults(self) -> bool: ...
    @resetToFactoryDefaults.setter
    def resetToFactoryDefaults(self, value: bool):
        self._resetToFactoryDefaults = value


class DateTimeInfo(vmodl.DynamicData):
    @property
    def timeZone(self) -> DateTimeSystem.TimeZone: ...
    @timeZone.setter
    def timeZone(self, value: DateTimeSystem.TimeZone):
        self._timeZone = value
    @property
    def systemClockProtocol(self) -> str: ...
    @systemClockProtocol.setter
    def systemClockProtocol(self, value: str):
        self._systemClockProtocol = value
    @property
    def ntpConfig(self) -> NtpConfig: ...
    @ntpConfig.setter
    def ntpConfig(self, value: NtpConfig):
        self._ntpConfig = value
    @property
    def ptpConfig(self) -> PtpConfig: ...
    @ptpConfig.setter
    def ptpConfig(self, value: PtpConfig):
        self._ptpConfig = value
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def disableEvents(self) -> bool: ...
    @disableEvents.setter
    def disableEvents(self, value: bool):
        self._disableEvents = value
    @property
    def disableFallback(self) -> bool: ...
    @disableFallback.setter
    def disableFallback(self, value: bool):
        self._disableFallback = value
    @property
    def inFallbackState(self) -> bool: ...
    @inFallbackState.setter
    def inFallbackState(self, value: bool):
        self._inFallbackState = value
    @property
    def serviceSync(self) -> bool: ...
    @serviceSync.setter
    def serviceSync(self, value: bool):
        self._serviceSync = value
    @property
    def lastSyncTime(self) -> datetime: ...
    @lastSyncTime.setter
    def lastSyncTime(self, value: datetime):
        self._lastSyncTime = value
    @property
    def remoteNtpServer(self) -> str: ...
    @remoteNtpServer.setter
    def remoteNtpServer(self, value: str):
        self._remoteNtpServer = value
    @property
    def ntpRunTime(self) -> long: ...
    @ntpRunTime.setter
    def ntpRunTime(self, value: long):
        self._ntpRunTime = value
    @property
    def ptpRunTime(self) -> long: ...
    @ptpRunTime.setter
    def ptpRunTime(self, value: long):
        self._ptpRunTime = value
    @property
    def ntpDuration(self) -> str: ...
    @ntpDuration.setter
    def ntpDuration(self, value: str):
        self._ntpDuration = value
    @property
    def ptpDuration(self) -> str: ...
    @ptpDuration.setter
    def ptpDuration(self, value: str):
        self._ptpDuration = value


    class Protocol(Enum):
        ntp = "ntp"
        ptp = "ptp"


class DeploymentInfo(vmodl.DynamicData):
    @property
    def bootedFromStatelessCache(self) -> bool: ...
    @bootedFromStatelessCache.setter
    def bootedFromStatelessCache(self, value: bool):
        self._bootedFromStatelessCache = value


class Device(vmodl.DynamicData):
    @property
    def deviceName(self) -> str: ...
    @deviceName.setter
    def deviceName(self, value: str):
        self._deviceName = value
    @property
    def deviceType(self) -> str: ...
    @deviceType.setter
    def deviceType(self, value: str):
        self._deviceType = value


class DhcpService(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def spec(self) -> DhcpService.Specification: ...
    @spec.setter
    def spec(self, value: DhcpService.Specification):
        self._spec = value


    class Config(vmodl.DynamicData):
        @property
        def changeOperation(self) -> str: ...
        @changeOperation.setter
        def changeOperation(self, value: str):
            self._changeOperation = value
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def spec(self) -> DhcpService.Specification: ...
        @spec.setter
        def spec(self, value: DhcpService.Specification):
            self._spec = value


    class Specification(vmodl.DynamicData):
        @property
        def virtualSwitch(self) -> str: ...
        @virtualSwitch.setter
        def virtualSwitch(self, value: str):
            self._virtualSwitch = value
        @property
        def defaultLeaseDuration(self) -> int: ...
        @defaultLeaseDuration.setter
        def defaultLeaseDuration(self, value: int):
            self._defaultLeaseDuration = value
        @property
        def leaseBeginIp(self) -> str: ...
        @leaseBeginIp.setter
        def leaseBeginIp(self, value: str):
            self._leaseBeginIp = value
        @property
        def leaseEndIp(self) -> str: ...
        @leaseEndIp.setter
        def leaseEndIp(self, value: str):
            self._leaseEndIp = value
        @property
        def maxLeaseDuration(self) -> int: ...
        @maxLeaseDuration.setter
        def maxLeaseDuration(self, value: int):
            self._maxLeaseDuration = value
        @property
        def unlimitedLease(self) -> bool: ...
        @unlimitedLease.setter
        def unlimitedLease(self, value: bool):
            self._unlimitedLease = value
        @property
        def ipSubnetAddr(self) -> str: ...
        @ipSubnetAddr.setter
        def ipSubnetAddr(self, value: str):
            self._ipSubnetAddr = value
        @property
        def ipSubnetMask(self) -> str: ...
        @ipSubnetMask.setter
        def ipSubnetMask(self, value: str):
            self._ipSubnetMask = value


class DiagnosticPartition(vmodl.DynamicData):
    @property
    def storageType(self) -> str: ...
    @storageType.setter
    def storageType(self, value: str):
        self._storageType = value
    @property
    def diagnosticType(self) -> str: ...
    @diagnosticType.setter
    def diagnosticType(self, value: str):
        self._diagnosticType = value
    @property
    def slots(self) -> int: ...
    @slots.setter
    def slots(self, value: int):
        self._slots = value
    @property
    def id(self) -> ScsiDisk.Partition: ...
    @id.setter
    def id(self, value: ScsiDisk.Partition):
        self._id = value


    class CreateDescription(vmodl.DynamicData):
        @property
        def layout(self) -> DiskPartitionInfo.Layout: ...
        @layout.setter
        def layout(self, value: DiskPartitionInfo.Layout):
            self._layout = value
        @property
        def diskUuid(self) -> str: ...
        @diskUuid.setter
        def diskUuid(self, value: str):
            self._diskUuid = value
        @property
        def spec(self) -> DiagnosticPartition.CreateSpec: ...
        @spec.setter
        def spec(self, value: DiagnosticPartition.CreateSpec):
            self._spec = value


    class CreateOption(vmodl.DynamicData):
        @property
        def storageType(self) -> str: ...
        @storageType.setter
        def storageType(self, value: str):
            self._storageType = value
        @property
        def diagnosticType(self) -> str: ...
        @diagnosticType.setter
        def diagnosticType(self, value: str):
            self._diagnosticType = value
        @property
        def disk(self) -> ScsiDisk: ...
        @disk.setter
        def disk(self, value: ScsiDisk):
            self._disk = value


    class CreateSpec(vmodl.DynamicData):
        @property
        def storageType(self) -> str: ...
        @storageType.setter
        def storageType(self, value: str):
            self._storageType = value
        @property
        def diagnosticType(self) -> str: ...
        @diagnosticType.setter
        def diagnosticType(self, value: str):
            self._diagnosticType = value
        @property
        def id(self) -> ScsiDisk.Partition: ...
        @id.setter
        def id(self, value: ScsiDisk.Partition):
            self._id = value
        @property
        def partition(self) -> DiskPartitionInfo.Specification: ...
        @partition.setter
        def partition(self, value: DiskPartitionInfo.Specification):
            self._partition = value
        @property
        def active(self) -> bool: ...
        @active.setter
        def active(self, value: bool):
            self._active = value


    class DiagnosticType(Enum):
        singleHost = "singleHost"
        multiHost = "multiHost"


    class StorageType(Enum):
        directAttached = "directAttached"
        networkAttached = "networkAttached"


class DigestInfo(vmodl.DynamicData):
    @property
    def digestMethod(self) -> str: ...
    @digestMethod.setter
    def digestMethod(self, value: str):
        self._digestMethod = value
    @property
    def digestValue(self) -> List[byte]: ...
    @digestValue.setter
    def digestValue(self, value: List[byte]):
        self._digestValue = value
    @property
    def objectName(self) -> str: ...
    @objectName.setter
    def objectName(self, value: str):
        self._objectName = value


    class DigestMethodType(Enum):
        SHA1 = "SHA1"
        MD5 = "MD5"
        SHA256 = "SHA256"
        SHA384 = "SHA384"
        SHA512 = "SHA512"
        SM3_256 = "SM3_256"


class DirectoryStoreInfo(AuthenticationStoreInfo): ...


class DiskConfigurationResult(vmodl.DynamicData):
    @property
    def devicePath(self) -> str: ...
    @devicePath.setter
    def devicePath(self, value: str):
        self._devicePath = value
    @property
    def success(self) -> bool: ...
    @success.setter
    def success(self, value: bool):
        self._success = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class DiskDimensions(vmodl.DynamicData):


    class Chs(vmodl.DynamicData):
        @property
        def cylinder(self) -> long: ...
        @cylinder.setter
        def cylinder(self, value: long):
            self._cylinder = value
        @property
        def head(self) -> int: ...
        @head.setter
        def head(self, value: int):
            self._head = value
        @property
        def sector(self) -> int: ...
        @sector.setter
        def sector(self, value: int):
            self._sector = value


    class Lba(vmodl.DynamicData):
        @property
        def blockSize(self) -> int: ...
        @blockSize.setter
        def blockSize(self, value: int):
            self._blockSize = value
        @property
        def block(self) -> long: ...
        @block.setter
        def block(self, value: long):
            self._block = value


class DiskPartitionInfo(vmodl.DynamicData):
    @property
    def deviceName(self) -> str: ...
    @deviceName.setter
    def deviceName(self, value: str):
        self._deviceName = value
    @property
    def spec(self) -> DiskPartitionInfo.Specification: ...
    @spec.setter
    def spec(self, value: DiskPartitionInfo.Specification):
        self._spec = value
    @property
    def layout(self) -> DiskPartitionInfo.Layout: ...
    @layout.setter
    def layout(self, value: DiskPartitionInfo.Layout):
        self._layout = value


    class BlockRange(vmodl.DynamicData):
        @property
        def partition(self) -> int: ...
        @partition.setter
        def partition(self, value: int):
            self._partition = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def start(self) -> DiskDimensions.Lba: ...
        @start.setter
        def start(self, value: DiskDimensions.Lba):
            self._start = value
        @property
        def end(self) -> DiskDimensions.Lba: ...
        @end.setter
        def end(self, value: DiskDimensions.Lba):
            self._end = value


    class Layout(vmodl.DynamicData):
        @property
        def total(self) -> DiskDimensions.Lba: ...
        @total.setter
        def total(self, value: DiskDimensions.Lba):
            self._total = value
        @property
        def partition(self) -> List[DiskPartitionInfo.BlockRange]: ...
        @partition.setter
        def partition(self, value: List[DiskPartitionInfo.BlockRange]):
            self._partition = value


    class Partition(vmodl.DynamicData):
        @property
        def partition(self) -> int: ...
        @partition.setter
        def partition(self, value: int):
            self._partition = value
        @property
        def startSector(self) -> long: ...
        @startSector.setter
        def startSector(self, value: long):
            self._startSector = value
        @property
        def endSector(self) -> long: ...
        @endSector.setter
        def endSector(self, value: long):
            self._endSector = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def guid(self) -> str: ...
        @guid.setter
        def guid(self, value: str):
            self._guid = value
        @property
        def logical(self) -> bool: ...
        @logical.setter
        def logical(self, value: bool):
            self._logical = value
        @property
        def attributes(self) -> byte: ...
        @attributes.setter
        def attributes(self, value: byte):
            self._attributes = value
        @property
        def partitionAlignment(self) -> long: ...
        @partitionAlignment.setter
        def partitionAlignment(self, value: long):
            self._partitionAlignment = value


    class Specification(vmodl.DynamicData):
        @property
        def partitionFormat(self) -> str: ...
        @partitionFormat.setter
        def partitionFormat(self, value: str):
            self._partitionFormat = value
        @property
        def chs(self) -> DiskDimensions.Chs: ...
        @chs.setter
        def chs(self, value: DiskDimensions.Chs):
            self._chs = value
        @property
        def totalSectors(self) -> long: ...
        @totalSectors.setter
        def totalSectors(self, value: long):
            self._totalSectors = value
        @property
        def partition(self) -> List[DiskPartitionInfo.Partition]: ...
        @partition.setter
        def partition(self, value: List[DiskPartitionInfo.Partition]):
            self._partition = value


    class PartitionFormat(Enum):
        gpt = "gpt"
        mbr = "mbr"
        unknown = "unknown"


    class Type(Enum):
        none = "none"
        vmfs = "vmfs"
        linuxNative = "linuxNative"
        linuxSwap = "linuxSwap"
        extended = "extended"
        ntfs = "ntfs"
        vmkDiagnostic = "vmkDiagnostic"
        vffs = "vffs"


class DnsConfig(vmodl.DynamicData):
    @property
    def dhcp(self) -> bool: ...
    @dhcp.setter
    def dhcp(self, value: bool):
        self._dhcp = value
    @property
    def virtualNicDevice(self) -> str: ...
    @virtualNicDevice.setter
    def virtualNicDevice(self, value: str):
        self._virtualNicDevice = value
    @property
    def ipv6VirtualNicDevice(self) -> str: ...
    @ipv6VirtualNicDevice.setter
    def ipv6VirtualNicDevice(self, value: str):
        self._ipv6VirtualNicDevice = value
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def domainName(self) -> str: ...
    @domainName.setter
    def domainName(self, value: str):
        self._domainName = value
    @property
    def address(self) -> List[str]: ...
    @address.setter
    def address(self, value: List[str]):
        self._address = value
    @property
    def searchDomain(self) -> List[str]: ...
    @searchDomain.setter
    def searchDomain(self, value: List[str]):
        self._searchDomain = value


class DnsConfigSpec(DnsConfig):
    @property
    def virtualNicConnection(self) -> VirtualNicConnection: ...
    @virtualNicConnection.setter
    def virtualNicConnection(self, value: VirtualNicConnection):
        self._virtualNicConnection = value
    @property
    def virtualNicConnectionV6(self) -> VirtualNicConnection: ...
    @virtualNicConnectionV6.setter
    def virtualNicConnectionV6(self, value: VirtualNicConnection):
        self._virtualNicConnectionV6 = value


class DvxClass(vmodl.DynamicData):
    @property
    def deviceClass(self) -> str: ...
    @deviceClass.setter
    def deviceClass(self, value: str):
        self._deviceClass = value
    @property
    def checkpointSupported(self) -> bool: ...
    @checkpointSupported.setter
    def checkpointSupported(self, value: bool):
        self._checkpointSupported = value
    @property
    def swDMATracingSupported(self) -> bool: ...
    @swDMATracingSupported.setter
    def swDMATracingSupported(self, value: bool):
        self._swDMATracingSupported = value
    @property
    def sriovNic(self) -> bool: ...
    @sriovNic.setter
    def sriovNic(self, value: bool):
        self._sriovNic = value


class EnterMaintenanceResult(vmodl.DynamicData):
    @property
    def vmFaults(self) -> List[vim.FaultsByVM]: ...
    @vmFaults.setter
    def vmFaults(self, value: List[vim.FaultsByVM]):
        self._vmFaults = value
    @property
    def hostFaults(self) -> List[vim.FaultsByHost]: ...
    @hostFaults.setter
    def hostFaults(self, value: List[vim.FaultsByHost]):
        self._hostFaults = value


class FaultToleranceManager():


    class ComponentHealthInfo(vmodl.DynamicData):
        @property
        def isStorageHealthy(self) -> bool: ...
        @isStorageHealthy.setter
        def isStorageHealthy(self, value: bool):
            self._isStorageHealthy = value
        @property
        def isNetworkHealthy(self) -> bool: ...
        @isNetworkHealthy.setter
        def isNetworkHealthy(self, value: bool):
            self._isNetworkHealthy = value


class FcoeConfig(vmodl.DynamicData):
    @property
    def priorityClass(self) -> int: ...
    @priorityClass.setter
    def priorityClass(self, value: int):
        self._priorityClass = value
    @property
    def sourceMac(self) -> str: ...
    @sourceMac.setter
    def sourceMac(self, value: str):
        self._sourceMac = value
    @property
    def vlanRange(self) -> List[FcoeConfig.VlanRange]: ...
    @vlanRange.setter
    def vlanRange(self, value: List[FcoeConfig.VlanRange]):
        self._vlanRange = value
    @property
    def capabilities(self) -> FcoeConfig.FcoeCapabilities: ...
    @capabilities.setter
    def capabilities(self, value: FcoeConfig.FcoeCapabilities):
        self._capabilities = value
    @property
    def fcoeActive(self) -> bool: ...
    @fcoeActive.setter
    def fcoeActive(self, value: bool):
        self._fcoeActive = value


    class FcoeCapabilities(vmodl.DynamicData):
        @property
        def priorityClass(self) -> bool: ...
        @priorityClass.setter
        def priorityClass(self, value: bool):
            self._priorityClass = value
        @property
        def sourceMacAddress(self) -> bool: ...
        @sourceMacAddress.setter
        def sourceMacAddress(self, value: bool):
            self._sourceMacAddress = value
        @property
        def vlanRange(self) -> bool: ...
        @vlanRange.setter
        def vlanRange(self, value: bool):
            self._vlanRange = value


    class FcoeSpecification(vmodl.DynamicData):
        @property
        def underlyingPnic(self) -> str: ...
        @underlyingPnic.setter
        def underlyingPnic(self, value: str):
            self._underlyingPnic = value
        @property
        def priorityClass(self) -> int: ...
        @priorityClass.setter
        def priorityClass(self, value: int):
            self._priorityClass = value
        @property
        def sourceMac(self) -> str: ...
        @sourceMac.setter
        def sourceMac(self, value: str):
            self._sourceMac = value
        @property
        def vlanRange(self) -> List[FcoeConfig.VlanRange]: ...
        @vlanRange.setter
        def vlanRange(self, value: List[FcoeConfig.VlanRange]):
            self._vlanRange = value


    class VlanRange(vmodl.DynamicData):
        @property
        def vlanLow(self) -> int: ...
        @vlanLow.setter
        def vlanLow(self, value: int):
            self._vlanLow = value
        @property
        def vlanHigh(self) -> int: ...
        @vlanHigh.setter
        def vlanHigh(self, value: int):
            self._vlanHigh = value


class FeatureCapability(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def featureName(self) -> str: ...
    @featureName.setter
    def featureName(self, value: str):
        self._featureName = value
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class FeatureMask(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def featureName(self) -> str: ...
    @featureName.setter
    def featureName(self, value: str):
        self._featureName = value
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class FeatureVersionInfo(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


    class FeatureVersionKey(Enum):
        faultTolerance = "faultTolerance"


class FibreChannelHba(HostBusAdapter):
    @property
    def portWorldWideName(self) -> long: ...
    @portWorldWideName.setter
    def portWorldWideName(self, value: long):
        self._portWorldWideName = value
    @property
    def nodeWorldWideName(self) -> long: ...
    @nodeWorldWideName.setter
    def nodeWorldWideName(self, value: long):
        self._nodeWorldWideName = value
    @property
    def portType(self) -> FibreChannelHba.PortType | Literal['fabric', 'loop', 'pointToPoint', 'unknown']: ...
    @portType.setter
    def portType(self, value: FibreChannelHba.PortType | Literal['fabric', 'loop', 'pointToPoint', 'unknown']):
        self._portType = value
    @property
    def speed(self) -> long: ...
    @speed.setter
    def speed(self, value: long):
        self._speed = value


    class PortType(Enum):
        fabric = "fabric"
        loop = "loop"
        pointToPoint = "pointToPoint"
        unknown = "unknown"


class FibreChannelOverEthernetHba(FibreChannelHba):
    @property
    def underlyingNic(self) -> str: ...
    @underlyingNic.setter
    def underlyingNic(self, value: str):
        self._underlyingNic = value
    @property
    def linkInfo(self) -> FibreChannelOverEthernetHba.LinkInfo: ...
    @linkInfo.setter
    def linkInfo(self, value: FibreChannelOverEthernetHba.LinkInfo):
        self._linkInfo = value
    @property
    def isSoftwareFcoe(self) -> bool: ...
    @isSoftwareFcoe.setter
    def isSoftwareFcoe(self, value: bool):
        self._isSoftwareFcoe = value
    @property
    def markedForRemoval(self) -> bool: ...
    @markedForRemoval.setter
    def markedForRemoval(self, value: bool):
        self._markedForRemoval = value


    class LinkInfo(vmodl.DynamicData):
        @property
        def vnportMac(self) -> str: ...
        @vnportMac.setter
        def vnportMac(self, value: str):
            self._vnportMac = value
        @property
        def fcfMac(self) -> str: ...
        @fcfMac.setter
        def fcfMac(self, value: str):
            self._fcfMac = value
        @property
        def vlanId(self) -> int: ...
        @vlanId.setter
        def vlanId(self, value: int):
            self._vlanId = value


class FibreChannelOverEthernetTargetTransport(FibreChannelTargetTransport):
    @property
    def vnportMac(self) -> str: ...
    @vnportMac.setter
    def vnportMac(self, value: str):
        self._vnportMac = value
    @property
    def fcfMac(self) -> str: ...
    @fcfMac.setter
    def fcfMac(self, value: str):
        self._fcfMac = value
    @property
    def vlanId(self) -> int: ...
    @vlanId.setter
    def vlanId(self, value: int):
        self._vlanId = value


class FibreChannelTargetTransport(TargetTransport):
    @property
    def portWorldWideName(self) -> long: ...
    @portWorldWideName.setter
    def portWorldWideName(self, value: long):
        self._portWorldWideName = value
    @property
    def nodeWorldWideName(self) -> long: ...
    @nodeWorldWideName.setter
    def nodeWorldWideName(self, value: long):
        self._nodeWorldWideName = value


class FileAccess(vmodl.DynamicData):
    @property
    def who(self) -> str: ...
    @who.setter
    def who(self, value: str):
        self._who = value
    @property
    def what(self) -> str: ...
    @what.setter
    def what(self, value: str):
        self._what = value


    class Modes(vmodl.DynamicData):
        @property
        def browse(self) -> str: ...
        @browse.setter
        def browse(self, value: str):
            self._browse = value
        @property
        def read(self) -> str: ...
        @read.setter
        def read(self, value: str):
            self._read = value
        @property
        def modify(self) -> str: ...
        @modify.setter
        def modify(self, value: str):
            self._modify = value
        @property
        def use(self) -> str: ...
        @use.setter
        def use(self, value: str):
            self._use = value
        @property
        def admin(self) -> str: ...
        @admin.setter
        def admin(self, value: str):
            self._admin = value
        @property
        def full(self) -> str: ...
        @full.setter
        def full(self, value: str):
            self._full = value


class FileSystemMountInfo(vmodl.DynamicData):
    @property
    def mountInfo(self) -> MountInfo: ...
    @mountInfo.setter
    def mountInfo(self, value: MountInfo):
        self._mountInfo = value
    @property
    def volume(self) -> FileSystemVolume: ...
    @volume.setter
    def volume(self, value: FileSystemVolume):
        self._volume = value
    @property
    def vStorageSupport(self) -> str: ...
    @vStorageSupport.setter
    def vStorageSupport(self, value: str):
        self._vStorageSupport = value


    class VStorageSupportStatus(Enum):
        vStorageSupported = "vStorageSupported"
        vStorageUnsupported = "vStorageUnsupported"
        vStorageUnknown = "vStorageUnknown"


class FileSystemVolume(vmodl.DynamicData):
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def capacity(self) -> long: ...
    @capacity.setter
    def capacity(self, value: long):
        self._capacity = value


    class FileSystemType(Enum):
        VMFS = "VMFS"
        NFS = "NFS"
        NFS41 = "NFS41"
        CIFS = "CIFS"
        vsan = "vsan"
        VFFS = "VFFS"
        VVOL = "VVOL"
        PMEM = "PMEM"
        vsanD = "vsanD"
        OTHER = "OTHER"


class FileSystemVolumeInfo(vmodl.DynamicData):
    @property
    def volumeTypeList(self) -> List[str]: ...
    @volumeTypeList.setter
    def volumeTypeList(self, value: List[str]):
        self._volumeTypeList = value
    @property
    def mountInfo(self) -> List[FileSystemMountInfo]: ...
    @mountInfo.setter
    def mountInfo(self, value: List[FileSystemMountInfo]):
        self._mountInfo = value


class FirewallConfig(vmodl.DynamicData):
    @property
    def rule(self) -> List[FirewallConfig.RuleSetConfig]: ...
    @rule.setter
    def rule(self, value: List[FirewallConfig.RuleSetConfig]):
        self._rule = value
    @property
    def defaultBlockingPolicy(self) -> FirewallInfo.DefaultPolicy: ...
    @defaultBlockingPolicy.setter
    def defaultBlockingPolicy(self, value: FirewallInfo.DefaultPolicy):
        self._defaultBlockingPolicy = value


    class RuleSetConfig(vmodl.DynamicData):
        @property
        def rulesetId(self) -> str: ...
        @rulesetId.setter
        def rulesetId(self, value: str):
            self._rulesetId = value
        @property
        def enabled(self) -> bool: ...
        @enabled.setter
        def enabled(self, value: bool):
            self._enabled = value
        @property
        def allowedHosts(self) -> Ruleset.IpList: ...
        @allowedHosts.setter
        def allowedHosts(self, value: Ruleset.IpList):
            self._allowedHosts = value


class FirewallInfo(vmodl.DynamicData):
    @property
    def defaultPolicy(self) -> FirewallInfo.DefaultPolicy: ...
    @defaultPolicy.setter
    def defaultPolicy(self, value: FirewallInfo.DefaultPolicy):
        self._defaultPolicy = value
    @property
    def ruleset(self) -> List[Ruleset]: ...
    @ruleset.setter
    def ruleset(self, value: List[Ruleset]):
        self._ruleset = value


    class DefaultPolicy(vmodl.DynamicData):
        @property
        def incomingBlocked(self) -> bool: ...
        @incomingBlocked.setter
        def incomingBlocked(self, value: bool):
            self._incomingBlocked = value
        @property
        def outgoingBlocked(self) -> bool: ...
        @outgoingBlocked.setter
        def outgoingBlocked(self, value: bool):
            self._outgoingBlocked = value


class FlagInfo(vmodl.DynamicData):
    @property
    def backgroundSnapshotsEnabled(self) -> bool: ...
    @backgroundSnapshotsEnabled.setter
    def backgroundSnapshotsEnabled(self, value: bool):
        self._backgroundSnapshotsEnabled = value


class ForceMountedInfo(vmodl.DynamicData):
    @property
    def persist(self) -> bool: ...
    @persist.setter
    def persist(self, value: bool):
        self._persist = value
    @property
    def mounted(self) -> bool: ...
    @mounted.setter
    def mounted(self, value: bool):
        self._mounted = value


class Fru(vmodl.DynamicData):
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def partName(self) -> str: ...
    @partName.setter
    def partName(self, value: str):
        self._partName = value
    @property
    def partNumber(self) -> str: ...
    @partNumber.setter
    def partNumber(self, value: str):
        self._partNumber = value
    @property
    def manufacturer(self) -> str: ...
    @manufacturer.setter
    def manufacturer(self, value: str):
        self._manufacturer = value
    @property
    def serialNumber(self) -> str: ...
    @serialNumber.setter
    def serialNumber(self, value: str):
        self._serialNumber = value
    @property
    def mfgTimeStamp(self) -> datetime: ...
    @mfgTimeStamp.setter
    def mfgTimeStamp(self, value: datetime):
        self._mfgTimeStamp = value


    class FruType(Enum):
        undefined = "undefined"
        board = "board"
        product = "product"


class GatewaySpec(vmodl.DynamicData):
    @property
    def gatewayType(self) -> str: ...
    @gatewayType.setter
    def gatewayType(self, value: str):
        self._gatewayType = value
    @property
    def gatewayId(self) -> str: ...
    @gatewayId.setter
    def gatewayId(self, value: str):
        self._gatewayId = value
    @property
    def trustVerificationToken(self) -> str: ...
    @trustVerificationToken.setter
    def trustVerificationToken(self, value: str):
        self._trustVerificationToken = value
    @property
    def hostAuthParams(self) -> List[vim.KeyValue]: ...
    @hostAuthParams.setter
    def hostAuthParams(self, value: List[vim.KeyValue]):
        self._hostAuthParams = value


class GraphicsConfig(vmodl.DynamicData):
    @property
    def hostDefaultGraphicsType(self) -> str: ...
    @hostDefaultGraphicsType.setter
    def hostDefaultGraphicsType(self, value: str):
        self._hostDefaultGraphicsType = value
    @property
    def sharedPassthruAssignmentPolicy(self) -> str: ...
    @sharedPassthruAssignmentPolicy.setter
    def sharedPassthruAssignmentPolicy(self, value: str):
        self._sharedPassthruAssignmentPolicy = value
    @property
    def deviceType(self) -> List[GraphicsConfig.DeviceType]: ...
    @deviceType.setter
    def deviceType(self, value: List[GraphicsConfig.DeviceType]):
        self._deviceType = value


    class DeviceType(vmodl.DynamicData):
        @property
        def deviceId(self) -> str: ...
        @deviceId.setter
        def deviceId(self, value: str):
            self._deviceId = value
        @property
        def graphicsType(self) -> str: ...
        @graphicsType.setter
        def graphicsType(self, value: str):
            self._graphicsType = value


    class GraphicsType(Enum):
        shared = "shared"
        sharedDirect = "sharedDirect"


    class SharedPassthruAssignmentPolicy(Enum):
        performance = "performance"
        consolidation = "consolidation"


class GraphicsInfo(vmodl.DynamicData):
    @property
    def deviceName(self) -> str: ...
    @deviceName.setter
    def deviceName(self, value: str):
        self._deviceName = value
    @property
    def vendorName(self) -> str: ...
    @vendorName.setter
    def vendorName(self, value: str):
        self._vendorName = value
    @property
    def pciId(self) -> str: ...
    @pciId.setter
    def pciId(self, value: str):
        self._pciId = value
    @property
    def graphicsType(self) -> str: ...
    @graphicsType.setter
    def graphicsType(self, value: str):
        self._graphicsType = value
    @property
    def memorySizeInKB(self) -> long: ...
    @memorySizeInKB.setter
    def memorySizeInKB(self, value: long):
        self._memorySizeInKB = value
    @property
    def vm(self) -> List[vim.VirtualMachine]: ...
    @vm.setter
    def vm(self, value: List[vim.VirtualMachine]):
        self._vm = value


class HardwareInfo(vmodl.DynamicData):
    @property
    def systemInfo(self) -> SystemInfo: ...
    @systemInfo.setter
    def systemInfo(self, value: SystemInfo):
        self._systemInfo = value
    @property
    def cpuPowerManagementInfo(self) -> CpuPowerManagementInfo: ...
    @cpuPowerManagementInfo.setter
    def cpuPowerManagementInfo(self, value: CpuPowerManagementInfo):
        self._cpuPowerManagementInfo = value
    @property
    def cpuInfo(self) -> CpuInfo: ...
    @cpuInfo.setter
    def cpuInfo(self, value: CpuInfo):
        self._cpuInfo = value
    @property
    def cpuPkg(self) -> List[CpuPackage]: ...
    @cpuPkg.setter
    def cpuPkg(self, value: List[CpuPackage]):
        self._cpuPkg = value
    @property
    def memorySize(self) -> long: ...
    @memorySize.setter
    def memorySize(self, value: long):
        self._memorySize = value
    @property
    def numaInfo(self) -> NumaInfo: ...
    @numaInfo.setter
    def numaInfo(self, value: NumaInfo):
        self._numaInfo = value
    @property
    def smcPresent(self) -> bool: ...
    @smcPresent.setter
    def smcPresent(self, value: bool):
        self._smcPresent = value
    @property
    def pciDevice(self) -> List[PciDevice]: ...
    @pciDevice.setter
    def pciDevice(self, value: List[PciDevice]):
        self._pciDevice = value
    @property
    def dvxClasses(self) -> List[DvxClass]: ...
    @dvxClasses.setter
    def dvxClasses(self, value: List[DvxClass]):
        self._dvxClasses = value
    @property
    def cpuFeature(self) -> List[CpuIdInfo]: ...
    @cpuFeature.setter
    def cpuFeature(self, value: List[CpuIdInfo]):
        self._cpuFeature = value
    @property
    def biosInfo(self) -> BIOSInfo: ...
    @biosInfo.setter
    def biosInfo(self, value: BIOSInfo):
        self._biosInfo = value
    @property
    def reliableMemoryInfo(self) -> ReliableMemoryInfo: ...
    @reliableMemoryInfo.setter
    def reliableMemoryInfo(self, value: ReliableMemoryInfo):
        self._reliableMemoryInfo = value
    @property
    def persistentMemoryInfo(self) -> PersistentMemoryInfo: ...
    @persistentMemoryInfo.setter
    def persistentMemoryInfo(self, value: PersistentMemoryInfo):
        self._persistentMemoryInfo = value
    @property
    def sgxInfo(self) -> SgxInfo: ...
    @sgxInfo.setter
    def sgxInfo(self, value: SgxInfo):
        self._sgxInfo = value
    @property
    def sevInfo(self) -> SevInfo: ...
    @sevInfo.setter
    def sevInfo(self, value: SevInfo):
        self._sevInfo = value
    @property
    def memoryTieringType(self) -> str: ...
    @memoryTieringType.setter
    def memoryTieringType(self, value: str):
        self._memoryTieringType = value
    @property
    def memoryTierInfo(self) -> List[MemoryTierInfo]: ...
    @memoryTierInfo.setter
    def memoryTierInfo(self, value: List[MemoryTierInfo]):
        self._memoryTierInfo = value


class HardwareStatusInfo(vmodl.DynamicData):
    @property
    def memoryStatusInfo(self) -> List[HardwareStatusInfo.HardwareElementInfo]: ...
    @memoryStatusInfo.setter
    def memoryStatusInfo(self, value: List[HardwareStatusInfo.HardwareElementInfo]):
        self._memoryStatusInfo = value
    @property
    def cpuStatusInfo(self) -> List[HardwareStatusInfo.HardwareElementInfo]: ...
    @cpuStatusInfo.setter
    def cpuStatusInfo(self, value: List[HardwareStatusInfo.HardwareElementInfo]):
        self._cpuStatusInfo = value
    @property
    def storageStatusInfo(self) -> List[HardwareStatusInfo.StorageStatusInfo]: ...
    @storageStatusInfo.setter
    def storageStatusInfo(self, value: List[HardwareStatusInfo.StorageStatusInfo]):
        self._storageStatusInfo = value
    @property
    def dpuStatusInfo(self) -> List[HardwareStatusInfo.DpuStatusInfo]: ...
    @dpuStatusInfo.setter
    def dpuStatusInfo(self, value: List[HardwareStatusInfo.DpuStatusInfo]):
        self._dpuStatusInfo = value


    class DpuStatusInfo(HardwareStatusInfo.HardwareElementInfo):
        @property
        def dpuId(self) -> str: ...
        @dpuId.setter
        def dpuId(self, value: str):
            self._dpuId = value
        @property
        def fru(self) -> Fru: ...
        @fru.setter
        def fru(self, value: Fru):
            self._fru = value
        @property
        def sensors(self) -> List[HardwareStatusInfo.DpuStatusInfo.OperationalInfo]: ...
        @sensors.setter
        def sensors(self, value: List[HardwareStatusInfo.DpuStatusInfo.OperationalInfo]):
            self._sensors = value


        class OperationalInfo(vmodl.DynamicData):
            @property
            def sensorId(self) -> str: ...
            @sensorId.setter
            def sensorId(self, value: str):
                self._sensorId = value
            @property
            def healthState(self) -> vim.ElementDescription: ...
            @healthState.setter
            def healthState(self, value: vim.ElementDescription):
                self._healthState = value
            @property
            def reading(self) -> str: ...
            @reading.setter
            def reading(self, value: str):
                self._reading = value
            @property
            def units(self) -> str: ...
            @units.setter
            def units(self, value: str):
                self._units = value
            @property
            def timeStamp(self) -> datetime: ...
            @timeStamp.setter
            def timeStamp(self, value: datetime):
                self._timeStamp = value


    class HardwareElementInfo(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def status(self) -> vim.ElementDescription: ...
        @status.setter
        def status(self, value: vim.ElementDescription):
            self._status = value


    class StorageStatusInfo(HardwareStatusInfo.HardwareElementInfo):
        @property
        def operationalInfo(self) -> List[HardwareStatusInfo.StorageStatusInfo.OperationalInfo]: ...
        @operationalInfo.setter
        def operationalInfo(self, value: List[HardwareStatusInfo.StorageStatusInfo.OperationalInfo]):
            self._operationalInfo = value


        class OperationalInfo(vmodl.DynamicData):
            @property
            def property(self) -> str: ...
            @property.setter
            def property(self, value: str):
                self._property = value
            @property
            def value(self) -> str: ...
            @value.setter
            def value(self, value: str):
                self._value = value


    class Status(Enum):
        Unknown = "Unknown"
        Green = "Green"
        Yellow = "Yellow"
        Red = "Red"


class HbaCreateSpec(vmodl.DynamicData): ...


class HostBusAdapter(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value
    @property
    def bus(self) -> int: ...
    @bus.setter
    def bus(self, value: int):
        self._bus = value
    @property
    def status(self) -> str: ...
    @status.setter
    def status(self, value: str):
        self._status = value
    @property
    def model(self) -> str: ...
    @model.setter
    def model(self, value: str):
        self._model = value
    @property
    def driver(self) -> str: ...
    @driver.setter
    def driver(self, value: str):
        self._driver = value
    @property
    def pci(self) -> str: ...
    @pci.setter
    def pci(self, value: str):
        self._pci = value
    @property
    def storageProtocol(self) -> str: ...
    @storageProtocol.setter
    def storageProtocol(self, value: str):
        self._storageProtocol = value


class HostProxySwitch(vmodl.DynamicData):
    @property
    def dvsUuid(self) -> str: ...
    @dvsUuid.setter
    def dvsUuid(self, value: str):
        self._dvsUuid = value
    @property
    def dvsName(self) -> str: ...
    @dvsName.setter
    def dvsName(self, value: str):
        self._dvsName = value
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def numPorts(self) -> int: ...
    @numPorts.setter
    def numPorts(self, value: int):
        self._numPorts = value
    @property
    def configNumPorts(self) -> int: ...
    @configNumPorts.setter
    def configNumPorts(self, value: int):
        self._configNumPorts = value
    @property
    def numPortsAvailable(self) -> int: ...
    @numPortsAvailable.setter
    def numPortsAvailable(self, value: int):
        self._numPortsAvailable = value
    @property
    def uplinkPort(self) -> List[vim.KeyValue]: ...
    @uplinkPort.setter
    def uplinkPort(self, value: List[vim.KeyValue]):
        self._uplinkPort = value
    @property
    def mtu(self) -> int: ...
    @mtu.setter
    def mtu(self, value: int):
        self._mtu = value
    @property
    def pnic(self) -> List[Link]: ...
    @pnic.setter
    def pnic(self, value: List[Link]):
        self._pnic = value
    @property
    def spec(self) -> HostProxySwitch.Specification: ...
    @spec.setter
    def spec(self, value: HostProxySwitch.Specification):
        self._spec = value
    @property
    def hostLag(self) -> List[HostProxySwitch.HostLagConfig]: ...
    @hostLag.setter
    def hostLag(self, value: List[HostProxySwitch.HostLagConfig]):
        self._hostLag = value
    @property
    def networkReservationSupported(self) -> bool: ...
    @networkReservationSupported.setter
    def networkReservationSupported(self, value: bool):
        self._networkReservationSupported = value
    @property
    def nsxtEnabled(self) -> bool: ...
    @nsxtEnabled.setter
    def nsxtEnabled(self, value: bool):
        self._nsxtEnabled = value
    @property
    def ensEnabled(self) -> bool: ...
    @ensEnabled.setter
    def ensEnabled(self, value: bool):
        self._ensEnabled = value
    @property
    def ensInterruptEnabled(self) -> bool: ...
    @ensInterruptEnabled.setter
    def ensInterruptEnabled(self, value: bool):
        self._ensInterruptEnabled = value
    @property
    def transportZones(self) -> List[vim.dvs.HostMember.TransportZoneInfo]: ...
    @transportZones.setter
    def transportZones(self, value: List[vim.dvs.HostMember.TransportZoneInfo]):
        self._transportZones = value
    @property
    def nsxUsedUplinkPort(self) -> List[str]: ...
    @nsxUsedUplinkPort.setter
    def nsxUsedUplinkPort(self, value: List[str]):
        self._nsxUsedUplinkPort = value
    @property
    def nsxtStatus(self) -> str: ...
    @nsxtStatus.setter
    def nsxtStatus(self, value: str):
        self._nsxtStatus = value
    @property
    def nsxtStatusDetail(self) -> str: ...
    @nsxtStatusDetail.setter
    def nsxtStatusDetail(self, value: str):
        self._nsxtStatusDetail = value
    @property
    def ensInfo(self) -> HostProxySwitch.EnsInfo: ...
    @ensInfo.setter
    def ensInfo(self, value: HostProxySwitch.EnsInfo):
        self._ensInfo = value
    @property
    def networkOffloadingEnabled(self) -> bool: ...
    @networkOffloadingEnabled.setter
    def networkOffloadingEnabled(self, value: bool):
        self._networkOffloadingEnabled = value


    class Config(vmodl.DynamicData):
        @property
        def changeOperation(self) -> str: ...
        @changeOperation.setter
        def changeOperation(self, value: str):
            self._changeOperation = value
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def spec(self) -> HostProxySwitch.Specification: ...
        @spec.setter
        def spec(self, value: HostProxySwitch.Specification):
            self._spec = value


    class EnsInfo(vmodl.DynamicData):
        @property
        def opsVersion(self) -> long: ...
        @opsVersion.setter
        def opsVersion(self, value: long):
            self._opsVersion = value
        @property
        def numPSOps(self) -> long: ...
        @numPSOps.setter
        def numPSOps(self, value: long):
            self._numPSOps = value
        @property
        def numLcoreOps(self) -> long: ...
        @numLcoreOps.setter
        def numLcoreOps(self, value: long):
            self._numLcoreOps = value
        @property
        def errorStatus(self) -> long: ...
        @errorStatus.setter
        def errorStatus(self, value: long):
            self._errorStatus = value
        @property
        def lcoreStatus(self) -> long: ...
        @lcoreStatus.setter
        def lcoreStatus(self, value: long):
            self._lcoreStatus = value


    class HostLagConfig(vmodl.DynamicData):
        @property
        def lagKey(self) -> str: ...
        @lagKey.setter
        def lagKey(self, value: str):
            self._lagKey = value
        @property
        def lagName(self) -> str: ...
        @lagName.setter
        def lagName(self, value: str):
            self._lagName = value
        @property
        def uplinkPort(self) -> List[vim.KeyValue]: ...
        @uplinkPort.setter
        def uplinkPort(self, value: List[vim.KeyValue]):
            self._uplinkPort = value


    class Specification(vmodl.DynamicData):
        @property
        def backing(self) -> vim.dvs.HostMember.Backing: ...
        @backing.setter
        def backing(self, value: vim.dvs.HostMember.Backing):
            self._backing = value


class InternetScsiHba(HostBusAdapter):
    @property
    def isSoftwareBased(self) -> bool: ...
    @isSoftwareBased.setter
    def isSoftwareBased(self, value: bool):
        self._isSoftwareBased = value
    @property
    def canBeDisabled(self) -> bool: ...
    @canBeDisabled.setter
    def canBeDisabled(self, value: bool):
        self._canBeDisabled = value
    @property
    def networkBindingSupport(self) -> InternetScsiHba.NetworkBindingSupportType | Literal['notsupported', 'optional', 'required']: ...
    @networkBindingSupport.setter
    def networkBindingSupport(self, value: InternetScsiHba.NetworkBindingSupportType | Literal['notsupported', 'optional', 'required']):
        self._networkBindingSupport = value
    @property
    def discoveryCapabilities(self) -> InternetScsiHba.DiscoveryCapabilities: ...
    @discoveryCapabilities.setter
    def discoveryCapabilities(self, value: InternetScsiHba.DiscoveryCapabilities):
        self._discoveryCapabilities = value
    @property
    def discoveryProperties(self) -> InternetScsiHba.DiscoveryProperties: ...
    @discoveryProperties.setter
    def discoveryProperties(self, value: InternetScsiHba.DiscoveryProperties):
        self._discoveryProperties = value
    @property
    def authenticationCapabilities(self) -> InternetScsiHba.AuthenticationCapabilities: ...
    @authenticationCapabilities.setter
    def authenticationCapabilities(self, value: InternetScsiHba.AuthenticationCapabilities):
        self._authenticationCapabilities = value
    @property
    def authenticationProperties(self) -> InternetScsiHba.AuthenticationProperties: ...
    @authenticationProperties.setter
    def authenticationProperties(self, value: InternetScsiHba.AuthenticationProperties):
        self._authenticationProperties = value
    @property
    def digestCapabilities(self) -> InternetScsiHba.DigestCapabilities: ...
    @digestCapabilities.setter
    def digestCapabilities(self, value: InternetScsiHba.DigestCapabilities):
        self._digestCapabilities = value
    @property
    def digestProperties(self) -> InternetScsiHba.DigestProperties: ...
    @digestProperties.setter
    def digestProperties(self, value: InternetScsiHba.DigestProperties):
        self._digestProperties = value
    @property
    def ipCapabilities(self) -> InternetScsiHba.IPCapabilities: ...
    @ipCapabilities.setter
    def ipCapabilities(self, value: InternetScsiHba.IPCapabilities):
        self._ipCapabilities = value
    @property
    def ipProperties(self) -> InternetScsiHba.IPProperties: ...
    @ipProperties.setter
    def ipProperties(self, value: InternetScsiHba.IPProperties):
        self._ipProperties = value
    @property
    def supportedAdvancedOptions(self) -> List[vim.option.OptionDef]: ...
    @supportedAdvancedOptions.setter
    def supportedAdvancedOptions(self, value: List[vim.option.OptionDef]):
        self._supportedAdvancedOptions = value
    @property
    def advancedOptions(self) -> List[InternetScsiHba.ParamValue]: ...
    @advancedOptions.setter
    def advancedOptions(self, value: List[InternetScsiHba.ParamValue]):
        self._advancedOptions = value
    @property
    def iScsiName(self) -> str: ...
    @iScsiName.setter
    def iScsiName(self, value: str):
        self._iScsiName = value
    @property
    def iScsiAlias(self) -> str: ...
    @iScsiAlias.setter
    def iScsiAlias(self, value: str):
        self._iScsiAlias = value
    @property
    def configuredSendTarget(self) -> List[InternetScsiHba.SendTarget]: ...
    @configuredSendTarget.setter
    def configuredSendTarget(self, value: List[InternetScsiHba.SendTarget]):
        self._configuredSendTarget = value
    @property
    def configuredStaticTarget(self) -> List[InternetScsiHba.StaticTarget]: ...
    @configuredStaticTarget.setter
    def configuredStaticTarget(self, value: List[InternetScsiHba.StaticTarget]):
        self._configuredStaticTarget = value
    @property
    def maxSpeedMb(self) -> int: ...
    @maxSpeedMb.setter
    def maxSpeedMb(self, value: int):
        self._maxSpeedMb = value
    @property
    def currentSpeedMb(self) -> int: ...
    @currentSpeedMb.setter
    def currentSpeedMb(self, value: int):
        self._currentSpeedMb = value


    class AuthenticationCapabilities(vmodl.DynamicData):
        @property
        def chapAuthSettable(self) -> bool: ...
        @chapAuthSettable.setter
        def chapAuthSettable(self, value: bool):
            self._chapAuthSettable = value
        @property
        def krb5AuthSettable(self) -> bool: ...
        @krb5AuthSettable.setter
        def krb5AuthSettable(self, value: bool):
            self._krb5AuthSettable = value
        @property
        def srpAuthSettable(self) -> bool: ...
        @srpAuthSettable.setter
        def srpAuthSettable(self, value: bool):
            self._srpAuthSettable = value
        @property
        def spkmAuthSettable(self) -> bool: ...
        @spkmAuthSettable.setter
        def spkmAuthSettable(self, value: bool):
            self._spkmAuthSettable = value
        @property
        def mutualChapSettable(self) -> bool: ...
        @mutualChapSettable.setter
        def mutualChapSettable(self, value: bool):
            self._mutualChapSettable = value
        @property
        def targetChapSettable(self) -> bool: ...
        @targetChapSettable.setter
        def targetChapSettable(self, value: bool):
            self._targetChapSettable = value
        @property
        def targetMutualChapSettable(self) -> bool: ...
        @targetMutualChapSettable.setter
        def targetMutualChapSettable(self, value: bool):
            self._targetMutualChapSettable = value


    class AuthenticationProperties(vmodl.DynamicData):
        @property
        def chapAuthEnabled(self) -> bool: ...
        @chapAuthEnabled.setter
        def chapAuthEnabled(self, value: bool):
            self._chapAuthEnabled = value
        @property
        def chapName(self) -> str: ...
        @chapName.setter
        def chapName(self, value: str):
            self._chapName = value
        @property
        def chapSecret(self) -> str: ...
        @chapSecret.setter
        def chapSecret(self, value: str):
            self._chapSecret = value
        @property
        def chapAuthenticationType(self) -> str: ...
        @chapAuthenticationType.setter
        def chapAuthenticationType(self, value: str):
            self._chapAuthenticationType = value
        @property
        def chapInherited(self) -> bool: ...
        @chapInherited.setter
        def chapInherited(self, value: bool):
            self._chapInherited = value
        @property
        def mutualChapName(self) -> str: ...
        @mutualChapName.setter
        def mutualChapName(self, value: str):
            self._mutualChapName = value
        @property
        def mutualChapSecret(self) -> str: ...
        @mutualChapSecret.setter
        def mutualChapSecret(self, value: str):
            self._mutualChapSecret = value
        @property
        def mutualChapAuthenticationType(self) -> str: ...
        @mutualChapAuthenticationType.setter
        def mutualChapAuthenticationType(self, value: str):
            self._mutualChapAuthenticationType = value
        @property
        def mutualChapInherited(self) -> bool: ...
        @mutualChapInherited.setter
        def mutualChapInherited(self, value: bool):
            self._mutualChapInherited = value


    class DigestCapabilities(vmodl.DynamicData):
        @property
        def headerDigestSettable(self) -> bool: ...
        @headerDigestSettable.setter
        def headerDigestSettable(self, value: bool):
            self._headerDigestSettable = value
        @property
        def dataDigestSettable(self) -> bool: ...
        @dataDigestSettable.setter
        def dataDigestSettable(self, value: bool):
            self._dataDigestSettable = value
        @property
        def targetHeaderDigestSettable(self) -> bool: ...
        @targetHeaderDigestSettable.setter
        def targetHeaderDigestSettable(self, value: bool):
            self._targetHeaderDigestSettable = value
        @property
        def targetDataDigestSettable(self) -> bool: ...
        @targetDataDigestSettable.setter
        def targetDataDigestSettable(self, value: bool):
            self._targetDataDigestSettable = value


    class DigestProperties(vmodl.DynamicData):
        @property
        def headerDigestType(self) -> str: ...
        @headerDigestType.setter
        def headerDigestType(self, value: str):
            self._headerDigestType = value
        @property
        def headerDigestInherited(self) -> bool: ...
        @headerDigestInherited.setter
        def headerDigestInherited(self, value: bool):
            self._headerDigestInherited = value
        @property
        def dataDigestType(self) -> str: ...
        @dataDigestType.setter
        def dataDigestType(self, value: str):
            self._dataDigestType = value
        @property
        def dataDigestInherited(self) -> bool: ...
        @dataDigestInherited.setter
        def dataDigestInherited(self, value: bool):
            self._dataDigestInherited = value


    class DiscoveryCapabilities(vmodl.DynamicData):
        @property
        def iSnsDiscoverySettable(self) -> bool: ...
        @iSnsDiscoverySettable.setter
        def iSnsDiscoverySettable(self, value: bool):
            self._iSnsDiscoverySettable = value
        @property
        def slpDiscoverySettable(self) -> bool: ...
        @slpDiscoverySettable.setter
        def slpDiscoverySettable(self, value: bool):
            self._slpDiscoverySettable = value
        @property
        def staticTargetDiscoverySettable(self) -> bool: ...
        @staticTargetDiscoverySettable.setter
        def staticTargetDiscoverySettable(self, value: bool):
            self._staticTargetDiscoverySettable = value
        @property
        def sendTargetsDiscoverySettable(self) -> bool: ...
        @sendTargetsDiscoverySettable.setter
        def sendTargetsDiscoverySettable(self, value: bool):
            self._sendTargetsDiscoverySettable = value


    class DiscoveryProperties(vmodl.DynamicData):
        @property
        def iSnsDiscoveryEnabled(self) -> bool: ...
        @iSnsDiscoveryEnabled.setter
        def iSnsDiscoveryEnabled(self, value: bool):
            self._iSnsDiscoveryEnabled = value
        @property
        def iSnsDiscoveryMethod(self) -> str: ...
        @iSnsDiscoveryMethod.setter
        def iSnsDiscoveryMethod(self, value: str):
            self._iSnsDiscoveryMethod = value
        @property
        def iSnsHost(self) -> str: ...
        @iSnsHost.setter
        def iSnsHost(self, value: str):
            self._iSnsHost = value
        @property
        def slpDiscoveryEnabled(self) -> bool: ...
        @slpDiscoveryEnabled.setter
        def slpDiscoveryEnabled(self, value: bool):
            self._slpDiscoveryEnabled = value
        @property
        def slpDiscoveryMethod(self) -> str: ...
        @slpDiscoveryMethod.setter
        def slpDiscoveryMethod(self, value: str):
            self._slpDiscoveryMethod = value
        @property
        def slpHost(self) -> str: ...
        @slpHost.setter
        def slpHost(self, value: str):
            self._slpHost = value
        @property
        def staticTargetDiscoveryEnabled(self) -> bool: ...
        @staticTargetDiscoveryEnabled.setter
        def staticTargetDiscoveryEnabled(self, value: bool):
            self._staticTargetDiscoveryEnabled = value
        @property
        def sendTargetsDiscoveryEnabled(self) -> bool: ...
        @sendTargetsDiscoveryEnabled.setter
        def sendTargetsDiscoveryEnabled(self, value: bool):
            self._sendTargetsDiscoveryEnabled = value


        class ISnsDiscoveryMethod(Enum):
            isnsStatic = "isnsStatic"
            isnsDhcp = "isnsDhcp"
            isnsSlp = "isnsSlp"


        class SlpDiscoveryMethod(Enum):
            slpDhcp = "slpDhcp"
            slpAutoUnicast = "slpAutoUnicast"
            slpAutoMulticast = "slpAutoMulticast"
            slpManual = "slpManual"


    class IPCapabilities(vmodl.DynamicData):
        @property
        def addressSettable(self) -> bool: ...
        @addressSettable.setter
        def addressSettable(self, value: bool):
            self._addressSettable = value
        @property
        def ipConfigurationMethodSettable(self) -> bool: ...
        @ipConfigurationMethodSettable.setter
        def ipConfigurationMethodSettable(self, value: bool):
            self._ipConfigurationMethodSettable = value
        @property
        def subnetMaskSettable(self) -> bool: ...
        @subnetMaskSettable.setter
        def subnetMaskSettable(self, value: bool):
            self._subnetMaskSettable = value
        @property
        def defaultGatewaySettable(self) -> bool: ...
        @defaultGatewaySettable.setter
        def defaultGatewaySettable(self, value: bool):
            self._defaultGatewaySettable = value
        @property
        def primaryDnsServerAddressSettable(self) -> bool: ...
        @primaryDnsServerAddressSettable.setter
        def primaryDnsServerAddressSettable(self, value: bool):
            self._primaryDnsServerAddressSettable = value
        @property
        def alternateDnsServerAddressSettable(self) -> bool: ...
        @alternateDnsServerAddressSettable.setter
        def alternateDnsServerAddressSettable(self, value: bool):
            self._alternateDnsServerAddressSettable = value
        @property
        def ipv6Supported(self) -> bool: ...
        @ipv6Supported.setter
        def ipv6Supported(self, value: bool):
            self._ipv6Supported = value
        @property
        def arpRedirectSettable(self) -> bool: ...
        @arpRedirectSettable.setter
        def arpRedirectSettable(self, value: bool):
            self._arpRedirectSettable = value
        @property
        def mtuSettable(self) -> bool: ...
        @mtuSettable.setter
        def mtuSettable(self, value: bool):
            self._mtuSettable = value
        @property
        def hostNameAsTargetAddress(self) -> bool: ...
        @hostNameAsTargetAddress.setter
        def hostNameAsTargetAddress(self, value: bool):
            self._hostNameAsTargetAddress = value
        @property
        def nameAliasSettable(self) -> bool: ...
        @nameAliasSettable.setter
        def nameAliasSettable(self, value: bool):
            self._nameAliasSettable = value
        @property
        def ipv4EnableSettable(self) -> bool: ...
        @ipv4EnableSettable.setter
        def ipv4EnableSettable(self, value: bool):
            self._ipv4EnableSettable = value
        @property
        def ipv6EnableSettable(self) -> bool: ...
        @ipv6EnableSettable.setter
        def ipv6EnableSettable(self, value: bool):
            self._ipv6EnableSettable = value
        @property
        def ipv6PrefixLengthSettable(self) -> bool: ...
        @ipv6PrefixLengthSettable.setter
        def ipv6PrefixLengthSettable(self, value: bool):
            self._ipv6PrefixLengthSettable = value
        @property
        def ipv6PrefixLength(self) -> int: ...
        @ipv6PrefixLength.setter
        def ipv6PrefixLength(self, value: int):
            self._ipv6PrefixLength = value
        @property
        def ipv6DhcpConfigurationSettable(self) -> bool: ...
        @ipv6DhcpConfigurationSettable.setter
        def ipv6DhcpConfigurationSettable(self, value: bool):
            self._ipv6DhcpConfigurationSettable = value
        @property
        def ipv6LinkLocalAutoConfigurationSettable(self) -> bool: ...
        @ipv6LinkLocalAutoConfigurationSettable.setter
        def ipv6LinkLocalAutoConfigurationSettable(self, value: bool):
            self._ipv6LinkLocalAutoConfigurationSettable = value
        @property
        def ipv6RouterAdvertisementConfigurationSettable(self) -> bool: ...
        @ipv6RouterAdvertisementConfigurationSettable.setter
        def ipv6RouterAdvertisementConfigurationSettable(self, value: bool):
            self._ipv6RouterAdvertisementConfigurationSettable = value
        @property
        def ipv6DefaultGatewaySettable(self) -> bool: ...
        @ipv6DefaultGatewaySettable.setter
        def ipv6DefaultGatewaySettable(self, value: bool):
            self._ipv6DefaultGatewaySettable = value
        @property
        def ipv6MaxStaticAddressesSupported(self) -> int: ...
        @ipv6MaxStaticAddressesSupported.setter
        def ipv6MaxStaticAddressesSupported(self, value: int):
            self._ipv6MaxStaticAddressesSupported = value


    class IPProperties(vmodl.DynamicData):
        @property
        def mac(self) -> str: ...
        @mac.setter
        def mac(self, value: str):
            self._mac = value
        @property
        def address(self) -> str: ...
        @address.setter
        def address(self, value: str):
            self._address = value
        @property
        def dhcpConfigurationEnabled(self) -> bool: ...
        @dhcpConfigurationEnabled.setter
        def dhcpConfigurationEnabled(self, value: bool):
            self._dhcpConfigurationEnabled = value
        @property
        def subnetMask(self) -> str: ...
        @subnetMask.setter
        def subnetMask(self, value: str):
            self._subnetMask = value
        @property
        def defaultGateway(self) -> str: ...
        @defaultGateway.setter
        def defaultGateway(self, value: str):
            self._defaultGateway = value
        @property
        def primaryDnsServerAddress(self) -> str: ...
        @primaryDnsServerAddress.setter
        def primaryDnsServerAddress(self, value: str):
            self._primaryDnsServerAddress = value
        @property
        def alternateDnsServerAddress(self) -> str: ...
        @alternateDnsServerAddress.setter
        def alternateDnsServerAddress(self, value: str):
            self._alternateDnsServerAddress = value
        @property
        def ipv6Address(self) -> str: ...
        @ipv6Address.setter
        def ipv6Address(self, value: str):
            self._ipv6Address = value
        @property
        def ipv6SubnetMask(self) -> str: ...
        @ipv6SubnetMask.setter
        def ipv6SubnetMask(self, value: str):
            self._ipv6SubnetMask = value
        @property
        def ipv6DefaultGateway(self) -> str: ...
        @ipv6DefaultGateway.setter
        def ipv6DefaultGateway(self, value: str):
            self._ipv6DefaultGateway = value
        @property
        def arpRedirectEnabled(self) -> bool: ...
        @arpRedirectEnabled.setter
        def arpRedirectEnabled(self, value: bool):
            self._arpRedirectEnabled = value
        @property
        def mtu(self) -> int: ...
        @mtu.setter
        def mtu(self, value: int):
            self._mtu = value
        @property
        def jumboFramesEnabled(self) -> bool: ...
        @jumboFramesEnabled.setter
        def jumboFramesEnabled(self, value: bool):
            self._jumboFramesEnabled = value
        @property
        def ipv4Enabled(self) -> bool: ...
        @ipv4Enabled.setter
        def ipv4Enabled(self, value: bool):
            self._ipv4Enabled = value
        @property
        def ipv6Enabled(self) -> bool: ...
        @ipv6Enabled.setter
        def ipv6Enabled(self, value: bool):
            self._ipv6Enabled = value
        @property
        def ipv6properties(self) -> InternetScsiHba.IPv6Properties: ...
        @ipv6properties.setter
        def ipv6properties(self, value: InternetScsiHba.IPv6Properties):
            self._ipv6properties = value


    class IPv6Properties(vmodl.DynamicData):
        @property
        def iscsiIpv6Address(self) -> List[InternetScsiHba.IscsiIpv6Address]: ...
        @iscsiIpv6Address.setter
        def iscsiIpv6Address(self, value: List[InternetScsiHba.IscsiIpv6Address]):
            self._iscsiIpv6Address = value
        @property
        def ipv6DhcpConfigurationEnabled(self) -> bool: ...
        @ipv6DhcpConfigurationEnabled.setter
        def ipv6DhcpConfigurationEnabled(self, value: bool):
            self._ipv6DhcpConfigurationEnabled = value
        @property
        def ipv6LinkLocalAutoConfigurationEnabled(self) -> bool: ...
        @ipv6LinkLocalAutoConfigurationEnabled.setter
        def ipv6LinkLocalAutoConfigurationEnabled(self, value: bool):
            self._ipv6LinkLocalAutoConfigurationEnabled = value
        @property
        def ipv6RouterAdvertisementConfigurationEnabled(self) -> bool: ...
        @ipv6RouterAdvertisementConfigurationEnabled.setter
        def ipv6RouterAdvertisementConfigurationEnabled(self, value: bool):
            self._ipv6RouterAdvertisementConfigurationEnabled = value
        @property
        def ipv6DefaultGateway(self) -> str: ...
        @ipv6DefaultGateway.setter
        def ipv6DefaultGateway(self, value: str):
            self._ipv6DefaultGateway = value


    class IscsiIpv6Address(vmodl.DynamicData):
        @property
        def address(self) -> str: ...
        @address.setter
        def address(self, value: str):
            self._address = value
        @property
        def prefixLength(self) -> int: ...
        @prefixLength.setter
        def prefixLength(self, value: int):
            self._prefixLength = value
        @property
        def origin(self) -> str: ...
        @origin.setter
        def origin(self, value: str):
            self._origin = value
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value


        class AddressConfigurationType(Enum):
            DHCP = "DHCP"
            AutoConfigured = "AutoConfigured"
            Static = "Static"
            Other = "Other"


        class IPv6AddressOperation(Enum):
            add = "add"
            remove = "remove"


    class ParamValue(vim.option.OptionValue):
        @property
        def isInherited(self) -> bool: ...
        @isInherited.setter
        def isInherited(self, value: bool):
            self._isInherited = value


    class SendTarget(vmodl.DynamicData):
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
        def authenticationProperties(self) -> InternetScsiHba.AuthenticationProperties: ...
        @authenticationProperties.setter
        def authenticationProperties(self, value: InternetScsiHba.AuthenticationProperties):
            self._authenticationProperties = value
        @property
        def digestProperties(self) -> InternetScsiHba.DigestProperties: ...
        @digestProperties.setter
        def digestProperties(self, value: InternetScsiHba.DigestProperties):
            self._digestProperties = value
        @property
        def supportedAdvancedOptions(self) -> List[vim.option.OptionDef]: ...
        @supportedAdvancedOptions.setter
        def supportedAdvancedOptions(self, value: List[vim.option.OptionDef]):
            self._supportedAdvancedOptions = value
        @property
        def advancedOptions(self) -> List[InternetScsiHba.ParamValue]: ...
        @advancedOptions.setter
        def advancedOptions(self, value: List[InternetScsiHba.ParamValue]):
            self._advancedOptions = value
        @property
        def parent(self) -> str: ...
        @parent.setter
        def parent(self, value: str):
            self._parent = value


    class StaticTarget(vmodl.DynamicData):
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
        def iScsiName(self) -> str: ...
        @iScsiName.setter
        def iScsiName(self, value: str):
            self._iScsiName = value
        @property
        def discoveryMethod(self) -> str: ...
        @discoveryMethod.setter
        def discoveryMethod(self, value: str):
            self._discoveryMethod = value
        @property
        def authenticationProperties(self) -> InternetScsiHba.AuthenticationProperties: ...
        @authenticationProperties.setter
        def authenticationProperties(self, value: InternetScsiHba.AuthenticationProperties):
            self._authenticationProperties = value
        @property
        def digestProperties(self) -> InternetScsiHba.DigestProperties: ...
        @digestProperties.setter
        def digestProperties(self, value: InternetScsiHba.DigestProperties):
            self._digestProperties = value
        @property
        def supportedAdvancedOptions(self) -> List[vim.option.OptionDef]: ...
        @supportedAdvancedOptions.setter
        def supportedAdvancedOptions(self, value: List[vim.option.OptionDef]):
            self._supportedAdvancedOptions = value
        @property
        def advancedOptions(self) -> List[InternetScsiHba.ParamValue]: ...
        @advancedOptions.setter
        def advancedOptions(self, value: List[InternetScsiHba.ParamValue]):
            self._advancedOptions = value
        @property
        def parent(self) -> str: ...
        @parent.setter
        def parent(self, value: str):
            self._parent = value


        class TargetDiscoveryMethod(Enum):
            staticMethod = "staticMethod"
            sendTargetMethod = "sendTargetMethod"
            slpMethod = "slpMethod"
            isnsMethod = "isnsMethod"
            unknownMethod = "unknownMethod"


    class TargetSet(vmodl.DynamicData):
        @property
        def staticTargets(self) -> List[InternetScsiHba.StaticTarget]: ...
        @staticTargets.setter
        def staticTargets(self, value: List[InternetScsiHba.StaticTarget]):
            self._staticTargets = value
        @property
        def sendTargets(self) -> List[InternetScsiHba.SendTarget]: ...
        @sendTargets.setter
        def sendTargets(self, value: List[InternetScsiHba.SendTarget]):
            self._sendTargets = value


    class ChapAuthenticationType(Enum):
        chapProhibited = "chapProhibited"
        chapDiscouraged = "chapDiscouraged"
        chapPreferred = "chapPreferred"
        chapRequired = "chapRequired"


    class DigestType(Enum):
        digestProhibited = "digestProhibited"
        digestDiscouraged = "digestDiscouraged"
        digestPreferred = "digestPreferred"
        digestRequired = "digestRequired"


    class NetworkBindingSupportType(Enum):
        notsupported = "notsupported"
        optional = "optional"
        required = "required"


class InternetScsiTargetTransport(TargetTransport):
    @property
    def iScsiName(self) -> str: ...
    @iScsiName.setter
    def iScsiName(self, value: str):
        self._iScsiName = value
    @property
    def iScsiAlias(self) -> str: ...
    @iScsiAlias.setter
    def iScsiAlias(self, value: str):
        self._iScsiAlias = value
    @property
    def address(self) -> List[str]: ...
    @address.setter
    def address(self, value: List[str]):
        self._address = value


class IpConfig(vmodl.DynamicData):
    @property
    def dhcp(self) -> bool: ...
    @dhcp.setter
    def dhcp(self, value: bool):
        self._dhcp = value
    @property
    def ipAddress(self) -> str: ...
    @ipAddress.setter
    def ipAddress(self, value: str):
        self._ipAddress = value
    @property
    def subnetMask(self) -> str: ...
    @subnetMask.setter
    def subnetMask(self, value: str):
        self._subnetMask = value
    @property
    def ipV6Config(self) -> IpConfig.IpV6AddressConfiguration: ...
    @ipV6Config.setter
    def ipV6Config(self, value: IpConfig.IpV6AddressConfiguration):
        self._ipV6Config = value


    class IpV6Address(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @ipAddress.setter
        def ipAddress(self, value: str):
            self._ipAddress = value
        @property
        def prefixLength(self) -> int: ...
        @prefixLength.setter
        def prefixLength(self, value: int):
            self._prefixLength = value
        @property
        def origin(self) -> str: ...
        @origin.setter
        def origin(self, value: str):
            self._origin = value
        @property
        def dadState(self) -> str: ...
        @dadState.setter
        def dadState(self, value: str):
            self._dadState = value
        @property
        def lifetime(self) -> datetime: ...
        @lifetime.setter
        def lifetime(self, value: datetime):
            self._lifetime = value
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value


    class IpV6AddressConfiguration(vmodl.DynamicData):
        @property
        def ipV6Address(self) -> List[IpConfig.IpV6Address]: ...
        @ipV6Address.setter
        def ipV6Address(self, value: List[IpConfig.IpV6Address]):
            self._ipV6Address = value
        @property
        def autoConfigurationEnabled(self) -> bool: ...
        @autoConfigurationEnabled.setter
        def autoConfigurationEnabled(self, value: bool):
            self._autoConfigurationEnabled = value
        @property
        def dhcpV6Enabled(self) -> bool: ...
        @dhcpV6Enabled.setter
        def dhcpV6Enabled(self, value: bool):
            self._dhcpV6Enabled = value


    class IpV6AddressConfigType(Enum):
        other = "other"
        manual = "manual"
        dhcp = "dhcp"
        linklayer = "linklayer"
        random = "random"


    class IpV6AddressStatus(Enum):
        preferred = "preferred"
        deprecated = "deprecated"
        invalid = "invalid"
        inaccessible = "inaccessible"
        unknown = "unknown"
        tentative = "tentative"
        duplicate = "duplicate"


class IpRouteConfig(vmodl.DynamicData):
    @property
    def defaultGateway(self) -> str: ...
    @defaultGateway.setter
    def defaultGateway(self, value: str):
        self._defaultGateway = value
    @property
    def gatewayDevice(self) -> str: ...
    @gatewayDevice.setter
    def gatewayDevice(self, value: str):
        self._gatewayDevice = value
    @property
    def ipV6DefaultGateway(self) -> str: ...
    @ipV6DefaultGateway.setter
    def ipV6DefaultGateway(self, value: str):
        self._ipV6DefaultGateway = value
    @property
    def ipV6GatewayDevice(self) -> str: ...
    @ipV6GatewayDevice.setter
    def ipV6GatewayDevice(self, value: str):
        self._ipV6GatewayDevice = value


class IpRouteConfigSpec(IpRouteConfig):
    @property
    def gatewayDeviceConnection(self) -> VirtualNicConnection: ...
    @gatewayDeviceConnection.setter
    def gatewayDeviceConnection(self, value: VirtualNicConnection):
        self._gatewayDeviceConnection = value
    @property
    def ipV6GatewayDeviceConnection(self) -> VirtualNicConnection: ...
    @ipV6GatewayDeviceConnection.setter
    def ipV6GatewayDeviceConnection(self, value: VirtualNicConnection):
        self._ipV6GatewayDeviceConnection = value


class IpRouteEntry(vmodl.DynamicData):
    @property
    def network(self) -> str: ...
    @network.setter
    def network(self, value: str):
        self._network = value
    @property
    def prefixLength(self) -> int: ...
    @prefixLength.setter
    def prefixLength(self, value: int):
        self._prefixLength = value
    @property
    def gateway(self) -> str: ...
    @gateway.setter
    def gateway(self, value: str):
        self._gateway = value
    @property
    def deviceName(self) -> str: ...
    @deviceName.setter
    def deviceName(self, value: str):
        self._deviceName = value


class IpRouteOp(vmodl.DynamicData):
    @property
    def changeOperation(self) -> str: ...
    @changeOperation.setter
    def changeOperation(self, value: str):
        self._changeOperation = value
    @property
    def route(self) -> IpRouteEntry: ...
    @route.setter
    def route(self, value: IpRouteEntry):
        self._route = value


class IpRouteTableConfig(vmodl.DynamicData):
    @property
    def ipRoute(self) -> List[IpRouteOp]: ...
    @ipRoute.setter
    def ipRoute(self, value: List[IpRouteOp]):
        self._ipRoute = value
    @property
    def ipv6Route(self) -> List[IpRouteOp]: ...
    @ipv6Route.setter
    def ipv6Route(self, value: List[IpRouteOp]):
        self._ipv6Route = value


class IpRouteTableInfo(vmodl.DynamicData):
    @property
    def ipRoute(self) -> List[IpRouteEntry]: ...
    @ipRoute.setter
    def ipRoute(self, value: List[IpRouteEntry]):
        self._ipRoute = value
    @property
    def ipv6Route(self) -> List[IpRouteEntry]: ...
    @ipv6Route.setter
    def ipv6Route(self, value: List[IpRouteEntry]):
        self._ipv6Route = value


class IpmiInfo(vmodl.DynamicData):
    @property
    def bmcIpAddress(self) -> str: ...
    @bmcIpAddress.setter
    def bmcIpAddress(self, value: str):
        self._bmcIpAddress = value
    @property
    def bmcMacAddress(self) -> str: ...
    @bmcMacAddress.setter
    def bmcMacAddress(self, value: str):
        self._bmcMacAddress = value
    @property
    def login(self) -> str: ...
    @login.setter
    def login(self, value: str):
        self._login = value
    @property
    def password(self) -> str: ...
    @password.setter
    def password(self, value: str):
        self._password = value


class LicenseSpec(vmodl.DynamicData):
    @property
    def source(self) -> vim.LicenseManager.LicenseSource: ...
    @source.setter
    def source(self, value: vim.LicenseManager.LicenseSource):
        self._source = value
    @property
    def editionKey(self) -> str: ...
    @editionKey.setter
    def editionKey(self, value: str):
        self._editionKey = value
    @property
    def disabledFeatureKey(self) -> List[str]: ...
    @disabledFeatureKey.setter
    def disabledFeatureKey(self, value: List[str]):
        self._disabledFeatureKey = value
    @property
    def enabledFeatureKey(self) -> List[str]: ...
    @enabledFeatureKey.setter
    def enabledFeatureKey(self, value: List[str]):
        self._enabledFeatureKey = value


class LinkDiscoveryProtocolConfig(vmodl.DynamicData):
    @property
    def protocol(self) -> str: ...
    @protocol.setter
    def protocol(self, value: str):
        self._protocol = value
    @property
    def operation(self) -> str: ...
    @operation.setter
    def operation(self, value: str):
        self._operation = value


    class OperationType(Enum):
        none = "none"
        listen = "listen"
        advertise = "advertise"
        both = "both"


    class ProtocolType(Enum):
        cdp = "cdp"
        lldp = "lldp"


class LocalAuthenticationInfo(AuthenticationStoreInfo): ...


class LocalDatastoreInfo(vim.Datastore.Info):
    @property
    def path(self) -> str: ...
    @path.setter
    def path(self, value: str):
        self._path = value


class LocalFileSystemVolume(FileSystemVolume):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value


    class Specification(vmodl.DynamicData):
        @property
        def device(self) -> str: ...
        @device.setter
        def device(self, value: str):
            self._device = value
        @property
        def localPath(self) -> str: ...
        @localPath.setter
        def localPath(self, value: str):
            self._localPath = value


class LowLevelProvisioningManager():


    class DiskLayoutSpec(vmodl.DynamicData):
        @property
        def controllerType(self) -> type: ...
        @controllerType.setter
        def controllerType(self, value: type):
            self._controllerType = value
        @property
        def busNumber(self) -> int: ...
        @busNumber.setter
        def busNumber(self, value: int):
            self._busNumber = value
        @property
        def unitNumber(self) -> int: ...
        @unitNumber.setter
        def unitNumber(self, value: int):
            self._unitNumber = value
        @property
        def srcFilename(self) -> str: ...
        @srcFilename.setter
        def srcFilename(self, value: str):
            self._srcFilename = value
        @property
        def dstFilename(self) -> str: ...
        @dstFilename.setter
        def dstFilename(self, value: str):
            self._dstFilename = value


    class FileDeleteResult(vmodl.DynamicData):
        @property
        def fileName(self) -> str: ...
        @fileName.setter
        def fileName(self, value: str):
            self._fileName = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


    class FileDeleteSpec(vmodl.DynamicData):
        @property
        def fileName(self) -> str: ...
        @fileName.setter
        def fileName(self, value: str):
            self._fileName = value
        @property
        def fileType(self) -> str: ...
        @fileType.setter
        def fileType(self, value: str):
            self._fileType = value


    class FileReserveResult(vmodl.DynamicData):
        @property
        def baseName(self) -> str: ...
        @baseName.setter
        def baseName(self, value: str):
            self._baseName = value
        @property
        def parentDir(self) -> str: ...
        @parentDir.setter
        def parentDir(self, value: str):
            self._parentDir = value
        @property
        def reservedName(self) -> str: ...
        @reservedName.setter
        def reservedName(self, value: str):
            self._reservedName = value


    class FileReserveSpec(vmodl.DynamicData):
        @property
        def baseName(self) -> str: ...
        @baseName.setter
        def baseName(self, value: str):
            self._baseName = value
        @property
        def parentDir(self) -> str: ...
        @parentDir.setter
        def parentDir(self, value: str):
            self._parentDir = value
        @property
        def fileType(self) -> str: ...
        @fileType.setter
        def fileType(self, value: str):
            self._fileType = value
        @property
        def storageProfile(self) -> str: ...
        @storageProfile.setter
        def storageProfile(self, value: str):
            self._storageProfile = value


    class SnapshotLayoutSpec(vmodl.DynamicData):
        @property
        def id(self) -> int: ...
        @id.setter
        def id(self, value: int):
            self._id = value
        @property
        def srcFilename(self) -> str: ...
        @srcFilename.setter
        def srcFilename(self, value: str):
            self._srcFilename = value
        @property
        def dstFilename(self) -> str: ...
        @dstFilename.setter
        def dstFilename(self, value: str):
            self._dstFilename = value
        @property
        def disk(self) -> List[LowLevelProvisioningManager.DiskLayoutSpec]: ...
        @disk.setter
        def disk(self, value: List[LowLevelProvisioningManager.DiskLayoutSpec]):
            self._disk = value


    class VmMigrationStatus(vmodl.DynamicData):
        @property
        def migrationId(self) -> long: ...
        @migrationId.setter
        def migrationId(self, value: long):
            self._migrationId = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def source(self) -> bool: ...
        @source.setter
        def source(self, value: bool):
            self._source = value
        @property
        def consideredSuccessful(self) -> bool: ...
        @consideredSuccessful.setter
        def consideredSuccessful(self, value: bool):
            self._consideredSuccessful = value


    class VmRecoveryInfo(vmodl.DynamicData):
        @property
        def version(self) -> str: ...
        @version.setter
        def version(self, value: str):
            self._version = value
        @property
        def biosUUID(self) -> str: ...
        @biosUUID.setter
        def biosUUID(self, value: str):
            self._biosUUID = value
        @property
        def instanceUUID(self) -> str: ...
        @instanceUUID.setter
        def instanceUUID(self, value: str):
            self._instanceUUID = value
        @property
        def ftInfo(self) -> vim.vm.FaultToleranceConfigInfo: ...
        @ftInfo.setter
        def ftInfo(self, value: vim.vm.FaultToleranceConfigInfo):
            self._ftInfo = value


    class FileType(Enum):
        File = "File"
        VirtualDisk = "VirtualDisk"
        Directory = "Directory"


    class ReloadTarget(Enum):
        currentConfig = "currentConfig"
        snapshotConfig = "snapshotConfig"


class MaintenanceSpec(vmodl.DynamicData):
    @property
    def vsanMode(self) -> DecommissionMode: ...
    @vsanMode.setter
    def vsanMode(self, value: DecommissionMode):
        self._vsanMode = value
    @property
    def purpose(self) -> str: ...
    @purpose.setter
    def purpose(self, value: str):
        self._purpose = value


    class Purpose(Enum):
        hostUpgrade = "hostUpgrade"


class MemorySpec(vmodl.DynamicData):
    @property
    def serviceConsoleReservation(self) -> long: ...
    @serviceConsoleReservation.setter
    def serviceConsoleReservation(self, value: long):
        self._serviceConsoleReservation = value


class MemoryTierInfo(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def flags(self) -> List[str]: ...
    @flags.setter
    def flags(self, value: List[str]):
        self._flags = value
    @property
    def size(self) -> long: ...
    @size.setter
    def size(self, value: long):
        self._size = value


class MountInfo(vmodl.DynamicData):
    @property
    def path(self) -> str: ...
    @path.setter
    def path(self, value: str):
        self._path = value
    @property
    def accessMode(self) -> str: ...
    @accessMode.setter
    def accessMode(self, value: str):
        self._accessMode = value
    @property
    def mounted(self) -> bool: ...
    @mounted.setter
    def mounted(self, value: bool):
        self._mounted = value
    @property
    def accessible(self) -> bool: ...
    @accessible.setter
    def accessible(self, value: bool):
        self._accessible = value
    @property
    def inaccessibleReason(self) -> str: ...
    @inaccessibleReason.setter
    def inaccessibleReason(self, value: str):
        self._inaccessibleReason = value
    @property
    def vmknicName(self) -> str: ...
    @vmknicName.setter
    def vmknicName(self, value: str):
        self._vmknicName = value
    @property
    def vmknicActive(self) -> bool: ...
    @vmknicActive.setter
    def vmknicActive(self, value: bool):
        self._vmknicActive = value
    @property
    def mountFailedReason(self) -> str: ...
    @mountFailedReason.setter
    def mountFailedReason(self, value: str):
        self._mountFailedReason = value
    @property
    def numTcpConnections(self) -> int: ...
    @numTcpConnections.setter
    def numTcpConnections(self, value: int):
        self._numTcpConnections = value


    class InaccessibleReason(Enum):
        AllPathsDown_Start = "AllPathsDown_Start"
        AllPathsDown_Timeout = "AllPathsDown_Timeout"
        PermanentDeviceLoss = "PermanentDeviceLoss"


    class MountFailedReason(Enum):
        CONNECT_FAILURE = "CONNECT_FAILURE"
        MOUNT_NOT_SUPPORTED = "MOUNT_NOT_SUPPORTED"
        NFS_NOT_SUPPORTED = "NFS_NOT_SUPPORTED"
        MOUNT_DENIED = "MOUNT_DENIED"
        MOUNT_NOT_DIR = "MOUNT_NOT_DIR"
        VOLUME_LIMIT_EXCEEDED = "VOLUME_LIMIT_EXCEEDED"
        CONN_LIMIT_EXCEEDED = "CONN_LIMIT_EXCEEDED"
        MOUNT_EXISTS = "MOUNT_EXISTS"
        OTHERS = "OTHERS"


class MultipathInfo(vmodl.DynamicData):
    @property
    def lun(self) -> List[MultipathInfo.LogicalUnit]: ...
    @lun.setter
    def lun(self, value: List[MultipathInfo.LogicalUnit]):
        self._lun = value


    class FixedLogicalUnitPolicy(MultipathInfo.LogicalUnitPolicy):
        @property
        def prefer(self) -> str: ...
        @prefer.setter
        def prefer(self, value: str):
            self._prefer = value


    class HppLogicalUnitPolicy(MultipathInfo.LogicalUnitPolicy):
        @property
        def bytes(self) -> long: ...
        @bytes.setter
        def bytes(self, value: long):
            self._bytes = value
        @property
        def iops(self) -> long: ...
        @iops.setter
        def iops(self, value: long):
            self._iops = value
        @property
        def path(self) -> str: ...
        @path.setter
        def path(self, value: str):
            self._path = value
        @property
        def latencyEvalTime(self) -> long: ...
        @latencyEvalTime.setter
        def latencyEvalTime(self, value: long):
            self._latencyEvalTime = value
        @property
        def samplingIosPerPath(self) -> long: ...
        @samplingIosPerPath.setter
        def samplingIosPerPath(self, value: long):
            self._samplingIosPerPath = value


    class LogicalUnit(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def id(self) -> str: ...
        @id.setter
        def id(self, value: str):
            self._id = value
        @property
        def lun(self) -> Link: ...
        @lun.setter
        def lun(self, value: Link):
            self._lun = value
        @property
        def path(self) -> List[MultipathInfo.Path]: ...
        @path.setter
        def path(self, value: List[MultipathInfo.Path]):
            self._path = value
        @property
        def policy(self) -> MultipathInfo.LogicalUnitPolicy: ...
        @policy.setter
        def policy(self, value: MultipathInfo.LogicalUnitPolicy):
            self._policy = value
        @property
        def storageArrayTypePolicy(self) -> MultipathInfo.LogicalUnitStorageArrayTypePolicy: ...
        @storageArrayTypePolicy.setter
        def storageArrayTypePolicy(self, value: MultipathInfo.LogicalUnitStorageArrayTypePolicy):
            self._storageArrayTypePolicy = value


    class LogicalUnitPolicy(vmodl.DynamicData):
        @property
        def policy(self) -> str: ...
        @policy.setter
        def policy(self, value: str):
            self._policy = value


    class LogicalUnitStorageArrayTypePolicy(vmodl.DynamicData):
        @property
        def policy(self) -> str: ...
        @policy.setter
        def policy(self, value: str):
            self._policy = value


    class Path(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def pathState(self) -> str: ...
        @pathState.setter
        def pathState(self, value: str):
            self._pathState = value
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value
        @property
        def isWorkingPath(self) -> bool: ...
        @isWorkingPath.setter
        def isWorkingPath(self, value: bool):
            self._isWorkingPath = value
        @property
        def adapter(self) -> Link: ...
        @adapter.setter
        def adapter(self, value: Link):
            self._adapter = value
        @property
        def lun(self) -> Link: ...
        @lun.setter
        def lun(self, value: Link):
            self._lun = value
        @property
        def transport(self) -> TargetTransport: ...
        @transport.setter
        def transport(self, value: TargetTransport):
            self._transport = value


    class PathState(Enum):
        standby = "standby"
        active = "active"
        disabled = "disabled"
        dead = "dead"
        unknown = "unknown"


class MultipathStateInfo(vmodl.DynamicData):
    @property
    def path(self) -> List[MultipathStateInfo.Path]: ...
    @path.setter
    def path(self, value: List[MultipathStateInfo.Path]):
        self._path = value


    class Path(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def pathState(self) -> str: ...
        @pathState.setter
        def pathState(self, value: str):
            self._pathState = value


class NasDatastoreInfo(vim.Datastore.Info):
    @property
    def nas(self) -> NasVolume: ...
    @nas.setter
    def nas(self, value: NasVolume):
        self._nas = value


class NasVolume(FileSystemVolume):
    @property
    def remoteHost(self) -> str: ...
    @remoteHost.setter
    def remoteHost(self, value: str):
        self._remoteHost = value
    @property
    def remotePath(self) -> str: ...
    @remotePath.setter
    def remotePath(self, value: str):
        self._remotePath = value
    @property
    def userName(self) -> str: ...
    @userName.setter
    def userName(self, value: str):
        self._userName = value
    @property
    def remoteHostNames(self) -> List[str]: ...
    @remoteHostNames.setter
    def remoteHostNames(self, value: List[str]):
        self._remoteHostNames = value
    @property
    def securityType(self) -> str: ...
    @securityType.setter
    def securityType(self, value: str):
        self._securityType = value
    @property
    def protocolEndpoint(self) -> bool: ...
    @protocolEndpoint.setter
    def protocolEndpoint(self, value: bool):
        self._protocolEndpoint = value


    class Config(vmodl.DynamicData):
        @property
        def changeOperation(self) -> str: ...
        @changeOperation.setter
        def changeOperation(self, value: str):
            self._changeOperation = value
        @property
        def spec(self) -> NasVolume.Specification: ...
        @spec.setter
        def spec(self, value: NasVolume.Specification):
            self._spec = value


    class Specification(vmodl.DynamicData):
        @property
        def remoteHost(self) -> str: ...
        @remoteHost.setter
        def remoteHost(self, value: str):
            self._remoteHost = value
        @property
        def remotePath(self) -> str: ...
        @remotePath.setter
        def remotePath(self, value: str):
            self._remotePath = value
        @property
        def localPath(self) -> str: ...
        @localPath.setter
        def localPath(self, value: str):
            self._localPath = value
        @property
        def accessMode(self) -> str: ...
        @accessMode.setter
        def accessMode(self, value: str):
            self._accessMode = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def userName(self) -> str: ...
        @userName.setter
        def userName(self, value: str):
            self._userName = value
        @property
        def password(self) -> str: ...
        @password.setter
        def password(self, value: str):
            self._password = value
        @property
        def remoteHostNames(self) -> List[str]: ...
        @remoteHostNames.setter
        def remoteHostNames(self, value: List[str]):
            self._remoteHostNames = value
        @property
        def securityType(self) -> str: ...
        @securityType.setter
        def securityType(self, value: str):
            self._securityType = value
        @property
        def vmknicToBind(self) -> str: ...
        @vmknicToBind.setter
        def vmknicToBind(self, value: str):
            self._vmknicToBind = value
        @property
        def vmknicBound(self) -> bool: ...
        @vmknicBound.setter
        def vmknicBound(self, value: bool):
            self._vmknicBound = value
        @property
        def connections(self) -> int: ...
        @connections.setter
        def connections(self, value: int):
            self._connections = value


    class UserInfo(vmodl.DynamicData):
        @property
        def user(self) -> str: ...
        @user.setter
        def user(self, value: str):
            self._user = value


    class SecurityType(Enum):
        AUTH_SYS = "AUTH_SYS"
        SEC_KRB5 = "SEC_KRB5"
        SEC_KRB5I = "SEC_KRB5I"


class NatService(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def spec(self) -> NatService.Specification: ...
    @spec.setter
    def spec(self, value: NatService.Specification):
        self._spec = value


    class Config(vmodl.DynamicData):
        @property
        def changeOperation(self) -> str: ...
        @changeOperation.setter
        def changeOperation(self, value: str):
            self._changeOperation = value
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def spec(self) -> NatService.Specification: ...
        @spec.setter
        def spec(self, value: NatService.Specification):
            self._spec = value


    class NameServiceSpec(vmodl.DynamicData):
        @property
        def dnsAutoDetect(self) -> bool: ...
        @dnsAutoDetect.setter
        def dnsAutoDetect(self, value: bool):
            self._dnsAutoDetect = value
        @property
        def dnsPolicy(self) -> str: ...
        @dnsPolicy.setter
        def dnsPolicy(self, value: str):
            self._dnsPolicy = value
        @property
        def dnsRetries(self) -> int: ...
        @dnsRetries.setter
        def dnsRetries(self, value: int):
            self._dnsRetries = value
        @property
        def dnsTimeout(self) -> int: ...
        @dnsTimeout.setter
        def dnsTimeout(self, value: int):
            self._dnsTimeout = value
        @property
        def dnsNameServer(self) -> List[str]: ...
        @dnsNameServer.setter
        def dnsNameServer(self, value: List[str]):
            self._dnsNameServer = value
        @property
        def nbdsTimeout(self) -> int: ...
        @nbdsTimeout.setter
        def nbdsTimeout(self, value: int):
            self._nbdsTimeout = value
        @property
        def nbnsRetries(self) -> int: ...
        @nbnsRetries.setter
        def nbnsRetries(self, value: int):
            self._nbnsRetries = value
        @property
        def nbnsTimeout(self) -> int: ...
        @nbnsTimeout.setter
        def nbnsTimeout(self, value: int):
            self._nbnsTimeout = value


    class PortForwardSpecification(vmodl.DynamicData):
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def hostPort(self) -> int: ...
        @hostPort.setter
        def hostPort(self, value: int):
            self._hostPort = value
        @property
        def guestPort(self) -> int: ...
        @guestPort.setter
        def guestPort(self, value: int):
            self._guestPort = value
        @property
        def guestIpAddress(self) -> str: ...
        @guestIpAddress.setter
        def guestIpAddress(self, value: str):
            self._guestIpAddress = value


    class Specification(vmodl.DynamicData):
        @property
        def virtualSwitch(self) -> str: ...
        @virtualSwitch.setter
        def virtualSwitch(self, value: str):
            self._virtualSwitch = value
        @property
        def activeFtp(self) -> bool: ...
        @activeFtp.setter
        def activeFtp(self, value: bool):
            self._activeFtp = value
        @property
        def allowAnyOui(self) -> bool: ...
        @allowAnyOui.setter
        def allowAnyOui(self, value: bool):
            self._allowAnyOui = value
        @property
        def configPort(self) -> bool: ...
        @configPort.setter
        def configPort(self, value: bool):
            self._configPort = value
        @property
        def ipGatewayAddress(self) -> str: ...
        @ipGatewayAddress.setter
        def ipGatewayAddress(self, value: str):
            self._ipGatewayAddress = value
        @property
        def udpTimeout(self) -> int: ...
        @udpTimeout.setter
        def udpTimeout(self, value: int):
            self._udpTimeout = value
        @property
        def portForward(self) -> List[NatService.PortForwardSpecification]: ...
        @portForward.setter
        def portForward(self, value: List[NatService.PortForwardSpecification]):
            self._portForward = value
        @property
        def nameService(self) -> NatService.NameServiceSpec: ...
        @nameService.setter
        def nameService(self, value: NatService.NameServiceSpec):
            self._nameService = value


class NetCapabilities(vmodl.DynamicData):
    @property
    def canSetPhysicalNicLinkSpeed(self) -> bool: ...
    @canSetPhysicalNicLinkSpeed.setter
    def canSetPhysicalNicLinkSpeed(self, value: bool):
        self._canSetPhysicalNicLinkSpeed = value
    @property
    def supportsNicTeaming(self) -> bool: ...
    @supportsNicTeaming.setter
    def supportsNicTeaming(self, value: bool):
        self._supportsNicTeaming = value
    @property
    def nicTeamingPolicy(self) -> List[str]: ...
    @nicTeamingPolicy.setter
    def nicTeamingPolicy(self, value: List[str]):
        self._nicTeamingPolicy = value
    @property
    def supportsVlan(self) -> bool: ...
    @supportsVlan.setter
    def supportsVlan(self, value: bool):
        self._supportsVlan = value
    @property
    def usesServiceConsoleNic(self) -> bool: ...
    @usesServiceConsoleNic.setter
    def usesServiceConsoleNic(self, value: bool):
        self._usesServiceConsoleNic = value
    @property
    def supportsNetworkHints(self) -> bool: ...
    @supportsNetworkHints.setter
    def supportsNetworkHints(self, value: bool):
        self._supportsNetworkHints = value
    @property
    def maxPortGroupsPerVswitch(self) -> int: ...
    @maxPortGroupsPerVswitch.setter
    def maxPortGroupsPerVswitch(self, value: int):
        self._maxPortGroupsPerVswitch = value
    @property
    def vswitchConfigSupported(self) -> bool: ...
    @vswitchConfigSupported.setter
    def vswitchConfigSupported(self, value: bool):
        self._vswitchConfigSupported = value
    @property
    def vnicConfigSupported(self) -> bool: ...
    @vnicConfigSupported.setter
    def vnicConfigSupported(self, value: bool):
        self._vnicConfigSupported = value
    @property
    def ipRouteConfigSupported(self) -> bool: ...
    @ipRouteConfigSupported.setter
    def ipRouteConfigSupported(self, value: bool):
        self._ipRouteConfigSupported = value
    @property
    def dnsConfigSupported(self) -> bool: ...
    @dnsConfigSupported.setter
    def dnsConfigSupported(self, value: bool):
        self._dnsConfigSupported = value
    @property
    def dhcpOnVnicSupported(self) -> bool: ...
    @dhcpOnVnicSupported.setter
    def dhcpOnVnicSupported(self, value: bool):
        self._dhcpOnVnicSupported = value
    @property
    def ipV6Supported(self) -> bool: ...
    @ipV6Supported.setter
    def ipV6Supported(self, value: bool):
        self._ipV6Supported = value
    @property
    def backupNfcNiocSupported(self) -> bool: ...
    @backupNfcNiocSupported.setter
    def backupNfcNiocSupported(self, value: bool):
        self._backupNfcNiocSupported = value


class NetOffloadCapabilities(vmodl.DynamicData):
    @property
    def csumOffload(self) -> bool: ...
    @csumOffload.setter
    def csumOffload(self, value: bool):
        self._csumOffload = value
    @property
    def tcpSegmentation(self) -> bool: ...
    @tcpSegmentation.setter
    def tcpSegmentation(self, value: bool):
        self._tcpSegmentation = value
    @property
    def zeroCopyXmit(self) -> bool: ...
    @zeroCopyXmit.setter
    def zeroCopyXmit(self, value: bool):
        self._zeroCopyXmit = value


class NetStackInstance(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def dnsConfig(self) -> DnsConfig: ...
    @dnsConfig.setter
    def dnsConfig(self, value: DnsConfig):
        self._dnsConfig = value
    @property
    def ipRouteConfig(self) -> IpRouteConfig: ...
    @ipRouteConfig.setter
    def ipRouteConfig(self, value: IpRouteConfig):
        self._ipRouteConfig = value
    @property
    def requestedMaxNumberOfConnections(self) -> int: ...
    @requestedMaxNumberOfConnections.setter
    def requestedMaxNumberOfConnections(self, value: int):
        self._requestedMaxNumberOfConnections = value
    @property
    def congestionControlAlgorithm(self) -> str: ...
    @congestionControlAlgorithm.setter
    def congestionControlAlgorithm(self, value: str):
        self._congestionControlAlgorithm = value
    @property
    def ipV6Enabled(self) -> bool: ...
    @ipV6Enabled.setter
    def ipV6Enabled(self, value: bool):
        self._ipV6Enabled = value
    @property
    def routeTableConfig(self) -> IpRouteTableConfig: ...
    @routeTableConfig.setter
    def routeTableConfig(self, value: IpRouteTableConfig):
        self._routeTableConfig = value


    class CongestionControlAlgorithmType(Enum):
        newreno = "newreno"
        cubic = "cubic"


    class SystemStackKey(Enum):
        defaultTcpipStack = "defaultTcpipStack"
        vmotion = "vmotion"
        vSphereProvisioning = "vSphereProvisioning"
        mirror = "mirror"
        ops = "ops"


class NetworkConfig(vmodl.DynamicData):
    @property
    def vswitch(self) -> List[VirtualSwitch.Config]: ...
    @vswitch.setter
    def vswitch(self, value: List[VirtualSwitch.Config]):
        self._vswitch = value
    @property
    def proxySwitch(self) -> List[HostProxySwitch.Config]: ...
    @proxySwitch.setter
    def proxySwitch(self, value: List[HostProxySwitch.Config]):
        self._proxySwitch = value
    @property
    def portgroup(self) -> List[PortGroup.Config]: ...
    @portgroup.setter
    def portgroup(self, value: List[PortGroup.Config]):
        self._portgroup = value
    @property
    def pnic(self) -> List[PhysicalNic.Config]: ...
    @pnic.setter
    def pnic(self, value: List[PhysicalNic.Config]):
        self._pnic = value
    @property
    def vnic(self) -> List[VirtualNic.Config]: ...
    @vnic.setter
    def vnic(self, value: List[VirtualNic.Config]):
        self._vnic = value
    @property
    def consoleVnic(self) -> List[VirtualNic.Config]: ...
    @consoleVnic.setter
    def consoleVnic(self, value: List[VirtualNic.Config]):
        self._consoleVnic = value
    @property
    def dnsConfig(self) -> DnsConfig: ...
    @dnsConfig.setter
    def dnsConfig(self, value: DnsConfig):
        self._dnsConfig = value
    @property
    def ipRouteConfig(self) -> IpRouteConfig: ...
    @ipRouteConfig.setter
    def ipRouteConfig(self, value: IpRouteConfig):
        self._ipRouteConfig = value
    @property
    def consoleIpRouteConfig(self) -> IpRouteConfig: ...
    @consoleIpRouteConfig.setter
    def consoleIpRouteConfig(self, value: IpRouteConfig):
        self._consoleIpRouteConfig = value
    @property
    def routeTableConfig(self) -> IpRouteTableConfig: ...
    @routeTableConfig.setter
    def routeTableConfig(self, value: IpRouteTableConfig):
        self._routeTableConfig = value
    @property
    def dhcp(self) -> List[DhcpService.Config]: ...
    @dhcp.setter
    def dhcp(self, value: List[DhcpService.Config]):
        self._dhcp = value
    @property
    def nat(self) -> List[NatService.Config]: ...
    @nat.setter
    def nat(self, value: List[NatService.Config]):
        self._nat = value
    @property
    def ipV6Enabled(self) -> bool: ...
    @ipV6Enabled.setter
    def ipV6Enabled(self, value: bool):
        self._ipV6Enabled = value
    @property
    def netStackSpec(self) -> List[NetworkConfig.NetStackSpec]: ...
    @netStackSpec.setter
    def netStackSpec(self, value: List[NetworkConfig.NetStackSpec]):
        self._netStackSpec = value
    @property
    def migrationStatus(self) -> str: ...
    @migrationStatus.setter
    def migrationStatus(self, value: str):
        self._migrationStatus = value


    class NetStackSpec(vmodl.DynamicData):
        @property
        def netStackInstance(self) -> NetStackInstance: ...
        @netStackInstance.setter
        def netStackInstance(self, value: NetStackInstance):
            self._netStackInstance = value
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value


    class Result(vmodl.DynamicData):
        @property
        def vnicDevice(self) -> List[str]: ...
        @vnicDevice.setter
        def vnicDevice(self, value: List[str]):
            self._vnicDevice = value
        @property
        def consoleVnicDevice(self) -> List[str]: ...
        @consoleVnicDevice.setter
        def consoleVnicDevice(self, value: List[str]):
            self._consoleVnicDevice = value


class NetworkInfo(vmodl.DynamicData):
    @property
    def vswitch(self) -> List[VirtualSwitch]: ...
    @vswitch.setter
    def vswitch(self, value: List[VirtualSwitch]):
        self._vswitch = value
    @property
    def proxySwitch(self) -> List[HostProxySwitch]: ...
    @proxySwitch.setter
    def proxySwitch(self, value: List[HostProxySwitch]):
        self._proxySwitch = value
    @property
    def portgroup(self) -> List[PortGroup]: ...
    @portgroup.setter
    def portgroup(self, value: List[PortGroup]):
        self._portgroup = value
    @property
    def pnic(self) -> List[PhysicalNic]: ...
    @pnic.setter
    def pnic(self, value: List[PhysicalNic]):
        self._pnic = value
    @property
    def rdmaDevice(self) -> List[RdmaDevice]: ...
    @rdmaDevice.setter
    def rdmaDevice(self, value: List[RdmaDevice]):
        self._rdmaDevice = value
    @property
    def vnic(self) -> List[VirtualNic]: ...
    @vnic.setter
    def vnic(self, value: List[VirtualNic]):
        self._vnic = value
    @property
    def consoleVnic(self) -> List[VirtualNic]: ...
    @consoleVnic.setter
    def consoleVnic(self, value: List[VirtualNic]):
        self._consoleVnic = value
    @property
    def dnsConfig(self) -> DnsConfig: ...
    @dnsConfig.setter
    def dnsConfig(self, value: DnsConfig):
        self._dnsConfig = value
    @property
    def ipRouteConfig(self) -> IpRouteConfig: ...
    @ipRouteConfig.setter
    def ipRouteConfig(self, value: IpRouteConfig):
        self._ipRouteConfig = value
    @property
    def consoleIpRouteConfig(self) -> IpRouteConfig: ...
    @consoleIpRouteConfig.setter
    def consoleIpRouteConfig(self, value: IpRouteConfig):
        self._consoleIpRouteConfig = value
    @property
    def routeTableInfo(self) -> IpRouteTableInfo: ...
    @routeTableInfo.setter
    def routeTableInfo(self, value: IpRouteTableInfo):
        self._routeTableInfo = value
    @property
    def dhcp(self) -> List[DhcpService]: ...
    @dhcp.setter
    def dhcp(self, value: List[DhcpService]):
        self._dhcp = value
    @property
    def nat(self) -> List[NatService]: ...
    @nat.setter
    def nat(self, value: List[NatService]):
        self._nat = value
    @property
    def ipV6Enabled(self) -> bool: ...
    @ipV6Enabled.setter
    def ipV6Enabled(self, value: bool):
        self._ipV6Enabled = value
    @property
    def atBootIpV6Enabled(self) -> bool: ...
    @atBootIpV6Enabled.setter
    def atBootIpV6Enabled(self, value: bool):
        self._atBootIpV6Enabled = value
    @property
    def netStackInstance(self) -> List[NetStackInstance]: ...
    @netStackInstance.setter
    def netStackInstance(self, value: List[NetStackInstance]):
        self._netStackInstance = value
    @property
    def opaqueSwitch(self) -> List[OpaqueSwitch]: ...
    @opaqueSwitch.setter
    def opaqueSwitch(self, value: List[OpaqueSwitch]):
        self._opaqueSwitch = value
    @property
    def opaqueNetwork(self) -> List[OpaqueNetworkInfo]: ...
    @opaqueNetwork.setter
    def opaqueNetwork(self, value: List[OpaqueNetworkInfo]):
        self._opaqueNetwork = value
    @property
    def nsxTransportNodeId(self) -> str: ...
    @nsxTransportNodeId.setter
    def nsxTransportNodeId(self, value: str):
        self._nsxTransportNodeId = value
    @property
    def nvdsToVdsMigrationRequired(self) -> bool: ...
    @nvdsToVdsMigrationRequired.setter
    def nvdsToVdsMigrationRequired(self, value: bool):
        self._nvdsToVdsMigrationRequired = value
    @property
    def migrationStatus(self) -> str: ...
    @migrationStatus.setter
    def migrationStatus(self, value: str):
        self._migrationStatus = value


class NetworkPolicy(vmodl.DynamicData):
    @property
    def security(self) -> NetworkPolicy.SecurityPolicy: ...
    @security.setter
    def security(self, value: NetworkPolicy.SecurityPolicy):
        self._security = value
    @property
    def nicTeaming(self) -> NetworkPolicy.NicTeamingPolicy: ...
    @nicTeaming.setter
    def nicTeaming(self, value: NetworkPolicy.NicTeamingPolicy):
        self._nicTeaming = value
    @property
    def offloadPolicy(self) -> NetOffloadCapabilities: ...
    @offloadPolicy.setter
    def offloadPolicy(self, value: NetOffloadCapabilities):
        self._offloadPolicy = value
    @property
    def shapingPolicy(self) -> NetworkPolicy.TrafficShapingPolicy: ...
    @shapingPolicy.setter
    def shapingPolicy(self, value: NetworkPolicy.TrafficShapingPolicy):
        self._shapingPolicy = value


    class NicFailureCriteria(vmodl.DynamicData):
        @property
        def checkSpeed(self) -> str: ...
        @checkSpeed.setter
        def checkSpeed(self, value: str):
            self._checkSpeed = value
        @property
        def speed(self) -> int: ...
        @speed.setter
        def speed(self, value: int):
            self._speed = value
        @property
        def checkDuplex(self) -> bool: ...
        @checkDuplex.setter
        def checkDuplex(self, value: bool):
            self._checkDuplex = value
        @property
        def fullDuplex(self) -> bool: ...
        @fullDuplex.setter
        def fullDuplex(self, value: bool):
            self._fullDuplex = value
        @property
        def checkErrorPercent(self) -> bool: ...
        @checkErrorPercent.setter
        def checkErrorPercent(self, value: bool):
            self._checkErrorPercent = value
        @property
        def percentage(self) -> int: ...
        @percentage.setter
        def percentage(self, value: int):
            self._percentage = value
        @property
        def checkBeacon(self) -> bool: ...
        @checkBeacon.setter
        def checkBeacon(self, value: bool):
            self._checkBeacon = value


    class NicOrderPolicy(vmodl.DynamicData):
        @property
        def activeNic(self) -> List[str]: ...
        @activeNic.setter
        def activeNic(self, value: List[str]):
            self._activeNic = value
        @property
        def standbyNic(self) -> List[str]: ...
        @standbyNic.setter
        def standbyNic(self, value: List[str]):
            self._standbyNic = value


    class NicTeamingPolicy(vmodl.DynamicData):
        @property
        def policy(self) -> str: ...
        @policy.setter
        def policy(self, value: str):
            self._policy = value
        @property
        def reversePolicy(self) -> bool: ...
        @reversePolicy.setter
        def reversePolicy(self, value: bool):
            self._reversePolicy = value
        @property
        def notifySwitches(self) -> bool: ...
        @notifySwitches.setter
        def notifySwitches(self, value: bool):
            self._notifySwitches = value
        @property
        def rollingOrder(self) -> bool: ...
        @rollingOrder.setter
        def rollingOrder(self, value: bool):
            self._rollingOrder = value
        @property
        def failureCriteria(self) -> NetworkPolicy.NicFailureCriteria: ...
        @failureCriteria.setter
        def failureCriteria(self, value: NetworkPolicy.NicFailureCriteria):
            self._failureCriteria = value
        @property
        def nicOrder(self) -> NetworkPolicy.NicOrderPolicy: ...
        @nicOrder.setter
        def nicOrder(self, value: NetworkPolicy.NicOrderPolicy):
            self._nicOrder = value


    class SecurityPolicy(vmodl.DynamicData):
        @property
        def allowPromiscuous(self) -> bool: ...
        @allowPromiscuous.setter
        def allowPromiscuous(self, value: bool):
            self._allowPromiscuous = value
        @property
        def macChanges(self) -> bool: ...
        @macChanges.setter
        def macChanges(self, value: bool):
            self._macChanges = value
        @property
        def forgedTransmits(self) -> bool: ...
        @forgedTransmits.setter
        def forgedTransmits(self, value: bool):
            self._forgedTransmits = value


    class TrafficShapingPolicy(vmodl.DynamicData):
        @property
        def enabled(self) -> bool: ...
        @enabled.setter
        def enabled(self, value: bool):
            self._enabled = value
        @property
        def averageBandwidth(self) -> long: ...
        @averageBandwidth.setter
        def averageBandwidth(self, value: long):
            self._averageBandwidth = value
        @property
        def peakBandwidth(self) -> long: ...
        @peakBandwidth.setter
        def peakBandwidth(self, value: long):
            self._peakBandwidth = value
        @property
        def burstSize(self) -> long: ...
        @burstSize.setter
        def burstSize(self, value: long):
            self._burstSize = value


class NfcConnectionInfo(DataTransportConnectionInfo):
    @property
    def streamingMemoryConsumed(self) -> long: ...
    @streamingMemoryConsumed.setter
    def streamingMemoryConsumed(self, value: long):
        self._streamingMemoryConsumed = value


class NtpConfig(vmodl.DynamicData):
    @property
    def server(self) -> List[str]: ...
    @server.setter
    def server(self, value: List[str]):
        self._server = value
    @property
    def configFile(self) -> List[str]: ...
    @configFile.setter
    def configFile(self, value: List[str]):
        self._configFile = value


class NumaInfo(vmodl.DynamicData):
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def numNodes(self) -> int: ...
    @numNodes.setter
    def numNodes(self, value: int):
        self._numNodes = value
    @property
    def numaNode(self) -> List[NumaNode]: ...
    @numaNode.setter
    def numaNode(self, value: List[NumaNode]):
        self._numaNode = value


class NumaNode(vmodl.DynamicData):
    @property
    def typeId(self) -> byte: ...
    @typeId.setter
    def typeId(self, value: byte):
        self._typeId = value
    @property
    def cpuID(self) -> List[short]: ...
    @cpuID.setter
    def cpuID(self, value: List[short]):
        self._cpuID = value
    @property
    def memorySize(self) -> long: ...
    @memorySize.setter
    def memorySize(self, value: long):
        self._memorySize = value
    @property
    def memoryRangeBegin(self) -> long: ...
    @memoryRangeBegin.setter
    def memoryRangeBegin(self, value: long):
        self._memoryRangeBegin = value
    @property
    def memoryRangeLength(self) -> long: ...
    @memoryRangeLength.setter
    def memoryRangeLength(self, value: long):
        self._memoryRangeLength = value
    @property
    def pciId(self) -> List[str]: ...
    @pciId.setter
    def pciId(self, value: List[str]):
        self._pciId = value


class NumericSensorInfo(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def healthState(self) -> vim.ElementDescription: ...
    @healthState.setter
    def healthState(self, value: vim.ElementDescription):
        self._healthState = value
    @property
    def currentReading(self) -> long: ...
    @currentReading.setter
    def currentReading(self, value: long):
        self._currentReading = value
    @property
    def unitModifier(self) -> int: ...
    @unitModifier.setter
    def unitModifier(self, value: int):
        self._unitModifier = value
    @property
    def baseUnits(self) -> str: ...
    @baseUnits.setter
    def baseUnits(self, value: str):
        self._baseUnits = value
    @property
    def rateUnits(self) -> str: ...
    @rateUnits.setter
    def rateUnits(self, value: str):
        self._rateUnits = value
    @property
    def sensorType(self) -> str: ...
    @sensorType.setter
    def sensorType(self, value: str):
        self._sensorType = value
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def sensorNumber(self) -> long: ...
    @sensorNumber.setter
    def sensorNumber(self, value: long):
        self._sensorNumber = value
    @property
    def timeStamp(self) -> str: ...
    @timeStamp.setter
    def timeStamp(self, value: str):
        self._timeStamp = value
    @property
    def fru(self) -> Fru: ...
    @fru.setter
    def fru(self, value: Fru):
        self._fru = value


    class HealthState(Enum):
        unknown = "unknown"
        green = "green"
        yellow = "yellow"
        red = "red"


    class SensorType(Enum):
        fan = "fan"
        power = "power"
        temperature = "temperature"
        voltage = "voltage"
        other = "other"
        processor = "processor"
        memory = "memory"
        storage = "storage"
        systemBoard = "systemBoard"
        battery = "battery"
        bios = "bios"
        cable = "cable"
        watchdog = "watchdog"


class NvmeConnectSpec(NvmeSpec):
    @property
    def subnqn(self) -> str: ...
    @subnqn.setter
    def subnqn(self, value: str):
        self._subnqn = value
    @property
    def controllerId(self) -> int: ...
    @controllerId.setter
    def controllerId(self, value: int):
        self._controllerId = value
    @property
    def adminQueueSize(self) -> int: ...
    @adminQueueSize.setter
    def adminQueueSize(self, value: int):
        self._adminQueueSize = value
    @property
    def keepAliveTimeout(self) -> int: ...
    @keepAliveTimeout.setter
    def keepAliveTimeout(self, value: int):
        self._keepAliveTimeout = value


class NvmeController(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def controllerNumber(self) -> int: ...
    @controllerNumber.setter
    def controllerNumber(self, value: int):
        self._controllerNumber = value
    @property
    def subnqn(self) -> str: ...
    @subnqn.setter
    def subnqn(self, value: str):
        self._subnqn = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def associatedAdapter(self) -> Link: ...
    @associatedAdapter.setter
    def associatedAdapter(self, value: Link):
        self._associatedAdapter = value
    @property
    def transportType(self) -> str: ...
    @transportType.setter
    def transportType(self, value: str):
        self._transportType = value
    @property
    def fusedOperationSupported(self) -> bool: ...
    @fusedOperationSupported.setter
    def fusedOperationSupported(self, value: bool):
        self._fusedOperationSupported = value
    @property
    def numberOfQueues(self) -> int: ...
    @numberOfQueues.setter
    def numberOfQueues(self, value: int):
        self._numberOfQueues = value
    @property
    def queueSize(self) -> int: ...
    @queueSize.setter
    def queueSize(self, value: int):
        self._queueSize = value
    @property
    def attachedNamespace(self) -> List[NvmeNamespace]: ...
    @attachedNamespace.setter
    def attachedNamespace(self, value: List[NvmeNamespace]):
        self._attachedNamespace = value
    @property
    def vendorId(self) -> str: ...
    @vendorId.setter
    def vendorId(self, value: str):
        self._vendorId = value
    @property
    def model(self) -> str: ...
    @model.setter
    def model(self, value: str):
        self._model = value
    @property
    def serialNumber(self) -> str: ...
    @serialNumber.setter
    def serialNumber(self, value: str):
        self._serialNumber = value
    @property
    def firmwareVersion(self) -> str: ...
    @firmwareVersion.setter
    def firmwareVersion(self, value: str):
        self._firmwareVersion = value


class NvmeDisconnectSpec(vmodl.DynamicData):
    @property
    def hbaName(self) -> str: ...
    @hbaName.setter
    def hbaName(self, value: str):
        self._hbaName = value
    @property
    def subnqn(self) -> str: ...
    @subnqn.setter
    def subnqn(self, value: str):
        self._subnqn = value
    @property
    def controllerNumber(self) -> int: ...
    @controllerNumber.setter
    def controllerNumber(self, value: int):
        self._controllerNumber = value


class NvmeDiscoverSpec(NvmeSpec):
    @property
    def autoConnect(self) -> bool: ...
    @autoConnect.setter
    def autoConnect(self, value: bool):
        self._autoConnect = value
    @property
    def rootDiscoveryController(self) -> bool: ...
    @rootDiscoveryController.setter
    def rootDiscoveryController(self, value: bool):
        self._rootDiscoveryController = value


class NvmeDiscoveryLog(vmodl.DynamicData):
    @property
    def entry(self) -> List[NvmeDiscoveryLog.Entry]: ...
    @entry.setter
    def entry(self, value: List[NvmeDiscoveryLog.Entry]):
        self._entry = value
    @property
    def complete(self) -> bool: ...
    @complete.setter
    def complete(self, value: bool):
        self._complete = value


    class Entry(vmodl.DynamicData):
        @property
        def subnqn(self) -> str: ...
        @subnqn.setter
        def subnqn(self, value: str):
            self._subnqn = value
        @property
        def subsystemType(self) -> str: ...
        @subsystemType.setter
        def subsystemType(self, value: str):
            self._subsystemType = value
        @property
        def subsystemPortId(self) -> int: ...
        @subsystemPortId.setter
        def subsystemPortId(self, value: int):
            self._subsystemPortId = value
        @property
        def controllerId(self) -> int: ...
        @controllerId.setter
        def controllerId(self, value: int):
            self._controllerId = value
        @property
        def adminQueueMaxSize(self) -> int: ...
        @adminQueueMaxSize.setter
        def adminQueueMaxSize(self, value: int):
            self._adminQueueMaxSize = value
        @property
        def transportParameters(self) -> NvmeTransportParameters: ...
        @transportParameters.setter
        def transportParameters(self, value: NvmeTransportParameters):
            self._transportParameters = value
        @property
        def transportRequirements(self) -> str: ...
        @transportRequirements.setter
        def transportRequirements(self, value: str):
            self._transportRequirements = value
        @property
        def connected(self) -> bool: ...
        @connected.setter
        def connected(self, value: bool):
            self._connected = value


    class SubsystemType(Enum):
        discovery = "discovery"
        nvm = "nvm"


    class TransportRequirements(Enum):
        secureChannelRequired = "secureChannelRequired"
        secureChannelNotRequired = "secureChannelNotRequired"
        requirementsNotSpecified = "requirementsNotSpecified"


class NvmeNamespace(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def id(self) -> int: ...
    @id.setter
    def id(self, value: int):
        self._id = value
    @property
    def blockSize(self) -> int: ...
    @blockSize.setter
    def blockSize(self, value: int):
        self._blockSize = value
    @property
    def capacityInBlocks(self) -> long: ...
    @capacityInBlocks.setter
    def capacityInBlocks(self, value: long):
        self._capacityInBlocks = value


class NvmeOpaqueTransportParameters(NvmeTransportParameters):
    @property
    def trtype(self) -> str: ...
    @trtype.setter
    def trtype(self, value: str):
        self._trtype = value
    @property
    def traddr(self) -> str: ...
    @traddr.setter
    def traddr(self, value: str):
        self._traddr = value
    @property
    def adrfam(self) -> str: ...
    @adrfam.setter
    def adrfam(self, value: str):
        self._adrfam = value
    @property
    def trsvcid(self) -> str: ...
    @trsvcid.setter
    def trsvcid(self, value: str):
        self._trsvcid = value
    @property
    def tsas(self) -> binary: ...
    @tsas.setter
    def tsas(self, value: binary):
        self._tsas = value


class NvmeOverFibreChannelParameters(NvmeTransportParameters):
    @property
    def nodeWorldWideName(self) -> long: ...
    @nodeWorldWideName.setter
    def nodeWorldWideName(self, value: long):
        self._nodeWorldWideName = value
    @property
    def portWorldWideName(self) -> long: ...
    @portWorldWideName.setter
    def portWorldWideName(self, value: long):
        self._portWorldWideName = value


class NvmeOverRdmaParameters(NvmeTransportParameters):
    @property
    def address(self) -> str: ...
    @address.setter
    def address(self, value: str):
        self._address = value
    @property
    def addressFamily(self) -> str: ...
    @addressFamily.setter
    def addressFamily(self, value: str):
        self._addressFamily = value
    @property
    def portNumber(self) -> int: ...
    @portNumber.setter
    def portNumber(self, value: int):
        self._portNumber = value


class NvmeOverTcpParameters(NvmeTransportParameters):
    @property
    def address(self) -> str: ...
    @address.setter
    def address(self, value: str):
        self._address = value
    @property
    def portNumber(self) -> int: ...
    @portNumber.setter
    def portNumber(self, value: int):
        self._portNumber = value
    @property
    def digestVerification(self) -> str: ...
    @digestVerification.setter
    def digestVerification(self, value: str):
        self._digestVerification = value


class NvmeSpec(vmodl.DynamicData):
    @property
    def hbaName(self) -> str: ...
    @hbaName.setter
    def hbaName(self, value: str):
        self._hbaName = value
    @property
    def transportParameters(self) -> NvmeTransportParameters: ...
    @transportParameters.setter
    def transportParameters(self, value: NvmeTransportParameters):
        self._transportParameters = value


class NvmeTopology(vmodl.DynamicData):
    @property
    def adapter(self) -> List[NvmeTopology.Interface]: ...
    @adapter.setter
    def adapter(self, value: List[NvmeTopology.Interface]):
        self._adapter = value


    class Interface(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def adapter(self) -> Link: ...
        @adapter.setter
        def adapter(self, value: Link):
            self._adapter = value
        @property
        def connectedController(self) -> List[NvmeController]: ...
        @connectedController.setter
        def connectedController(self, value: List[NvmeController]):
            self._connectedController = value


class NvmeTransportParameters(vmodl.DynamicData):


    class NvmeAddressFamily(Enum):
        ipv4 = "ipv4"
        ipv6 = "ipv6"
        infiniBand = "infiniBand"
        fc = "fc"
        loopback = "loopback"
        unknown = "unknown"


class OpaqueNetworkInfo(vmodl.DynamicData):
    @property
    def opaqueNetworkId(self) -> str: ...
    @opaqueNetworkId.setter
    def opaqueNetworkId(self, value: str):
        self._opaqueNetworkId = value
    @property
    def opaqueNetworkName(self) -> str: ...
    @opaqueNetworkName.setter
    def opaqueNetworkName(self, value: str):
        self._opaqueNetworkName = value
    @property
    def opaqueNetworkType(self) -> str: ...
    @opaqueNetworkType.setter
    def opaqueNetworkType(self, value: str):
        self._opaqueNetworkType = value
    @property
    def pnicZone(self) -> List[str]: ...
    @pnicZone.setter
    def pnicZone(self, value: List[str]):
        self._pnicZone = value
    @property
    def capability(self) -> vim.OpaqueNetwork.Capability: ...
    @capability.setter
    def capability(self, value: vim.OpaqueNetwork.Capability):
        self._capability = value
    @property
    def extraConfig(self) -> List[vim.option.OptionValue]: ...
    @extraConfig.setter
    def extraConfig(self, value: List[vim.option.OptionValue]):
        self._extraConfig = value


class OpaqueSwitch(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def pnic(self) -> List[Link]: ...
    @pnic.setter
    def pnic(self, value: List[Link]):
        self._pnic = value
    @property
    def pnicZone(self) -> List[OpaqueSwitch.PhysicalNicZone]: ...
    @pnicZone.setter
    def pnicZone(self, value: List[OpaqueSwitch.PhysicalNicZone]):
        self._pnicZone = value
    @property
    def status(self) -> str: ...
    @status.setter
    def status(self, value: str):
        self._status = value
    @property
    def vtep(self) -> List[VirtualNic]: ...
    @vtep.setter
    def vtep(self, value: List[VirtualNic]):
        self._vtep = value
    @property
    def extraConfig(self) -> List[vim.option.OptionValue]: ...
    @extraConfig.setter
    def extraConfig(self, value: List[vim.option.OptionValue]):
        self._extraConfig = value
    @property
    def featureCapability(self) -> List[FeatureCapability]: ...
    @featureCapability.setter
    def featureCapability(self, value: List[FeatureCapability]):
        self._featureCapability = value


    class PhysicalNicZone(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def pnicDevice(self) -> List[str]: ...
        @pnicDevice.setter
        def pnicDevice(self, value: List[str]):
            self._pnicDevice = value


    class OpaqueSwitchState(Enum):
        up = "up"
        warning = "warning"
        down = "down"
        maintenance = "maintenance"


class PMemDatastoreInfo(vim.Datastore.Info):
    @property
    def pmem(self) -> PMemVolume: ...
    @pmem.setter
    def pmem(self, value: PMemVolume):
        self._pmem = value


class PMemVolume(FileSystemVolume):
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value


class ParallelScsiHba(HostBusAdapter): ...


class ParallelScsiTargetTransport(TargetTransport): ...


class PathSelectionPolicyOption(vmodl.DynamicData):
    @property
    def policy(self) -> vim.ElementDescription: ...
    @policy.setter
    def policy(self, value: vim.ElementDescription):
        self._policy = value


class PciDevice(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def classId(self) -> short: ...
    @classId.setter
    def classId(self, value: short):
        self._classId = value
    @property
    def bus(self) -> byte: ...
    @bus.setter
    def bus(self, value: byte):
        self._bus = value
    @property
    def slot(self) -> byte: ...
    @slot.setter
    def slot(self, value: byte):
        self._slot = value
    @property
    def function(self) -> byte: ...
    @function.setter
    def function(self, value: byte):
        self._function = value
    @property
    def vendorId(self) -> short: ...
    @vendorId.setter
    def vendorId(self, value: short):
        self._vendorId = value
    @property
    def subVendorId(self) -> short: ...
    @subVendorId.setter
    def subVendorId(self, value: short):
        self._subVendorId = value
    @property
    def vendorName(self) -> str: ...
    @vendorName.setter
    def vendorName(self, value: str):
        self._vendorName = value
    @property
    def deviceId(self) -> short: ...
    @deviceId.setter
    def deviceId(self, value: short):
        self._deviceId = value
    @property
    def subDeviceId(self) -> short: ...
    @subDeviceId.setter
    def subDeviceId(self, value: short):
        self._subDeviceId = value
    @property
    def parentBridge(self) -> str: ...
    @parentBridge.setter
    def parentBridge(self, value: str):
        self._parentBridge = value
    @property
    def deviceName(self) -> str: ...
    @deviceName.setter
    def deviceName(self, value: str):
        self._deviceName = value


class PciPassthruConfig(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def passthruEnabled(self) -> bool: ...
    @passthruEnabled.setter
    def passthruEnabled(self, value: bool):
        self._passthruEnabled = value
    @property
    def applyNow(self) -> bool: ...
    @applyNow.setter
    def applyNow(self, value: bool):
        self._applyNow = value
    @property
    def hardwareLabel(self) -> str: ...
    @hardwareLabel.setter
    def hardwareLabel(self, value: str):
        self._hardwareLabel = value


class PciPassthruInfo(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def dependentDevice(self) -> str: ...
    @dependentDevice.setter
    def dependentDevice(self, value: str):
        self._dependentDevice = value
    @property
    def passthruEnabled(self) -> bool: ...
    @passthruEnabled.setter
    def passthruEnabled(self, value: bool):
        self._passthruEnabled = value
    @property
    def passthruCapable(self) -> bool: ...
    @passthruCapable.setter
    def passthruCapable(self, value: bool):
        self._passthruCapable = value
    @property
    def passthruActive(self) -> bool: ...
    @passthruActive.setter
    def passthruActive(self, value: bool):
        self._passthruActive = value
    @property
    def hardwareLabel(self) -> str: ...
    @hardwareLabel.setter
    def hardwareLabel(self, value: str):
        self._hardwareLabel = value


class PcieHba(HostBusAdapter): ...


class PcieTargetTransport(TargetTransport): ...


class PersistentMemoryInfo(vmodl.DynamicData):
    @property
    def capacityInMB(self) -> long: ...
    @capacityInMB.setter
    def capacityInMB(self, value: long):
        self._capacityInMB = value
    @property
    def volumeUUID(self) -> str: ...
    @volumeUUID.setter
    def volumeUUID(self, value: str):
        self._volumeUUID = value


class PhysicalNic(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value
    @property
    def pci(self) -> str: ...
    @pci.setter
    def pci(self, value: str):
        self._pci = value
    @property
    def driver(self) -> str: ...
    @driver.setter
    def driver(self, value: str):
        self._driver = value
    @property
    def driverVersion(self) -> str: ...
    @driverVersion.setter
    def driverVersion(self, value: str):
        self._driverVersion = value
    @property
    def firmwareVersion(self) -> str: ...
    @firmwareVersion.setter
    def firmwareVersion(self, value: str):
        self._firmwareVersion = value
    @property
    def linkSpeed(self) -> PhysicalNic.LinkSpeedDuplex: ...
    @linkSpeed.setter
    def linkSpeed(self, value: PhysicalNic.LinkSpeedDuplex):
        self._linkSpeed = value
    @property
    def validLinkSpecification(self) -> List[PhysicalNic.LinkSpeedDuplex]: ...
    @validLinkSpecification.setter
    def validLinkSpecification(self, value: List[PhysicalNic.LinkSpeedDuplex]):
        self._validLinkSpecification = value
    @property
    def spec(self) -> PhysicalNic.Specification: ...
    @spec.setter
    def spec(self, value: PhysicalNic.Specification):
        self._spec = value
    @property
    def wakeOnLanSupported(self) -> bool: ...
    @wakeOnLanSupported.setter
    def wakeOnLanSupported(self, value: bool):
        self._wakeOnLanSupported = value
    @property
    def mac(self) -> str: ...
    @mac.setter
    def mac(self, value: str):
        self._mac = value
    @property
    def fcoeConfiguration(self) -> FcoeConfig: ...
    @fcoeConfiguration.setter
    def fcoeConfiguration(self, value: FcoeConfig):
        self._fcoeConfiguration = value
    @property
    def vmDirectPathGen2Supported(self) -> bool: ...
    @vmDirectPathGen2Supported.setter
    def vmDirectPathGen2Supported(self, value: bool):
        self._vmDirectPathGen2Supported = value
    @property
    def vmDirectPathGen2SupportedMode(self) -> str: ...
    @vmDirectPathGen2SupportedMode.setter
    def vmDirectPathGen2SupportedMode(self, value: str):
        self._vmDirectPathGen2SupportedMode = value
    @property
    def resourcePoolSchedulerAllowed(self) -> bool: ...
    @resourcePoolSchedulerAllowed.setter
    def resourcePoolSchedulerAllowed(self, value: bool):
        self._resourcePoolSchedulerAllowed = value
    @property
    def resourcePoolSchedulerDisallowedReason(self) -> List[str]: ...
    @resourcePoolSchedulerDisallowedReason.setter
    def resourcePoolSchedulerDisallowedReason(self, value: List[str]):
        self._resourcePoolSchedulerDisallowedReason = value
    @property
    def autoNegotiateSupported(self) -> bool: ...
    @autoNegotiateSupported.setter
    def autoNegotiateSupported(self, value: bool):
        self._autoNegotiateSupported = value
    @property
    def enhancedNetworkingStackSupported(self) -> bool: ...
    @enhancedNetworkingStackSupported.setter
    def enhancedNetworkingStackSupported(self, value: bool):
        self._enhancedNetworkingStackSupported = value
    @property
    def ensInterruptSupported(self) -> bool: ...
    @ensInterruptSupported.setter
    def ensInterruptSupported(self, value: bool):
        self._ensInterruptSupported = value
    @property
    def rdmaDevice(self) -> Link: ...
    @rdmaDevice.setter
    def rdmaDevice(self, value: Link):
        self._rdmaDevice = value
    @property
    def dpuId(self) -> str: ...
    @dpuId.setter
    def dpuId(self, value: str):
        self._dpuId = value


    class CdpDeviceCapability(vmodl.DynamicData):
        @property
        def router(self) -> bool: ...
        @router.setter
        def router(self, value: bool):
            self._router = value
        @property
        def transparentBridge(self) -> bool: ...
        @transparentBridge.setter
        def transparentBridge(self, value: bool):
            self._transparentBridge = value
        @property
        def sourceRouteBridge(self) -> bool: ...
        @sourceRouteBridge.setter
        def sourceRouteBridge(self, value: bool):
            self._sourceRouteBridge = value
        @property
        def networkSwitch(self) -> bool: ...
        @networkSwitch.setter
        def networkSwitch(self, value: bool):
            self._networkSwitch = value
        @property
        def host(self) -> bool: ...
        @host.setter
        def host(self, value: bool):
            self._host = value
        @property
        def igmpEnabled(self) -> bool: ...
        @igmpEnabled.setter
        def igmpEnabled(self, value: bool):
            self._igmpEnabled = value
        @property
        def repeater(self) -> bool: ...
        @repeater.setter
        def repeater(self, value: bool):
            self._repeater = value


    class CdpInfo(vmodl.DynamicData):
        @property
        def cdpVersion(self) -> int: ...
        @cdpVersion.setter
        def cdpVersion(self, value: int):
            self._cdpVersion = value
        @property
        def timeout(self) -> int: ...
        @timeout.setter
        def timeout(self, value: int):
            self._timeout = value
        @property
        def ttl(self) -> int: ...
        @ttl.setter
        def ttl(self, value: int):
            self._ttl = value
        @property
        def samples(self) -> int: ...
        @samples.setter
        def samples(self, value: int):
            self._samples = value
        @property
        def devId(self) -> str: ...
        @devId.setter
        def devId(self, value: str):
            self._devId = value
        @property
        def address(self) -> str: ...
        @address.setter
        def address(self, value: str):
            self._address = value
        @property
        def portId(self) -> str: ...
        @portId.setter
        def portId(self, value: str):
            self._portId = value
        @property
        def deviceCapability(self) -> PhysicalNic.CdpDeviceCapability: ...
        @deviceCapability.setter
        def deviceCapability(self, value: PhysicalNic.CdpDeviceCapability):
            self._deviceCapability = value
        @property
        def softwareVersion(self) -> str: ...
        @softwareVersion.setter
        def softwareVersion(self, value: str):
            self._softwareVersion = value
        @property
        def hardwarePlatform(self) -> str: ...
        @hardwarePlatform.setter
        def hardwarePlatform(self, value: str):
            self._hardwarePlatform = value
        @property
        def ipPrefix(self) -> str: ...
        @ipPrefix.setter
        def ipPrefix(self, value: str):
            self._ipPrefix = value
        @property
        def ipPrefixLen(self) -> int: ...
        @ipPrefixLen.setter
        def ipPrefixLen(self, value: int):
            self._ipPrefixLen = value
        @property
        def vlan(self) -> int: ...
        @vlan.setter
        def vlan(self, value: int):
            self._vlan = value
        @property
        def fullDuplex(self) -> bool: ...
        @fullDuplex.setter
        def fullDuplex(self, value: bool):
            self._fullDuplex = value
        @property
        def mtu(self) -> int: ...
        @mtu.setter
        def mtu(self, value: int):
            self._mtu = value
        @property
        def systemName(self) -> str: ...
        @systemName.setter
        def systemName(self, value: str):
            self._systemName = value
        @property
        def systemOID(self) -> str: ...
        @systemOID.setter
        def systemOID(self, value: str):
            self._systemOID = value
        @property
        def mgmtAddr(self) -> str: ...
        @mgmtAddr.setter
        def mgmtAddr(self, value: str):
            self._mgmtAddr = value
        @property
        def location(self) -> str: ...
        @location.setter
        def location(self, value: str):
            self._location = value


    class Config(vmodl.DynamicData):
        @property
        def device(self) -> str: ...
        @device.setter
        def device(self, value: str):
            self._device = value
        @property
        def spec(self) -> PhysicalNic.Specification: ...
        @spec.setter
        def spec(self, value: PhysicalNic.Specification):
            self._spec = value


    class LinkSpeedDuplex(vmodl.DynamicData):
        @property
        def speedMb(self) -> int: ...
        @speedMb.setter
        def speedMb(self, value: int):
            self._speedMb = value
        @property
        def duplex(self) -> bool: ...
        @duplex.setter
        def duplex(self, value: bool):
            self._duplex = value


    class LldpInfo(vmodl.DynamicData):
        @property
        def chassisId(self) -> str: ...
        @chassisId.setter
        def chassisId(self, value: str):
            self._chassisId = value
        @property
        def portId(self) -> str: ...
        @portId.setter
        def portId(self, value: str):
            self._portId = value
        @property
        def timeToLive(self) -> int: ...
        @timeToLive.setter
        def timeToLive(self, value: int):
            self._timeToLive = value
        @property
        def parameter(self) -> List[vmodl.KeyAnyValue]: ...
        @parameter.setter
        def parameter(self, value: List[vmodl.KeyAnyValue]):
            self._parameter = value


    class NetworkHint(vmodl.DynamicData):
        @property
        def device(self) -> str: ...
        @device.setter
        def device(self, value: str):
            self._device = value
        @property
        def subnet(self) -> List[PhysicalNic.NetworkHint.IpNetwork]: ...
        @subnet.setter
        def subnet(self, value: List[PhysicalNic.NetworkHint.IpNetwork]):
            self._subnet = value
        @property
        def network(self) -> List[PhysicalNic.NetworkHint.NamedNetwork]: ...
        @network.setter
        def network(self, value: List[PhysicalNic.NetworkHint.NamedNetwork]):
            self._network = value
        @property
        def connectedSwitchPort(self) -> PhysicalNic.CdpInfo: ...
        @connectedSwitchPort.setter
        def connectedSwitchPort(self, value: PhysicalNic.CdpInfo):
            self._connectedSwitchPort = value
        @property
        def lldpInfo(self) -> PhysicalNic.LldpInfo: ...
        @lldpInfo.setter
        def lldpInfo(self, value: PhysicalNic.LldpInfo):
            self._lldpInfo = value


        class HintElement(vmodl.DynamicData):
            @property
            def vlanId(self) -> int: ...
            @vlanId.setter
            def vlanId(self, value: int):
                self._vlanId = value


        class IpNetwork(PhysicalNic.NetworkHint.HintElement):
            @property
            def ipSubnet(self) -> str: ...
            @ipSubnet.setter
            def ipSubnet(self, value: str):
                self._ipSubnet = value


        class NamedNetwork(PhysicalNic.NetworkHint.HintElement):
            @property
            def network(self) -> str: ...
            @network.setter
            def network(self, value: str):
                self._network = value


    class Specification(vmodl.DynamicData):
        @property
        def ip(self) -> IpConfig: ...
        @ip.setter
        def ip(self, value: IpConfig):
            self._ip = value
        @property
        def linkSpeed(self) -> PhysicalNic.LinkSpeedDuplex: ...
        @linkSpeed.setter
        def linkSpeed(self, value: PhysicalNic.LinkSpeedDuplex):
            self._linkSpeed = value
        @property
        def enableEnhancedNetworkingStack(self) -> bool: ...
        @enableEnhancedNetworkingStack.setter
        def enableEnhancedNetworkingStack(self, value: bool):
            self._enableEnhancedNetworkingStack = value
        @property
        def ensInterruptEnabled(self) -> bool: ...
        @ensInterruptEnabled.setter
        def ensInterruptEnabled(self, value: bool):
            self._ensInterruptEnabled = value


    class ResourcePoolSchedulerDisallowedReason(Enum):
        userOptOut = "userOptOut"
        hardwareUnsupported = "hardwareUnsupported"


    class VmDirectPathGen2SupportedMode(Enum):
        upt = "upt"


class PlugStoreTopology(vmodl.DynamicData):
    @property
    def adapter(self) -> List[PlugStoreTopology.Adapter]: ...
    @adapter.setter
    def adapter(self, value: List[PlugStoreTopology.Adapter]):
        self._adapter = value
    @property
    def path(self) -> List[PlugStoreTopology.Path]: ...
    @path.setter
    def path(self, value: List[PlugStoreTopology.Path]):
        self._path = value
    @property
    def target(self) -> List[PlugStoreTopology.Target]: ...
    @target.setter
    def target(self, value: List[PlugStoreTopology.Target]):
        self._target = value
    @property
    def device(self) -> List[PlugStoreTopology.Device]: ...
    @device.setter
    def device(self, value: List[PlugStoreTopology.Device]):
        self._device = value
    @property
    def plugin(self) -> List[PlugStoreTopology.Plugin]: ...
    @plugin.setter
    def plugin(self, value: List[PlugStoreTopology.Plugin]):
        self._plugin = value


    class Adapter(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def adapter(self) -> Link: ...
        @adapter.setter
        def adapter(self, value: Link):
            self._adapter = value
        @property
        def path(self) -> List[Link]: ...
        @path.setter
        def path(self, value: List[Link]):
            self._path = value


    class Device(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def lun(self) -> Link: ...
        @lun.setter
        def lun(self, value: Link):
            self._lun = value
        @property
        def path(self) -> List[Link]: ...
        @path.setter
        def path(self, value: List[Link]):
            self._path = value


    class Path(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def channelNumber(self) -> int: ...
        @channelNumber.setter
        def channelNumber(self, value: int):
            self._channelNumber = value
        @property
        def targetNumber(self) -> int: ...
        @targetNumber.setter
        def targetNumber(self, value: int):
            self._targetNumber = value
        @property
        def lunNumber(self) -> int: ...
        @lunNumber.setter
        def lunNumber(self, value: int):
            self._lunNumber = value
        @property
        def adapter(self) -> Link: ...
        @adapter.setter
        def adapter(self, value: Link):
            self._adapter = value
        @property
        def target(self) -> Link: ...
        @target.setter
        def target(self, value: Link):
            self._target = value
        @property
        def device(self) -> Link: ...
        @device.setter
        def device(self, value: Link):
            self._device = value


    class Plugin(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def device(self) -> List[Link]: ...
        @device.setter
        def device(self, value: List[Link]):
            self._device = value
        @property
        def claimedPath(self) -> List[Link]: ...
        @claimedPath.setter
        def claimedPath(self, value: List[Link]):
            self._claimedPath = value


    class Target(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def transport(self) -> TargetTransport: ...
        @transport.setter
        def transport(self, value: TargetTransport):
            self._transport = value


class PortGroup(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def port(self) -> List[PortGroup.Port]: ...
    @port.setter
    def port(self, value: List[PortGroup.Port]):
        self._port = value
    @property
    def vswitch(self) -> Link: ...
    @vswitch.setter
    def vswitch(self, value: Link):
        self._vswitch = value
    @property
    def computedPolicy(self) -> NetworkPolicy: ...
    @computedPolicy.setter
    def computedPolicy(self, value: NetworkPolicy):
        self._computedPolicy = value
    @property
    def spec(self) -> PortGroup.Specification: ...
    @spec.setter
    def spec(self, value: PortGroup.Specification):
        self._spec = value


    class Config(vmodl.DynamicData):
        @property
        def changeOperation(self) -> str: ...
        @changeOperation.setter
        def changeOperation(self, value: str):
            self._changeOperation = value
        @property
        def spec(self) -> PortGroup.Specification: ...
        @spec.setter
        def spec(self, value: PortGroup.Specification):
            self._spec = value


    class Port(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def mac(self) -> List[str]: ...
        @mac.setter
        def mac(self, value: List[str]):
            self._mac = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value


    class Specification(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def vlanId(self) -> int: ...
        @vlanId.setter
        def vlanId(self, value: int):
            self._vlanId = value
        @property
        def vswitchName(self) -> str: ...
        @vswitchName.setter
        def vswitchName(self, value: str):
            self._vswitchName = value
        @property
        def policy(self) -> NetworkPolicy: ...
        @policy.setter
        def policy(self, value: NetworkPolicy):
            self._policy = value


    class PortConnecteeType(Enum):
        virtualMachine = "virtualMachine"
        systemManagement = "systemManagement"
        host = "host"
        unknown = "unknown"


class ProtocolEndpoint(vmodl.DynamicData):
    @property
    def peType(self) -> str: ...
    @peType.setter
    def peType(self, value: str):
        self._peType = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def hostKey(self) -> List[vim.HostSystem]: ...
    @hostKey.setter
    def hostKey(self, value: List[vim.HostSystem]):
        self._hostKey = value
    @property
    def storageArray(self) -> str: ...
    @storageArray.setter
    def storageArray(self, value: str):
        self._storageArray = value
    @property
    def nfsServer(self) -> str: ...
    @nfsServer.setter
    def nfsServer(self, value: str):
        self._nfsServer = value
    @property
    def nfsDir(self) -> str: ...
    @nfsDir.setter
    def nfsDir(self, value: str):
        self._nfsDir = value
    @property
    def nfsServerScope(self) -> str: ...
    @nfsServerScope.setter
    def nfsServerScope(self, value: str):
        self._nfsServerScope = value
    @property
    def nfsServerMajor(self) -> str: ...
    @nfsServerMajor.setter
    def nfsServerMajor(self, value: str):
        self._nfsServerMajor = value
    @property
    def nfsServerAuthType(self) -> str: ...
    @nfsServerAuthType.setter
    def nfsServerAuthType(self, value: str):
        self._nfsServerAuthType = value
    @property
    def nfsServerUser(self) -> str: ...
    @nfsServerUser.setter
    def nfsServerUser(self, value: str):
        self._nfsServerUser = value
    @property
    def deviceId(self) -> str: ...
    @deviceId.setter
    def deviceId(self, value: str):
        self._deviceId = value


    class PEType(Enum):
        block = "block"
        nas = "nas"


    class ProtocolEndpointType(Enum):
        scsi = "scsi"
        nfs = "nfs"
        nfs4x = "nfs4x"


class PtpConfig(vmodl.DynamicData):
    @property
    def domain(self) -> int: ...
    @domain.setter
    def domain(self, value: int):
        self._domain = value
    @property
    def port(self) -> List[PtpConfig.PtpPort]: ...
    @port.setter
    def port(self, value: List[PtpConfig.PtpPort]):
        self._port = value


    class PtpPort(vmodl.DynamicData):
        @property
        def index(self) -> int: ...
        @index.setter
        def index(self, value: int):
            self._index = value
        @property
        def deviceType(self) -> str: ...
        @deviceType.setter
        def deviceType(self, value: str):
            self._deviceType = value
        @property
        def device(self) -> str: ...
        @device.setter
        def device(self, value: str):
            self._device = value
        @property
        def ipConfig(self) -> IpConfig: ...
        @ipConfig.setter
        def ipConfig(self, value: IpConfig):
            self._ipConfig = value


    class DeviceType(Enum):
        none = "none"
        virtualNic = "virtualNic"
        pciPassthruNic = "pciPassthruNic"


class QualifiedName(vmodl.DynamicData):
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value


class RdmaDevice(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value
    @property
    def driver(self) -> str: ...
    @driver.setter
    def driver(self, value: str):
        self._driver = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def backing(self) -> RdmaDevice.Backing: ...
    @backing.setter
    def backing(self, value: RdmaDevice.Backing):
        self._backing = value
    @property
    def connectionInfo(self) -> RdmaDevice.ConnectionInfo: ...
    @connectionInfo.setter
    def connectionInfo(self, value: RdmaDevice.ConnectionInfo):
        self._connectionInfo = value
    @property
    def capability(self) -> RdmaDevice.Capability: ...
    @capability.setter
    def capability(self, value: RdmaDevice.Capability):
        self._capability = value


    class Backing(vmodl.DynamicData): ...


    class Capability(vmodl.DynamicData):
        @property
        def roceV1Capable(self) -> bool: ...
        @roceV1Capable.setter
        def roceV1Capable(self, value: bool):
            self._roceV1Capable = value
        @property
        def roceV2Capable(self) -> bool: ...
        @roceV2Capable.setter
        def roceV2Capable(self, value: bool):
            self._roceV2Capable = value
        @property
        def iWarpCapable(self) -> bool: ...
        @iWarpCapable.setter
        def iWarpCapable(self, value: bool):
            self._iWarpCapable = value


    class ConnectionInfo(vmodl.DynamicData):
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value
        @property
        def mtu(self) -> int: ...
        @mtu.setter
        def mtu(self, value: int):
            self._mtu = value
        @property
        def speedInMbps(self) -> int: ...
        @speedInMbps.setter
        def speedInMbps(self, value: int):
            self._speedInMbps = value


    class PnicBacking(RdmaDevice.Backing):
        @property
        def pairedUplink(self) -> Link: ...
        @pairedUplink.setter
        def pairedUplink(self, value: Link):
            self._pairedUplink = value


    class ConnectionState(Enum):
        unknown = "unknown"
        down = "down"
        init = "init"
        armed = "armed"
        active = "active"
        activeDefer = "activeDefer"


class RdmaHba(HostBusAdapter):
    @property
    def associatedRdmaDevice(self) -> str: ...
    @associatedRdmaDevice.setter
    def associatedRdmaDevice(self, value: str):
        self._associatedRdmaDevice = value


class RdmaTargetTransport(TargetTransport): ...


class ReliableMemoryInfo(vmodl.DynamicData):
    @property
    def memorySize(self) -> long: ...
    @memorySize.setter
    def memorySize(self, value: long):
        self._memorySize = value


class ResignatureRescanResult(vmodl.DynamicData):
    @property
    def rescan(self) -> List[VmfsRescanResult]: ...
    @rescan.setter
    def rescan(self, value: List[VmfsRescanResult]):
        self._rescan = value
    @property
    def result(self) -> vim.Datastore: ...
    @result.setter
    def result(self, value: vim.Datastore):
        self._result = value


class Ruleset(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def label(self) -> str: ...
    @label.setter
    def label(self, value: str):
        self._label = value
    @property
    def required(self) -> bool: ...
    @required.setter
    def required(self, value: bool):
        self._required = value
    @property
    def rule(self) -> List[Ruleset.Rule]: ...
    @rule.setter
    def rule(self, value: List[Ruleset.Rule]):
        self._rule = value
    @property
    def service(self) -> str: ...
    @service.setter
    def service(self, value: str):
        self._service = value
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def allowedHosts(self) -> Ruleset.IpList: ...
    @allowedHosts.setter
    def allowedHosts(self, value: Ruleset.IpList):
        self._allowedHosts = value


    class IpList(vmodl.DynamicData):
        @property
        def ipAddress(self) -> List[str]: ...
        @ipAddress.setter
        def ipAddress(self, value: List[str]):
            self._ipAddress = value
        @property
        def ipNetwork(self) -> List[Ruleset.IpNetwork]: ...
        @ipNetwork.setter
        def ipNetwork(self, value: List[Ruleset.IpNetwork]):
            self._ipNetwork = value
        @property
        def allIp(self) -> bool: ...
        @allIp.setter
        def allIp(self, value: bool):
            self._allIp = value


    class IpNetwork(vmodl.DynamicData):
        @property
        def network(self) -> str: ...
        @network.setter
        def network(self, value: str):
            self._network = value
        @property
        def prefixLength(self) -> int: ...
        @prefixLength.setter
        def prefixLength(self, value: int):
            self._prefixLength = value


    class Rule(vmodl.DynamicData):
        @property
        def port(self) -> int: ...
        @port.setter
        def port(self, value: int):
            self._port = value
        @property
        def endPort(self) -> int: ...
        @endPort.setter
        def endPort(self, value: int):
            self._endPort = value
        @property
        def direction(self) -> Ruleset.Rule.Direction | Literal['inbound', 'outbound']: ...
        @direction.setter
        def direction(self, value: Ruleset.Rule.Direction | Literal['inbound', 'outbound']):
            self._direction = value
        @property
        def portType(self) -> Ruleset.Rule.PortType | Literal['src', 'dst']: ...
        @portType.setter
        def portType(self, value: Ruleset.Rule.PortType | Literal['src', 'dst']):
            self._portType = value
        @property
        def protocol(self) -> str: ...
        @protocol.setter
        def protocol(self, value: str):
            self._protocol = value


        class Direction(Enum):
            inbound = "inbound"
            outbound = "outbound"


    class RulesetSpec(vmodl.DynamicData):
        @property
        def allowedHosts(self) -> Ruleset.IpList: ...
        @allowedHosts.setter
        def allowedHosts(self, value: Ruleset.IpList):
            self._allowedHosts = value


class RuntimeInfo(vmodl.DynamicData):
    @property
    def connectionState(self) -> vim.HostSystem.ConnectionState | Literal['connected', 'notResponding', 'disconnected']: ...
    @connectionState.setter
    def connectionState(self, value: vim.HostSystem.ConnectionState | Literal['connected', 'notResponding', 'disconnected']):
        self._connectionState = value
    @property
    def powerState(self) -> vim.HostSystem.PowerState | Literal['poweredOn', 'poweredOff', 'standBy', 'unknown']: ...
    @powerState.setter
    def powerState(self, value: vim.HostSystem.PowerState | Literal['poweredOn', 'poweredOff', 'standBy', 'unknown']):
        self._powerState = value
    @property
    def standbyMode(self) -> str: ...
    @standbyMode.setter
    def standbyMode(self, value: str):
        self._standbyMode = value
    @property
    def inMaintenanceMode(self) -> bool: ...
    @inMaintenanceMode.setter
    def inMaintenanceMode(self, value: bool):
        self._inMaintenanceMode = value
    @property
    def inQuarantineMode(self) -> bool: ...
    @inQuarantineMode.setter
    def inQuarantineMode(self, value: bool):
        self._inQuarantineMode = value
    @property
    def bootTime(self) -> datetime: ...
    @bootTime.setter
    def bootTime(self, value: datetime):
        self._bootTime = value
    @property
    def healthSystemRuntime(self) -> HealthStatusSystem.Runtime: ...
    @healthSystemRuntime.setter
    def healthSystemRuntime(self, value: HealthStatusSystem.Runtime):
        self._healthSystemRuntime = value
    @property
    def dasHostState(self) -> vim.cluster.DasFdmHostState: ...
    @dasHostState.setter
    def dasHostState(self, value: vim.cluster.DasFdmHostState):
        self._dasHostState = value
    @property
    def tpmPcrValues(self) -> List[TpmDigestInfo]: ...
    @tpmPcrValues.setter
    def tpmPcrValues(self, value: List[TpmDigestInfo]):
        self._tpmPcrValues = value
    @property
    def vsanRuntimeInfo(self) -> VsanRuntimeInfo: ...
    @vsanRuntimeInfo.setter
    def vsanRuntimeInfo(self, value: VsanRuntimeInfo):
        self._vsanRuntimeInfo = value
    @property
    def networkRuntimeInfo(self) -> RuntimeInfo.NetworkRuntimeInfo: ...
    @networkRuntimeInfo.setter
    def networkRuntimeInfo(self, value: RuntimeInfo.NetworkRuntimeInfo):
        self._networkRuntimeInfo = value
    @property
    def vFlashResourceRuntimeInfo(self) -> VFlashManager.VFlashResourceRunTimeInfo: ...
    @vFlashResourceRuntimeInfo.setter
    def vFlashResourceRuntimeInfo(self, value: VFlashManager.VFlashResourceRunTimeInfo):
        self._vFlashResourceRuntimeInfo = value
    @property
    def hostMaxVirtualDiskCapacity(self) -> long: ...
    @hostMaxVirtualDiskCapacity.setter
    def hostMaxVirtualDiskCapacity(self, value: long):
        self._hostMaxVirtualDiskCapacity = value
    @property
    def cryptoState(self) -> str: ...
    @cryptoState.setter
    def cryptoState(self, value: str):
        self._cryptoState = value
    @property
    def cryptoKeyId(self) -> vim.encryption.CryptoKeyId: ...
    @cryptoKeyId.setter
    def cryptoKeyId(self, value: vim.encryption.CryptoKeyId):
        self._cryptoKeyId = value
    @property
    def statelessNvdsMigrationReady(self) -> str: ...
    @statelessNvdsMigrationReady.setter
    def statelessNvdsMigrationReady(self, value: str):
        self._statelessNvdsMigrationReady = value
    @property
    def stateEncryption(self) -> RuntimeInfo.StateEncryptionInfo: ...
    @stateEncryption.setter
    def stateEncryption(self, value: RuntimeInfo.StateEncryptionInfo):
        self._stateEncryption = value


    class NetStackInstanceRuntimeInfo(vmodl.DynamicData):
        @property
        def netStackInstanceKey(self) -> str: ...
        @netStackInstanceKey.setter
        def netStackInstanceKey(self, value: str):
            self._netStackInstanceKey = value
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value
        @property
        def vmknicKeys(self) -> List[str]: ...
        @vmknicKeys.setter
        def vmknicKeys(self, value: List[str]):
            self._vmknicKeys = value
        @property
        def maxNumberOfConnections(self) -> int: ...
        @maxNumberOfConnections.setter
        def maxNumberOfConnections(self, value: int):
            self._maxNumberOfConnections = value
        @property
        def currentIpV6Enabled(self) -> bool: ...
        @currentIpV6Enabled.setter
        def currentIpV6Enabled(self, value: bool):
            self._currentIpV6Enabled = value


        class State(Enum):
            inactive = "inactive"
            active = "active"
            deactivating = "deactivating"
            activating = "activating"


    class NetworkResourceRuntimeInfo(vmodl.DynamicData):
        @property
        def pnicResourceInfo(self) -> List[RuntimeInfo.PnicNetworkResourceInfo]: ...
        @pnicResourceInfo.setter
        def pnicResourceInfo(self, value: List[RuntimeInfo.PnicNetworkResourceInfo]):
            self._pnicResourceInfo = value


    class NetworkRuntimeInfo(vmodl.DynamicData):
        @property
        def netStackInstanceRuntimeInfo(self) -> List[RuntimeInfo.NetStackInstanceRuntimeInfo]: ...
        @netStackInstanceRuntimeInfo.setter
        def netStackInstanceRuntimeInfo(self, value: List[RuntimeInfo.NetStackInstanceRuntimeInfo]):
            self._netStackInstanceRuntimeInfo = value
        @property
        def networkResourceRuntime(self) -> RuntimeInfo.NetworkResourceRuntimeInfo: ...
        @networkResourceRuntime.setter
        def networkResourceRuntime(self, value: RuntimeInfo.NetworkResourceRuntimeInfo):
            self._networkResourceRuntime = value


    class PlacedVirtualNicIdentifier(vmodl.DynamicData):
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @vm.setter
        def vm(self, value: vim.VirtualMachine):
            self._vm = value
        @property
        def vnicKey(self) -> str: ...
        @vnicKey.setter
        def vnicKey(self, value: str):
            self._vnicKey = value
        @property
        def reservation(self) -> int: ...
        @reservation.setter
        def reservation(self, value: int):
            self._reservation = value


    class PnicNetworkResourceInfo(vmodl.DynamicData):
        @property
        def pnicDevice(self) -> str: ...
        @pnicDevice.setter
        def pnicDevice(self, value: str):
            self._pnicDevice = value
        @property
        def availableBandwidthForVMTraffic(self) -> long: ...
        @availableBandwidthForVMTraffic.setter
        def availableBandwidthForVMTraffic(self, value: long):
            self._availableBandwidthForVMTraffic = value
        @property
        def unusedBandwidthForVMTraffic(self) -> long: ...
        @unusedBandwidthForVMTraffic.setter
        def unusedBandwidthForVMTraffic(self, value: long):
            self._unusedBandwidthForVMTraffic = value
        @property
        def placedVirtualNics(self) -> List[RuntimeInfo.PlacedVirtualNicIdentifier]: ...
        @placedVirtualNics.setter
        def placedVirtualNics(self, value: List[RuntimeInfo.PlacedVirtualNicIdentifier]):
            self._placedVirtualNics = value


    class StateEncryptionInfo(vmodl.DynamicData):
        @property
        def protectionMode(self) -> str: ...
        @protectionMode.setter
        def protectionMode(self, value: str):
            self._protectionMode = value
        @property
        def requireSecureBoot(self) -> bool: ...
        @requireSecureBoot.setter
        def requireSecureBoot(self, value: bool):
            self._requireSecureBoot = value
        @property
        def requireExecInstalledOnly(self) -> bool: ...
        @requireExecInstalledOnly.setter
        def requireExecInstalledOnly(self, value: bool):
            self._requireExecInstalledOnly = value


        class ProtectionMode(Enum):
            none = "none"
            tpm = "tpm"


    class StatelessNvdsMigrationState(Enum):
        ready = "ready"
        notNeeded = "notNeeded"
        unknown = "unknown"


class ScsiDisk(ScsiLun):
    @property
    def capacity(self) -> DiskDimensions.Lba: ...
    @capacity.setter
    def capacity(self, value: DiskDimensions.Lba):
        self._capacity = value
    @property
    def devicePath(self) -> str: ...
    @devicePath.setter
    def devicePath(self, value: str):
        self._devicePath = value
    @property
    def ssd(self) -> bool: ...
    @ssd.setter
    def ssd(self, value: bool):
        self._ssd = value
    @property
    def localDisk(self) -> bool: ...
    @localDisk.setter
    def localDisk(self, value: bool):
        self._localDisk = value
    @property
    def physicalLocation(self) -> List[str]: ...
    @physicalLocation.setter
    def physicalLocation(self, value: List[str]):
        self._physicalLocation = value
    @property
    def emulatedDIXDIFEnabled(self) -> bool: ...
    @emulatedDIXDIFEnabled.setter
    def emulatedDIXDIFEnabled(self, value: bool):
        self._emulatedDIXDIFEnabled = value
    @property
    def vsanDiskInfo(self) -> VsanDiskInfo: ...
    @vsanDiskInfo.setter
    def vsanDiskInfo(self, value: VsanDiskInfo):
        self._vsanDiskInfo = value
    @property
    def scsiDiskType(self) -> str: ...
    @scsiDiskType.setter
    def scsiDiskType(self, value: str):
        self._scsiDiskType = value


    class Partition(vmodl.DynamicData):
        @property
        def diskName(self) -> str: ...
        @diskName.setter
        def diskName(self, value: str):
            self._diskName = value
        @property
        def partition(self) -> int: ...
        @partition.setter
        def partition(self, value: int):
            self._partition = value


    class ScsiDiskType(Enum):
        native512 = "native512"
        emulated512 = "emulated512"
        native4k = "native4k"
        SoftwareEmulated4k = "SoftwareEmulated4k"
        unknown = "unknown"


class ScsiLun(Device):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def descriptor(self) -> List[ScsiLun.Descriptor]: ...
    @descriptor.setter
    def descriptor(self, value: List[ScsiLun.Descriptor]):
        self._descriptor = value
    @property
    def canonicalName(self) -> str: ...
    @canonicalName.setter
    def canonicalName(self, value: str):
        self._canonicalName = value
    @property
    def displayName(self) -> str: ...
    @displayName.setter
    def displayName(self, value: str):
        self._displayName = value
    @property
    def lunType(self) -> str: ...
    @lunType.setter
    def lunType(self, value: str):
        self._lunType = value
    @property
    def vendor(self) -> str: ...
    @vendor.setter
    def vendor(self, value: str):
        self._vendor = value
    @property
    def model(self) -> str: ...
    @model.setter
    def model(self, value: str):
        self._model = value
    @property
    def revision(self) -> str: ...
    @revision.setter
    def revision(self, value: str):
        self._revision = value
    @property
    def scsiLevel(self) -> int: ...
    @scsiLevel.setter
    def scsiLevel(self, value: int):
        self._scsiLevel = value
    @property
    def serialNumber(self) -> str: ...
    @serialNumber.setter
    def serialNumber(self, value: str):
        self._serialNumber = value
    @property
    def durableName(self) -> ScsiLun.DurableName: ...
    @durableName.setter
    def durableName(self, value: ScsiLun.DurableName):
        self._durableName = value
    @property
    def alternateName(self) -> List[ScsiLun.DurableName]: ...
    @alternateName.setter
    def alternateName(self, value: List[ScsiLun.DurableName]):
        self._alternateName = value
    @property
    def standardInquiry(self) -> List[byte]: ...
    @standardInquiry.setter
    def standardInquiry(self, value: List[byte]):
        self._standardInquiry = value
    @property
    def queueDepth(self) -> int: ...
    @queueDepth.setter
    def queueDepth(self, value: int):
        self._queueDepth = value
    @property
    def operationalState(self) -> List[str]: ...
    @operationalState.setter
    def operationalState(self, value: List[str]):
        self._operationalState = value
    @property
    def capabilities(self) -> ScsiLun.Capabilities: ...
    @capabilities.setter
    def capabilities(self, value: ScsiLun.Capabilities):
        self._capabilities = value
    @property
    def vStorageSupport(self) -> str: ...
    @vStorageSupport.setter
    def vStorageSupport(self, value: str):
        self._vStorageSupport = value
    @property
    def protocolEndpoint(self) -> bool: ...
    @protocolEndpoint.setter
    def protocolEndpoint(self, value: bool):
        self._protocolEndpoint = value
    @property
    def perenniallyReserved(self) -> bool: ...
    @perenniallyReserved.setter
    def perenniallyReserved(self, value: bool):
        self._perenniallyReserved = value
    @property
    def clusteredVmdkSupported(self) -> bool: ...
    @clusteredVmdkSupported.setter
    def clusteredVmdkSupported(self, value: bool):
        self._clusteredVmdkSupported = value
    @property
    def applicationProtocol(self) -> str: ...
    @applicationProtocol.setter
    def applicationProtocol(self, value: str):
        self._applicationProtocol = value
    @property
    def dispersedNs(self) -> bool: ...
    @dispersedNs.setter
    def dispersedNs(self, value: bool):
        self._dispersedNs = value


    class Capabilities(vmodl.DynamicData):
        @property
        def updateDisplayNameSupported(self) -> bool: ...
        @updateDisplayNameSupported.setter
        def updateDisplayNameSupported(self, value: bool):
            self._updateDisplayNameSupported = value


    class Descriptor(vmodl.DynamicData):
        @property
        def quality(self) -> str: ...
        @quality.setter
        def quality(self, value: str):
            self._quality = value
        @property
        def id(self) -> str: ...
        @id.setter
        def id(self, value: str):
            self._id = value


    class DurableName(vmodl.DynamicData):
        @property
        def namespace(self) -> str: ...
        @namespace.setter
        def namespace(self, value: str):
            self._namespace = value
        @property
        def namespaceId(self) -> byte: ...
        @namespaceId.setter
        def namespaceId(self, value: byte):
            self._namespaceId = value
        @property
        def data(self) -> List[byte]: ...
        @data.setter
        def data(self, value: List[byte]):
            self._data = value


    class DescriptorQuality(Enum):
        highQuality = "highQuality"
        mediumQuality = "mediumQuality"
        lowQuality = "lowQuality"
        unknownQuality = "unknownQuality"


    class DeviceProtocol(Enum):
        NVMe = "NVMe"
        SCSI = "SCSI"


    class ScsiLunType(Enum):
        disk = "disk"
        tape = "tape"
        printer = "printer"
        processor = "processor"
        worm = "worm"
        cdrom = "cdrom"
        scanner = "scanner"
        opticalDevice = "opticalDevice"
        mediaChanger = "mediaChanger"
        communications = "communications"
        storageArrayController = "storageArrayController"
        enclosure = "enclosure"
        unknown = "unknown"


class ScsiTopology(vmodl.DynamicData):
    @property
    def adapter(self) -> List[ScsiTopology.Interface]: ...
    @adapter.setter
    def adapter(self, value: List[ScsiTopology.Interface]):
        self._adapter = value


    class Interface(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def adapter(self) -> Link: ...
        @adapter.setter
        def adapter(self, value: Link):
            self._adapter = value
        @property
        def target(self) -> List[ScsiTopology.Target]: ...
        @target.setter
        def target(self, value: List[ScsiTopology.Target]):
            self._target = value


    class Lun(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def lun(self) -> int: ...
        @lun.setter
        def lun(self, value: int):
            self._lun = value
        @property
        def scsiLun(self) -> Link: ...
        @scsiLun.setter
        def scsiLun(self, value: Link):
            self._scsiLun = value


    class Target(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def target(self) -> int: ...
        @target.setter
        def target(self, value: int):
            self._target = value
        @property
        def lun(self) -> List[ScsiTopology.Lun]: ...
        @lun.setter
        def lun(self, value: List[ScsiTopology.Lun]):
            self._lun = value
        @property
        def transport(self) -> TargetTransport: ...
        @transport.setter
        def transport(self, value: TargetTransport):
            self._transport = value


class SecuritySpec(vmodl.DynamicData):
    @property
    def adminPassword(self) -> str: ...
    @adminPassword.setter
    def adminPassword(self, value: str):
        self._adminPassword = value
    @property
    def removePermission(self) -> List[vim.AuthorizationManager.Permission]: ...
    @removePermission.setter
    def removePermission(self, value: List[vim.AuthorizationManager.Permission]):
        self._removePermission = value
    @property
    def addPermission(self) -> List[vim.AuthorizationManager.Permission]: ...
    @addPermission.setter
    def addPermission(self, value: List[vim.AuthorizationManager.Permission]):
        self._addPermission = value


class SerialAttachedHba(HostBusAdapter):
    @property
    def nodeWorldWideName(self) -> str: ...
    @nodeWorldWideName.setter
    def nodeWorldWideName(self, value: str):
        self._nodeWorldWideName = value


class SerialAttachedTargetTransport(TargetTransport): ...


class Service(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def label(self) -> str: ...
    @label.setter
    def label(self, value: str):
        self._label = value
    @property
    def required(self) -> bool: ...
    @required.setter
    def required(self, value: bool):
        self._required = value
    @property
    def uninstallable(self) -> bool: ...
    @uninstallable.setter
    def uninstallable(self, value: bool):
        self._uninstallable = value
    @property
    def running(self) -> bool: ...
    @running.setter
    def running(self, value: bool):
        self._running = value
    @property
    def ruleset(self) -> List[str]: ...
    @ruleset.setter
    def ruleset(self, value: List[str]):
        self._ruleset = value
    @property
    def policy(self) -> str: ...
    @policy.setter
    def policy(self, value: str):
        self._policy = value
    @property
    def sourcePackage(self) -> Service.SourcePackage: ...
    @sourcePackage.setter
    def sourcePackage(self, value: Service.SourcePackage):
        self._sourcePackage = value


    class SourcePackage(vmodl.DynamicData):
        @property
        def sourcePackageName(self) -> str: ...
        @sourcePackageName.setter
        def sourcePackageName(self, value: str):
            self._sourcePackageName = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value


    class Policy(Enum):
        on = "on"
        automatic = "automatic"
        off = "off"


class ServiceConfig(vmodl.DynamicData):
    @property
    def serviceId(self) -> str: ...
    @serviceId.setter
    def serviceId(self, value: str):
        self._serviceId = value
    @property
    def startupPolicy(self) -> str: ...
    @startupPolicy.setter
    def startupPolicy(self, value: str):
        self._startupPolicy = value


class ServiceInfo(vmodl.DynamicData):
    @property
    def service(self) -> List[Service]: ...
    @service.setter
    def service(self, value: List[Service]):
        self._service = value


class SevInfo(vmodl.DynamicData):
    @property
    def sevState(self) -> str: ...
    @sevState.setter
    def sevState(self, value: str):
        self._sevState = value
    @property
    def maxSevEsGuests(self) -> long: ...
    @maxSevEsGuests.setter
    def maxSevEsGuests(self, value: long):
        self._maxSevEsGuests = value


    class SevState(Enum):
        uninitialized = "uninitialized"
        initialized = "initialized"
        working = "working"


class SgxInfo(vmodl.DynamicData):
    @property
    def sgxState(self) -> str: ...
    @sgxState.setter
    def sgxState(self, value: str):
        self._sgxState = value
    @property
    def totalEpcMemory(self) -> long: ...
    @totalEpcMemory.setter
    def totalEpcMemory(self, value: long):
        self._totalEpcMemory = value
    @property
    def flcMode(self) -> str: ...
    @flcMode.setter
    def flcMode(self, value: str):
        self._flcMode = value
    @property
    def lePubKeyHash(self) -> str: ...
    @lePubKeyHash.setter
    def lePubKeyHash(self, value: str):
        self._lePubKeyHash = value
    @property
    def registrationInfo(self) -> SgxRegistrationInfo: ...
    @registrationInfo.setter
    def registrationInfo(self, value: SgxRegistrationInfo):
        self._registrationInfo = value


    class FlcModes(Enum):
        off = "off"
        locked = "locked"
        unlocked = "unlocked"


    class SgxStates(Enum):
        notPresent = "notPresent"
        disabledBIOS = "disabledBIOS"
        disabledCFW101 = "disabledCFW101"
        disabledCPUMismatch = "disabledCPUMismatch"
        disabledNoFLC = "disabledNoFLC"
        disabledNUMAUnsup = "disabledNUMAUnsup"
        disabledMaxEPCRegs = "disabledMaxEPCRegs"
        enabled = "enabled"


class SgxRegistrationInfo(vmodl.DynamicData):
    @property
    def status(self) -> str: ...
    @status.setter
    def status(self, value: str):
        self._status = value
    @property
    def biosError(self) -> int: ...
    @biosError.setter
    def biosError(self, value: int):
        self._biosError = value
    @property
    def registrationUrl(self) -> str: ...
    @registrationUrl.setter
    def registrationUrl(self, value: str):
        self._registrationUrl = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def ppid(self) -> str: ...
    @ppid.setter
    def ppid(self, value: str):
        self._ppid = value
    @property
    def lastRegisteredTime(self) -> datetime: ...
    @lastRegisteredTime.setter
    def lastRegisteredTime(self, value: datetime):
        self._lastRegisteredTime = value


    class RegistrationStatus(Enum):
        notApplicable = "notApplicable"
        incomplete = "incomplete"
        complete = "complete"


    class RegistrationType(Enum):
        manifest = "manifest"
        addPackage = "addPackage"


class SharedGpuCapabilities(vmodl.DynamicData):
    @property
    def vgpu(self) -> str: ...
    @vgpu.setter
    def vgpu(self, value: str):
        self._vgpu = value
    @property
    def diskSnapshotSupported(self) -> bool: ...
    @diskSnapshotSupported.setter
    def diskSnapshotSupported(self, value: bool):
        self._diskSnapshotSupported = value
    @property
    def memorySnapshotSupported(self) -> bool: ...
    @memorySnapshotSupported.setter
    def memorySnapshotSupported(self, value: bool):
        self._memorySnapshotSupported = value
    @property
    def suspendSupported(self) -> bool: ...
    @suspendSupported.setter
    def suspendSupported(self, value: bool):
        self._suspendSupported = value
    @property
    def migrateSupported(self) -> bool: ...
    @migrateSupported.setter
    def migrateSupported(self, value: bool):
        self._migrateSupported = value


class SoftwarePackage(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def vendor(self) -> str: ...
    @vendor.setter
    def vendor(self, value: str):
        self._vendor = value
    @property
    def acceptanceLevel(self) -> str: ...
    @acceptanceLevel.setter
    def acceptanceLevel(self, value: str):
        self._acceptanceLevel = value
    @property
    def summary(self) -> str: ...
    @summary.setter
    def summary(self, value: str):
        self._summary = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def referenceURL(self) -> List[str]: ...
    @referenceURL.setter
    def referenceURL(self, value: List[str]):
        self._referenceURL = value
    @property
    def creationDate(self) -> datetime: ...
    @creationDate.setter
    def creationDate(self, value: datetime):
        self._creationDate = value
    @property
    def depends(self) -> List[SoftwarePackage.Relation]: ...
    @depends.setter
    def depends(self, value: List[SoftwarePackage.Relation]):
        self._depends = value
    @property
    def conflicts(self) -> List[SoftwarePackage.Relation]: ...
    @conflicts.setter
    def conflicts(self, value: List[SoftwarePackage.Relation]):
        self._conflicts = value
    @property
    def replaces(self) -> List[SoftwarePackage.Relation]: ...
    @replaces.setter
    def replaces(self, value: List[SoftwarePackage.Relation]):
        self._replaces = value
    @property
    def provides(self) -> List[str]: ...
    @provides.setter
    def provides(self, value: List[str]):
        self._provides = value
    @property
    def maintenanceModeRequired(self) -> bool: ...
    @maintenanceModeRequired.setter
    def maintenanceModeRequired(self, value: bool):
        self._maintenanceModeRequired = value
    @property
    def hardwarePlatformsRequired(self) -> List[str]: ...
    @hardwarePlatformsRequired.setter
    def hardwarePlatformsRequired(self, value: List[str]):
        self._hardwarePlatformsRequired = value
    @property
    def capability(self) -> SoftwarePackage.Capability: ...
    @capability.setter
    def capability(self, value: SoftwarePackage.Capability):
        self._capability = value
    @property
    def tag(self) -> List[str]: ...
    @tag.setter
    def tag(self, value: List[str]):
        self._tag = value
    @property
    def payload(self) -> List[str]: ...
    @payload.setter
    def payload(self, value: List[str]):
        self._payload = value


    class Capability(vmodl.DynamicData):
        @property
        def liveInstallAllowed(self) -> bool: ...
        @liveInstallAllowed.setter
        def liveInstallAllowed(self, value: bool):
            self._liveInstallAllowed = value
        @property
        def liveRemoveAllowed(self) -> bool: ...
        @liveRemoveAllowed.setter
        def liveRemoveAllowed(self, value: bool):
            self._liveRemoveAllowed = value
        @property
        def statelessReady(self) -> bool: ...
        @statelessReady.setter
        def statelessReady(self, value: bool):
            self._statelessReady = value
        @property
        def overlay(self) -> bool: ...
        @overlay.setter
        def overlay(self, value: bool):
            self._overlay = value


    class Relation(vmodl.DynamicData):
        @property
        def constraint(self) -> str: ...
        @constraint.setter
        def constraint(self, value: str):
            self._constraint = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def version(self) -> str: ...
        @version.setter
        def version(self, value: str):
            self._version = value


    class Constraint(Enum):
        equals = "equals"
        lessThan = "lessThan"
        lessThanEqual = "lessThanEqual"
        greaterThanEqual = "greaterThanEqual"
        greaterThan = "greaterThan"


    class VibType(Enum):
        bootbank = "bootbank"
        tools = "tools"
        meta = "meta"


class SriovConfig(PciPassthruConfig):
    @property
    def sriovEnabled(self) -> bool: ...
    @sriovEnabled.setter
    def sriovEnabled(self, value: bool):
        self._sriovEnabled = value
    @property
    def numVirtualFunction(self) -> int: ...
    @numVirtualFunction.setter
    def numVirtualFunction(self, value: int):
        self._numVirtualFunction = value


class SriovDevicePoolInfo(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class SriovInfo(PciPassthruInfo):
    @property
    def sriovEnabled(self) -> bool: ...
    @sriovEnabled.setter
    def sriovEnabled(self, value: bool):
        self._sriovEnabled = value
    @property
    def sriovCapable(self) -> bool: ...
    @sriovCapable.setter
    def sriovCapable(self, value: bool):
        self._sriovCapable = value
    @property
    def sriovActive(self) -> bool: ...
    @sriovActive.setter
    def sriovActive(self, value: bool):
        self._sriovActive = value
    @property
    def numVirtualFunctionRequested(self) -> int: ...
    @numVirtualFunctionRequested.setter
    def numVirtualFunctionRequested(self, value: int):
        self._numVirtualFunctionRequested = value
    @property
    def numVirtualFunction(self) -> int: ...
    @numVirtualFunction.setter
    def numVirtualFunction(self, value: int):
        self._numVirtualFunction = value
    @property
    def maxVirtualFunctionSupported(self) -> int: ...
    @maxVirtualFunctionSupported.setter
    def maxVirtualFunctionSupported(self, value: int):
        self._maxVirtualFunctionSupported = value


class SriovNetworkDevicePoolInfo(SriovDevicePoolInfo):
    @property
    def switchKey(self) -> str: ...
    @switchKey.setter
    def switchKey(self, value: str):
        self._switchKey = value
    @property
    def switchUuid(self) -> str: ...
    @switchUuid.setter
    def switchUuid(self, value: str):
        self._switchUuid = value
    @property
    def pnic(self) -> List[PhysicalNic]: ...
    @pnic.setter
    def pnic(self, value: List[PhysicalNic]):
        self._pnic = value


class SslThumbprintInfo(vmodl.DynamicData):
    @property
    def principal(self) -> str: ...
    @principal.setter
    def principal(self, value: str):
        self._principal = value
    @property
    def ownerTag(self) -> str: ...
    @ownerTag.setter
    def ownerTag(self, value: str):
        self._ownerTag = value
    @property
    def sslThumbprints(self) -> List[str]: ...
    @sslThumbprints.setter
    def sslThumbprints(self, value: List[str]):
        self._sslThumbprints = value


class StorageArrayTypePolicyOption(vmodl.DynamicData):
    @property
    def policy(self) -> vim.ElementDescription: ...
    @policy.setter
    def policy(self, value: vim.ElementDescription):
        self._policy = value


class StorageDeviceInfo(vmodl.DynamicData):
    @property
    def hostBusAdapter(self) -> List[HostBusAdapter]: ...
    @hostBusAdapter.setter
    def hostBusAdapter(self, value: List[HostBusAdapter]):
        self._hostBusAdapter = value
    @property
    def scsiLun(self) -> List[ScsiLun]: ...
    @scsiLun.setter
    def scsiLun(self, value: List[ScsiLun]):
        self._scsiLun = value
    @property
    def scsiTopology(self) -> ScsiTopology: ...
    @scsiTopology.setter
    def scsiTopology(self, value: ScsiTopology):
        self._scsiTopology = value
    @property
    def nvmeTopology(self) -> NvmeTopology: ...
    @nvmeTopology.setter
    def nvmeTopology(self, value: NvmeTopology):
        self._nvmeTopology = value
    @property
    def multipathInfo(self) -> MultipathInfo: ...
    @multipathInfo.setter
    def multipathInfo(self, value: MultipathInfo):
        self._multipathInfo = value
    @property
    def plugStoreTopology(self) -> PlugStoreTopology: ...
    @plugStoreTopology.setter
    def plugStoreTopology(self, value: PlugStoreTopology):
        self._plugStoreTopology = value
    @property
    def softwareInternetScsiEnabled(self) -> bool: ...
    @softwareInternetScsiEnabled.setter
    def softwareInternetScsiEnabled(self, value: bool):
        self._softwareInternetScsiEnabled = value


class Summary(vmodl.DynamicData):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def hardware(self) -> Summary.HardwareSummary: ...
    @hardware.setter
    def hardware(self, value: Summary.HardwareSummary):
        self._hardware = value
    @property
    def runtime(self) -> RuntimeInfo: ...
    @runtime.setter
    def runtime(self, value: RuntimeInfo):
        self._runtime = value
    @property
    def config(self) -> Summary.ConfigSummary: ...
    @config.setter
    def config(self, value: Summary.ConfigSummary):
        self._config = value
    @property
    def quickStats(self) -> Summary.QuickStats: ...
    @quickStats.setter
    def quickStats(self, value: Summary.QuickStats):
        self._quickStats = value
    @property
    def overallStatus(self) -> vim.ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']: ...
    @overallStatus.setter
    def overallStatus(self, value: vim.ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']):
        self._overallStatus = value
    @property
    def rebootRequired(self) -> bool: ...
    @rebootRequired.setter
    def rebootRequired(self, value: bool):
        self._rebootRequired = value
    @property
    def customValue(self) -> List[vim.CustomFieldsManager.Value]: ...
    @customValue.setter
    def customValue(self, value: List[vim.CustomFieldsManager.Value]):
        self._customValue = value
    @property
    def managementServerIp(self) -> str: ...
    @managementServerIp.setter
    def managementServerIp(self, value: str):
        self._managementServerIp = value
    @property
    def maxEVCModeKey(self) -> str: ...
    @maxEVCModeKey.setter
    def maxEVCModeKey(self, value: str):
        self._maxEVCModeKey = value
    @property
    def currentEVCModeKey(self) -> str: ...
    @currentEVCModeKey.setter
    def currentEVCModeKey(self, value: str):
        self._currentEVCModeKey = value
    @property
    def currentEVCGraphicsModeKey(self) -> str: ...
    @currentEVCGraphicsModeKey.setter
    def currentEVCGraphicsModeKey(self, value: str):
        self._currentEVCGraphicsModeKey = value
    @property
    def gateway(self) -> Summary.GatewaySummary: ...
    @gateway.setter
    def gateway(self, value: Summary.GatewaySummary):
        self._gateway = value
    @property
    def tpmAttestation(self) -> TpmAttestationInfo: ...
    @tpmAttestation.setter
    def tpmAttestation(self, value: TpmAttestationInfo):
        self._tpmAttestation = value
    @property
    def trustAuthorityAttestationInfos(self) -> List[TrustAuthorityAttestationInfo]: ...
    @trustAuthorityAttestationInfos.setter
    def trustAuthorityAttestationInfos(self, value: List[TrustAuthorityAttestationInfo]):
        self._trustAuthorityAttestationInfos = value


    class ConfigSummary(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def port(self) -> int: ...
        @port.setter
        def port(self, value: int):
            self._port = value
        @property
        def sslThumbprint(self) -> str: ...
        @sslThumbprint.setter
        def sslThumbprint(self, value: str):
            self._sslThumbprint = value
        @property
        def product(self) -> vim.AboutInfo: ...
        @product.setter
        def product(self, value: vim.AboutInfo):
            self._product = value
        @property
        def vmotionEnabled(self) -> bool: ...
        @vmotionEnabled.setter
        def vmotionEnabled(self, value: bool):
            self._vmotionEnabled = value
        @property
        def faultToleranceEnabled(self) -> bool: ...
        @faultToleranceEnabled.setter
        def faultToleranceEnabled(self, value: bool):
            self._faultToleranceEnabled = value
        @property
        def featureVersion(self) -> List[FeatureVersionInfo]: ...
        @featureVersion.setter
        def featureVersion(self, value: List[FeatureVersionInfo]):
            self._featureVersion = value
        @property
        def agentVmDatastore(self) -> vim.Datastore: ...
        @agentVmDatastore.setter
        def agentVmDatastore(self, value: vim.Datastore):
            self._agentVmDatastore = value
        @property
        def agentVmNetwork(self) -> vim.Network: ...
        @agentVmNetwork.setter
        def agentVmNetwork(self, value: vim.Network):
            self._agentVmNetwork = value


    class GatewaySummary(vmodl.DynamicData):
        @property
        def gatewayType(self) -> str: ...
        @gatewayType.setter
        def gatewayType(self, value: str):
            self._gatewayType = value
        @property
        def gatewayId(self) -> str: ...
        @gatewayId.setter
        def gatewayId(self, value: str):
            self._gatewayId = value


    class HardwareSummary(vmodl.DynamicData):
        @property
        def vendor(self) -> str: ...
        @vendor.setter
        def vendor(self, value: str):
            self._vendor = value
        @property
        def model(self) -> str: ...
        @model.setter
        def model(self, value: str):
            self._model = value
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def otherIdentifyingInfo(self) -> List[SystemIdentificationInfo]: ...
        @otherIdentifyingInfo.setter
        def otherIdentifyingInfo(self, value: List[SystemIdentificationInfo]):
            self._otherIdentifyingInfo = value
        @property
        def memorySize(self) -> long: ...
        @memorySize.setter
        def memorySize(self, value: long):
            self._memorySize = value
        @property
        def cpuModel(self) -> str: ...
        @cpuModel.setter
        def cpuModel(self, value: str):
            self._cpuModel = value
        @property
        def cpuMhz(self) -> int: ...
        @cpuMhz.setter
        def cpuMhz(self, value: int):
            self._cpuMhz = value
        @property
        def numCpuPkgs(self) -> short: ...
        @numCpuPkgs.setter
        def numCpuPkgs(self, value: short):
            self._numCpuPkgs = value
        @property
        def numCpuCores(self) -> short: ...
        @numCpuCores.setter
        def numCpuCores(self, value: short):
            self._numCpuCores = value
        @property
        def numCpuThreads(self) -> short: ...
        @numCpuThreads.setter
        def numCpuThreads(self, value: short):
            self._numCpuThreads = value
        @property
        def numNics(self) -> int: ...
        @numNics.setter
        def numNics(self, value: int):
            self._numNics = value
        @property
        def numHBAs(self) -> int: ...
        @numHBAs.setter
        def numHBAs(self, value: int):
            self._numHBAs = value


    class QuickStats(vmodl.DynamicData):
        @property
        def overallCpuUsage(self) -> int: ...
        @overallCpuUsage.setter
        def overallCpuUsage(self, value: int):
            self._overallCpuUsage = value
        @property
        def overallMemoryUsage(self) -> int: ...
        @overallMemoryUsage.setter
        def overallMemoryUsage(self, value: int):
            self._overallMemoryUsage = value
        @property
        def distributedCpuFairness(self) -> int: ...
        @distributedCpuFairness.setter
        def distributedCpuFairness(self, value: int):
            self._distributedCpuFairness = value
        @property
        def distributedMemoryFairness(self) -> int: ...
        @distributedMemoryFairness.setter
        def distributedMemoryFairness(self, value: int):
            self._distributedMemoryFairness = value
        @property
        def availablePMemCapacity(self) -> int: ...
        @availablePMemCapacity.setter
        def availablePMemCapacity(self, value: int):
            self._availablePMemCapacity = value
        @property
        def uptime(self) -> int: ...
        @uptime.setter
        def uptime(self, value: int):
            self._uptime = value


class SystemEventInfo(vmodl.DynamicData):
    @property
    def recordId(self) -> long: ...
    @recordId.setter
    def recordId(self, value: long):
        self._recordId = value
    @property
    def when(self) -> str: ...
    @when.setter
    def when(self, value: str):
        self._when = value
    @property
    def selType(self) -> long: ...
    @selType.setter
    def selType(self, value: long):
        self._selType = value
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str):
        self._message = value
    @property
    def sensorNumber(self) -> long: ...
    @sensorNumber.setter
    def sensorNumber(self, value: long):
        self._sensorNumber = value


class SystemHealthInfo(vmodl.DynamicData):
    @property
    def numericSensorInfo(self) -> List[NumericSensorInfo]: ...
    @numericSensorInfo.setter
    def numericSensorInfo(self, value: List[NumericSensorInfo]):
        self._numericSensorInfo = value


class SystemIdentificationInfo(vmodl.DynamicData):
    @property
    def identifierValue(self) -> str: ...
    @identifierValue.setter
    def identifierValue(self, value: str):
        self._identifierValue = value
    @property
    def identifierType(self) -> vim.ElementDescription: ...
    @identifierType.setter
    def identifierType(self, value: vim.ElementDescription):
        self._identifierType = value


    class Identifier(Enum):
        AssetTag = "AssetTag"
        ServiceTag = "ServiceTag"
        OemSpecificString = "OemSpecificString"
        EnclosureSerialNumberTag = "EnclosureSerialNumberTag"
        SerialNumberTag = "SerialNumberTag"


class SystemInfo(vmodl.DynamicData):
    @property
    def vendor(self) -> str: ...
    @vendor.setter
    def vendor(self, value: str):
        self._vendor = value
    @property
    def model(self) -> str: ...
    @model.setter
    def model(self, value: str):
        self._model = value
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def otherIdentifyingInfo(self) -> List[SystemIdentificationInfo]: ...
    @otherIdentifyingInfo.setter
    def otherIdentifyingInfo(self, value: List[SystemIdentificationInfo]):
        self._otherIdentifyingInfo = value
    @property
    def serialNumber(self) -> str: ...
    @serialNumber.setter
    def serialNumber(self, value: str):
        self._serialNumber = value
    @property
    def qualifiedName(self) -> List[QualifiedName]: ...
    @qualifiedName.setter
    def qualifiedName(self, value: List[QualifiedName]):
        self._qualifiedName = value
    @property
    def vvolHostNQN(self) -> QualifiedName: ...
    @vvolHostNQN.setter
    def vvolHostNQN(self, value: QualifiedName):
        self._vvolHostNQN = value
    @property
    def vvolHostId(self) -> str: ...
    @vvolHostId.setter
    def vvolHostId(self, value: str):
        self._vvolHostId = value


class SystemResourceInfo(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def config(self) -> vim.ResourceConfigSpec: ...
    @config.setter
    def config(self, value: vim.ResourceConfigSpec):
        self._config = value
    @property
    def child(self) -> List[SystemResourceInfo]: ...
    @child.setter
    def child(self, value: List[SystemResourceInfo]):
        self._child = value


class SystemSwapConfiguration(vmodl.DynamicData):
    @property
    def option(self) -> List[SystemSwapConfiguration.SystemSwapOption]: ...
    @option.setter
    def option(self, value: List[SystemSwapConfiguration.SystemSwapOption]):
        self._option = value


    class DatastoreOption(SystemSwapConfiguration.SystemSwapOption):
        @property
        def datastore(self) -> str: ...
        @datastore.setter
        def datastore(self, value: str):
            self._datastore = value


    class DisabledOption(SystemSwapConfiguration.SystemSwapOption): ...


    class HostCacheOption(SystemSwapConfiguration.SystemSwapOption): ...


    class HostLocalSwapOption(SystemSwapConfiguration.SystemSwapOption): ...


    class SystemSwapOption(vmodl.DynamicData):
        @property
        def key(self) -> int: ...
        @key.setter
        def key(self, value: int):
            self._key = value


class TargetTransport(vmodl.DynamicData): ...


class TcpHba(HostBusAdapter):
    @property
    def associatedPnic(self) -> str: ...
    @associatedPnic.setter
    def associatedPnic(self, value: str):
        self._associatedPnic = value


class TcpHbaCreateSpec(HbaCreateSpec):
    @property
    def pnic(self) -> str: ...
    @pnic.setter
    def pnic(self, value: str):
        self._pnic = value


class TcpTargetTransport(TargetTransport): ...


class TpmAttestationInfo(vmodl.DynamicData):
    @property
    def time(self) -> datetime: ...
    @time.setter
    def time(self, value: datetime):
        self._time = value
    @property
    def status(self) -> TpmAttestationInfo.AcceptanceStatus | Literal['notAccepted', 'accepted']: ...
    @status.setter
    def status(self, value: TpmAttestationInfo.AcceptanceStatus | Literal['notAccepted', 'accepted']):
        self._status = value
    @property
    def message(self) -> vmodl.LocalizableMessage: ...
    @message.setter
    def message(self, value: vmodl.LocalizableMessage):
        self._message = value


    class AcceptanceStatus(Enum):
        notAccepted = "notAccepted"
        accepted = "accepted"


class TpmAttestationReport(vmodl.DynamicData):
    @property
    def tpmPcrValues(self) -> List[TpmDigestInfo]: ...
    @tpmPcrValues.setter
    def tpmPcrValues(self, value: List[TpmDigestInfo]):
        self._tpmPcrValues = value
    @property
    def tpmEvents(self) -> List[TpmEventLogEntry]: ...
    @tpmEvents.setter
    def tpmEvents(self, value: List[TpmEventLogEntry]):
        self._tpmEvents = value
    @property
    def tpmLogReliable(self) -> bool: ...
    @tpmLogReliable.setter
    def tpmLogReliable(self, value: bool):
        self._tpmLogReliable = value


class TpmBootCompleteEventDetails(TpmEventDetails): ...


class TpmBootSecurityOptionEventDetails(TpmEventDetails):
    @property
    def bootSecurityOption(self) -> str: ...
    @bootSecurityOption.setter
    def bootSecurityOption(self, value: str):
        self._bootSecurityOption = value


class TpmCommandEventDetails(TpmEventDetails):
    @property
    def commandLine(self) -> str: ...
    @commandLine.setter
    def commandLine(self, value: str):
        self._commandLine = value


class TpmDigestInfo(DigestInfo):
    @property
    def pcrNumber(self) -> int: ...
    @pcrNumber.setter
    def pcrNumber(self, value: int):
        self._pcrNumber = value


class TpmEventDetails(vmodl.DynamicData):
    @property
    def dataHash(self) -> List[byte]: ...
    @dataHash.setter
    def dataHash(self, value: List[byte]):
        self._dataHash = value
    @property
    def dataHashMethod(self) -> str: ...
    @dataHashMethod.setter
    def dataHashMethod(self, value: str):
        self._dataHashMethod = value


class TpmEventLogEntry(vmodl.DynamicData):
    @property
    def pcrIndex(self) -> int: ...
    @pcrIndex.setter
    def pcrIndex(self, value: int):
        self._pcrIndex = value
    @property
    def eventDetails(self) -> TpmEventDetails: ...
    @eventDetails.setter
    def eventDetails(self, value: TpmEventDetails):
        self._eventDetails = value


class TpmNvTagEventDetails(TpmBootSecurityOptionEventDetails): ...


class TpmOptionEventDetails(TpmEventDetails):
    @property
    def optionsFileName(self) -> str: ...
    @optionsFileName.setter
    def optionsFileName(self, value: str):
        self._optionsFileName = value
    @property
    def bootOptions(self) -> List[byte]: ...
    @bootOptions.setter
    def bootOptions(self, value: List[byte]):
        self._bootOptions = value


class TpmSignerEventDetails(TpmBootSecurityOptionEventDetails): ...


class TpmSoftwareComponentEventDetails(TpmEventDetails):
    @property
    def componentName(self) -> str: ...
    @componentName.setter
    def componentName(self, value: str):
        self._componentName = value
    @property
    def vibName(self) -> str: ...
    @vibName.setter
    def vibName(self, value: str):
        self._vibName = value
    @property
    def vibVersion(self) -> str: ...
    @vibVersion.setter
    def vibVersion(self, value: str):
        self._vibVersion = value
    @property
    def vibVendor(self) -> str: ...
    @vibVendor.setter
    def vibVendor(self, value: str):
        self._vibVendor = value


class TpmVersionEventDetails(TpmEventDetails):
    @property
    def version(self) -> binary: ...
    @version.setter
    def version(self, value: binary):
        self._version = value


class TrustAuthorityAttestationInfo(vmodl.DynamicData):
    @property
    def attestationStatus(self) -> str: ...
    @attestationStatus.setter
    def attestationStatus(self, value: str):
        self._attestationStatus = value
    @property
    def serviceId(self) -> str: ...
    @serviceId.setter
    def serviceId(self, value: str):
        self._serviceId = value
    @property
    def attestedAt(self) -> datetime: ...
    @attestedAt.setter
    def attestedAt(self, value: datetime):
        self._attestedAt = value
    @property
    def attestedUntil(self) -> datetime: ...
    @attestedUntil.setter
    def attestedUntil(self, value: datetime):
        self._attestedUntil = value
    @property
    def messages(self) -> List[vmodl.LocalizableMessage]: ...
    @messages.setter
    def messages(self, value: List[vmodl.LocalizableMessage]):
        self._messages = value


    class AttestationStatus(Enum):
        attested = "attested"
        notAttested = "notAttested"
        unknown = "unknown"


class UnresolvedVmfsExtent(vmodl.DynamicData):
    @property
    def device(self) -> ScsiDisk.Partition: ...
    @device.setter
    def device(self, value: ScsiDisk.Partition):
        self._device = value
    @property
    def devicePath(self) -> str: ...
    @devicePath.setter
    def devicePath(self, value: str):
        self._devicePath = value
    @property
    def vmfsUuid(self) -> str: ...
    @vmfsUuid.setter
    def vmfsUuid(self, value: str):
        self._vmfsUuid = value
    @property
    def isHeadExtent(self) -> bool: ...
    @isHeadExtent.setter
    def isHeadExtent(self, value: bool):
        self._isHeadExtent = value
    @property
    def ordinal(self) -> int: ...
    @ordinal.setter
    def ordinal(self, value: int):
        self._ordinal = value
    @property
    def startBlock(self) -> int: ...
    @startBlock.setter
    def startBlock(self, value: int):
        self._startBlock = value
    @property
    def endBlock(self) -> int: ...
    @endBlock.setter
    def endBlock(self, value: int):
        self._endBlock = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


    class UnresolvedReason(Enum):
        diskIdMismatch = "diskIdMismatch"
        uuidConflict = "uuidConflict"


class UnresolvedVmfsResignatureSpec(vmodl.DynamicData):
    @property
    def extentDevicePath(self) -> List[str]: ...
    @extentDevicePath.setter
    def extentDevicePath(self, value: List[str]):
        self._extentDevicePath = value


class UnresolvedVmfsResolutionResult(vmodl.DynamicData):
    @property
    def spec(self) -> UnresolvedVmfsResolutionSpec: ...
    @spec.setter
    def spec(self, value: UnresolvedVmfsResolutionSpec):
        self._spec = value
    @property
    def vmfs(self) -> VmfsVolume: ...
    @vmfs.setter
    def vmfs(self, value: VmfsVolume):
        self._vmfs = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class UnresolvedVmfsResolutionSpec(vmodl.DynamicData):
    @property
    def extentDevicePath(self) -> List[str]: ...
    @extentDevicePath.setter
    def extentDevicePath(self, value: List[str]):
        self._extentDevicePath = value
    @property
    def uuidResolution(self) -> str: ...
    @uuidResolution.setter
    def uuidResolution(self, value: str):
        self._uuidResolution = value


    class VmfsUuidResolution(Enum):
        resignature = "resignature"
        forceMount = "forceMount"


class UnresolvedVmfsVolume(vmodl.DynamicData):
    @property
    def extent(self) -> List[UnresolvedVmfsExtent]: ...
    @extent.setter
    def extent(self, value: List[UnresolvedVmfsExtent]):
        self._extent = value
    @property
    def vmfsLabel(self) -> str: ...
    @vmfsLabel.setter
    def vmfsLabel(self, value: str):
        self._vmfsLabel = value
    @property
    def vmfsUuid(self) -> str: ...
    @vmfsUuid.setter
    def vmfsUuid(self, value: str):
        self._vmfsUuid = value
    @property
    def totalBlocks(self) -> int: ...
    @totalBlocks.setter
    def totalBlocks(self, value: int):
        self._totalBlocks = value
    @property
    def resolveStatus(self) -> UnresolvedVmfsVolume.ResolveStatus: ...
    @resolveStatus.setter
    def resolveStatus(self, value: UnresolvedVmfsVolume.ResolveStatus):
        self._resolveStatus = value


    class ResolveStatus(vmodl.DynamicData):
        @property
        def resolvable(self) -> bool: ...
        @resolvable.setter
        def resolvable(self, value: bool):
            self._resolvable = value
        @property
        def incompleteExtents(self) -> bool: ...
        @incompleteExtents.setter
        def incompleteExtents(self, value: bool):
            self._incompleteExtents = value
        @property
        def multipleCopies(self) -> bool: ...
        @multipleCopies.setter
        def multipleCopies(self, value: bool):
            self._multipleCopies = value


class VFlashResourceConfigurationResult(vmodl.DynamicData):
    @property
    def devicePath(self) -> List[str]: ...
    @devicePath.setter
    def devicePath(self, value: List[str]):
        self._devicePath = value
    @property
    def vffs(self) -> VffsVolume: ...
    @vffs.setter
    def vffs(self, value: VffsVolume):
        self._vffs = value
    @property
    def diskConfigurationResult(self) -> List[DiskConfigurationResult]: ...
    @diskConfigurationResult.setter
    def diskConfigurationResult(self, value: List[DiskConfigurationResult]):
        self._diskConfigurationResult = value


class VMotionConfig(vmodl.DynamicData):
    @property
    def vmotionNicKey(self) -> str: ...
    @vmotionNicKey.setter
    def vmotionNicKey(self, value: str):
        self._vmotionNicKey = value
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value


class VMotionInfo(vmodl.DynamicData):
    @property
    def netConfig(self) -> VMotionSystem.NetConfig: ...
    @netConfig.setter
    def netConfig(self, value: VMotionSystem.NetConfig):
        self._netConfig = value
    @property
    def ipConfig(self) -> IpConfig: ...
    @ipConfig.setter
    def ipConfig(self, value: IpConfig):
        self._ipConfig = value


class VMotionManager():


    class DstInstantCloneResult(vmodl.DynamicData):
        @property
        def dstVmId(self) -> int: ...
        @dstVmId.setter
        def dstVmId(self, value: int):
            self._dstVmId = value
        @property
        def startTime(self) -> long: ...
        @startTime.setter
        def startTime(self, value: long):
            self._startTime = value
        @property
        def cptLoadTime(self) -> long: ...
        @cptLoadTime.setter
        def cptLoadTime(self, value: long):
            self._cptLoadTime = value
        @property
        def cptLoadDoneTime(self) -> long: ...
        @cptLoadDoneTime.setter
        def cptLoadDoneTime(self, value: long):
            self._cptLoadDoneTime = value
        @property
        def replicateMemDoneTime(self) -> long: ...
        @replicateMemDoneTime.setter
        def replicateMemDoneTime(self, value: long):
            self._replicateMemDoneTime = value
        @property
        def endTime(self) -> long: ...
        @endTime.setter
        def endTime(self, value: long):
            self._endTime = value
        @property
        def cptXferTime(self) -> long: ...
        @cptXferTime.setter
        def cptXferTime(self, value: long):
            self._cptXferTime = value
        @property
        def cptCacheUsed(self) -> long: ...
        @cptCacheUsed.setter
        def cptCacheUsed(self, value: long):
            self._cptCacheUsed = value
        @property
        def devCptStreamSize(self) -> long: ...
        @devCptStreamSize.setter
        def devCptStreamSize(self, value: long):
            self._devCptStreamSize = value
        @property
        def devCptStreamTime(self) -> long: ...
        @devCptStreamTime.setter
        def devCptStreamTime(self, value: long):
            self._devCptStreamTime = value


    class SrcInstantCloneResult(vmodl.DynamicData):
        @property
        def startTime(self) -> long: ...
        @startTime.setter
        def startTime(self, value: long):
            self._startTime = value
        @property
        def quiesceTime(self) -> long: ...
        @quiesceTime.setter
        def quiesceTime(self, value: long):
            self._quiesceTime = value
        @property
        def quiesceDoneTime(self) -> long: ...
        @quiesceDoneTime.setter
        def quiesceDoneTime(self, value: long):
            self._quiesceDoneTime = value
        @property
        def resumeDoneTime(self) -> long: ...
        @resumeDoneTime.setter
        def resumeDoneTime(self, value: long):
            self._resumeDoneTime = value
        @property
        def endTime(self) -> long: ...
        @endTime.setter
        def endTime(self, value: long):
            self._endTime = value


class VfatVolume(FileSystemVolume): ...


class VffsVolume(FileSystemVolume):
    @property
    def majorVersion(self) -> int: ...
    @majorVersion.setter
    def majorVersion(self, value: int):
        self._majorVersion = value
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def extent(self) -> List[ScsiDisk.Partition]: ...
    @extent.setter
    def extent(self, value: List[ScsiDisk.Partition]):
        self._extent = value


    class Specification(vmodl.DynamicData):
        @property
        def devicePath(self) -> str: ...
        @devicePath.setter
        def devicePath(self, value: str):
            self._devicePath = value
        @property
        def partition(self) -> DiskPartitionInfo.Specification: ...
        @partition.setter
        def partition(self, value: DiskPartitionInfo.Specification):
            self._partition = value
        @property
        def majorVersion(self) -> int: ...
        @majorVersion.setter
        def majorVersion(self, value: int):
            self._majorVersion = value
        @property
        def volumeName(self) -> str: ...
        @volumeName.setter
        def volumeName(self, value: str):
            self._volumeName = value


class VirtualNic(vmodl.DynamicData):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def portgroup(self) -> str: ...
    @portgroup.setter
    def portgroup(self, value: str):
        self._portgroup = value
    @property
    def spec(self) -> VirtualNic.Specification: ...
    @spec.setter
    def spec(self, value: VirtualNic.Specification):
        self._spec = value
    @property
    def port(self) -> Link: ...
    @port.setter
    def port(self, value: Link):
        self._port = value


    class Config(vmodl.DynamicData):
        @property
        def changeOperation(self) -> str: ...
        @changeOperation.setter
        def changeOperation(self, value: str):
            self._changeOperation = value
        @property
        def device(self) -> str: ...
        @device.setter
        def device(self, value: str):
            self._device = value
        @property
        def portgroup(self) -> str: ...
        @portgroup.setter
        def portgroup(self, value: str):
            self._portgroup = value
        @property
        def spec(self) -> VirtualNic.Specification: ...
        @spec.setter
        def spec(self, value: VirtualNic.Specification):
            self._spec = value


    class IpRouteSpec(vmodl.DynamicData):
        @property
        def ipRouteConfig(self) -> IpRouteConfig: ...
        @ipRouteConfig.setter
        def ipRouteConfig(self, value: IpRouteConfig):
            self._ipRouteConfig = value


    class OpaqueNetworkSpec(vmodl.DynamicData):
        @property
        def opaqueNetworkId(self) -> str: ...
        @opaqueNetworkId.setter
        def opaqueNetworkId(self, value: str):
            self._opaqueNetworkId = value
        @property
        def opaqueNetworkType(self) -> str: ...
        @opaqueNetworkType.setter
        def opaqueNetworkType(self, value: str):
            self._opaqueNetworkType = value


    class Specification(vmodl.DynamicData):
        @property
        def ip(self) -> IpConfig: ...
        @ip.setter
        def ip(self, value: IpConfig):
            self._ip = value
        @property
        def mac(self) -> str: ...
        @mac.setter
        def mac(self, value: str):
            self._mac = value
        @property
        def distributedVirtualPort(self) -> vim.dvs.PortConnection: ...
        @distributedVirtualPort.setter
        def distributedVirtualPort(self, value: vim.dvs.PortConnection):
            self._distributedVirtualPort = value
        @property
        def portgroup(self) -> str: ...
        @portgroup.setter
        def portgroup(self, value: str):
            self._portgroup = value
        @property
        def mtu(self) -> int: ...
        @mtu.setter
        def mtu(self, value: int):
            self._mtu = value
        @property
        def tsoEnabled(self) -> bool: ...
        @tsoEnabled.setter
        def tsoEnabled(self, value: bool):
            self._tsoEnabled = value
        @property
        def netStackInstanceKey(self) -> str: ...
        @netStackInstanceKey.setter
        def netStackInstanceKey(self, value: str):
            self._netStackInstanceKey = value
        @property
        def opaqueNetwork(self) -> VirtualNic.OpaqueNetworkSpec: ...
        @opaqueNetwork.setter
        def opaqueNetwork(self, value: VirtualNic.OpaqueNetworkSpec):
            self._opaqueNetwork = value
        @property
        def externalId(self) -> str: ...
        @externalId.setter
        def externalId(self, value: str):
            self._externalId = value
        @property
        def pinnedPnic(self) -> str: ...
        @pinnedPnic.setter
        def pinnedPnic(self, value: str):
            self._pinnedPnic = value
        @property
        def ipRouteSpec(self) -> VirtualNic.IpRouteSpec: ...
        @ipRouteSpec.setter
        def ipRouteSpec(self, value: VirtualNic.IpRouteSpec):
            self._ipRouteSpec = value
        @property
        def systemOwned(self) -> bool: ...
        @systemOwned.setter
        def systemOwned(self, value: bool):
            self._systemOwned = value
        @property
        def dpuId(self) -> str: ...
        @dpuId.setter
        def dpuId(self, value: str):
            self._dpuId = value


class VirtualNicConnection(vmodl.DynamicData):
    @property
    def portgroup(self) -> str: ...
    @portgroup.setter
    def portgroup(self, value: str):
        self._portgroup = value
    @property
    def dvPort(self) -> vim.dvs.PortConnection: ...
    @dvPort.setter
    def dvPort(self, value: vim.dvs.PortConnection):
        self._dvPort = value
    @property
    def opNetwork(self) -> VirtualNic.OpaqueNetworkSpec: ...
    @opNetwork.setter
    def opNetwork(self, value: VirtualNic.OpaqueNetworkSpec):
        self._opNetwork = value


class VirtualNicManagerInfo(vmodl.DynamicData):
    @property
    def netConfig(self) -> List[VirtualNicManager.NetConfig]: ...
    @netConfig.setter
    def netConfig(self, value: List[VirtualNicManager.NetConfig]):
        self._netConfig = value


class VirtualSwitch(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def numPorts(self) -> int: ...
    @numPorts.setter
    def numPorts(self, value: int):
        self._numPorts = value
    @property
    def numPortsAvailable(self) -> int: ...
    @numPortsAvailable.setter
    def numPortsAvailable(self, value: int):
        self._numPortsAvailable = value
    @property
    def mtu(self) -> int: ...
    @mtu.setter
    def mtu(self, value: int):
        self._mtu = value
    @property
    def portgroup(self) -> List[Link]: ...
    @portgroup.setter
    def portgroup(self, value: List[Link]):
        self._portgroup = value
    @property
    def pnic(self) -> List[Link]: ...
    @pnic.setter
    def pnic(self, value: List[Link]):
        self._pnic = value
    @property
    def spec(self) -> VirtualSwitch.Specification: ...
    @spec.setter
    def spec(self, value: VirtualSwitch.Specification):
        self._spec = value


    class AutoBridge(VirtualSwitch.Bridge):
        @property
        def excludedNicDevice(self) -> List[str]: ...
        @excludedNicDevice.setter
        def excludedNicDevice(self, value: List[str]):
            self._excludedNicDevice = value


    class BeaconConfig(vmodl.DynamicData):
        @property
        def interval(self) -> int: ...
        @interval.setter
        def interval(self, value: int):
            self._interval = value


    class BondBridge(VirtualSwitch.Bridge):
        @property
        def nicDevice(self) -> List[str]: ...
        @nicDevice.setter
        def nicDevice(self, value: List[str]):
            self._nicDevice = value
        @property
        def beacon(self) -> VirtualSwitch.BeaconConfig: ...
        @beacon.setter
        def beacon(self, value: VirtualSwitch.BeaconConfig):
            self._beacon = value
        @property
        def linkDiscoveryProtocolConfig(self) -> LinkDiscoveryProtocolConfig: ...
        @linkDiscoveryProtocolConfig.setter
        def linkDiscoveryProtocolConfig(self, value: LinkDiscoveryProtocolConfig):
            self._linkDiscoveryProtocolConfig = value


    class Bridge(vmodl.DynamicData): ...


    class Config(vmodl.DynamicData):
        @property
        def changeOperation(self) -> str: ...
        @changeOperation.setter
        def changeOperation(self, value: str):
            self._changeOperation = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def spec(self) -> VirtualSwitch.Specification: ...
        @spec.setter
        def spec(self, value: VirtualSwitch.Specification):
            self._spec = value


    class SimpleBridge(VirtualSwitch.Bridge):
        @property
        def nicDevice(self) -> str: ...
        @nicDevice.setter
        def nicDevice(self, value: str):
            self._nicDevice = value


    class Specification(vmodl.DynamicData):
        @property
        def numPorts(self) -> int: ...
        @numPorts.setter
        def numPorts(self, value: int):
            self._numPorts = value
        @property
        def bridge(self) -> VirtualSwitch.Bridge: ...
        @bridge.setter
        def bridge(self, value: VirtualSwitch.Bridge):
            self._bridge = value
        @property
        def policy(self) -> NetworkPolicy: ...
        @policy.setter
        def policy(self, value: NetworkPolicy):
            self._policy = value
        @property
        def mtu(self) -> int: ...
        @mtu.setter
        def mtu(self, value: int):
            self._mtu = value


class VmciAccessManager():


    class AccessSpec(vmodl.DynamicData):
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @vm.setter
        def vm(self, value: vim.VirtualMachine):
            self._vm = value
        @property
        def services(self) -> List[str]: ...
        @services.setter
        def services(self, value: List[str]):
            self._services = value
        @property
        def mode(self) -> str: ...
        @mode.setter
        def mode(self, value: str):
            self._mode = value


class VmfsDatastoreCreateSpec(VmfsDatastoreSpec):
    @property
    def partition(self) -> DiskPartitionInfo.Specification: ...
    @partition.setter
    def partition(self, value: DiskPartitionInfo.Specification):
        self._partition = value
    @property
    def vmfs(self) -> VmfsVolume.Specification: ...
    @vmfs.setter
    def vmfs(self, value: VmfsVolume.Specification):
        self._vmfs = value
    @property
    def extent(self) -> List[ScsiDisk.Partition]: ...
    @extent.setter
    def extent(self, value: List[ScsiDisk.Partition]):
        self._extent = value


class VmfsDatastoreExpandSpec(VmfsDatastoreSpec):
    @property
    def partition(self) -> DiskPartitionInfo.Specification: ...
    @partition.setter
    def partition(self, value: DiskPartitionInfo.Specification):
        self._partition = value
    @property
    def extent(self) -> ScsiDisk.Partition: ...
    @extent.setter
    def extent(self, value: ScsiDisk.Partition):
        self._extent = value


class VmfsDatastoreExtendSpec(VmfsDatastoreSpec):
    @property
    def partition(self) -> DiskPartitionInfo.Specification: ...
    @partition.setter
    def partition(self, value: DiskPartitionInfo.Specification):
        self._partition = value
    @property
    def extent(self) -> List[ScsiDisk.Partition]: ...
    @extent.setter
    def extent(self, value: List[ScsiDisk.Partition]):
        self._extent = value


class VmfsDatastoreInfo(vim.Datastore.Info):
    @property
    def maxPhysicalRDMFileSize(self) -> long: ...
    @maxPhysicalRDMFileSize.setter
    def maxPhysicalRDMFileSize(self, value: long):
        self._maxPhysicalRDMFileSize = value
    @property
    def maxVirtualRDMFileSize(self) -> long: ...
    @maxVirtualRDMFileSize.setter
    def maxVirtualRDMFileSize(self, value: long):
        self._maxVirtualRDMFileSize = value
    @property
    def vmfs(self) -> VmfsVolume: ...
    @vmfs.setter
    def vmfs(self, value: VmfsVolume):
        self._vmfs = value


class VmfsDatastoreOption(vmodl.DynamicData):
    @property
    def info(self) -> VmfsDatastoreOption.Info: ...
    @info.setter
    def info(self, value: VmfsDatastoreOption.Info):
        self._info = value
    @property
    def spec(self) -> VmfsDatastoreSpec: ...
    @spec.setter
    def spec(self, value: VmfsDatastoreSpec):
        self._spec = value


    class AllExtentInfo(VmfsDatastoreOption.SingleExtentInfo): ...


    class Info(vmodl.DynamicData):
        @property
        def layout(self) -> DiskPartitionInfo.Layout: ...
        @layout.setter
        def layout(self, value: DiskPartitionInfo.Layout):
            self._layout = value
        @property
        def partitionFormatChange(self) -> bool: ...
        @partitionFormatChange.setter
        def partitionFormatChange(self, value: bool):
            self._partitionFormatChange = value


    class MultipleExtentInfo(VmfsDatastoreOption.Info):
        @property
        def vmfsExtent(self) -> List[DiskPartitionInfo.BlockRange]: ...
        @vmfsExtent.setter
        def vmfsExtent(self, value: List[DiskPartitionInfo.BlockRange]):
            self._vmfsExtent = value


    class SingleExtentInfo(VmfsDatastoreOption.Info):
        @property
        def vmfsExtent(self) -> DiskPartitionInfo.BlockRange: ...
        @vmfsExtent.setter
        def vmfsExtent(self, value: DiskPartitionInfo.BlockRange):
            self._vmfsExtent = value


class VmfsDatastoreSpec(vmodl.DynamicData):
    @property
    def diskUuid(self) -> str: ...
    @diskUuid.setter
    def diskUuid(self, value: str):
        self._diskUuid = value


class VmfsRescanResult(vmodl.DynamicData):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class VmfsVolume(FileSystemVolume):
    @property
    def blockSizeMb(self) -> int: ...
    @blockSizeMb.setter
    def blockSizeMb(self, value: int):
        self._blockSizeMb = value
    @property
    def blockSize(self) -> int: ...
    @blockSize.setter
    def blockSize(self, value: int):
        self._blockSize = value
    @property
    def unmapGranularity(self) -> int: ...
    @unmapGranularity.setter
    def unmapGranularity(self, value: int):
        self._unmapGranularity = value
    @property
    def unmapPriority(self) -> str: ...
    @unmapPriority.setter
    def unmapPriority(self, value: str):
        self._unmapPriority = value
    @property
    def unmapBandwidthSpec(self) -> VmfsVolume.UnmapBandwidthSpec: ...
    @unmapBandwidthSpec.setter
    def unmapBandwidthSpec(self, value: VmfsVolume.UnmapBandwidthSpec):
        self._unmapBandwidthSpec = value
    @property
    def maxBlocks(self) -> int: ...
    @maxBlocks.setter
    def maxBlocks(self, value: int):
        self._maxBlocks = value
    @property
    def majorVersion(self) -> int: ...
    @majorVersion.setter
    def majorVersion(self, value: int):
        self._majorVersion = value
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def extent(self) -> List[ScsiDisk.Partition]: ...
    @extent.setter
    def extent(self, value: List[ScsiDisk.Partition]):
        self._extent = value
    @property
    def vmfsUpgradable(self) -> bool: ...
    @vmfsUpgradable.setter
    def vmfsUpgradable(self, value: bool):
        self._vmfsUpgradable = value
    @property
    def forceMountedInfo(self) -> ForceMountedInfo: ...
    @forceMountedInfo.setter
    def forceMountedInfo(self, value: ForceMountedInfo):
        self._forceMountedInfo = value
    @property
    def ssd(self) -> bool: ...
    @ssd.setter
    def ssd(self, value: bool):
        self._ssd = value
    @property
    def local(self) -> bool: ...
    @local.setter
    def local(self, value: bool):
        self._local = value
    @property
    def scsiDiskType(self) -> str: ...
    @scsiDiskType.setter
    def scsiDiskType(self, value: str):
        self._scsiDiskType = value


    class ConfigOption(vmodl.DynamicData):
        @property
        def blockSizeOption(self) -> int: ...
        @blockSizeOption.setter
        def blockSizeOption(self, value: int):
            self._blockSizeOption = value
        @property
        def unmapGranularityOption(self) -> List[int]: ...
        @unmapGranularityOption.setter
        def unmapGranularityOption(self, value: List[int]):
            self._unmapGranularityOption = value
        @property
        def unmapBandwidthFixedValue(self) -> vim.option.LongOption: ...
        @unmapBandwidthFixedValue.setter
        def unmapBandwidthFixedValue(self, value: vim.option.LongOption):
            self._unmapBandwidthFixedValue = value
        @property
        def unmapBandwidthDynamicMin(self) -> vim.option.LongOption: ...
        @unmapBandwidthDynamicMin.setter
        def unmapBandwidthDynamicMin(self, value: vim.option.LongOption):
            self._unmapBandwidthDynamicMin = value
        @property
        def unmapBandwidthDynamicMax(self) -> vim.option.LongOption: ...
        @unmapBandwidthDynamicMax.setter
        def unmapBandwidthDynamicMax(self, value: vim.option.LongOption):
            self._unmapBandwidthDynamicMax = value
        @property
        def unmapBandwidthIncrement(self) -> long: ...
        @unmapBandwidthIncrement.setter
        def unmapBandwidthIncrement(self, value: long):
            self._unmapBandwidthIncrement = value
        @property
        def unmapBandwidthUltraLow(self) -> long: ...
        @unmapBandwidthUltraLow.setter
        def unmapBandwidthUltraLow(self, value: long):
            self._unmapBandwidthUltraLow = value


    class Specification(vmodl.DynamicData):
        @property
        def extent(self) -> ScsiDisk.Partition: ...
        @extent.setter
        def extent(self, value: ScsiDisk.Partition):
            self._extent = value
        @property
        def blockSizeMb(self) -> int: ...
        @blockSizeMb.setter
        def blockSizeMb(self, value: int):
            self._blockSizeMb = value
        @property
        def majorVersion(self) -> int: ...
        @majorVersion.setter
        def majorVersion(self, value: int):
            self._majorVersion = value
        @property
        def volumeName(self) -> str: ...
        @volumeName.setter
        def volumeName(self, value: str):
            self._volumeName = value
        @property
        def blockSize(self) -> int: ...
        @blockSize.setter
        def blockSize(self, value: int):
            self._blockSize = value
        @property
        def unmapGranularity(self) -> int: ...
        @unmapGranularity.setter
        def unmapGranularity(self, value: int):
            self._unmapGranularity = value
        @property
        def unmapPriority(self) -> str: ...
        @unmapPriority.setter
        def unmapPriority(self, value: str):
            self._unmapPriority = value
        @property
        def unmapBandwidthSpec(self) -> VmfsVolume.UnmapBandwidthSpec: ...
        @unmapBandwidthSpec.setter
        def unmapBandwidthSpec(self, value: VmfsVolume.UnmapBandwidthSpec):
            self._unmapBandwidthSpec = value


    class UnmapBandwidthSpec(vmodl.DynamicData):
        @property
        def policy(self) -> str: ...
        @policy.setter
        def policy(self, value: str):
            self._policy = value
        @property
        def fixedValue(self) -> long: ...
        @fixedValue.setter
        def fixedValue(self, value: long):
            self._fixedValue = value
        @property
        def dynamicMin(self) -> long: ...
        @dynamicMin.setter
        def dynamicMin(self, value: long):
            self._dynamicMin = value
        @property
        def dynamicMax(self) -> long: ...
        @dynamicMax.setter
        def dynamicMax(self, value: long):
            self._dynamicMax = value


    class UnmapBandwidthPolicy(Enum):
        fixed = "fixed"
        dynamic = "dynamic"


    class UnmapPriority(Enum):
        none = "none"
        low = "low"


class VsanDatastoreInfo(vim.Datastore.Info):
    @property
    def membershipUuid(self) -> str: ...
    @membershipUuid.setter
    def membershipUuid(self, value: str):
        self._membershipUuid = value
    @property
    def accessGenNo(self) -> int: ...
    @accessGenNo.setter
    def accessGenNo(self, value: int):
        self._accessGenNo = value


class VvolDatastoreInfo(vim.Datastore.Info):
    @property
    def vvolDS(self) -> VvolVolume: ...
    @vvolDS.setter
    def vvolDS(self, value: VvolVolume):
        self._vvolDS = value


class VvolVolume(FileSystemVolume):
    @property
    def scId(self) -> str: ...
    @scId.setter
    def scId(self, value: str):
        self._scId = value
    @property
    def hostPE(self) -> List[VvolVolume.HostProtocolEndpoint]: ...
    @hostPE.setter
    def hostPE(self, value: List[VvolVolume.HostProtocolEndpoint]):
        self._hostPE = value
    @property
    def vasaProviderInfo(self) -> List[vim.VimVasaProviderInfo]: ...
    @vasaProviderInfo.setter
    def vasaProviderInfo(self, value: List[vim.VimVasaProviderInfo]):
        self._vasaProviderInfo = value
    @property
    def storageArray(self) -> List[vim.VasaStorageArray]: ...
    @storageArray.setter
    def storageArray(self, value: List[vim.VasaStorageArray]):
        self._storageArray = value
    @property
    def protocolEndpointType(self) -> str: ...
    @protocolEndpointType.setter
    def protocolEndpointType(self, value: str):
        self._protocolEndpointType = value


    class HostProtocolEndpoint(vmodl.DynamicData):
        @property
        def key(self) -> vim.HostSystem: ...
        @key.setter
        def key(self, value: vim.HostSystem):
            self._key = value
        @property
        def protocolEndpoint(self) -> List[ProtocolEndpoint]: ...
        @protocolEndpoint.setter
        def protocolEndpoint(self, value: List[ProtocolEndpoint]):
            self._protocolEndpoint = value


    class Specification(vmodl.DynamicData):
        @property
        def maxSizeInMB(self) -> long: ...
        @maxSizeInMB.setter
        def maxSizeInMB(self, value: long):
            self._maxSizeInMB = value
        @property
        def volumeName(self) -> str: ...
        @volumeName.setter
        def volumeName(self, value: str):
            self._volumeName = value
        @property
        def vasaProviderInfo(self) -> List[vim.VimVasaProviderInfo]: ...
        @vasaProviderInfo.setter
        def vasaProviderInfo(self, value: List[vim.VimVasaProviderInfo]):
            self._vasaProviderInfo = value
        @property
        def storageArray(self) -> List[vim.VasaStorageArray]: ...
        @storageArray.setter
        def storageArray(self, value: List[vim.VasaStorageArray]):
            self._storageArray = value
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value