# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import CpuIdInfo

class Capability(DynamicData):
   class ReplayUnsupportedReason(Enum):
      incompatibleProduct: ClassVar['ReplayUnsupportedReason'] = 'incompatibleProduct'
      incompatibleCpu: ClassVar['ReplayUnsupportedReason'] = 'incompatibleCpu'
      hvDisabled: ClassVar['ReplayUnsupportedReason'] = 'hvDisabled'
      cpuidLimitSet: ClassVar['ReplayUnsupportedReason'] = 'cpuidLimitSet'
      oldBIOS: ClassVar['ReplayUnsupportedReason'] = 'oldBIOS'
      unknown: ClassVar['ReplayUnsupportedReason'] = 'unknown'

   class FtUnsupportedReason(Enum):
      vMotionNotLicensed: ClassVar['FtUnsupportedReason'] = 'vMotionNotLicensed'
      missingVMotionNic: ClassVar['FtUnsupportedReason'] = 'missingVMotionNic'
      missingFTLoggingNic: ClassVar['FtUnsupportedReason'] = 'missingFTLoggingNic'
      ftNotLicensed: ClassVar['FtUnsupportedReason'] = 'ftNotLicensed'
      haAgentIssue: ClassVar['FtUnsupportedReason'] = 'haAgentIssue'
      unsupportedProduct: ClassVar['FtUnsupportedReason'] = 'unsupportedProduct'
      cpuHvUnsupported: ClassVar['FtUnsupportedReason'] = 'cpuHvUnsupported'
      cpuHwmmuUnsupported: ClassVar['FtUnsupportedReason'] = 'cpuHwmmuUnsupported'
      cpuHvDisabled: ClassVar['FtUnsupportedReason'] = 'cpuHvDisabled'

   class VmDirectPathGen2UnsupportedReason(Enum):
      hostNptIncompatibleProduct: ClassVar['VmDirectPathGen2UnsupportedReason'] = 'hostNptIncompatibleProduct'
      hostNptIncompatibleHardware: ClassVar['VmDirectPathGen2UnsupportedReason'] = 'hostNptIncompatibleHardware'
      hostNptDisabled: ClassVar['VmDirectPathGen2UnsupportedReason'] = 'hostNptDisabled'

   class UnmapMethodSupported(Enum):
      priority: ClassVar['UnmapMethodSupported'] = 'priority'
      fixed: ClassVar['UnmapMethodSupported'] = 'fixed'
      dynamic: ClassVar['UnmapMethodSupported'] = 'dynamic'

   recursiveResourcePoolsSupported: bool
   cpuMemoryResourceConfigurationSupported: bool
   rebootSupported: bool
   shutdownSupported: bool
   vmotionSupported: bool
   standbySupported: bool
   ipmiSupported: Optional[bool] = None
   maxSupportedVMs: Optional[int] = None
   maxRunningVMs: Optional[int] = None
   maxSupportedVcpus: Optional[int] = None
   maxRegisteredVMs: Optional[int] = None
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
   vmotionAcrossNetworkSupported: Optional[bool] = None
   maxNumDisksSVMotion: Optional[int] = None
   maxVirtualDiskDescVersionSupported: Optional[int] = None
   hbrNicSelectionSupported: bool
   vrNfcNicSelectionSupported: bool
   recordReplaySupported: bool
   ftSupported: bool
   replayUnsupportedReason: Optional[str] = None
   replayCompatibilityIssues: list[str] = []
   smpFtSupported: bool
   ftCompatibilityIssues: list[str] = []
   smpFtCompatibilityIssues: list[str] = []
   maxVcpusPerFtVm: Optional[int] = None
   loginBySSLThumbprintSupported: Optional[bool] = None
   cloneFromSnapshotSupported: bool
   deltaDiskBackingsSupported: bool
   perVMNetworkTrafficShapingSupported: bool
   tpmSupported: bool
   tpmVersion: Optional[str] = None
   txtEnabled: Optional[bool] = None
   supportedCpuFeature: list[CpuIdInfo] = []
   virtualExecUsageSupported: bool
   storageIORMSupported: bool
   vmDirectPathGen2Supported: Optional[bool] = None
   vmDirectPathGen2UnsupportedReason: list[str] = []
   vmDirectPathGen2UnsupportedReasonExtended: Optional[str] = None
   supportedVmfsMajorVersion: list[int] = []
   vStorageCapable: bool
   snapshotRelayoutSupported: bool
   firewallIpRulesSupported: Optional[bool] = None
   servicePackageInfoSupported: Optional[bool] = None
   maxHostRunningVms: Optional[int] = None
   maxHostSupportedVcpus: Optional[int] = None
   vmfsDatastoreMountCapable: bool
   eightPlusHostVmfsSharedAccessSupported: bool
   nestedHVSupported: bool
   vPMCSupported: bool
   interVMCommunicationThroughVMCISupported: bool
   scheduledHardwareUpgradeSupported: Optional[bool] = None
   featureCapabilitiesSupported: bool
   latencySensitivitySupported: bool
   storagePolicySupported: Optional[bool] = None
   accel3dSupported: bool
   reliableMemoryAware: Optional[bool] = None
   multipleNetworkStackInstanceSupported: Optional[bool] = None
   messageBusProxySupported: Optional[bool] = None
   vsanSupported: Optional[bool] = None
   vFlashSupported: Optional[bool] = None
   hostAccessManagerSupported: Optional[bool] = None
   provisioningNicSelectionSupported: bool
   nfs41Supported: Optional[bool] = None
   nfs41Krb5iSupported: Optional[bool] = None
   turnDiskLocatorLedSupported: Optional[bool] = None
   virtualVolumeDatastoreSupported: Optional[bool] = None
   markAsSsdSupported: Optional[bool] = None
   markAsLocalSupported: Optional[bool] = None
   smartCardAuthenticationSupported: Optional[bool] = None
   pMemSupported: Optional[bool] = None
   pMemSnapshotSupported: Optional[bool] = None
   cryptoSupported: Optional[bool] = None
   oneKVolumeAPIsSupported: Optional[bool] = None
   gatewayOnNicSupported: Optional[bool] = None
   upitSupported: Optional[bool] = None
   cpuHwMmuSupported: Optional[bool] = None
   encryptedVMotionSupported: Optional[bool] = None
   encryptionChangeOnAddRemoveSupported: Optional[bool] = None
   encryptionHotOperationSupported: Optional[bool] = None
   encryptionWithSnapshotsSupported: Optional[bool] = None
   encryptionFaultToleranceSupported: Optional[bool] = None
   encryptionMemorySaveSupported: Optional[bool] = None
   encryptionRDMSupported: Optional[bool] = None
   encryptionVFlashSupported: Optional[bool] = None
   encryptionCBRCSupported: Optional[bool] = None
   encryptionHBRSupported: Optional[bool] = None
   ftEfiSupported: Optional[bool] = None
   unmapMethodSupported: Optional[str] = None
   maxMemMBPerFtVm: Optional[int] = None
   virtualMmuUsageIgnored: Optional[bool] = None
   virtualExecUsageIgnored: Optional[bool] = None
   vmCreateDateSupported: Optional[bool] = None
   vmfs3EOLSupported: Optional[bool] = None
   ftVmcpSupported: Optional[bool] = None
   quickBootSupported: Optional[bool] = None
   encryptedFtSupported: Optional[bool] = None
   assignableHardwareSupported: Optional[bool] = None
   suspendToMemorySupported: Optional[bool] = None
   useFeatureReqsForOldHWv: Optional[bool] = None
   markPerenniallyReservedSupported: Optional[bool] = None
   hppPspSupported: Optional[bool] = None
   deviceRebindWithoutRebootSupported: Optional[bool] = None
   storagePolicyChangeSupported: Optional[bool] = None
   precisionTimeProtocolSupported: Optional[bool] = None
   remoteDeviceVMotionSupported: Optional[bool] = None
   maxSupportedVmMemory: Optional[int] = None
   ahDeviceHintsSupported: Optional[bool] = None
   nvmeOverTcpSupported: Optional[bool] = None
   nvmeStorageFabricServicesSupported: Optional[bool] = None
   assignHwPciConfigSupported: Optional[bool] = None
   timeConfigSupported: Optional[bool] = None
   nvmeBatchOperationsSupported: Optional[bool] = None
   pMemFailoverSupported: Optional[bool] = None
   hostConfigEncryptionSupported: Optional[bool] = None
   maxSupportedSimultaneousThreads: Optional[int] = None
   ptpConfigSupported: Optional[bool] = None
   maxSupportedPtpPorts: Optional[int] = None
   sgxRegistrationSupported: Optional[bool] = None
   pMemIndependentSnapshotSupported: Optional[bool] = None
   iommuSLDirtyCapable: Optional[bool] = None
   vmknicBindingSupported: Optional[bool] = None
   ultralowFixedUnmapSupported: Optional[bool] = None
   nvmeVvolSupported: Optional[bool] = None
   fptHotplugSupported: Optional[bool] = None
   mconnectSupported: Optional[bool] = None
   vsanNicMgmtSupported: Optional[bool] = None
   vvolNQNSupported: Optional[bool] = None
   stretchedSCSupported: Optional[bool] = None
   vmknicBindingOnNFSv41: Optional[bool] = None
   vpStatusCheckSupported: Optional[bool] = None
   nConnectSupported: Optional[bool] = None
   userKeySupported: Optional[bool] = None
   ndcmSupported: Optional[bool] = None
   uefiSecureBoot: Optional[bool] = None
