# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import check as check
from . import customization as customization
from . import device as device
from . import guest as guest
from . import replication as replication

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.cluster
import pyVmomi.vim.dvs
import pyVmomi.vim.encryption
import pyVmomi.vim.ext
import pyVmomi.vim.host
import pyVmomi.vim.net
import pyVmomi.vim.option
import pyVmomi.vim.vApp
import pyVmomi.vim.vm.customization
import pyVmomi.vim.vm.device
import pyVmomi.vim.vm.guest
import pyVmomi.vim.vm.replication



class AffinityInfo(pyVmomi.vmodl.DynamicData):
   affinitySet: list[int] = []


class BaseIndependentFilterSpec(pyVmomi.vmodl.DynamicData):
   pass


class BootOptions(pyVmomi.vmodl.DynamicData):
   class NetworkBootProtocolType(pyVmomi.VmomiSupport.Enum):
      ipv4: _typing.ClassVar['NetworkBootProtocolType'] = 'ipv4'
      ipv6: _typing.ClassVar['NetworkBootProtocolType'] = 'ipv6'

   class BootableDevice(pyVmomi.vmodl.DynamicData):
      pass

   class BootableDiskDevice(BootableDevice):
      deviceKey: int

   class BootableEthernetDevice(BootableDevice):
      deviceKey: int

   class BootableFloppyDevice(BootableDevice):
      pass

   class BootableCdromDevice(BootableDevice):
      pass

   bootDelay: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   enterBIOSSetup: _typing.Optional[bool] = None
   efiSecureBootEnabled: _typing.Optional[bool] = None
   bootRetryEnabled: _typing.Optional[bool] = None
   bootRetryDelay: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   bootOrder: list[BootableDevice] = []
   networkBootProtocol: _typing.Optional[str] = None


class Capability(pyVmomi.vmodl.DynamicData):
   snapshotOperationsSupported: bool
   multipleSnapshotsSupported: bool
   snapshotConfigSupported: bool
   poweredOffSnapshotsSupported: bool
   memorySnapshotsSupported: bool
   revertToSnapshotSupported: bool
   quiescedSnapshotsSupported: bool
   disableSnapshotsSupported: bool
   lockSnapshotsSupported: bool
   consolePreferencesSupported: bool
   cpuFeatureMaskSupported: bool
   s1AcpiManagementSupported: bool
   settingScreenResolutionSupported: bool
   toolsAutoUpdateSupported: bool
   vmNpivWwnSupported: bool
   npivWwnOnNonRdmVmSupported: bool
   vmNpivWwnDisableSupported: bool
   vmNpivWwnUpdateSupported: bool
   swapPlacementSupported: bool
   toolsSyncTimeSupported: bool
   virtualMmuUsageSupported: bool
   diskSharesSupported: bool
   bootOptionsSupported: bool
   bootRetryOptionsSupported: bool
   settingVideoRamSizeSupported: bool
   settingDisplayTopologySupported: bool
   recordReplaySupported: bool
   changeTrackingSupported: bool
   multipleCoresPerSocketSupported: bool
   hostBasedReplicationSupported: bool
   guestAutoLockSupported: bool
   memoryReservationLockSupported: bool
   featureRequirementSupported: bool
   poweredOnMonitorTypeChangeSupported: bool
   seSparseDiskSupported: bool
   nestedHVSupported: bool
   vPMCSupported: bool
   secureBootSupported: _typing.Optional[bool] = None
   perVmEvcSupported: _typing.Optional[bool] = None
   virtualMmuUsageIgnored: _typing.Optional[bool] = None
   virtualExecUsageIgnored: _typing.Optional[bool] = None
   diskOnlySnapshotOnSuspendedVMSupported: _typing.Optional[bool] = None
   suspendToMemorySupported: _typing.Optional[bool] = None
   toolsSyncTimeAllowSupported: _typing.Optional[bool] = None
   sevSupported: _typing.Optional[bool] = None
   pmemFailoverSupported: _typing.Optional[bool] = None
   requireSgxAttestationSupported: _typing.Optional[bool] = None
   changeModeDisksSupported: _typing.Optional[bool] = None
   vendorDeviceGroupSupported: _typing.Optional[bool] = None
   sevSnpSupported: _typing.Optional[bool] = None
   tdxSupported: _typing.Optional[bool] = None
   ehvSecureBootSupported: _typing.Optional[bool] = None


class CdromInfo(TargetInfo):
   description: _typing.Optional[str] = None


class CertThumbprint(pyVmomi.vmodl.DynamicData):
   class HashAlgorithm(pyVmomi.VmomiSupport.Enum):
      sha256: _typing.ClassVar['HashAlgorithm'] = 'sha256'

   thumbprint: str
   hashAlgorithm: _typing.Optional[str] = None


class CloneSpec(pyVmomi.vmodl.DynamicData):
   class TpmProvisionPolicy(pyVmomi.VmomiSupport.Enum):
      copy: _typing.ClassVar['TpmProvisionPolicy'] = 'copy'
      replace: _typing.ClassVar['TpmProvisionPolicy'] = 'replace'

   location: RelocateSpec
   template: bool
   config: _typing.Optional[ConfigSpec] = None
   customization: _typing.Optional[pyVmomi.vim.vm.customization.Specification] = None
   powerOn: bool
   snapshot: _typing.Optional[Snapshot] = None
   memory: _typing.Optional[bool] = None
   tpmProvisionPolicy: _typing.Optional[str] = None


class ConfigInfo(pyVmomi.vmodl.DynamicData):
   class NpivWwnType(pyVmomi.VmomiSupport.Enum):
      vc: _typing.ClassVar['NpivWwnType'] = 'vc'
      host: _typing.ClassVar['NpivWwnType'] = 'host'
      external: _typing.ClassVar['NpivWwnType'] = 'external'

   class SwapPlacementType(pyVmomi.VmomiSupport.Enum):
      inherit: _typing.ClassVar['SwapPlacementType'] = 'inherit'
      vmDirectory: _typing.ClassVar['SwapPlacementType'] = 'vmDirectory'
      hostLocal: _typing.ClassVar['SwapPlacementType'] = 'hostLocal'

   class DatastoreUrlPair(pyVmomi.vmodl.DynamicData):
      name: str
      url: str

   class OverheadInfo(pyVmomi.vmodl.DynamicData):
      initialMemoryReservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      initialSwapReservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   changeVersion: str
   modified: _datetime.datetime
   name: str
   guestFullName: str
   version: str
   uuid: str
   createDate: _typing.Optional[_datetime.datetime] = None
   instanceUuid: _typing.Optional[str] = None
   npivNodeWorldWideName: list[pyVmomi.VmomiSupport.long] = []
   npivPortWorldWideName: list[pyVmomi.VmomiSupport.long] = []
   npivWorldWideNameType: _typing.Optional[str] = None
   npivDesiredNodeWwns: _typing.Optional[pyVmomi.VmomiSupport.short] = None
   npivDesiredPortWwns: _typing.Optional[pyVmomi.VmomiSupport.short] = None
   npivTemporaryDisabled: _typing.Optional[bool] = None
   npivOnNonRdmDisks: _typing.Optional[bool] = None
   locationId: _typing.Optional[str] = None
   template: bool
   guestId: str
   alternateGuestName: str
   annotation: _typing.Optional[str] = None
   files: FileInfo
   tools: _typing.Optional[ToolsConfigInfo] = None
   flags: FlagInfo
   consolePreferences: _typing.Optional[ConsolePreferences] = None
   defaultPowerOps: DefaultPowerOpInfo
   rebootPowerOff: _typing.Optional[bool] = None
   hardware: VirtualHardware
   vcpuConfig: list[VcpuConfig] = []
   cpuAllocation: _typing.Optional[pyVmomi.vim.ResourceAllocationInfo] = None
   memoryAllocation: _typing.Optional[pyVmomi.vim.ResourceAllocationInfo] = None
   latencySensitivity: _typing.Optional[pyVmomi.vim.LatencySensitivity] = None
   memoryHotAddEnabled: _typing.Optional[bool] = None
   cpuHotAddEnabled: _typing.Optional[bool] = None
   cpuHotRemoveEnabled: _typing.Optional[bool] = None
   hotPlugMemoryLimit: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   hotPlugMemoryIncrementSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   cpuAffinity: _typing.Optional[AffinityInfo] = None
   memoryAffinity: _typing.Optional[AffinityInfo] = None
   networkShaper: _typing.Optional[NetworkShaperInfo] = None
   extraConfig: list[pyVmomi.vim.option.OptionValue] = []
   cpuFeatureMask: list[pyVmomi.vim.host.CpuIdInfo] = []
   datastoreUrl: list[DatastoreUrlPair] = []
   swapPlacement: _typing.Optional[str] = None
   bootOptions: _typing.Optional[BootOptions] = None
   ftInfo: _typing.Optional[FaultToleranceConfigInfo] = None
   repConfig: _typing.Optional[ReplicationConfigSpec] = None
   vAppConfig: _typing.Optional[pyVmomi.vim.vApp.VmConfigInfo] = None
   vAssertsEnabled: _typing.Optional[bool] = None
   changeTrackingEnabled: _typing.Optional[bool] = None
   firmware: _typing.Optional[str] = None
   maxMksConnections: _typing.Optional[int] = None
   guestAutoLockEnabled: _typing.Optional[bool] = None
   managedBy: _typing.Optional[pyVmomi.vim.ext.ManagedByInfo] = None
   memoryReservationLockedToMax: _typing.Optional[bool] = None
   initialOverhead: _typing.Optional[OverheadInfo] = None
   nestedHVEnabled: _typing.Optional[bool] = None
   vPMCEnabled: _typing.Optional[bool] = None
   scheduledHardwareUpgradeInfo: _typing.Optional[ScheduledHardwareUpgradeInfo] = None
   forkConfigInfo: _typing.Optional[ForkConfigInfo] = None
   vFlashCacheReservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   vmxConfigChecksum: _typing.Optional[pyVmomi.VmomiSupport.binary] = None
   messageBusTunnelEnabled: _typing.Optional[bool] = None
   vmStorageObjectId: _typing.Optional[str] = None
   swapStorageObjectId: _typing.Optional[str] = None
   keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None
   guestIntegrityInfo: _typing.Optional[GuestIntegrityInfo] = None
   migrateEncryption: _typing.Optional[str] = None
   sgxInfo: _typing.Optional[SgxInfo] = None
   contentLibItemInfo: _typing.Optional[ContentLibraryItemInfo] = None
   ftEncryptionMode: _typing.Optional[str] = None
   guestMonitoringModeInfo: _typing.Optional[GuestMonitoringModeInfo] = None
   sevEnabled: _typing.Optional[bool] = None
   numaInfo: _typing.Optional[VirtualNumaInfo] = None
   pmemFailoverEnabled: _typing.Optional[bool] = None
   vmxStatsCollectionEnabled: _typing.Optional[bool] = None
   vmOpNotificationToAppEnabled: _typing.Optional[bool] = None
   vmOpNotificationTimeout: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   deviceSwap: _typing.Optional[VirtualDeviceSwap] = None
   pmem: _typing.Optional[VirtualPMem] = None
   deviceGroups: _typing.Optional[VirtualDeviceGroups] = None
   fixedPassthruHotPlugEnabled: _typing.Optional[bool] = None
   metroFtEnabled: _typing.Optional[bool] = None
   vmxRuntimeConfig: list[pyVmomi.vim.option.OptionValue] = []
   metroFtHostGroup: _typing.Optional[str] = None
   tdxEnabled: _typing.Optional[bool] = None
   sevSnpEnabled: _typing.Optional[bool] = None
   guestArchitecture: _typing.Optional[str] = None


class ConfigOption(pyVmomi.vmodl.DynamicData):
   version: str
   description: str
   guestOSDescriptor: list[GuestOsDescriptor] = []
   guestOSDefaultIndex: int
   hardwareOptions: VirtualHardwareOption
   capabilities: Capability
   datastore: DatastoreOption
   defaultDevice: list[pyVmomi.vim.vm.device.VirtualDevice] = []
   supportedMonitorType: list[str] = []
   supportedOvfEnvironmentTransport: list[str] = []
   supportedOvfInstallTransport: list[str] = []
   propertyRelations: list[PropertyRelation] = []


class ConfigOptionDescriptor(pyVmomi.vmodl.DynamicData):
   key: str
   description: _typing.Optional[str] = None
   host: list[pyVmomi.vim.HostSystem] = []
   createSupported: bool
   defaultConfigOption: bool
   runSupported: bool
   upgradeSupported: bool


class ConfigSpec(pyVmomi.vmodl.DynamicData):
   class NpivWwnOp(pyVmomi.VmomiSupport.Enum):
      generate: _typing.ClassVar['NpivWwnOp'] = 'generate'
      set: _typing.ClassVar['NpivWwnOp'] = 'set'
      remove: _typing.ClassVar['NpivWwnOp'] = 'remove'
      extend: _typing.ClassVar['NpivWwnOp'] = 'extend'

   class EncryptedFtModes(pyVmomi.VmomiSupport.Enum):
      ftEncryptionDisabled: _typing.ClassVar['EncryptedFtModes'] = 'ftEncryptionDisabled'
      ftEncryptionOpportunistic: _typing.ClassVar['EncryptedFtModes'] = 'ftEncryptionOpportunistic'
      ftEncryptionRequired: _typing.ClassVar['EncryptedFtModes'] = 'ftEncryptionRequired'

   class EncryptedVMotionModes(pyVmomi.VmomiSupport.Enum):
      disabled: _typing.ClassVar['EncryptedVMotionModes'] = 'disabled'
      opportunistic: _typing.ClassVar['EncryptedVMotionModes'] = 'opportunistic'
      required: _typing.ClassVar['EncryptedVMotionModes'] = 'required'

   class CpuIdInfoSpec(pyVmomi.vim.option.ArrayUpdateSpec):
      info: _typing.Optional[pyVmomi.vim.host.CpuIdInfo] = None

   changeVersion: _typing.Optional[str] = None
   name: _typing.Optional[str] = None
   version: _typing.Optional[str] = None
   createDate: _typing.Optional[_datetime.datetime] = None
   uuid: _typing.Optional[str] = None
   instanceUuid: _typing.Optional[str] = None
   npivNodeWorldWideName: list[pyVmomi.VmomiSupport.long] = []
   npivPortWorldWideName: list[pyVmomi.VmomiSupport.long] = []
   npivWorldWideNameType: _typing.Optional[str] = None
   npivDesiredNodeWwns: _typing.Optional[pyVmomi.VmomiSupport.short] = None
   npivDesiredPortWwns: _typing.Optional[pyVmomi.VmomiSupport.short] = None
   npivTemporaryDisabled: _typing.Optional[bool] = None
   npivOnNonRdmDisks: _typing.Optional[bool] = None
   npivWorldWideNameOp: _typing.Optional[str] = None
   locationId: _typing.Optional[str] = None
   guestId: _typing.Optional[str] = None
   alternateGuestName: _typing.Optional[str] = None
   annotation: _typing.Optional[str] = None
   files: _typing.Optional[FileInfo] = None
   tools: _typing.Optional[ToolsConfigInfo] = None
   flags: _typing.Optional[FlagInfo] = None
   consolePreferences: _typing.Optional[ConsolePreferences] = None
   powerOpInfo: _typing.Optional[DefaultPowerOpInfo] = None
   rebootPowerOff: _typing.Optional[bool] = None
   numCPUs: _typing.Optional[int] = None
   vcpuConfig: list[VcpuConfig] = []
   numCoresPerSocket: _typing.Optional[int] = None
   memoryMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   memoryHotAddEnabled: _typing.Optional[bool] = None
   cpuHotAddEnabled: _typing.Optional[bool] = None
   cpuHotRemoveEnabled: _typing.Optional[bool] = None
   virtualICH7MPresent: _typing.Optional[bool] = None
   virtualSMCPresent: _typing.Optional[bool] = None
   deviceChange: list[pyVmomi.vim.vm.device.VirtualDeviceSpec] = []
   cpuAllocation: _typing.Optional[pyVmomi.vim.ResourceAllocationInfo] = None
   memoryAllocation: _typing.Optional[pyVmomi.vim.ResourceAllocationInfo] = None
   latencySensitivity: _typing.Optional[pyVmomi.vim.LatencySensitivity] = None
   cpuAffinity: _typing.Optional[AffinityInfo] = None
   memoryAffinity: _typing.Optional[AffinityInfo] = None
   networkShaper: _typing.Optional[NetworkShaperInfo] = None
   cpuFeatureMask: list[CpuIdInfoSpec] = []
   extraConfig: list[pyVmomi.vim.option.OptionValue] = []
   swapPlacement: _typing.Optional[str] = None
   bootOptions: _typing.Optional[BootOptions] = None
   vAppConfig: _typing.Optional[pyVmomi.vim.vApp.VmConfigSpec] = None
   ftInfo: _typing.Optional[FaultToleranceConfigInfo] = None
   repConfig: _typing.Optional[ReplicationConfigSpec] = None
   vAppConfigRemoved: _typing.Optional[bool] = None
   vAssertsEnabled: _typing.Optional[bool] = None
   changeTrackingEnabled: _typing.Optional[bool] = None
   firmware: _typing.Optional[str] = None
   maxMksConnections: _typing.Optional[int] = None
   guestAutoLockEnabled: _typing.Optional[bool] = None
   managedBy: _typing.Optional[pyVmomi.vim.ext.ManagedByInfo] = None
   memoryReservationLockedToMax: _typing.Optional[bool] = None
   nestedHVEnabled: _typing.Optional[bool] = None
   vPMCEnabled: _typing.Optional[bool] = None
   scheduledHardwareUpgradeInfo: _typing.Optional[ScheduledHardwareUpgradeInfo] = None
   vmProfile: list[ProfileSpec] = []
   messageBusTunnelEnabled: _typing.Optional[bool] = None
   crypto: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None
   migrateEncryption: _typing.Optional[str] = None
   sgxInfo: _typing.Optional[SgxInfo] = None
   ftEncryptionMode: _typing.Optional[str] = None
   guestMonitoringModeInfo: _typing.Optional[GuestMonitoringModeInfo] = None
   sevEnabled: _typing.Optional[bool] = None
   virtualNuma: _typing.Optional[VirtualNuma] = None
   motherboardLayout: _typing.Optional[str] = None
   pmemFailoverEnabled: _typing.Optional[bool] = None
   vmxStatsCollectionEnabled: _typing.Optional[bool] = None
   vmOpNotificationToAppEnabled: _typing.Optional[bool] = None
   vmOpNotificationTimeout: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   deviceSwap: _typing.Optional[VirtualDeviceSwap] = None
   simultaneousThreads: _typing.Optional[int] = None
   pmem: _typing.Optional[VirtualPMem] = None
   deviceGroups: _typing.Optional[VirtualDeviceGroups] = None
   fixedPassthruHotPlugEnabled: _typing.Optional[bool] = None
   metroFtEnabled: _typing.Optional[bool] = None
   metroFtHostGroup: _typing.Optional[str] = None
   tdxEnabled: _typing.Optional[bool] = None
   sevSnpEnabled: _typing.Optional[bool] = None
   tagSpecs: list[pyVmomi.vim.TagSpec] = []
   vmPlacementPolicies: list[VmPlacementPolicy] = []


class ConfigTarget(pyVmomi.vmodl.DynamicData):
   numCpus: int
   numCpuCores: int
   numNumaNodes: int
   maxCpusPerHost: _typing.Optional[int] = None
   smcPresent: bool
   datastore: list[DatastoreInfo] = []
   network: list[NetworkInfo] = []
   opaqueNetwork: list[OpaqueNetworkInfo] = []
   distributedVirtualPortgroup: list[pyVmomi.vim.dvs.DistributedVirtualPortgroupInfo] = []
   distributedVirtualSwitch: list[pyVmomi.vim.dvs.DistributedVirtualSwitchInfo] = []
   subnetInfo: list[SubnetInfo] = []
   cdRom: list[CdromInfo] = []
   serial: list[SerialInfo] = []
   parallel: list[ParallelInfo] = []
   sound: list[SoundInfo] = []
   usb: list[UsbInfo] = []
   floppy: list[FloppyInfo] = []
   legacyNetworkInfo: list[LegacyNetworkSwitchInfo] = []
   scsiPassthrough: list[ScsiPassthroughInfo] = []
   scsiDisk: list[ScsiDiskDeviceInfo] = []
   ideDisk: list[IdeDiskDeviceInfo] = []
   maxMemMBOptimalPerf: int
   supportedMaxMemMB: _typing.Optional[int] = None
   resourcePool: _typing.Optional[pyVmomi.vim.ResourcePool.RuntimeInfo] = None
   autoVmotion: _typing.Optional[bool] = None
   pciPassthrough: list[PciPassthroughInfo] = []
   sriov: list[SriovInfo] = []
   vFlashModule: list[VFlashModuleInfo] = []
   sharedGpuPassthroughTypes: list[PciSharedGpuPassthroughInfo] = []
   availablePersistentMemoryReservationMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   dynamicPassthrough: list[DynamicPassthroughInfo] = []
   sgxTargetInfo: _typing.Optional[SgxTargetInfo] = None
   precisionClockInfo: list[PrecisionClockInfo] = []
   sevSupported: _typing.Optional[bool] = None
   vgpuDeviceInfo: list[VgpuDeviceInfo] = []
   vgpuProfileInfo: list[VgpuProfileInfo] = []
   vendorDeviceGroupInfo: list[VendorDeviceGroupInfo] = []
   maxSimultaneousThreads: _typing.Optional[int] = None
   dvxClassInfo: list[DvxClassInfo] = []
   sevSnpSupported: _typing.Optional[bool] = None
   tdxSupported: _typing.Optional[bool] = None
   vMotionBandwidth: list[pyVmomi.VmomiSupport.long] = []


class ConsolePreferences(pyVmomi.vmodl.DynamicData):
   powerOnWhenOpened: _typing.Optional[bool] = None
   enterFullScreenOnPowerOn: _typing.Optional[bool] = None
   closeOnPowerOffOrSuspend: _typing.Optional[bool] = None


class ContentLibraryItemInfo(pyVmomi.vmodl.DynamicData):
   contentLibraryItemUuid: str
   contentLibraryItemVersion: _typing.Optional[str] = None


class DatastoreInfo(TargetInfo):
   datastore: pyVmomi.vim.Datastore.Summary
   capability: pyVmomi.vim.Datastore.Capability
   maxFileSize: pyVmomi.VmomiSupport.long
   maxVirtualDiskCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maxPhysicalRDMFileSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maxVirtualRDMFileSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   mode: str
   vStorageSupport: _typing.Optional[str] = None
   supportedVDiskFormats: list[str] = []


class DatastoreOption(pyVmomi.vmodl.DynamicData):
   class FileSystemVolumeOption(pyVmomi.vmodl.DynamicData):
      fileSystemType: type
      majorVersion: _typing.Optional[int] = None

   unsupportedVolumes: list[FileSystemVolumeOption] = []


class DefaultPowerOpInfo(pyVmomi.vmodl.DynamicData):
   class PowerOpType(pyVmomi.VmomiSupport.Enum):
      soft: _typing.ClassVar['PowerOpType'] = 'soft'
      hard: _typing.ClassVar['PowerOpType'] = 'hard'
      preset: _typing.ClassVar['PowerOpType'] = 'preset'

   class StandbyActionType(pyVmomi.VmomiSupport.Enum):
      checkpoint: _typing.ClassVar['StandbyActionType'] = 'checkpoint'
      powerOnSuspend: _typing.ClassVar['StandbyActionType'] = 'powerOnSuspend'

   powerOffType: _typing.Optional[str] = None
   suspendType: _typing.Optional[str] = None
   resetType: _typing.Optional[str] = None
   defaultPowerOffType: _typing.Optional[str] = None
   defaultSuspendType: _typing.Optional[str] = None
   defaultResetType: _typing.Optional[str] = None
   standbyAction: _typing.Optional[str] = None

class DefaultProfileSpec(ProfileSpec):
   pass


class DefinedProfileSpec(ProfileSpec):
   profileId: str
   replicationSpec: _typing.Optional[pyVmomi.vim.vm.replication.ReplicationSpec] = None
   profileData: _typing.Optional[ProfileRawData] = None
   profileParams: list[pyVmomi.vim.KeyValue] = []


class DeviceRuntimeInfo(pyVmomi.vmodl.DynamicData):
   class DeviceRuntimeState(pyVmomi.vmodl.DynamicData):
      pass

   class VirtualEthernetCardRuntimeState(DeviceRuntimeState):
      class VmDirectPathGen2InactiveReasonVm(pyVmomi.VmomiSupport.Enum):
         vmNptIncompatibleGuest: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleGuest'
         vmNptIncompatibleGuestDriver: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleGuestDriver'
         vmNptIncompatibleAdapterType: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleAdapterType'
         vmNptDisabledOrDisconnectedAdapter: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptDisabledOrDisconnectedAdapter'
         vmNptIncompatibleAdapterFeatures: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleAdapterFeatures'
         vmNptIncompatibleBackingType: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptIncompatibleBackingType'
         vmNptInsufficientMemoryReservation: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptInsufficientMemoryReservation'
         vmNptFaultToleranceOrRecordReplayConfigured: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptFaultToleranceOrRecordReplayConfigured'
         vmNptConflictingIOChainConfigured: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptConflictingIOChainConfigured'
         vmNptMonitorBlocks: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptMonitorBlocks'
         vmNptConflictingOperationInProgress: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptConflictingOperationInProgress'
         vmNptRuntimeError: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptRuntimeError'
         vmNptOutOfIntrVector: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptOutOfIntrVector'
         vmNptVMCIActive: _typing.ClassVar['VmDirectPathGen2InactiveReasonVm'] = 'vmNptVMCIActive'

      class VmDirectPathGen2InactiveReasonOther(pyVmomi.VmomiSupport.Enum):
         vmNptIncompatibleHost: _typing.ClassVar['VmDirectPathGen2InactiveReasonOther'] = 'vmNptIncompatibleHost'
         vmNptIncompatibleNetwork: _typing.ClassVar['VmDirectPathGen2InactiveReasonOther'] = 'vmNptIncompatibleNetwork'

      vmDirectPathGen2Active: _typing.Optional[bool] = None
      vmDirectPathGen2InactiveReasonVm: list[str] = []
      vmDirectPathGen2InactiveReasonOther: list[str] = []
      vmDirectPathGen2InactiveReasonExtended: _typing.Optional[str] = None
      uptv2Active: _typing.Optional[bool] = None
      uptv2InactiveReasonVm: list[str] = []
      uptv2InactiveReasonOther: list[str] = []
      reservationStatus: _typing.Optional[str] = None
      attachmentStatus: _typing.Optional[str] = None
      featureRequirement: list[FeatureRequirement] = []

   runtimeState: DeviceRuntimeState
   key: int


class DiskDeviceInfo(TargetInfo):
   capacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   vm: list[pyVmomi.vim.VirtualMachine] = []


class DvxClassInfo(pyVmomi.vmodl.DynamicData):
   deviceClass: pyVmomi.vim.ElementDescription
   vendorName: str
   sriovNic: bool
   configParams: list[pyVmomi.vim.option.OptionDef] = []


class DynamicPassthroughInfo(TargetInfo):
   vendorName: str
   deviceName: str
   customLabel: _typing.Optional[str] = None
   vendorId: int
   deviceId: int

class EmptyIndependentFilterSpec(BaseIndependentFilterSpec):
   pass

class EmptyProfileSpec(ProfileSpec):
   pass


class FaultToleranceConfigInfo(pyVmomi.vmodl.DynamicData):
   role: int
   instanceUuids: list[str] = []
   configPaths: list[str] = []
   orphaned: _typing.Optional[bool] = None


class FaultToleranceConfigSpec(pyVmomi.vmodl.DynamicData):
   metaDataPath: _typing.Optional[FaultToleranceMetaSpec] = None
   secondaryVmSpec: _typing.Optional[FaultToleranceVMConfigSpec] = None
   metroFtEnabled: _typing.Optional[bool] = None
   metroFtHostGroup: _typing.Optional[str] = None


class FaultToleranceMetaSpec(pyVmomi.vmodl.DynamicData):
   metaDataDatastore: pyVmomi.vim.Datastore


class FaultTolerancePrimaryConfigInfo(FaultToleranceConfigInfo):
   secondaries: list[pyVmomi.vim.VirtualMachine] = []


class FaultToleranceSecondaryConfigInfo(FaultToleranceConfigInfo):
   primaryVM: pyVmomi.vim.VirtualMachine


class FaultToleranceSecondaryOpResult(pyVmomi.vmodl.DynamicData):
   vm: pyVmomi.vim.VirtualMachine
   powerOnAttempted: bool
   powerOnResult: _typing.Optional[pyVmomi.vim.cluster.PowerOnVmResult] = None


class FaultToleranceVMConfigSpec(pyVmomi.vmodl.DynamicData):
   class FaultToleranceDiskSpec(pyVmomi.vmodl.DynamicData):
      disk: pyVmomi.vim.vm.device.VirtualDevice
      datastore: pyVmomi.vim.Datastore

   vmConfig: _typing.Optional[pyVmomi.vim.Datastore] = None
   disks: list[FaultToleranceDiskSpec] = []


class FeatureRequirement(pyVmomi.vmodl.DynamicData):
   key: str
   featureName: str
   value: str


class FileInfo(pyVmomi.vmodl.DynamicData):
   vmPathName: _typing.Optional[str] = None
   snapshotDirectory: _typing.Optional[str] = None
   suspendDirectory: _typing.Optional[str] = None
   logDirectory: _typing.Optional[str] = None
   ftMetadataDirectory: _typing.Optional[str] = None


class FileLayout(pyVmomi.vmodl.DynamicData):
   class DiskLayout(pyVmomi.vmodl.DynamicData):
      key: int
      diskFile: list[str] = []

   class SnapshotLayout(pyVmomi.vmodl.DynamicData):
      key: Snapshot
      snapshotFile: list[str] = []

   configFile: list[str] = []
   logFile: list[str] = []
   disk: list[DiskLayout] = []
   snapshot: list[SnapshotLayout] = []
   swapFile: _typing.Optional[str] = None


class FileLayoutEx(pyVmomi.vmodl.DynamicData):
   class FileType(pyVmomi.VmomiSupport.Enum):
      config: _typing.ClassVar['FileType'] = 'config'
      extendedConfig: _typing.ClassVar['FileType'] = 'extendedConfig'
      diskDescriptor: _typing.ClassVar['FileType'] = 'diskDescriptor'
      diskExtent: _typing.ClassVar['FileType'] = 'diskExtent'
      digestDescriptor: _typing.ClassVar['FileType'] = 'digestDescriptor'
      digestExtent: _typing.ClassVar['FileType'] = 'digestExtent'
      diskReplicationState: _typing.ClassVar['FileType'] = 'diskReplicationState'
      log: _typing.ClassVar['FileType'] = 'log'
      stat: _typing.ClassVar['FileType'] = 'stat'
      namespaceData: _typing.ClassVar['FileType'] = 'namespaceData'
      dataSetsDiskModeStore: _typing.ClassVar['FileType'] = 'dataSetsDiskModeStore'
      dataSetsVmModeStore: _typing.ClassVar['FileType'] = 'dataSetsVmModeStore'
      nvram: _typing.ClassVar['FileType'] = 'nvram'
      snapshotData: _typing.ClassVar['FileType'] = 'snapshotData'
      snapshotMemory: _typing.ClassVar['FileType'] = 'snapshotMemory'
      snapshotList: _typing.ClassVar['FileType'] = 'snapshotList'
      snapshotManifestList: _typing.ClassVar['FileType'] = 'snapshotManifestList'
      suspend: _typing.ClassVar['FileType'] = 'suspend'
      suspendMemory: _typing.ClassVar['FileType'] = 'suspendMemory'
      swap: _typing.ClassVar['FileType'] = 'swap'
      uwswap: _typing.ClassVar['FileType'] = 'uwswap'
      core: _typing.ClassVar['FileType'] = 'core'
      screenshot: _typing.ClassVar['FileType'] = 'screenshot'
      ftMetadata: _typing.ClassVar['FileType'] = 'ftMetadata'
      guestCustomization: _typing.ClassVar['FileType'] = 'guestCustomization'

   class FileInfo(pyVmomi.vmodl.DynamicData):
      key: int
      name: str
      type: str
      size: pyVmomi.VmomiSupport.long
      uniqueSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      backingObjectId: _typing.Optional[str] = None
      accessible: _typing.Optional[bool] = None

   class DiskUnit(pyVmomi.vmodl.DynamicData):
      fileKey: list[int] = []

   class DiskLayout(pyVmomi.vmodl.DynamicData):
      key: int
      virtualDiskFormat: _typing.Optional[str] = None
      chain: list[DiskUnit] = []

   class SnapshotLayout(pyVmomi.vmodl.DynamicData):
      key: Snapshot
      dataKey: int
      memoryKey: int
      disk: list[DiskLayout] = []

   file: list[FileInfo] = []
   disk: list[DiskLayout] = []
   snapshot: list[SnapshotLayout] = []
   timestamp: _datetime.datetime


class FlagInfo(pyVmomi.vmodl.DynamicData):
   class HtSharing(pyVmomi.VmomiSupport.Enum):
      any: _typing.ClassVar['HtSharing'] = 'any'
      none: _typing.ClassVar['HtSharing'] = 'none'
      internal: _typing.ClassVar['HtSharing'] = 'internal'

   class PowerOffBehavior(pyVmomi.VmomiSupport.Enum):
      powerOff: _typing.ClassVar['PowerOffBehavior'] = 'powerOff'
      revert: _typing.ClassVar['PowerOffBehavior'] = 'revert'
      prompt: _typing.ClassVar['PowerOffBehavior'] = 'prompt'
      take: _typing.ClassVar['PowerOffBehavior'] = 'take'

   class MonitorType(pyVmomi.VmomiSupport.Enum):
      release: _typing.ClassVar['MonitorType'] = 'release'
      debug: _typing.ClassVar['MonitorType'] = 'debug'
      stats: _typing.ClassVar['MonitorType'] = 'stats'

   class VirtualMmuUsage(pyVmomi.VmomiSupport.Enum):
      automatic: _typing.ClassVar['VirtualMmuUsage'] = 'automatic'
      on: _typing.ClassVar['VirtualMmuUsage'] = 'on'
      off: _typing.ClassVar['VirtualMmuUsage'] = 'off'

   class VirtualExecUsage(pyVmomi.VmomiSupport.Enum):
      hvAuto: _typing.ClassVar['VirtualExecUsage'] = 'hvAuto'
      hvOn: _typing.ClassVar['VirtualExecUsage'] = 'hvOn'
      hvOff: _typing.ClassVar['VirtualExecUsage'] = 'hvOff'

   disableAcceleration: _typing.Optional[bool] = None
   enableLogging: _typing.Optional[bool] = None
   useToe: _typing.Optional[bool] = None
   runWithDebugInfo: _typing.Optional[bool] = None
   monitorType: _typing.Optional[str] = None
   htSharing: _typing.Optional[str] = None
   snapshotDisabled: _typing.Optional[bool] = None
   snapshotLocked: _typing.Optional[bool] = None
   diskUuidEnabled: _typing.Optional[bool] = None
   virtualMmuUsage: _typing.Optional[str] = None
   virtualExecUsage: _typing.Optional[str] = None
   snapshotPowerOffBehavior: _typing.Optional[str] = None
   recordReplayEnabled: _typing.Optional[bool] = None
   faultToleranceType: _typing.Optional[str] = None
   cbrcCacheEnabled: _typing.Optional[bool] = None
   vvtdEnabled: _typing.Optional[bool] = None
   vbsEnabled: _typing.Optional[bool] = None

class FloppyInfo(TargetInfo):
   pass


class ForkConfigInfo(pyVmomi.vmodl.DynamicData):
   class ChildType(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['ChildType'] = 'none'
      persistent: _typing.ClassVar['ChildType'] = 'persistent'
      nonpersistent: _typing.ClassVar['ChildType'] = 'nonpersistent'

   parentEnabled: _typing.Optional[bool] = None
   childForkGroupId: _typing.Optional[str] = None
   parentForkGroupId: _typing.Optional[str] = None
   childType: _typing.Optional[str] = None


class GuestCustomizationManager(pyVmomi.VmomiSupport.ManagedObject):
   def Customize(self, vm: pyVmomi.vim.VirtualMachine, auth: pyVmomi.vim.vm.guest.GuestAuthentication, spec: pyVmomi.vim.vm.customization.Specification, configParams: list[pyVmomi.vim.option.OptionValue]) -> pyVmomi.vim.Task: ...
   def StartNetwork(self, vm: pyVmomi.vim.VirtualMachine, auth: pyVmomi.vim.vm.guest.GuestAuthentication) -> pyVmomi.vim.Task: ...
   def AbortCustomization(self, vm: pyVmomi.vim.VirtualMachine, auth: pyVmomi.vim.vm.guest.GuestAuthentication) -> pyVmomi.vim.Task: ...


class GuestInfo(pyVmomi.vmodl.DynamicData):
   class ToolsStatus(pyVmomi.VmomiSupport.Enum):
      toolsNotInstalled: _typing.ClassVar['ToolsStatus'] = 'toolsNotInstalled'
      toolsNotRunning: _typing.ClassVar['ToolsStatus'] = 'toolsNotRunning'
      toolsOld: _typing.ClassVar['ToolsStatus'] = 'toolsOld'
      toolsOk: _typing.ClassVar['ToolsStatus'] = 'toolsOk'

   class ToolsVersionStatus(pyVmomi.VmomiSupport.Enum):
      guestToolsNotInstalled: _typing.ClassVar['ToolsVersionStatus'] = 'guestToolsNotInstalled'
      guestToolsNeedUpgrade: _typing.ClassVar['ToolsVersionStatus'] = 'guestToolsNeedUpgrade'
      guestToolsCurrent: _typing.ClassVar['ToolsVersionStatus'] = 'guestToolsCurrent'
      guestToolsUnmanaged: _typing.ClassVar['ToolsVersionStatus'] = 'guestToolsUnmanaged'
      guestToolsTooOld: _typing.ClassVar['ToolsVersionStatus'] = 'guestToolsTooOld'
      guestToolsSupportedOld: _typing.ClassVar['ToolsVersionStatus'] = 'guestToolsSupportedOld'
      guestToolsSupportedNew: _typing.ClassVar['ToolsVersionStatus'] = 'guestToolsSupportedNew'
      guestToolsTooNew: _typing.ClassVar['ToolsVersionStatus'] = 'guestToolsTooNew'
      guestToolsBlacklisted: _typing.ClassVar['ToolsVersionStatus'] = 'guestToolsBlacklisted'

   class ToolsRunningStatus(pyVmomi.VmomiSupport.Enum):
      guestToolsNotRunning: _typing.ClassVar['ToolsRunningStatus'] = 'guestToolsNotRunning'
      guestToolsRunning: _typing.ClassVar['ToolsRunningStatus'] = 'guestToolsRunning'
      guestToolsExecutingScripts: _typing.ClassVar['ToolsRunningStatus'] = 'guestToolsExecutingScripts'

   class ToolsInstallType(pyVmomi.VmomiSupport.Enum):
      guestToolsTypeUnknown: _typing.ClassVar['ToolsInstallType'] = 'guestToolsTypeUnknown'
      guestToolsTypeMSI: _typing.ClassVar['ToolsInstallType'] = 'guestToolsTypeMSI'
      guestToolsTypeTar: _typing.ClassVar['ToolsInstallType'] = 'guestToolsTypeTar'
      guestToolsTypeOSP: _typing.ClassVar['ToolsInstallType'] = 'guestToolsTypeOSP'
      guestToolsTypeOpenVMTools: _typing.ClassVar['ToolsInstallType'] = 'guestToolsTypeOpenVMTools'

   class GuestRebootStatus(pyVmomi.vmodl.DynamicData):
      rebootRequested: bool
      requestingComponents: list[str] = []
      requestTimestamp: _typing.Optional[_datetime.datetime] = None

   class VirtualDiskMapping(pyVmomi.vmodl.DynamicData):
      key: int

   class DiskInfo(pyVmomi.vmodl.DynamicData):
      diskPath: _typing.Optional[str] = None
      capacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      freeSpace: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      filesystemType: _typing.Optional[str] = None
      mappings: list[VirtualDiskMapping] = []

   class NicInfo(pyVmomi.vmodl.DynamicData):
      network: _typing.Optional[str] = None
      ipAddress: list[str] = []
      macAddress: _typing.Optional[str] = None
      connected: bool
      deviceConfigId: int
      dnsConfig: _typing.Optional[pyVmomi.vim.net.DnsConfigInfo] = None
      ipConfig: _typing.Optional[pyVmomi.vim.net.IpConfigInfo] = None
      netBIOSConfig: _typing.Optional[pyVmomi.vim.net.NetBIOSConfigInfo] = None

   class StackInfo(pyVmomi.vmodl.DynamicData):
      dnsConfig: _typing.Optional[pyVmomi.vim.net.DnsConfigInfo] = None
      ipRouteConfig: _typing.Optional[pyVmomi.vim.net.IpRouteConfigInfo] = None
      ipStackConfig: list[pyVmomi.vim.KeyValue] = []
      dhcpConfig: _typing.Optional[pyVmomi.vim.net.DhcpConfigInfo] = None

   class ScreenInfo(pyVmomi.vmodl.DynamicData):
      width: int
      height: int

   class GuestState(pyVmomi.VmomiSupport.Enum):
      running: _typing.ClassVar['GuestState'] = 'running'
      shuttingDown: _typing.ClassVar['GuestState'] = 'shuttingDown'
      resetting: _typing.ClassVar['GuestState'] = 'resetting'
      standby: _typing.ClassVar['GuestState'] = 'standby'
      notRunning: _typing.ClassVar['GuestState'] = 'notRunning'
      unknown: _typing.ClassVar['GuestState'] = 'unknown'

   class AppStateType(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['AppStateType'] = 'none'
      appStateOk: _typing.ClassVar['AppStateType'] = 'appStateOk'
      appStateNeedReset: _typing.ClassVar['AppStateType'] = 'appStateNeedReset'

   class NamespaceGenerationInfo(pyVmomi.vmodl.DynamicData):
      key: str
      generationNo: int

   class CustomizationStatus(pyVmomi.VmomiSupport.Enum):
      TOOLSDEPLOYPKG_IDLE: _typing.ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_IDLE'
      TOOLSDEPLOYPKG_PENDING: _typing.ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_PENDING'
      TOOLSDEPLOYPKG_RUNNING: _typing.ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_RUNNING'
      TOOLSDEPLOYPKG_SUCCEEDED: _typing.ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_SUCCEEDED'
      TOOLSDEPLOYPKG_FAILED: _typing.ClassVar['CustomizationStatus'] = 'TOOLSDEPLOYPKG_FAILED'

   class CustomizationInfo(pyVmomi.vmodl.DynamicData):
      customizationStatus: str
      startTime: _typing.Optional[_datetime.datetime] = None
      endTime: _typing.Optional[_datetime.datetime] = None
      errorMsg: _typing.Optional[str] = None

   toolsStatus: _typing.Optional[ToolsStatus] = None
   toolsVersionStatus: _typing.Optional[str] = None
   toolsVersionStatus2: _typing.Optional[str] = None
   toolsRunningStatus: _typing.Optional[str] = None
   toolsVersion: _typing.Optional[str] = None
   toolsInstallType: _typing.Optional[str] = None
   guestId: _typing.Optional[str] = None
   guestFamily: _typing.Optional[str] = None
   guestFullName: _typing.Optional[str] = None
   guestRebootStatus: _typing.Optional[GuestRebootStatus] = None
   guestDetailedData: _typing.Optional[str] = None
   hostName: _typing.Optional[str] = None
   ipAddress: _typing.Optional[str] = None
   net: list[NicInfo] = []
   ipStack: list[StackInfo] = []
   disk: list[DiskInfo] = []
   screen: _typing.Optional[ScreenInfo] = None
   guestState: str
   appHeartbeatStatus: _typing.Optional[str] = None
   guestKernelCrashed: _typing.Optional[bool] = None
   appState: _typing.Optional[str] = None
   guestOperationsReady: _typing.Optional[bool] = None
   interactiveGuestOperationsReady: _typing.Optional[bool] = None
   guestStateChangeSupported: _typing.Optional[bool] = None
   generationInfo: list[NamespaceGenerationInfo] = []
   hwVersion: _typing.Optional[str] = None
   customizationInfo: _typing.Optional[CustomizationInfo] = None


class GuestIntegrityInfo(pyVmomi.vmodl.DynamicData):
   enabled: _typing.Optional[bool] = None


class GuestMonitoringModeInfo(pyVmomi.vmodl.DynamicData):
   gmmFile: _typing.Optional[str] = None
   gmmAppliance: _typing.Optional[str] = None


class GuestOsDescriptor(pyVmomi.vmodl.DynamicData):
   class GuestOsFamily(pyVmomi.VmomiSupport.Enum):
      windowsGuest: _typing.ClassVar['GuestOsFamily'] = 'windowsGuest'
      linuxGuest: _typing.ClassVar['GuestOsFamily'] = 'linuxGuest'
      netwareGuest: _typing.ClassVar['GuestOsFamily'] = 'netwareGuest'
      solarisGuest: _typing.ClassVar['GuestOsFamily'] = 'solarisGuest'
      darwinGuestFamily: _typing.ClassVar['GuestOsFamily'] = 'darwinGuestFamily'
      otherGuestFamily: _typing.ClassVar['GuestOsFamily'] = 'otherGuestFamily'

   class GuestArchitecture(pyVmomi.VmomiSupport.Enum):
      x86: _typing.ClassVar['GuestArchitecture'] = 'x86'
      arm: _typing.ClassVar['GuestArchitecture'] = 'arm'

   class GuestOsIdentifier(pyVmomi.VmomiSupport.Enum):
      dosGuest: _typing.ClassVar['GuestOsIdentifier'] = 'dosGuest'
      win31Guest: _typing.ClassVar['GuestOsIdentifier'] = 'win31Guest'
      win95Guest: _typing.ClassVar['GuestOsIdentifier'] = 'win95Guest'
      win98Guest: _typing.ClassVar['GuestOsIdentifier'] = 'win98Guest'
      winMeGuest: _typing.ClassVar['GuestOsIdentifier'] = 'winMeGuest'
      winNTGuest: _typing.ClassVar['GuestOsIdentifier'] = 'winNTGuest'
      win2000ProGuest: _typing.ClassVar['GuestOsIdentifier'] = 'win2000ProGuest'
      win2000ServGuest: _typing.ClassVar['GuestOsIdentifier'] = 'win2000ServGuest'
      win2000AdvServGuest: _typing.ClassVar['GuestOsIdentifier'] = 'win2000AdvServGuest'
      winXPHomeGuest: _typing.ClassVar['GuestOsIdentifier'] = 'winXPHomeGuest'
      winXPProGuest: _typing.ClassVar['GuestOsIdentifier'] = 'winXPProGuest'
      winXPPro64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'winXPPro64Guest'
      winNetWebGuest: _typing.ClassVar['GuestOsIdentifier'] = 'winNetWebGuest'
      winNetStandardGuest: _typing.ClassVar['GuestOsIdentifier'] = 'winNetStandardGuest'
      winNetEnterpriseGuest: _typing.ClassVar['GuestOsIdentifier'] = 'winNetEnterpriseGuest'
      winNetDatacenterGuest: _typing.ClassVar['GuestOsIdentifier'] = 'winNetDatacenterGuest'
      winNetBusinessGuest: _typing.ClassVar['GuestOsIdentifier'] = 'winNetBusinessGuest'
      winNetStandard64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'winNetStandard64Guest'
      winNetEnterprise64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'winNetEnterprise64Guest'
      winLonghornGuest: _typing.ClassVar['GuestOsIdentifier'] = 'winLonghornGuest'
      winLonghorn64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'winLonghorn64Guest'
      winNetDatacenter64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'winNetDatacenter64Guest'
      winVistaGuest: _typing.ClassVar['GuestOsIdentifier'] = 'winVistaGuest'
      winVista64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'winVista64Guest'
      windows7Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows7Guest'
      windows7_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows7_64Guest'
      windows7Server64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows7Server64Guest'
      windows8Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows8Guest'
      windows8_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows8_64Guest'
      windows8Server64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows8Server64Guest'
      windows9Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows9Guest'
      windows9_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows9_64Guest'
      windows9Server64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows9Server64Guest'
      windows11_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows11_64Guest'
      windows12_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows12_64Guest'
      windowsHyperVGuest: _typing.ClassVar['GuestOsIdentifier'] = 'windowsHyperVGuest'
      windows2019srv_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows2019srv_64Guest'
      windows2019srvNext_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows2019srvNext_64Guest'
      windows2022srvNext_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'windows2022srvNext_64Guest'
      freebsdGuest: _typing.ClassVar['GuestOsIdentifier'] = 'freebsdGuest'
      freebsd64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'freebsd64Guest'
      freebsd11Guest: _typing.ClassVar['GuestOsIdentifier'] = 'freebsd11Guest'
      freebsd11_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'freebsd11_64Guest'
      freebsd12Guest: _typing.ClassVar['GuestOsIdentifier'] = 'freebsd12Guest'
      freebsd12_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'freebsd12_64Guest'
      freebsd13Guest: _typing.ClassVar['GuestOsIdentifier'] = 'freebsd13Guest'
      freebsd13_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'freebsd13_64Guest'
      freebsd14Guest: _typing.ClassVar['GuestOsIdentifier'] = 'freebsd14Guest'
      freebsd14_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'freebsd14_64Guest'
      freebsd15Guest: _typing.ClassVar['GuestOsIdentifier'] = 'freebsd15Guest'
      freebsd15_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'freebsd15_64Guest'
      redhatGuest: _typing.ClassVar['GuestOsIdentifier'] = 'redhatGuest'
      rhel2Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel2Guest'
      rhel3Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel3Guest'
      rhel3_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel3_64Guest'
      rhel4Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel4Guest'
      rhel4_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel4_64Guest'
      rhel5Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel5Guest'
      rhel5_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel5_64Guest'
      rhel6Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel6Guest'
      rhel6_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel6_64Guest'
      rhel7Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel7Guest'
      rhel7_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel7_64Guest'
      rhel8_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel8_64Guest'
      rhel9_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel9_64Guest'
      rhel10_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rhel10_64Guest'
      centosGuest: _typing.ClassVar['GuestOsIdentifier'] = 'centosGuest'
      centos64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'centos64Guest'
      centos6Guest: _typing.ClassVar['GuestOsIdentifier'] = 'centos6Guest'
      centos6_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'centos6_64Guest'
      centos7Guest: _typing.ClassVar['GuestOsIdentifier'] = 'centos7Guest'
      centos7_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'centos7_64Guest'
      centos8_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'centos8_64Guest'
      centos9_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'centos9_64Guest'
      oracleLinuxGuest: _typing.ClassVar['GuestOsIdentifier'] = 'oracleLinuxGuest'
      oracleLinux64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'oracleLinux64Guest'
      oracleLinux6Guest: _typing.ClassVar['GuestOsIdentifier'] = 'oracleLinux6Guest'
      oracleLinux6_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'oracleLinux6_64Guest'
      oracleLinux7Guest: _typing.ClassVar['GuestOsIdentifier'] = 'oracleLinux7Guest'
      oracleLinux7_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'oracleLinux7_64Guest'
      oracleLinux8_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'oracleLinux8_64Guest'
      oracleLinux9_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'oracleLinux9_64Guest'
      oracleLinux10_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'oracleLinux10_64Guest'
      suseGuest: _typing.ClassVar['GuestOsIdentifier'] = 'suseGuest'
      suse64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'suse64Guest'
      slesGuest: _typing.ClassVar['GuestOsIdentifier'] = 'slesGuest'
      sles64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'sles64Guest'
      sles10Guest: _typing.ClassVar['GuestOsIdentifier'] = 'sles10Guest'
      sles10_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'sles10_64Guest'
      sles11Guest: _typing.ClassVar['GuestOsIdentifier'] = 'sles11Guest'
      sles11_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'sles11_64Guest'
      sles12Guest: _typing.ClassVar['GuestOsIdentifier'] = 'sles12Guest'
      sles12_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'sles12_64Guest'
      sles15_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'sles15_64Guest'
      sles16_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'sles16_64Guest'
      nld9Guest: _typing.ClassVar['GuestOsIdentifier'] = 'nld9Guest'
      oesGuest: _typing.ClassVar['GuestOsIdentifier'] = 'oesGuest'
      sjdsGuest: _typing.ClassVar['GuestOsIdentifier'] = 'sjdsGuest'
      mandrakeGuest: _typing.ClassVar['GuestOsIdentifier'] = 'mandrakeGuest'
      mandrivaGuest: _typing.ClassVar['GuestOsIdentifier'] = 'mandrivaGuest'
      mandriva64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'mandriva64Guest'
      turboLinuxGuest: _typing.ClassVar['GuestOsIdentifier'] = 'turboLinuxGuest'
      turboLinux64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'turboLinux64Guest'
      ubuntuGuest: _typing.ClassVar['GuestOsIdentifier'] = 'ubuntuGuest'
      ubuntu64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'ubuntu64Guest'
      debian4Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian4Guest'
      debian4_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian4_64Guest'
      debian5Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian5Guest'
      debian5_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian5_64Guest'
      debian6Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian6Guest'
      debian6_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian6_64Guest'
      debian7Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian7Guest'
      debian7_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian7_64Guest'
      debian8Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian8Guest'
      debian8_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian8_64Guest'
      debian9Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian9Guest'
      debian9_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian9_64Guest'
      debian10Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian10Guest'
      debian10_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian10_64Guest'
      debian11Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian11Guest'
      debian11_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian11_64Guest'
      debian12Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian12Guest'
      debian12_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian12_64Guest'
      debian13Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian13Guest'
      debian13_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'debian13_64Guest'
      asianux3Guest: _typing.ClassVar['GuestOsIdentifier'] = 'asianux3Guest'
      asianux3_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'asianux3_64Guest'
      asianux4Guest: _typing.ClassVar['GuestOsIdentifier'] = 'asianux4Guest'
      asianux4_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'asianux4_64Guest'
      asianux5_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'asianux5_64Guest'
      asianux7_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'asianux7_64Guest'
      asianux8_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'asianux8_64Guest'
      asianux9_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'asianux9_64Guest'
      miraclelinux_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'miraclelinux_64Guest'
      pardus_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'pardus_64Guest'
      opensuseGuest: _typing.ClassVar['GuestOsIdentifier'] = 'opensuseGuest'
      opensuse64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'opensuse64Guest'
      fedoraGuest: _typing.ClassVar['GuestOsIdentifier'] = 'fedoraGuest'
      fedora64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'fedora64Guest'
      coreos64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'coreos64Guest'
      vmwarePhoton64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'vmwarePhoton64Guest'
      other24xLinuxGuest: _typing.ClassVar['GuestOsIdentifier'] = 'other24xLinuxGuest'
      other26xLinuxGuest: _typing.ClassVar['GuestOsIdentifier'] = 'other26xLinuxGuest'
      otherLinuxGuest: _typing.ClassVar['GuestOsIdentifier'] = 'otherLinuxGuest'
      other3xLinuxGuest: _typing.ClassVar['GuestOsIdentifier'] = 'other3xLinuxGuest'
      other4xLinuxGuest: _typing.ClassVar['GuestOsIdentifier'] = 'other4xLinuxGuest'
      other5xLinuxGuest: _typing.ClassVar['GuestOsIdentifier'] = 'other5xLinuxGuest'
      other6xLinuxGuest: _typing.ClassVar['GuestOsIdentifier'] = 'other6xLinuxGuest'
      other7xLinuxGuest: _typing.ClassVar['GuestOsIdentifier'] = 'other7xLinuxGuest'
      genericLinuxGuest: _typing.ClassVar['GuestOsIdentifier'] = 'genericLinuxGuest'
      other24xLinux64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'other24xLinux64Guest'
      other26xLinux64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'other26xLinux64Guest'
      other3xLinux64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'other3xLinux64Guest'
      other4xLinux64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'other4xLinux64Guest'
      other5xLinux64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'other5xLinux64Guest'
      other6xLinux64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'other6xLinux64Guest'
      other7xLinux64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'other7xLinux64Guest'
      otherLinux64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'otherLinux64Guest'
      solaris6Guest: _typing.ClassVar['GuestOsIdentifier'] = 'solaris6Guest'
      solaris7Guest: _typing.ClassVar['GuestOsIdentifier'] = 'solaris7Guest'
      solaris8Guest: _typing.ClassVar['GuestOsIdentifier'] = 'solaris8Guest'
      solaris9Guest: _typing.ClassVar['GuestOsIdentifier'] = 'solaris9Guest'
      solaris10Guest: _typing.ClassVar['GuestOsIdentifier'] = 'solaris10Guest'
      solaris10_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'solaris10_64Guest'
      solaris11_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'solaris11_64Guest'
      fusionos_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'fusionos_64Guest'
      prolinux_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'prolinux_64Guest'
      kylinlinux_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'kylinlinux_64Guest'
      flatcar_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'flatcar_64Guest'
      os2Guest: _typing.ClassVar['GuestOsIdentifier'] = 'os2Guest'
      eComStationGuest: _typing.ClassVar['GuestOsIdentifier'] = 'eComStationGuest'
      eComStation2Guest: _typing.ClassVar['GuestOsIdentifier'] = 'eComStation2Guest'
      netware4Guest: _typing.ClassVar['GuestOsIdentifier'] = 'netware4Guest'
      netware5Guest: _typing.ClassVar['GuestOsIdentifier'] = 'netware5Guest'
      netware6Guest: _typing.ClassVar['GuestOsIdentifier'] = 'netware6Guest'
      openServer5Guest: _typing.ClassVar['GuestOsIdentifier'] = 'openServer5Guest'
      openServer6Guest: _typing.ClassVar['GuestOsIdentifier'] = 'openServer6Guest'
      unixWare7Guest: _typing.ClassVar['GuestOsIdentifier'] = 'unixWare7Guest'
      darwinGuest: _typing.ClassVar['GuestOsIdentifier'] = 'darwinGuest'
      darwin64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin64Guest'
      darwin10Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin10Guest'
      darwin10_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin10_64Guest'
      darwin11Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin11Guest'
      darwin11_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin11_64Guest'
      darwin12_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin12_64Guest'
      darwin13_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin13_64Guest'
      darwin14_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin14_64Guest'
      darwin15_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin15_64Guest'
      darwin16_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin16_64Guest'
      darwin17_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin17_64Guest'
      darwin18_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin18_64Guest'
      darwin19_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin19_64Guest'
      darwin20_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin20_64Guest'
      darwin21_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin21_64Guest'
      darwin22_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin22_64Guest'
      darwin23_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'darwin23_64Guest'
      vmkernelGuest: _typing.ClassVar['GuestOsIdentifier'] = 'vmkernelGuest'
      vmkernel5Guest: _typing.ClassVar['GuestOsIdentifier'] = 'vmkernel5Guest'
      vmkernel6Guest: _typing.ClassVar['GuestOsIdentifier'] = 'vmkernel6Guest'
      vmkernel65Guest: _typing.ClassVar['GuestOsIdentifier'] = 'vmkernel65Guest'
      vmkernel7Guest: _typing.ClassVar['GuestOsIdentifier'] = 'vmkernel7Guest'
      vmkernel8Guest: _typing.ClassVar['GuestOsIdentifier'] = 'vmkernel8Guest'
      vmkernel9Guest: _typing.ClassVar['GuestOsIdentifier'] = 'vmkernel9Guest'
      amazonlinux2_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'amazonlinux2_64Guest'
      amazonlinux3_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'amazonlinux3_64Guest'
      crxPod1Guest: _typing.ClassVar['GuestOsIdentifier'] = 'crxPod1Guest'
      crxSys1Guest: _typing.ClassVar['GuestOsIdentifier'] = 'crxSys1Guest'
      rockylinux_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'rockylinux_64Guest'
      almalinux_64Guest: _typing.ClassVar['GuestOsIdentifier'] = 'almalinux_64Guest'
      otherGuest: _typing.ClassVar['GuestOsIdentifier'] = 'otherGuest'
      otherGuest64: _typing.ClassVar['GuestOsIdentifier'] = 'otherGuest64'

   class FirmwareType(pyVmomi.VmomiSupport.Enum):
      bios: _typing.ClassVar['FirmwareType'] = 'bios'
      efi: _typing.ClassVar['FirmwareType'] = 'efi'
      csm: _typing.ClassVar['FirmwareType'] = 'csm'

   class SupportLevel(pyVmomi.VmomiSupport.Enum):
      experimental: _typing.ClassVar['SupportLevel'] = 'experimental'
      legacy: _typing.ClassVar['SupportLevel'] = 'legacy'
      terminated: _typing.ClassVar['SupportLevel'] = 'terminated'
      supported: _typing.ClassVar['SupportLevel'] = 'supported'
      unsupported: _typing.ClassVar['SupportLevel'] = 'unsupported'
      deprecated: _typing.ClassVar['SupportLevel'] = 'deprecated'
      techPreview: _typing.ClassVar['SupportLevel'] = 'techPreview'

   id: str
   family: str
   fullName: str
   supportedMaxCPUs: int
   numSupportedPhysicalSockets: int
   numSupportedCoresPerSocket: int
   supportedMinMemMB: int
   supportedMaxMemMB: int
   recommendedMemMB: int
   recommendedColorDepth: int
   supportedDiskControllerList: list[type] = []
   recommendedSCSIController: _typing.Optional[type] = None
   recommendedDiskController: type
   supportedNumDisks: int
   recommendedDiskSizeMB: int
   recommendedCdromController: type
   supportedEthernetCard: list[type] = []
   recommendedEthernetCard: _typing.Optional[type] = None
   supportsSlaveDisk: _typing.Optional[bool] = None
   cpuFeatureMask: list[pyVmomi.vim.host.CpuIdInfo] = []
   smcRequired: bool
   supportsWakeOnLan: bool
   supportsVMI: bool
   supportsMemoryHotAdd: bool
   supportsCpuHotAdd: bool
   supportsCpuHotRemove: bool
   supportedFirmware: list[str] = []
   recommendedFirmware: str
   supportedUSBControllerList: list[type] = []
   recommendedUSBController: _typing.Optional[type] = None
   supports3D: bool
   recommended3D: bool
   smcRecommended: bool
   ich7mRecommended: bool
   usbRecommended: bool
   supportLevel: str
   supportedForCreate: bool
   vRAMSizeInKB: pyVmomi.vim.option.IntOption
   numSupportedFloppyDevices: int
   wakeOnLanEthernetCard: list[type] = []
   supportsPvscsiControllerForBoot: bool
   diskUuidEnabled: bool
   supportsHotPlugPCI: bool
   supportsSecureBoot: _typing.Optional[bool] = None
   defaultSecureBoot: _typing.Optional[bool] = None
   persistentMemorySupported: _typing.Optional[bool] = None
   supportedMinPersistentMemoryMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   supportedMaxPersistentMemoryMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   recommendedPersistentMemoryMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   persistentMemoryHotAddSupported: _typing.Optional[bool] = None
   persistentMemoryHotRemoveSupported: _typing.Optional[bool] = None
   persistentMemoryColdGrowthSupported: _typing.Optional[bool] = None
   persistentMemoryColdGrowthGranularityMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   persistentMemoryHotGrowthSupported: _typing.Optional[bool] = None
   persistentMemoryHotGrowthGranularityMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   numRecommendedPhysicalSockets: _typing.Optional[int] = None
   numRecommendedCoresPerSocket: _typing.Optional[int] = None
   vvtdSupported: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   vbsSupported: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   vsgxSupported: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   vsgxRemoteAttestationSupported: _typing.Optional[bool] = None
   supportsTPM20: _typing.Optional[bool] = None
   recommendedTPM20: _typing.Optional[bool] = None
   vwdtSupported: _typing.Optional[bool] = None


class GuestQuiesceSpec(pyVmomi.vmodl.DynamicData):
   timeout: _typing.Optional[int] = None


class IdeDiskDeviceInfo(DiskDeviceInfo):
   class PartitionInfo(pyVmomi.vmodl.DynamicData):
      id: int
      capacity: int

   partitionTable: list[PartitionInfo] = []


class IndependentFilterSpec(BaseIndependentFilterSpec):
   filterName: str
   filterClass: _typing.Optional[str] = None
   filterCapabilities: list[pyVmomi.vim.KeyValue] = []


class InstantCloneSpec(pyVmomi.vmodl.DynamicData):
   name: str
   location: RelocateSpec
   config: list[pyVmomi.vim.option.OptionValue] = []
   biosUuid: _typing.Optional[str] = None


class LegacyNetworkSwitchInfo(pyVmomi.vmodl.DynamicData):
   name: str


class Message(pyVmomi.vmodl.DynamicData):
   id: str
   argument: list[object] = []
   text: _typing.Optional[str] = None


class NetworkInfo(TargetInfo):
   network: pyVmomi.vim.Network.Summary
   vswitch: _typing.Optional[str] = None


class NetworkShaperInfo(pyVmomi.vmodl.DynamicData):
   enabled: _typing.Optional[bool] = None
   peakBps: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   averageBps: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   burstSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class OpaqueNetworkInfo(TargetInfo):
   network: pyVmomi.vim.OpaqueNetwork.Summary
   networkReservationSupported: _typing.Optional[bool] = None

class ParallelInfo(TargetInfo):
   pass


class PciPassthroughInfo(TargetInfo):
   pciDevice: pyVmomi.vim.host.PciDevice
   systemId: str

class PciSharedGpuPassthroughInfo(TargetInfo):
   vgpu: str


class PrecisionClockInfo(TargetInfo):
   systemClockProtocol: _typing.Optional[str] = None


class ProfileDetails(pyVmomi.vmodl.DynamicData):
   class DiskProfileDetails(pyVmomi.vmodl.DynamicData):
      diskId: int
      profile: list[ProfileSpec] = []

   profile: list[ProfileSpec] = []
   diskProfileDetails: list[DiskProfileDetails] = []


class ProfileRawData(pyVmomi.vmodl.DynamicData):
   extensionKey: str
   objectData: _typing.Optional[str] = None


class ProfileSpec(pyVmomi.vmodl.DynamicData):
   pass


class PropertyRelation(pyVmomi.vmodl.DynamicData):
   key: pyVmomi.vmodl.DynamicProperty
   relations: list[pyVmomi.vmodl.DynamicProperty] = []


class QuestionInfo(pyVmomi.vmodl.DynamicData):
   id: str
   text: str
   choice: pyVmomi.vim.option.ChoiceOption
   message: list[Message] = []


class RelocateSpec(pyVmomi.vmodl.DynamicData):
   class Transformation(pyVmomi.VmomiSupport.Enum):
      flat: _typing.ClassVar['Transformation'] = 'flat'
      sparse: _typing.ClassVar['Transformation'] = 'sparse'

   class DiskLocator(pyVmomi.vmodl.DynamicData):
      class BackingSpec(pyVmomi.vmodl.DynamicData):
         parent: _typing.Optional[BackingSpec] = None
         crypto: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None

      diskId: int
      datastore: pyVmomi.vim.Datastore
      diskMoveType: _typing.Optional[str] = None
      diskBackingInfo: _typing.Optional[pyVmomi.vim.vm.device.VirtualDevice.BackingInfo] = None
      profile: list[ProfileSpec] = []
      backing: _typing.Optional[BackingSpec] = None
      filterSpec: list[BaseIndependentFilterSpec] = []

   class DiskMoveOptions(pyVmomi.VmomiSupport.Enum):
      moveAllDiskBackingsAndAllowSharing: _typing.ClassVar['DiskMoveOptions'] = 'moveAllDiskBackingsAndAllowSharing'
      moveAllDiskBackingsAndDisallowSharing: _typing.ClassVar['DiskMoveOptions'] = 'moveAllDiskBackingsAndDisallowSharing'
      moveChildMostDiskBacking: _typing.ClassVar['DiskMoveOptions'] = 'moveChildMostDiskBacking'
      createNewChildDiskBacking: _typing.ClassVar['DiskMoveOptions'] = 'createNewChildDiskBacking'
      moveAllDiskBackingsAndConsolidate: _typing.ClassVar['DiskMoveOptions'] = 'moveAllDiskBackingsAndConsolidate'

   service: _typing.Optional[pyVmomi.vim.ServiceLocator] = None
   folder: _typing.Optional[pyVmomi.vim.Folder] = None
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None
   diskMoveType: _typing.Optional[str] = None
   pool: _typing.Optional[pyVmomi.vim.ResourcePool] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   disk: list[DiskLocator] = []
   transform: _typing.Optional[Transformation] = None
   deviceChange: list[pyVmomi.vim.vm.device.VirtualDeviceSpec] = []
   profile: list[ProfileSpec] = []
   cryptoSpec: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None
   tagSpecs: list[pyVmomi.vim.TagSpec] = []
   vmPlacementPolicies: list[VmPlacementPolicy] = []


class ReplicationConfigSpec(pyVmomi.vmodl.DynamicData):
   class DiskSettings(pyVmomi.vmodl.DynamicData):
      key: int
      diskReplicationId: str

   generation: pyVmomi.VmomiSupport.long
   vmReplicationId: str
   destination: str
   port: int
   rpo: pyVmomi.VmomiSupport.long
   quiesceGuestEnabled: bool
   paused: bool
   oppUpdatesEnabled: bool
   netCompressionEnabled: _typing.Optional[bool] = None
   netEncryptionEnabled: _typing.Optional[bool] = None
   encryptionDestination: _typing.Optional[str] = None
   additionalEncryptionDestination: list[str] = []
   encryptionPort: _typing.Optional[int] = None
   remoteCertificateThumbprint: _typing.Optional[str] = None
   dataSetsReplicationEnabled: _typing.Optional[bool] = None
   useHbrProxyHttpPreamble: _typing.Optional[bool] = None
   disk: list[DiskSettings] = []


class RuntimeInfo(pyVmomi.vmodl.DynamicData):
   class DasProtectionState(pyVmomi.vmodl.DynamicData):
      dasProtected: bool

   device: list[DeviceRuntimeInfo] = []
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   connectionState: pyVmomi.vim.VirtualMachine.ConnectionState
   powerState: pyVmomi.vim.VirtualMachine.PowerState
   vmFailoverInProgress: _typing.Optional[bool] = None
   faultToleranceState: pyVmomi.vim.VirtualMachine.FaultToleranceState
   dasVmProtection: _typing.Optional[DasProtectionState] = None
   toolsInstallerMounted: bool
   suspendTime: _typing.Optional[_datetime.datetime] = None
   bootTime: _typing.Optional[_datetime.datetime] = None
   suspendInterval: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   question: _typing.Optional[QuestionInfo] = None
   memoryOverhead: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maxCpuUsage: _typing.Optional[int] = None
   maxMemoryUsage: _typing.Optional[int] = None
   numMksConnections: int
   recordReplayState: pyVmomi.vim.VirtualMachine.RecordReplayState
   cleanPowerOff: _typing.Optional[bool] = None
   needSecondaryReason: _typing.Optional[str] = None
   onlineStandby: bool
   minRequiredEVCModeKey: _typing.Optional[str] = None
   consolidationNeeded: bool
   offlineFeatureRequirement: list[FeatureRequirement] = []
   featureRequirement: list[FeatureRequirement] = []
   featureMask: list[pyVmomi.vim.host.FeatureMask] = []
   vFlashCacheAllocation: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   paused: _typing.Optional[bool] = None
   snapshotInBackground: _typing.Optional[bool] = None
   quiescedForkParent: _typing.Optional[bool] = None
   instantCloneFrozen: _typing.Optional[bool] = None
   cryptoState: _typing.Optional[str] = None
   suspendedToMemory: _typing.Optional[bool] = None
   opNotificationTimeout: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   iommuActive: _typing.Optional[bool] = None
   consolidateWorkTotal: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   consolidateWorkDone: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   diskChainBroken: _typing.Optional[bool] = None


class ScheduledHardwareUpgradeInfo(pyVmomi.vmodl.DynamicData):
   class HardwareUpgradePolicy(pyVmomi.VmomiSupport.Enum):
      never: _typing.ClassVar['HardwareUpgradePolicy'] = 'never'
      onSoftPowerOff: _typing.ClassVar['HardwareUpgradePolicy'] = 'onSoftPowerOff'
      always: _typing.ClassVar['HardwareUpgradePolicy'] = 'always'

   class HardwareUpgradeStatus(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['HardwareUpgradeStatus'] = 'none'
      pending: _typing.ClassVar['HardwareUpgradeStatus'] = 'pending'
      success: _typing.ClassVar['HardwareUpgradeStatus'] = 'success'
      failed: _typing.ClassVar['HardwareUpgradeStatus'] = 'failed'

   upgradePolicy: _typing.Optional[str] = None
   versionKey: _typing.Optional[str] = None
   scheduledHardwareUpgradeStatus: _typing.Optional[str] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class ScsiDiskDeviceInfo(DiskDeviceInfo):
   disk: _typing.Optional[pyVmomi.vim.host.ScsiDisk] = None
   transportHint: _typing.Optional[str] = None
   lunNumber: _typing.Optional[int] = None


class ScsiPassthroughInfo(TargetInfo):
   class ScsiClass(pyVmomi.VmomiSupport.Enum):
      disk: _typing.ClassVar['ScsiClass'] = 'disk'
      tape: _typing.ClassVar['ScsiClass'] = 'tape'
      printer: _typing.ClassVar['ScsiClass'] = 'printer'
      processor: _typing.ClassVar['ScsiClass'] = 'processor'
      worm: _typing.ClassVar['ScsiClass'] = 'worm'
      cdrom: _typing.ClassVar['ScsiClass'] = 'cdrom'
      scanner: _typing.ClassVar['ScsiClass'] = 'scanner'
      optical: _typing.ClassVar['ScsiClass'] = 'optical'
      media: _typing.ClassVar['ScsiClass'] = 'media'
      com: _typing.ClassVar['ScsiClass'] = 'com'
      raid: _typing.ClassVar['ScsiClass'] = 'raid'
      unknown: _typing.ClassVar['ScsiClass'] = 'unknown'

   scsiClass: str
   vendor: str
   physicalUnitNumber: int

class SerialInfo(TargetInfo):
   pass


class SgxInfo(pyVmomi.vmodl.DynamicData):
   class FlcModes(pyVmomi.VmomiSupport.Enum):
      locked: _typing.ClassVar['FlcModes'] = 'locked'
      unlocked: _typing.ClassVar['FlcModes'] = 'unlocked'

   epcSize: pyVmomi.VmomiSupport.long
   flcMode: _typing.Optional[str] = None
   lePubKeyHash: _typing.Optional[str] = None
   requireAttestation: _typing.Optional[bool] = None


class SgxTargetInfo(TargetInfo):
   maxEpcSize: pyVmomi.VmomiSupport.long
   flcModes: list[str] = []
   lePubKeyHashes: list[str] = []
   requireAttestationSupported: _typing.Optional[bool] = None


class Snapshot(pyVmomi.vim.ExtensibleManagedObject):
   @property
   def config(self) -> ConfigInfo: ...
   @property
   def childSnapshot(self) -> list[Snapshot]: ...
   @property
   def vm(self) -> pyVmomi.vim.VirtualMachine: ...

   def Revert(self, host: _typing.Optional[pyVmomi.vim.HostSystem], suppressPowerOn: _typing.Optional[bool]) -> pyVmomi.vim.Task: ...
   def Remove(self, removeChildren: bool, consolidate: _typing.Optional[bool]) -> pyVmomi.vim.Task: ...
   def Rename(self, name: _typing.Optional[str], description: _typing.Optional[str]) -> None: ...
   def ExportSnapshot(self) -> pyVmomi.vim.HttpNfcLease: ...


class SnapshotInfo(pyVmomi.vmodl.DynamicData):
   currentSnapshot: _typing.Optional[Snapshot] = None
   rootSnapshotList: list[SnapshotTree] = []


class SnapshotSelectionSpec(pyVmomi.vmodl.DynamicData):
   retentionDays: _typing.Optional[int] = None


class SnapshotTree(pyVmomi.vmodl.DynamicData):
   snapshot: Snapshot
   vm: pyVmomi.vim.VirtualMachine
   name: str
   description: str
   id: int
   createTime: _datetime.datetime
   state: pyVmomi.vim.VirtualMachine.PowerState
   quiesced: bool
   backupManifest: _typing.Optional[str] = None
   childSnapshotList: list[SnapshotTree] = []
   replaySupported: _typing.Optional[bool] = None

class SoundInfo(TargetInfo):
   pass


class SriovDevicePoolInfo(pyVmomi.vmodl.DynamicData):
   key: str


class SriovInfo(PciPassthroughInfo):
   virtualFunction: bool
   pnic: _typing.Optional[str] = None
   devicePool: _typing.Optional[SriovDevicePoolInfo] = None


class SriovNetworkDevicePoolInfo(SriovDevicePoolInfo):
   switchKey: _typing.Optional[str] = None
   switchUuid: _typing.Optional[str] = None


class StorageInfo(pyVmomi.vmodl.DynamicData):
   class UsageOnDatastore(pyVmomi.vmodl.DynamicData):
      datastore: pyVmomi.vim.Datastore
      committed: pyVmomi.VmomiSupport.long
      uncommitted: pyVmomi.VmomiSupport.long
      unshared: pyVmomi.VmomiSupport.long

   perDatastoreUsage: list[UsageOnDatastore] = []
   timestamp: _datetime.datetime


class SubnetInfo(TargetInfo):
   class FolderInfo(pyVmomi.vmodl.DynamicData):
      name: str
      folder: pyVmomi.vim.Folder

   id: str
   subnetFolderInfo: FolderInfo
   vpcFolderInfo: FolderInfo
   projectFolderInfo: _typing.Optional[FolderInfo] = None
   rootFolderInfo: FolderInfo


class Summary(pyVmomi.vmodl.DynamicData):
   class ConfigSummary(pyVmomi.vmodl.DynamicData):
      name: str
      template: bool
      vmPathName: str
      memorySizeMB: _typing.Optional[int] = None
      cpuReservation: _typing.Optional[int] = None
      memoryReservation: _typing.Optional[int] = None
      numCpu: _typing.Optional[int] = None
      numEthernetCards: _typing.Optional[int] = None
      numVirtualDisks: _typing.Optional[int] = None
      uuid: _typing.Optional[str] = None
      instanceUuid: _typing.Optional[str] = None
      guestId: _typing.Optional[str] = None
      guestFullName: _typing.Optional[str] = None
      annotation: _typing.Optional[str] = None
      product: _typing.Optional[pyVmomi.vim.vApp.ProductInfo] = None
      installBootRequired: _typing.Optional[bool] = None
      ftInfo: _typing.Optional[FaultToleranceConfigInfo] = None
      managedBy: _typing.Optional[pyVmomi.vim.ext.ManagedByInfo] = None
      tpmPresent: _typing.Optional[bool] = None
      numVmiopBackings: _typing.Optional[int] = None
      hwVersion: _typing.Optional[str] = None

   class QuickStats(pyVmomi.vmodl.DynamicData):
      class MemoryTierStats(pyVmomi.vmodl.DynamicData):
         memoryTierType: str
         readBandwidth: pyVmomi.VmomiSupport.long

      overallCpuUsage: _typing.Optional[int] = None
      overallCpuDemand: _typing.Optional[int] = None
      overallCpuReadiness: _typing.Optional[int] = None
      guestMemoryUsage: _typing.Optional[int] = None
      hostMemoryUsage: _typing.Optional[int] = None
      guestHeartbeatStatus: pyVmomi.vim.ManagedEntity.Status
      distributedCpuEntitlement: _typing.Optional[int] = None
      distributedMemoryEntitlement: _typing.Optional[int] = None
      staticCpuEntitlement: _typing.Optional[int] = None
      staticMemoryEntitlement: _typing.Optional[int] = None
      grantedMemory: _typing.Optional[int] = None
      privateMemory: _typing.Optional[int] = None
      sharedMemory: _typing.Optional[int] = None
      swappedMemory: _typing.Optional[int] = None
      balloonedMemory: _typing.Optional[int] = None
      consumedOverheadMemory: _typing.Optional[int] = None
      ftLogBandwidth: _typing.Optional[int] = None
      ftSecondaryLatency: _typing.Optional[int] = None
      ftLatencyStatus: _typing.Optional[pyVmomi.vim.ManagedEntity.Status] = None
      compressedMemory: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      uptimeSeconds: _typing.Optional[int] = None
      ssdSwappedMemory: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      activeMemory: _typing.Optional[int] = None
      memoryTierStats: list[MemoryTierStats] = []

   class GuestSummary(pyVmomi.vmodl.DynamicData):
      guestId: _typing.Optional[str] = None
      guestFullName: _typing.Optional[str] = None
      toolsStatus: _typing.Optional[GuestInfo.ToolsStatus] = None
      toolsVersionStatus: _typing.Optional[str] = None
      toolsVersionStatus2: _typing.Optional[str] = None
      toolsRunningStatus: _typing.Optional[str] = None
      hostName: _typing.Optional[str] = None
      ipAddress: _typing.Optional[str] = None
      hwVersion: _typing.Optional[str] = None

   class StorageSummary(pyVmomi.vmodl.DynamicData):
      committed: pyVmomi.VmomiSupport.long
      uncommitted: pyVmomi.VmomiSupport.long
      unshared: pyVmomi.VmomiSupport.long
      timestamp: _datetime.datetime

   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   runtime: RuntimeInfo
   guest: _typing.Optional[GuestSummary] = None
   config: ConfigSummary
   storage: _typing.Optional[StorageSummary] = None
   quickStats: QuickStats
   overallStatus: pyVmomi.vim.ManagedEntity.Status
   customValue: list[pyVmomi.vim.CustomFieldsManager.Value] = []


class TargetInfo(pyVmomi.vmodl.DynamicData):
   class ConfigurationTag(pyVmomi.VmomiSupport.Enum):
      compliant: _typing.ClassVar['ConfigurationTag'] = 'compliant'
      clusterWide: _typing.ClassVar['ConfigurationTag'] = 'clusterWide'

   name: str
   configurationTag: list[str] = []


class ToolsConfigInfo(pyVmomi.vmodl.DynamicData):
   class UpgradePolicy(pyVmomi.VmomiSupport.Enum):
      manual: _typing.ClassVar['UpgradePolicy'] = 'manual'
      upgradeAtPowerCycle: _typing.ClassVar['UpgradePolicy'] = 'upgradeAtPowerCycle'

   class ToolsLastInstallInfo(pyVmomi.vmodl.DynamicData):
      counter: int
      fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

   toolsVersion: _typing.Optional[int] = None
   toolsInstallType: _typing.Optional[str] = None
   afterPowerOn: _typing.Optional[bool] = None
   afterResume: _typing.Optional[bool] = None
   beforeGuestStandby: _typing.Optional[bool] = None
   beforeGuestShutdown: _typing.Optional[bool] = None
   beforeGuestReboot: _typing.Optional[bool] = None
   toolsUpgradePolicy: _typing.Optional[str] = None
   pendingCustomization: _typing.Optional[str] = None
   customizationKeyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None
   syncTimeWithHostAllowed: _typing.Optional[bool] = None
   syncTimeWithHost: _typing.Optional[bool] = None
   lastInstallInfo: _typing.Optional[ToolsLastInstallInfo] = None


class UsbInfo(TargetInfo):
   class Speed(pyVmomi.VmomiSupport.Enum):
      low: _typing.ClassVar['Speed'] = 'low'
      full: _typing.ClassVar['Speed'] = 'full'
      high: _typing.ClassVar['Speed'] = 'high'
      superSpeed: _typing.ClassVar['Speed'] = 'superSpeed'
      superSpeedPlus: _typing.ClassVar['Speed'] = 'superSpeedPlus'
      superSpeed20Gbps: _typing.ClassVar['Speed'] = 'superSpeed20Gbps'
      unknownSpeed: _typing.ClassVar['Speed'] = 'unknownSpeed'

   class Family(pyVmomi.VmomiSupport.Enum):
      audio: _typing.ClassVar['Family'] = 'audio'
      hid: _typing.ClassVar['Family'] = 'hid'
      hid_bootable: _typing.ClassVar['Family'] = 'hid_bootable'
      physical: _typing.ClassVar['Family'] = 'physical'
      communication: _typing.ClassVar['Family'] = 'communication'
      imaging: _typing.ClassVar['Family'] = 'imaging'
      printer: _typing.ClassVar['Family'] = 'printer'
      storage: _typing.ClassVar['Family'] = 'storage'
      hub: _typing.ClassVar['Family'] = 'hub'
      smart_card: _typing.ClassVar['Family'] = 'smart_card'
      security: _typing.ClassVar['Family'] = 'security'
      video: _typing.ClassVar['Family'] = 'video'
      wireless: _typing.ClassVar['Family'] = 'wireless'
      bluetooth: _typing.ClassVar['Family'] = 'bluetooth'
      wusb: _typing.ClassVar['Family'] = 'wusb'
      pda: _typing.ClassVar['Family'] = 'pda'
      vendor_specific: _typing.ClassVar['Family'] = 'vendor_specific'
      other: _typing.ClassVar['Family'] = 'other'
      unknownFamily: _typing.ClassVar['Family'] = 'unknownFamily'

   description: str
   vendor: int
   product: int
   physicalPath: str
   family: list[str] = []
   speed: list[str] = []
   summary: _typing.Optional[Summary] = None


class UsbScanCodeSpec(pyVmomi.vmodl.DynamicData):
   class ModifierType(pyVmomi.vmodl.DynamicData):
      leftControl: _typing.Optional[bool] = None
      leftShift: _typing.Optional[bool] = None
      leftAlt: _typing.Optional[bool] = None
      leftGui: _typing.Optional[bool] = None
      rightControl: _typing.Optional[bool] = None
      rightShift: _typing.Optional[bool] = None
      rightAlt: _typing.Optional[bool] = None
      rightGui: _typing.Optional[bool] = None

   class KeyEvent(pyVmomi.vmodl.DynamicData):
      usbHidCode: int
      modifiers: _typing.Optional[ModifierType] = None

   keyEvents: list[KeyEvent] = []


class VFlashModuleInfo(TargetInfo):
   vFlashModule: pyVmomi.vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption


class VMotionStunTimeInfo(TargetInfo):
   migrationBW: pyVmomi.VmomiSupport.long
   stunTime: pyVmomi.VmomiSupport.long


class VcpuConfig(pyVmomi.vmodl.DynamicData):
   latencySensitivity: _typing.Optional[pyVmomi.vim.LatencySensitivity] = None


class VendorDeviceGroupInfo(TargetInfo):
   class ComponentDeviceInfo(pyVmomi.vmodl.DynamicData):
      class ComponentType(pyVmomi.VmomiSupport.Enum):
         pciPassthru: _typing.ClassVar['ComponentType'] = 'pciPassthru'
         nvidiaVgpu: _typing.ClassVar['ComponentType'] = 'nvidiaVgpu'
         sriovNic: _typing.ClassVar['ComponentType'] = 'sriovNic'
         dvx: _typing.ClassVar['ComponentType'] = 'dvx'

      type: str
      vendorName: str
      deviceName: str
      isConfigurable: bool
      device: pyVmomi.vim.vm.device.VirtualDevice

   deviceGroupName: str
   deviceGroupDescription: _typing.Optional[str] = None
   componentDeviceInfo: list[ComponentDeviceInfo] = []


class VgpuDeviceInfo(TargetInfo):
   deviceName: str
   deviceVendorId: pyVmomi.VmomiSupport.long
   maxFbSizeInGib: pyVmomi.VmomiSupport.long
   timeSlicedCapable: bool
   migCapable: bool
   computeProfileCapable: bool
   quadroProfileCapable: bool


class VgpuProfileInfo(TargetInfo):
   class ProfileSharing(pyVmomi.VmomiSupport.Enum):
      timeSliced: _typing.ClassVar['ProfileSharing'] = 'timeSliced'
      mig: _typing.ClassVar['ProfileSharing'] = 'mig'

   class ProfileClass(pyVmomi.VmomiSupport.Enum):
      compute: _typing.ClassVar['ProfileClass'] = 'compute'
      quadro: _typing.ClassVar['ProfileClass'] = 'quadro'

   profileName: str
   deviceVendorId: pyVmomi.VmomiSupport.long
   fbSizeInGib: pyVmomi.VmomiSupport.long
   profileSharing: str
   profileClass: str
   stunTimeEstimates: list[VMotionStunTimeInfo] = []


class VirtualDeviceGroups(pyVmomi.vmodl.DynamicData):
   class DeviceGroup(pyVmomi.vmodl.DynamicData):
      groupInstanceKey: int
      deviceInfo: _typing.Optional[pyVmomi.vim.Description] = None

   class VendorDeviceGroup(DeviceGroup):
      deviceGroupName: str

   deviceGroup: list[DeviceGroup] = []


class VirtualDeviceSwap(pyVmomi.vmodl.DynamicData):
   class DeviceSwapStatus(pyVmomi.VmomiSupport.Enum):
      none: _typing.ClassVar['DeviceSwapStatus'] = 'none'
      scheduled: _typing.ClassVar['DeviceSwapStatus'] = 'scheduled'
      inprogress: _typing.ClassVar['DeviceSwapStatus'] = 'inprogress'
      failed: _typing.ClassVar['DeviceSwapStatus'] = 'failed'
      completed: _typing.ClassVar['DeviceSwapStatus'] = 'completed'

   class DeviceSwapInfo(pyVmomi.vmodl.DynamicData):
      enabled: _typing.Optional[bool] = None
      applicable: _typing.Optional[bool] = None
      status: _typing.Optional[str] = None

   lsiToPvscsi: _typing.Optional[DeviceSwapInfo] = None


class VirtualHardware(pyVmomi.vmodl.DynamicData):
   class MotherboardLayout(pyVmomi.VmomiSupport.Enum):
      i440bxHostBridge: _typing.ClassVar['MotherboardLayout'] = 'i440bxHostBridge'
      acpiHostBridges: _typing.ClassVar['MotherboardLayout'] = 'acpiHostBridges'

   numCPU: int
   numCoresPerSocket: _typing.Optional[int] = None
   autoCoresPerSocket: _typing.Optional[bool] = None
   memoryMB: int
   virtualICH7MPresent: _typing.Optional[bool] = None
   virtualSMCPresent: _typing.Optional[bool] = None
   device: list[pyVmomi.vim.vm.device.VirtualDevice] = []
   motherboardLayout: _typing.Optional[str] = None
   simultaneousThreads: _typing.Optional[int] = None


class VirtualHardwareOption(pyVmomi.vmodl.DynamicData):
   hwVersion: int
   virtualDeviceOption: list[pyVmomi.vim.vm.device.VirtualDeviceOption] = []
   deviceListReadonly: bool
   numCPU: list[int] = []
   numCoresPerSocket: pyVmomi.vim.option.IntOption
   autoCoresPerSocket: _typing.Optional[pyVmomi.vim.option.BoolOption] = None
   numCpuReadonly: bool
   memoryMB: pyVmomi.vim.option.LongOption
   numPCIControllers: pyVmomi.vim.option.IntOption
   numIDEControllers: pyVmomi.vim.option.IntOption
   numUSBControllers: pyVmomi.vim.option.IntOption
   numUSBXHCIControllers: pyVmomi.vim.option.IntOption
   numSIOControllers: pyVmomi.vim.option.IntOption
   numPS2Controllers: pyVmomi.vim.option.IntOption
   licensingLimit: list[pyVmomi.VmomiSupport.PropertyPath] = []
   numSupportedWwnPorts: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numSupportedWwnNodes: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   resourceConfigOption: pyVmomi.vim.ResourceConfigOption
   numNVDIMMControllers: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numTPMDevices: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numWDTDevices: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numPrecisionClockDevices: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   epcMemoryMB: _typing.Optional[pyVmomi.vim.option.LongOption] = None
   acpiHostBridgesFirmware: list[str] = []
   numCpuSimultaneousThreads: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numNumaNodes: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   numDeviceGroups: _typing.Optional[pyVmomi.vim.option.IntOption] = None
   deviceGroupTypes: list[type] = []


class VirtualNuma(pyVmomi.vmodl.DynamicData):
   coresPerNumaNode: _typing.Optional[int] = None
   exposeVnumaOnCpuHotadd: _typing.Optional[bool] = None


class VirtualNumaInfo(pyVmomi.vmodl.DynamicData):
   coresPerNumaNode: _typing.Optional[int] = None
   autoCoresPerNumaNode: _typing.Optional[bool] = None
   vnumaOnCpuHotaddExposed: _typing.Optional[bool] = None


class VirtualPMem(pyVmomi.vmodl.DynamicData):
   class SnapshotMode(pyVmomi.VmomiSupport.Enum):
      independent_persistent: _typing.ClassVar['SnapshotMode'] = 'independent_persistent'
      independent_eraseonrevert: _typing.ClassVar['SnapshotMode'] = 'independent_eraseonrevert'

   snapshotMode: _typing.Optional[str] = None


class VmImportSpec(pyVmomi.vim.ImportSpec):
   configSpec: ConfigSpec
   resPoolEntity: _typing.Optional[pyVmomi.vim.ResourcePool] = None


class VmPlacementPolicy(pyVmomi.vmodl.DynamicData):
   class VmPlacementPolicyStrictness(pyVmomi.VmomiSupport.Enum):
      PreferredDuringPlacementPreferredDuringExecution: _typing.ClassVar['VmPlacementPolicyStrictness'] = 'PreferredDuringPlacementPreferredDuringExecution'
      RequiredDuringPlacementPreferredDuringExecution: _typing.ClassVar['VmPlacementPolicyStrictness'] = 'RequiredDuringPlacementPreferredDuringExecution'

   class VmPlacementPolicyTopology(pyVmomi.VmomiSupport.Enum):
      Host: _typing.ClassVar['VmPlacementPolicyTopology'] = 'Host'
      ClusterComputeResource: _typing.ClassVar['VmPlacementPolicyTopology'] = 'ClusterComputeResource'
      VSphereZone: _typing.ClassVar['VmPlacementPolicyTopology'] = 'VSphereZone'


class VmToVmGroupsAntiAffinity(VmPlacementPolicy):
   selfTag: _typing.Optional[pyVmomi.vim.TagId] = None
   antiAffinedVmGroupTags: list[pyVmomi.vim.TagId] = []
   policyStrictness: _typing.Optional[str] = None
   policyTopology: _typing.Optional[str] = None


class VmVmAffinity(VmPlacementPolicy):
   affinedVmsTag: pyVmomi.vim.TagId
   policyStrictness: _typing.Optional[str] = None
   policyTopology: _typing.Optional[str] = None


class VmVmAntiAffinity(VmPlacementPolicy):
   antiAffinedVmsTag: pyVmomi.vim.TagId
   policyStrictness: _typing.Optional[str] = None
   policyTopology: _typing.Optional[str] = None


class WindowsQuiesceSpec(GuestQuiesceSpec):
   class VssBackupContext(pyVmomi.VmomiSupport.Enum):
      ctx_auto: _typing.ClassVar['VssBackupContext'] = 'ctx_auto'
      ctx_backup: _typing.ClassVar['VssBackupContext'] = 'ctx_backup'
      ctx_file_share_backup: _typing.ClassVar['VssBackupContext'] = 'ctx_file_share_backup'

   vssBackupType: _typing.Optional[int] = None
   vssBootableSystemState: _typing.Optional[bool] = None
   vssPartialFileSupport: _typing.Optional[bool] = None
   vssBackupContext: _typing.Optional[str] = None
