# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.cluster
import pyVmomi.vim.dvs
import pyVmomi.vim.encryption
import pyVmomi.vim.option
import pyVmomi.vim.vm
import pyVmomi.vim.vsan
import pyVmomi.vim.vm.device
import pyVmomi.vim.vsan.host



class ActiveDirectoryAuthentication(DirectoryStore):
   class CertificateDigest(pyVmomi.VmomiSupport.Enum):
      SHA1: _typing.ClassVar['CertificateDigest'] = 'SHA1'

   def JoinDomain(self, domainName: str, userName: str, password: str) -> pyVmomi.vim.Task: ...
   def JoinDomainWithCAM(self, domainName: str, camServer: str) -> pyVmomi.vim.Task: ...
   def ImportCertificateForCAM(self, certPath: str, camServer: str) -> pyVmomi.vim.Task: ...
   def LeaveCurrentDomain(self, force: bool) -> pyVmomi.vim.Task: ...
   def EnableSmartCardAuthentication(self) -> None: ...
   def InstallSmartCardTrustAnchor(self, cert: str) -> None: ...
   def ReplaceSmartCardTrustAnchors(self, certs: list[str]) -> None: ...
   def RemoveSmartCardTrustAnchor(self, issuer: str, serial: str) -> None: ...
   def RemoveSmartCardTrustAnchorByFingerprint(self, fingerprint: str, digest: str) -> None: ...
   def RemoveSmartCardTrustAnchorCertificate(self, certificate: str) -> None: ...
   def ListSmartCardTrustAnchors(self) -> list[str]: ...
   def DisableSmartCardAuthentication(self) -> None: ...


class ActiveDirectoryInfo(DirectoryStoreInfo):
   class DomainMembershipStatus(pyVmomi.VmomiSupport.Enum):
      unknown: _typing.ClassVar['DomainMembershipStatus'] = 'unknown'
      ok: _typing.ClassVar['DomainMembershipStatus'] = 'ok'
      noServers: _typing.ClassVar['DomainMembershipStatus'] = 'noServers'
      clientTrustBroken: _typing.ClassVar['DomainMembershipStatus'] = 'clientTrustBroken'
      serverTrustBroken: _typing.ClassVar['DomainMembershipStatus'] = 'serverTrustBroken'
      inconsistentTrust: _typing.ClassVar['DomainMembershipStatus'] = 'inconsistentTrust'
      otherProblem: _typing.ClassVar['DomainMembershipStatus'] = 'otherProblem'

   joinedDomain: _typing.Optional[str] = None
   trustedDomain: list[str] = []
   domainMembershipStatus: _typing.Optional[str] = None
   smartCardAuthenticationEnabled: _typing.Optional[bool] = None


class ActiveDirectorySpec(pyVmomi.vmodl.DynamicData):
   class Specification(pyVmomi.vmodl.DynamicData):
      domainName: _typing.Optional[str] = None
      userName: _typing.Optional[str] = None
      password: _typing.Optional[str] = None
      camServer: _typing.Optional[str] = None
      thumbprint: _typing.Optional[str] = None
      certificate: _typing.Optional[str] = None
      smartCardAuthenticationEnabled: _typing.Optional[bool] = None
      smartCardTrustAnchors: list[str] = []

   changeOperation: str
   spec: _typing.Optional[Specification] = None


class AssignableHardwareBinding(pyVmomi.vmodl.DynamicData):
   instanceId: str
   vm: pyVmomi.vim.VirtualMachine
   pciId: _typing.Optional[str] = None
   deviceKey: _typing.Optional[int] = None


class AssignableHardwareConfig(pyVmomi.vmodl.DynamicData):
   class AttributeOverride(pyVmomi.vmodl.DynamicData):
      instanceId: str
      name: str
      value: _typing.Optional[object] = None

   attributeOverride: list[AttributeOverride] = []


class AssignableHardwareManager(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def binding(self) -> list[AssignableHardwareBinding]: ...
   @property
   def config(self) -> AssignableHardwareConfig: ...

   def DownloadDescriptionTree(self) -> pyVmomi.VmomiSupport.binary: ...
   def RetrieveDynamicPassthroughInfo(self) -> list[pyVmomi.vim.vm.DynamicPassthroughInfo]: ...
   def RetrieveVendorDeviceGroupInfo(self) -> list[pyVmomi.vim.vm.VendorDeviceGroupInfo]: ...
   def UpdateConfig(self, config: AssignableHardwareConfig) -> None: ...


class AuthenticationInfo(pyVmomi.vmodl.DynamicData):
   principal: str
   ownerTag: str
   sslCertificates: list[str] = []


class AuthenticationManager(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def info(self) -> AuthenticationManagerInfo: ...
   @property
   def supportedStore(self) -> list[AuthenticationStore]: ...


class AuthenticationManagerInfo(pyVmomi.vmodl.DynamicData):
   authConfig: list[AuthenticationStoreInfo] = []


class AuthenticationStore(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def info(self) -> AuthenticationStoreInfo: ...


class AuthenticationStoreInfo(pyVmomi.vmodl.DynamicData):
   enabled: bool


class AutoStartManager(pyVmomi.VmomiSupport.ManagedObject):
   class Action(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['Action'] = 'none'
      systemDefault: _typing.ClassVar['Action'] = 'systemDefault'
      powerOn: _typing.ClassVar['Action'] = 'powerOn'
      powerOff: _typing.ClassVar['Action'] = 'powerOff'
      guestShutdown: _typing.ClassVar['Action'] = 'guestShutdown'
      suspend: _typing.ClassVar['Action'] = 'suspend'

   class SystemDefaults(pyVmomi.vmodl.DynamicData):
      enabled: _typing.Optional[bool] = None
      startDelay: _typing.Optional[int] = None
      stopDelay: _typing.Optional[int] = None
      waitForHeartbeat: _typing.Optional[bool] = None
      stopAction: _typing.Optional[str] = None

   class AutoPowerInfo(pyVmomi.vmodl.DynamicData):
      class WaitHeartbeatSetting(pyVmomi.VmomiSupport.Enum):
         yes: _typing.ClassVar['WaitHeartbeatSetting'] = 'yes'
         no: _typing.ClassVar['WaitHeartbeatSetting'] = 'no'
         systemDefault: _typing.ClassVar['WaitHeartbeatSetting'] = 'systemDefault'

      key: pyVmomi.vim.VirtualMachine
      startOrder: int
      startDelay: int
      waitForHeartbeat: WaitHeartbeatSetting
      startAction: str
      stopDelay: int
      stopAction: str

   class Config(pyVmomi.vmodl.DynamicData):
      defaults: _typing.Optional[SystemDefaults] = None
      powerInfo: list[AutoPowerInfo] = []

   @property
   def config(self) -> Config: ...

   def Reconfigure(self, spec: Config) -> None: ...
   def AutoPowerOn(self) -> None: ...
   def AutoPowerOff(self) -> None: ...


class BIOSInfo(pyVmomi.vmodl.DynamicData):
   class FirmwareType(pyVmomi.VmomiSupport.Enum):
      BIOS: _typing.ClassVar['FirmwareType'] = 'BIOS'
      UEFI: _typing.ClassVar['FirmwareType'] = 'UEFI'

   biosVersion: _typing.Optional[str] = None
   releaseDate: _typing.Optional[_datetime.datetime] = None
   vendor: _typing.Optional[str] = None
   majorRelease: _typing.Optional[int] = None
   minorRelease: _typing.Optional[int] = None
   firmwareMajorRelease: _typing.Optional[int] = None
   firmwareMinorRelease: _typing.Optional[int] = None
   firmwareType: _typing.Optional[str] = None

class BlockAdapterTargetTransport(TargetTransport):
   pass

class BlockHba(HostBusAdapter):
   pass


class BootDeviceInfo(pyVmomi.vmodl.DynamicData):
   bootDevices: list[BootDeviceSystem.BootDevice] = []
   currentBootDeviceKey: _typing.Optional[str] = None


class BootDeviceSystem(pyVmomi.VmomiSupport.ManagedObject):
   class BootDevice(pyVmomi.vmodl.DynamicData):
      key: str
      description: str

   def QueryBootDevices(self) -> _typing.Optional[BootDeviceInfo]: ...
   def UpdateBootDevice(self, key: str) -> None: ...


class CacheConfigurationManager(pyVmomi.VmomiSupport.ManagedObject):
   class CacheConfigurationSpec(pyVmomi.vmodl.DynamicData):
      datastore: pyVmomi.vim.Datastore
      swapSize: pyVmomi.VmomiSupport.long

   class CacheConfigurationInfo(pyVmomi.vmodl.DynamicData):
      key: pyVmomi.vim.Datastore
      swapSize: pyVmomi.VmomiSupport.long

   @property
   def cacheConfigurationInfo(self) -> list[CacheConfigurationInfo]: ...

   def ConfigureCache(self, spec: CacheConfigurationSpec) -> pyVmomi.vim.Task: ...


class Capability(pyVmomi.vmodl.DynamicData):
   class ReplayUnsupportedReason(pyVmomi.VmomiSupport.Enum):
      incompatibleProduct: _typing.ClassVar['ReplayUnsupportedReason'] = 'incompatibleProduct'
      incompatibleCpu: _typing.ClassVar['ReplayUnsupportedReason'] = 'incompatibleCpu'
      hvDisabled: _typing.ClassVar['ReplayUnsupportedReason'] = 'hvDisabled'
      cpuidLimitSet: _typing.ClassVar['ReplayUnsupportedReason'] = 'cpuidLimitSet'
      oldBIOS: _typing.ClassVar['ReplayUnsupportedReason'] = 'oldBIOS'
      unknown: _typing.ClassVar['ReplayUnsupportedReason'] = 'unknown'

   class FtUnsupportedReason(pyVmomi.VmomiSupport.Enum):
      vMotionNotLicensed: _typing.ClassVar['FtUnsupportedReason'] = 'vMotionNotLicensed'
      missingVMotionNic: _typing.ClassVar['FtUnsupportedReason'] = 'missingVMotionNic'
      missingFTLoggingNic: _typing.ClassVar['FtUnsupportedReason'] = 'missingFTLoggingNic'
      ftNotLicensed: _typing.ClassVar['FtUnsupportedReason'] = 'ftNotLicensed'
      haAgentIssue: _typing.ClassVar['FtUnsupportedReason'] = 'haAgentIssue'
      unsupportedProduct: _typing.ClassVar['FtUnsupportedReason'] = 'unsupportedProduct'
      cpuHvUnsupported: _typing.ClassVar['FtUnsupportedReason'] = 'cpuHvUnsupported'
      cpuHwmmuUnsupported: _typing.ClassVar['FtUnsupportedReason'] = 'cpuHwmmuUnsupported'
      cpuHvDisabled: _typing.ClassVar['FtUnsupportedReason'] = 'cpuHvDisabled'

   class DRTMTypes(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['DRTMTypes'] = 'none'
      intelTxt: _typing.ClassVar['DRTMTypes'] = 'intelTxt'
      amdSkinit: _typing.ClassVar['DRTMTypes'] = 'amdSkinit'

   class VmDirectPathGen2UnsupportedReason(pyVmomi.VmomiSupport.Enum):
      hostNptIncompatibleProduct: _typing.ClassVar['VmDirectPathGen2UnsupportedReason'] = 'hostNptIncompatibleProduct'
      hostNptIncompatibleHardware: _typing.ClassVar['VmDirectPathGen2UnsupportedReason'] = 'hostNptIncompatibleHardware'
      hostNptDisabled: _typing.ClassVar['VmDirectPathGen2UnsupportedReason'] = 'hostNptDisabled'

   class UnmapMethodSupported(pyVmomi.VmomiSupport.Enum):
      priority: _typing.ClassVar['UnmapMethodSupported'] = 'priority'
      fixed: _typing.ClassVar['UnmapMethodSupported'] = 'fixed'
      dynamic: _typing.ClassVar['UnmapMethodSupported'] = 'dynamic'

   recursiveResourcePoolsSupported: bool
   cpuMemoryResourceConfigurationSupported: bool
   rebootSupported: bool
   shutdownSupported: bool
   vmotionSupported: bool
   standbySupported: bool
   ipmiSupported: _typing.Optional[bool] = None
   maxSupportedVMs: _typing.Optional[int] = None
   maxRunningVMs: _typing.Optional[int] = None
   maxSupportedVcpus: _typing.Optional[int] = None
   maxRegisteredVMs: _typing.Optional[int] = None
   datastorePrincipalSupported: bool
   sanSupported: bool
   nfsSupported: bool
   iscsiSupported: bool
   vlanTaggingSupported: bool
   nicTeamingSupported: bool
   highGuestMemSupported: bool
   maintenanceModeSupported: bool
   suspendedRelocateSupported: bool
   restrictedSnapshotRelocateSupported: bool
   perVmSwapFiles: bool
   localSwapDatastoreSupported: bool
   unsharedSwapVMotionSupported: bool
   backgroundSnapshotsSupported: bool
   preAssignedPCIUnitNumbersSupported: bool
   screenshotSupported: bool
   scaledScreenshotSupported: bool
   storageVMotionSupported: bool
   vmotionWithStorageVMotionSupported: bool
   vmotionAcrossNetworkSupported: _typing.Optional[bool] = None
   maxNumDisksSVMotion: _typing.Optional[int] = None
   maxVirtualDiskDescVersionSupported: _typing.Optional[int] = None
   hbrNicSelectionSupported: bool
   vrNfcNicSelectionSupported: bool
   recordReplaySupported: bool
   ftSupported: bool
   replayUnsupportedReason: _typing.Optional[str] = None
   replayCompatibilityIssues: list[str] = []
   smpFtSupported: bool
   ftCompatibilityIssues: list[str] = []
   smpFtCompatibilityIssues: list[str] = []
   maxVcpusPerFtVm: _typing.Optional[int] = None
   loginBySSLThumbprintSupported: _typing.Optional[bool] = None
   cloneFromSnapshotSupported: bool
   deltaDiskBackingsSupported: bool
   perVMNetworkTrafficShapingSupported: bool
   tpmSupported: bool
   tpmVersion: _typing.Optional[str] = None
   txtEnabled: _typing.Optional[bool] = None
   drtmType: _typing.Optional[str] = None
   supportedCpuFeature: list[CpuIdInfo] = []
   virtualExecUsageSupported: bool
   storageIORMSupported: bool
   vmDirectPathGen2Supported: _typing.Optional[bool] = None
   vmDirectPathGen2UnsupportedReason: list[str] = []
   vmDirectPathGen2UnsupportedReasonExtended: _typing.Optional[str] = None
   supportedVmfsMajorVersion: list[int] = []
   vStorageCapable: bool
   snapshotRelayoutSupported: bool
   firewallIpRulesSupported: _typing.Optional[bool] = None
   servicePackageInfoSupported: _typing.Optional[bool] = None
   maxHostRunningVms: _typing.Optional[int] = None
   maxHostSupportedVcpus: _typing.Optional[int] = None
   vmfsDatastoreMountCapable: bool
   eightPlusHostVmfsSharedAccessSupported: bool
   nestedHVSupported: bool
   vPMCSupported: bool
   interVMCommunicationThroughVMCISupported: bool
   scheduledHardwareUpgradeSupported: _typing.Optional[bool] = None
   featureCapabilitiesSupported: bool
   latencySensitivitySupported: bool
   storagePolicySupported: _typing.Optional[bool] = None
   accel3dSupported: bool
   reliableMemoryAware: _typing.Optional[bool] = None
   multipleNetworkStackInstanceSupported: _typing.Optional[bool] = None
   messageBusProxySupported: _typing.Optional[bool] = None
   vsanSupported: _typing.Optional[bool] = None
   vFlashSupported: _typing.Optional[bool] = None
   hostAccessManagerSupported: _typing.Optional[bool] = None
   provisioningNicSelectionSupported: bool
   nfs41Supported: _typing.Optional[bool] = None
   nfs41Krb5iSupported: _typing.Optional[bool] = None
   turnDiskLocatorLedSupported: _typing.Optional[bool] = None
   virtualVolumeDatastoreSupported: _typing.Optional[bool] = None
   markAsSsdSupported: _typing.Optional[bool] = None
   markAsLocalSupported: _typing.Optional[bool] = None
   smartCardAuthenticationSupported: _typing.Optional[bool] = None
   pMemSupported: _typing.Optional[bool] = None
   pMemSnapshotSupported: _typing.Optional[bool] = None
   cryptoSupported: _typing.Optional[bool] = None
   oneKVolumeAPIsSupported: _typing.Optional[bool] = None
   gatewayOnNicSupported: _typing.Optional[bool] = None
   upitSupported: _typing.Optional[bool] = None
   cpuHwMmuSupported: _typing.Optional[bool] = None
   encryptedVMotionSupported: _typing.Optional[bool] = None
   encryptionChangeOnAddRemoveSupported: _typing.Optional[bool] = None
   encryptionHotOperationSupported: _typing.Optional[bool] = None
   encryptionWithSnapshotsSupported: _typing.Optional[bool] = None
   encryptionFaultToleranceSupported: _typing.Optional[bool] = None
   encryptionMemorySaveSupported: _typing.Optional[bool] = None
   encryptionRDMSupported: _typing.Optional[bool] = None
   encryptionVFlashSupported: _typing.Optional[bool] = None
   encryptionCBRCSupported: _typing.Optional[bool] = None
   encryptionHBRSupported: _typing.Optional[bool] = None
   ftEfiSupported: _typing.Optional[bool] = None
   unmapMethodSupported: _typing.Optional[str] = None
   maxMemMBPerFtVm: _typing.Optional[int] = None
   virtualMmuUsageIgnored: _typing.Optional[bool] = None
   virtualExecUsageIgnored: _typing.Optional[bool] = None
   vmCreateDateSupported: _typing.Optional[bool] = None
   vmfs3EOLSupported: _typing.Optional[bool] = None
   ftVmcpSupported: _typing.Optional[bool] = None
   quickBootSupported: _typing.Optional[bool] = None
   encryptedFtSupported: _typing.Optional[bool] = None
   assignableHardwareSupported: _typing.Optional[bool] = None
   suspendToMemorySupported: _typing.Optional[bool] = None
   useFeatureReqsForOldHWv: _typing.Optional[bool] = None
   markPerenniallyReservedSupported: _typing.Optional[bool] = None
   hppPspSupported: _typing.Optional[bool] = None
   deviceRebindWithoutRebootSupported: _typing.Optional[bool] = None
   storagePolicyChangeSupported: _typing.Optional[bool] = None
   precisionTimeProtocolSupported: _typing.Optional[bool] = None
   remoteDeviceVMotionSupported: _typing.Optional[bool] = None
   maxSupportedVmMemory: _typing.Optional[int] = None
   ahDeviceHintsSupported: _typing.Optional[bool] = None
   nvmeOverTcpSupported: _typing.Optional[bool] = None
   nvmeStorageFabricServicesSupported: _typing.Optional[bool] = None
   assignHwPciConfigSupported: _typing.Optional[bool] = None
   timeConfigSupported: _typing.Optional[bool] = None
   nvmeBatchOperationsSupported: _typing.Optional[bool] = None
   pMemFailoverSupported: _typing.Optional[bool] = None
   hostConfigEncryptionSupported: _typing.Optional[bool] = None
   maxSupportedSimultaneousThreads: _typing.Optional[int] = None
   ptpConfigSupported: _typing.Optional[bool] = None
   maxSupportedPtpPorts: _typing.Optional[int] = None
   sgxRegistrationSupported: _typing.Optional[bool] = None
   pMemIndependentSnapshotSupported: _typing.Optional[bool] = None
   iommuSLDirtyCapable: _typing.Optional[bool] = None
   vmknicBindingSupported: _typing.Optional[bool] = None
   ultralowFixedUnmapSupported: _typing.Optional[bool] = None
   nvmeVvolSupported: _typing.Optional[bool] = None
   fptHotplugSupported: _typing.Optional[bool] = None
   mconnectSupported: _typing.Optional[bool] = None
   vsanNicMgmtSupported: _typing.Optional[bool] = None
   vvolNQNSupported: _typing.Optional[bool] = None
   stretchedSCSupported: _typing.Optional[bool] = None
   vmknicBindingOnNFSv41: _typing.Optional[bool] = None
   vpStatusCheckSupported: _typing.Optional[bool] = None
   e2e4knSupported: _typing.Optional[bool] = None
   vsanDedicatedVmkNicSupported: _typing.Optional[bool] = None
   nConnectSupported: _typing.Optional[bool] = None
   userKeySupported: _typing.Optional[bool] = None
   ndcmSupported: _typing.Optional[bool] = None
   uefiSecureBoot: _typing.Optional[bool] = None
   vpxdVmxGenerationSupported: _typing.Optional[bool] = None
   nfs41Krb5pSupported: _typing.Optional[bool] = None
   cimSupported: _typing.Optional[bool] = None
   npivSupported: _typing.Optional[bool] = None
   entitlementSupported: _typing.Optional[bool] = None
   monitorUnrestricted: _typing.Optional[bool] = None
   vnetworkingNicSelectionSupported: _typing.Optional[bool] = None
   directPathInfoSupported: _typing.Optional[bool] = None
   fcdLinkedCloneSupported: _typing.Optional[bool] = None
   ehvQuickBootSupported: _typing.Optional[bool] = None
   nestedHvTieringEnabled: _typing.Optional[bool] = None


class CertificateManager(pyVmomi.VmomiSupport.ManagedObject):
   class CertificateKind(pyVmomi.VmomiSupport.Enum):
      Machine: _typing.ClassVar['CertificateKind'] = 'Machine'
      VASAClient: _typing.ClassVar['CertificateKind'] = 'VASAClient'

   class CryptoAlgorithm(pyVmomi.VmomiSupport.Enum):
      RSA_2048: _typing.ClassVar['CryptoAlgorithm'] = 'RSA_2048'
      RSA_3072: _typing.ClassVar['CryptoAlgorithm'] = 'RSA_3072'
      RSA_4096: _typing.ClassVar['CryptoAlgorithm'] = 'RSA_4096'

   class CertificateSpec(pyVmomi.vmodl.DynamicData):
      kind: str
      subjectAlternativeNames: list[str] = []
      cryptoAlgorithm: _typing.Optional[str] = None

   class CertificateInfo(pyVmomi.vmodl.DynamicData):
      class CertificateStatus(pyVmomi.VmomiSupport.Enum):
         unknown: _typing.ClassVar['CertificateStatus'] = 'unknown'
         expired: _typing.ClassVar['CertificateStatus'] = 'expired'
         expiring: _typing.ClassVar['CertificateStatus'] = 'expiring'
         expiringShortly: _typing.ClassVar['CertificateStatus'] = 'expiringShortly'
         expirationImminent: _typing.ClassVar['CertificateStatus'] = 'expirationImminent'
         good: _typing.ClassVar['CertificateStatus'] = 'good'

      kind: _typing.Optional[str] = None
      issuer: _typing.Optional[str] = None
      notBefore: _typing.Optional[_datetime.datetime] = None
      notAfter: _typing.Optional[_datetime.datetime] = None
      subject: _typing.Optional[str] = None
      status: str

   @property
   def certificateInfo(self) -> CertificateInfo: ...

   def RetrieveCertificateInfoList(self) -> list[CertificateInfo]: ...
   def GenerateCertificateSigningRequest(self, useIpAddressAsCommonName: bool, spec: _typing.Optional[CertificateSpec]) -> str: ...
   def GenerateCertificateSigningRequestByDn(self, distinguishedName: str, spec: _typing.Optional[CertificateSpec]) -> str: ...
   def ProvisionServerPrivateKey(self, key: str) -> None: ...
   def InstallServerCertificate(self, cert: str) -> None: ...
   def ReplaceCACertificatesAndCRLs(self, caCert: list[str], caCrl: list[str]) -> None: ...
   def NotifyAffectedServices(self, services: list[str]) -> None: ...
   def ListCACertificates(self) -> list[str]: ...
   def ListCACertificateRevocationLists(self) -> list[str]: ...


class ConfigChange(pyVmomi.vmodl.DynamicData):
   class Mode(pyVmomi.VmomiSupport.Enum):
      modify: _typing.ClassVar['Mode'] = 'modify'
      replace: _typing.ClassVar['Mode'] = 'replace'

   class Operation(pyVmomi.VmomiSupport.Enum):
      add: _typing.ClassVar['Operation'] = 'add'
      remove: _typing.ClassVar['Operation'] = 'remove'
      edit: _typing.ClassVar['Operation'] = 'edit'
      ignore: _typing.ClassVar['Operation'] = 'ignore'

   class Owner(pyVmomi.VmomiSupport.Enum):
      NSX: _typing.ClassVar['Owner'] = 'NSX'
      VSAN: _typing.ClassVar['Owner'] = 'VSAN'


class ConfigInfo(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   product: pyVmomi.vim.AboutInfo
   deploymentInfo: _typing.Optional[DeploymentInfo] = None
   hyperThread: _typing.Optional[CpuSchedulerSystem.HyperThreadScheduleInfo] = None
   cpuScheduler: _typing.Optional[CpuSchedulerSystem.CpuSchedulerInfo] = None
   consoleReservation: _typing.Optional[MemoryManagerSystem.ServiceConsoleReservationInfo] = None
   virtualMachineReservation: _typing.Optional[MemoryManagerSystem.VirtualMachineReservationInfo] = None
   storageDevice: _typing.Optional[StorageDeviceInfo] = None
   multipathState: _typing.Optional[MultipathStateInfo] = None
   fileSystemVolume: _typing.Optional[FileSystemVolumeInfo] = None
   systemFile: list[str] = []
   network: _typing.Optional[NetworkInfo] = None
   vmotion: _typing.Optional[VMotionInfo] = None
   virtualNicManagerInfo: _typing.Optional[VirtualNicManagerInfo] = None
   capabilities: _typing.Optional[NetCapabilities] = None
   datastoreCapabilities: _typing.Optional[DatastoreSystem.Capabilities] = None
   offloadCapabilities: _typing.Optional[NetOffloadCapabilities] = None
   service: _typing.Optional[ServiceInfo] = None
   firewall: _typing.Optional[FirewallInfo] = None
   autoStart: _typing.Optional[AutoStartManager.Config] = None
   activeDiagnosticPartition: _typing.Optional[DiagnosticPartition] = None
   option: list[pyVmomi.vim.option.OptionValue] = []
   optionDef: list[pyVmomi.vim.option.OptionDef] = []
   datastorePrincipal: _typing.Optional[str] = None
   localSwapDatastore: _typing.Optional[pyVmomi.vim.Datastore] = None
   systemSwapConfiguration: _typing.Optional[SystemSwapConfiguration] = None
   systemResources: _typing.Optional[SystemResourceInfo] = None
   dateTimeInfo: _typing.Optional[DateTimeInfo] = None
   flags: _typing.Optional[FlagInfo] = None
   adminDisabled: _typing.Optional[bool] = None
   lockdownMode: _typing.Optional[HostAccessManager.LockdownMode] = None
   ipmi: _typing.Optional[IpmiInfo] = None
   sslThumbprintInfo: _typing.Optional[SslThumbprintInfo] = None
   sslThumbprintData: list[SslThumbprintInfo] = []
   authenticationData: list[AuthenticationInfo] = []
   certificate: list[pyVmomi.VmomiSupport.byte] = []
   pciPassthruInfo: list[PciPassthruInfo] = []
   authenticationManagerInfo: _typing.Optional[AuthenticationManagerInfo] = None
   featureVersion: list[FeatureVersionInfo] = []
   powerSystemCapability: _typing.Optional[PowerSystem.Capability] = None
   powerSystemInfo: _typing.Optional[PowerSystem.Info] = None
   cacheConfigurationInfo: list[CacheConfigurationManager.CacheConfigurationInfo] = []
   wakeOnLanCapable: _typing.Optional[bool] = None
   featureCapability: list[FeatureCapability] = []
   maskedFeatureCapability: list[FeatureCapability] = []
   vFlashConfigInfo: _typing.Optional[VFlashManager.VFlashConfigInfo] = None
   vsanHostConfig: _typing.Optional[pyVmomi.vim.vsan.host.ConfigInfo] = None
   domainList: list[str] = []
   scriptCheckSum: _typing.Optional[pyVmomi.VmomiSupport.binary] = None
   hostConfigCheckSum: _typing.Optional[pyVmomi.VmomiSupport.binary] = None
   descriptionTreeCheckSum: _typing.Optional[pyVmomi.VmomiSupport.binary] = None
   graphicsInfo: list[GraphicsInfo] = []
   sharedPassthruGpuTypes: list[str] = []
   graphicsConfig: _typing.Optional[GraphicsConfig] = None
   sharedGpuCapabilities: list[SharedGpuCapabilities] = []
   ioFilterInfo: list[pyVmomi.vim.IoFilterManager.HostIoFilterInfo] = []
   sriovDevicePool: list[SriovDevicePoolInfo] = []
   assignableHardwareBinding: list[AssignableHardwareBinding] = []
   assignableHardwareConfig: _typing.Optional[AssignableHardwareConfig] = None


class ConfigManager(pyVmomi.vmodl.DynamicData):
   cpuScheduler: _typing.Optional[CpuSchedulerSystem] = None
   datastoreSystem: _typing.Optional[DatastoreSystem] = None
   memoryManager: _typing.Optional[MemoryManagerSystem] = None
   storageSystem: _typing.Optional[StorageSystem] = None
   networkSystem: _typing.Optional[NetworkSystem] = None
   vmotionSystem: _typing.Optional[VMotionSystem] = None
   virtualNicManager: _typing.Optional[VirtualNicManager] = None
   serviceSystem: _typing.Optional[ServiceSystem] = None
   firewallSystem: _typing.Optional[FirewallSystem] = None
   advancedOption: _typing.Optional[pyVmomi.vim.option.OptionManager] = None
   diagnosticSystem: _typing.Optional[DiagnosticSystem] = None
   autoStartManager: _typing.Optional[AutoStartManager] = None
   snmpSystem: _typing.Optional[SnmpSystem] = None
   dateTimeSystem: _typing.Optional[DateTimeSystem] = None
   patchManager: _typing.Optional[PatchManager] = None
   imageConfigManager: _typing.Optional[ImageConfigManager] = None
   bootDeviceSystem: _typing.Optional[BootDeviceSystem] = None
   firmwareSystem: _typing.Optional[FirmwareSystem] = None
   healthStatusSystem: _typing.Optional[HealthStatusSystem] = None
   pciPassthruSystem: _typing.Optional[PciPassthruSystem] = None
   licenseManager: _typing.Optional[pyVmomi.vim.LicenseManager] = None
   kernelModuleSystem: _typing.Optional[KernelModuleSystem] = None
   authenticationManager: _typing.Optional[AuthenticationManager] = None
   powerSystem: _typing.Optional[PowerSystem] = None
   cacheConfigurationManager: _typing.Optional[CacheConfigurationManager] = None
   esxAgentHostManager: _typing.Optional[EsxAgentHostManager] = None
   iscsiManager: _typing.Optional[IscsiManager] = None
   vFlashManager: _typing.Optional[VFlashManager] = None
   vsanSystem: _typing.Optional[VsanSystem] = None
   messageBusProxy: _typing.Optional[MessageBusProxy] = None
   userDirectory: _typing.Optional[pyVmomi.vim.UserDirectory] = None
   accountManager: _typing.Optional[LocalAccountManager] = None
   hostAccessManager: _typing.Optional[HostAccessManager] = None
   graphicsManager: _typing.Optional[GraphicsManager] = None
   vsanInternalSystem: _typing.Optional[VsanInternalSystem] = None
   certificateManager: _typing.Optional[CertificateManager] = None
   cryptoManager: _typing.Optional[pyVmomi.vim.encryption.CryptoManager] = None
   nvdimmSystem: _typing.Optional[NvdimmSystem] = None
   assignableHardwareManager: _typing.Optional[AssignableHardwareManager] = None


class ConfigSpec(pyVmomi.vmodl.DynamicData):
   nasDatastore: list[NasVolume.Config] = []
   network: _typing.Optional[NetworkConfig] = None
   nicTypeSelection: list[VirtualNicManager.NicTypeSelection] = []
   service: list[ServiceConfig] = []
   firewall: _typing.Optional[FirewallConfig] = None
   option: list[pyVmomi.vim.option.OptionValue] = []
   datastorePrincipal: _typing.Optional[str] = None
   datastorePrincipalPasswd: _typing.Optional[str] = None
   datetime: _typing.Optional[DateTimeConfig] = None
   storageDevice: _typing.Optional[StorageDeviceInfo] = None
   license: _typing.Optional[LicenseSpec] = None
   security: _typing.Optional[SecuritySpec] = None
   userAccount: list[LocalAccountManager.AccountSpecification] = []
   usergroupAccount: list[LocalAccountManager.AccountSpecification] = []
   memory: _typing.Optional[MemorySpec] = None
   activeDirectory: list[ActiveDirectorySpec] = []
   genericConfig: list[pyVmomi.vmodl.KeyAnyValue] = []
   graphicsConfig: _typing.Optional[GraphicsConfig] = None
   assignableHardwareConfig: _typing.Optional[AssignableHardwareConfig] = None


class ConnectInfo(pyVmomi.vmodl.DynamicData):
   class NetworkInfo(pyVmomi.vmodl.DynamicData):
      summary: pyVmomi.vim.Network.Summary

   class NewNetworkInfo(NetworkInfo):
      pass

   class DatastoreInfo(pyVmomi.vmodl.DynamicData):
      summary: pyVmomi.vim.Datastore.Summary

   class DatastoreExistsInfo(DatastoreInfo):
      newDatastoreName: str

   class DatastoreNameConflictInfo(DatastoreInfo):
      newDatastoreName: str

   class LicenseInfo(pyVmomi.vmodl.DynamicData):
      license: pyVmomi.vim.LicenseManager.LicenseInfo
      evaluation: pyVmomi.vim.LicenseManager.EvaluationInfo
      resource: _typing.Optional[pyVmomi.vim.LicenseManager.LicensableResourceInfo] = None

   serverIp: _typing.Optional[str] = None
   inDasCluster: _typing.Optional[bool] = None
   host: Summary
   vm: list[pyVmomi.vim.vm.Summary] = []
   vimAccountNameRequired: _typing.Optional[bool] = None
   clusterSupported: _typing.Optional[bool] = None
   network: list[NetworkInfo] = []
   datastore: list[DatastoreInfo] = []
   license: _typing.Optional[LicenseInfo] = None
   capability: _typing.Optional[Capability] = None


class ConnectSpec(pyVmomi.vmodl.DynamicData):
   hostName: _typing.Optional[str] = None
   port: _typing.Optional[int] = None
   sslThumbprint: _typing.Optional[str] = None
   sslCertificate: _typing.Optional[str] = None
   userName: _typing.Optional[str] = None
   password: _typing.Optional[str] = None
   vmFolder: _typing.Optional[pyVmomi.vim.Folder] = None
   force: bool
   vimAccountName: _typing.Optional[str] = None
   vimAccountPassword: _typing.Optional[str] = None
   managementIp: _typing.Optional[str] = None
   lockdownMode: _typing.Optional[HostAccessManager.LockdownMode] = None
   hostGateway: _typing.Optional[GatewaySpec] = None


class CpuIdInfo(pyVmomi.vmodl.DynamicData):
   level: int
   vendor: _typing.Optional[str] = None
   eax: _typing.Optional[str] = None
   ebx: _typing.Optional[str] = None
   ecx: _typing.Optional[str] = None
   edx: _typing.Optional[str] = None


class CpuInfo(pyVmomi.vmodl.DynamicData):
   numCpuPackages: pyVmomi.VmomiSupport.short
   numCpuCores: pyVmomi.VmomiSupport.short
   numCpuThreads: pyVmomi.VmomiSupport.short
   hz: pyVmomi.VmomiSupport.long


class CpuPackage(pyVmomi.vmodl.DynamicData):
   class Vendor(pyVmomi.VmomiSupport.Enum):
      unknown: _typing.ClassVar['Vendor'] = 'unknown'
      intel: _typing.ClassVar['Vendor'] = 'intel'
      amd: _typing.ClassVar['Vendor'] = 'amd'
      hygon: _typing.ClassVar['Vendor'] = 'hygon'
      arm: _typing.ClassVar['Vendor'] = 'arm'

   index: pyVmomi.VmomiSupport.short
   vendor: str
   hz: pyVmomi.VmomiSupport.long
   busHz: pyVmomi.VmomiSupport.long
   description: str
   threadId: list[pyVmomi.VmomiSupport.short] = []
   cpuFeature: list[CpuIdInfo] = []
   family: _typing.Optional[pyVmomi.VmomiSupport.short] = None
   model: _typing.Optional[pyVmomi.VmomiSupport.short] = None
   stepping: _typing.Optional[pyVmomi.VmomiSupport.short] = None


class CpuPowerManagementInfo(pyVmomi.vmodl.DynamicData):
   class PolicyType(pyVmomi.VmomiSupport.Enum):
      off: _typing.ClassVar['PolicyType'] = 'off'
      staticPolicy: _typing.ClassVar['PolicyType'] = 'staticPolicy'
      dynamicPolicy: _typing.ClassVar['PolicyType'] = 'dynamicPolicy'

   currentPolicy: _typing.Optional[str] = None
   hardwareSupport: _typing.Optional[str] = None


class CpuSchedulerSystem(pyVmomi.vim.ExtensibleManagedObject):
   class HyperThreadScheduleInfo(pyVmomi.vmodl.DynamicData):
      available: bool
      active: bool
      config: bool

   class CpuSchedulerInfo(pyVmomi.vmodl.DynamicData):
      class CpuSchedulerPolicyInfo(pyVmomi.VmomiSupport.Enum):
         systemDefault: _typing.ClassVar['CpuSchedulerPolicyInfo'] = 'systemDefault'
         scav1: _typing.ClassVar['CpuSchedulerPolicyInfo'] = 'scav1'
         scav2: _typing.ClassVar['CpuSchedulerPolicyInfo'] = 'scav2'

      policy: str

   @property
   def cpuSchedulerInfo(self) -> _typing.Optional[CpuSchedulerInfo]: ...
   @property
   def hyperthreadInfo(self) -> _typing.Optional[HyperThreadScheduleInfo]: ...

   def EnableHyperThreading(self) -> None: ...
   def DisableHyperThreading(self) -> None: ...


class DataTransportConnectionInfo(pyVmomi.vmodl.DynamicData):
   staticMemoryConsumed: pyVmomi.VmomiSupport.long


class DatastoreBrowser(pyVmomi.VmomiSupport.ManagedObject):
   class FileInfo(pyVmomi.vmodl.DynamicData):
      class Details(pyVmomi.vmodl.DynamicData):
         fileType: bool
         fileSize: bool
         modification: bool
         fileOwner: bool

      path: str
      friendlyName: _typing.Optional[str] = None
      fileSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      modification: _typing.Optional[_datetime.datetime] = None
      owner: _typing.Optional[str] = None

   class Query(pyVmomi.vmodl.DynamicData):
      pass

   class VmConfigQuery(Query):
      class Filter(pyVmomi.vmodl.DynamicData):
         matchConfigVersion: list[int] = []
         encrypted: _typing.Optional[bool] = None

      class Details(pyVmomi.vmodl.DynamicData):
         configVersion: bool
         encryption: _typing.Optional[bool] = None

      filter: _typing.Optional[Filter] = None
      details: _typing.Optional[Details] = None

   class TemplateVmConfigQuery(VmConfigQuery):
      pass

   class VmDiskQuery(Query):
      class Filter(pyVmomi.vmodl.DynamicData):
         diskType: list[type] = []
         matchHardwareVersion: list[int] = []
         controllerType: list[type] = []
         thin: _typing.Optional[bool] = None
         encrypted: _typing.Optional[bool] = None

      class Details(pyVmomi.vmodl.DynamicData):
         diskType: bool
         capacityKb: bool
         hardwareVersion: bool
         controllerType: _typing.Optional[bool] = None
         diskExtents: _typing.Optional[bool] = None
         thin: _typing.Optional[bool] = None
         encryption: _typing.Optional[bool] = None
         sectorFormat: _typing.Optional[bool] = None

      filter: _typing.Optional[Filter] = None
      details: _typing.Optional[Details] = None

   class FolderQuery(Query):
      pass

   class VmSnapshotQuery(Query):
      pass

   class IsoImageQuery(Query):
      pass

   class FloppyImageQuery(Query):
      pass

   class VmNvramQuery(Query):
      pass

   class VmLogQuery(Query):
      pass

   class VmConfigInfo(FileInfo):
      class VmConfigEncryptionInfo(pyVmomi.vmodl.DynamicData):
         keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None

      configVersion: _typing.Optional[int] = None
      encryption: _typing.Optional[VmConfigEncryptionInfo] = None

   class TemplateVmConfigInfo(VmConfigInfo):
      pass

   class VmDiskInfo(FileInfo):
      class VmDiskEncryptionInfo(pyVmomi.vmodl.DynamicData):
         keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None

      diskType: _typing.Optional[type] = None
      capacityKb: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      hardwareVersion: _typing.Optional[int] = None
      controllerType: _typing.Optional[type] = None
      diskExtents: list[str] = []
      thin: _typing.Optional[bool] = None
      encryption: _typing.Optional[VmDiskEncryptionInfo] = None
      sectorFormat: _typing.Optional[str] = None

   class FolderInfo(FileInfo):
      pass

   class VmSnapshotInfo(FileInfo):
      pass

   class IsoImageInfo(FileInfo):
      pass

   class FloppyImageInfo(FileInfo):
      pass

   class VmNvramInfo(FileInfo):
      pass

   class VmLogInfo(FileInfo):
      pass

   class SearchSpec(pyVmomi.vmodl.DynamicData):
      query: list[Query] = []
      details: _typing.Optional[FileInfo.Details] = None
      searchCaseInsensitive: _typing.Optional[bool] = None
      matchPattern: list[str] = []
      sortFoldersFirst: _typing.Optional[bool] = None

   class SearchResults(pyVmomi.vmodl.DynamicData):
      datastore: _typing.Optional[pyVmomi.vim.Datastore] = None
      folderPath: _typing.Optional[str] = None
      file: list[FileInfo] = []

   @property
   def datastore(self) -> list[pyVmomi.vim.Datastore]: ...
   @property
   def supportedType(self) -> list[Query]: ...

   def Search(self, datastorePath: str, searchSpec: _typing.Optional[SearchSpec]) -> pyVmomi.vim.Task: ...
   def SearchSubFolders(self, datastorePath: str, searchSpec: _typing.Optional[SearchSpec]) -> pyVmomi.vim.Task: ...
   def DeleteFile(self, datastorePath: str) -> None: ...


class DatastoreSystem(pyVmomi.VmomiSupport.ManagedObject):
   class Capabilities(pyVmomi.vmodl.DynamicData):
      nfsMountCreationRequired: bool
      nfsMountCreationSupported: bool
      localDatastoreSupported: bool
      vmfsExtentExpansionSupported: bool

   class VvolDatastoreSpec(pyVmomi.vmodl.DynamicData):
      name: str
      scId: str

   class DatastoreResult(pyVmomi.vmodl.DynamicData):
      key: pyVmomi.vim.Datastore
      fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

   @property
   def datastore(self) -> list[pyVmomi.vim.Datastore]: ...
   @property
   def capabilities(self) -> Capabilities: ...

   def UpdateLocalSwapDatastore(self, datastore: _typing.Optional[pyVmomi.vim.Datastore]) -> None: ...
   def QueryAvailableDisksForVmfs(self, datastore: _typing.Optional[pyVmomi.vim.Datastore]) -> list[ScsiDisk]: ...
   def QueryVmfsDatastoreCreateOptions(self, devicePath: str, vmfsMajorVersion: _typing.Optional[int]) -> list[VmfsDatastoreOption]: ...
   def CreateVmfsDatastore(self, spec: VmfsDatastoreCreateSpec) -> pyVmomi.vim.Datastore: ...
   def QueryVmfsDatastoreExtendOptions(self, datastore: pyVmomi.vim.Datastore, devicePath: str, suppressExpandCandidates: _typing.Optional[bool]) -> list[VmfsDatastoreOption]: ...
   def QueryVmfsDatastoreExpandOptions(self, datastore: pyVmomi.vim.Datastore) -> list[VmfsDatastoreOption]: ...
   def ExtendVmfsDatastore(self, datastore: pyVmomi.vim.Datastore, spec: VmfsDatastoreExtendSpec) -> pyVmomi.vim.Datastore: ...
   def EnableClusteredVmdkSupport(self, datastore: pyVmomi.vim.Datastore) -> None: ...
   def DisableClusteredVmdkSupport(self, datastore: pyVmomi.vim.Datastore) -> None: ...
   def ExpandVmfsDatastore(self, datastore: pyVmomi.vim.Datastore, spec: VmfsDatastoreExpandSpec) -> pyVmomi.vim.Datastore: ...
   def CreateNasDatastore(self, spec: NasVolume.Specification) -> pyVmomi.vim.Datastore: ...
   def CreateLocalDatastore(self, name: str, path: str) -> pyVmomi.vim.Datastore: ...
   def CreateVvolDatastore(self, spec: VvolDatastoreSpec) -> pyVmomi.vim.Datastore: ...
   def RemoveDatastore(self, datastore: pyVmomi.vim.Datastore) -> None: ...
   def SetMaxQueueDepth(self, datastore: pyVmomi.vim.Datastore, maxQdepth: pyVmomi.VmomiSupport.long) -> None: ...
   def ResolveNfsServerHostName(self, hostName: str, volumeName: _typing.Optional[str], force: _typing.Optional[bool], isNFS41: _typing.Optional[bool]) -> None: ...
   def QueryMaxQueueDepth(self, datastore: pyVmomi.vim.Datastore) -> pyVmomi.VmomiSupport.long: ...
   def RemoveDatastoreEx(self, datastore: list[pyVmomi.vim.Datastore]) -> pyVmomi.vim.Task: ...
   def ConfigureDatastorePrincipal(self, userName: str, password: _typing.Optional[str]) -> None: ...
   def QueryUnresolvedVmfsVolumes(self) -> list[UnresolvedVmfsVolume]: ...
   def ResignatureUnresolvedVmfsVolume(self, resolutionSpec: UnresolvedVmfsResignatureSpec) -> pyVmomi.vim.Task: ...


class DateTimeConfig(pyVmomi.vmodl.DynamicData):
   timeZone: _typing.Optional[str] = None
   ntpConfig: _typing.Optional[NtpConfig] = None
   ptpConfig: _typing.Optional[PtpConfig] = None
   protocol: _typing.Optional[str] = None
   enabled: _typing.Optional[bool] = None
   disableEvents: _typing.Optional[bool] = None
   disableFallback: _typing.Optional[bool] = None
   resetToFactoryDefaults: _typing.Optional[bool] = None


class DateTimeInfo(pyVmomi.vmodl.DynamicData):
   class Protocol(pyVmomi.VmomiSupport.Enum):
      ntp: _typing.ClassVar['Protocol'] = 'ntp'
      ptp: _typing.ClassVar['Protocol'] = 'ptp'

   timeZone: DateTimeSystem.TimeZone
   systemClockProtocol: _typing.Optional[str] = None
   ntpConfig: _typing.Optional[NtpConfig] = None
   ptpConfig: _typing.Optional[PtpConfig] = None
   enabled: _typing.Optional[bool] = None
   disableEvents: _typing.Optional[bool] = None
   disableFallback: _typing.Optional[bool] = None
   inFallbackState: _typing.Optional[bool] = None
   serviceSync: _typing.Optional[bool] = None
   lastSyncTime: _typing.Optional[_datetime.datetime] = None
   remoteNtpServer: _typing.Optional[str] = None
   ntpRunTime: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   ptpRunTime: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   ntpDuration: _typing.Optional[str] = None
   ptpDuration: _typing.Optional[str] = None


class DateTimeSystem(pyVmomi.VmomiSupport.ManagedObject):
   class TimeZone(pyVmomi.vmodl.DynamicData):
      key: str
      name: str
      description: str
      gmtOffset: int

   class ServiceTestResult(pyVmomi.vmodl.DynamicData):
      workingNormally: bool
      report: list[str] = []

   @property
   def dateTimeInfo(self) -> DateTimeInfo: ...

   def UpdateConfig(self, config: DateTimeConfig) -> None: ...
   def QueryAvailableTimeZones(self) -> list[TimeZone]: ...
   def QueryDateTime(self) -> _datetime.datetime: ...
   def UpdateDateTime(self, dateTime: _datetime.datetime) -> None: ...
   def Refresh(self) -> None: ...
   def TestTimeService(self) -> _typing.Optional[ServiceTestResult]: ...


class DeploymentInfo(pyVmomi.vmodl.DynamicData):
   bootedFromStatelessCache: _typing.Optional[bool] = None


class Device(pyVmomi.vmodl.DynamicData):
   deviceName: str
   deviceType: str


class DevicePciId(pyVmomi.vmodl.DynamicData):
   vendorId: pyVmomi.VmomiSupport.long
   deviceId: pyVmomi.VmomiSupport.long
   subVendorId: pyVmomi.VmomiSupport.long
   subDeviceId: pyVmomi.VmomiSupport.long


class DhcpService(pyVmomi.vmodl.DynamicData):
   class Specification(pyVmomi.vmodl.DynamicData):
      virtualSwitch: str
      defaultLeaseDuration: int
      leaseBeginIp: str
      leaseEndIp: str
      maxLeaseDuration: int
      unlimitedLease: bool
      ipSubnetAddr: str
      ipSubnetMask: str

   class Config(pyVmomi.vmodl.DynamicData):
      changeOperation: _typing.Optional[str] = None
      key: str
      spec: Specification

   key: str
   spec: Specification


class DiagnosticPartition(pyVmomi.vmodl.DynamicData):
   class StorageType(pyVmomi.VmomiSupport.Enum):
      directAttached: _typing.ClassVar['StorageType'] = 'directAttached'
      networkAttached: _typing.ClassVar['StorageType'] = 'networkAttached'

   class DiagnosticType(pyVmomi.VmomiSupport.Enum):
      singleHost: _typing.ClassVar['DiagnosticType'] = 'singleHost'
      multiHost: _typing.ClassVar['DiagnosticType'] = 'multiHost'

   class CreateOption(pyVmomi.vmodl.DynamicData):
      storageType: str
      diagnosticType: str
      disk: ScsiDisk

   class CreateSpec(pyVmomi.vmodl.DynamicData):
      storageType: str
      diagnosticType: str
      id: ScsiDisk.Partition
      partition: DiskPartitionInfo.Specification
      active: _typing.Optional[bool] = None

   class CreateDescription(pyVmomi.vmodl.DynamicData):
      layout: DiskPartitionInfo.Layout
      diskUuid: str
      spec: CreateSpec

   storageType: str
   diagnosticType: str
   slots: int
   id: ScsiDisk.Partition


class DiagnosticSystem(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def activePartition(self) -> _typing.Optional[DiagnosticPartition]: ...

   def QueryAvailablePartition(self) -> list[DiagnosticPartition]: ...
   def SelectActivePartition(self, partition: _typing.Optional[ScsiDisk.Partition]) -> None: ...
   def QueryPartitionCreateOptions(self, storageType: str, diagnosticType: str) -> list[DiagnosticPartition.CreateOption]: ...
   def QueryPartitionCreateDesc(self, diskUuid: str, diagnosticType: str) -> DiagnosticPartition.CreateDescription: ...
   def CreateDiagnosticPartition(self, spec: DiagnosticPartition.CreateSpec) -> None: ...


class DigestInfo(pyVmomi.vmodl.DynamicData):
   class DigestMethodType(pyVmomi.VmomiSupport.Enum):
      SHA1: _typing.ClassVar['DigestMethodType'] = 'SHA1'
      MD5: _typing.ClassVar['DigestMethodType'] = 'MD5'
      SHA256: _typing.ClassVar['DigestMethodType'] = 'SHA256'
      SHA384: _typing.ClassVar['DigestMethodType'] = 'SHA384'
      SHA512: _typing.ClassVar['DigestMethodType'] = 'SHA512'
      SM3_256: _typing.ClassVar['DigestMethodType'] = 'SM3_256'

   digestMethod: str
   digestValue: list[pyVmomi.VmomiSupport.byte] = []
   objectName: _typing.Optional[str] = None

class DigestVerificationSetting:
   pass

class DirectoryStore(AuthenticationStore):
   pass

class DirectoryStoreInfo(AuthenticationStoreInfo):
   pass


class DiskConfigurationResult(pyVmomi.vmodl.DynamicData):
   devicePath: _typing.Optional[str] = None
   success: _typing.Optional[bool] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class DiskDimensions(pyVmomi.vmodl.DynamicData):
   class Chs(pyVmomi.vmodl.DynamicData):
      cylinder: pyVmomi.VmomiSupport.long
      head: int
      sector: int

   class Lba(pyVmomi.vmodl.DynamicData):
      blockSize: int
      block: pyVmomi.VmomiSupport.long


class DiskPartitionInfo(pyVmomi.vmodl.DynamicData):
   class PartitionFormat(pyVmomi.VmomiSupport.Enum):
      gpt: _typing.ClassVar['PartitionFormat'] = 'gpt'
      mbr: _typing.ClassVar['PartitionFormat'] = 'mbr'
      unknown: _typing.ClassVar['PartitionFormat'] = 'unknown'

   class Type(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['Type'] = 'none'
      vmfs: _typing.ClassVar['Type'] = 'vmfs'
      linuxNative: _typing.ClassVar['Type'] = 'linuxNative'
      linuxSwap: _typing.ClassVar['Type'] = 'linuxSwap'
      extended: _typing.ClassVar['Type'] = 'extended'
      ntfs: _typing.ClassVar['Type'] = 'ntfs'
      vmkDiagnostic: _typing.ClassVar['Type'] = 'vmkDiagnostic'
      vffs: _typing.ClassVar['Type'] = 'vffs'

   class Partition(pyVmomi.vmodl.DynamicData):
      partition: int
      startSector: pyVmomi.VmomiSupport.long
      endSector: pyVmomi.VmomiSupport.long
      type: str
      guid: _typing.Optional[str] = None
      logical: bool
      attributes: pyVmomi.VmomiSupport.byte
      partitionAlignment: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class BlockRange(pyVmomi.vmodl.DynamicData):
      partition: _typing.Optional[int] = None
      type: str
      start: DiskDimensions.Lba
      end: DiskDimensions.Lba

   class Specification(pyVmomi.vmodl.DynamicData):
      partitionFormat: _typing.Optional[str] = None
      chs: _typing.Optional[DiskDimensions.Chs] = None
      totalSectors: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      partition: list[Partition] = []
      sectorSize: _typing.Optional[int] = None

   class Layout(pyVmomi.vmodl.DynamicData):
      total: _typing.Optional[DiskDimensions.Lba] = None
      partition: list[BlockRange] = []

   deviceName: str
   spec: Specification
   layout: Layout


class DnsConfig(pyVmomi.vmodl.DynamicData):
   dhcp: bool
   virtualNicDevice: _typing.Optional[str] = None
   ipv6VirtualNicDevice: _typing.Optional[str] = None
   hostName: str
   domainName: str
   address: list[str] = []
   searchDomain: list[str] = []


class DnsConfigSpec(DnsConfig):
   virtualNicConnection: _typing.Optional[VirtualNicConnection] = None
   virtualNicConnectionV6: _typing.Optional[VirtualNicConnection] = None


class DvxClass(pyVmomi.vmodl.DynamicData):
   deviceClass: str
   checkpointSupported: bool
   swDMATracingSupported: bool
   sriovNic: bool


class EnterMaintenanceResult(pyVmomi.vmodl.DynamicData):
   vmFaults: list[pyVmomi.vim.FaultsByVM] = []
   hostFaults: list[pyVmomi.vim.FaultsByHost] = []


class EsxAgentHostManager(pyVmomi.VmomiSupport.ManagedObject):
   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      agentVmDatastore: _typing.Optional[pyVmomi.vim.Datastore] = None
      agentVmNetwork: _typing.Optional[pyVmomi.vim.Network] = None

   @property
   def configInfo(self) -> ConfigInfo: ...

   def UpdateConfig(self, configInfo: ConfigInfo) -> None: ...


class FcoeConfig(pyVmomi.vmodl.DynamicData):
   class VlanRange(pyVmomi.vmodl.DynamicData):
      vlanLow: int
      vlanHigh: int

   class FcoeCapabilities(pyVmomi.vmodl.DynamicData):
      priorityClass: bool
      sourceMacAddress: bool
      vlanRange: bool

   class FcoeSpecification(pyVmomi.vmodl.DynamicData):
      underlyingPnic: str
      priorityClass: _typing.Optional[int] = None
      sourceMac: _typing.Optional[str] = None
      vlanRange: list[VlanRange] = []

   priorityClass: int
   sourceMac: str
   vlanRange: list[VlanRange] = []
   capabilities: FcoeCapabilities
   fcoeActive: bool


class FeatureCapability(pyVmomi.vmodl.DynamicData):
   key: str
   featureName: str
   value: str


class FeatureMask(pyVmomi.vmodl.DynamicData):
   key: str
   featureName: str
   value: str


class FeatureVersionInfo(pyVmomi.vmodl.DynamicData):
   class FeatureVersionKey(pyVmomi.VmomiSupport.Enum):
      faultTolerance: _typing.ClassVar['FeatureVersionKey'] = 'faultTolerance'

   key: str
   value: str


class FibreChannelHba(HostBusAdapter):
   class PortType(pyVmomi.VmomiSupport.Enum):
      fabric: _typing.ClassVar['PortType'] = 'fabric'
      loop: _typing.ClassVar['PortType'] = 'loop'
      pointToPoint: _typing.ClassVar['PortType'] = 'pointToPoint'
      unknown: _typing.ClassVar['PortType'] = 'unknown'

   portWorldWideName: pyVmomi.VmomiSupport.long
   nodeWorldWideName: pyVmomi.VmomiSupport.long
   portType: PortType
   speed: pyVmomi.VmomiSupport.long


class FibreChannelOverEthernetHba(FibreChannelHba):
   class LinkInfo(pyVmomi.vmodl.DynamicData):
      vnportMac: str
      fcfMac: str
      vlanId: int

   underlyingNic: str
   linkInfo: LinkInfo
   isSoftwareFcoe: bool
   markedForRemoval: _typing.Optional[bool] = None

class FibreChannelOverEthernetTargetTransport(FibreChannelTargetTransport):
   vnportMac: str
   fcfMac: str
   vlanId: int


class FibreChannelTargetTransport(TargetTransport):
   portWorldWideName: pyVmomi.VmomiSupport.long
   nodeWorldWideName: pyVmomi.VmomiSupport.long


class FileAccess(pyVmomi.vmodl.DynamicData):
   class Modes(pyVmomi.vmodl.DynamicData):
      browse: _typing.Optional[str] = None
      read: str
      modify: str
      use: str
      admin: _typing.Optional[str] = None
      full: str

   who: str
   what: str


class FileSystemMountInfo(pyVmomi.vmodl.DynamicData):
   class VStorageSupportStatus(pyVmomi.VmomiSupport.Enum):
      vStorageSupported: _typing.ClassVar['VStorageSupportStatus'] = 'vStorageSupported'
      vStorageUnsupported: _typing.ClassVar['VStorageSupportStatus'] = 'vStorageUnsupported'
      vStorageUnknown: _typing.ClassVar['VStorageSupportStatus'] = 'vStorageUnknown'

   mountInfo: MountInfo
   volume: FileSystemVolume
   vStorageSupport: _typing.Optional[str] = None


class FileSystemVolume(pyVmomi.vmodl.DynamicData):
   class FileSystemType(pyVmomi.VmomiSupport.Enum):
      VMFS: _typing.ClassVar['FileSystemType'] = 'VMFS'
      NFS: _typing.ClassVar['FileSystemType'] = 'NFS'
      NFS41: _typing.ClassVar['FileSystemType'] = 'NFS41'
      CIFS: _typing.ClassVar['FileSystemType'] = 'CIFS'
      vsan: _typing.ClassVar['FileSystemType'] = 'vsan'
      VFFS: _typing.ClassVar['FileSystemType'] = 'VFFS'
      VVOL: _typing.ClassVar['FileSystemType'] = 'VVOL'
      PMEM: _typing.ClassVar['FileSystemType'] = 'PMEM'
      vsanD: _typing.ClassVar['FileSystemType'] = 'vsanD'
      OTHER: _typing.ClassVar['FileSystemType'] = 'OTHER'

   type: str
   name: str
   capacity: pyVmomi.VmomiSupport.long


class FileSystemVolumeInfo(pyVmomi.vmodl.DynamicData):
   volumeTypeList: list[str] = []
   mountInfo: list[FileSystemMountInfo] = []


class FirewallConfig(pyVmomi.vmodl.DynamicData):
   class RuleSetConfig(pyVmomi.vmodl.DynamicData):
      rulesetId: str
      enabled: bool
      allowedHosts: _typing.Optional[Ruleset.IpList] = None

   rule: list[RuleSetConfig] = []
   defaultBlockingPolicy: FirewallInfo.DefaultPolicy


class FirewallInfo(pyVmomi.vmodl.DynamicData):
   class DefaultPolicy(pyVmomi.vmodl.DynamicData):
      incomingBlocked: _typing.Optional[bool] = None
      outgoingBlocked: _typing.Optional[bool] = None

   defaultPolicy: DefaultPolicy
   ruleset: list[Ruleset] = []


class FirewallSystem(pyVmomi.vim.ExtensibleManagedObject):
   class ServiceName(pyVmomi.VmomiSupport.Enum):
      vpxa: _typing.ClassVar['ServiceName'] = 'vpxa'

   class RuleSetId(pyVmomi.VmomiSupport.Enum):
      faultTolerance: _typing.ClassVar['RuleSetId'] = 'faultTolerance'
      fdm: _typing.ClassVar['RuleSetId'] = 'fdm'
      updateManager: _typing.ClassVar['RuleSetId'] = 'updateManager'
      vpxHeartbeats: _typing.ClassVar['RuleSetId'] = 'vpxHeartbeats'

   @property
   def firewallInfo(self) -> _typing.Optional[FirewallInfo]: ...

   def UpdateDefaultPolicy(self, defaultPolicy: FirewallInfo.DefaultPolicy) -> None: ...
   def EnableRuleset(self, id: str) -> None: ...
   def DisableRuleset(self, id: str) -> None: ...
   def UpdateRuleset(self, id: str, spec: Ruleset.RulesetSpec) -> None: ...
   def Refresh(self) -> None: ...


class FirmwareSystem(pyVmomi.VmomiSupport.ManagedObject):
   def ResetToFactoryDefaults(self) -> None: ...
   def BackupConfiguration(self) -> str: ...
   def QueryConfigUploadURL(self) -> str: ...
   def RestoreConfiguration(self, force: bool) -> None: ...


class FlagInfo(pyVmomi.vmodl.DynamicData):
   backgroundSnapshotsEnabled: _typing.Optional[bool] = None


class ForceMountedInfo(pyVmomi.vmodl.DynamicData):
   persist: bool
   mounted: bool


class Fru(pyVmomi.vmodl.DynamicData):
   class FruType(pyVmomi.VmomiSupport.Enum):
      undefined: _typing.ClassVar['FruType'] = 'undefined'
      board: _typing.ClassVar['FruType'] = 'board'
      product: _typing.ClassVar['FruType'] = 'product'

   type: str
   partName: str
   partNumber: str
   manufacturer: str
   serialNumber: _typing.Optional[str] = None
   mfgTimeStamp: _typing.Optional[_datetime.datetime] = None


class GatewaySpec(pyVmomi.vmodl.DynamicData):
   gatewayType: str
   gatewayId: _typing.Optional[str] = None
   trustVerificationToken: _typing.Optional[str] = None
   hostAuthParams: list[pyVmomi.vim.KeyValue] = []


class GraphicsConfig(pyVmomi.vmodl.DynamicData):
   class GraphicsType(pyVmomi.VmomiSupport.Enum):
      shared: _typing.ClassVar['GraphicsType'] = 'shared'
      sharedDirect: _typing.ClassVar['GraphicsType'] = 'sharedDirect'

   class SharedPassthruAssignmentPolicy(pyVmomi.VmomiSupport.Enum):
      performance: _typing.ClassVar['SharedPassthruAssignmentPolicy'] = 'performance'
      consolidation: _typing.ClassVar['SharedPassthruAssignmentPolicy'] = 'consolidation'

   class VgpuMode(pyVmomi.VmomiSupport.Enum):
      sameSize: _typing.ClassVar['VgpuMode'] = 'sameSize'
      mixedSize: _typing.ClassVar['VgpuMode'] = 'mixedSize'

   class DeviceType(pyVmomi.vmodl.DynamicData):
      deviceId: str
      graphicsType: str
      vgpuMode: _typing.Optional[str] = None

   hostDefaultGraphicsType: str
   sharedPassthruAssignmentPolicy: str
   deviceType: list[DeviceType] = []


class GraphicsInfo(pyVmomi.vmodl.DynamicData):
   class GraphicsType(pyVmomi.VmomiSupport.Enum):
      basic: _typing.ClassVar['GraphicsType'] = 'basic'
      shared: _typing.ClassVar['GraphicsType'] = 'shared'
      direct: _typing.ClassVar['GraphicsType'] = 'direct'
      sharedDirect: _typing.ClassVar['GraphicsType'] = 'sharedDirect'

   class VgpuMode(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['VgpuMode'] = 'none'
      sameSize: _typing.ClassVar['VgpuMode'] = 'sameSize'
      mixedSize: _typing.ClassVar['VgpuMode'] = 'mixedSize'
      multiInstanceGpu: _typing.ClassVar['VgpuMode'] = 'multiInstanceGpu'

   deviceName: str
   vendorName: str
   pciId: str
   graphicsType: str
   vgpuMode: _typing.Optional[str] = None
   memorySizeInKB: pyVmomi.VmomiSupport.long
   vm: list[pyVmomi.vim.VirtualMachine] = []


class GraphicsManager(pyVmomi.vim.ExtensibleManagedObject):
   @property
   def graphicsInfo(self) -> list[GraphicsInfo]: ...
   @property
   def graphicsConfig(self) -> _typing.Optional[GraphicsConfig]: ...
   @property
   def sharedPassthruGpuTypes(self) -> list[str]: ...
   @property
   def sharedGpuCapabilities(self) -> list[SharedGpuCapabilities]: ...

   def RetrieveVgpuDeviceInfo(self) -> list[pyVmomi.vim.vm.VgpuDeviceInfo]: ...
   def RetrieveVgpuProfileInfo(self) -> list[pyVmomi.vim.vm.VgpuProfileInfo]: ...
   def Refresh(self) -> None: ...
   def IsSharedGraphicsActive(self) -> bool: ...
   def UpdateGraphicsConfig(self, config: GraphicsConfig) -> None: ...


class HardwareInfo(pyVmomi.vmodl.DynamicData):
   systemInfo: SystemInfo
   cpuPowerManagementInfo: _typing.Optional[CpuPowerManagementInfo] = None
   cpuInfo: CpuInfo
   cpuPkg: list[CpuPackage] = []
   memorySize: pyVmomi.VmomiSupport.long
   numaInfo: _typing.Optional[NumaInfo] = None
   smcPresent: bool
   pciDevice: list[PciDevice] = []
   dvxClasses: list[DvxClass] = []
   cpuFeature: list[CpuIdInfo] = []
   biosInfo: _typing.Optional[BIOSInfo] = None
   reliableMemoryInfo: _typing.Optional[ReliableMemoryInfo] = None
   persistentMemoryInfo: _typing.Optional[PersistentMemoryInfo] = None
   sgxInfo: _typing.Optional[SgxInfo] = None
   sevInfo: _typing.Optional[SevInfo] = None
   memoryTieringType: _typing.Optional[str] = None
   memoryTierInfo: list[MemoryTierInfo] = []
   tdxInfo: _typing.Optional[TdxInfo] = None


class HardwareStatusInfo(pyVmomi.vmodl.DynamicData):
   class Status(pyVmomi.VmomiSupport.Enum):
      Unknown: _typing.ClassVar['Status'] = 'Unknown'
      Green: _typing.ClassVar['Status'] = 'Green'
      Yellow: _typing.ClassVar['Status'] = 'Yellow'
      Red: _typing.ClassVar['Status'] = 'Red'

   class HardwareElementInfo(pyVmomi.vmodl.DynamicData):
      name: str
      status: pyVmomi.vim.ElementDescription

   class StorageStatusInfo(HardwareElementInfo):
      class OperationalInfo(pyVmomi.vmodl.DynamicData):
         property: str
         value: str

      operationalInfo: list[OperationalInfo] = []

   class DpuStatusInfo(HardwareElementInfo):
      class OperationalInfo(pyVmomi.vmodl.DynamicData):
         sensorId: str
         healthState: _typing.Optional[pyVmomi.vim.ElementDescription] = None
         reading: str
         units: _typing.Optional[str] = None
         timeStamp: _typing.Optional[_datetime.datetime] = None

      dpuId: str
      fru: _typing.Optional[Fru] = None
      sensors: list[OperationalInfo] = []

   memoryStatusInfo: list[HardwareElementInfo] = []
   cpuStatusInfo: list[HardwareElementInfo] = []
   storageStatusInfo: list[StorageStatusInfo] = []
   dpuStatusInfo: list[DpuStatusInfo] = []


class HbaCreateSpec(pyVmomi.vmodl.DynamicData):
   pass


class HealthStatusSystem(pyVmomi.VmomiSupport.ManagedObject):
   class Runtime(pyVmomi.vmodl.DynamicData):
      systemHealthInfo: _typing.Optional[SystemHealthInfo] = None
      hardwareStatusInfo: _typing.Optional[HardwareStatusInfo] = None

   @property
   def runtime(self) -> Runtime: ...

   def Refresh(self) -> None: ...
   def ResetSystemHealthInfo(self) -> None: ...
   def ClearSystemEventLog(self) -> None: ...
   def FetchSystemEventLog(self) -> list[SystemEventInfo]: ...


class HostAccessManager(pyVmomi.VmomiSupport.ManagedObject):
   class AccessMode(pyVmomi.VmomiSupport.Enum):
      accessNone: _typing.ClassVar['AccessMode'] = 'accessNone'
      accessAdmin: _typing.ClassVar['AccessMode'] = 'accessAdmin'
      accessNoAccess: _typing.ClassVar['AccessMode'] = 'accessNoAccess'
      accessReadOnly: _typing.ClassVar['AccessMode'] = 'accessReadOnly'
      accessOther: _typing.ClassVar['AccessMode'] = 'accessOther'

   class AccessEntry(pyVmomi.vmodl.DynamicData):
      principal: str
      group: bool
      accessMode: AccessMode

   class LockdownMode(pyVmomi.VmomiSupport.Enum):
      lockdownDisabled: _typing.ClassVar['LockdownMode'] = 'lockdownDisabled'
      lockdownNormal: _typing.ClassVar['LockdownMode'] = 'lockdownNormal'
      lockdownStrict: _typing.ClassVar['LockdownMode'] = 'lockdownStrict'

   @property
   def lockdownMode(self) -> LockdownMode: ...

   def RetrieveAccessEntries(self) -> list[AccessEntry]: ...
   def ChangeAccessMode(self, principal: str, isGroup: bool, accessMode: AccessMode) -> None: ...
   def QuerySystemUsers(self) -> list[str]: ...
   def UpdateSystemUsers(self, users: list[str]) -> None: ...
   def QueryLockdownExceptions(self) -> list[str]: ...
   def UpdateLockdownExceptions(self, users: list[str]) -> None: ...
   def ChangeLockdownMode(self, mode: LockdownMode) -> None: ...


class HostBusAdapter(pyVmomi.vmodl.DynamicData):
   key: _typing.Optional[str] = None
   device: str
   bus: int
   status: str
   model: str
   driver: _typing.Optional[str] = None
   pci: _typing.Optional[str] = None
   storageProtocol: _typing.Optional[str] = None
   driverVersion: _typing.Optional[str] = None
   firmwareVersion: _typing.Optional[str] = None


class HostProxySwitch(pyVmomi.vmodl.DynamicData):
   class Specification(pyVmomi.vmodl.DynamicData):
      backing: _typing.Optional[pyVmomi.vim.dvs.HostMember.Backing] = None

   class Config(pyVmomi.vmodl.DynamicData):
      changeOperation: _typing.Optional[str] = None
      uuid: str
      spec: _typing.Optional[Specification] = None

   class HostLagConfig(pyVmomi.vmodl.DynamicData):
      lagKey: str
      lagName: _typing.Optional[str] = None
      uplinkPort: list[pyVmomi.vim.KeyValue] = []

   class EnsInfo(pyVmomi.vmodl.DynamicData):
      opsVersion: pyVmomi.VmomiSupport.long
      numPSOps: pyVmomi.VmomiSupport.long
      numLcoreOps: pyVmomi.VmomiSupport.long
      errorStatus: pyVmomi.VmomiSupport.long
      lcoreStatus: pyVmomi.VmomiSupport.long

   dvsUuid: str
   dvsName: str
   key: str
   numPorts: int
   configNumPorts: _typing.Optional[int] = None
   numPortsAvailable: int
   uplinkPort: list[pyVmomi.vim.KeyValue] = []
   mtu: _typing.Optional[int] = None
   pnic: list[PhysicalNic] = []
   spec: Specification
   hostLag: list[HostLagConfig] = []
   networkReservationSupported: _typing.Optional[bool] = None
   nsxtEnabled: _typing.Optional[bool] = None
   ensEnabled: _typing.Optional[bool] = None
   ensInterruptEnabled: _typing.Optional[bool] = None
   transportZones: list[pyVmomi.vim.dvs.HostMember.TransportZoneInfo] = []
   nsxUsedUplinkPort: list[str] = []
   nsxtStatus: _typing.Optional[str] = None
   nsxtStatusDetail: _typing.Optional[str] = None
   ensInfo: _typing.Optional[EnsInfo] = None
   networkOffloadingEnabled: _typing.Optional[bool] = None
   hostUplinkState: list[pyVmomi.vim.dvs.HostMember.HostUplinkState] = []
   autoDeployOwned: _typing.Optional[bool] = None
   hostPerfNicOffloadState: _typing.Optional[pyVmomi.vim.dvs.HostMember.HostPerfNicOffloadState] = None
   teplessMode: _typing.Optional[bool] = None


class HostSpbm(pyVmomi.VmomiSupport.ManagedObject):
   pass


class HostSpbmDatastoreInfo(pyVmomi.vmodl.DynamicData):
   datastoreUrl: str
   namespace: str
   defaultProfileId: str


class HostSpbmHashInfo(pyVmomi.vmodl.DynamicData):
   policyInfoHash: str
   datastoreInfoHash: str


class HostSpbmPolicyBlobInfo(pyVmomi.vmodl.DynamicData):
   policyBlob: str
   namespace: str


class HostSpbmPolicyInfo(pyVmomi.vmodl.DynamicData):
   profileId: str
   name: str
   description: _typing.Optional[str] = None
   generationId: pyVmomi.VmomiSupport.long
   policyBlobInfo: list[HostSpbmPolicyBlobInfo] = []


class ImageConfigManager(pyVmomi.VmomiSupport.ManagedObject):
   class AcceptanceLevel(pyVmomi.VmomiSupport.Enum):
      vmware_certified: _typing.ClassVar['AcceptanceLevel'] = 'vmware_certified'
      vmware_accepted: _typing.ClassVar['AcceptanceLevel'] = 'vmware_accepted'
      partner: _typing.ClassVar['AcceptanceLevel'] = 'partner'
      community: _typing.ClassVar['AcceptanceLevel'] = 'community'

   class ImageProfileSummary(pyVmomi.vmodl.DynamicData):
      name: str
      vendor: str

   def QueryHostAcceptanceLevel(self) -> str: ...
   def QueryHostImageProfile(self) -> ImageProfileSummary: ...
   def UpdateAcceptanceLevel(self, newAcceptanceLevel: str) -> None: ...
   def FetchSoftwarePackages(self) -> list[SoftwarePackage]: ...
   def InstallDate(self) -> _datetime.datetime: ...


class InternetScsiHba(HostBusAdapter):
   class ParamValue(pyVmomi.vim.option.OptionValue):
      isInherited: _typing.Optional[bool] = None

   class DiscoveryCapabilities(pyVmomi.vmodl.DynamicData):
      iSnsDiscoverySettable: bool
      slpDiscoverySettable: bool
      staticTargetDiscoverySettable: bool
      sendTargetsDiscoverySettable: bool

   class DiscoveryProperties(pyVmomi.vmodl.DynamicData):
      class ISnsDiscoveryMethod(pyVmomi.VmomiSupport.Enum):
         isnsStatic: _typing.ClassVar['ISnsDiscoveryMethod'] = 'isnsStatic'
         isnsDhcp: _typing.ClassVar['ISnsDiscoveryMethod'] = 'isnsDhcp'
         isnsSlp: _typing.ClassVar['ISnsDiscoveryMethod'] = 'isnsSlp'

      class SlpDiscoveryMethod(pyVmomi.VmomiSupport.Enum):
         slpDhcp: _typing.ClassVar['SlpDiscoveryMethod'] = 'slpDhcp'
         slpAutoUnicast: _typing.ClassVar['SlpDiscoveryMethod'] = 'slpAutoUnicast'
         slpAutoMulticast: _typing.ClassVar['SlpDiscoveryMethod'] = 'slpAutoMulticast'
         slpManual: _typing.ClassVar['SlpDiscoveryMethod'] = 'slpManual'

      iSnsDiscoveryEnabled: bool
      iSnsDiscoveryMethod: _typing.Optional[str] = None
      iSnsHost: _typing.Optional[str] = None
      slpDiscoveryEnabled: bool
      slpDiscoveryMethod: _typing.Optional[str] = None
      slpHost: _typing.Optional[str] = None
      staticTargetDiscoveryEnabled: bool
      sendTargetsDiscoveryEnabled: bool

   class ChapAuthenticationType(pyVmomi.VmomiSupport.Enum):
      chapProhibited: _typing.ClassVar['ChapAuthenticationType'] = 'chapProhibited'
      chapDiscouraged: _typing.ClassVar['ChapAuthenticationType'] = 'chapDiscouraged'
      chapPreferred: _typing.ClassVar['ChapAuthenticationType'] = 'chapPreferred'
      chapRequired: _typing.ClassVar['ChapAuthenticationType'] = 'chapRequired'

   class AuthenticationCapabilities(pyVmomi.vmodl.DynamicData):
      chapAuthSettable: bool
      krb5AuthSettable: bool
      srpAuthSettable: bool
      spkmAuthSettable: bool
      mutualChapSettable: _typing.Optional[bool] = None
      targetChapSettable: _typing.Optional[bool] = None
      targetMutualChapSettable: _typing.Optional[bool] = None

   class AuthenticationProperties(pyVmomi.vmodl.DynamicData):
      chapAuthEnabled: bool
      chapName: _typing.Optional[str] = None
      chapSecret: _typing.Optional[str] = None
      chapAuthenticationType: _typing.Optional[str] = None
      chapInherited: _typing.Optional[bool] = None
      mutualChapName: _typing.Optional[str] = None
      mutualChapSecret: _typing.Optional[str] = None
      mutualChapAuthenticationType: _typing.Optional[str] = None
      mutualChapInherited: _typing.Optional[bool] = None

   class DigestType(pyVmomi.VmomiSupport.Enum):
      digestProhibited: _typing.ClassVar['DigestType'] = 'digestProhibited'
      digestDiscouraged: _typing.ClassVar['DigestType'] = 'digestDiscouraged'
      digestPreferred: _typing.ClassVar['DigestType'] = 'digestPreferred'
      digestRequired: _typing.ClassVar['DigestType'] = 'digestRequired'

   class DigestCapabilities(pyVmomi.vmodl.DynamicData):
      headerDigestSettable: _typing.Optional[bool] = None
      dataDigestSettable: _typing.Optional[bool] = None
      targetHeaderDigestSettable: _typing.Optional[bool] = None
      targetDataDigestSettable: _typing.Optional[bool] = None

   class DigestProperties(pyVmomi.vmodl.DynamicData):
      headerDigestType: _typing.Optional[str] = None
      headerDigestInherited: _typing.Optional[bool] = None
      dataDigestType: _typing.Optional[str] = None
      dataDigestInherited: _typing.Optional[bool] = None

   class IPCapabilities(pyVmomi.vmodl.DynamicData):
      addressSettable: bool
      ipConfigurationMethodSettable: bool
      subnetMaskSettable: bool
      defaultGatewaySettable: bool
      primaryDnsServerAddressSettable: bool
      alternateDnsServerAddressSettable: bool
      ipv6Supported: _typing.Optional[bool] = None
      arpRedirectSettable: _typing.Optional[bool] = None
      mtuSettable: _typing.Optional[bool] = None
      hostNameAsTargetAddress: _typing.Optional[bool] = None
      nameAliasSettable: _typing.Optional[bool] = None
      ipv4EnableSettable: _typing.Optional[bool] = None
      ipv6EnableSettable: _typing.Optional[bool] = None
      ipv6PrefixLengthSettable: _typing.Optional[bool] = None
      ipv6PrefixLength: _typing.Optional[int] = None
      ipv6DhcpConfigurationSettable: _typing.Optional[bool] = None
      ipv6LinkLocalAutoConfigurationSettable: _typing.Optional[bool] = None
      ipv6RouterAdvertisementConfigurationSettable: _typing.Optional[bool] = None
      ipv6DefaultGatewaySettable: _typing.Optional[bool] = None
      ipv6MaxStaticAddressesSupported: _typing.Optional[int] = None

   class IscsiIpv6Address(pyVmomi.vmodl.DynamicData):
      class AddressConfigurationType(pyVmomi.VmomiSupport.Enum):
         DHCP: _typing.ClassVar['AddressConfigurationType'] = 'DHCP'
         AutoConfigured: _typing.ClassVar['AddressConfigurationType'] = 'AutoConfigured'
         Static: _typing.ClassVar['AddressConfigurationType'] = 'Static'
         Other: _typing.ClassVar['AddressConfigurationType'] = 'Other'

      class IPv6AddressOperation(pyVmomi.VmomiSupport.Enum):
         add: _typing.ClassVar['IPv6AddressOperation'] = 'add'
         remove: _typing.ClassVar['IPv6AddressOperation'] = 'remove'

      address: str
      prefixLength: int
      origin: str
      operation: _typing.Optional[str] = None

   class IPv6Properties(pyVmomi.vmodl.DynamicData):
      iscsiIpv6Address: list[IscsiIpv6Address] = []
      ipv6DhcpConfigurationEnabled: _typing.Optional[bool] = None
      ipv6LinkLocalAutoConfigurationEnabled: _typing.Optional[bool] = None
      ipv6RouterAdvertisementConfigurationEnabled: _typing.Optional[bool] = None
      ipv6DefaultGateway: _typing.Optional[str] = None

   class IPProperties(pyVmomi.vmodl.DynamicData):
      mac: _typing.Optional[str] = None
      address: _typing.Optional[str] = None
      dhcpConfigurationEnabled: bool
      subnetMask: _typing.Optional[str] = None
      defaultGateway: _typing.Optional[str] = None
      primaryDnsServerAddress: _typing.Optional[str] = None
      alternateDnsServerAddress: _typing.Optional[str] = None
      ipv6Address: _typing.Optional[str] = None
      ipv6SubnetMask: _typing.Optional[str] = None
      ipv6DefaultGateway: _typing.Optional[str] = None
      arpRedirectEnabled: _typing.Optional[bool] = None
      mtu: _typing.Optional[int] = None
      jumboFramesEnabled: _typing.Optional[bool] = None
      ipv4Enabled: _typing.Optional[bool] = None
      ipv6Enabled: _typing.Optional[bool] = None
      ipv6properties: _typing.Optional[IPv6Properties] = None

   class SendTarget(pyVmomi.vmodl.DynamicData):
      address: str
      port: _typing.Optional[int] = None
      authenticationProperties: _typing.Optional[AuthenticationProperties] = None
      digestProperties: _typing.Optional[DigestProperties] = None
      supportedAdvancedOptions: list[pyVmomi.vim.option.OptionDef] = []
      advancedOptions: list[ParamValue] = []
      parent: _typing.Optional[str] = None

   class StaticTarget(pyVmomi.vmodl.DynamicData):
      class TargetDiscoveryMethod(pyVmomi.VmomiSupport.Enum):
         staticMethod: _typing.ClassVar['TargetDiscoveryMethod'] = 'staticMethod'
         sendTargetMethod: _typing.ClassVar['TargetDiscoveryMethod'] = 'sendTargetMethod'
         slpMethod: _typing.ClassVar['TargetDiscoveryMethod'] = 'slpMethod'
         isnsMethod: _typing.ClassVar['TargetDiscoveryMethod'] = 'isnsMethod'
         unknownMethod: _typing.ClassVar['TargetDiscoveryMethod'] = 'unknownMethod'

      address: str
      port: _typing.Optional[int] = None
      iScsiName: str
      discoveryMethod: _typing.Optional[str] = None
      authenticationProperties: _typing.Optional[AuthenticationProperties] = None
      digestProperties: _typing.Optional[DigestProperties] = None
      supportedAdvancedOptions: list[pyVmomi.vim.option.OptionDef] = []
      advancedOptions: list[ParamValue] = []
      parent: _typing.Optional[str] = None

   class TargetSet(pyVmomi.vmodl.DynamicData):
      staticTargets: list[StaticTarget] = []
      sendTargets: list[SendTarget] = []

   class NetworkBindingSupportType(pyVmomi.VmomiSupport.Enum):
      notsupported: _typing.ClassVar['NetworkBindingSupportType'] = 'notsupported'
      optional: _typing.ClassVar['NetworkBindingSupportType'] = 'optional'
      required: _typing.ClassVar['NetworkBindingSupportType'] = 'required'

   isSoftwareBased: bool
   canBeDisabled: _typing.Optional[bool] = None
   networkBindingSupport: _typing.Optional[NetworkBindingSupportType] = None
   discoveryCapabilities: DiscoveryCapabilities
   discoveryProperties: DiscoveryProperties
   authenticationCapabilities: AuthenticationCapabilities
   authenticationProperties: AuthenticationProperties
   digestCapabilities: _typing.Optional[DigestCapabilities] = None
   digestProperties: _typing.Optional[DigestProperties] = None
   ipCapabilities: IPCapabilities
   ipProperties: IPProperties
   supportedAdvancedOptions: list[pyVmomi.vim.option.OptionDef] = []
   advancedOptions: list[ParamValue] = []
   iScsiName: str
   iScsiAlias: _typing.Optional[str] = None
   configuredSendTarget: list[SendTarget] = []
   configuredStaticTarget: list[StaticTarget] = []
   maxSpeedMb: _typing.Optional[int] = None
   currentSpeedMb: _typing.Optional[int] = None


class InternetScsiTargetTransport(TargetTransport):
   iScsiName: str
   iScsiAlias: str
   address: list[str] = []


class IpConfig(pyVmomi.vmodl.DynamicData):
   class IpV6AddressConfigType(pyVmomi.VmomiSupport.Enum):
      other: _typing.ClassVar['IpV6AddressConfigType'] = 'other'
      manual: _typing.ClassVar['IpV6AddressConfigType'] = 'manual'
      dhcp: _typing.ClassVar['IpV6AddressConfigType'] = 'dhcp'
      linklayer: _typing.ClassVar['IpV6AddressConfigType'] = 'linklayer'
      random: _typing.ClassVar['IpV6AddressConfigType'] = 'random'

   class IpV6AddressStatus(pyVmomi.VmomiSupport.Enum):
      preferred: _typing.ClassVar['IpV6AddressStatus'] = 'preferred'
      deprecated: _typing.ClassVar['IpV6AddressStatus'] = 'deprecated'
      invalid: _typing.ClassVar['IpV6AddressStatus'] = 'invalid'
      inaccessible: _typing.ClassVar['IpV6AddressStatus'] = 'inaccessible'
      unknown: _typing.ClassVar['IpV6AddressStatus'] = 'unknown'
      tentative: _typing.ClassVar['IpV6AddressStatus'] = 'tentative'
      duplicate: _typing.ClassVar['IpV6AddressStatus'] = 'duplicate'

   class IpV6Address(pyVmomi.vmodl.DynamicData):
      ipAddress: str
      prefixLength: int
      origin: _typing.Optional[str] = None
      dadState: _typing.Optional[str] = None
      lifetime: _typing.Optional[_datetime.datetime] = None
      operation: _typing.Optional[str] = None

   class IpV6AddressConfiguration(pyVmomi.vmodl.DynamicData):
      ipV6Address: list[IpV6Address] = []
      autoConfigurationEnabled: _typing.Optional[bool] = None
      dhcpV6Enabled: _typing.Optional[bool] = None

   dhcp: bool
   ipAddress: _typing.Optional[str] = None
   subnetMask: _typing.Optional[str] = None
   ipV6Config: _typing.Optional[IpV6AddressConfiguration] = None


class IpRouteConfig(pyVmomi.vmodl.DynamicData):
   defaultGateway: _typing.Optional[str] = None
   gatewayDevice: _typing.Optional[str] = None
   ipV6DefaultGateway: _typing.Optional[str] = None
   ipV6GatewayDevice: _typing.Optional[str] = None


class IpRouteConfigSpec(IpRouteConfig):
   gatewayDeviceConnection: _typing.Optional[VirtualNicConnection] = None
   ipV6GatewayDeviceConnection: _typing.Optional[VirtualNicConnection] = None


class IpRouteEntry(pyVmomi.vmodl.DynamicData):
   network: str
   prefixLength: int
   gateway: str
   deviceName: _typing.Optional[str] = None


class IpRouteOp(pyVmomi.vmodl.DynamicData):
   changeOperation: str
   route: IpRouteEntry


class IpRouteTableConfig(pyVmomi.vmodl.DynamicData):
   ipRoute: list[IpRouteOp] = []
   ipv6Route: list[IpRouteOp] = []


class IpRouteTableInfo(pyVmomi.vmodl.DynamicData):
   ipRoute: list[IpRouteEntry] = []
   ipv6Route: list[IpRouteEntry] = []


class IpmiInfo(pyVmomi.vmodl.DynamicData):
   bmcIpAddress: _typing.Optional[str] = None
   bmcMacAddress: _typing.Optional[str] = None
   login: _typing.Optional[str] = None
   password: _typing.Optional[str] = None


class IscsiManager(pyVmomi.VmomiSupport.ManagedObject):
   class IscsiStatus(pyVmomi.vmodl.DynamicData):
      reason: list[pyVmomi.vmodl.MethodFault] = []

   class IscsiPortInfo(pyVmomi.vmodl.DynamicData):
      class PathStatus(pyVmomi.VmomiSupport.Enum):
         notUsed: _typing.ClassVar['PathStatus'] = 'notUsed'
         active: _typing.ClassVar['PathStatus'] = 'active'
         standBy: _typing.ClassVar['PathStatus'] = 'standBy'
         lastActive: _typing.ClassVar['PathStatus'] = 'lastActive'

      vnicDevice: _typing.Optional[str] = None
      vnic: _typing.Optional[VirtualNic] = None
      pnicDevice: _typing.Optional[str] = None
      pnic: _typing.Optional[PhysicalNic] = None
      switchName: _typing.Optional[str] = None
      switchUuid: _typing.Optional[str] = None
      portgroupName: _typing.Optional[str] = None
      portgroupKey: _typing.Optional[str] = None
      portKey: _typing.Optional[str] = None
      opaqueNetworkId: _typing.Optional[str] = None
      opaqueNetworkType: _typing.Optional[str] = None
      opaqueNetworkName: _typing.Optional[str] = None
      externalId: _typing.Optional[str] = None
      complianceStatus: _typing.Optional[IscsiStatus] = None
      pathStatus: _typing.Optional[str] = None

   class IscsiDependencyEntity(pyVmomi.vmodl.DynamicData):
      pnicDevice: str
      vnicDevice: str
      vmhbaName: str

   class IscsiMigrationDependency(pyVmomi.vmodl.DynamicData):
      migrationAllowed: bool
      disallowReason: _typing.Optional[IscsiStatus] = None
      dependency: list[IscsiDependencyEntity] = []

   def QueryVnicStatus(self, vnicDevice: str) -> IscsiStatus: ...
   def QueryPnicStatus(self, pnicDevice: str) -> IscsiStatus: ...
   def QueryBoundVnics(self, iScsiHbaName: str) -> list[IscsiPortInfo]: ...
   def QueryCandidateNics(self, iScsiHbaName: str) -> list[IscsiPortInfo]: ...
   def BindVnic(self, iScsiHbaName: str, vnicDevice: str) -> None: ...
   def UnbindVnic(self, iScsiHbaName: str, vnicDevice: str, force: bool) -> None: ...
   def QueryMigrationDependencies(self, pnicDevice: list[str]) -> IscsiMigrationDependency: ...


class KernelModuleSystem(pyVmomi.VmomiSupport.ManagedObject):
   class ModuleInfo(pyVmomi.vmodl.DynamicData):
      class SectionInfo(pyVmomi.vmodl.DynamicData):
         address: pyVmomi.VmomiSupport.long
         length: _typing.Optional[int] = None

      id: int
      name: str
      version: str
      filename: str
      optionString: str
      loaded: bool
      enabled: bool
      useCount: int
      readOnlySection: SectionInfo
      writableSection: SectionInfo
      textSection: SectionInfo
      dataSection: SectionInfo
      bssSection: SectionInfo

   def QueryModules(self) -> list[ModuleInfo]: ...
   def UpdateModuleOptionString(self, name: str, options: str) -> None: ...
   def QueryConfiguredModuleOptionString(self, name: str) -> str: ...


class LACPInfo(pyVmomi.vmodl.DynamicData):
   dvsName: str
   lags: list[LAGInfo] = []


class LAGInfo(pyVmomi.vmodl.DynamicData):
   lagName: str
   groupState: int
   vnics: list[str] = []
   uplinks: list[LAGUplinkInfo] = []


class LAGUplinkInfo(pyVmomi.vmodl.DynamicData):
   uplinkName: str
   portState: int
   bundleState: str


class LicenseSpec(pyVmomi.vmodl.DynamicData):
   source: _typing.Optional[pyVmomi.vim.LicenseManager.LicenseSource] = None
   editionKey: _typing.Optional[str] = None
   disabledFeatureKey: list[str] = []
   enabledFeatureKey: list[str] = []


class LinkDiscoveryProtocolConfig(pyVmomi.vmodl.DynamicData):
   class ProtocolType(pyVmomi.VmomiSupport.Enum):
      cdp: _typing.ClassVar['ProtocolType'] = 'cdp'
      lldp: _typing.ClassVar['ProtocolType'] = 'lldp'

   class OperationType(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['OperationType'] = 'none'
      listen: _typing.ClassVar['OperationType'] = 'listen'
      advertise: _typing.ClassVar['OperationType'] = 'advertise'
      both: _typing.ClassVar['OperationType'] = 'both'

   protocol: str
   operation: str


class LocalAccountManager(pyVmomi.VmomiSupport.ManagedObject):
   class AccountSpecification(pyVmomi.vmodl.DynamicData):
      id: str
      password: _typing.Optional[str] = None
      description: _typing.Optional[str] = None

   class PosixAccountSpecification(AccountSpecification):
      posixId: _typing.Optional[int] = None
      shellAccess: _typing.Optional[bool] = None

   def CreateUser(self, user: AccountSpecification) -> None: ...
   def UpdateUser(self, user: AccountSpecification) -> None: ...
   def CreateGroup(self, group: AccountSpecification) -> None: ...
   def RemoveUser(self, userName: str) -> None: ...
   def RemoveGroup(self, groupName: str) -> None: ...
   def AssignUserToGroup(self, user: str, group: str) -> None: ...
   def UnassignUserFromGroup(self, user: str, group: str) -> None: ...
   def ChangePassword(self, user: str, oldPassword: str, newPassword: str) -> None: ...

class LocalAuthentication(AuthenticationStore):
   pass

class LocalAuthenticationInfo(AuthenticationStoreInfo):
   pass


class LocalDatastoreInfo(pyVmomi.vim.Datastore.Info):
   path: _typing.Optional[str] = None


class LocalFileSystemVolume(FileSystemVolume):
   class Specification(pyVmomi.vmodl.DynamicData):
      device: str
      localPath: str

   device: str


class MaintenanceSpec(pyVmomi.vmodl.DynamicData):
   class Purpose(pyVmomi.VmomiSupport.Enum):
      hostUpgrade: _typing.ClassVar['Purpose'] = 'hostUpgrade'

   class EvacuationMode(pyVmomi.vmodl.DynamicData):
      workloadNonDisruptive: bool

   vsanMode: _typing.Optional[pyVmomi.vim.vsan.host.DecommissionMode] = None
   purpose: _typing.Optional[str] = None
   evacMode: _typing.Optional[EvacuationMode] = None


class MemoryManagerSystem(pyVmomi.vim.ExtensibleManagedObject):
   class ServiceConsoleReservationInfo(pyVmomi.vmodl.DynamicData):
      serviceConsoleReservedCfg: pyVmomi.VmomiSupport.long
      serviceConsoleReserved: pyVmomi.VmomiSupport.long
      unreserved: pyVmomi.VmomiSupport.long

   class VirtualMachineReservationInfo(pyVmomi.vmodl.DynamicData):
      class AllocationPolicy(pyVmomi.VmomiSupport.Enum):
         swapNone: _typing.ClassVar['AllocationPolicy'] = 'swapNone'
         swapSome: _typing.ClassVar['AllocationPolicy'] = 'swapSome'
         swapMost: _typing.ClassVar['AllocationPolicy'] = 'swapMost'

      virtualMachineMin: pyVmomi.VmomiSupport.long
      virtualMachineMax: pyVmomi.VmomiSupport.long
      virtualMachineReserved: pyVmomi.VmomiSupport.long
      allocationPolicy: str

   class VirtualMachineReservationSpec(pyVmomi.vmodl.DynamicData):
      virtualMachineReserved: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      allocationPolicy: _typing.Optional[str] = None

   @property
   def consoleReservationInfo(self) -> _typing.Optional[ServiceConsoleReservationInfo]: ...
   @property
   def virtualMachineReservationInfo(self) -> _typing.Optional[VirtualMachineReservationInfo]: ...

   def ReconfigureServiceConsoleReservation(self, cfgBytes: pyVmomi.VmomiSupport.long) -> None: ...
   def ReconfigureVirtualMachineReservation(self, spec: VirtualMachineReservationSpec) -> None: ...


class MemorySpec(pyVmomi.vmodl.DynamicData):
   serviceConsoleReservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None

class MemoryTierFlags:
   pass


class MemoryTierInfo(pyVmomi.vmodl.DynamicData):
   name: str
   type: str
   flags: list[str] = []
   internalFlags: list[str] = []
   size: pyVmomi.VmomiSupport.long

class MemoryTierType:
   pass

class MemoryTieringType:
   pass


class MessageBusProxy(pyVmomi.VmomiSupport.ManagedObject):
   pass


class MountInfo(pyVmomi.vmodl.DynamicData):
   class AccessMode(pyVmomi.VmomiSupport.Enum):
      readWrite: _typing.ClassVar['AccessMode'] = 'readWrite'
      readOnly: _typing.ClassVar['AccessMode'] = 'readOnly'

   class InaccessibleReason(pyVmomi.VmomiSupport.Enum):
      AllPathsDown_Start: _typing.ClassVar['InaccessibleReason'] = 'AllPathsDown_Start'
      AllPathsDown_Timeout: _typing.ClassVar['InaccessibleReason'] = 'AllPathsDown_Timeout'
      PermanentDeviceLoss: _typing.ClassVar['InaccessibleReason'] = 'PermanentDeviceLoss'

   class MountFailedReason(pyVmomi.VmomiSupport.Enum):
      CONNECT_FAILURE: _typing.ClassVar['MountFailedReason'] = 'CONNECT_FAILURE'
      MOUNT_NOT_SUPPORTED: _typing.ClassVar['MountFailedReason'] = 'MOUNT_NOT_SUPPORTED'
      NFS_NOT_SUPPORTED: _typing.ClassVar['MountFailedReason'] = 'NFS_NOT_SUPPORTED'
      MOUNT_DENIED: _typing.ClassVar['MountFailedReason'] = 'MOUNT_DENIED'
      MOUNT_NOT_DIR: _typing.ClassVar['MountFailedReason'] = 'MOUNT_NOT_DIR'
      VOLUME_LIMIT_EXCEEDED: _typing.ClassVar['MountFailedReason'] = 'VOLUME_LIMIT_EXCEEDED'
      CONN_LIMIT_EXCEEDED: _typing.ClassVar['MountFailedReason'] = 'CONN_LIMIT_EXCEEDED'
      MOUNT_EXISTS: _typing.ClassVar['MountFailedReason'] = 'MOUNT_EXISTS'
      OTHERS: _typing.ClassVar['MountFailedReason'] = 'OTHERS'

   path: _typing.Optional[str] = None
   accessMode: str
   mounted: _typing.Optional[bool] = None
   accessible: _typing.Optional[bool] = None
   inaccessibleReason: _typing.Optional[str] = None
   vmknicName: _typing.Optional[str] = None
   vmknicActive: _typing.Optional[bool] = None
   mountFailedReason: _typing.Optional[str] = None
   numTcpConnections: _typing.Optional[int] = None


class MultipathInfo(pyVmomi.vmodl.DynamicData):
   class PathState(pyVmomi.VmomiSupport.Enum):
      standby: _typing.ClassVar['PathState'] = 'standby'
      active: _typing.ClassVar['PathState'] = 'active'
      disabled: _typing.ClassVar['PathState'] = 'disabled'
      dead: _typing.ClassVar['PathState'] = 'dead'
      unknown: _typing.ClassVar['PathState'] = 'unknown'

   class LogicalUnitPolicy(pyVmomi.vmodl.DynamicData):
      policy: str

   class HppLogicalUnitPolicy(LogicalUnitPolicy):
      bytes: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      iops: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      path: _typing.Optional[str] = None
      latencyEvalTime: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      samplingIosPerPath: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class LogicalUnitStorageArrayTypePolicy(pyVmomi.vmodl.DynamicData):
      policy: str

   class FixedLogicalUnitPolicy(LogicalUnitPolicy):
      prefer: str

   class LogicalUnit(pyVmomi.vmodl.DynamicData):
      key: str
      id: str
      lun: ScsiLun
      path: list[Path] = []
      policy: LogicalUnitPolicy
      storageArrayTypePolicy: _typing.Optional[LogicalUnitStorageArrayTypePolicy] = None

   class Path(pyVmomi.vmodl.DynamicData):
      key: str
      name: str
      pathState: str
      state: _typing.Optional[str] = None
      isWorkingPath: _typing.Optional[bool] = None
      adapter: HostBusAdapter
      lun: LogicalUnit
      transport: _typing.Optional[TargetTransport] = None

   lun: list[LogicalUnit] = []


class MultipathStateInfo(pyVmomi.vmodl.DynamicData):
   class Path(pyVmomi.vmodl.DynamicData):
      name: str
      pathState: str

   path: list[Path] = []


class NasDatastoreInfo(pyVmomi.vim.Datastore.Info):
   nas: _typing.Optional[NasVolume] = None


class NasVolume(FileSystemVolume):
   class UserInfo(pyVmomi.vmodl.DynamicData):
      user: str

   class SecurityType(pyVmomi.VmomiSupport.Enum):
      AUTH_SYS: _typing.ClassVar['SecurityType'] = 'AUTH_SYS'
      SEC_KRB5: _typing.ClassVar['SecurityType'] = 'SEC_KRB5'
      SEC_KRB5I: _typing.ClassVar['SecurityType'] = 'SEC_KRB5I'
      SEC_KRB5P: _typing.ClassVar['SecurityType'] = 'SEC_KRB5P'

   class Specification(pyVmomi.vmodl.DynamicData):
      remoteHost: str
      remotePath: str
      localPath: str
      accessMode: str
      type: _typing.Optional[str] = None
      userName: _typing.Optional[str] = None
      password: _typing.Optional[str] = None
      remoteHostNames: list[str] = []
      securityType: _typing.Optional[str] = None
      vmknicToBind: _typing.Optional[str] = None
      vmknicBound: _typing.Optional[bool] = None
      connections: _typing.Optional[int] = None

   class Config(pyVmomi.vmodl.DynamicData):
      changeOperation: _typing.Optional[str] = None
      spec: _typing.Optional[Specification] = None

   remoteHost: str
   remotePath: str
   userName: _typing.Optional[str] = None
   remoteHostNames: list[str] = []
   securityType: _typing.Optional[str] = None
   protocolEndpoint: _typing.Optional[bool] = None


class NatService(pyVmomi.vmodl.DynamicData):
   class PortForwardSpecification(pyVmomi.vmodl.DynamicData):
      type: str
      name: str
      hostPort: int
      guestPort: int
      guestIpAddress: str

   class NameServiceSpec(pyVmomi.vmodl.DynamicData):
      dnsAutoDetect: bool
      dnsPolicy: str
      dnsRetries: int
      dnsTimeout: int
      dnsNameServer: list[str] = []
      nbdsTimeout: int
      nbnsRetries: int
      nbnsTimeout: int

   class Specification(pyVmomi.vmodl.DynamicData):
      virtualSwitch: str
      activeFtp: bool
      allowAnyOui: bool
      configPort: bool
      ipGatewayAddress: str
      udpTimeout: int
      portForward: list[PortForwardSpecification] = []
      nameService: _typing.Optional[NameServiceSpec] = None

   class Config(pyVmomi.vmodl.DynamicData):
      changeOperation: _typing.Optional[str] = None
      key: str
      spec: Specification

   key: str
   spec: Specification


class NetCapabilities(pyVmomi.vmodl.DynamicData):
   canSetPhysicalNicLinkSpeed: bool
   supportsNicTeaming: bool
   nicTeamingPolicy: list[str] = []
   supportsVlan: bool
   usesServiceConsoleNic: bool
   supportsNetworkHints: bool
   maxPortGroupsPerVswitch: _typing.Optional[int] = None
   vswitchConfigSupported: bool
   vnicConfigSupported: bool
   ipRouteConfigSupported: bool
   dnsConfigSupported: bool
   dhcpOnVnicSupported: bool
   ipV6Supported: bool
   backupNfcNiocSupported: _typing.Optional[bool] = None


class NetOffloadCapabilities(pyVmomi.vmodl.DynamicData):
   csumOffload: _typing.Optional[bool] = None
   tcpSegmentation: _typing.Optional[bool] = None
   zeroCopyXmit: _typing.Optional[bool] = None


class NetStackInstance(pyVmomi.vmodl.DynamicData):
   class SystemStackKey(pyVmomi.VmomiSupport.Enum):
      defaultTcpipStack: _typing.ClassVar['SystemStackKey'] = 'defaultTcpipStack'
      vmotion: _typing.ClassVar['SystemStackKey'] = 'vmotion'
      vSphereProvisioning: _typing.ClassVar['SystemStackKey'] = 'vSphereProvisioning'
      mirror: _typing.ClassVar['SystemStackKey'] = 'mirror'
      ops: _typing.ClassVar['SystemStackKey'] = 'ops'
      vnetworking: _typing.ClassVar['SystemStackKey'] = 'vnetworking'

   class CongestionControlAlgorithmType(pyVmomi.VmomiSupport.Enum):
      newreno: _typing.ClassVar['CongestionControlAlgorithmType'] = 'newreno'
      cubic: _typing.ClassVar['CongestionControlAlgorithmType'] = 'cubic'

   key: _typing.Optional[str] = None
   name: _typing.Optional[str] = None
   dnsConfig: _typing.Optional[DnsConfig] = None
   ipRouteConfig: _typing.Optional[IpRouteConfig] = None
   requestedMaxNumberOfConnections: _typing.Optional[int] = None
   congestionControlAlgorithm: _typing.Optional[str] = None
   ipV6Enabled: _typing.Optional[bool] = None
   routeTableConfig: _typing.Optional[IpRouteTableConfig] = None
   owner: _typing.Optional[str] = None


class NetworkConfig(pyVmomi.vmodl.DynamicData):
   class Result(pyVmomi.vmodl.DynamicData):
      vnicDevice: list[str] = []
      consoleVnicDevice: list[str] = []

   class NetStackSpec(pyVmomi.vmodl.DynamicData):
      netStackInstance: NetStackInstance
      operation: _typing.Optional[str] = None

   vswitch: list[VirtualSwitch.Config] = []
   proxySwitch: list[HostProxySwitch.Config] = []
   portgroup: list[PortGroup.Config] = []
   pnic: list[PhysicalNic.Config] = []
   vnic: list[VirtualNic.Config] = []
   consoleVnic: list[VirtualNic.Config] = []
   dnsConfig: _typing.Optional[DnsConfig] = None
   ipRouteConfig: _typing.Optional[IpRouteConfig] = None
   consoleIpRouteConfig: _typing.Optional[IpRouteConfig] = None
   routeTableConfig: _typing.Optional[IpRouteTableConfig] = None
   dhcp: list[DhcpService.Config] = []
   nat: list[NatService.Config] = []
   ipV6Enabled: _typing.Optional[bool] = None
   netStackSpec: list[NetStackSpec] = []
   migrationStatus: _typing.Optional[str] = None


class NetworkInfo(pyVmomi.vmodl.DynamicData):
   vswitch: list[VirtualSwitch] = []
   proxySwitch: list[HostProxySwitch] = []
   portgroup: list[PortGroup] = []
   pnic: list[PhysicalNic] = []
   rdmaDevice: list[RdmaDevice] = []
   vnic: list[VirtualNic] = []
   consoleVnic: list[VirtualNic] = []
   dnsConfig: _typing.Optional[DnsConfig] = None
   ipRouteConfig: _typing.Optional[IpRouteConfig] = None
   consoleIpRouteConfig: _typing.Optional[IpRouteConfig] = None
   routeTableInfo: _typing.Optional[IpRouteTableInfo] = None
   dhcp: list[DhcpService] = []
   nat: list[NatService] = []
   ipV6Enabled: _typing.Optional[bool] = None
   atBootIpV6Enabled: _typing.Optional[bool] = None
   netStackInstance: list[NetStackInstance] = []
   opaqueSwitch: list[OpaqueSwitch] = []
   opaqueNetwork: list[OpaqueNetworkInfo] = []
   nsxTransportNodeId: _typing.Optional[str] = None
   nvdsToVdsMigrationRequired: _typing.Optional[bool] = None
   migrationStatus: _typing.Optional[str] = None


class NetworkPolicy(pyVmomi.vmodl.DynamicData):
   class SecurityPolicy(pyVmomi.vmodl.DynamicData):
      allowPromiscuous: _typing.Optional[bool] = None
      macChanges: _typing.Optional[bool] = None
      forgedTransmits: _typing.Optional[bool] = None

   class TrafficShapingPolicy(pyVmomi.vmodl.DynamicData):
      enabled: _typing.Optional[bool] = None
      averageBandwidth: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      peakBandwidth: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      burstSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class NicFailureCriteria(pyVmomi.vmodl.DynamicData):
      checkSpeed: _typing.Optional[str] = None
      speed: _typing.Optional[int] = None
      checkDuplex: _typing.Optional[bool] = None
      fullDuplex: _typing.Optional[bool] = None
      checkErrorPercent: _typing.Optional[bool] = None
      percentage: _typing.Optional[int] = None
      checkBeacon: _typing.Optional[bool] = None

   class NicOrderPolicy(pyVmomi.vmodl.DynamicData):
      activeNic: list[str] = []
      standbyNic: list[str] = []

   class NicTeamingPolicy(pyVmomi.vmodl.DynamicData):
      policy: _typing.Optional[str] = None
      reversePolicy: _typing.Optional[bool] = None
      notifySwitches: _typing.Optional[bool] = None
      rollingOrder: _typing.Optional[bool] = None
      failureCriteria: _typing.Optional[NicFailureCriteria] = None
      nicOrder: _typing.Optional[NicOrderPolicy] = None

   security: _typing.Optional[SecurityPolicy] = None
   nicTeaming: _typing.Optional[NicTeamingPolicy] = None
   offloadPolicy: _typing.Optional[NetOffloadCapabilities] = None
   shapingPolicy: _typing.Optional[TrafficShapingPolicy] = None


class NetworkSystem(pyVmomi.vim.ExtensibleManagedObject):
   @property
   def capabilities(self) -> _typing.Optional[NetCapabilities]: ...
   @property
   def networkInfo(self) -> _typing.Optional[NetworkInfo]: ...
   @property
   def offloadCapabilities(self) -> _typing.Optional[NetOffloadCapabilities]: ...
   @property
   def networkConfig(self) -> _typing.Optional[NetworkConfig]: ...
   @property
   def dnsConfig(self) -> _typing.Optional[DnsConfig]: ...
   @property
   def ipRouteConfig(self) -> _typing.Optional[IpRouteConfig]: ...
   @property
   def consoleIpRouteConfig(self) -> _typing.Optional[IpRouteConfig]: ...

   def UpdateNetworkConfig(self, config: NetworkConfig, changeMode: str) -> NetworkConfig.Result: ...
   def UpdateDnsConfig(self, config: DnsConfig) -> None: ...
   def UpdateIpRouteConfig(self, config: IpRouteConfig) -> None: ...
   def UpdateConsoleIpRouteConfig(self, config: IpRouteConfig) -> None: ...
   def UpdateIpRouteTableConfig(self, config: IpRouteTableConfig) -> None: ...
   def AddVirtualSwitch(self, vswitchName: str, spec: _typing.Optional[VirtualSwitch.Specification]) -> None: ...
   def RemoveVirtualSwitch(self, vswitchName: str) -> None: ...
   def UpdateVirtualSwitch(self, vswitchName: str, spec: VirtualSwitch.Specification) -> None: ...
   def AddPortGroup(self, portgrp: PortGroup.Specification) -> None: ...
   def RemovePortGroup(self, pgName: str) -> None: ...
   def UpdatePortGroup(self, pgName: str, portgrp: PortGroup.Specification) -> None: ...
   def UpdatePhysicalNicLinkSpeed(self, device: str, linkSpeed: _typing.Optional[PhysicalNic.LinkSpeedDuplex]) -> None: ...
   def QueryNetworkHint(self, device: list[str]) -> list[PhysicalNic.NetworkHint]: ...
   def AddVirtualNic(self, portgroup: str, nic: VirtualNic.Specification) -> str: ...
   def RemoveVirtualNic(self, device: str) -> None: ...
   def UpdateVirtualNic(self, device: str, nic: VirtualNic.Specification) -> None: ...
   def AddServiceConsoleVirtualNic(self, portgroup: str, nic: VirtualNic.Specification) -> str: ...
   def RemoveServiceConsoleVirtualNic(self, device: str) -> None: ...
   def UpdateServiceConsoleVirtualNic(self, device: str, nic: VirtualNic.Specification) -> None: ...
   def RestartServiceConsoleVirtualNic(self, device: str) -> None: ...
   def Refresh(self) -> None: ...
   def StartDpuFailover(self, dvsName: str, targetDpuAlias: _typing.Optional[str]) -> None: ...


class NfcConnectionInfo(DataTransportConnectionInfo):
   streamingMemoryConsumed: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class NtpConfig(pyVmomi.vmodl.DynamicData):
   server: list[str] = []
   configFile: list[str] = []


class NumaInfo(pyVmomi.vmodl.DynamicData):
   type: str
   numNodes: int
   numaNode: list[NumaNode] = []


class NumaNode(pyVmomi.vmodl.DynamicData):
   typeId: pyVmomi.VmomiSupport.byte
   cpuID: list[pyVmomi.VmomiSupport.short] = []
   memorySize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   memoryRangeBegin: pyVmomi.VmomiSupport.long
   memoryRangeLength: pyVmomi.VmomiSupport.long
   pciId: list[str] = []


class NumericSensorInfo(pyVmomi.vmodl.DynamicData):
   class HealthState(pyVmomi.VmomiSupport.Enum):
      unknown: _typing.ClassVar['HealthState'] = 'unknown'
      green: _typing.ClassVar['HealthState'] = 'green'
      yellow: _typing.ClassVar['HealthState'] = 'yellow'
      red: _typing.ClassVar['HealthState'] = 'red'

   class SensorType(pyVmomi.VmomiSupport.Enum):
      fan: _typing.ClassVar['SensorType'] = 'fan'
      power: _typing.ClassVar['SensorType'] = 'power'
      temperature: _typing.ClassVar['SensorType'] = 'temperature'
      voltage: _typing.ClassVar['SensorType'] = 'voltage'
      other: _typing.ClassVar['SensorType'] = 'other'
      processor: _typing.ClassVar['SensorType'] = 'processor'
      memory: _typing.ClassVar['SensorType'] = 'memory'
      storage: _typing.ClassVar['SensorType'] = 'storage'
      systemBoard: _typing.ClassVar['SensorType'] = 'systemBoard'
      battery: _typing.ClassVar['SensorType'] = 'battery'
      bios: _typing.ClassVar['SensorType'] = 'bios'
      cable: _typing.ClassVar['SensorType'] = 'cable'
      watchdog: _typing.ClassVar['SensorType'] = 'watchdog'

   name: str
   healthState: _typing.Optional[pyVmomi.vim.ElementDescription] = None
   currentReading: pyVmomi.VmomiSupport.long
   unitModifier: int
   baseUnits: str
   rateUnits: _typing.Optional[str] = None
   sensorType: str
   id: _typing.Optional[str] = None
   sensorNumber: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   timeStamp: _typing.Optional[str] = None
   fru: _typing.Optional[Fru] = None


class NvdimmSystem(pyVmomi.VmomiSupport.ManagedObject):
   class RangeType(pyVmomi.VmomiSupport.Enum):
      volatileRange: _typing.ClassVar['RangeType'] = 'volatileRange'
      persistentRange: _typing.ClassVar['RangeType'] = 'persistentRange'
      controlRange: _typing.ClassVar['RangeType'] = 'controlRange'
      blockRange: _typing.ClassVar['RangeType'] = 'blockRange'
      volatileVirtualDiskRange: _typing.ClassVar['RangeType'] = 'volatileVirtualDiskRange'
      volatileVirtualCDRange: _typing.ClassVar['RangeType'] = 'volatileVirtualCDRange'
      persistentVirtualDiskRange: _typing.ClassVar['RangeType'] = 'persistentVirtualDiskRange'
      persistentVirtualCDRange: _typing.ClassVar['RangeType'] = 'persistentVirtualCDRange'

   class NamespaceType(pyVmomi.VmomiSupport.Enum):
      blockNamespace: _typing.ClassVar['NamespaceType'] = 'blockNamespace'
      persistentNamespace: _typing.ClassVar['NamespaceType'] = 'persistentNamespace'

   class HealthInfo(pyVmomi.vmodl.DynamicData):
      class StateFlag(pyVmomi.VmomiSupport.Enum):
         normal: _typing.ClassVar['StateFlag'] = 'normal'
         error: _typing.ClassVar['StateFlag'] = 'error'

      healthStatus: str
      healthInformation: str
      stateFlagInfo: list[str] = []
      dimmTemperature: int
      dimmTemperatureThreshold: int
      spareBlocksPercentage: int
      spareBlockThreshold: int
      dimmLifespanPercentage: int
      esTemperature: _typing.Optional[int] = None
      esTemperatureThreshold: _typing.Optional[int] = None
      esLifespanPercentage: _typing.Optional[int] = None

   class RegionInfo(pyVmomi.vmodl.DynamicData):
      regionId: int
      setId: int
      rangeType: str
      startAddr: pyVmomi.VmomiSupport.long
      size: pyVmomi.VmomiSupport.long
      offset: pyVmomi.VmomiSupport.long

   class Summary(pyVmomi.vmodl.DynamicData):
      numDimms: int
      healthStatus: str
      totalCapacity: pyVmomi.VmomiSupport.long
      persistentCapacity: pyVmomi.VmomiSupport.long
      blockCapacity: pyVmomi.VmomiSupport.long
      availableCapacity: pyVmomi.VmomiSupport.long
      numInterleavesets: int
      numNamespaces: int

   class DimmInfo(pyVmomi.vmodl.DynamicData):
      dimmHandle: int
      healthInfo: HealthInfo
      totalCapacity: pyVmomi.VmomiSupport.long
      persistentCapacity: pyVmomi.VmomiSupport.long
      availablePersistentCapacity: pyVmomi.VmomiSupport.long
      volatileCapacity: pyVmomi.VmomiSupport.long
      availableVolatileCapacity: pyVmomi.VmomiSupport.long
      blockCapacity: pyVmomi.VmomiSupport.long
      regionInfo: list[RegionInfo] = []
      representationString: str

   class InterleaveSetInfo(pyVmomi.vmodl.DynamicData):
      class InterleaveSetState(pyVmomi.VmomiSupport.Enum):
         invalid: _typing.ClassVar['InterleaveSetState'] = 'invalid'
         active: _typing.ClassVar['InterleaveSetState'] = 'active'

      setId: int
      rangeType: str
      baseAddress: pyVmomi.VmomiSupport.long
      size: pyVmomi.VmomiSupport.long
      availableSize: pyVmomi.VmomiSupport.long
      deviceList: list[int] = []
      state: str

   class Guid(pyVmomi.vmodl.DynamicData):
      uuid: str

   class NamespaceInfo(pyVmomi.vmodl.DynamicData):
      class NamespaceHealthStatus(pyVmomi.VmomiSupport.Enum):
         normal: _typing.ClassVar['NamespaceHealthStatus'] = 'normal'
         missing: _typing.ClassVar['NamespaceHealthStatus'] = 'missing'
         labelMissing: _typing.ClassVar['NamespaceHealthStatus'] = 'labelMissing'
         interleaveBroken: _typing.ClassVar['NamespaceHealthStatus'] = 'interleaveBroken'
         labelInconsistent: _typing.ClassVar['NamespaceHealthStatus'] = 'labelInconsistent'
         bttCorrupt: _typing.ClassVar['NamespaceHealthStatus'] = 'bttCorrupt'
         badBlockSize: _typing.ClassVar['NamespaceHealthStatus'] = 'badBlockSize'

      class NamespaceState(pyVmomi.VmomiSupport.Enum):
         invalid: _typing.ClassVar['NamespaceState'] = 'invalid'
         notInUse: _typing.ClassVar['NamespaceState'] = 'notInUse'
         inUse: _typing.ClassVar['NamespaceState'] = 'inUse'

      uuid: str
      friendlyName: str
      blockSize: pyVmomi.VmomiSupport.long
      blockCount: pyVmomi.VmomiSupport.long
      type: str
      namespaceHealthStatus: str
      locationID: int
      state: str

   class NamespaceDetails(pyVmomi.vmodl.DynamicData):
      class NamespaceHealthStatus(pyVmomi.VmomiSupport.Enum):
         normal: _typing.ClassVar['NamespaceHealthStatus'] = 'normal'
         missing: _typing.ClassVar['NamespaceHealthStatus'] = 'missing'
         labelMissing: _typing.ClassVar['NamespaceHealthStatus'] = 'labelMissing'
         interleaveBroken: _typing.ClassVar['NamespaceHealthStatus'] = 'interleaveBroken'
         labelInconsistent: _typing.ClassVar['NamespaceHealthStatus'] = 'labelInconsistent'

      class NamespaceState(pyVmomi.VmomiSupport.Enum):
         invalid: _typing.ClassVar['NamespaceState'] = 'invalid'
         notInUse: _typing.ClassVar['NamespaceState'] = 'notInUse'
         inUse: _typing.ClassVar['NamespaceState'] = 'inUse'

      uuid: str
      friendlyName: str
      size: pyVmomi.VmomiSupport.long
      type: str
      namespaceHealthStatus: str
      interleavesetID: int
      state: str

   class NamespaceCreateSpec(pyVmomi.vmodl.DynamicData):
      friendlyName: _typing.Optional[str] = None
      blockSize: pyVmomi.VmomiSupport.long
      blockCount: pyVmomi.VmomiSupport.long
      type: str
      locationID: int

   class PMemNamespaceCreateSpec(pyVmomi.vmodl.DynamicData):
      friendlyName: _typing.Optional[str] = None
      size: pyVmomi.VmomiSupport.long
      interleavesetID: int

   class NamespaceDeleteSpec(pyVmomi.vmodl.DynamicData):
      uuid: str

   class NvdimmSystemInfo(pyVmomi.vmodl.DynamicData):
      summary: _typing.Optional[Summary] = None
      dimms: list[int] = []
      dimmInfo: list[DimmInfo] = []
      interleaveSet: list[int] = []
      iSetInfo: list[InterleaveSetInfo] = []
      namespace: list[Guid] = []
      nsInfo: list[NamespaceInfo] = []
      nsDetails: list[NamespaceDetails] = []

   @property
   def nvdimmSystemInfo(self) -> NvdimmSystemInfo: ...

   def CreateNamespace(self, createSpec: NamespaceCreateSpec) -> pyVmomi.vim.Task: ...
   def CreatePMemNamespace(self, createSpec: PMemNamespaceCreateSpec) -> pyVmomi.vim.Task: ...
   def DeleteNamespace(self, deleteSpec: NamespaceDeleteSpec) -> pyVmomi.vim.Task: ...
   def DeleteBlockNamespaces(self) -> pyVmomi.vim.Task: ...


class NvmeConnectSpec(NvmeSpec):
   subnqn: str
   controllerId: _typing.Optional[int] = None
   adminQueueSize: _typing.Optional[int] = None
   keepAliveTimeout: _typing.Optional[int] = None


class NvmeController(pyVmomi.vmodl.DynamicData):
   key: str
   controllerNumber: int
   subnqn: str
   name: str
   associatedAdapter: HostBusAdapter
   transportType: str
   fusedOperationSupported: bool
   numberOfQueues: int
   queueSize: int
   attachedNamespace: list[NvmeNamespace] = []
   vendorId: _typing.Optional[str] = None
   model: _typing.Optional[str] = None
   serialNumber: _typing.Optional[str] = None
   firmwareVersion: _typing.Optional[str] = None


class NvmeDisconnectSpec(pyVmomi.vmodl.DynamicData):
   hbaName: str
   subnqn: _typing.Optional[str] = None
   controllerNumber: _typing.Optional[int] = None


class NvmeDiscoverSpec(NvmeSpec):
   autoConnect: _typing.Optional[bool] = None
   rootDiscoveryController: _typing.Optional[bool] = None


class NvmeDiscoveryLog(pyVmomi.vmodl.DynamicData):
   class SubsystemType(pyVmomi.VmomiSupport.Enum):
      discovery: _typing.ClassVar['SubsystemType'] = 'discovery'
      nvm: _typing.ClassVar['SubsystemType'] = 'nvm'

   class TransportRequirements(pyVmomi.VmomiSupport.Enum):
      secureChannelRequired: _typing.ClassVar['TransportRequirements'] = 'secureChannelRequired'
      secureChannelNotRequired: _typing.ClassVar['TransportRequirements'] = 'secureChannelNotRequired'
      requirementsNotSpecified: _typing.ClassVar['TransportRequirements'] = 'requirementsNotSpecified'

   class Entry(pyVmomi.vmodl.DynamicData):
      subnqn: str
      subsystemType: str
      subsystemPortId: int
      controllerId: int
      adminQueueMaxSize: int
      transportParameters: NvmeTransportParameters
      transportRequirements: str
      connected: bool

   entry: list[Entry] = []
   complete: bool


class NvmeNamespace(pyVmomi.vmodl.DynamicData):
   key: str
   name: str
   id: int
   blockSize: int
   capacityInBlocks: pyVmomi.VmomiSupport.long


class NvmeOpaqueTransportParameters(NvmeTransportParameters):
   trtype: str
   traddr: str
   adrfam: str
   trsvcid: str
   tsas: pyVmomi.VmomiSupport.binary


class NvmeOverFibreChannelParameters(NvmeTransportParameters):
   nodeWorldWideName: pyVmomi.VmomiSupport.long
   portWorldWideName: pyVmomi.VmomiSupport.long


class NvmeOverRdmaParameters(NvmeTransportParameters):
   address: str
   addressFamily: _typing.Optional[str] = None
   portNumber: _typing.Optional[int] = None


class NvmeOverTcpParameters(NvmeTransportParameters):
   address: str
   portNumber: _typing.Optional[int] = None
   digestVerification: _typing.Optional[str] = None


class NvmeSpec(pyVmomi.vmodl.DynamicData):
   hbaName: str
   transportParameters: NvmeTransportParameters


class NvmeTopology(pyVmomi.vmodl.DynamicData):
   class Interface(pyVmomi.vmodl.DynamicData):
      key: str
      adapter: HostBusAdapter
      connectedController: list[NvmeController] = []

   adapter: list[Interface] = []


class NvmeTransportParameters(pyVmomi.vmodl.DynamicData):
   class NvmeAddressFamily(pyVmomi.VmomiSupport.Enum):
      ipv4: _typing.ClassVar['NvmeAddressFamily'] = 'ipv4'
      ipv6: _typing.ClassVar['NvmeAddressFamily'] = 'ipv6'
      infiniBand: _typing.ClassVar['NvmeAddressFamily'] = 'infiniBand'
      fc: _typing.ClassVar['NvmeAddressFamily'] = 'fc'
      loopback: _typing.ClassVar['NvmeAddressFamily'] = 'loopback'
      unknown: _typing.ClassVar['NvmeAddressFamily'] = 'unknown'

class NvmeTransportType:
   pass


class OpaqueNetworkInfo(pyVmomi.vmodl.DynamicData):
   opaqueNetworkId: str
   opaqueNetworkName: str
   opaqueNetworkType: str
   pnicZone: list[str] = []
   capability: _typing.Optional[pyVmomi.vim.OpaqueNetwork.Capability] = None
   extraConfig: list[pyVmomi.vim.option.OptionValue] = []


class OpaqueSwitch(pyVmomi.vmodl.DynamicData):
   class OpaqueSwitchState(pyVmomi.VmomiSupport.Enum):
      up: _typing.ClassVar['OpaqueSwitchState'] = 'up'
      warning: _typing.ClassVar['OpaqueSwitchState'] = 'warning'
      down: _typing.ClassVar['OpaqueSwitchState'] = 'down'
      maintenance: _typing.ClassVar['OpaqueSwitchState'] = 'maintenance'

   class PhysicalNicZone(pyVmomi.vmodl.DynamicData):
      key: str
      pnicDevice: list[str] = []

   key: str
   name: _typing.Optional[str] = None
   pnic: list[PhysicalNic] = []
   pnicZone: list[PhysicalNicZone] = []
   status: _typing.Optional[str] = None
   vtep: list[VirtualNic] = []
   extraConfig: list[pyVmomi.vim.option.OptionValue] = []
   featureCapability: list[FeatureCapability] = []


class PMemDatastoreInfo(pyVmomi.vim.Datastore.Info):
   pmem: PMemVolume

class PMemVolume(FileSystemVolume):
   uuid: str
   version: str

class ParallelScsiHba(HostBusAdapter):
   pass

class ParallelScsiTargetTransport(TargetTransport):
   pass

class PartialMaintenanceModeId:
   pass


class PartialMaintenanceModeRuntimeInfo(pyVmomi.vmodl.DynamicData):
   key: str
   hostStatus: str

class PartialMaintenanceModeStatus:
   pass


class PatchManager(pyVmomi.VmomiSupport.ManagedObject):
   class Result(pyVmomi.vmodl.DynamicData):
      version: str
      status: list[Status] = []
      xmlResult: _typing.Optional[str] = None

   class Status(pyVmomi.vmodl.DynamicData):
      class Reason(pyVmomi.VmomiSupport.Enum):
         obsoleted: _typing.ClassVar['Reason'] = 'obsoleted'
         missingPatch: _typing.ClassVar['Reason'] = 'missingPatch'
         missingLib: _typing.ClassVar['Reason'] = 'missingLib'
         hasDependentPatch: _typing.ClassVar['Reason'] = 'hasDependentPatch'
         conflictPatch: _typing.ClassVar['Reason'] = 'conflictPatch'
         conflictLib: _typing.ClassVar['Reason'] = 'conflictLib'

      class Integrity(pyVmomi.VmomiSupport.Enum):
         validated: _typing.ClassVar['Integrity'] = 'validated'
         keyNotFound: _typing.ClassVar['Integrity'] = 'keyNotFound'
         keyRevoked: _typing.ClassVar['Integrity'] = 'keyRevoked'
         keyExpired: _typing.ClassVar['Integrity'] = 'keyExpired'
         digestMismatch: _typing.ClassVar['Integrity'] = 'digestMismatch'
         notEnoughSignatures: _typing.ClassVar['Integrity'] = 'notEnoughSignatures'
         validationError: _typing.ClassVar['Integrity'] = 'validationError'

      class InstallState(pyVmomi.VmomiSupport.Enum):
         hostRestarted: _typing.ClassVar['InstallState'] = 'hostRestarted'
         imageActive: _typing.ClassVar['InstallState'] = 'imageActive'

      class PrerequisitePatch(pyVmomi.vmodl.DynamicData):
         id: str
         installState: list[str] = []

      id: str
      applicable: bool
      reason: list[str] = []
      integrity: _typing.Optional[str] = None
      installed: bool
      installState: list[str] = []
      prerequisitePatch: list[PrerequisitePatch] = []
      restartRequired: bool
      reconnectRequired: bool
      vmOffRequired: bool
      supersededPatchIds: list[str] = []

   class Locator(pyVmomi.vmodl.DynamicData):
      url: str
      proxy: _typing.Optional[str] = None

   class PatchManagerOperationSpec(pyVmomi.vmodl.DynamicData):
      proxy: _typing.Optional[str] = None
      port: _typing.Optional[int] = None
      userName: _typing.Optional[str] = None
      password: _typing.Optional[str] = None
      cmdOption: _typing.Optional[str] = None

   def Check(self, metaUrls: list[str], bundleUrls: list[str], spec: _typing.Optional[PatchManagerOperationSpec]) -> pyVmomi.vim.Task: ...
   def Scan(self, repository: Locator, updateID: list[str]) -> pyVmomi.vim.Task: ...
   def ScanV2(self, metaUrls: list[str], bundleUrls: list[str], spec: _typing.Optional[PatchManagerOperationSpec]) -> pyVmomi.vim.Task: ...
   def Stage(self, metaUrls: list[str], bundleUrls: list[str], vibUrls: list[str], spec: _typing.Optional[PatchManagerOperationSpec]) -> pyVmomi.vim.Task: ...
   def Install(self, repository: Locator, updateID: str, force: _typing.Optional[bool]) -> pyVmomi.vim.Task: ...
   def InstallV2(self, metaUrls: list[str], bundleUrls: list[str], vibUrls: list[str], spec: _typing.Optional[PatchManagerOperationSpec]) -> pyVmomi.vim.Task: ...
   def Uninstall(self, bulletinIds: list[str], spec: _typing.Optional[PatchManagerOperationSpec]) -> pyVmomi.vim.Task: ...
   def Query(self, spec: _typing.Optional[PatchManagerOperationSpec]) -> pyVmomi.vim.Task: ...


class PathSelectionPolicyOption(pyVmomi.vmodl.DynamicData):
   policy: pyVmomi.vim.ElementDescription


class PciDevice(pyVmomi.vmodl.DynamicData):
   class DirectPathInfo(pyVmomi.vmodl.DynamicData):
      interconnectType: _typing.Optional[str] = None
      driverName: _typing.Optional[str] = None
      driverVersion: _typing.Optional[str] = None
      availableMemory: _typing.Optional[int] = None

   id: str
   classId: pyVmomi.VmomiSupport.short
   bus: pyVmomi.VmomiSupport.byte
   slot: pyVmomi.VmomiSupport.byte
   physicalSlot: _typing.Optional[int] = None
   slotDescription: _typing.Optional[str] = None
   function: pyVmomi.VmomiSupport.byte
   vendorId: pyVmomi.VmomiSupport.short
   subVendorId: pyVmomi.VmomiSupport.short
   vendorName: str
   deviceId: pyVmomi.VmomiSupport.short
   subDeviceId: pyVmomi.VmomiSupport.short
   parentBridge: _typing.Optional[str] = None
   deviceName: str
   deviceClassName: _typing.Optional[str] = None
   directPathInfo: _typing.Optional[DirectPathInfo] = None


class PciPassthruConfig(pyVmomi.vmodl.DynamicData):
   id: str
   passthruEnabled: bool
   applyNow: _typing.Optional[bool] = None
   hardwareLabel: _typing.Optional[str] = None


class PciPassthruInfo(pyVmomi.vmodl.DynamicData):
   class DirectPathDeviceMode(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['DirectPathDeviceMode'] = 'none'
      host: _typing.ClassVar['DirectPathDeviceMode'] = 'host'
      directPath: _typing.ClassVar['DirectPathDeviceMode'] = 'directPath'
      enhancedDirectPath: _typing.ClassVar['DirectPathDeviceMode'] = 'enhancedDirectPath'
      vGpuSameSize: _typing.ClassVar['DirectPathDeviceMode'] = 'vGpuSameSize'
      vGpuMixedSize: _typing.ClassVar['DirectPathDeviceMode'] = 'vGpuMixedSize'
      systemSelect: _typing.ClassVar['DirectPathDeviceMode'] = 'systemSelect'

   class DirectPathState(pyVmomi.vmodl.DynamicData):
      mode: str
      configurableModes: list[str] = []
      usedMemory: _typing.Optional[int] = None

   id: str
   dependentDevice: str
   passthruEnabled: bool
   passthruCapable: bool
   passthruActive: bool
   hardwareLabel: _typing.Optional[str] = None
   directPathState: _typing.Optional[DirectPathState] = None


class PciPassthruSystem(pyVmomi.vim.ExtensibleManagedObject):
   @property
   def pciPassthruInfo(self) -> list[PciPassthruInfo]: ...
   @property
   def sriovDevicePoolInfo(self) -> list[SriovDevicePoolInfo]: ...

   def Refresh(self) -> None: ...
   def UpdatePassthruConfig(self, config: list[PciPassthruConfig]) -> None: ...

class PcieHba(HostBusAdapter):
   pass

class PcieTargetTransport(TargetTransport):
   pass


class PersistentMemoryInfo(pyVmomi.vmodl.DynamicData):
   capacityInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   volumeUUID: _typing.Optional[str] = None


class PhysicalNic(pyVmomi.vmodl.DynamicData):
   class Specification(pyVmomi.vmodl.DynamicData):
      ip: _typing.Optional[IpConfig] = None
      linkSpeed: _typing.Optional[LinkSpeedDuplex] = None
      enableEnhancedNetworkingStack: _typing.Optional[bool] = None
      ensInterruptEnabled: _typing.Optional[bool] = None

   class Config(pyVmomi.vmodl.DynamicData):
      device: str
      spec: Specification

   class LinkSpeedDuplex(pyVmomi.vmodl.DynamicData):
      speedMb: int
      duplex: bool

   class NetworkHint(pyVmomi.vmodl.DynamicData):
      class HintElement(pyVmomi.vmodl.DynamicData):
         vlanId: _typing.Optional[int] = None

      class IpNetwork(NetworkHint.HintElement):
         ipSubnet: str

      class NamedNetwork(NetworkHint.HintElement):
         network: str

      device: str
      subnet: list[IpNetwork] = []
      network: list[NamedNetwork] = []
      connectedSwitchPort: _typing.Optional[CdpInfo] = None
      lldpInfo: _typing.Optional[LldpInfo] = None

   class CdpDeviceCapability(pyVmomi.vmodl.DynamicData):
      router: bool
      transparentBridge: bool
      sourceRouteBridge: bool
      networkSwitch: bool
      host: bool
      igmpEnabled: bool
      repeater: bool

   class CdpInfo(pyVmomi.vmodl.DynamicData):
      cdpVersion: _typing.Optional[int] = None
      timeout: _typing.Optional[int] = None
      ttl: _typing.Optional[int] = None
      samples: _typing.Optional[int] = None
      devId: _typing.Optional[str] = None
      address: _typing.Optional[str] = None
      portId: _typing.Optional[str] = None
      deviceCapability: _typing.Optional[CdpDeviceCapability] = None
      softwareVersion: _typing.Optional[str] = None
      hardwarePlatform: _typing.Optional[str] = None
      ipPrefix: _typing.Optional[str] = None
      ipPrefixLen: _typing.Optional[int] = None
      vlan: _typing.Optional[int] = None
      fullDuplex: _typing.Optional[bool] = None
      mtu: _typing.Optional[int] = None
      systemName: _typing.Optional[str] = None
      systemOID: _typing.Optional[str] = None
      mgmtAddr: _typing.Optional[str] = None
      location: _typing.Optional[str] = None

   class LldpInfo(pyVmomi.vmodl.DynamicData):
      chassisId: str
      portId: str
      timeToLive: int
      parameter: list[pyVmomi.vmodl.KeyAnyValue] = []

   class VmDirectPathGen2SupportedMode(pyVmomi.VmomiSupport.Enum):
      upt: _typing.ClassVar['VmDirectPathGen2SupportedMode'] = 'upt'

   class ResourcePoolSchedulerDisallowedReason(pyVmomi.VmomiSupport.Enum):
      userOptOut: _typing.ClassVar['ResourcePoolSchedulerDisallowedReason'] = 'userOptOut'
      hardwareUnsupported: _typing.ClassVar['ResourcePoolSchedulerDisallowedReason'] = 'hardwareUnsupported'

   key: _typing.Optional[str] = None
   device: str
   pci: str
   driver: _typing.Optional[str] = None
   driverVersion: _typing.Optional[str] = None
   firmwareVersion: _typing.Optional[str] = None
   linkSpeed: _typing.Optional[LinkSpeedDuplex] = None
   validLinkSpecification: list[LinkSpeedDuplex] = []
   spec: Specification
   wakeOnLanSupported: bool
   mac: str
   fcoeConfiguration: _typing.Optional[FcoeConfig] = None
   vmDirectPathGen2Supported: _typing.Optional[bool] = None
   vmDirectPathGen2SupportedMode: _typing.Optional[str] = None
   resourcePoolSchedulerAllowed: _typing.Optional[bool] = None
   resourcePoolSchedulerDisallowedReason: list[str] = []
   autoNegotiateSupported: _typing.Optional[bool] = None
   enhancedNetworkingStackSupported: _typing.Optional[bool] = None
   ensInterruptSupported: _typing.Optional[bool] = None
   rdmaDevice: _typing.Optional[RdmaDevice] = None
   dpuId: _typing.Optional[str] = None
   perfNicOffloadSupported: _typing.Optional[bool] = None


class PlugStoreTopology(pyVmomi.vmodl.DynamicData):
   class Adapter(pyVmomi.vmodl.DynamicData):
      key: str
      adapter: HostBusAdapter
      path: list[Path] = []

   class Path(pyVmomi.vmodl.DynamicData):
      key: str
      name: str
      channelNumber: _typing.Optional[int] = None
      targetNumber: _typing.Optional[int] = None
      lunNumber: _typing.Optional[int] = None
      adapter: _typing.Optional[Adapter] = None
      target: _typing.Optional[Target] = None
      device: _typing.Optional[Device] = None

   class Device(pyVmomi.vmodl.DynamicData):
      key: str
      lun: ScsiLun
      path: list[Path] = []

   class Plugin(pyVmomi.vmodl.DynamicData):
      key: str
      name: str
      device: list[Device] = []
      claimedPath: list[Path] = []

   class Target(pyVmomi.vmodl.DynamicData):
      key: str
      transport: _typing.Optional[TargetTransport] = None

   adapter: list[Adapter] = []
   path: list[Path] = []
   target: list[Target] = []
   device: list[Device] = []
   plugin: list[Plugin] = []


class PnicTSOInfo(pyVmomi.vmodl.DynamicData):
   nicName: str
   isSupported: bool
   isEnabled: bool


class PodVMInfo(pyVmomi.vmodl.DynamicData):
   hasPageSharingPodVM: bool
   podVMOverheadInfo: PodVMOverheadInfo


class PodVMOverheadInfo(pyVmomi.vmodl.DynamicData):
   crxPageSharingSupported: bool
   podVMOverheadWithoutPageSharing: int
   podVMOverheadWithPageSharing: int


class PortGroup(pyVmomi.vmodl.DynamicData):
   class PortConnecteeType(pyVmomi.VmomiSupport.Enum):
      virtualMachine: _typing.ClassVar['PortConnecteeType'] = 'virtualMachine'
      systemManagement: _typing.ClassVar['PortConnecteeType'] = 'systemManagement'
      host: _typing.ClassVar['PortConnecteeType'] = 'host'
      unknown: _typing.ClassVar['PortConnecteeType'] = 'unknown'

   class Specification(pyVmomi.vmodl.DynamicData):
      name: str
      vlanId: int
      vswitchName: str
      policy: NetworkPolicy

   class Config(pyVmomi.vmodl.DynamicData):
      changeOperation: _typing.Optional[str] = None
      spec: _typing.Optional[Specification] = None

   class Port(pyVmomi.vmodl.DynamicData):
      key: _typing.Optional[str] = None
      mac: list[str] = []
      type: str

   key: _typing.Optional[str] = None
   port: list[Port] = []
   vswitch: _typing.Optional[VirtualSwitch] = None
   computedPolicy: NetworkPolicy
   spec: Specification


class PowerSystem(pyVmomi.VmomiSupport.ManagedObject):
   class PowerPolicy(pyVmomi.vmodl.DynamicData):
      key: int
      name: str
      shortName: str
      description: str

   class Capability(pyVmomi.vmodl.DynamicData):
      availablePolicy: list[PowerPolicy] = []

   class Info(pyVmomi.vmodl.DynamicData):
      currentPolicy: PowerPolicy

   @property
   def capability(self) -> Capability: ...
   @property
   def info(self) -> Info: ...

   def ConfigurePolicy(self, key: int) -> None: ...


class ProtocolEndpoint(pyVmomi.vmodl.DynamicData):
   class PEType(pyVmomi.VmomiSupport.Enum):
      block: _typing.ClassVar['PEType'] = 'block'
      nas: _typing.ClassVar['PEType'] = 'nas'

   class ProtocolEndpointType(pyVmomi.VmomiSupport.Enum):
      scsi: _typing.ClassVar['ProtocolEndpointType'] = 'scsi'
      nfs: _typing.ClassVar['ProtocolEndpointType'] = 'nfs'
      nfs4x: _typing.ClassVar['ProtocolEndpointType'] = 'nfs4x'

   peType: str
   type: _typing.Optional[str] = None
   uuid: str
   hostKey: list[pyVmomi.vim.HostSystem] = []
   storageArray: _typing.Optional[str] = None
   nfsServer: _typing.Optional[str] = None
   nfsDir: _typing.Optional[str] = None
   nfsServerScope: _typing.Optional[str] = None
   nfsServerMajor: _typing.Optional[str] = None
   nfsServerAuthType: _typing.Optional[str] = None
   nfsServerUser: _typing.Optional[str] = None
   deviceId: _typing.Optional[str] = None
   usedByStretchedContainer: _typing.Optional[bool] = None


class PtpConfig(pyVmomi.vmodl.DynamicData):
   class DeviceType(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['DeviceType'] = 'none'
      virtualNic: _typing.ClassVar['DeviceType'] = 'virtualNic'
      pciPassthruNic: _typing.ClassVar['DeviceType'] = 'pciPassthruNic'

   class PtpPort(pyVmomi.vmodl.DynamicData):
      index: int
      deviceType: _typing.Optional[str] = None
      device: _typing.Optional[str] = None
      ipConfig: _typing.Optional[IpConfig] = None

   domain: _typing.Optional[int] = None
   port: list[PtpPort] = []


class QualifiedName(pyVmomi.vmodl.DynamicData):
   class Type(pyVmomi.VmomiSupport.Enum):
      nvmeQualifiedName: _typing.ClassVar['Type'] = 'nvmeQualifiedName'
      vvolNvmeQualifiedName: _typing.ClassVar['Type'] = 'vvolNvmeQualifiedName'

   value: str
   type: str


class RdmaDevice(pyVmomi.vmodl.DynamicData):
   class Backing(pyVmomi.vmodl.DynamicData):
      pass

   class PnicBacking(Backing):
      pairedUplink: PhysicalNic

   class ConnectionState(pyVmomi.VmomiSupport.Enum):
      unknown: _typing.ClassVar['ConnectionState'] = 'unknown'
      down: _typing.ClassVar['ConnectionState'] = 'down'
      init: _typing.ClassVar['ConnectionState'] = 'init'
      armed: _typing.ClassVar['ConnectionState'] = 'armed'
      active: _typing.ClassVar['ConnectionState'] = 'active'
      activeDefer: _typing.ClassVar['ConnectionState'] = 'activeDefer'

   class ConnectionInfo(pyVmomi.vmodl.DynamicData):
      state: str
      mtu: int
      speedInMbps: int

   class Capability(pyVmomi.vmodl.DynamicData):
      roceV1Capable: bool
      roceV2Capable: bool
      iWarpCapable: bool

   key: str
   device: str
   driver: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   backing: _typing.Optional[Backing] = None
   connectionInfo: ConnectionInfo
   capability: Capability


class RdmaHba(HostBusAdapter):
   associatedRdmaDevice: _typing.Optional[str] = None

class RdmaProtocol:
   pass

class RdmaTargetTransport(TargetTransport):
   pass


class ReliableMemoryInfo(pyVmomi.vmodl.DynamicData):
   memorySize: pyVmomi.VmomiSupport.long


class ResignatureRescanResult(pyVmomi.vmodl.DynamicData):
   rescan: list[VmfsRescanResult] = []
   result: pyVmomi.vim.Datastore


class Ruleset(pyVmomi.vmodl.DynamicData):
   class IpNetwork(pyVmomi.vmodl.DynamicData):
      network: str
      prefixLength: int

   class IpList(pyVmomi.vmodl.DynamicData):
      ipAddress: list[str] = []
      ipNetwork: list[IpNetwork] = []
      allIp: bool

   class RulesetSpec(pyVmomi.vmodl.DynamicData):
      allowedHosts: IpList

   class Rule(pyVmomi.vmodl.DynamicData):
      class Direction(pyVmomi.VmomiSupport.Enum):
         inbound: _typing.ClassVar['Direction'] = 'inbound'
         outbound: _typing.ClassVar['Direction'] = 'outbound'

      class PortType(pyVmomi.VmomiSupport.Enum):
         src: _typing.ClassVar['PortType'] = 'src'
         dst: _typing.ClassVar['PortType'] = 'dst'

      class Protocol(pyVmomi.VmomiSupport.Enum):
         tcp: _typing.ClassVar['Protocol'] = 'tcp'
         udp: _typing.ClassVar['Protocol'] = 'udp'

      port: int
      endPort: _typing.Optional[int] = None
      direction: Direction
      portType: _typing.Optional[PortType] = None
      protocol: str

   key: str
   label: str
   required: bool
   rule: list[Rule] = []
   service: _typing.Optional[str] = None
   enabled: bool
   allowedHosts: _typing.Optional[IpList] = None
   userControllable: _typing.Optional[bool] = None
   ipListUserConfigurable: _typing.Optional[bool] = None


class RuntimeInfo(pyVmomi.vmodl.DynamicData):
   class NetStackInstanceRuntimeInfo(pyVmomi.vmodl.DynamicData):
      class State(pyVmomi.VmomiSupport.Enum):
         inactive: _typing.ClassVar['State'] = 'inactive'
         active: _typing.ClassVar['State'] = 'active'
         deactivating: _typing.ClassVar['State'] = 'deactivating'
         activating: _typing.ClassVar['State'] = 'activating'

      netStackInstanceKey: str
      state: _typing.Optional[str] = None
      vmknicKeys: list[str] = []
      maxNumberOfConnections: _typing.Optional[int] = None
      currentIpV6Enabled: _typing.Optional[bool] = None

   class PlacedVirtualNicIdentifier(pyVmomi.vmodl.DynamicData):
      vm: pyVmomi.vim.VirtualMachine
      vnicKey: str
      reservation: _typing.Optional[int] = None

   class PnicNetworkResourceInfo(pyVmomi.vmodl.DynamicData):
      pnicDevice: str
      availableBandwidthForVMTraffic: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      unusedBandwidthForVMTraffic: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      placedVirtualNics: list[PlacedVirtualNicIdentifier] = []

   class NetworkResourceRuntimeInfo(pyVmomi.vmodl.DynamicData):
      pnicResourceInfo: list[PnicNetworkResourceInfo] = []

   class NetworkRuntimeInfo(pyVmomi.vmodl.DynamicData):
      netStackInstanceRuntimeInfo: list[NetStackInstanceRuntimeInfo] = []
      networkResourceRuntime: _typing.Optional[NetworkResourceRuntimeInfo] = None

   class StatelessNvdsMigrationState(pyVmomi.VmomiSupport.Enum):
      ready: _typing.ClassVar['StatelessNvdsMigrationState'] = 'ready'
      notNeeded: _typing.ClassVar['StatelessNvdsMigrationState'] = 'notNeeded'
      unknown: _typing.ClassVar['StatelessNvdsMigrationState'] = 'unknown'

   class StateEncryptionInfo(pyVmomi.vmodl.DynamicData):
      class ProtectionMode(pyVmomi.VmomiSupport.Enum):
         none: _typing.ClassVar['ProtectionMode'] = 'none'
         tpm: _typing.ClassVar['ProtectionMode'] = 'tpm'

      protectionMode: str
      requireSecureBoot: _typing.Optional[bool] = None
      requireExecInstalledOnly: _typing.Optional[bool] = None

   connectionState: pyVmomi.vim.HostSystem.ConnectionState
   powerState: pyVmomi.vim.HostSystem.PowerState
   standbyMode: _typing.Optional[str] = None
   inMaintenanceMode: bool
   inQuarantineMode: _typing.Optional[bool] = None
   bootTime: _typing.Optional[_datetime.datetime] = None
   healthSystemRuntime: _typing.Optional[HealthStatusSystem.Runtime] = None
   dasHostState: _typing.Optional[pyVmomi.vim.cluster.DasFdmHostState] = None
   tpmPcrValues: list[TpmDigestInfo] = []
   vsanRuntimeInfo: _typing.Optional[pyVmomi.vim.vsan.host.VsanRuntimeInfo] = None
   networkRuntimeInfo: _typing.Optional[NetworkRuntimeInfo] = None
   vFlashResourceRuntimeInfo: _typing.Optional[VFlashManager.VFlashResourceRunTimeInfo] = None
   hostMaxVirtualDiskCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   cryptoState: _typing.Optional[str] = None
   cryptoKeyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None
   statelessNvdsMigrationReady: _typing.Optional[str] = None
   partialMaintenanceMode: list[PartialMaintenanceModeRuntimeInfo] = []
   stateEncryption: _typing.Optional[StateEncryptionInfo] = None
   podVMInfo: _typing.Optional[PodVMInfo] = None


class ScsiDisk(ScsiLun):
   class Partition(pyVmomi.vmodl.DynamicData):
      diskName: str
      partition: int

   class ScsiDiskType(pyVmomi.VmomiSupport.Enum):
      native512: _typing.ClassVar['ScsiDiskType'] = 'native512'
      emulated512: _typing.ClassVar['ScsiDiskType'] = 'emulated512'
      native4k: _typing.ClassVar['ScsiDiskType'] = 'native4k'
      SoftwareEmulated4k: _typing.ClassVar['ScsiDiskType'] = 'SoftwareEmulated4k'
      unknown: _typing.ClassVar['ScsiDiskType'] = 'unknown'

   capacity: DiskDimensions.Lba
   devicePath: str
   ssd: _typing.Optional[bool] = None
   localDisk: _typing.Optional[bool] = None
   physicalLocation: list[str] = []
   emulatedDIXDIFEnabled: _typing.Optional[bool] = None
   vsanDiskInfo: _typing.Optional[pyVmomi.vim.vsan.host.VsanDiskInfo] = None
   scsiDiskType: _typing.Optional[str] = None
   usedByMemoryTiering: _typing.Optional[bool] = None


class ScsiLun(Device):
   class ScsiLunType(pyVmomi.VmomiSupport.Enum):
      disk: _typing.ClassVar['ScsiLunType'] = 'disk'
      tape: _typing.ClassVar['ScsiLunType'] = 'tape'
      printer: _typing.ClassVar['ScsiLunType'] = 'printer'
      processor: _typing.ClassVar['ScsiLunType'] = 'processor'
      worm: _typing.ClassVar['ScsiLunType'] = 'worm'
      cdrom: _typing.ClassVar['ScsiLunType'] = 'cdrom'
      scanner: _typing.ClassVar['ScsiLunType'] = 'scanner'
      opticalDevice: _typing.ClassVar['ScsiLunType'] = 'opticalDevice'
      mediaChanger: _typing.ClassVar['ScsiLunType'] = 'mediaChanger'
      communications: _typing.ClassVar['ScsiLunType'] = 'communications'
      storageArrayController: _typing.ClassVar['ScsiLunType'] = 'storageArrayController'
      enclosure: _typing.ClassVar['ScsiLunType'] = 'enclosure'
      unknown: _typing.ClassVar['ScsiLunType'] = 'unknown'

   class DeviceProtocol(pyVmomi.VmomiSupport.Enum):
      NVMe: _typing.ClassVar['DeviceProtocol'] = 'NVMe'
      SCSI: _typing.ClassVar['DeviceProtocol'] = 'SCSI'

   class Capabilities(pyVmomi.vmodl.DynamicData):
      updateDisplayNameSupported: bool

   class DurableName(pyVmomi.vmodl.DynamicData):
      namespace: str
      namespaceId: pyVmomi.VmomiSupport.byte
      data: list[pyVmomi.VmomiSupport.byte] = []

   class State(pyVmomi.VmomiSupport.Enum):
      unknownState: _typing.ClassVar['State'] = 'unknownState'
      ok: _typing.ClassVar['State'] = 'ok'
      error: _typing.ClassVar['State'] = 'error'
      off: _typing.ClassVar['State'] = 'off'
      quiesced: _typing.ClassVar['State'] = 'quiesced'
      degraded: _typing.ClassVar['State'] = 'degraded'
      lostCommunication: _typing.ClassVar['State'] = 'lostCommunication'
      timeout: _typing.ClassVar['State'] = 'timeout'

   class DescriptorQuality(pyVmomi.VmomiSupport.Enum):
      highQuality: _typing.ClassVar['DescriptorQuality'] = 'highQuality'
      mediumQuality: _typing.ClassVar['DescriptorQuality'] = 'mediumQuality'
      lowQuality: _typing.ClassVar['DescriptorQuality'] = 'lowQuality'
      unknownQuality: _typing.ClassVar['DescriptorQuality'] = 'unknownQuality'

   class Descriptor(pyVmomi.vmodl.DynamicData):
      quality: str
      id: str

   class VStorageSupportStatus(pyVmomi.VmomiSupport.Enum):
      vStorageSupported: _typing.ClassVar['VStorageSupportStatus'] = 'vStorageSupported'
      vStorageUnsupported: _typing.ClassVar['VStorageSupportStatus'] = 'vStorageUnsupported'
      vStorageUnknown: _typing.ClassVar['VStorageSupportStatus'] = 'vStorageUnknown'

   class LunReservationStatus(pyVmomi.VmomiSupport.Enum):
      LUN_RESERVED_UNKNOWN: _typing.ClassVar['LunReservationStatus'] = 'LUN_RESERVED_UNKNOWN'
      LUN_RESERVED_YES: _typing.ClassVar['LunReservationStatus'] = 'LUN_RESERVED_YES'
      LUN_RESERVED_NO: _typing.ClassVar['LunReservationStatus'] = 'LUN_RESERVED_NO'
      LUN_RESERVED_NOT_SUPPORTED: _typing.ClassVar['LunReservationStatus'] = 'LUN_RESERVED_NOT_SUPPORTED'

   key: _typing.Optional[str] = None
   uuid: str
   descriptor: list[Descriptor] = []
   canonicalName: _typing.Optional[str] = None
   displayName: _typing.Optional[str] = None
   lunType: str
   vendor: _typing.Optional[str] = None
   model: _typing.Optional[str] = None
   revision: _typing.Optional[str] = None
   scsiLevel: _typing.Optional[int] = None
   serialNumber: _typing.Optional[str] = None
   durableName: _typing.Optional[DurableName] = None
   alternateName: list[DurableName] = []
   standardInquiry: list[pyVmomi.VmomiSupport.byte] = []
   queueDepth: _typing.Optional[int] = None
   operationalState: list[str] = []
   capabilities: _typing.Optional[Capabilities] = None
   vStorageSupport: _typing.Optional[str] = None
   protocolEndpoint: _typing.Optional[bool] = None
   perenniallyReserved: _typing.Optional[bool] = None
   clusteredVmdkSupported: _typing.Optional[bool] = None
   applicationProtocol: _typing.Optional[str] = None
   dispersedNs: _typing.Optional[bool] = None
   deviceReservation: _typing.Optional[str] = None


class ScsiTopology(pyVmomi.vmodl.DynamicData):
   class Interface(pyVmomi.vmodl.DynamicData):
      key: str
      adapter: HostBusAdapter
      target: list[Target] = []

   class Target(pyVmomi.vmodl.DynamicData):
      key: str
      target: int
      lun: list[Lun] = []
      transport: _typing.Optional[TargetTransport] = None

   class Lun(pyVmomi.vmodl.DynamicData):
      key: str
      lun: int
      scsiLun: ScsiLun

   adapter: list[Interface] = []


class SecuritySpec(pyVmomi.vmodl.DynamicData):
   adminPassword: _typing.Optional[str] = None
   removePermission: list[pyVmomi.vim.AuthorizationManager.Permission] = []
   addPermission: list[pyVmomi.vim.AuthorizationManager.Permission] = []

class SerialAttachedHba(HostBusAdapter):
   nodeWorldWideName: str

class SerialAttachedTargetTransport(TargetTransport):
   pass


class Service(pyVmomi.vmodl.DynamicData):
   class Policy(pyVmomi.VmomiSupport.Enum):
      on: _typing.ClassVar['Policy'] = 'on'
      automatic: _typing.ClassVar['Policy'] = 'automatic'
      off: _typing.ClassVar['Policy'] = 'off'

   class SourcePackage(pyVmomi.vmodl.DynamicData):
      sourcePackageName: str
      description: str

   key: str
   label: str
   required: bool
   uninstallable: bool
   running: bool
   ruleset: list[str] = []
   policy: str
   sourcePackage: _typing.Optional[SourcePackage] = None


class ServiceConfig(pyVmomi.vmodl.DynamicData):
   serviceId: str
   startupPolicy: str


class ServiceInfo(pyVmomi.vmodl.DynamicData):
   service: list[Service] = []


class ServiceSystem(pyVmomi.vim.ExtensibleManagedObject):
   @property
   def serviceInfo(self) -> ServiceInfo: ...

   def UpdatePolicy(self, id: str, policy: str) -> None: ...
   def Start(self, id: str) -> None: ...
   def Stop(self, id: str) -> None: ...
   def Restart(self, id: str) -> None: ...
   def Uninstall(self, id: str) -> None: ...
   def Refresh(self) -> None: ...


class SevInfo(pyVmomi.vmodl.DynamicData):
   class SevState(pyVmomi.VmomiSupport.Enum):
      uninitialized: _typing.ClassVar['SevState'] = 'uninitialized'
      initialized: _typing.ClassVar['SevState'] = 'initialized'
      working: _typing.ClassVar['SevState'] = 'working'
      disabledBios: _typing.ClassVar['SevState'] = 'disabledBios'

   sevState: str
   maxSevEsGuests: pyVmomi.VmomiSupport.long
   snpState: _typing.Optional[str] = None
   snpSupported: _typing.Optional[bool] = None


class SgxInfo(pyVmomi.vmodl.DynamicData):
   class SgxStates(pyVmomi.VmomiSupport.Enum):
      notPresent: _typing.ClassVar['SgxStates'] = 'notPresent'
      disabledBIOS: _typing.ClassVar['SgxStates'] = 'disabledBIOS'
      disabledCFW101: _typing.ClassVar['SgxStates'] = 'disabledCFW101'
      disabledCPUMismatch: _typing.ClassVar['SgxStates'] = 'disabledCPUMismatch'
      disabledNoFLC: _typing.ClassVar['SgxStates'] = 'disabledNoFLC'
      disabledNUMAUnsup: _typing.ClassVar['SgxStates'] = 'disabledNUMAUnsup'
      disabledMaxEPCRegs: _typing.ClassVar['SgxStates'] = 'disabledMaxEPCRegs'
      enabled: _typing.ClassVar['SgxStates'] = 'enabled'

   class FlcModes(pyVmomi.VmomiSupport.Enum):
      off: _typing.ClassVar['FlcModes'] = 'off'
      locked: _typing.ClassVar['FlcModes'] = 'locked'
      unlocked: _typing.ClassVar['FlcModes'] = 'unlocked'

   sgxState: str
   totalEpcMemory: pyVmomi.VmomiSupport.long
   flcMode: str
   lePubKeyHash: _typing.Optional[str] = None
   registrationInfo: _typing.Optional[SgxRegistrationInfo] = None


class SgxRegistrationInfo(pyVmomi.vmodl.DynamicData):
   class RegistrationStatus(pyVmomi.VmomiSupport.Enum):
      notApplicable: _typing.ClassVar['RegistrationStatus'] = 'notApplicable'
      incomplete: _typing.ClassVar['RegistrationStatus'] = 'incomplete'
      complete: _typing.ClassVar['RegistrationStatus'] = 'complete'

   class RegistrationType(pyVmomi.VmomiSupport.Enum):
      manifest: _typing.ClassVar['RegistrationType'] = 'manifest'
      addPackage: _typing.ClassVar['RegistrationType'] = 'addPackage'

   status: _typing.Optional[str] = None
   biosError: _typing.Optional[int] = None
   registrationUrl: _typing.Optional[str] = None
   type: _typing.Optional[str] = None
   ppid: _typing.Optional[str] = None
   lastRegisteredTime: _typing.Optional[_datetime.datetime] = None


class SharedGpuCapabilities(pyVmomi.vmodl.DynamicData):
   vgpu: str
   diskSnapshotSupported: bool
   memorySnapshotSupported: bool
   suspendSupported: bool
   migrateSupported: bool


class SnmpSystem(pyVmomi.VmomiSupport.ManagedObject):
   class SnmpConfigSpec(pyVmomi.vmodl.DynamicData):
      class Destination(pyVmomi.vmodl.DynamicData):
         hostName: str
         port: int
         community: str

      enabled: _typing.Optional[bool] = None
      port: _typing.Optional[int] = None
      readOnlyCommunities: list[str] = []
      trapTargets: list[Destination] = []
      option: list[pyVmomi.vim.KeyValue] = []

   class AgentLimits(pyVmomi.vmodl.DynamicData):
      class Capability(pyVmomi.VmomiSupport.Enum):
         COMPLETE: _typing.ClassVar['Capability'] = 'COMPLETE'
         DIAGNOSTICS: _typing.ClassVar['Capability'] = 'DIAGNOSTICS'
         CONFIGURATION: _typing.ClassVar['Capability'] = 'CONFIGURATION'

      maxReadOnlyCommunities: int
      maxTrapDestinations: int
      maxCommunityLength: int
      maxBufferSize: int
      capability: Capability

   @property
   def configuration(self) -> SnmpConfigSpec: ...
   @property
   def limits(self) -> AgentLimits: ...

   def ReconfigureSnmpAgent(self, spec: SnmpConfigSpec) -> None: ...
   def SendTestNotification(self) -> None: ...


class SoftwarePackage(pyVmomi.vmodl.DynamicData):
   class VibType(pyVmomi.VmomiSupport.Enum):
      bootbank: _typing.ClassVar['VibType'] = 'bootbank'
      tools: _typing.ClassVar['VibType'] = 'tools'
      meta: _typing.ClassVar['VibType'] = 'meta'

   class Capability(pyVmomi.vmodl.DynamicData):
      liveInstallAllowed: _typing.Optional[bool] = None
      liveRemoveAllowed: _typing.Optional[bool] = None
      statelessReady: _typing.Optional[bool] = None
      overlay: _typing.Optional[bool] = None

   class Constraint(pyVmomi.VmomiSupport.Enum):
      equals: _typing.ClassVar['Constraint'] = 'equals'
      lessThan: _typing.ClassVar['Constraint'] = 'lessThan'
      lessThanEqual: _typing.ClassVar['Constraint'] = 'lessThanEqual'
      greaterThanEqual: _typing.ClassVar['Constraint'] = 'greaterThanEqual'
      greaterThan: _typing.ClassVar['Constraint'] = 'greaterThan'

   class Relation(pyVmomi.vmodl.DynamicData):
      constraint: _typing.Optional[str] = None
      name: str
      version: _typing.Optional[str] = None

   name: str
   version: str
   type: str
   vendor: str
   acceptanceLevel: str
   summary: str
   description: str
   referenceURL: list[str] = []
   creationDate: _typing.Optional[_datetime.datetime] = None
   depends: list[Relation] = []
   conflicts: list[Relation] = []
   replaces: list[Relation] = []
   provides: list[str] = []
   maintenanceModeRequired: _typing.Optional[bool] = None
   hardwarePlatformsRequired: list[str] = []
   capability: Capability
   tag: list[str] = []
   payload: list[str] = []

class SriovConfig(PciPassthruConfig):
   sriovEnabled: bool
   numVirtualFunction: int


class SriovDevicePoolInfo(pyVmomi.vmodl.DynamicData):
   key: str

class SriovInfo(PciPassthruInfo):
   sriovEnabled: bool
   sriovCapable: bool
   sriovActive: bool
   numVirtualFunctionRequested: int
   numVirtualFunction: int
   maxVirtualFunctionSupported: int


class SriovNetworkDevicePoolInfo(SriovDevicePoolInfo):
   switchKey: _typing.Optional[str] = None
   switchUuid: _typing.Optional[str] = None
   pnic: list[PhysicalNic] = []


class SslThumbprintInfo(pyVmomi.vmodl.DynamicData):
   principal: str
   ownerTag: str
   sslThumbprints: list[str] = []


class StorageArrayTypePolicyOption(pyVmomi.vmodl.DynamicData):
   policy: pyVmomi.vim.ElementDescription


class StorageDeviceInfo(pyVmomi.vmodl.DynamicData):
   hostBusAdapter: list[HostBusAdapter] = []
   scsiLun: list[ScsiLun] = []
   scsiTopology: _typing.Optional[ScsiTopology] = None
   nvmeTopology: _typing.Optional[NvmeTopology] = None
   multipathInfo: _typing.Optional[MultipathInfo] = None
   plugStoreTopology: _typing.Optional[PlugStoreTopology] = None
   softwareInternetScsiEnabled: bool

class StorageProtocol:
   pass


class StorageSystem(pyVmomi.vim.ExtensibleManagedObject):
   class VmfsVolumeResult(pyVmomi.vmodl.DynamicData):
      key: str
      fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

   class ScsiLunResult(pyVmomi.vmodl.DynamicData):
      key: str
      fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

   class DiskLocatorLedResult(pyVmomi.vmodl.DynamicData):
      key: str
      fault: pyVmomi.vmodl.MethodFault

   @property
   def storageDeviceInfo(self) -> _typing.Optional[StorageDeviceInfo]: ...
   @property
   def fileSystemVolumeInfo(self) -> FileSystemVolumeInfo: ...
   @property
   def systemFile(self) -> list[str]: ...
   @property
   def multipathStateInfo(self) -> _typing.Optional[MultipathStateInfo]: ...

   def RetrieveDiskPartitionInfo(self, devicePath: list[str]) -> list[DiskPartitionInfo]: ...
   def ComputeDiskPartitionInfo(self, devicePath: str, layout: DiskPartitionInfo.Layout, partitionFormat: _typing.Optional[str]) -> DiskPartitionInfo: ...
   def ComputeDiskPartitionInfoForResize(self, partition: ScsiDisk.Partition, blockRange: DiskPartitionInfo.BlockRange, partitionFormat: _typing.Optional[str]) -> DiskPartitionInfo: ...
   def UpdateDiskPartitions(self, devicePath: str, spec: DiskPartitionInfo.Specification) -> None: ...
   def FormatVmfs(self, createSpec: VmfsVolume.Specification) -> VmfsVolume: ...
   def MountVmfsVolume(self, vmfsUuid: str) -> None: ...
   def UnmountVmfsVolume(self, vmfsUuid: str) -> None: ...
   def UnmountVmfsVolumeEx(self, vmfsUuid: list[str]) -> pyVmomi.vim.Task: ...
   def MountVmfsVolumeEx(self, vmfsUuid: list[str]) -> pyVmomi.vim.Task: ...
   def UnmapVmfsVolumeEx(self, vmfsUuid: list[str]) -> pyVmomi.vim.Task: ...
   def DeleteVmfsVolumeState(self, vmfsUuid: str) -> None: ...
   def RescanVmfs(self) -> None: ...
   def AttachVmfsExtent(self, vmfsPath: str, extent: ScsiDisk.Partition) -> None: ...
   def ExpandVmfsExtent(self, vmfsPath: str, extent: ScsiDisk.Partition) -> None: ...
   def UpgradeVmfs(self, vmfsPath: str) -> None: ...
   def UpgradeVmLayout(self) -> None: ...
   def QueryUnresolvedVmfsVolume(self) -> list[UnresolvedVmfsVolume]: ...
   def ResolveMultipleUnresolvedVmfsVolumes(self, resolutionSpec: list[UnresolvedVmfsResolutionSpec]) -> list[UnresolvedVmfsResolutionResult]: ...
   def ResolveMultipleUnresolvedVmfsVolumesEx(self, resolutionSpec: list[UnresolvedVmfsResolutionSpec]) -> pyVmomi.vim.Task: ...
   def UnmountForceMountedVmfsVolume(self, vmfsUuid: str) -> None: ...
   def RescanHba(self, hbaDevice: str) -> None: ...
   def RescanAllHba(self) -> None: ...
   def UpdateSoftwareInternetScsiEnabled(self, enabled: bool) -> None: ...
   def UpdateInternetScsiDiscoveryProperties(self, iScsiHbaDevice: str, discoveryProperties: InternetScsiHba.DiscoveryProperties) -> None: ...
   def UpdateInternetScsiAuthenticationProperties(self, iScsiHbaDevice: str, authenticationProperties: InternetScsiHba.AuthenticationProperties, targetSet: _typing.Optional[InternetScsiHba.TargetSet]) -> None: ...
   def UpdateInternetScsiDigestProperties(self, iScsiHbaDevice: str, targetSet: _typing.Optional[InternetScsiHba.TargetSet], digestProperties: InternetScsiHba.DigestProperties) -> None: ...
   def UpdateInternetScsiAdvancedOptions(self, iScsiHbaDevice: str, targetSet: _typing.Optional[InternetScsiHba.TargetSet], options: list[InternetScsiHba.ParamValue]) -> None: ...
   def UpdateInternetScsiIPProperties(self, iScsiHbaDevice: str, ipProperties: InternetScsiHba.IPProperties) -> None: ...
   def UpdateInternetScsiName(self, iScsiHbaDevice: str, iScsiName: str) -> None: ...
   def UpdateInternetScsiAlias(self, iScsiHbaDevice: str, iScsiAlias: str) -> None: ...
   def AddInternetScsiSendTargets(self, iScsiHbaDevice: str, targets: list[InternetScsiHba.SendTarget]) -> None: ...
   def RemoveInternetScsiSendTargets(self, iScsiHbaDevice: str, targets: list[InternetScsiHba.SendTarget], force: _typing.Optional[bool]) -> None: ...
   def AddInternetScsiStaticTargets(self, iScsiHbaDevice: str, targets: list[InternetScsiHba.StaticTarget]) -> None: ...
   def RemoveInternetScsiStaticTargets(self, iScsiHbaDevice: str, targets: list[InternetScsiHba.StaticTarget]) -> None: ...
   def EnableMultipathPath(self, pathName: str) -> None: ...
   def DisableMultipathPath(self, pathName: str) -> None: ...
   def SetMultipathLunPolicy(self, lunId: str, policy: MultipathInfo.LogicalUnitPolicy) -> None: ...
   def UpdateHppMultipathLunPolicy(self, lunId: str, policy: MultipathInfo.HppLogicalUnitPolicy) -> None: ...
   def QueryPathSelectionPolicyOptions(self) -> list[PathSelectionPolicyOption]: ...
   def QueryStorageArrayTypePolicyOptions(self) -> list[StorageArrayTypePolicyOption]: ...
   def UpdateScsiLunDisplayName(self, lunUuid: str, displayName: str) -> None: ...
   def DetachScsiLun(self, lunUuid: str) -> None: ...
   def DetachScsiLunEx(self, lunUuid: list[str]) -> pyVmomi.vim.Task: ...
   def DeleteScsiLunState(self, lunCanonicalName: str) -> None: ...
   def AttachScsiLun(self, lunUuid: str) -> None: ...
   def AttachScsiLunEx(self, lunUuid: list[str]) -> pyVmomi.vim.Task: ...
   def Refresh(self) -> None: ...
   def DiscoverFcoeHbas(self, fcoeSpec: FcoeConfig.FcoeSpecification) -> None: ...
   def MarkForRemoval(self, hbaName: str, remove: bool) -> None: ...
   def FormatVffs(self, createSpec: VffsVolume.Specification) -> VffsVolume: ...
   def ExtendVffs(self, vffsPath: str, devicePath: str, spec: _typing.Optional[DiskPartitionInfo.Specification]) -> None: ...
   def DestroyVffs(self, vffsPath: str) -> None: ...
   def MountVffsVolume(self, vffsUuid: str) -> None: ...
   def UnmountVffsVolume(self, vffsUuid: str) -> None: ...
   def DeleteVffsVolumeState(self, vffsUuid: str) -> None: ...
   def RescanVffs(self) -> None: ...
   def QueryAvailableSsds(self, vffsPath: _typing.Optional[str]) -> list[ScsiDisk]: ...
   def SetNFSUser(self, user: str, password: str) -> None: ...
   def ChangeNFSUserPassword(self, password: str) -> None: ...
   def QueryNFSUser(self) -> _typing.Optional[NasVolume.UserInfo]: ...
   def ClearNFSUser(self) -> None: ...
   def TurnDiskLocatorLedOn(self, scsiDiskUuids: list[str]) -> pyVmomi.vim.Task: ...
   def TurnDiskLocatorLedOff(self, scsiDiskUuids: list[str]) -> pyVmomi.vim.Task: ...
   def MarkAsSsd(self, scsiDiskUuid: str) -> pyVmomi.vim.Task: ...
   def MarkAsNonSsd(self, scsiDiskUuid: str) -> pyVmomi.vim.Task: ...
   def MarkAsLocal(self, scsiDiskUuid: str) -> pyVmomi.vim.Task: ...
   def MarkAsNonLocal(self, scsiDiskUuid: str) -> pyVmomi.vim.Task: ...
   def UpdateVmfsUnmapPriority(self, vmfsUuid: str, unmapPriority: str) -> None: ...
   def UpdateVmfsUnmapBandwidth(self, vmfsUuid: str, unmapBandwidthSpec: VmfsVolume.UnmapBandwidthSpec) -> None: ...
   def QueryVmfsConfigOption(self) -> list[VmfsVolume.ConfigOption]: ...
   def MarkPerenniallyReserved(self, lunUuid: str, state: bool) -> None: ...
   def MarkPerenniallyReservedEx(self, lunUuid: list[str], state: bool) -> pyVmomi.vim.Task: ...
   def CreateNvmeOverRdmaAdapter(self, rdmaDeviceName: str) -> None: ...
   def RemoveNvmeOverRdmaAdapter(self, hbaDeviceName: str) -> None: ...
   def CreateSoftwareAdapter(self, spec: HbaCreateSpec) -> None: ...
   def RemoveSoftwareAdapter(self, hbaDeviceName: str) -> None: ...
   def DiscoverNvmeControllers(self, discoverSpec: NvmeDiscoverSpec) -> NvmeDiscoveryLog: ...
   def ConnectNvmeController(self, connectSpec: NvmeConnectSpec) -> None: ...
   def DisconnectNvmeController(self, disconnectSpec: NvmeDisconnectSpec) -> None: ...
   def ConnectNvmeControllerEx(self, connectSpec: list[NvmeConnectSpec]) -> pyVmomi.vim.Task: ...
   def DisconnectNvmeControllerEx(self, disconnectSpec: list[NvmeDisconnectSpec]) -> pyVmomi.vim.Task: ...


class Summary(pyVmomi.vmodl.DynamicData):
   class HardwareSummary(pyVmomi.vmodl.DynamicData):
      vendor: str
      model: str
      family: _typing.Optional[str] = None
      uuid: str
      otherIdentifyingInfo: list[SystemIdentificationInfo] = []
      memorySize: pyVmomi.VmomiSupport.long
      cpuModel: str
      cpuMhz: int
      numCpuPkgs: pyVmomi.VmomiSupport.short
      numCpuCores: pyVmomi.VmomiSupport.short
      numCpuThreads: pyVmomi.VmomiSupport.short
      numNics: int
      numHBAs: int

   class QuickStats(pyVmomi.vmodl.DynamicData):
      overallCpuUsage: _typing.Optional[int] = None
      overallMemoryUsage: _typing.Optional[int] = None
      distributedCpuFairness: _typing.Optional[int] = None
      distributedMemoryFairness: _typing.Optional[int] = None
      availablePMemCapacity: _typing.Optional[int] = None
      uptime: _typing.Optional[int] = None

   class ConfigSummary(pyVmomi.vmodl.DynamicData):
      name: str
      port: int
      sslThumbprint: _typing.Optional[str] = None
      sslCertificate: _typing.Optional[str] = None
      product: _typing.Optional[pyVmomi.vim.AboutInfo] = None
      vmotionEnabled: bool
      faultToleranceEnabled: bool
      featureVersion: list[FeatureVersionInfo] = []
      agentVmDatastore: _typing.Optional[pyVmomi.vim.Datastore] = None
      agentVmNetwork: _typing.Optional[pyVmomi.vim.Network] = None

   class GatewaySummary(pyVmomi.vmodl.DynamicData):
      gatewayType: str
      gatewayId: str

   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   hardware: _typing.Optional[HardwareSummary] = None
   runtime: _typing.Optional[RuntimeInfo] = None
   config: ConfigSummary
   quickStats: QuickStats
   overallStatus: pyVmomi.vim.ManagedEntity.Status
   rebootRequired: bool
   rebootRequiredReason: list[pyVmomi.vmodl.LocalizableMessage] = []
   maintenanceModeRequired: _typing.Optional[bool] = None
   customValue: list[pyVmomi.vim.CustomFieldsManager.Value] = []
   managementServerIp: _typing.Optional[str] = None
   maxEVCModeKey: _typing.Optional[str] = None
   currentEVCModeKey: _typing.Optional[str] = None
   currentEVCGraphicsModeKey: _typing.Optional[str] = None
   gateway: _typing.Optional[GatewaySummary] = None
   tpmAttestation: _typing.Optional[TpmAttestationInfo] = None
   trustAuthorityAttestationInfos: list[TrustAuthorityAttestationInfo] = []


class SystemEventInfo(pyVmomi.vmodl.DynamicData):
   recordId: pyVmomi.VmomiSupport.long
   when: str
   selType: pyVmomi.VmomiSupport.long
   message: str
   sensorNumber: pyVmomi.VmomiSupport.long


class SystemHealthInfo(pyVmomi.vmodl.DynamicData):
   numericSensorInfo: list[NumericSensorInfo] = []


class SystemIdentificationInfo(pyVmomi.vmodl.DynamicData):
   class Identifier(pyVmomi.VmomiSupport.Enum):
      AssetTag: _typing.ClassVar['Identifier'] = 'AssetTag'
      ServiceTag: _typing.ClassVar['Identifier'] = 'ServiceTag'
      OemSpecificString: _typing.ClassVar['Identifier'] = 'OemSpecificString'
      EnclosureSerialNumberTag: _typing.ClassVar['Identifier'] = 'EnclosureSerialNumberTag'
      SerialNumberTag: _typing.ClassVar['Identifier'] = 'SerialNumberTag'

   identifierValue: str
   identifierType: pyVmomi.vim.ElementDescription


class SystemInfo(pyVmomi.vmodl.DynamicData):
   vendor: str
   model: str
   family: _typing.Optional[str] = None
   uuid: str
   otherIdentifyingInfo: list[SystemIdentificationInfo] = []
   serialNumber: _typing.Optional[str] = None
   qualifiedName: list[QualifiedName] = []
   vvolHostNQN: _typing.Optional[QualifiedName] = None
   vvolHostId: _typing.Optional[str] = None
   bootCommandLine: _typing.Optional[str] = None


class SystemResourceInfo(pyVmomi.vmodl.DynamicData):
   key: str
   config: _typing.Optional[pyVmomi.vim.ResourceConfigSpec] = None
   child: list[SystemResourceInfo] = []


class SystemSwapConfiguration(pyVmomi.vmodl.DynamicData):
   class SystemSwapOption(pyVmomi.vmodl.DynamicData):
      key: int

   class DisabledOption(SystemSwapOption):
      pass

   class HostCacheOption(SystemSwapOption):
      pass

   class HostLocalSwapOption(SystemSwapOption):
      pass

   class DatastoreOption(SystemSwapOption):
      datastore: str

   option: list[SystemSwapOption] = []


class TargetTransport(pyVmomi.vmodl.DynamicData):
   pass


class TcpHba(HostBusAdapter):
   associatedPnic: _typing.Optional[str] = None

class TcpHbaCreateSpec(HbaCreateSpec):
   pnic: str

class TcpTargetTransport(TargetTransport):
   pass


class TdxInfo(pyVmomi.vmodl.DynamicData):
   class TdxState(pyVmomi.VmomiSupport.Enum):
      initializing: _typing.ClassVar['TdxState'] = 'initializing'
      initialized: _typing.ClassVar['TdxState'] = 'initialized'
      configured: _typing.ClassVar['TdxState'] = 'configured'
      ready: _typing.ClassVar['TdxState'] = 'ready'
      disabledBios: _typing.ClassVar['TdxState'] = 'disabledBios'

   tdxState: str
   numTDXPrivateKeyIDs: int


class TpmAttestationInfo(pyVmomi.vmodl.DynamicData):
   class AcceptanceStatus(pyVmomi.VmomiSupport.Enum):
      notAccepted: _typing.ClassVar['AcceptanceStatus'] = 'notAccepted'
      accepted: _typing.ClassVar['AcceptanceStatus'] = 'accepted'

   time: _datetime.datetime
   status: AcceptanceStatus
   message: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None


class TpmAttestationReport(pyVmomi.vmodl.DynamicData):
   tpmPcrValues: list[TpmDigestInfo] = []
   tpmEvents: list[TpmEventLogEntry] = []
   tpmLogReliable: bool

class TpmBootCompleteEventDetails(TpmEventDetails):
   pass

class TpmBootSecurityOptionEventDetails(TpmEventDetails):
   bootSecurityOption: str

class TpmCommandEventDetails(TpmEventDetails):
   commandLine: str

class TpmDigestInfo(DigestInfo):
   pcrNumber: int


class TpmEventDetails(pyVmomi.vmodl.DynamicData):
   dataHash: list[pyVmomi.VmomiSupport.byte] = []
   dataHashMethod: _typing.Optional[str] = None


class TpmEventLogEntry(pyVmomi.vmodl.DynamicData):
   pcrIndex: int
   eventDetails: TpmEventDetails

class TpmNvTagEventDetails(TpmBootSecurityOptionEventDetails):
   pass


class TpmOptionEventDetails(TpmEventDetails):
   optionsFileName: str
   bootOptions: list[pyVmomi.VmomiSupport.byte] = []

class TpmSignerEventDetails(TpmBootSecurityOptionEventDetails):
   pass

class TpmSoftwareComponentEventDetails(TpmEventDetails):
   componentName: str
   vibName: str
   vibVersion: str
   vibVendor: str

class TpmSystemVersionEventDetails(TpmEventDetails):
   systemVersion: str


class TpmVersionEventDetails(TpmEventDetails):
   version: pyVmomi.VmomiSupport.binary


class TrustAuthorityAttestationInfo(pyVmomi.vmodl.DynamicData):
   class AttestationStatus(pyVmomi.VmomiSupport.Enum):
      attested: _typing.ClassVar['AttestationStatus'] = 'attested'
      notAttested: _typing.ClassVar['AttestationStatus'] = 'notAttested'
      unknown: _typing.ClassVar['AttestationStatus'] = 'unknown'

   attestationStatus: str
   serviceId: _typing.Optional[str] = None
   attestedAt: _typing.Optional[_datetime.datetime] = None
   attestedUntil: _typing.Optional[_datetime.datetime] = None
   messages: list[pyVmomi.vmodl.LocalizableMessage] = []


class UnresolvedVmfsExtent(pyVmomi.vmodl.DynamicData):
   class UnresolvedReason(pyVmomi.VmomiSupport.Enum):
      diskIdMismatch: _typing.ClassVar['UnresolvedReason'] = 'diskIdMismatch'
      uuidConflict: _typing.ClassVar['UnresolvedReason'] = 'uuidConflict'

   device: ScsiDisk.Partition
   devicePath: str
   vmfsUuid: str
   isHeadExtent: bool
   ordinal: int
   startBlock: int
   endBlock: int
   reason: str


class UnresolvedVmfsResignatureSpec(pyVmomi.vmodl.DynamicData):
   extentDevicePath: list[str] = []


class UnresolvedVmfsResolutionResult(pyVmomi.vmodl.DynamicData):
   spec: UnresolvedVmfsResolutionSpec
   vmfs: _typing.Optional[VmfsVolume] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class UnresolvedVmfsResolutionSpec(pyVmomi.vmodl.DynamicData):
   class VmfsUuidResolution(pyVmomi.VmomiSupport.Enum):
      resignature: _typing.ClassVar['VmfsUuidResolution'] = 'resignature'
      forceMount: _typing.ClassVar['VmfsUuidResolution'] = 'forceMount'

   extentDevicePath: list[str] = []
   uuidResolution: str


class UnresolvedVmfsVolume(pyVmomi.vmodl.DynamicData):
   class ResolveStatus(pyVmomi.vmodl.DynamicData):
      resolvable: bool
      incompleteExtents: _typing.Optional[bool] = None
      multipleCopies: _typing.Optional[bool] = None

   extent: list[UnresolvedVmfsExtent] = []
   vmfsLabel: str
   vmfsUuid: str
   totalBlocks: int
   resolveStatus: ResolveStatus


class VFlashManager(pyVmomi.VmomiSupport.ManagedObject):
   class VFlashResourceConfigSpec(pyVmomi.vmodl.DynamicData):
      vffsUuid: str

   class VFlashResourceConfigInfo(pyVmomi.vmodl.DynamicData):
      vffs: _typing.Optional[VffsVolume] = None
      capacity: pyVmomi.VmomiSupport.long

   class VFlashResourceRunTimeInfo(pyVmomi.vmodl.DynamicData):
      usage: pyVmomi.VmomiSupport.long
      capacity: pyVmomi.VmomiSupport.long
      accessible: bool
      capacityForVmCache: pyVmomi.VmomiSupport.long
      freeForVmCache: pyVmomi.VmomiSupport.long

   class VFlashCacheConfigSpec(pyVmomi.vmodl.DynamicData):
      defaultVFlashModule: str
      swapCacheReservationInGB: pyVmomi.VmomiSupport.long

   class VFlashCacheConfigInfo(pyVmomi.vmodl.DynamicData):
      class VFlashModuleConfigOption(pyVmomi.vmodl.DynamicData):
         vFlashModule: str
         vFlashModuleVersion: str
         minSupportedModuleVersion: str
         cacheConsistencyType: pyVmomi.vim.option.ChoiceOption
         cacheMode: pyVmomi.vim.option.ChoiceOption
         blockSizeInKBOption: pyVmomi.vim.option.LongOption
         reservationInMBOption: pyVmomi.vim.option.LongOption
         maxDiskSizeInKB: pyVmomi.VmomiSupport.long

      vFlashModuleConfigOption: list[VFlashModuleConfigOption] = []
      defaultVFlashModule: _typing.Optional[str] = None
      swapCacheReservationInGB: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class VFlashConfigInfo(pyVmomi.vmodl.DynamicData):
      vFlashResourceConfigInfo: _typing.Optional[VFlashResourceConfigInfo] = None
      vFlashCacheConfigInfo: _typing.Optional[VFlashCacheConfigInfo] = None

   @property
   def vFlashConfigInfo(self) -> _typing.Optional[VFlashConfigInfo]: ...

   def ConfigureVFlashResourceEx(self, devicePath: list[str]) -> pyVmomi.vim.Task: ...
   def ConfigureVFlashResource(self, spec: VFlashResourceConfigSpec) -> None: ...
   def RemoveVFlashResource(self) -> None: ...
   def ConfigureHostVFlashCache(self, spec: VFlashCacheConfigSpec) -> None: ...
   def GetVFlashModuleDefaultConfig(self, vFlashModule: str) -> pyVmomi.vim.vm.device.VirtualDisk.VFlashCacheConfigInfo: ...


class VFlashResourceConfigurationResult(pyVmomi.vmodl.DynamicData):
   devicePath: list[str] = []
   vffs: _typing.Optional[VffsVolume] = None
   diskConfigurationResult: list[DiskConfigurationResult] = []


class VMotionConfig(pyVmomi.vmodl.DynamicData):
   vmotionNicKey: _typing.Optional[str] = None
   enabled: bool


class VMotionInfo(pyVmomi.vmodl.DynamicData):
   netConfig: _typing.Optional[VMotionSystem.NetConfig] = None
   ipConfig: _typing.Optional[IpConfig] = None


class VMotionSystem(pyVmomi.vim.ExtensibleManagedObject):
   class NetConfig(pyVmomi.vmodl.DynamicData):
      candidateVnic: list[VirtualNic] = []
      selectedVnic: _typing.Optional[VirtualNic] = None

   @property
   def netConfig(self) -> _typing.Optional[NetConfig]: ...
   @property
   def ipConfig(self) -> _typing.Optional[IpConfig]: ...

   def UpdateIpConfig(self, ipConfig: IpConfig) -> None: ...
   def SelectVnic(self, device: str) -> None: ...
   def DeselectVnic(self) -> None: ...


class VSANStretchedClusterHostCapability(pyVmomi.vmodl.DynamicData):
   featureVersion: str

class VfatVolume(FileSystemVolume):
   pass


class VffsVolume(FileSystemVolume):
   class Specification(pyVmomi.vmodl.DynamicData):
      devicePath: str
      partition: _typing.Optional[DiskPartitionInfo.Specification] = None
      majorVersion: int
      volumeName: str

   majorVersion: int
   version: str
   uuid: str
   extent: list[ScsiDisk.Partition] = []


class VirtualNic(pyVmomi.vmodl.DynamicData):
   class Specification(pyVmomi.vmodl.DynamicData):
      ip: _typing.Optional[IpConfig] = None
      mac: _typing.Optional[str] = None
      distributedVirtualPort: _typing.Optional[pyVmomi.vim.dvs.PortConnection] = None
      portgroup: _typing.Optional[str] = None
      mtu: _typing.Optional[int] = None
      tsoEnabled: _typing.Optional[bool] = None
      netStackInstanceKey: _typing.Optional[str] = None
      opaqueNetwork: _typing.Optional[OpaqueNetworkSpec] = None
      externalId: _typing.Optional[str] = None
      pinnedPnic: _typing.Optional[str] = None
      ipRouteSpec: _typing.Optional[IpRouteSpec] = None
      systemOwned: _typing.Optional[bool] = None
      dpuId: _typing.Optional[str] = None

   class Config(pyVmomi.vmodl.DynamicData):
      changeOperation: _typing.Optional[str] = None
      device: _typing.Optional[str] = None
      portgroup: str
      spec: _typing.Optional[Specification] = None

   class OpaqueNetworkSpec(pyVmomi.vmodl.DynamicData):
      opaqueNetworkId: str
      opaqueNetworkType: str

   class IpRouteSpec(pyVmomi.vmodl.DynamicData):
      ipRouteConfig: _typing.Optional[IpRouteConfig] = None

   device: str
   key: str
   portgroup: str
   spec: Specification
   port: _typing.Optional[PortGroup.Port] = None
   owner: _typing.Optional[str] = None


class VirtualNicConnection(pyVmomi.vmodl.DynamicData):
   portgroup: _typing.Optional[str] = None
   dvPort: _typing.Optional[pyVmomi.vim.dvs.PortConnection] = None
   opNetwork: _typing.Optional[VirtualNic.OpaqueNetworkSpec] = None


class VirtualNicManager(pyVmomi.vim.ExtensibleManagedObject):
   class NicType(pyVmomi.VmomiSupport.Enum):
      vmotion: _typing.ClassVar['NicType'] = 'vmotion'
      faultToleranceLogging: _typing.ClassVar['NicType'] = 'faultToleranceLogging'
      vSphereReplication: _typing.ClassVar['NicType'] = 'vSphereReplication'
      vSphereReplicationNFC: _typing.ClassVar['NicType'] = 'vSphereReplicationNFC'
      management: _typing.ClassVar['NicType'] = 'management'
      vsan: _typing.ClassVar['NicType'] = 'vsan'
      vSphereProvisioning: _typing.ClassVar['NicType'] = 'vSphereProvisioning'
      vsanWitness: _typing.ClassVar['NicType'] = 'vsanWitness'
      vSphereBackupNFC: _typing.ClassVar['NicType'] = 'vSphereBackupNFC'
      ptp: _typing.ClassVar['NicType'] = 'ptp'
      vsanReplication: _typing.ClassVar['NicType'] = 'vsanReplication'
      nvmeTcp: _typing.ClassVar['NicType'] = 'nvmeTcp'
      nvmeRdma: _typing.ClassVar['NicType'] = 'nvmeRdma'
      vsanExternal: _typing.ClassVar['NicType'] = 'vsanExternal'
      vnetworking: _typing.ClassVar['NicType'] = 'vnetworking'

   class NicTypeSelection(pyVmomi.vmodl.DynamicData):
      vnic: VirtualNicConnection
      nicType: list[str] = []

   class NetConfig(pyVmomi.vmodl.DynamicData):
      nicType: str
      multiSelectAllowed: bool
      candidateVnic: list[VirtualNic] = []
      selectedVnic: list[VirtualNic] = []

   @property
   def info(self) -> VirtualNicManagerInfo: ...

   def QueryNetConfig(self, nicType: str) -> _typing.Optional[NetConfig]: ...
   def SelectVnic(self, nicType: str, device: str) -> None: ...
   def DeselectVnic(self, nicType: str, device: str) -> None: ...


class VirtualNicManagerInfo(pyVmomi.vmodl.DynamicData):
   netConfig: list[VirtualNicManager.NetConfig] = []


class VirtualSwitch(pyVmomi.vmodl.DynamicData):
   class Bridge(pyVmomi.vmodl.DynamicData):
      pass

   class AutoBridge(Bridge):
      excludedNicDevice: list[str] = []

   class SimpleBridge(Bridge):
      nicDevice: str

   class BondBridge(Bridge):
      nicDevice: list[str] = []
      beacon: _typing.Optional[BeaconConfig] = None
      linkDiscoveryProtocolConfig: _typing.Optional[LinkDiscoveryProtocolConfig] = None

   class BeaconConfig(pyVmomi.vmodl.DynamicData):
      interval: int

   class Specification(pyVmomi.vmodl.DynamicData):
      numPorts: int
      bridge: _typing.Optional[Bridge] = None
      policy: _typing.Optional[NetworkPolicy] = None
      mtu: _typing.Optional[int] = None

   class Config(pyVmomi.vmodl.DynamicData):
      changeOperation: _typing.Optional[str] = None
      name: str
      spec: _typing.Optional[Specification] = None

   name: str
   key: str
   numPorts: int
   numPortsAvailable: int
   mtu: _typing.Optional[int] = None
   portgroup: list[PortGroup] = []
   pnic: list[PhysicalNic] = []
   spec: Specification


class VmfsDatastoreCreateSpec(VmfsDatastoreSpec):
   partition: DiskPartitionInfo.Specification
   vmfs: VmfsVolume.Specification
   extent: list[ScsiDisk.Partition] = []

class VmfsDatastoreExpandSpec(VmfsDatastoreSpec):
   partition: DiskPartitionInfo.Specification
   extent: ScsiDisk.Partition

class VmfsDatastoreExtendSpec(VmfsDatastoreSpec):
   partition: DiskPartitionInfo.Specification
   extent: list[ScsiDisk.Partition] = []


class VmfsDatastoreInfo(pyVmomi.vim.Datastore.Info):
   maxPhysicalRDMFileSize: pyVmomi.VmomiSupport.long
   maxVirtualRDMFileSize: pyVmomi.VmomiSupport.long
   vmfs: _typing.Optional[VmfsVolume] = None


class VmfsDatastoreOption(pyVmomi.vmodl.DynamicData):
   class Info(pyVmomi.vmodl.DynamicData):
      layout: DiskPartitionInfo.Layout
      partitionFormatChange: _typing.Optional[bool] = None

   class SingleExtentInfo(Info):
      vmfsExtent: DiskPartitionInfo.BlockRange

   class AllExtentInfo(SingleExtentInfo):
      pass

   class MultipleExtentInfo(Info):
      vmfsExtent: list[DiskPartitionInfo.BlockRange] = []

   info: Info
   spec: VmfsDatastoreSpec


class VmfsDatastoreSpec(pyVmomi.vmodl.DynamicData):
   diskUuid: str


class VmfsRescanResult(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VmfsVolume(FileSystemVolume):
   class Specification(pyVmomi.vmodl.DynamicData):
      extent: ScsiDisk.Partition
      blockSizeMb: _typing.Optional[int] = None
      majorVersion: int
      volumeName: str
      blockSize: _typing.Optional[int] = None
      unmapGranularity: _typing.Optional[int] = None
      unmapPriority: _typing.Optional[str] = None
      unmapBandwidthSpec: _typing.Optional[UnmapBandwidthSpec] = None

   class UnmapBandwidthSpec(pyVmomi.vmodl.DynamicData):
      policy: str
      fixedValue: pyVmomi.VmomiSupport.long
      dynamicMin: pyVmomi.VmomiSupport.long
      dynamicMax: pyVmomi.VmomiSupport.long

   class UnmapPriority(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['UnmapPriority'] = 'none'
      low: _typing.ClassVar['UnmapPriority'] = 'low'

   class UnmapBandwidthPolicy(pyVmomi.VmomiSupport.Enum):
      fixed: _typing.ClassVar['UnmapBandwidthPolicy'] = 'fixed'
      dynamic: _typing.ClassVar['UnmapBandwidthPolicy'] = 'dynamic'

   class ConfigOption(pyVmomi.vmodl.DynamicData):
      blockSizeOption: int
      unmapGranularityOption: list[int] = []
      unmapBandwidthFixedValue: _typing.Optional[pyVmomi.vim.option.LongOption] = None
      unmapBandwidthDynamicMin: _typing.Optional[pyVmomi.vim.option.LongOption] = None
      unmapBandwidthDynamicMax: _typing.Optional[pyVmomi.vim.option.LongOption] = None
      unmapBandwidthIncrement: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      unmapBandwidthUltraLow: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   blockSizeMb: int
   blockSize: _typing.Optional[int] = None
   unmapGranularity: _typing.Optional[int] = None
   unmapPriority: _typing.Optional[str] = None
   unmapBandwidthSpec: _typing.Optional[UnmapBandwidthSpec] = None
   maxBlocks: int
   majorVersion: int
   version: str
   uuid: str
   extent: list[ScsiDisk.Partition] = []
   vmfsUpgradable: bool
   forceMountedInfo: _typing.Optional[ForceMountedInfo] = None
   ssd: _typing.Optional[bool] = None
   local: _typing.Optional[bool] = None
   scsiDiskType: _typing.Optional[str] = None


class VsanBasicDeviceInfo(pyVmomi.vmodl.DynamicData):
   deviceName: str
   pciId: _typing.Optional[str] = None
   fwVersion: _typing.Optional[str] = None
   features: list[str] = []


class VsanClusterMembershipInfo(pyVmomi.vmodl.DynamicData):
   clusterUuid: _typing.Optional[str] = None
   health: _typing.Optional[str] = None
   membershipUuid: _typing.Optional[str] = None
   memberUuid: list[str] = []

class VsanControllerType:
   pass


class VsanDaemonHealth(pyVmomi.vmodl.DynamicData):
   name: str
   alive: bool
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VsanDatastoreInfo(pyVmomi.vim.Datastore.Info):
   membershipUuid: _typing.Optional[str] = None
   accessGenNo: _typing.Optional[int] = None

class VsanDiskBalanceState:
   pass


class VsanDiskEncryptionHealth(pyVmomi.vmodl.DynamicData):
   diskHealth: _typing.Optional[VsanPhysicalDiskHealth] = None
   encryptionIssues: list[str] = []


class VsanDiskRebalanceResult(pyVmomi.vmodl.DynamicData):
   status: str
   bytesMoving: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   remainingBytesToMove: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   diskUsage: _typing.Optional[float] = None
   maxDiskUsage: _typing.Optional[float] = None
   minDiskUsage: _typing.Optional[float] = None
   avgDiskUsage: _typing.Optional[float] = None
   diskCompUsage: _typing.Optional[float] = None
   maxDiskCompUsage: _typing.Optional[float] = None
   minDiskCompUsage: _typing.Optional[float] = None
   avgDiskCompUsage: _typing.Optional[float] = None


class VsanDitEncryptionHealthSummary(pyVmomi.vmodl.DynamicData):
   hostname: _typing.Optional[str] = None
   health: _typing.Optional[str] = None
   reason: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None
   ditEncryptionInfo: _typing.Optional[pyVmomi.vim.vsan.host.DataInTransitEncryptionInfo] = None


class VsanEncryptionHealthSummary(pyVmomi.vmodl.DynamicData):
   hostname: _typing.Optional[str] = None
   encryptionInfo: _typing.Optional[pyVmomi.vim.vsan.host.EncryptionInfo] = None
   overallKmsHealth: str
   kmsHealth: list[VsanKmsHealth] = []
   encryptionIssues: list[str] = []
   diskResults: list[VsanDiskEncryptionHealth] = []
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   aesniEnabled: _typing.Optional[bool] = None
   inconsistentlyEncryptedObjectCount: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   hostEncryptionDekId: _typing.Optional[str] = None
   kekVerifierHealth: _typing.Optional[bool] = None
   dekVerifierHealth: _typing.Optional[bool] = None

class VsanEncryptionIssue:
   pass


class VsanFailedRepairObjectResult(pyVmomi.vmodl.DynamicData):
   uuid: str
   errMessage: _typing.Optional[str] = None


class VsanFileServerHealthSummary(pyVmomi.vmodl.DynamicData):
   domainName: _typing.Optional[str] = None
   fileServerIp: _typing.Optional[str] = None
   nfsdHealth: _typing.Optional[str] = None
   networkHealth: _typing.Optional[str] = None
   rootfsHealth: _typing.Optional[str] = None
   description: _typing.Optional[str] = None
   smbConnections: _typing.Optional[int] = None
   smbDaemonHealth: _typing.Optional[str] = None
   adTestJoinHealth: _typing.Optional[str] = None
   dnsLookupHealth: _typing.Optional[str] = None


class VsanFileServiceBalanceHealth(pyVmomi.vmodl.DynamicData):
   health: _typing.Optional[str] = None
   description: _typing.Optional[str] = None


class VsanFileServiceHealthSummary(pyVmomi.vmodl.DynamicData):
   hostname: _typing.Optional[str] = None
   overallHealth: _typing.Optional[str] = None
   enabled: _typing.Optional[bool] = None
   vdfsdStatus: _typing.Optional[VsanResourceHealth] = None
   fsvmStatus: _typing.Optional[VsanResourceHealth] = None
   rootFsStatus: _typing.Optional[VsanFileServiceRootFsHealth] = None
   fileServerHealth: list[VsanFileServerHealthSummary] = []
   fileShareHealth: list[VsanFileServiceShareHealthSummary] = []
   balanceStatus: _typing.Optional[VsanFileServiceBalanceHealth] = None
   hostLoadStatus: _typing.Optional[VsanResourceHealth] = None


class VsanFileServiceRootFsHealth(pyVmomi.vmodl.DynamicData):
   created: _typing.Optional[bool] = None
   health: _typing.Optional[str] = None
   description: _typing.Optional[str] = None


class VsanFileServiceShareHealthSummary(pyVmomi.vmodl.DynamicData):
   overallHealth: _typing.Optional[str] = None
   domainName: _typing.Optional[str] = None
   shareUuid: _typing.Optional[str] = None
   shareName: _typing.Optional[str] = None
   objectHealth: _typing.Optional[VsanObjectOverallHealth] = None
   description: _typing.Optional[str] = None
   extensible: _typing.Optional[bool] = None
   spbmProfileUuid: _typing.Optional[str] = None
   spbmProfileGenerationId: _typing.Optional[str] = None
   sharePolicyMismatch: _typing.Optional[bool] = None


class VsanHclCommonDeviceInfo(pyVmomi.vmodl.DynamicData):
   deviceName: str
   displayName: _typing.Optional[str] = None
   driverName: _typing.Optional[str] = None
   driverVersion: _typing.Optional[str] = None
   vendorId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   deviceId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   subVendorId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   subDeviceId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   extraInfo: list[pyVmomi.vim.KeyValue] = []
   deviceOnHcl: _typing.Optional[bool] = None
   releaseSupported: _typing.Optional[bool] = None
   releasesOnHcl: list[str] = []
   driverVersionsOnHcl: list[str] = []
   driverVersionSupported: _typing.Optional[bool] = None
   fwVersionSupported: _typing.Optional[bool] = None
   fwVersionOnHcl: list[str] = []
   fwVersion: _typing.Optional[str] = None
   driversOnHcl: list[pyVmomi.vim.vsan.VsanHclDriverInfo] = []


class VsanHclComputeResource(pyVmomi.vmodl.DynamicData):
   memory: VsanHclMemInfo


class VsanHclControllerInfo(pyVmomi.vmodl.DynamicData):
   deviceName: str
   deviceDisplayName: _typing.Optional[str] = None
   driverName: _typing.Optional[str] = None
   driverVersion: _typing.Optional[str] = None
   vendorId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   deviceId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   subVendorId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   subDeviceId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   extraInfo: list[pyVmomi.vim.KeyValue] = []
   deviceOnHcl: _typing.Optional[bool] = None
   releaseSupported: _typing.Optional[bool] = None
   releasesOnHcl: list[str] = []
   driverVersionsOnHcl: list[str] = []
   driverVersionSupported: _typing.Optional[bool] = None
   fwVersionSupported: _typing.Optional[bool] = None
   fwVersionOnHcl: list[str] = []
   cacheConfigSupported: _typing.Optional[bool] = None
   cacheConfigOnHcl: list[str] = []
   raidConfigSupported: _typing.Optional[bool] = None
   raidConfigOnHcl: list[str] = []
   fwVersion: _typing.Optional[str] = None
   raidConfig: _typing.Optional[str] = None
   cacheConfig: _typing.Optional[str] = None
   cimProviderInfo: _typing.Optional[VsanHostCimProviderInfo] = None
   usedByVsan: _typing.Optional[bool] = None
   disks: list[VsanHclDiskInfo] = []
   issues: list[pyVmomi.vmodl.MethodFault] = []
   remediableIssues: list[str] = []
   driversOnHcl: list[pyVmomi.vim.vsan.VsanHclDriverInfo] = []
   fwAuxVersion: _typing.Optional[str] = None
   queueDepth: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   queueDepthOnHcl: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   queueDepthSupported: _typing.Optional[bool] = None
   diskMode: _typing.Optional[str] = None
   diskModeOnHcl: list[str] = []
   diskModeSupported: _typing.Optional[bool] = None
   toolName: _typing.Optional[str] = None
   toolVersion: _typing.Optional[str] = None
   productId: _typing.Optional[str] = None
   diskCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   vcgEntryInfo: list[VsanVcgDeviceInfo] = []
   controllerType: _typing.Optional[str] = None
   userSelectedVcgId: _typing.Optional[int] = None
   vsanCompatibility: list[str] = []


class VsanHclDiskInfo(pyVmomi.vmodl.DynamicData):
   deviceName: str
   model: _typing.Optional[str] = None
   isSsd: _typing.Optional[bool] = None
   vsanDisk: bool
   issues: list[pyVmomi.vmodl.MethodFault] = []
   remediableIssues: list[str] = []
   uuid: _typing.Optional[str] = None
   capacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   vsanCompatibility: list[str] = []


class VsanHclFirmwareFile(pyVmomi.vmodl.DynamicData):
   fileType: str
   filenameOrUrl: str
   sha1sum: str


class VsanHclFirmwareUpdateSpec(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   hbaDevice: str
   fwFiles: list[VsanHclFirmwareFile] = []
   allowDowngrade: _typing.Optional[bool] = None
   firmwareComponent: list[VsanHostFwComponent] = []


class VsanHclMemInfo(pyVmomi.vmodl.DynamicData):
   memorySize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   vsanHostCompatibility: list[str] = []


class VsanHclNicInfo(VsanHclCommonDeviceInfo):
   vmknic: _typing.Optional[str] = None
   useByVsan: _typing.Optional[bool] = None
   rdmaConfig: _typing.Optional[VsanNicRdmaInfo] = None
   vsanHostCompatibility: list[str] = []
   nicLinkSpeedInMbps: _typing.Optional[int] = None


class VsanHealthObjectStats(pyVmomi.vmodl.DynamicData):
   numAutoManagedObjects: pyVmomi.VmomiSupport.long
   numFTT3ManagedObjects: pyVmomi.VmomiSupport.long


class VsanHealthQuerySpec(pyVmomi.vmodl.DynamicData):
   includeAllRemoteClusters: _typing.Optional[bool] = None
   remoteClusterUuids: list[str] = []
   latencyOnly: _typing.Optional[bool] = None
   mode: _typing.Optional[str] = None


class VsanHealthSystem(pyVmomi.VmomiSupport.ManagedObject):
   def QueryVerifyNetworkSettings(self, peers: list[str], ROBOStretchedClusterWitnesses: list[str], vMotionPeers: list[str], spec: _typing.Optional[VsanHealthQuerySpec]) -> VsanNetworkHealthResult: ...
   def QueryCheckLimits(self, spec: _typing.Optional[VsanHostQueryCheckLimitsSpec]) -> VsanLimitHealthResult: ...
   def QueryHostInfoByUuids(self, uuids: list[str]) -> list[VsanQueryResultHostInfo]: ...
   def QueryAdvCfg(self, options: list[str], includeAllAdvOptions: _typing.Optional[bool], nonDefaultOnly: _typing.Optional[bool]) -> list[pyVmomi.vim.option.OptionValue]: ...
   def QueryRunIperfServer(self, multicast: bool, serverIp: _typing.Optional[str], durationSec: _typing.Optional[int]) -> VsanNetworkLoadTestResult: ...
   def QueryRunIperfClient(self, multicast: bool, serverIp: str, durationSec: _typing.Optional[int], spec: _typing.Optional[VsanIperfClientSpec]) -> VsanNetworkLoadTestResult: ...
   def QueryObjectHealthSummary(self, objUuids: list[str], includeObjUuids: _typing.Optional[bool], localHostOnly: _typing.Optional[bool], includeNonComplianceObjDetail: _typing.Optional[bool], spec: _typing.Optional[VsanHealthQuerySpec]) -> VsanObjectOverallHealth: ...
   def QueryPhysicalDiskHealthSummary(self) -> VsanPhysicalDiskHealthSummary: ...
   def QueryEncryptionHealthSummary(self) -> VsanEncryptionHealthSummary: ...
   def QueryFileServiceHealthSummary(self) -> VsanFileServiceHealthSummary: ...
   def PrepareVmdkLoadTest(self, runname: str, specs: list[VsanVmdkLoadTestSpec]) -> str: ...
   def RunVmdkLoadTest(self, runname: str, durationSec: int, specs: list[VsanVmdkLoadTestSpec]) -> list[VsanVmdkLoadTestResult]: ...
   def CleanupVmdkLoadTest(self, runname: str, specs: list[VsanVmdkLoadTestSpec]) -> str: ...
   def QueryVersion(self, displayVersion: _typing.Optional[bool]) -> str: ...
   def CheckClomdLiveness(self) -> bool: ...
   def RepairImmediateObjects(self, uuids: list[str], repairType: _typing.Optional[str]) -> VsanRepairObjectsResult: ...
   def GetHclInfo(self, includeVendorInfo: _typing.Optional[bool], vsanEsaEligibleDisksOnly: _typing.Optional[bool]) -> VsanHostHclInfo: ...
   def StartProactiveRebalance(self, timeSpan: _typing.Optional[int], varianceThreshold: _typing.Optional[float], timeThreshold: _typing.Optional[int], rateThreshold: _typing.Optional[int]) -> bool: ...
   def StopProactiveRebalance(self) -> bool: ...
   def GetProactiveRebalanceInfo(self) -> VsanProactiveRebalanceInfoEx: ...
   def WaitForVsanHealthGenerationIdChange(self, timeout: int) -> bool: ...
   def FlashScsiControllerFirmware(self, spec: VsanHclFirmwareUpdateSpec) -> pyVmomi.vim.Task: ...
   def CreateVmHealthTest(self, timeout: int) -> pyVmomi.vim.cluster.VsanHostCreateVmHealthTestResult: ...
   def QuerySmartStats(self, disks: list[str], includeAllDisks: _typing.Optional[bool]) -> VsanSmartStatsHostSummary: ...
   def QueryHostEMMState(self) -> VsanHostEMMSummary: ...
   def GetNetworkDiagnosticsHealthInfo(self) -> VsanNetworkDiagnosticsHealthInfo: ...


class VsanHostCimProviderInfo(pyVmomi.vmodl.DynamicData):
   cimProviderSupported: _typing.Optional[bool] = None
   installedCIMProvider: _typing.Optional[str] = None
   cimProviderOnHcl: list[str] = []
   cimProviderLinksOnHcl: list[pyVmomi.vim.vsan.VsanDownloadItem] = []


class VsanHostEMMSummary(pyVmomi.vmodl.DynamicData):
   hostname: _typing.Optional[str] = None
   inMaintenanceMode: _typing.Optional[bool] = None
   inDecomState: _typing.Optional[bool] = None


class VsanHostFwComponent(pyVmomi.vmodl.DynamicData):
   name: str
   url: _typing.Optional[str] = None
   sha1sum: _typing.Optional[str] = None
   currentVersion: _typing.Optional[str] = None
   suggestedVersion: _typing.Optional[str] = None
   componentID: list[str] = []


class VsanHostGlobalDedupConfigHealthSummary(pyVmomi.vmodl.DynamicData):
   hostname: _typing.Optional[str] = None
   health: _typing.Optional[str] = None


class VsanHostHciMeshDitEncryptionHealth(pyVmomi.vmodl.DynamicData):
   clusterUuid: str
   clusterName: str
   ownerVc: _typing.Optional[str] = None
   isLocalOwnerVc: _typing.Optional[bool] = None
   health: str
   issues: list[str] = []


class VsanHostHciMeshDitEncryptionHealthSummary(pyVmomi.vmodl.DynamicData):
   hostname: str
   clusterUuid: str
   clusterName: str
   ownerVc: str
   isLocalOwnerVc: _typing.Optional[bool] = None
   capable: _typing.Optional[bool] = None
   clusterHealths: list[VsanHostHciMeshDitEncryptionHealth] = []


class VsanHostHclInfo(pyVmomi.vmodl.DynamicData):
   hostname: str
   hclChecked: bool
   releaseName: _typing.Optional[str] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   controllers: list[VsanHclControllerInfo] = []
   pnics: list[VsanHclNicInfo] = []
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   computeResource: _typing.Optional[VsanHclComputeResource] = None
   vsanHostCompatibility: list[str] = []


class VsanHostHealthSystemStatusResult(pyVmomi.vmodl.DynamicData):
   hostname: str
   status: str
   issues: list[str] = []


class VsanHostHwDeviceId(pyVmomi.vmodl.DynamicData):
   pciId: DevicePciId
   productId: _typing.Optional[str] = None
   diskCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanHostIoInsightInfo(pyVmomi.vmodl.DynamicData):
   host: pyVmomi.vim.HostSystem
   ioinsightWorldId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   faultMessage: _typing.Optional[str] = None
   ioinsightInfo: _typing.Optional[VsanIoInsightInfo] = None

class VsanHostQueryCheckLimitsOptionType:
   pass


class VsanHostQueryCheckLimitsSpec(pyVmomi.vmodl.DynamicData):
   optionTypes: list[str] = []
   fetchAll: bool


class VsanHostReference(pyVmomi.vmodl.DynamicData):
   hostname: str


class VsanHostVirtualApplianceInfo(pyVmomi.vmodl.DynamicData):
   hostKey: pyVmomi.vim.HostSystem
   isVirtualApp: bool
   isDeployedFromOVF: _typing.Optional[bool] = None


class VsanHostVmdkLoadTestResult(pyVmomi.vmodl.DynamicData):
   hostname: str
   issueFound: bool
   faultMessage: _typing.Optional[str] = None
   vmdkResults: list[VsanVmdkLoadTestResult] = []


class VsanHwToVcgInfoMapping(pyVmomi.vmodl.DynamicData):
   vsanHostHwDeviceId: VsanHostHwDeviceId
   vcgId: int


class VsanInternalSystem(pyVmomi.VmomiSupport.ManagedObject):
   class CmmdsQuery(pyVmomi.vmodl.DynamicData):
      type: _typing.Optional[str] = None
      uuid: _typing.Optional[str] = None
      owner: _typing.Optional[str] = None

   class PolicyCost(pyVmomi.vmodl.DynamicData):
      changeDataSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      currentDataSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      tempDataSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      copyDataSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      changeFlashReadCacheSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      currentFlashReadCacheSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      currentDiskSpaceToAddressSpaceRatio: _typing.Optional[float] = None
      diskSpaceToAddressSpaceRatio: _typing.Optional[float] = None

   class PolicySatisfiability(pyVmomi.vmodl.DynamicData):
      uuid: _typing.Optional[str] = None
      isSatisfiable: bool
      reason: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None
      cost: _typing.Optional[PolicyCost] = None

   class PolicyChangeBatch(pyVmomi.vmodl.DynamicData):
      uuid: list[str] = []
      policy: _typing.Optional[str] = None

   class NewPolicyBatch(pyVmomi.vmodl.DynamicData):
      size: list[pyVmomi.VmomiSupport.long] = []
      policy: _typing.Optional[str] = None

   class VsanPhysicalDiskDiagnosticsResult(pyVmomi.vmodl.DynamicData):
      diskUuid: str
      success: bool
      failureReason: _typing.Optional[str] = None

   class DeleteVsanObjectsResult(pyVmomi.vmodl.DynamicData):
      uuid: str
      success: bool
      failureReason: list[pyVmomi.vmodl.LocalizableMessage] = []

   class VsanObjectOperationResult(pyVmomi.vmodl.DynamicData):
      uuid: str
      failureReason: list[pyVmomi.vmodl.LocalizableMessage] = []

   def QueryCmmds(self, queries: list[CmmdsQuery]) -> str: ...
   def QueryPhysicalVsanDisks(self, props: list[str]) -> str: ...
   def QueryVsanObjects(self, uuids: list[str]) -> str: ...
   def QueryObjectsOnPhysicalVsanDisk(self, disks: list[str]) -> str: ...
   def AbdicateDomOwnership(self, uuids: list[str]) -> list[str]: ...
   def QueryVsanStatistics(self, labels: list[str]) -> str: ...
   def ReconfigureDomObject(self, uuid: str, policy: str) -> None: ...
   def QuerySyncingVsanObjects(self, uuids: list[str]) -> str: ...
   def RunVsanPhysicalDiskDiagnostics(self, disks: list[str]) -> list[VsanPhysicalDiskDiagnosticsResult]: ...
   def GetVsanObjExtAttrs(self, uuids: list[str]) -> str: ...
   def ReconfigurationSatisfiable(self, pcbs: list[PolicyChangeBatch], ignoreSatisfiability: _typing.Optional[bool]) -> list[PolicySatisfiability]: ...
   def CanProvisionObjects(self, npbs: list[NewPolicyBatch], ignoreSatisfiability: _typing.Optional[bool]) -> list[PolicySatisfiability]: ...
   def DeleteVsanObjects(self, uuids: list[str], force: _typing.Optional[bool]) -> list[DeleteVsanObjectsResult]: ...
   def UpgradeVsanObjects(self, uuids: list[str], newVersion: int) -> list[VsanObjectOperationResult]: ...
   def QueryVsanObjectUuidsByFilter(self, uuids: list[str], limit: _typing.Optional[int], version: _typing.Optional[int]) -> list[str]: ...


class VsanIoInsightInfo(pyVmomi.vmodl.DynamicData):
   state: _typing.Optional[str] = None
   monitoredVMs: list[pyVmomi.vim.VirtualMachine] = []

class VsanIoInsightState:
   pass


class VsanIperfClientSpec(pyVmomi.vmodl.DynamicData):
   Reverse: bool


class VsanKmsHealth(pyVmomi.vmodl.DynamicData):
   serverName: str
   health: str
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   trustHealth: _typing.Optional[str] = None
   certHealth: _typing.Optional[str] = None
   certExpireDate: _typing.Optional[_datetime.datetime] = None


class VsanLicensedDiskResult(pyVmomi.vmodl.DynamicData):
   uuid: str
   name: str
   capacity: pyVmomi.VmomiSupport.long


class VsanLimitHealthResult(pyVmomi.vmodl.DynamicData):
   hostname: _typing.Optional[str] = None
   issueFound: bool
   maxComponents: int
   freeComponents: int
   componentLimitHealth: str
   lowestFreeDiskSpacePct: int
   usedDiskSpaceB: pyVmomi.VmomiSupport.long
   totalDiskSpaceB: pyVmomi.VmomiSupport.long
   diskFreeSpaceHealth: str
   reservedRcSizeB: pyVmomi.VmomiSupport.long
   totalRcSizeB: pyVmomi.VmomiSupport.long
   rcFreeReservationHealth: str
   totalLogicalSpaceB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   logicalSpaceUsedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   dedupMetadataSizeB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   diskTransientCapacityUsedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   dgTransientCapacityUsedB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   slackSpaceCapRequired: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   resyncPauseThreshold: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   spaceEfficiencyMetadataSizeB: _typing.Optional[pyVmomi.vim.vsan.VsanSpaceEfficiencyMetadataSize] = None
   hostRebuildCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   minSpaceRequiredForVsanOp: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   enforceCapResrvSpace: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   cdReservedSizeB: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanNetworkDiagnosticsHealthInfo(pyVmomi.vmodl.DynamicData):
   vnicInfo: list[VirtualNic] = []
   pnicTSOInfo: list[PnicTSOInfo] = []
   LACPInfo: list[LACPInfo] = []


class VsanNetworkHealthResult(pyVmomi.vmodl.DynamicData):
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   hostname: _typing.Optional[str] = None
   vsanVmknicPresent: _typing.Optional[bool] = None
   ipSubnets: list[str] = []
   issueFound: _typing.Optional[bool] = None
   peerHealth: list[VsanNetworkPeerHealthResult] = []
   vMotionHealth: list[VsanNetworkPeerHealthResult] = []
   multicastConfig: _typing.Optional[str] = None
   unicastConfig: _typing.Optional[str] = None
   inUnicast: _typing.Optional[bool] = None
   rdmaEnabled: _typing.Optional[bool] = None
   rdtConnProtocol: _typing.Optional[str] = None
   serverClusters: list[VsanServerClusterInfo] = []
   externalPeerHealth: list[VsanNetworkPeerHealthResult] = []


class VsanNetworkLoadTestResult(pyVmomi.vmodl.DynamicData):
   hostname: str
   status: _typing.Optional[str] = None
   client: bool
   bandwidthBps: pyVmomi.VmomiSupport.long
   totalBytes: pyVmomi.VmomiSupport.long
   lostDatagrams: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   lossPct: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   sentDatagrams: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   jitterMs: _typing.Optional[float] = None


class VsanNetworkPeerHealthResult(pyVmomi.vmodl.DynamicData):
   peer: _typing.Optional[str] = None
   peerHostname: _typing.Optional[str] = None
   peerVmknicName: _typing.Optional[str] = None
   smallPingTestSuccessPct: _typing.Optional[int] = None
   largePingTestSuccessPct: _typing.Optional[int] = None
   maxLatencyUs: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   onSameIpSubnet: _typing.Optional[bool] = None
   sourceVmknicName: _typing.Optional[str] = None
   connectivityHealthState: _typing.Optional[str] = None
   missingHeartBeatCount: _typing.Optional[int] = None


class VsanNicRdmaInfo(pyVmomi.vmodl.DynamicData):
   rdmaCapable: _typing.Optional[bool] = None
   rdmaProtocolCapable: _typing.Optional[str] = None
   dcbEnabled: _typing.Optional[bool] = None
   dcbMode: _typing.Optional[str] = None
   pfcEnabled: _typing.Optional[bool] = None
   pfcConfig: _typing.Optional[str] = None


class VsanObjectHealth(pyVmomi.vmodl.DynamicData):
   class VsanObjectHealthState(pyVmomi.VmomiSupport.Enum):
      inaccessible: _typing.ClassVar['VsanObjectHealthState'] = 'inaccessible'
      reducedavailabilitywithnorebuild: _typing.ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithnorebuild'
      reducedavailabilitywithnorebuilddelaytimer: _typing.ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithnorebuilddelaytimer'
      reducedavailabilitywithactiverebuild: _typing.ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithactiverebuild'
      datamove: _typing.ClassVar['VsanObjectHealthState'] = 'datamove'
      nonavailabilityrelatedreconfig: _typing.ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedreconfig'
      nonavailabilityrelatedincompliance: _typing.ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedincompliance'
      healthy: _typing.ClassVar['VsanObjectHealthState'] = 'healthy'
      reducedavailabilitywithpolicypending: _typing.ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithpolicypending'
      reducedavailabilitywithpolicypendingfailed: _typing.ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithpolicypendingfailed'
      reducedavailabilitywithpausedrebuild: _typing.ClassVar['VsanObjectHealthState'] = 'reducedavailabilitywithpausedrebuild'
      nonavailabilityrelatedincompliancewithpolicypending: _typing.ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedincompliancewithpolicypending'
      nonavailabilityrelatedincompliancewithpolicypendingfailed: _typing.ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedincompliancewithpolicypendingfailed'
      nonavailabilityrelatedincompliancewithpausedrebuild: _typing.ClassVar['VsanObjectHealthState'] = 'nonavailabilityrelatedincompliancewithpausedrebuild'
      remoteAccessible: _typing.ClassVar['VsanObjectHealthState'] = 'remoteAccessible'
      VsanObjectHealthState_Unknown: _typing.ClassVar['VsanObjectHealthState'] = 'VsanObjectHealthState_Unknown'

   numObjects: int
   health: _typing.Optional[str] = None
   objUuids: list[str] = []
   vsanClusterUuid: _typing.Optional[str] = None


class VsanObjectOverallHealth(pyVmomi.vmodl.DynamicData):
   objectHealthDetail: list[VsanObjectHealth] = []
   objectsComplianceDetail: list[pyVmomi.vim.cluster.StorageComplianceResult] = []
   objectVersionCompliance: _typing.Optional[bool] = None
   objectFormatChangeRequiredUuids: list[str] = []
   objectsRelayoutBytes: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   globalDedupStoreHealth: _typing.Optional[str] = None
   objectStats: _typing.Optional[VsanHealthObjectStats] = None
   vsanObjectsForObjectStoreVolumes: list[str] = []

class VsanPeerHostConnectivityHealthState:
   pass


class VsanPhysicalDiskHealth(pyVmomi.vmodl.DynamicData):
   name: str
   uuid: str
   inCmmds: bool
   inVsi: bool
   dedupScope: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   formatVersion: _typing.Optional[int] = None
   isAllFlash: _typing.Optional[int] = None
   congestionValue: _typing.Optional[int] = None
   congestionArea: _typing.Optional[str] = None
   congestionHealth: _typing.Optional[str] = None
   metadataHealth: _typing.Optional[str] = None
   operationalHealthDescription: _typing.Optional[str] = None
   operationalHealth: _typing.Optional[str] = None
   dedupUsageHealth: _typing.Optional[str] = None
   capacityHealth: _typing.Optional[str] = None
   summaryHealth: str
   capacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   usedCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   reservedCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   totalBytes: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   freeBytes: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   hashedBytes: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   dedupedBytes: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   scsiDisk: _typing.Optional[ScsiDisk] = None
   usedComponents: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maxComponents: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   compLimitHealth: _typing.Optional[str] = None
   encryptionEnabled: _typing.Optional[bool] = None
   kmsProviderId: _typing.Optional[str] = None
   kekId: _typing.Optional[str] = None
   dekGenerationId: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   encryptedUnlocked: _typing.Optional[bool] = None
   rebalanceResult: _typing.Optional[VsanDiskRebalanceResult] = None
   dekId: _typing.Optional[str] = None
   kekVerifierHealth: _typing.Optional[bool] = None
   dekVerifierHealth: _typing.Optional[bool] = None
   logicalCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   logicalCapacityUsed: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   logicalCapacityHealth: _typing.Optional[str] = None
   vsanDiskGroupUuid: _typing.Optional[str] = None
   dgLayoutIssue: _typing.Optional[bool] = None
   usedMetadataComponents: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maxMetadataComponents: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   pendingClusterDekId: _typing.Optional[str] = None
   dmekVerifierHealth: _typing.Optional[bool] = None


class VsanPhysicalDiskHealthSummary(pyVmomi.vmodl.DynamicData):
   overallHealth: str
   heapsWithIssues: list[VsanResourceHealth] = []
   slabsWithIssues: list[VsanResourceHealth] = []
   disks: list[VsanPhysicalDiskHealth] = []
   componentsWithIssues: list[VsanResourceHealth] = []
   hostname: _typing.Optional[str] = None
   hostDedupScope: _typing.Optional[int] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   licensedDisks: list[VsanLicensedDiskResult] = []


class VsanProactiveRebalanceInfoEx(pyVmomi.vmodl.DynamicData):
   running: _typing.Optional[bool] = None
   startTs: _typing.Optional[_datetime.datetime] = None
   stopTs: _typing.Optional[_datetime.datetime] = None
   varianceThreshold: _typing.Optional[float] = None
   timeThreshold: _typing.Optional[int] = None
   rateThreshold: _typing.Optional[int] = None
   hostname: _typing.Optional[str] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VsanQueryResultHostInfo(pyVmomi.vmodl.DynamicData):
   uuid: _typing.Optional[str] = None
   hostnameInCmmds: _typing.Optional[str] = None
   vsanIpv4Addresses: list[str] = []


class VsanRepairObjectsResult(pyVmomi.vmodl.DynamicData):
   inQueueObjects: list[str] = []
   failedRepairObjects: list[VsanFailedRepairObjectResult] = []
   notInQueueObjects: list[str] = []


class VsanResourceHealth(pyVmomi.vmodl.DynamicData):
   resource: str
   health: str
   description: _typing.Optional[str] = None


class VsanServerClusterInfo(pyVmomi.vmodl.DynamicData):
   cluster: _typing.Optional[pyVmomi.vim.ClusterComputeResource] = None
   peerHealth: list[VsanNetworkPeerHealthResult] = []
   membership: _typing.Optional[VsanClusterMembershipInfo] = None


class VsanSmartDiskStats(pyVmomi.vmodl.DynamicData):
   disk: str
   stats: list[VsanSmartParameter] = []
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VsanSmartParameter(pyVmomi.vmodl.DynamicData):
   parameter: _typing.Optional[str] = None
   value: _typing.Optional[int] = None
   threshold: _typing.Optional[int] = None
   worst: _typing.Optional[int] = None

class VsanSmartParameterType:
   pass


class VsanSmartStatsHostSummary(pyVmomi.vmodl.DynamicData):
   hostname: _typing.Optional[str] = None
   smartStats: list[VsanSmartDiskStats] = []


class VsanSystem(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def config(self) -> pyVmomi.vim.vsan.host.ConfigInfo: ...

   def QueryDisksForVsan(self, canonicalName: list[str]) -> list[pyVmomi.vim.vsan.host.DiskResult]: ...
   def AddDisks(self, disk: list[ScsiDisk]) -> pyVmomi.vim.Task: ...
   def InitializeDisks(self, mapping: list[pyVmomi.vim.vsan.host.DiskMapping]) -> pyVmomi.vim.Task: ...
   def RemoveDisk(self, disk: list[ScsiDisk], maintenanceSpec: _typing.Optional[MaintenanceSpec], timeout: _typing.Optional[int]) -> pyVmomi.vim.Task: ...
   def RemoveDiskMapping(self, mapping: list[pyVmomi.vim.vsan.host.DiskMapping], maintenanceSpec: _typing.Optional[MaintenanceSpec], timeout: _typing.Optional[int]) -> pyVmomi.vim.Task: ...
   def UnmountDiskMapping(self, mapping: list[pyVmomi.vim.vsan.host.DiskMapping]) -> pyVmomi.vim.Task: ...
   def Update(self, config: pyVmomi.vim.vsan.host.ConfigInfo) -> pyVmomi.vim.Task: ...
   def QueryHostStatus(self) -> pyVmomi.vim.vsan.host.ClusterStatus: ...
   def EvacuateNode(self, maintenanceSpec: MaintenanceSpec, timeout: int) -> pyVmomi.vim.Task: ...
   def RecommissionNode(self) -> pyVmomi.vim.Task: ...


class VsanSystemEx(pyVmomi.VmomiSupport.ManagedObject):
   def QueryWhatIfEvacuationResult(self, evacEntityUuid: str) -> pyVmomi.vim.vsan.host.VsanWhatIfEvacResult: ...
   def GetRuntimeStats(self, stats: list[str], clusterUuid: _typing.Optional[str]) -> pyVmomi.vim.vsan.host.RuntimeStats: ...
   def GetAboutInfoEx(self) -> pyVmomi.vim.vsan.host.AboutInfoEx: ...
   def QuerySyncingVsanObjects(self, uuids: list[str], start: _typing.Optional[int], limit: _typing.Optional[int], includeSummary: _typing.Optional[bool]) -> pyVmomi.vim.vsan.host.VsanSyncingObjectQueryResult: ...
   def QueryHostDrsStats(self, hostUuids: list[str], vms: list[str], hostIndex: _typing.Optional[int]) -> pyVmomi.vim.vsan.host.DrsStats: ...
   def UnmountDiskMappingEx(self, mappings: list[pyVmomi.vim.vsan.host.DiskMapping], maintenanceSpec: _typing.Optional[MaintenanceSpec], timeout: _typing.Optional[int], evacReason: _typing.Optional[str]) -> pyVmomi.vim.Task: ...
   def QueryHostStatusEx(self, clusterUuids: list[str]) -> list[pyVmomi.vim.vsan.host.ClusterStatus]: ...
   def WipeDisk(self, disks: list[str]) -> pyVmomi.vim.Task: ...
   def QueryWipeDiskStatus(self, disks: list[str]) -> list[pyVmomi.vim.vsan.host.WipeDiskStatus]: ...
   def AbortWipeDisk(self, disks: list[str]) -> list[pyVmomi.vim.vsan.host.AbortWipeDiskStatus]: ...


class VsanUpdateManager(pyVmomi.VmomiSupport.ManagedObject):
   def VsanVibScan(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], vibSpecs: list[pyVmomi.vim.vsan.VsanVibSpec]) -> list[pyVmomi.vim.vsan.VsanVibScanResult]: ...
   def VsanVibInstall(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource], vibSpecs: list[pyVmomi.vim.vsan.VsanVibSpec], scanResults: list[pyVmomi.vim.vsan.VsanVibScanResult], firmwareSpecs: list[VsanHclFirmwareUpdateSpec], maintenanceSpec: _typing.Optional[MaintenanceSpec], rolling: _typing.Optional[bool], noSigCheck: _typing.Optional[bool]) -> pyVmomi.vim.Task: ...
   def VsanVibInstallPreflightCheck(self, cluster: _typing.Optional[pyVmomi.vim.ComputeResource]) -> pyVmomi.vim.vsan.VsanVibInstallPreflightStatus: ...


class VsanVcgDeviceInfo(pyVmomi.vmodl.DynamicData):
   vcgId: int
   vcgModelName: _typing.Optional[str] = None


class VsanVcsaDeployerSystem(pyVmomi.VmomiSupport.ManagedObject):
   def PrepareVsanForVcsa(self, spec: pyVmomi.vim.vsan.VsanPrepareVsanForVcsaSpec) -> _typing.Optional[str]: ...
   def PostConfigForVcsa(self, spec: pyVmomi.vim.vsan.VsanVcPostDeployConfigSpec) -> _typing.Optional[str]: ...
   def VcsaGetBootstrapProgress(self, taskId: list[str]) -> list[pyVmomi.vim.vsan.VsanVcsaDeploymentProgress]: ...


class VsanVmdkIOLoadSpec(pyVmomi.vmodl.DynamicData):
   readPct: int
   oio: int
   iosizeB: int
   dataSizeMb: pyVmomi.VmomiSupport.long
   random: bool
   startOffsetB: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanVmdkLoadTestResult(pyVmomi.vmodl.DynamicData):
   success: bool
   faultMessage: _typing.Optional[str] = None
   spec: VsanVmdkLoadTestSpec
   actualDurationSec: _typing.Optional[int] = None
   totalBytes: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   iops: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   tputBps: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   avgLatencyUs: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maxLatencyUs: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   numIoAboveLatencyThreshold: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanVmdkLoadTestSpec(pyVmomi.vmodl.DynamicData):
   vmdkCreateSpec: _typing.Optional[pyVmomi.vim.VirtualDiskManager.FileBackedVirtualDiskSpec] = None
   vmdkIOSpec: _typing.Optional[VsanVmdkIOLoadSpec] = None
   vmdkIOSpecSequence: list[VsanVmdkIOLoadSpec] = []
   stepDurationSec: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class VsanVsanPcapResult(pyVmomi.vmodl.DynamicData):
   calltime: float
   vmknic: str
   tcpdumpFilter: str
   snaplen: int
   pkts: list[str] = []
   pcap: _typing.Optional[str] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   hostname: _typing.Optional[str] = None


class VvolDatastoreInfo(pyVmomi.vim.Datastore.Info):
   vvolDS: _typing.Optional[VvolVolume] = None


class VvolNQN(pyVmomi.vmodl.DynamicData):
   targetNQN: str
   storageArray: str
   online: bool


class VvolVolume(FileSystemVolume):
   class Specification(pyVmomi.vmodl.DynamicData):
      maxSizeInMB: pyVmomi.VmomiSupport.long
      volumeName: str
      vasaProviderInfo: list[pyVmomi.vim.VimVasaProviderInfo] = []
      storageArray: list[pyVmomi.vim.VasaStorageArray] = []
      uuid: str
      stretched: _typing.Optional[bool] = None

   class HostProtocolEndpoint(pyVmomi.vmodl.DynamicData):
      key: pyVmomi.vim.HostSystem
      protocolEndpoint: list[ProtocolEndpoint] = []

   class HostVvolNQN(pyVmomi.vmodl.DynamicData):
      host: _typing.Optional[pyVmomi.vim.HostSystem] = None
      vvolNQN: list[VvolNQN] = []

   scId: str
   hostPE: list[HostProtocolEndpoint] = []
   hostVvolNQN: list[HostVvolNQN] = []
   vasaProviderInfo: list[pyVmomi.vim.VimVasaProviderInfo] = []
   storageArray: list[pyVmomi.vim.VasaStorageArray] = []
   protocolEndpointType: _typing.Optional[str] = None
   vvolNQNFieldsAvailable: _typing.Optional[bool] = None
   stretched: _typing.Optional[bool] = None
