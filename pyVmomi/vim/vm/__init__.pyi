from typing import List, Literal
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType, PropertyPath, binary, long, short
from . import check as check
from . import customization as customization
from . import device as device
from . import guest as guest
from . import replication as replication


class GuestCustomizationManager(ManagedObject):
    def Customize(self, vm: vim.VirtualMachine, auth: vim.vm.guest.GuestAuthentication, spec: vim.vm.customization.Specification, configParams: List[vim.option.OptionValue]) -> vim.Task: ...
    def StartNetwork(self, vm: vim.VirtualMachine, auth: vim.vm.guest.GuestAuthentication) -> vim.Task: ...
    def AbortCustomization(self, vm: vim.VirtualMachine, auth: vim.vm.guest.GuestAuthentication) -> vim.Task: ...


class Snapshot(vim.ExtensibleManagedObject):
    @property
    def config(self) -> ConfigInfo: ...
    @property
    def childSnapshot(self) -> List[Snapshot]: ...
    @property
    def vm(self) -> vim.VirtualMachine: ...
    def Revert(self, host: vim.HostSystem, suppressPowerOn: bool) -> vim.Task: ...
    def Remove(self, removeChildren: bool, consolidate: bool) -> vim.Task: ...
    def Rename(self, name: str, description: str) -> NoneType: ...
    def ExportSnapshot(self) -> vim.HttpNfcLease: ...


class AffinityInfo(vmodl.DynamicData):
    @property
    def affinitySet(self) -> List[int]: ...
    @affinitySet.setter
    def affinitySet(self, value: List[int]):
        self._affinitySet = value


class BaseIndependentFilterSpec(vmodl.DynamicData): ...


class BootOptions(vmodl.DynamicData):
    @property
    def bootDelay(self) -> long: ...
    @bootDelay.setter
    def bootDelay(self, value: long):
        self._bootDelay = value
    @property
    def enterBIOSSetup(self) -> bool: ...
    @enterBIOSSetup.setter
    def enterBIOSSetup(self, value: bool):
        self._enterBIOSSetup = value
    @property
    def efiSecureBootEnabled(self) -> bool: ...
    @efiSecureBootEnabled.setter
    def efiSecureBootEnabled(self, value: bool):
        self._efiSecureBootEnabled = value
    @property
    def bootRetryEnabled(self) -> bool: ...
    @bootRetryEnabled.setter
    def bootRetryEnabled(self, value: bool):
        self._bootRetryEnabled = value
    @property
    def bootRetryDelay(self) -> long: ...
    @bootRetryDelay.setter
    def bootRetryDelay(self, value: long):
        self._bootRetryDelay = value
    @property
    def bootOrder(self) -> List[BootOptions.BootableDevice]: ...
    @bootOrder.setter
    def bootOrder(self, value: List[BootOptions.BootableDevice]):
        self._bootOrder = value
    @property
    def networkBootProtocol(self) -> str: ...
    @networkBootProtocol.setter
    def networkBootProtocol(self, value: str):
        self._networkBootProtocol = value


    class BootableCdromDevice(BootOptions.BootableDevice): ...


    class BootableDevice(vmodl.DynamicData): ...


    class BootableDiskDevice(BootOptions.BootableDevice):
        @property
        def deviceKey(self) -> int: ...
        @deviceKey.setter
        def deviceKey(self, value: int):
            self._deviceKey = value


    class BootableEthernetDevice(BootOptions.BootableDevice):
        @property
        def deviceKey(self) -> int: ...
        @deviceKey.setter
        def deviceKey(self, value: int):
            self._deviceKey = value


    class BootableFloppyDevice(BootOptions.BootableDevice): ...


    class NetworkBootProtocolType(Enum):
        ipv4 = "ipv4"
        ipv6 = "ipv6"


class Capability(vmodl.DynamicData):
    @property
    def snapshotOperationsSupported(self) -> bool: ...
    @snapshotOperationsSupported.setter
    def snapshotOperationsSupported(self, value: bool):
        self._snapshotOperationsSupported = value
    @property
    def multipleSnapshotsSupported(self) -> bool: ...
    @multipleSnapshotsSupported.setter
    def multipleSnapshotsSupported(self, value: bool):
        self._multipleSnapshotsSupported = value
    @property
    def snapshotConfigSupported(self) -> bool: ...
    @snapshotConfigSupported.setter
    def snapshotConfigSupported(self, value: bool):
        self._snapshotConfigSupported = value
    @property
    def poweredOffSnapshotsSupported(self) -> bool: ...
    @poweredOffSnapshotsSupported.setter
    def poweredOffSnapshotsSupported(self, value: bool):
        self._poweredOffSnapshotsSupported = value
    @property
    def memorySnapshotsSupported(self) -> bool: ...
    @memorySnapshotsSupported.setter
    def memorySnapshotsSupported(self, value: bool):
        self._memorySnapshotsSupported = value
    @property
    def revertToSnapshotSupported(self) -> bool: ...
    @revertToSnapshotSupported.setter
    def revertToSnapshotSupported(self, value: bool):
        self._revertToSnapshotSupported = value
    @property
    def quiescedSnapshotsSupported(self) -> bool: ...
    @quiescedSnapshotsSupported.setter
    def quiescedSnapshotsSupported(self, value: bool):
        self._quiescedSnapshotsSupported = value
    @property
    def disableSnapshotsSupported(self) -> bool: ...
    @disableSnapshotsSupported.setter
    def disableSnapshotsSupported(self, value: bool):
        self._disableSnapshotsSupported = value
    @property
    def lockSnapshotsSupported(self) -> bool: ...
    @lockSnapshotsSupported.setter
    def lockSnapshotsSupported(self, value: bool):
        self._lockSnapshotsSupported = value
    @property
    def consolePreferencesSupported(self) -> bool: ...
    @consolePreferencesSupported.setter
    def consolePreferencesSupported(self, value: bool):
        self._consolePreferencesSupported = value
    @property
    def cpuFeatureMaskSupported(self) -> bool: ...
    @cpuFeatureMaskSupported.setter
    def cpuFeatureMaskSupported(self, value: bool):
        self._cpuFeatureMaskSupported = value
    @property
    def s1AcpiManagementSupported(self) -> bool: ...
    @s1AcpiManagementSupported.setter
    def s1AcpiManagementSupported(self, value: bool):
        self._s1AcpiManagementSupported = value
    @property
    def settingScreenResolutionSupported(self) -> bool: ...
    @settingScreenResolutionSupported.setter
    def settingScreenResolutionSupported(self, value: bool):
        self._settingScreenResolutionSupported = value
    @property
    def toolsAutoUpdateSupported(self) -> bool: ...
    @toolsAutoUpdateSupported.setter
    def toolsAutoUpdateSupported(self, value: bool):
        self._toolsAutoUpdateSupported = value
    @property
    def vmNpivWwnSupported(self) -> bool: ...
    @vmNpivWwnSupported.setter
    def vmNpivWwnSupported(self, value: bool):
        self._vmNpivWwnSupported = value
    @property
    def npivWwnOnNonRdmVmSupported(self) -> bool: ...
    @npivWwnOnNonRdmVmSupported.setter
    def npivWwnOnNonRdmVmSupported(self, value: bool):
        self._npivWwnOnNonRdmVmSupported = value
    @property
    def vmNpivWwnDisableSupported(self) -> bool: ...
    @vmNpivWwnDisableSupported.setter
    def vmNpivWwnDisableSupported(self, value: bool):
        self._vmNpivWwnDisableSupported = value
    @property
    def vmNpivWwnUpdateSupported(self) -> bool: ...
    @vmNpivWwnUpdateSupported.setter
    def vmNpivWwnUpdateSupported(self, value: bool):
        self._vmNpivWwnUpdateSupported = value
    @property
    def swapPlacementSupported(self) -> bool: ...
    @swapPlacementSupported.setter
    def swapPlacementSupported(self, value: bool):
        self._swapPlacementSupported = value
    @property
    def toolsSyncTimeSupported(self) -> bool: ...
    @toolsSyncTimeSupported.setter
    def toolsSyncTimeSupported(self, value: bool):
        self._toolsSyncTimeSupported = value
    @property
    def virtualMmuUsageSupported(self) -> bool: ...
    @virtualMmuUsageSupported.setter
    def virtualMmuUsageSupported(self, value: bool):
        self._virtualMmuUsageSupported = value
    @property
    def diskSharesSupported(self) -> bool: ...
    @diskSharesSupported.setter
    def diskSharesSupported(self, value: bool):
        self._diskSharesSupported = value
    @property
    def bootOptionsSupported(self) -> bool: ...
    @bootOptionsSupported.setter
    def bootOptionsSupported(self, value: bool):
        self._bootOptionsSupported = value
    @property
    def bootRetryOptionsSupported(self) -> bool: ...
    @bootRetryOptionsSupported.setter
    def bootRetryOptionsSupported(self, value: bool):
        self._bootRetryOptionsSupported = value
    @property
    def settingVideoRamSizeSupported(self) -> bool: ...
    @settingVideoRamSizeSupported.setter
    def settingVideoRamSizeSupported(self, value: bool):
        self._settingVideoRamSizeSupported = value
    @property
    def settingDisplayTopologySupported(self) -> bool: ...
    @settingDisplayTopologySupported.setter
    def settingDisplayTopologySupported(self, value: bool):
        self._settingDisplayTopologySupported = value
    @property
    def recordReplaySupported(self) -> bool: ...
    @recordReplaySupported.setter
    def recordReplaySupported(self, value: bool):
        self._recordReplaySupported = value
    @property
    def changeTrackingSupported(self) -> bool: ...
    @changeTrackingSupported.setter
    def changeTrackingSupported(self, value: bool):
        self._changeTrackingSupported = value
    @property
    def multipleCoresPerSocketSupported(self) -> bool: ...
    @multipleCoresPerSocketSupported.setter
    def multipleCoresPerSocketSupported(self, value: bool):
        self._multipleCoresPerSocketSupported = value
    @property
    def hostBasedReplicationSupported(self) -> bool: ...
    @hostBasedReplicationSupported.setter
    def hostBasedReplicationSupported(self, value: bool):
        self._hostBasedReplicationSupported = value
    @property
    def guestAutoLockSupported(self) -> bool: ...
    @guestAutoLockSupported.setter
    def guestAutoLockSupported(self, value: bool):
        self._guestAutoLockSupported = value
    @property
    def memoryReservationLockSupported(self) -> bool: ...
    @memoryReservationLockSupported.setter
    def memoryReservationLockSupported(self, value: bool):
        self._memoryReservationLockSupported = value
    @property
    def featureRequirementSupported(self) -> bool: ...
    @featureRequirementSupported.setter
    def featureRequirementSupported(self, value: bool):
        self._featureRequirementSupported = value
    @property
    def poweredOnMonitorTypeChangeSupported(self) -> bool: ...
    @poweredOnMonitorTypeChangeSupported.setter
    def poweredOnMonitorTypeChangeSupported(self, value: bool):
        self._poweredOnMonitorTypeChangeSupported = value
    @property
    def seSparseDiskSupported(self) -> bool: ...
    @seSparseDiskSupported.setter
    def seSparseDiskSupported(self, value: bool):
        self._seSparseDiskSupported = value
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
    def secureBootSupported(self) -> bool: ...
    @secureBootSupported.setter
    def secureBootSupported(self, value: bool):
        self._secureBootSupported = value
    @property
    def perVmEvcSupported(self) -> bool: ...
    @perVmEvcSupported.setter
    def perVmEvcSupported(self, value: bool):
        self._perVmEvcSupported = value
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
    def diskOnlySnapshotOnSuspendedVMSupported(self) -> bool: ...
    @diskOnlySnapshotOnSuspendedVMSupported.setter
    def diskOnlySnapshotOnSuspendedVMSupported(self, value: bool):
        self._diskOnlySnapshotOnSuspendedVMSupported = value
    @property
    def suspendToMemorySupported(self) -> bool: ...
    @suspendToMemorySupported.setter
    def suspendToMemorySupported(self, value: bool):
        self._suspendToMemorySupported = value
    @property
    def toolsSyncTimeAllowSupported(self) -> bool: ...
    @toolsSyncTimeAllowSupported.setter
    def toolsSyncTimeAllowSupported(self, value: bool):
        self._toolsSyncTimeAllowSupported = value
    @property
    def sevSupported(self) -> bool: ...
    @sevSupported.setter
    def sevSupported(self, value: bool):
        self._sevSupported = value
    @property
    def pmemFailoverSupported(self) -> bool: ...
    @pmemFailoverSupported.setter
    def pmemFailoverSupported(self, value: bool):
        self._pmemFailoverSupported = value
    @property
    def requireSgxAttestationSupported(self) -> bool: ...
    @requireSgxAttestationSupported.setter
    def requireSgxAttestationSupported(self, value: bool):
        self._requireSgxAttestationSupported = value
    @property
    def changeModeDisksSupported(self) -> bool: ...
    @changeModeDisksSupported.setter
    def changeModeDisksSupported(self, value: bool):
        self._changeModeDisksSupported = value
    @property
    def vendorDeviceGroupSupported(self) -> bool: ...
    @vendorDeviceGroupSupported.setter
    def vendorDeviceGroupSupported(self, value: bool):
        self._vendorDeviceGroupSupported = value


class CdromInfo(TargetInfo):
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value


class CertThumbprint(vmodl.DynamicData):
    @property
    def thumbprint(self) -> str: ...
    @thumbprint.setter
    def thumbprint(self, value: str):
        self._thumbprint = value
    @property
    def hashAlgorithm(self) -> str: ...
    @hashAlgorithm.setter
    def hashAlgorithm(self, value: str):
        self._hashAlgorithm = value


    class HashAlgorithm(Enum):
        sha256 = "sha256"


class CloneSpec(vmodl.DynamicData):
    @property
    def location(self) -> RelocateSpec: ...
    @location.setter
    def location(self, value: RelocateSpec):
        self._location = value
    @property
    def template(self) -> bool: ...
    @template.setter
    def template(self, value: bool):
        self._template = value
    @property
    def config(self) -> ConfigSpec: ...
    @config.setter
    def config(self, value: ConfigSpec):
        self._config = value
    @property
    def customization(self) -> vim.vm.customization.Specification: ...
    @customization.setter
    def customization(self, value: vim.vm.customization.Specification):
        self._customization = value
    @property
    def powerOn(self) -> bool: ...
    @powerOn.setter
    def powerOn(self, value: bool):
        self._powerOn = value
    @property
    def snapshot(self) -> Snapshot: ...
    @snapshot.setter
    def snapshot(self, value: Snapshot):
        self._snapshot = value
    @property
    def memory(self) -> bool: ...
    @memory.setter
    def memory(self, value: bool):
        self._memory = value
    @property
    def tpmProvisionPolicy(self) -> str: ...
    @tpmProvisionPolicy.setter
    def tpmProvisionPolicy(self, value: str):
        self._tpmProvisionPolicy = value


    class TpmProvisionPolicy(Enum):
        copy = "copy"
        replace = "replace"


class ConfigInfo(vmodl.DynamicData):
    @property
    def changeVersion(self) -> str: ...
    @changeVersion.setter
    def changeVersion(self, value: str):
        self._changeVersion = value
    @property
    def modified(self) -> datetime: ...
    @modified.setter
    def modified(self, value: datetime):
        self._modified = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def guestFullName(self) -> str: ...
    @guestFullName.setter
    def guestFullName(self, value: str):
        self._guestFullName = value
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
    def createDate(self) -> datetime: ...
    @createDate.setter
    def createDate(self, value: datetime):
        self._createDate = value
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value
    @property
    def npivNodeWorldWideName(self) -> List[long]: ...
    @npivNodeWorldWideName.setter
    def npivNodeWorldWideName(self, value: List[long]):
        self._npivNodeWorldWideName = value
    @property
    def npivPortWorldWideName(self) -> List[long]: ...
    @npivPortWorldWideName.setter
    def npivPortWorldWideName(self, value: List[long]):
        self._npivPortWorldWideName = value
    @property
    def npivWorldWideNameType(self) -> str: ...
    @npivWorldWideNameType.setter
    def npivWorldWideNameType(self, value: str):
        self._npivWorldWideNameType = value
    @property
    def npivDesiredNodeWwns(self) -> short: ...
    @npivDesiredNodeWwns.setter
    def npivDesiredNodeWwns(self, value: short):
        self._npivDesiredNodeWwns = value
    @property
    def npivDesiredPortWwns(self) -> short: ...
    @npivDesiredPortWwns.setter
    def npivDesiredPortWwns(self, value: short):
        self._npivDesiredPortWwns = value
    @property
    def npivTemporaryDisabled(self) -> bool: ...
    @npivTemporaryDisabled.setter
    def npivTemporaryDisabled(self, value: bool):
        self._npivTemporaryDisabled = value
    @property
    def npivOnNonRdmDisks(self) -> bool: ...
    @npivOnNonRdmDisks.setter
    def npivOnNonRdmDisks(self, value: bool):
        self._npivOnNonRdmDisks = value
    @property
    def locationId(self) -> str: ...
    @locationId.setter
    def locationId(self, value: str):
        self._locationId = value
    @property
    def template(self) -> bool: ...
    @template.setter
    def template(self, value: bool):
        self._template = value
    @property
    def guestId(self) -> str: ...
    @guestId.setter
    def guestId(self, value: str):
        self._guestId = value
    @property
    def alternateGuestName(self) -> str: ...
    @alternateGuestName.setter
    def alternateGuestName(self, value: str):
        self._alternateGuestName = value
    @property
    def annotation(self) -> str: ...
    @annotation.setter
    def annotation(self, value: str):
        self._annotation = value
    @property
    def files(self) -> FileInfo: ...
    @files.setter
    def files(self, value: FileInfo):
        self._files = value
    @property
    def tools(self) -> ToolsConfigInfo: ...
    @tools.setter
    def tools(self, value: ToolsConfigInfo):
        self._tools = value
    @property
    def flags(self) -> FlagInfo: ...
    @flags.setter
    def flags(self, value: FlagInfo):
        self._flags = value
    @property
    def consolePreferences(self) -> ConsolePreferences: ...
    @consolePreferences.setter
    def consolePreferences(self, value: ConsolePreferences):
        self._consolePreferences = value
    @property
    def defaultPowerOps(self) -> DefaultPowerOpInfo: ...
    @defaultPowerOps.setter
    def defaultPowerOps(self, value: DefaultPowerOpInfo):
        self._defaultPowerOps = value
    @property
    def rebootPowerOff(self) -> bool: ...
    @rebootPowerOff.setter
    def rebootPowerOff(self, value: bool):
        self._rebootPowerOff = value
    @property
    def hardware(self) -> VirtualHardware: ...
    @hardware.setter
    def hardware(self, value: VirtualHardware):
        self._hardware = value
    @property
    def vcpuConfig(self) -> List[VcpuConfig]: ...
    @vcpuConfig.setter
    def vcpuConfig(self, value: List[VcpuConfig]):
        self._vcpuConfig = value
    @property
    def cpuAllocation(self) -> vim.ResourceAllocationInfo: ...
    @cpuAllocation.setter
    def cpuAllocation(self, value: vim.ResourceAllocationInfo):
        self._cpuAllocation = value
    @property
    def memoryAllocation(self) -> vim.ResourceAllocationInfo: ...
    @memoryAllocation.setter
    def memoryAllocation(self, value: vim.ResourceAllocationInfo):
        self._memoryAllocation = value
    @property
    def latencySensitivity(self) -> vim.LatencySensitivity: ...
    @latencySensitivity.setter
    def latencySensitivity(self, value: vim.LatencySensitivity):
        self._latencySensitivity = value
    @property
    def memoryHotAddEnabled(self) -> bool: ...
    @memoryHotAddEnabled.setter
    def memoryHotAddEnabled(self, value: bool):
        self._memoryHotAddEnabled = value
    @property
    def cpuHotAddEnabled(self) -> bool: ...
    @cpuHotAddEnabled.setter
    def cpuHotAddEnabled(self, value: bool):
        self._cpuHotAddEnabled = value
    @property
    def cpuHotRemoveEnabled(self) -> bool: ...
    @cpuHotRemoveEnabled.setter
    def cpuHotRemoveEnabled(self, value: bool):
        self._cpuHotRemoveEnabled = value
    @property
    def hotPlugMemoryLimit(self) -> long: ...
    @hotPlugMemoryLimit.setter
    def hotPlugMemoryLimit(self, value: long):
        self._hotPlugMemoryLimit = value
    @property
    def hotPlugMemoryIncrementSize(self) -> long: ...
    @hotPlugMemoryIncrementSize.setter
    def hotPlugMemoryIncrementSize(self, value: long):
        self._hotPlugMemoryIncrementSize = value
    @property
    def cpuAffinity(self) -> AffinityInfo: ...
    @cpuAffinity.setter
    def cpuAffinity(self, value: AffinityInfo):
        self._cpuAffinity = value
    @property
    def memoryAffinity(self) -> AffinityInfo: ...
    @memoryAffinity.setter
    def memoryAffinity(self, value: AffinityInfo):
        self._memoryAffinity = value
    @property
    def networkShaper(self) -> NetworkShaperInfo: ...
    @networkShaper.setter
    def networkShaper(self, value: NetworkShaperInfo):
        self._networkShaper = value
    @property
    def extraConfig(self) -> List[vim.option.OptionValue]: ...
    @extraConfig.setter
    def extraConfig(self, value: List[vim.option.OptionValue]):
        self._extraConfig = value
    @property
    def cpuFeatureMask(self) -> List[vim.host.CpuIdInfo]: ...
    @cpuFeatureMask.setter
    def cpuFeatureMask(self, value: List[vim.host.CpuIdInfo]):
        self._cpuFeatureMask = value
    @property
    def datastoreUrl(self) -> List[ConfigInfo.DatastoreUrlPair]: ...
    @datastoreUrl.setter
    def datastoreUrl(self, value: List[ConfigInfo.DatastoreUrlPair]):
        self._datastoreUrl = value
    @property
    def swapPlacement(self) -> str: ...
    @swapPlacement.setter
    def swapPlacement(self, value: str):
        self._swapPlacement = value
    @property
    def bootOptions(self) -> BootOptions: ...
    @bootOptions.setter
    def bootOptions(self, value: BootOptions):
        self._bootOptions = value
    @property
    def ftInfo(self) -> FaultToleranceConfigInfo: ...
    @ftInfo.setter
    def ftInfo(self, value: FaultToleranceConfigInfo):
        self._ftInfo = value
    @property
    def repConfig(self) -> ReplicationConfigSpec: ...
    @repConfig.setter
    def repConfig(self, value: ReplicationConfigSpec):
        self._repConfig = value
    @property
    def vAppConfig(self) -> vim.vApp.VmConfigInfo: ...
    @vAppConfig.setter
    def vAppConfig(self, value: vim.vApp.VmConfigInfo):
        self._vAppConfig = value
    @property
    def vAssertsEnabled(self) -> bool: ...
    @vAssertsEnabled.setter
    def vAssertsEnabled(self, value: bool):
        self._vAssertsEnabled = value
    @property
    def changeTrackingEnabled(self) -> bool: ...
    @changeTrackingEnabled.setter
    def changeTrackingEnabled(self, value: bool):
        self._changeTrackingEnabled = value
    @property
    def firmware(self) -> str: ...
    @firmware.setter
    def firmware(self, value: str):
        self._firmware = value
    @property
    def maxMksConnections(self) -> int: ...
    @maxMksConnections.setter
    def maxMksConnections(self, value: int):
        self._maxMksConnections = value
    @property
    def guestAutoLockEnabled(self) -> bool: ...
    @guestAutoLockEnabled.setter
    def guestAutoLockEnabled(self, value: bool):
        self._guestAutoLockEnabled = value
    @property
    def managedBy(self) -> vim.ext.ManagedByInfo: ...
    @managedBy.setter
    def managedBy(self, value: vim.ext.ManagedByInfo):
        self._managedBy = value
    @property
    def memoryReservationLockedToMax(self) -> bool: ...
    @memoryReservationLockedToMax.setter
    def memoryReservationLockedToMax(self, value: bool):
        self._memoryReservationLockedToMax = value
    @property
    def initialOverhead(self) -> ConfigInfo.OverheadInfo: ...
    @initialOverhead.setter
    def initialOverhead(self, value: ConfigInfo.OverheadInfo):
        self._initialOverhead = value
    @property
    def nestedHVEnabled(self) -> bool: ...
    @nestedHVEnabled.setter
    def nestedHVEnabled(self, value: bool):
        self._nestedHVEnabled = value
    @property
    def vPMCEnabled(self) -> bool: ...
    @vPMCEnabled.setter
    def vPMCEnabled(self, value: bool):
        self._vPMCEnabled = value
    @property
    def scheduledHardwareUpgradeInfo(self) -> ScheduledHardwareUpgradeInfo: ...
    @scheduledHardwareUpgradeInfo.setter
    def scheduledHardwareUpgradeInfo(self, value: ScheduledHardwareUpgradeInfo):
        self._scheduledHardwareUpgradeInfo = value
    @property
    def forkConfigInfo(self) -> ForkConfigInfo: ...
    @forkConfigInfo.setter
    def forkConfigInfo(self, value: ForkConfigInfo):
        self._forkConfigInfo = value
    @property
    def vFlashCacheReservation(self) -> long: ...
    @vFlashCacheReservation.setter
    def vFlashCacheReservation(self, value: long):
        self._vFlashCacheReservation = value
    @property
    def vmxConfigChecksum(self) -> binary: ...
    @vmxConfigChecksum.setter
    def vmxConfigChecksum(self, value: binary):
        self._vmxConfigChecksum = value
    @property
    def messageBusTunnelEnabled(self) -> bool: ...
    @messageBusTunnelEnabled.setter
    def messageBusTunnelEnabled(self, value: bool):
        self._messageBusTunnelEnabled = value
    @property
    def vmStorageObjectId(self) -> str: ...
    @vmStorageObjectId.setter
    def vmStorageObjectId(self, value: str):
        self._vmStorageObjectId = value
    @property
    def swapStorageObjectId(self) -> str: ...
    @swapStorageObjectId.setter
    def swapStorageObjectId(self, value: str):
        self._swapStorageObjectId = value
    @property
    def keyId(self) -> vim.encryption.CryptoKeyId: ...
    @keyId.setter
    def keyId(self, value: vim.encryption.CryptoKeyId):
        self._keyId = value
    @property
    def guestIntegrityInfo(self) -> GuestIntegrityInfo: ...
    @guestIntegrityInfo.setter
    def guestIntegrityInfo(self, value: GuestIntegrityInfo):
        self._guestIntegrityInfo = value
    @property
    def migrateEncryption(self) -> str: ...
    @migrateEncryption.setter
    def migrateEncryption(self, value: str):
        self._migrateEncryption = value
    @property
    def sgxInfo(self) -> SgxInfo: ...
    @sgxInfo.setter
    def sgxInfo(self, value: SgxInfo):
        self._sgxInfo = value
    @property
    def contentLibItemInfo(self) -> ContentLibraryItemInfo: ...
    @contentLibItemInfo.setter
    def contentLibItemInfo(self, value: ContentLibraryItemInfo):
        self._contentLibItemInfo = value
    @property
    def ftEncryptionMode(self) -> str: ...
    @ftEncryptionMode.setter
    def ftEncryptionMode(self, value: str):
        self._ftEncryptionMode = value
    @property
    def guestMonitoringModeInfo(self) -> GuestMonitoringModeInfo: ...
    @guestMonitoringModeInfo.setter
    def guestMonitoringModeInfo(self, value: GuestMonitoringModeInfo):
        self._guestMonitoringModeInfo = value
    @property
    def sevEnabled(self) -> bool: ...
    @sevEnabled.setter
    def sevEnabled(self, value: bool):
        self._sevEnabled = value
    @property
    def numaInfo(self) -> VirtualNumaInfo: ...
    @numaInfo.setter
    def numaInfo(self, value: VirtualNumaInfo):
        self._numaInfo = value
    @property
    def pmemFailoverEnabled(self) -> bool: ...
    @pmemFailoverEnabled.setter
    def pmemFailoverEnabled(self, value: bool):
        self._pmemFailoverEnabled = value
    @property
    def vmxStatsCollectionEnabled(self) -> bool: ...
    @vmxStatsCollectionEnabled.setter
    def vmxStatsCollectionEnabled(self, value: bool):
        self._vmxStatsCollectionEnabled = value
    @property
    def vmOpNotificationToAppEnabled(self) -> bool: ...
    @vmOpNotificationToAppEnabled.setter
    def vmOpNotificationToAppEnabled(self, value: bool):
        self._vmOpNotificationToAppEnabled = value
    @property
    def vmOpNotificationTimeout(self) -> long: ...
    @vmOpNotificationTimeout.setter
    def vmOpNotificationTimeout(self, value: long):
        self._vmOpNotificationTimeout = value
    @property
    def deviceSwap(self) -> VirtualDeviceSwap: ...
    @deviceSwap.setter
    def deviceSwap(self, value: VirtualDeviceSwap):
        self._deviceSwap = value
    @property
    def pmem(self) -> VirtualPMem: ...
    @pmem.setter
    def pmem(self, value: VirtualPMem):
        self._pmem = value
    @property
    def deviceGroups(self) -> VirtualDeviceGroups: ...
    @deviceGroups.setter
    def deviceGroups(self, value: VirtualDeviceGroups):
        self._deviceGroups = value
    @property
    def fixedPassthruHotPlugEnabled(self) -> bool: ...
    @fixedPassthruHotPlugEnabled.setter
    def fixedPassthruHotPlugEnabled(self, value: bool):
        self._fixedPassthruHotPlugEnabled = value


    class DatastoreUrlPair(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value


    class OverheadInfo(vmodl.DynamicData):
        @property
        def initialMemoryReservation(self) -> long: ...
        @initialMemoryReservation.setter
        def initialMemoryReservation(self, value: long):
            self._initialMemoryReservation = value
        @property
        def initialSwapReservation(self) -> long: ...
        @initialSwapReservation.setter
        def initialSwapReservation(self, value: long):
            self._initialSwapReservation = value


    class NpivWwnType(Enum):
        vc = "vc"
        host = "host"
        external = "external"


    class SwapPlacementType(Enum):
        inherit = "inherit"
        vmDirectory = "vmDirectory"
        hostLocal = "hostLocal"


class ConfigOption(vmodl.DynamicData):
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def guestOSDescriptor(self) -> List[GuestOsDescriptor]: ...
    @guestOSDescriptor.setter
    def guestOSDescriptor(self, value: List[GuestOsDescriptor]):
        self._guestOSDescriptor = value
    @property
    def guestOSDefaultIndex(self) -> int: ...
    @guestOSDefaultIndex.setter
    def guestOSDefaultIndex(self, value: int):
        self._guestOSDefaultIndex = value
    @property
    def hardwareOptions(self) -> VirtualHardwareOption: ...
    @hardwareOptions.setter
    def hardwareOptions(self, value: VirtualHardwareOption):
        self._hardwareOptions = value
    @property
    def capabilities(self) -> Capability: ...
    @capabilities.setter
    def capabilities(self, value: Capability):
        self._capabilities = value
    @property
    def datastore(self) -> DatastoreOption: ...
    @datastore.setter
    def datastore(self, value: DatastoreOption):
        self._datastore = value
    @property
    def defaultDevice(self) -> List[vim.vm.device.VirtualDevice]: ...
    @defaultDevice.setter
    def defaultDevice(self, value: List[vim.vm.device.VirtualDevice]):
        self._defaultDevice = value
    @property
    def supportedMonitorType(self) -> List[str]: ...
    @supportedMonitorType.setter
    def supportedMonitorType(self, value: List[str]):
        self._supportedMonitorType = value
    @property
    def supportedOvfEnvironmentTransport(self) -> List[str]: ...
    @supportedOvfEnvironmentTransport.setter
    def supportedOvfEnvironmentTransport(self, value: List[str]):
        self._supportedOvfEnvironmentTransport = value
    @property
    def supportedOvfInstallTransport(self) -> List[str]: ...
    @supportedOvfInstallTransport.setter
    def supportedOvfInstallTransport(self, value: List[str]):
        self._supportedOvfInstallTransport = value
    @property
    def propertyRelations(self) -> List[PropertyRelation]: ...
    @propertyRelations.setter
    def propertyRelations(self, value: List[PropertyRelation]):
        self._propertyRelations = value


class ConfigOptionDescriptor(vmodl.DynamicData):
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
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @host.setter
    def host(self, value: List[vim.HostSystem]):
        self._host = value
    @property
    def createSupported(self) -> bool: ...
    @createSupported.setter
    def createSupported(self, value: bool):
        self._createSupported = value
    @property
    def defaultConfigOption(self) -> bool: ...
    @defaultConfigOption.setter
    def defaultConfigOption(self, value: bool):
        self._defaultConfigOption = value
    @property
    def runSupported(self) -> bool: ...
    @runSupported.setter
    def runSupported(self, value: bool):
        self._runSupported = value
    @property
    def upgradeSupported(self) -> bool: ...
    @upgradeSupported.setter
    def upgradeSupported(self, value: bool):
        self._upgradeSupported = value


class ConfigSpec(vmodl.DynamicData):
    @property
    def changeVersion(self) -> str: ...
    @changeVersion.setter
    def changeVersion(self, value: str):
        self._changeVersion = value
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
    def createDate(self) -> datetime: ...
    @createDate.setter
    def createDate(self, value: datetime):
        self._createDate = value
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value
    @property
    def npivNodeWorldWideName(self) -> List[long]: ...
    @npivNodeWorldWideName.setter
    def npivNodeWorldWideName(self, value: List[long]):
        self._npivNodeWorldWideName = value
    @property
    def npivPortWorldWideName(self) -> List[long]: ...
    @npivPortWorldWideName.setter
    def npivPortWorldWideName(self, value: List[long]):
        self._npivPortWorldWideName = value
    @property
    def npivWorldWideNameType(self) -> str: ...
    @npivWorldWideNameType.setter
    def npivWorldWideNameType(self, value: str):
        self._npivWorldWideNameType = value
    @property
    def npivDesiredNodeWwns(self) -> short: ...
    @npivDesiredNodeWwns.setter
    def npivDesiredNodeWwns(self, value: short):
        self._npivDesiredNodeWwns = value
    @property
    def npivDesiredPortWwns(self) -> short: ...
    @npivDesiredPortWwns.setter
    def npivDesiredPortWwns(self, value: short):
        self._npivDesiredPortWwns = value
    @property
    def npivTemporaryDisabled(self) -> bool: ...
    @npivTemporaryDisabled.setter
    def npivTemporaryDisabled(self, value: bool):
        self._npivTemporaryDisabled = value
    @property
    def npivOnNonRdmDisks(self) -> bool: ...
    @npivOnNonRdmDisks.setter
    def npivOnNonRdmDisks(self, value: bool):
        self._npivOnNonRdmDisks = value
    @property
    def npivWorldWideNameOp(self) -> str: ...
    @npivWorldWideNameOp.setter
    def npivWorldWideNameOp(self, value: str):
        self._npivWorldWideNameOp = value
    @property
    def locationId(self) -> str: ...
    @locationId.setter
    def locationId(self, value: str):
        self._locationId = value
    @property
    def guestId(self) -> str: ...
    @guestId.setter
    def guestId(self, value: str):
        self._guestId = value
    @property
    def alternateGuestName(self) -> str: ...
    @alternateGuestName.setter
    def alternateGuestName(self, value: str):
        self._alternateGuestName = value
    @property
    def annotation(self) -> str: ...
    @annotation.setter
    def annotation(self, value: str):
        self._annotation = value
    @property
    def files(self) -> FileInfo: ...
    @files.setter
    def files(self, value: FileInfo):
        self._files = value
    @property
    def tools(self) -> ToolsConfigInfo: ...
    @tools.setter
    def tools(self, value: ToolsConfigInfo):
        self._tools = value
    @property
    def flags(self) -> FlagInfo: ...
    @flags.setter
    def flags(self, value: FlagInfo):
        self._flags = value
    @property
    def consolePreferences(self) -> ConsolePreferences: ...
    @consolePreferences.setter
    def consolePreferences(self, value: ConsolePreferences):
        self._consolePreferences = value
    @property
    def powerOpInfo(self) -> DefaultPowerOpInfo: ...
    @powerOpInfo.setter
    def powerOpInfo(self, value: DefaultPowerOpInfo):
        self._powerOpInfo = value
    @property
    def rebootPowerOff(self) -> bool: ...
    @rebootPowerOff.setter
    def rebootPowerOff(self, value: bool):
        self._rebootPowerOff = value
    @property
    def numCPUs(self) -> int: ...
    @numCPUs.setter
    def numCPUs(self, value: int):
        self._numCPUs = value
    @property
    def vcpuConfig(self) -> List[VcpuConfig]: ...
    @vcpuConfig.setter
    def vcpuConfig(self, value: List[VcpuConfig]):
        self._vcpuConfig = value
    @property
    def numCoresPerSocket(self) -> int: ...
    @numCoresPerSocket.setter
    def numCoresPerSocket(self, value: int):
        self._numCoresPerSocket = value
    @property
    def memoryMB(self) -> long: ...
    @memoryMB.setter
    def memoryMB(self, value: long):
        self._memoryMB = value
    @property
    def memoryHotAddEnabled(self) -> bool: ...
    @memoryHotAddEnabled.setter
    def memoryHotAddEnabled(self, value: bool):
        self._memoryHotAddEnabled = value
    @property
    def cpuHotAddEnabled(self) -> bool: ...
    @cpuHotAddEnabled.setter
    def cpuHotAddEnabled(self, value: bool):
        self._cpuHotAddEnabled = value
    @property
    def cpuHotRemoveEnabled(self) -> bool: ...
    @cpuHotRemoveEnabled.setter
    def cpuHotRemoveEnabled(self, value: bool):
        self._cpuHotRemoveEnabled = value
    @property
    def virtualICH7MPresent(self) -> bool: ...
    @virtualICH7MPresent.setter
    def virtualICH7MPresent(self, value: bool):
        self._virtualICH7MPresent = value
    @property
    def virtualSMCPresent(self) -> bool: ...
    @virtualSMCPresent.setter
    def virtualSMCPresent(self, value: bool):
        self._virtualSMCPresent = value
    @property
    def deviceChange(self) -> List[vim.vm.device.VirtualDeviceSpec]: ...
    @deviceChange.setter
    def deviceChange(self, value: List[vim.vm.device.VirtualDeviceSpec]):
        self._deviceChange = value
    @property
    def cpuAllocation(self) -> vim.ResourceAllocationInfo: ...
    @cpuAllocation.setter
    def cpuAllocation(self, value: vim.ResourceAllocationInfo):
        self._cpuAllocation = value
    @property
    def memoryAllocation(self) -> vim.ResourceAllocationInfo: ...
    @memoryAllocation.setter
    def memoryAllocation(self, value: vim.ResourceAllocationInfo):
        self._memoryAllocation = value
    @property
    def latencySensitivity(self) -> vim.LatencySensitivity: ...
    @latencySensitivity.setter
    def latencySensitivity(self, value: vim.LatencySensitivity):
        self._latencySensitivity = value
    @property
    def cpuAffinity(self) -> AffinityInfo: ...
    @cpuAffinity.setter
    def cpuAffinity(self, value: AffinityInfo):
        self._cpuAffinity = value
    @property
    def memoryAffinity(self) -> AffinityInfo: ...
    @memoryAffinity.setter
    def memoryAffinity(self, value: AffinityInfo):
        self._memoryAffinity = value
    @property
    def networkShaper(self) -> NetworkShaperInfo: ...
    @networkShaper.setter
    def networkShaper(self, value: NetworkShaperInfo):
        self._networkShaper = value
    @property
    def cpuFeatureMask(self) -> List[ConfigSpec.CpuIdInfoSpec]: ...
    @cpuFeatureMask.setter
    def cpuFeatureMask(self, value: List[ConfigSpec.CpuIdInfoSpec]):
        self._cpuFeatureMask = value
    @property
    def extraConfig(self) -> List[vim.option.OptionValue]: ...
    @extraConfig.setter
    def extraConfig(self, value: List[vim.option.OptionValue]):
        self._extraConfig = value
    @property
    def swapPlacement(self) -> str: ...
    @swapPlacement.setter
    def swapPlacement(self, value: str):
        self._swapPlacement = value
    @property
    def bootOptions(self) -> BootOptions: ...
    @bootOptions.setter
    def bootOptions(self, value: BootOptions):
        self._bootOptions = value
    @property
    def vAppConfig(self) -> vim.vApp.VmConfigSpec: ...
    @vAppConfig.setter
    def vAppConfig(self, value: vim.vApp.VmConfigSpec):
        self._vAppConfig = value
    @property
    def ftInfo(self) -> FaultToleranceConfigInfo: ...
    @ftInfo.setter
    def ftInfo(self, value: FaultToleranceConfigInfo):
        self._ftInfo = value
    @property
    def repConfig(self) -> ReplicationConfigSpec: ...
    @repConfig.setter
    def repConfig(self, value: ReplicationConfigSpec):
        self._repConfig = value
    @property
    def vAppConfigRemoved(self) -> bool: ...
    @vAppConfigRemoved.setter
    def vAppConfigRemoved(self, value: bool):
        self._vAppConfigRemoved = value
    @property
    def vAssertsEnabled(self) -> bool: ...
    @vAssertsEnabled.setter
    def vAssertsEnabled(self, value: bool):
        self._vAssertsEnabled = value
    @property
    def changeTrackingEnabled(self) -> bool: ...
    @changeTrackingEnabled.setter
    def changeTrackingEnabled(self, value: bool):
        self._changeTrackingEnabled = value
    @property
    def firmware(self) -> str: ...
    @firmware.setter
    def firmware(self, value: str):
        self._firmware = value
    @property
    def maxMksConnections(self) -> int: ...
    @maxMksConnections.setter
    def maxMksConnections(self, value: int):
        self._maxMksConnections = value
    @property
    def guestAutoLockEnabled(self) -> bool: ...
    @guestAutoLockEnabled.setter
    def guestAutoLockEnabled(self, value: bool):
        self._guestAutoLockEnabled = value
    @property
    def managedBy(self) -> vim.ext.ManagedByInfo: ...
    @managedBy.setter
    def managedBy(self, value: vim.ext.ManagedByInfo):
        self._managedBy = value
    @property
    def memoryReservationLockedToMax(self) -> bool: ...
    @memoryReservationLockedToMax.setter
    def memoryReservationLockedToMax(self, value: bool):
        self._memoryReservationLockedToMax = value
    @property
    def nestedHVEnabled(self) -> bool: ...
    @nestedHVEnabled.setter
    def nestedHVEnabled(self, value: bool):
        self._nestedHVEnabled = value
    @property
    def vPMCEnabled(self) -> bool: ...
    @vPMCEnabled.setter
    def vPMCEnabled(self, value: bool):
        self._vPMCEnabled = value
    @property
    def scheduledHardwareUpgradeInfo(self) -> ScheduledHardwareUpgradeInfo: ...
    @scheduledHardwareUpgradeInfo.setter
    def scheduledHardwareUpgradeInfo(self, value: ScheduledHardwareUpgradeInfo):
        self._scheduledHardwareUpgradeInfo = value
    @property
    def vmProfile(self) -> List[ProfileSpec]: ...
    @vmProfile.setter
    def vmProfile(self, value: List[ProfileSpec]):
        self._vmProfile = value
    @property
    def messageBusTunnelEnabled(self) -> bool: ...
    @messageBusTunnelEnabled.setter
    def messageBusTunnelEnabled(self, value: bool):
        self._messageBusTunnelEnabled = value
    @property
    def crypto(self) -> vim.encryption.CryptoSpec: ...
    @crypto.setter
    def crypto(self, value: vim.encryption.CryptoSpec):
        self._crypto = value
    @property
    def migrateEncryption(self) -> str: ...
    @migrateEncryption.setter
    def migrateEncryption(self, value: str):
        self._migrateEncryption = value
    @property
    def sgxInfo(self) -> SgxInfo: ...
    @sgxInfo.setter
    def sgxInfo(self, value: SgxInfo):
        self._sgxInfo = value
    @property
    def ftEncryptionMode(self) -> str: ...
    @ftEncryptionMode.setter
    def ftEncryptionMode(self, value: str):
        self._ftEncryptionMode = value
    @property
    def guestMonitoringModeInfo(self) -> GuestMonitoringModeInfo: ...
    @guestMonitoringModeInfo.setter
    def guestMonitoringModeInfo(self, value: GuestMonitoringModeInfo):
        self._guestMonitoringModeInfo = value
    @property
    def sevEnabled(self) -> bool: ...
    @sevEnabled.setter
    def sevEnabled(self, value: bool):
        self._sevEnabled = value
    @property
    def virtualNuma(self) -> VirtualNuma: ...
    @virtualNuma.setter
    def virtualNuma(self, value: VirtualNuma):
        self._virtualNuma = value
    @property
    def motherboardLayout(self) -> str: ...
    @motherboardLayout.setter
    def motherboardLayout(self, value: str):
        self._motherboardLayout = value
    @property
    def pmemFailoverEnabled(self) -> bool: ...
    @pmemFailoverEnabled.setter
    def pmemFailoverEnabled(self, value: bool):
        self._pmemFailoverEnabled = value
    @property
    def vmxStatsCollectionEnabled(self) -> bool: ...
    @vmxStatsCollectionEnabled.setter
    def vmxStatsCollectionEnabled(self, value: bool):
        self._vmxStatsCollectionEnabled = value
    @property
    def vmOpNotificationToAppEnabled(self) -> bool: ...
    @vmOpNotificationToAppEnabled.setter
    def vmOpNotificationToAppEnabled(self, value: bool):
        self._vmOpNotificationToAppEnabled = value
    @property
    def vmOpNotificationTimeout(self) -> long: ...
    @vmOpNotificationTimeout.setter
    def vmOpNotificationTimeout(self, value: long):
        self._vmOpNotificationTimeout = value
    @property
    def deviceSwap(self) -> VirtualDeviceSwap: ...
    @deviceSwap.setter
    def deviceSwap(self, value: VirtualDeviceSwap):
        self._deviceSwap = value
    @property
    def simultaneousThreads(self) -> int: ...
    @simultaneousThreads.setter
    def simultaneousThreads(self, value: int):
        self._simultaneousThreads = value
    @property
    def pmem(self) -> VirtualPMem: ...
    @pmem.setter
    def pmem(self, value: VirtualPMem):
        self._pmem = value
    @property
    def deviceGroups(self) -> VirtualDeviceGroups: ...
    @deviceGroups.setter
    def deviceGroups(self, value: VirtualDeviceGroups):
        self._deviceGroups = value
    @property
    def fixedPassthruHotPlugEnabled(self) -> bool: ...
    @fixedPassthruHotPlugEnabled.setter
    def fixedPassthruHotPlugEnabled(self, value: bool):
        self._fixedPassthruHotPlugEnabled = value


    class CpuIdInfoSpec(vim.option.ArrayUpdateSpec):
        @property
        def info(self) -> vim.host.CpuIdInfo: ...
        @info.setter
        def info(self, value: vim.host.CpuIdInfo):
            self._info = value


    class EncryptedFtModes(Enum):
        ftEncryptionDisabled = "ftEncryptionDisabled"
        ftEncryptionOpportunistic = "ftEncryptionOpportunistic"
        ftEncryptionRequired = "ftEncryptionRequired"


    class EncryptedVMotionModes(Enum):
        disabled = "disabled"
        opportunistic = "opportunistic"
        required = "required"


    class NpivWwnOp(Enum):
        generate = "generate"
        set = "set"
        remove = "remove"
        extend = "extend"


class ConfigTarget(vmodl.DynamicData):
    @property
    def numCpus(self) -> int: ...
    @numCpus.setter
    def numCpus(self, value: int):
        self._numCpus = value
    @property
    def numCpuCores(self) -> int: ...
    @numCpuCores.setter
    def numCpuCores(self, value: int):
        self._numCpuCores = value
    @property
    def numNumaNodes(self) -> int: ...
    @numNumaNodes.setter
    def numNumaNodes(self, value: int):
        self._numNumaNodes = value
    @property
    def maxCpusPerHost(self) -> int: ...
    @maxCpusPerHost.setter
    def maxCpusPerHost(self, value: int):
        self._maxCpusPerHost = value
    @property
    def smcPresent(self) -> bool: ...
    @smcPresent.setter
    def smcPresent(self, value: bool):
        self._smcPresent = value
    @property
    def datastore(self) -> List[DatastoreInfo]: ...
    @datastore.setter
    def datastore(self, value: List[DatastoreInfo]):
        self._datastore = value
    @property
    def network(self) -> List[NetworkInfo]: ...
    @network.setter
    def network(self, value: List[NetworkInfo]):
        self._network = value
    @property
    def opaqueNetwork(self) -> List[OpaqueNetworkInfo]: ...
    @opaqueNetwork.setter
    def opaqueNetwork(self, value: List[OpaqueNetworkInfo]):
        self._opaqueNetwork = value
    @property
    def distributedVirtualPortgroup(self) -> List[vim.dvs.DistributedVirtualPortgroupInfo]: ...
    @distributedVirtualPortgroup.setter
    def distributedVirtualPortgroup(self, value: List[vim.dvs.DistributedVirtualPortgroupInfo]):
        self._distributedVirtualPortgroup = value
    @property
    def distributedVirtualSwitch(self) -> List[vim.dvs.DistributedVirtualSwitchInfo]: ...
    @distributedVirtualSwitch.setter
    def distributedVirtualSwitch(self, value: List[vim.dvs.DistributedVirtualSwitchInfo]):
        self._distributedVirtualSwitch = value
    @property
    def cdRom(self) -> List[CdromInfo]: ...
    @cdRom.setter
    def cdRom(self, value: List[CdromInfo]):
        self._cdRom = value
    @property
    def serial(self) -> List[SerialInfo]: ...
    @serial.setter
    def serial(self, value: List[SerialInfo]):
        self._serial = value
    @property
    def parallel(self) -> List[ParallelInfo]: ...
    @parallel.setter
    def parallel(self, value: List[ParallelInfo]):
        self._parallel = value
    @property
    def sound(self) -> List[SoundInfo]: ...
    @sound.setter
    def sound(self, value: List[SoundInfo]):
        self._sound = value
    @property
    def usb(self) -> List[UsbInfo]: ...
    @usb.setter
    def usb(self, value: List[UsbInfo]):
        self._usb = value
    @property
    def floppy(self) -> List[FloppyInfo]: ...
    @floppy.setter
    def floppy(self, value: List[FloppyInfo]):
        self._floppy = value
    @property
    def legacyNetworkInfo(self) -> List[LegacyNetworkSwitchInfo]: ...
    @legacyNetworkInfo.setter
    def legacyNetworkInfo(self, value: List[LegacyNetworkSwitchInfo]):
        self._legacyNetworkInfo = value
    @property
    def scsiPassthrough(self) -> List[ScsiPassthroughInfo]: ...
    @scsiPassthrough.setter
    def scsiPassthrough(self, value: List[ScsiPassthroughInfo]):
        self._scsiPassthrough = value
    @property
    def scsiDisk(self) -> List[ScsiDiskDeviceInfo]: ...
    @scsiDisk.setter
    def scsiDisk(self, value: List[ScsiDiskDeviceInfo]):
        self._scsiDisk = value
    @property
    def ideDisk(self) -> List[IdeDiskDeviceInfo]: ...
    @ideDisk.setter
    def ideDisk(self, value: List[IdeDiskDeviceInfo]):
        self._ideDisk = value
    @property
    def maxMemMBOptimalPerf(self) -> int: ...
    @maxMemMBOptimalPerf.setter
    def maxMemMBOptimalPerf(self, value: int):
        self._maxMemMBOptimalPerf = value
    @property
    def supportedMaxMemMB(self) -> int: ...
    @supportedMaxMemMB.setter
    def supportedMaxMemMB(self, value: int):
        self._supportedMaxMemMB = value
    @property
    def resourcePool(self) -> vim.ResourcePool.RuntimeInfo: ...
    @resourcePool.setter
    def resourcePool(self, value: vim.ResourcePool.RuntimeInfo):
        self._resourcePool = value
    @property
    def autoVmotion(self) -> bool: ...
    @autoVmotion.setter
    def autoVmotion(self, value: bool):
        self._autoVmotion = value
    @property
    def pciPassthrough(self) -> List[PciPassthroughInfo]: ...
    @pciPassthrough.setter
    def pciPassthrough(self, value: List[PciPassthroughInfo]):
        self._pciPassthrough = value
    @property
    def sriov(self) -> List[SriovInfo]: ...
    @sriov.setter
    def sriov(self, value: List[SriovInfo]):
        self._sriov = value
    @property
    def vFlashModule(self) -> List[VFlashModuleInfo]: ...
    @vFlashModule.setter
    def vFlashModule(self, value: List[VFlashModuleInfo]):
        self._vFlashModule = value
    @property
    def sharedGpuPassthroughTypes(self) -> List[PciSharedGpuPassthroughInfo]: ...
    @sharedGpuPassthroughTypes.setter
    def sharedGpuPassthroughTypes(self, value: List[PciSharedGpuPassthroughInfo]):
        self._sharedGpuPassthroughTypes = value
    @property
    def availablePersistentMemoryReservationMB(self) -> long: ...
    @availablePersistentMemoryReservationMB.setter
    def availablePersistentMemoryReservationMB(self, value: long):
        self._availablePersistentMemoryReservationMB = value
    @property
    def dynamicPassthrough(self) -> List[DynamicPassthroughInfo]: ...
    @dynamicPassthrough.setter
    def dynamicPassthrough(self, value: List[DynamicPassthroughInfo]):
        self._dynamicPassthrough = value
    @property
    def sgxTargetInfo(self) -> SgxTargetInfo: ...
    @sgxTargetInfo.setter
    def sgxTargetInfo(self, value: SgxTargetInfo):
        self._sgxTargetInfo = value
    @property
    def precisionClockInfo(self) -> List[PrecisionClockInfo]: ...
    @precisionClockInfo.setter
    def precisionClockInfo(self, value: List[PrecisionClockInfo]):
        self._precisionClockInfo = value
    @property
    def sevSupported(self) -> bool: ...
    @sevSupported.setter
    def sevSupported(self, value: bool):
        self._sevSupported = value
    @property
    def vgpuDeviceInfo(self) -> List[VgpuDeviceInfo]: ...
    @vgpuDeviceInfo.setter
    def vgpuDeviceInfo(self, value: List[VgpuDeviceInfo]):
        self._vgpuDeviceInfo = value
    @property
    def vgpuProfileInfo(self) -> List[VgpuProfileInfo]: ...
    @vgpuProfileInfo.setter
    def vgpuProfileInfo(self, value: List[VgpuProfileInfo]):
        self._vgpuProfileInfo = value
    @property
    def vendorDeviceGroupInfo(self) -> List[VendorDeviceGroupInfo]: ...
    @vendorDeviceGroupInfo.setter
    def vendorDeviceGroupInfo(self, value: List[VendorDeviceGroupInfo]):
        self._vendorDeviceGroupInfo = value
    @property
    def maxSimultaneousThreads(self) -> int: ...
    @maxSimultaneousThreads.setter
    def maxSimultaneousThreads(self, value: int):
        self._maxSimultaneousThreads = value
    @property
    def dvxClassInfo(self) -> List[DvxClassInfo]: ...
    @dvxClassInfo.setter
    def dvxClassInfo(self, value: List[DvxClassInfo]):
        self._dvxClassInfo = value


class ConsolePreferences(vmodl.DynamicData):
    @property
    def powerOnWhenOpened(self) -> bool: ...
    @powerOnWhenOpened.setter
    def powerOnWhenOpened(self, value: bool):
        self._powerOnWhenOpened = value
    @property
    def enterFullScreenOnPowerOn(self) -> bool: ...
    @enterFullScreenOnPowerOn.setter
    def enterFullScreenOnPowerOn(self, value: bool):
        self._enterFullScreenOnPowerOn = value
    @property
    def closeOnPowerOffOrSuspend(self) -> bool: ...
    @closeOnPowerOffOrSuspend.setter
    def closeOnPowerOffOrSuspend(self, value: bool):
        self._closeOnPowerOffOrSuspend = value


class ContentLibraryItemInfo(vmodl.DynamicData):
    @property
    def contentLibraryItemUuid(self) -> str: ...
    @contentLibraryItemUuid.setter
    def contentLibraryItemUuid(self, value: str):
        self._contentLibraryItemUuid = value
    @property
    def contentLibraryItemVersion(self) -> str: ...
    @contentLibraryItemVersion.setter
    def contentLibraryItemVersion(self, value: str):
        self._contentLibraryItemVersion = value


class DatastoreInfo(TargetInfo):
    @property
    def datastore(self) -> vim.Datastore.Summary: ...
    @datastore.setter
    def datastore(self, value: vim.Datastore.Summary):
        self._datastore = value
    @property
    def capability(self) -> vim.Datastore.Capability: ...
    @capability.setter
    def capability(self, value: vim.Datastore.Capability):
        self._capability = value
    @property
    def maxFileSize(self) -> long: ...
    @maxFileSize.setter
    def maxFileSize(self, value: long):
        self._maxFileSize = value
    @property
    def maxVirtualDiskCapacity(self) -> long: ...
    @maxVirtualDiskCapacity.setter
    def maxVirtualDiskCapacity(self, value: long):
        self._maxVirtualDiskCapacity = value
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
    def mode(self) -> str: ...
    @mode.setter
    def mode(self, value: str):
        self._mode = value
    @property
    def vStorageSupport(self) -> str: ...
    @vStorageSupport.setter
    def vStorageSupport(self, value: str):
        self._vStorageSupport = value


class DatastoreOption(vmodl.DynamicData):
    @property
    def unsupportedVolumes(self) -> List[DatastoreOption.FileSystemVolumeOption]: ...
    @unsupportedVolumes.setter
    def unsupportedVolumes(self, value: List[DatastoreOption.FileSystemVolumeOption]):
        self._unsupportedVolumes = value


    class FileSystemVolumeOption(vmodl.DynamicData):
        @property
        def fileSystemType(self) -> type: ...
        @fileSystemType.setter
        def fileSystemType(self, value: type):
            self._fileSystemType = value
        @property
        def majorVersion(self) -> int: ...
        @majorVersion.setter
        def majorVersion(self, value: int):
            self._majorVersion = value


class DefaultPowerOpInfo(vmodl.DynamicData):
    @property
    def powerOffType(self) -> str: ...
    @powerOffType.setter
    def powerOffType(self, value: str):
        self._powerOffType = value
    @property
    def suspendType(self) -> str: ...
    @suspendType.setter
    def suspendType(self, value: str):
        self._suspendType = value
    @property
    def resetType(self) -> str: ...
    @resetType.setter
    def resetType(self, value: str):
        self._resetType = value
    @property
    def defaultPowerOffType(self) -> str: ...
    @defaultPowerOffType.setter
    def defaultPowerOffType(self, value: str):
        self._defaultPowerOffType = value
    @property
    def defaultSuspendType(self) -> str: ...
    @defaultSuspendType.setter
    def defaultSuspendType(self, value: str):
        self._defaultSuspendType = value
    @property
    def defaultResetType(self) -> str: ...
    @defaultResetType.setter
    def defaultResetType(self, value: str):
        self._defaultResetType = value
    @property
    def standbyAction(self) -> str: ...
    @standbyAction.setter
    def standbyAction(self, value: str):
        self._standbyAction = value


    class PowerOpType(Enum):
        soft = "soft"
        hard = "hard"
        preset = "preset"


    class StandbyActionType(Enum):
        checkpoint = "checkpoint"
        powerOnSuspend = "powerOnSuspend"


class DefaultProfileSpec(ProfileSpec): ...


class DefinedProfileSpec(ProfileSpec):
    @property
    def profileId(self) -> str: ...
    @profileId.setter
    def profileId(self, value: str):
        self._profileId = value
    @property
    def replicationSpec(self) -> vim.vm.replication.ReplicationSpec: ...
    @replicationSpec.setter
    def replicationSpec(self, value: vim.vm.replication.ReplicationSpec):
        self._replicationSpec = value
    @property
    def profileData(self) -> ProfileRawData: ...
    @profileData.setter
    def profileData(self, value: ProfileRawData):
        self._profileData = value
    @property
    def profileParams(self) -> List[vim.KeyValue]: ...
    @profileParams.setter
    def profileParams(self, value: List[vim.KeyValue]):
        self._profileParams = value


class DeviceRuntimeInfo(vmodl.DynamicData):
    @property
    def runtimeState(self) -> DeviceRuntimeInfo.DeviceRuntimeState: ...
    @runtimeState.setter
    def runtimeState(self, value: DeviceRuntimeInfo.DeviceRuntimeState):
        self._runtimeState = value
    @property
    def key(self) -> int: ...
    @key.setter
    def key(self, value: int):
        self._key = value


    class DeviceRuntimeState(vmodl.DynamicData): ...


    class VirtualEthernetCardRuntimeState(DeviceRuntimeInfo.DeviceRuntimeState):
        @property
        def vmDirectPathGen2Active(self) -> bool: ...
        @vmDirectPathGen2Active.setter
        def vmDirectPathGen2Active(self, value: bool):
            self._vmDirectPathGen2Active = value
        @property
        def vmDirectPathGen2InactiveReasonVm(self) -> List[str]: ...
        @vmDirectPathGen2InactiveReasonVm.setter
        def vmDirectPathGen2InactiveReasonVm(self, value: List[str]):
            self._vmDirectPathGen2InactiveReasonVm = value
        @property
        def vmDirectPathGen2InactiveReasonOther(self) -> List[str]: ...
        @vmDirectPathGen2InactiveReasonOther.setter
        def vmDirectPathGen2InactiveReasonOther(self, value: List[str]):
            self._vmDirectPathGen2InactiveReasonOther = value
        @property
        def vmDirectPathGen2InactiveReasonExtended(self) -> str: ...
        @vmDirectPathGen2InactiveReasonExtended.setter
        def vmDirectPathGen2InactiveReasonExtended(self, value: str):
            self._vmDirectPathGen2InactiveReasonExtended = value
        @property
        def uptv2Active(self) -> bool: ...
        @uptv2Active.setter
        def uptv2Active(self, value: bool):
            self._uptv2Active = value
        @property
        def uptv2InactiveReasonVm(self) -> List[str]: ...
        @uptv2InactiveReasonVm.setter
        def uptv2InactiveReasonVm(self, value: List[str]):
            self._uptv2InactiveReasonVm = value
        @property
        def uptv2InactiveReasonOther(self) -> List[str]: ...
        @uptv2InactiveReasonOther.setter
        def uptv2InactiveReasonOther(self, value: List[str]):
            self._uptv2InactiveReasonOther = value
        @property
        def reservationStatus(self) -> str: ...
        @reservationStatus.setter
        def reservationStatus(self, value: str):
            self._reservationStatus = value
        @property
        def attachmentStatus(self) -> str: ...
        @attachmentStatus.setter
        def attachmentStatus(self, value: str):
            self._attachmentStatus = value
        @property
        def featureRequirement(self) -> List[FeatureRequirement]: ...
        @featureRequirement.setter
        def featureRequirement(self, value: List[FeatureRequirement]):
            self._featureRequirement = value


        class VmDirectPathGen2InactiveReasonOther(Enum):
            vmNptIncompatibleHost = "vmNptIncompatibleHost"
            vmNptIncompatibleNetwork = "vmNptIncompatibleNetwork"


        class VmDirectPathGen2InactiveReasonVm(Enum):
            vmNptIncompatibleGuest = "vmNptIncompatibleGuest"
            vmNptIncompatibleGuestDriver = "vmNptIncompatibleGuestDriver"
            vmNptIncompatibleAdapterType = "vmNptIncompatibleAdapterType"
            vmNptDisabledOrDisconnectedAdapter = "vmNptDisabledOrDisconnectedAdapter"
            vmNptIncompatibleAdapterFeatures = "vmNptIncompatibleAdapterFeatures"
            vmNptIncompatibleBackingType = "vmNptIncompatibleBackingType"
            vmNptInsufficientMemoryReservation = "vmNptInsufficientMemoryReservation"
            vmNptFaultToleranceOrRecordReplayConfigured = "vmNptFaultToleranceOrRecordReplayConfigured"
            vmNptConflictingIOChainConfigured = "vmNptConflictingIOChainConfigured"
            vmNptMonitorBlocks = "vmNptMonitorBlocks"
            vmNptConflictingOperationInProgress = "vmNptConflictingOperationInProgress"
            vmNptRuntimeError = "vmNptRuntimeError"
            vmNptOutOfIntrVector = "vmNptOutOfIntrVector"
            vmNptVMCIActive = "vmNptVMCIActive"


class DiskDeviceInfo(TargetInfo):
    @property
    def capacity(self) -> long: ...
    @capacity.setter
    def capacity(self, value: long):
        self._capacity = value
    @property
    def vm(self) -> List[vim.VirtualMachine]: ...
    @vm.setter
    def vm(self, value: List[vim.VirtualMachine]):
        self._vm = value


class DvxClassInfo(vmodl.DynamicData):
    @property
    def deviceClass(self) -> vim.ElementDescription: ...
    @deviceClass.setter
    def deviceClass(self, value: vim.ElementDescription):
        self._deviceClass = value
    @property
    def vendorName(self) -> str: ...
    @vendorName.setter
    def vendorName(self, value: str):
        self._vendorName = value
    @property
    def sriovNic(self) -> bool: ...
    @sriovNic.setter
    def sriovNic(self, value: bool):
        self._sriovNic = value
    @property
    def configParams(self) -> List[vim.option.OptionDef]: ...
    @configParams.setter
    def configParams(self, value: List[vim.option.OptionDef]):
        self._configParams = value


class DynamicPassthroughInfo(TargetInfo):
    @property
    def vendorName(self) -> str: ...
    @vendorName.setter
    def vendorName(self, value: str):
        self._vendorName = value
    @property
    def deviceName(self) -> str: ...
    @deviceName.setter
    def deviceName(self, value: str):
        self._deviceName = value
    @property
    def customLabel(self) -> str: ...
    @customLabel.setter
    def customLabel(self, value: str):
        self._customLabel = value
    @property
    def vendorId(self) -> int: ...
    @vendorId.setter
    def vendorId(self, value: int):
        self._vendorId = value
    @property
    def deviceId(self) -> int: ...
    @deviceId.setter
    def deviceId(self, value: int):
        self._deviceId = value


class EmptyIndependentFilterSpec(BaseIndependentFilterSpec): ...


class EmptyProfileSpec(ProfileSpec): ...


class FaultToleranceConfigInfo(vmodl.DynamicData):
    @property
    def role(self) -> int: ...
    @role.setter
    def role(self, value: int):
        self._role = value
    @property
    def instanceUuids(self) -> List[str]: ...
    @instanceUuids.setter
    def instanceUuids(self, value: List[str]):
        self._instanceUuids = value
    @property
    def configPaths(self) -> List[str]: ...
    @configPaths.setter
    def configPaths(self, value: List[str]):
        self._configPaths = value
    @property
    def orphaned(self) -> bool: ...
    @orphaned.setter
    def orphaned(self, value: bool):
        self._orphaned = value


class FaultToleranceConfigSpec(vmodl.DynamicData):
    @property
    def metaDataPath(self) -> FaultToleranceMetaSpec: ...
    @metaDataPath.setter
    def metaDataPath(self, value: FaultToleranceMetaSpec):
        self._metaDataPath = value
    @property
    def secondaryVmSpec(self) -> FaultToleranceVMConfigSpec: ...
    @secondaryVmSpec.setter
    def secondaryVmSpec(self, value: FaultToleranceVMConfigSpec):
        self._secondaryVmSpec = value


class FaultToleranceMetaSpec(vmodl.DynamicData):
    @property
    def metaDataDatastore(self) -> vim.Datastore: ...
    @metaDataDatastore.setter
    def metaDataDatastore(self, value: vim.Datastore):
        self._metaDataDatastore = value


class FaultTolerancePrimaryConfigInfo(FaultToleranceConfigInfo):
    @property
    def secondaries(self) -> List[vim.VirtualMachine]: ...
    @secondaries.setter
    def secondaries(self, value: List[vim.VirtualMachine]):
        self._secondaries = value


class FaultToleranceSecondaryConfigInfo(FaultToleranceConfigInfo):
    @property
    def primaryVM(self) -> vim.VirtualMachine: ...
    @primaryVM.setter
    def primaryVM(self, value: vim.VirtualMachine):
        self._primaryVM = value


class FaultToleranceSecondaryOpResult(vmodl.DynamicData):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def powerOnAttempted(self) -> bool: ...
    @powerOnAttempted.setter
    def powerOnAttempted(self, value: bool):
        self._powerOnAttempted = value
    @property
    def powerOnResult(self) -> vim.cluster.PowerOnVmResult: ...
    @powerOnResult.setter
    def powerOnResult(self, value: vim.cluster.PowerOnVmResult):
        self._powerOnResult = value


class FaultToleranceVMConfigSpec(vmodl.DynamicData):
    @property
    def vmConfig(self) -> vim.Datastore: ...
    @vmConfig.setter
    def vmConfig(self, value: vim.Datastore):
        self._vmConfig = value
    @property
    def disks(self) -> List[FaultToleranceVMConfigSpec.FaultToleranceDiskSpec]: ...
    @disks.setter
    def disks(self, value: List[FaultToleranceVMConfigSpec.FaultToleranceDiskSpec]):
        self._disks = value


    class FaultToleranceDiskSpec(vmodl.DynamicData):
        @property
        def disk(self) -> vim.vm.device.VirtualDevice: ...
        @disk.setter
        def disk(self, value: vim.vm.device.VirtualDevice):
            self._disk = value
        @property
        def datastore(self) -> vim.Datastore: ...
        @datastore.setter
        def datastore(self, value: vim.Datastore):
            self._datastore = value


class FeatureRequirement(vmodl.DynamicData):
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


class FileInfo(vmodl.DynamicData):
    @property
    def vmPathName(self) -> str: ...
    @vmPathName.setter
    def vmPathName(self, value: str):
        self._vmPathName = value
    @property
    def snapshotDirectory(self) -> str: ...
    @snapshotDirectory.setter
    def snapshotDirectory(self, value: str):
        self._snapshotDirectory = value
    @property
    def suspendDirectory(self) -> str: ...
    @suspendDirectory.setter
    def suspendDirectory(self, value: str):
        self._suspendDirectory = value
    @property
    def logDirectory(self) -> str: ...
    @logDirectory.setter
    def logDirectory(self, value: str):
        self._logDirectory = value
    @property
    def ftMetadataDirectory(self) -> str: ...
    @ftMetadataDirectory.setter
    def ftMetadataDirectory(self, value: str):
        self._ftMetadataDirectory = value


class FileLayout(vmodl.DynamicData):
    @property
    def configFile(self) -> List[str]: ...
    @configFile.setter
    def configFile(self, value: List[str]):
        self._configFile = value
    @property
    def logFile(self) -> List[str]: ...
    @logFile.setter
    def logFile(self, value: List[str]):
        self._logFile = value
    @property
    def disk(self) -> List[FileLayout.DiskLayout]: ...
    @disk.setter
    def disk(self, value: List[FileLayout.DiskLayout]):
        self._disk = value
    @property
    def snapshot(self) -> List[FileLayout.SnapshotLayout]: ...
    @snapshot.setter
    def snapshot(self, value: List[FileLayout.SnapshotLayout]):
        self._snapshot = value
    @property
    def swapFile(self) -> str: ...
    @swapFile.setter
    def swapFile(self, value: str):
        self._swapFile = value


    class DiskLayout(vmodl.DynamicData):
        @property
        def key(self) -> int: ...
        @key.setter
        def key(self, value: int):
            self._key = value
        @property
        def diskFile(self) -> List[str]: ...
        @diskFile.setter
        def diskFile(self, value: List[str]):
            self._diskFile = value


    class SnapshotLayout(vmodl.DynamicData):
        @property
        def key(self) -> Snapshot: ...
        @key.setter
        def key(self, value: Snapshot):
            self._key = value
        @property
        def snapshotFile(self) -> List[str]: ...
        @snapshotFile.setter
        def snapshotFile(self, value: List[str]):
            self._snapshotFile = value


class FileLayoutEx(vmodl.DynamicData):
    @property
    def file(self) -> List[FileLayoutEx.FileInfo]: ...
    @file.setter
    def file(self, value: List[FileLayoutEx.FileInfo]):
        self._file = value
    @property
    def disk(self) -> List[FileLayoutEx.DiskLayout]: ...
    @disk.setter
    def disk(self, value: List[FileLayoutEx.DiskLayout]):
        self._disk = value
    @property
    def snapshot(self) -> List[FileLayoutEx.SnapshotLayout]: ...
    @snapshot.setter
    def snapshot(self, value: List[FileLayoutEx.SnapshotLayout]):
        self._snapshot = value
    @property
    def timestamp(self) -> datetime: ...
    @timestamp.setter
    def timestamp(self, value: datetime):
        self._timestamp = value


    class DiskLayout(vmodl.DynamicData):
        @property
        def key(self) -> int: ...
        @key.setter
        def key(self, value: int):
            self._key = value
        @property
        def chain(self) -> List[FileLayoutEx.DiskUnit]: ...
        @chain.setter
        def chain(self, value: List[FileLayoutEx.DiskUnit]):
            self._chain = value


    class DiskUnit(vmodl.DynamicData):
        @property
        def fileKey(self) -> List[int]: ...
        @fileKey.setter
        def fileKey(self, value: List[int]):
            self._fileKey = value


    class FileInfo(vmodl.DynamicData):
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
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def size(self) -> long: ...
        @size.setter
        def size(self, value: long):
            self._size = value
        @property
        def uniqueSize(self) -> long: ...
        @uniqueSize.setter
        def uniqueSize(self, value: long):
            self._uniqueSize = value
        @property
        def backingObjectId(self) -> str: ...
        @backingObjectId.setter
        def backingObjectId(self, value: str):
            self._backingObjectId = value
        @property
        def accessible(self) -> bool: ...
        @accessible.setter
        def accessible(self, value: bool):
            self._accessible = value


    class SnapshotLayout(vmodl.DynamicData):
        @property
        def key(self) -> Snapshot: ...
        @key.setter
        def key(self, value: Snapshot):
            self._key = value
        @property
        def dataKey(self) -> int: ...
        @dataKey.setter
        def dataKey(self, value: int):
            self._dataKey = value
        @property
        def memoryKey(self) -> int: ...
        @memoryKey.setter
        def memoryKey(self, value: int):
            self._memoryKey = value
        @property
        def disk(self) -> List[FileLayoutEx.DiskLayout]: ...
        @disk.setter
        def disk(self, value: List[FileLayoutEx.DiskLayout]):
            self._disk = value


    class FileType(Enum):
        config = "config"
        extendedConfig = "extendedConfig"
        diskDescriptor = "diskDescriptor"
        diskExtent = "diskExtent"
        digestDescriptor = "digestDescriptor"
        digestExtent = "digestExtent"
        diskReplicationState = "diskReplicationState"
        log = "log"
        stat = "stat"
        namespaceData = "namespaceData"
        dataSetsDiskModeStore = "dataSetsDiskModeStore"
        dataSetsVmModeStore = "dataSetsVmModeStore"
        nvram = "nvram"
        snapshotData = "snapshotData"
        snapshotMemory = "snapshotMemory"
        snapshotList = "snapshotList"
        snapshotManifestList = "snapshotManifestList"
        suspend = "suspend"
        suspendMemory = "suspendMemory"
        swap = "swap"
        uwswap = "uwswap"
        core = "core"
        screenshot = "screenshot"
        ftMetadata = "ftMetadata"
        guestCustomization = "guestCustomization"


class FlagInfo(vmodl.DynamicData):
    @property
    def disableAcceleration(self) -> bool: ...
    @disableAcceleration.setter
    def disableAcceleration(self, value: bool):
        self._disableAcceleration = value
    @property
    def enableLogging(self) -> bool: ...
    @enableLogging.setter
    def enableLogging(self, value: bool):
        self._enableLogging = value
    @property
    def useToe(self) -> bool: ...
    @useToe.setter
    def useToe(self, value: bool):
        self._useToe = value
    @property
    def runWithDebugInfo(self) -> bool: ...
    @runWithDebugInfo.setter
    def runWithDebugInfo(self, value: bool):
        self._runWithDebugInfo = value
    @property
    def monitorType(self) -> str: ...
    @monitorType.setter
    def monitorType(self, value: str):
        self._monitorType = value
    @property
    def htSharing(self) -> str: ...
    @htSharing.setter
    def htSharing(self, value: str):
        self._htSharing = value
    @property
    def snapshotDisabled(self) -> bool: ...
    @snapshotDisabled.setter
    def snapshotDisabled(self, value: bool):
        self._snapshotDisabled = value
    @property
    def snapshotLocked(self) -> bool: ...
    @snapshotLocked.setter
    def snapshotLocked(self, value: bool):
        self._snapshotLocked = value
    @property
    def diskUuidEnabled(self) -> bool: ...
    @diskUuidEnabled.setter
    def diskUuidEnabled(self, value: bool):
        self._diskUuidEnabled = value
    @property
    def virtualMmuUsage(self) -> str: ...
    @virtualMmuUsage.setter
    def virtualMmuUsage(self, value: str):
        self._virtualMmuUsage = value
    @property
    def virtualExecUsage(self) -> str: ...
    @virtualExecUsage.setter
    def virtualExecUsage(self, value: str):
        self._virtualExecUsage = value
    @property
    def snapshotPowerOffBehavior(self) -> str: ...
    @snapshotPowerOffBehavior.setter
    def snapshotPowerOffBehavior(self, value: str):
        self._snapshotPowerOffBehavior = value
    @property
    def recordReplayEnabled(self) -> bool: ...
    @recordReplayEnabled.setter
    def recordReplayEnabled(self, value: bool):
        self._recordReplayEnabled = value
    @property
    def faultToleranceType(self) -> str: ...
    @faultToleranceType.setter
    def faultToleranceType(self, value: str):
        self._faultToleranceType = value
    @property
    def cbrcCacheEnabled(self) -> bool: ...
    @cbrcCacheEnabled.setter
    def cbrcCacheEnabled(self, value: bool):
        self._cbrcCacheEnabled = value
    @property
    def vvtdEnabled(self) -> bool: ...
    @vvtdEnabled.setter
    def vvtdEnabled(self, value: bool):
        self._vvtdEnabled = value
    @property
    def vbsEnabled(self) -> bool: ...
    @vbsEnabled.setter
    def vbsEnabled(self, value: bool):
        self._vbsEnabled = value


    class HtSharing(Enum):
        any = "any"
        none = "none"
        internal = "internal"


    class MonitorType(Enum):
        release = "release"
        debug = "debug"
        stats = "stats"


    class PowerOffBehavior(Enum):
        powerOff = "powerOff"
        revert = "revert"
        prompt = "prompt"
        take = "take"


    class VirtualExecUsage(Enum):
        hvAuto = "hvAuto"
        hvOn = "hvOn"
        hvOff = "hvOff"


    class VirtualMmuUsage(Enum):
        automatic = "automatic"
        on = "on"
        off = "off"


class FloppyInfo(TargetInfo): ...


class ForkConfigInfo(vmodl.DynamicData):
    @property
    def parentEnabled(self) -> bool: ...
    @parentEnabled.setter
    def parentEnabled(self, value: bool):
        self._parentEnabled = value
    @property
    def childForkGroupId(self) -> str: ...
    @childForkGroupId.setter
    def childForkGroupId(self, value: str):
        self._childForkGroupId = value
    @property
    def parentForkGroupId(self) -> str: ...
    @parentForkGroupId.setter
    def parentForkGroupId(self, value: str):
        self._parentForkGroupId = value
    @property
    def childType(self) -> str: ...
    @childType.setter
    def childType(self, value: str):
        self._childType = value


    class ChildType(Enum):
        none = "none"
        persistent = "persistent"
        nonpersistent = "nonpersistent"


class GuestInfo(vmodl.DynamicData):
    @property
    def toolsStatus(self) -> GuestInfo.ToolsStatus | Literal['toolsNotInstalled', 'toolsNotRunning', 'toolsOld', 'toolsOk']: ...
    @toolsStatus.setter
    def toolsStatus(self, value: GuestInfo.ToolsStatus | Literal['toolsNotInstalled', 'toolsNotRunning', 'toolsOld', 'toolsOk']):
        self._toolsStatus = value
    @property
    def toolsVersionStatus(self) -> str: ...
    @toolsVersionStatus.setter
    def toolsVersionStatus(self, value: str):
        self._toolsVersionStatus = value
    @property
    def toolsVersionStatus2(self) -> str: ...
    @toolsVersionStatus2.setter
    def toolsVersionStatus2(self, value: str):
        self._toolsVersionStatus2 = value
    @property
    def toolsRunningStatus(self) -> str: ...
    @toolsRunningStatus.setter
    def toolsRunningStatus(self, value: str):
        self._toolsRunningStatus = value
    @property
    def toolsVersion(self) -> str: ...
    @toolsVersion.setter
    def toolsVersion(self, value: str):
        self._toolsVersion = value
    @property
    def toolsInstallType(self) -> str: ...
    @toolsInstallType.setter
    def toolsInstallType(self, value: str):
        self._toolsInstallType = value
    @property
    def guestId(self) -> str: ...
    @guestId.setter
    def guestId(self, value: str):
        self._guestId = value
    @property
    def guestFamily(self) -> str: ...
    @guestFamily.setter
    def guestFamily(self, value: str):
        self._guestFamily = value
    @property
    def guestFullName(self) -> str: ...
    @guestFullName.setter
    def guestFullName(self, value: str):
        self._guestFullName = value
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def ipAddress(self) -> str: ...
    @ipAddress.setter
    def ipAddress(self, value: str):
        self._ipAddress = value
    @property
    def net(self) -> List[GuestInfo.NicInfo]: ...
    @net.setter
    def net(self, value: List[GuestInfo.NicInfo]):
        self._net = value
    @property
    def ipStack(self) -> List[GuestInfo.StackInfo]: ...
    @ipStack.setter
    def ipStack(self, value: List[GuestInfo.StackInfo]):
        self._ipStack = value
    @property
    def disk(self) -> List[GuestInfo.DiskInfo]: ...
    @disk.setter
    def disk(self, value: List[GuestInfo.DiskInfo]):
        self._disk = value
    @property
    def screen(self) -> GuestInfo.ScreenInfo: ...
    @screen.setter
    def screen(self, value: GuestInfo.ScreenInfo):
        self._screen = value
    @property
    def guestState(self) -> str: ...
    @guestState.setter
    def guestState(self, value: str):
        self._guestState = value
    @property
    def appHeartbeatStatus(self) -> str: ...
    @appHeartbeatStatus.setter
    def appHeartbeatStatus(self, value: str):
        self._appHeartbeatStatus = value
    @property
    def guestKernelCrashed(self) -> bool: ...
    @guestKernelCrashed.setter
    def guestKernelCrashed(self, value: bool):
        self._guestKernelCrashed = value
    @property
    def appState(self) -> str: ...
    @appState.setter
    def appState(self, value: str):
        self._appState = value
    @property
    def guestOperationsReady(self) -> bool: ...
    @guestOperationsReady.setter
    def guestOperationsReady(self, value: bool):
        self._guestOperationsReady = value
    @property
    def interactiveGuestOperationsReady(self) -> bool: ...
    @interactiveGuestOperationsReady.setter
    def interactiveGuestOperationsReady(self, value: bool):
        self._interactiveGuestOperationsReady = value
    @property
    def guestStateChangeSupported(self) -> bool: ...
    @guestStateChangeSupported.setter
    def guestStateChangeSupported(self, value: bool):
        self._guestStateChangeSupported = value
    @property
    def generationInfo(self) -> List[GuestInfo.NamespaceGenerationInfo]: ...
    @generationInfo.setter
    def generationInfo(self, value: List[GuestInfo.NamespaceGenerationInfo]):
        self._generationInfo = value
    @property
    def hwVersion(self) -> str: ...
    @hwVersion.setter
    def hwVersion(self, value: str):
        self._hwVersion = value
    @property
    def customizationInfo(self) -> GuestInfo.CustomizationInfo: ...
    @customizationInfo.setter
    def customizationInfo(self, value: GuestInfo.CustomizationInfo):
        self._customizationInfo = value


    class CustomizationInfo(vmodl.DynamicData):
        @property
        def customizationStatus(self) -> str: ...
        @customizationStatus.setter
        def customizationStatus(self, value: str):
            self._customizationStatus = value
        @property
        def startTime(self) -> datetime: ...
        @startTime.setter
        def startTime(self, value: datetime):
            self._startTime = value
        @property
        def endTime(self) -> datetime: ...
        @endTime.setter
        def endTime(self, value: datetime):
            self._endTime = value
        @property
        def errorMsg(self) -> str: ...
        @errorMsg.setter
        def errorMsg(self, value: str):
            self._errorMsg = value


    class DiskInfo(vmodl.DynamicData):
        @property
        def diskPath(self) -> str: ...
        @diskPath.setter
        def diskPath(self, value: str):
            self._diskPath = value
        @property
        def capacity(self) -> long: ...
        @capacity.setter
        def capacity(self, value: long):
            self._capacity = value
        @property
        def freeSpace(self) -> long: ...
        @freeSpace.setter
        def freeSpace(self, value: long):
            self._freeSpace = value
        @property
        def filesystemType(self) -> str: ...
        @filesystemType.setter
        def filesystemType(self, value: str):
            self._filesystemType = value
        @property
        def mappings(self) -> List[GuestInfo.VirtualDiskMapping]: ...
        @mappings.setter
        def mappings(self, value: List[GuestInfo.VirtualDiskMapping]):
            self._mappings = value


    class NamespaceGenerationInfo(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def generationNo(self) -> int: ...
        @generationNo.setter
        def generationNo(self, value: int):
            self._generationNo = value


    class NicInfo(vmodl.DynamicData):
        @property
        def network(self) -> str: ...
        @network.setter
        def network(self, value: str):
            self._network = value
        @property
        def ipAddress(self) -> List[str]: ...
        @ipAddress.setter
        def ipAddress(self, value: List[str]):
            self._ipAddress = value
        @property
        def macAddress(self) -> str: ...
        @macAddress.setter
        def macAddress(self, value: str):
            self._macAddress = value
        @property
        def connected(self) -> bool: ...
        @connected.setter
        def connected(self, value: bool):
            self._connected = value
        @property
        def deviceConfigId(self) -> int: ...
        @deviceConfigId.setter
        def deviceConfigId(self, value: int):
            self._deviceConfigId = value
        @property
        def dnsConfig(self) -> vim.net.DnsConfigInfo: ...
        @dnsConfig.setter
        def dnsConfig(self, value: vim.net.DnsConfigInfo):
            self._dnsConfig = value
        @property
        def ipConfig(self) -> vim.net.IpConfigInfo: ...
        @ipConfig.setter
        def ipConfig(self, value: vim.net.IpConfigInfo):
            self._ipConfig = value
        @property
        def netBIOSConfig(self) -> vim.net.NetBIOSConfigInfo: ...
        @netBIOSConfig.setter
        def netBIOSConfig(self, value: vim.net.NetBIOSConfigInfo):
            self._netBIOSConfig = value


    class ScreenInfo(vmodl.DynamicData):
        @property
        def width(self) -> int: ...
        @width.setter
        def width(self, value: int):
            self._width = value
        @property
        def height(self) -> int: ...
        @height.setter
        def height(self, value: int):
            self._height = value


    class StackInfo(vmodl.DynamicData):
        @property
        def dnsConfig(self) -> vim.net.DnsConfigInfo: ...
        @dnsConfig.setter
        def dnsConfig(self, value: vim.net.DnsConfigInfo):
            self._dnsConfig = value
        @property
        def ipRouteConfig(self) -> vim.net.IpRouteConfigInfo: ...
        @ipRouteConfig.setter
        def ipRouteConfig(self, value: vim.net.IpRouteConfigInfo):
            self._ipRouteConfig = value
        @property
        def ipStackConfig(self) -> List[vim.KeyValue]: ...
        @ipStackConfig.setter
        def ipStackConfig(self, value: List[vim.KeyValue]):
            self._ipStackConfig = value
        @property
        def dhcpConfig(self) -> vim.net.DhcpConfigInfo: ...
        @dhcpConfig.setter
        def dhcpConfig(self, value: vim.net.DhcpConfigInfo):
            self._dhcpConfig = value


    class VirtualDiskMapping(vmodl.DynamicData):
        @property
        def key(self) -> int: ...
        @key.setter
        def key(self, value: int):
            self._key = value


    class AppStateType(Enum):
        none = "none"
        appStateOk = "appStateOk"
        appStateNeedReset = "appStateNeedReset"


    class CustomizationStatus(Enum):
        TOOLSDEPLOYPKG_IDLE = "TOOLSDEPLOYPKG_IDLE"
        TOOLSDEPLOYPKG_PENDING = "TOOLSDEPLOYPKG_PENDING"
        TOOLSDEPLOYPKG_RUNNING = "TOOLSDEPLOYPKG_RUNNING"
        TOOLSDEPLOYPKG_SUCCEEDED = "TOOLSDEPLOYPKG_SUCCEEDED"
        TOOLSDEPLOYPKG_FAILED = "TOOLSDEPLOYPKG_FAILED"


    class GuestState(Enum):
        running = "running"
        shuttingDown = "shuttingDown"
        resetting = "resetting"
        standby = "standby"
        notRunning = "notRunning"
        unknown = "unknown"


    class ToolsInstallType(Enum):
        guestToolsTypeUnknown = "guestToolsTypeUnknown"
        guestToolsTypeMSI = "guestToolsTypeMSI"
        guestToolsTypeTar = "guestToolsTypeTar"
        guestToolsTypeOSP = "guestToolsTypeOSP"
        guestToolsTypeOpenVMTools = "guestToolsTypeOpenVMTools"


    class ToolsRunningStatus(Enum):
        guestToolsNotRunning = "guestToolsNotRunning"
        guestToolsRunning = "guestToolsRunning"
        guestToolsExecutingScripts = "guestToolsExecutingScripts"


    class ToolsStatus(Enum):
        toolsNotInstalled = "toolsNotInstalled"
        toolsNotRunning = "toolsNotRunning"
        toolsOld = "toolsOld"
        toolsOk = "toolsOk"


    class ToolsVersionStatus(Enum):
        guestToolsNotInstalled = "guestToolsNotInstalled"
        guestToolsNeedUpgrade = "guestToolsNeedUpgrade"
        guestToolsCurrent = "guestToolsCurrent"
        guestToolsUnmanaged = "guestToolsUnmanaged"
        guestToolsTooOld = "guestToolsTooOld"
        guestToolsSupportedOld = "guestToolsSupportedOld"
        guestToolsSupportedNew = "guestToolsSupportedNew"
        guestToolsTooNew = "guestToolsTooNew"
        guestToolsBlacklisted = "guestToolsBlacklisted"


class GuestIntegrityInfo(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value


class GuestMonitoringModeInfo(vmodl.DynamicData):
    @property
    def gmmFile(self) -> str: ...
    @gmmFile.setter
    def gmmFile(self, value: str):
        self._gmmFile = value
    @property
    def gmmAppliance(self) -> str: ...
    @gmmAppliance.setter
    def gmmAppliance(self, value: str):
        self._gmmAppliance = value


class GuestOsDescriptor(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def family(self) -> str: ...
    @family.setter
    def family(self, value: str):
        self._family = value
    @property
    def fullName(self) -> str: ...
    @fullName.setter
    def fullName(self, value: str):
        self._fullName = value
    @property
    def supportedMaxCPUs(self) -> int: ...
    @supportedMaxCPUs.setter
    def supportedMaxCPUs(self, value: int):
        self._supportedMaxCPUs = value
    @property
    def numSupportedPhysicalSockets(self) -> int: ...
    @numSupportedPhysicalSockets.setter
    def numSupportedPhysicalSockets(self, value: int):
        self._numSupportedPhysicalSockets = value
    @property
    def numSupportedCoresPerSocket(self) -> int: ...
    @numSupportedCoresPerSocket.setter
    def numSupportedCoresPerSocket(self, value: int):
        self._numSupportedCoresPerSocket = value
    @property
    def supportedMinMemMB(self) -> int: ...
    @supportedMinMemMB.setter
    def supportedMinMemMB(self, value: int):
        self._supportedMinMemMB = value
    @property
    def supportedMaxMemMB(self) -> int: ...
    @supportedMaxMemMB.setter
    def supportedMaxMemMB(self, value: int):
        self._supportedMaxMemMB = value
    @property
    def recommendedMemMB(self) -> int: ...
    @recommendedMemMB.setter
    def recommendedMemMB(self, value: int):
        self._recommendedMemMB = value
    @property
    def recommendedColorDepth(self) -> int: ...
    @recommendedColorDepth.setter
    def recommendedColorDepth(self, value: int):
        self._recommendedColorDepth = value
    @property
    def supportedDiskControllerList(self) -> List[type]: ...
    @supportedDiskControllerList.setter
    def supportedDiskControllerList(self, value: List[type]):
        self._supportedDiskControllerList = value
    @property
    def recommendedSCSIController(self) -> type: ...
    @recommendedSCSIController.setter
    def recommendedSCSIController(self, value: type):
        self._recommendedSCSIController = value
    @property
    def recommendedDiskController(self) -> type: ...
    @recommendedDiskController.setter
    def recommendedDiskController(self, value: type):
        self._recommendedDiskController = value
    @property
    def supportedNumDisks(self) -> int: ...
    @supportedNumDisks.setter
    def supportedNumDisks(self, value: int):
        self._supportedNumDisks = value
    @property
    def recommendedDiskSizeMB(self) -> int: ...
    @recommendedDiskSizeMB.setter
    def recommendedDiskSizeMB(self, value: int):
        self._recommendedDiskSizeMB = value
    @property
    def recommendedCdromController(self) -> type: ...
    @recommendedCdromController.setter
    def recommendedCdromController(self, value: type):
        self._recommendedCdromController = value
    @property
    def supportedEthernetCard(self) -> List[type]: ...
    @supportedEthernetCard.setter
    def supportedEthernetCard(self, value: List[type]):
        self._supportedEthernetCard = value
    @property
    def recommendedEthernetCard(self) -> type: ...
    @recommendedEthernetCard.setter
    def recommendedEthernetCard(self, value: type):
        self._recommendedEthernetCard = value
    @property
    def supportsSlaveDisk(self) -> bool: ...
    @supportsSlaveDisk.setter
    def supportsSlaveDisk(self, value: bool):
        self._supportsSlaveDisk = value
    @property
    def cpuFeatureMask(self) -> List[vim.host.CpuIdInfo]: ...
    @cpuFeatureMask.setter
    def cpuFeatureMask(self, value: List[vim.host.CpuIdInfo]):
        self._cpuFeatureMask = value
    @property
    def smcRequired(self) -> bool: ...
    @smcRequired.setter
    def smcRequired(self, value: bool):
        self._smcRequired = value
    @property
    def supportsWakeOnLan(self) -> bool: ...
    @supportsWakeOnLan.setter
    def supportsWakeOnLan(self, value: bool):
        self._supportsWakeOnLan = value
    @property
    def supportsVMI(self) -> bool: ...
    @supportsVMI.setter
    def supportsVMI(self, value: bool):
        self._supportsVMI = value
    @property
    def supportsMemoryHotAdd(self) -> bool: ...
    @supportsMemoryHotAdd.setter
    def supportsMemoryHotAdd(self, value: bool):
        self._supportsMemoryHotAdd = value
    @property
    def supportsCpuHotAdd(self) -> bool: ...
    @supportsCpuHotAdd.setter
    def supportsCpuHotAdd(self, value: bool):
        self._supportsCpuHotAdd = value
    @property
    def supportsCpuHotRemove(self) -> bool: ...
    @supportsCpuHotRemove.setter
    def supportsCpuHotRemove(self, value: bool):
        self._supportsCpuHotRemove = value
    @property
    def supportedFirmware(self) -> List[str]: ...
    @supportedFirmware.setter
    def supportedFirmware(self, value: List[str]):
        self._supportedFirmware = value
    @property
    def recommendedFirmware(self) -> str: ...
    @recommendedFirmware.setter
    def recommendedFirmware(self, value: str):
        self._recommendedFirmware = value
    @property
    def supportedUSBControllerList(self) -> List[type]: ...
    @supportedUSBControllerList.setter
    def supportedUSBControllerList(self, value: List[type]):
        self._supportedUSBControllerList = value
    @property
    def recommendedUSBController(self) -> type: ...
    @recommendedUSBController.setter
    def recommendedUSBController(self, value: type):
        self._recommendedUSBController = value
    @property
    def supports3D(self) -> bool: ...
    @supports3D.setter
    def supports3D(self, value: bool):
        self._supports3D = value
    @property
    def recommended3D(self) -> bool: ...
    @recommended3D.setter
    def recommended3D(self, value: bool):
        self._recommended3D = value
    @property
    def smcRecommended(self) -> bool: ...
    @smcRecommended.setter
    def smcRecommended(self, value: bool):
        self._smcRecommended = value
    @property
    def ich7mRecommended(self) -> bool: ...
    @ich7mRecommended.setter
    def ich7mRecommended(self, value: bool):
        self._ich7mRecommended = value
    @property
    def usbRecommended(self) -> bool: ...
    @usbRecommended.setter
    def usbRecommended(self, value: bool):
        self._usbRecommended = value
    @property
    def supportLevel(self) -> str: ...
    @supportLevel.setter
    def supportLevel(self, value: str):
        self._supportLevel = value
    @property
    def supportedForCreate(self) -> bool: ...
    @supportedForCreate.setter
    def supportedForCreate(self, value: bool):
        self._supportedForCreate = value
    @property
    def vRAMSizeInKB(self) -> vim.option.IntOption: ...
    @vRAMSizeInKB.setter
    def vRAMSizeInKB(self, value: vim.option.IntOption):
        self._vRAMSizeInKB = value
    @property
    def numSupportedFloppyDevices(self) -> int: ...
    @numSupportedFloppyDevices.setter
    def numSupportedFloppyDevices(self, value: int):
        self._numSupportedFloppyDevices = value
    @property
    def wakeOnLanEthernetCard(self) -> List[type]: ...
    @wakeOnLanEthernetCard.setter
    def wakeOnLanEthernetCard(self, value: List[type]):
        self._wakeOnLanEthernetCard = value
    @property
    def supportsPvscsiControllerForBoot(self) -> bool: ...
    @supportsPvscsiControllerForBoot.setter
    def supportsPvscsiControllerForBoot(self, value: bool):
        self._supportsPvscsiControllerForBoot = value
    @property
    def diskUuidEnabled(self) -> bool: ...
    @diskUuidEnabled.setter
    def diskUuidEnabled(self, value: bool):
        self._diskUuidEnabled = value
    @property
    def supportsHotPlugPCI(self) -> bool: ...
    @supportsHotPlugPCI.setter
    def supportsHotPlugPCI(self, value: bool):
        self._supportsHotPlugPCI = value
    @property
    def supportsSecureBoot(self) -> bool: ...
    @supportsSecureBoot.setter
    def supportsSecureBoot(self, value: bool):
        self._supportsSecureBoot = value
    @property
    def defaultSecureBoot(self) -> bool: ...
    @defaultSecureBoot.setter
    def defaultSecureBoot(self, value: bool):
        self._defaultSecureBoot = value
    @property
    def persistentMemorySupported(self) -> bool: ...
    @persistentMemorySupported.setter
    def persistentMemorySupported(self, value: bool):
        self._persistentMemorySupported = value
    @property
    def supportedMinPersistentMemoryMB(self) -> long: ...
    @supportedMinPersistentMemoryMB.setter
    def supportedMinPersistentMemoryMB(self, value: long):
        self._supportedMinPersistentMemoryMB = value
    @property
    def supportedMaxPersistentMemoryMB(self) -> long: ...
    @supportedMaxPersistentMemoryMB.setter
    def supportedMaxPersistentMemoryMB(self, value: long):
        self._supportedMaxPersistentMemoryMB = value
    @property
    def recommendedPersistentMemoryMB(self) -> long: ...
    @recommendedPersistentMemoryMB.setter
    def recommendedPersistentMemoryMB(self, value: long):
        self._recommendedPersistentMemoryMB = value
    @property
    def persistentMemoryHotAddSupported(self) -> bool: ...
    @persistentMemoryHotAddSupported.setter
    def persistentMemoryHotAddSupported(self, value: bool):
        self._persistentMemoryHotAddSupported = value
    @property
    def persistentMemoryHotRemoveSupported(self) -> bool: ...
    @persistentMemoryHotRemoveSupported.setter
    def persistentMemoryHotRemoveSupported(self, value: bool):
        self._persistentMemoryHotRemoveSupported = value
    @property
    def persistentMemoryColdGrowthSupported(self) -> bool: ...
    @persistentMemoryColdGrowthSupported.setter
    def persistentMemoryColdGrowthSupported(self, value: bool):
        self._persistentMemoryColdGrowthSupported = value
    @property
    def persistentMemoryColdGrowthGranularityMB(self) -> long: ...
    @persistentMemoryColdGrowthGranularityMB.setter
    def persistentMemoryColdGrowthGranularityMB(self, value: long):
        self._persistentMemoryColdGrowthGranularityMB = value
    @property
    def persistentMemoryHotGrowthSupported(self) -> bool: ...
    @persistentMemoryHotGrowthSupported.setter
    def persistentMemoryHotGrowthSupported(self, value: bool):
        self._persistentMemoryHotGrowthSupported = value
    @property
    def persistentMemoryHotGrowthGranularityMB(self) -> long: ...
    @persistentMemoryHotGrowthGranularityMB.setter
    def persistentMemoryHotGrowthGranularityMB(self, value: long):
        self._persistentMemoryHotGrowthGranularityMB = value
    @property
    def numRecommendedPhysicalSockets(self) -> int: ...
    @numRecommendedPhysicalSockets.setter
    def numRecommendedPhysicalSockets(self, value: int):
        self._numRecommendedPhysicalSockets = value
    @property
    def numRecommendedCoresPerSocket(self) -> int: ...
    @numRecommendedCoresPerSocket.setter
    def numRecommendedCoresPerSocket(self, value: int):
        self._numRecommendedCoresPerSocket = value
    @property
    def vvtdSupported(self) -> vim.option.BoolOption: ...
    @vvtdSupported.setter
    def vvtdSupported(self, value: vim.option.BoolOption):
        self._vvtdSupported = value
    @property
    def vbsSupported(self) -> vim.option.BoolOption: ...
    @vbsSupported.setter
    def vbsSupported(self, value: vim.option.BoolOption):
        self._vbsSupported = value
    @property
    def vsgxSupported(self) -> vim.option.BoolOption: ...
    @vsgxSupported.setter
    def vsgxSupported(self, value: vim.option.BoolOption):
        self._vsgxSupported = value
    @property
    def vsgxRemoteAttestationSupported(self) -> bool: ...
    @vsgxRemoteAttestationSupported.setter
    def vsgxRemoteAttestationSupported(self, value: bool):
        self._vsgxRemoteAttestationSupported = value
    @property
    def supportsTPM20(self) -> bool: ...
    @supportsTPM20.setter
    def supportsTPM20(self, value: bool):
        self._supportsTPM20 = value
    @property
    def recommendedTPM20(self) -> bool: ...
    @recommendedTPM20.setter
    def recommendedTPM20(self, value: bool):
        self._recommendedTPM20 = value
    @property
    def vwdtSupported(self) -> bool: ...
    @vwdtSupported.setter
    def vwdtSupported(self, value: bool):
        self._vwdtSupported = value


    class FirmwareType(Enum):
        bios = "bios"
        efi = "efi"
        csm = "csm"


    class GuestOsFamily(Enum):
        windowsGuest = "windowsGuest"
        linuxGuest = "linuxGuest"
        netwareGuest = "netwareGuest"
        solarisGuest = "solarisGuest"
        darwinGuestFamily = "darwinGuestFamily"
        otherGuestFamily = "otherGuestFamily"


    class GuestOsIdentifier(Enum):
        dosGuest = "dosGuest"
        win31Guest = "win31Guest"
        win95Guest = "win95Guest"
        win98Guest = "win98Guest"
        winMeGuest = "winMeGuest"
        winNTGuest = "winNTGuest"
        win2000ProGuest = "win2000ProGuest"
        win2000ServGuest = "win2000ServGuest"
        win2000AdvServGuest = "win2000AdvServGuest"
        winXPHomeGuest = "winXPHomeGuest"
        winXPProGuest = "winXPProGuest"
        winXPPro64Guest = "winXPPro64Guest"
        winNetWebGuest = "winNetWebGuest"
        winNetStandardGuest = "winNetStandardGuest"
        winNetEnterpriseGuest = "winNetEnterpriseGuest"
        winNetDatacenterGuest = "winNetDatacenterGuest"
        winNetBusinessGuest = "winNetBusinessGuest"
        winNetStandard64Guest = "winNetStandard64Guest"
        winNetEnterprise64Guest = "winNetEnterprise64Guest"
        winLonghornGuest = "winLonghornGuest"
        winLonghorn64Guest = "winLonghorn64Guest"
        winNetDatacenter64Guest = "winNetDatacenter64Guest"
        winVistaGuest = "winVistaGuest"
        winVista64Guest = "winVista64Guest"
        windows7Guest = "windows7Guest"
        windows7_64Guest = "windows7_64Guest"
        windows7Server64Guest = "windows7Server64Guest"
        windows8Guest = "windows8Guest"
        windows8_64Guest = "windows8_64Guest"
        windows8Server64Guest = "windows8Server64Guest"
        windows9Guest = "windows9Guest"
        windows9_64Guest = "windows9_64Guest"
        windows9Server64Guest = "windows9Server64Guest"
        windows11_64Guest = "windows11_64Guest"
        windows12_64Guest = "windows12_64Guest"
        windowsHyperVGuest = "windowsHyperVGuest"
        windows2019srv_64Guest = "windows2019srv_64Guest"
        windows2019srvNext_64Guest = "windows2019srvNext_64Guest"
        windows2022srvNext_64Guest = "windows2022srvNext_64Guest"
        freebsdGuest = "freebsdGuest"
        freebsd64Guest = "freebsd64Guest"
        freebsd11Guest = "freebsd11Guest"
        freebsd11_64Guest = "freebsd11_64Guest"
        freebsd12Guest = "freebsd12Guest"
        freebsd12_64Guest = "freebsd12_64Guest"
        freebsd13Guest = "freebsd13Guest"
        freebsd13_64Guest = "freebsd13_64Guest"
        freebsd14Guest = "freebsd14Guest"
        freebsd14_64Guest = "freebsd14_64Guest"
        redhatGuest = "redhatGuest"
        rhel2Guest = "rhel2Guest"
        rhel3Guest = "rhel3Guest"
        rhel3_64Guest = "rhel3_64Guest"
        rhel4Guest = "rhel4Guest"
        rhel4_64Guest = "rhel4_64Guest"
        rhel5Guest = "rhel5Guest"
        rhel5_64Guest = "rhel5_64Guest"
        rhel6Guest = "rhel6Guest"
        rhel6_64Guest = "rhel6_64Guest"
        rhel7Guest = "rhel7Guest"
        rhel7_64Guest = "rhel7_64Guest"
        rhel8_64Guest = "rhel8_64Guest"
        rhel9_64Guest = "rhel9_64Guest"
        centosGuest = "centosGuest"
        centos64Guest = "centos64Guest"
        centos6Guest = "centos6Guest"
        centos6_64Guest = "centos6_64Guest"
        centos7Guest = "centos7Guest"
        centos7_64Guest = "centos7_64Guest"
        centos8_64Guest = "centos8_64Guest"
        centos9_64Guest = "centos9_64Guest"
        oracleLinuxGuest = "oracleLinuxGuest"
        oracleLinux64Guest = "oracleLinux64Guest"
        oracleLinux6Guest = "oracleLinux6Guest"
        oracleLinux6_64Guest = "oracleLinux6_64Guest"
        oracleLinux7Guest = "oracleLinux7Guest"
        oracleLinux7_64Guest = "oracleLinux7_64Guest"
        oracleLinux8_64Guest = "oracleLinux8_64Guest"
        oracleLinux9_64Guest = "oracleLinux9_64Guest"
        suseGuest = "suseGuest"
        suse64Guest = "suse64Guest"
        slesGuest = "slesGuest"
        sles64Guest = "sles64Guest"
        sles10Guest = "sles10Guest"
        sles10_64Guest = "sles10_64Guest"
        sles11Guest = "sles11Guest"
        sles11_64Guest = "sles11_64Guest"
        sles12Guest = "sles12Guest"
        sles12_64Guest = "sles12_64Guest"
        sles15_64Guest = "sles15_64Guest"
        sles16_64Guest = "sles16_64Guest"
        nld9Guest = "nld9Guest"
        oesGuest = "oesGuest"
        sjdsGuest = "sjdsGuest"
        mandrakeGuest = "mandrakeGuest"
        mandrivaGuest = "mandrivaGuest"
        mandriva64Guest = "mandriva64Guest"
        turboLinuxGuest = "turboLinuxGuest"
        turboLinux64Guest = "turboLinux64Guest"
        ubuntuGuest = "ubuntuGuest"
        ubuntu64Guest = "ubuntu64Guest"
        debian4Guest = "debian4Guest"
        debian4_64Guest = "debian4_64Guest"
        debian5Guest = "debian5Guest"
        debian5_64Guest = "debian5_64Guest"
        debian6Guest = "debian6Guest"
        debian6_64Guest = "debian6_64Guest"
        debian7Guest = "debian7Guest"
        debian7_64Guest = "debian7_64Guest"
        debian8Guest = "debian8Guest"
        debian8_64Guest = "debian8_64Guest"
        debian9Guest = "debian9Guest"
        debian9_64Guest = "debian9_64Guest"
        debian10Guest = "debian10Guest"
        debian10_64Guest = "debian10_64Guest"
        debian11Guest = "debian11Guest"
        debian11_64Guest = "debian11_64Guest"
        debian12Guest = "debian12Guest"
        debian12_64Guest = "debian12_64Guest"
        asianux3Guest = "asianux3Guest"
        asianux3_64Guest = "asianux3_64Guest"
        asianux4Guest = "asianux4Guest"
        asianux4_64Guest = "asianux4_64Guest"
        asianux5_64Guest = "asianux5_64Guest"
        asianux7_64Guest = "asianux7_64Guest"
        asianux8_64Guest = "asianux8_64Guest"
        asianux9_64Guest = "asianux9_64Guest"
        opensuseGuest = "opensuseGuest"
        opensuse64Guest = "opensuse64Guest"
        fedoraGuest = "fedoraGuest"
        fedora64Guest = "fedora64Guest"
        coreos64Guest = "coreos64Guest"
        vmwarePhoton64Guest = "vmwarePhoton64Guest"
        other24xLinuxGuest = "other24xLinuxGuest"
        other26xLinuxGuest = "other26xLinuxGuest"
        otherLinuxGuest = "otherLinuxGuest"
        other3xLinuxGuest = "other3xLinuxGuest"
        other4xLinuxGuest = "other4xLinuxGuest"
        other5xLinuxGuest = "other5xLinuxGuest"
        other6xLinuxGuest = "other6xLinuxGuest"
        genericLinuxGuest = "genericLinuxGuest"
        other24xLinux64Guest = "other24xLinux64Guest"
        other26xLinux64Guest = "other26xLinux64Guest"
        other3xLinux64Guest = "other3xLinux64Guest"
        other4xLinux64Guest = "other4xLinux64Guest"
        other5xLinux64Guest = "other5xLinux64Guest"
        other6xLinux64Guest = "other6xLinux64Guest"
        otherLinux64Guest = "otherLinux64Guest"
        solaris6Guest = "solaris6Guest"
        solaris7Guest = "solaris7Guest"
        solaris8Guest = "solaris8Guest"
        solaris9Guest = "solaris9Guest"
        solaris10Guest = "solaris10Guest"
        solaris10_64Guest = "solaris10_64Guest"
        solaris11_64Guest = "solaris11_64Guest"
        os2Guest = "os2Guest"
        eComStationGuest = "eComStationGuest"
        eComStation2Guest = "eComStation2Guest"
        netware4Guest = "netware4Guest"
        netware5Guest = "netware5Guest"
        netware6Guest = "netware6Guest"
        openServer5Guest = "openServer5Guest"
        openServer6Guest = "openServer6Guest"
        unixWare7Guest = "unixWare7Guest"
        darwinGuest = "darwinGuest"
        darwin64Guest = "darwin64Guest"
        darwin10Guest = "darwin10Guest"
        darwin10_64Guest = "darwin10_64Guest"
        darwin11Guest = "darwin11Guest"
        darwin11_64Guest = "darwin11_64Guest"
        darwin12_64Guest = "darwin12_64Guest"
        darwin13_64Guest = "darwin13_64Guest"
        darwin14_64Guest = "darwin14_64Guest"
        darwin15_64Guest = "darwin15_64Guest"
        darwin16_64Guest = "darwin16_64Guest"
        darwin17_64Guest = "darwin17_64Guest"
        darwin18_64Guest = "darwin18_64Guest"
        darwin19_64Guest = "darwin19_64Guest"
        darwin20_64Guest = "darwin20_64Guest"
        darwin21_64Guest = "darwin21_64Guest"
        darwin22_64Guest = "darwin22_64Guest"
        darwin23_64Guest = "darwin23_64Guest"
        vmkernelGuest = "vmkernelGuest"
        vmkernel5Guest = "vmkernel5Guest"
        vmkernel6Guest = "vmkernel6Guest"
        vmkernel65Guest = "vmkernel65Guest"
        vmkernel7Guest = "vmkernel7Guest"
        vmkernel8Guest = "vmkernel8Guest"
        amazonlinux2_64Guest = "amazonlinux2_64Guest"
        amazonlinux3_64Guest = "amazonlinux3_64Guest"
        crxPod1Guest = "crxPod1Guest"
        rockylinux_64Guest = "rockylinux_64Guest"
        almalinux_64Guest = "almalinux_64Guest"
        otherGuest = "otherGuest"
        otherGuest64 = "otherGuest64"


    class SupportLevel(Enum):
        experimental = "experimental"
        legacy = "legacy"
        terminated = "terminated"
        supported = "supported"
        unsupported = "unsupported"
        deprecated = "deprecated"
        techPreview = "techPreview"


class GuestQuiesceSpec(vmodl.DynamicData):
    @property
    def timeout(self) -> int: ...
    @timeout.setter
    def timeout(self, value: int):
        self._timeout = value


class IdeDiskDeviceInfo(DiskDeviceInfo):
    @property
    def partitionTable(self) -> List[IdeDiskDeviceInfo.PartitionInfo]: ...
    @partitionTable.setter
    def partitionTable(self, value: List[IdeDiskDeviceInfo.PartitionInfo]):
        self._partitionTable = value


    class PartitionInfo(vmodl.DynamicData):
        @property
        def id(self) -> int: ...
        @id.setter
        def id(self, value: int):
            self._id = value
        @property
        def capacity(self) -> int: ...
        @capacity.setter
        def capacity(self, value: int):
            self._capacity = value


class IndependentFilterSpec(BaseIndependentFilterSpec):
    @property
    def filterName(self) -> str: ...
    @filterName.setter
    def filterName(self, value: str):
        self._filterName = value
    @property
    def filterClass(self) -> str: ...
    @filterClass.setter
    def filterClass(self, value: str):
        self._filterClass = value
    @property
    def filterCapabilities(self) -> List[vim.KeyValue]: ...
    @filterCapabilities.setter
    def filterCapabilities(self, value: List[vim.KeyValue]):
        self._filterCapabilities = value


class InstantCloneSpec(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def location(self) -> RelocateSpec: ...
    @location.setter
    def location(self, value: RelocateSpec):
        self._location = value
    @property
    def config(self) -> List[vim.option.OptionValue]: ...
    @config.setter
    def config(self, value: List[vim.option.OptionValue]):
        self._config = value
    @property
    def biosUuid(self) -> str: ...
    @biosUuid.setter
    def biosUuid(self, value: str):
        self._biosUuid = value


class LegacyNetworkSwitchInfo(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class Message(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def argument(self) -> List[object]: ...
    @argument.setter
    def argument(self, value: List[object]):
        self._argument = value
    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str):
        self._text = value


class MetadataManager():


    class VmMetadata(vmodl.DynamicData):
        @property
        def vmId(self) -> str: ...
        @vmId.setter
        def vmId(self, value: str):
            self._vmId = value
        @property
        def metadata(self) -> str: ...
        @metadata.setter
        def metadata(self, value: str):
            self._metadata = value


    class VmMetadataInput(vmodl.DynamicData):
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value
        @property
        def vmMetadata(self) -> MetadataManager.VmMetadata: ...
        @vmMetadata.setter
        def vmMetadata(self, value: MetadataManager.VmMetadata):
            self._vmMetadata = value


    class VmMetadataOwner(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value


        class Owner(Enum):
            ComVmwareVsphereHA = "ComVmwareVsphereHA"


    class VmMetadataResult(vmodl.DynamicData):
        @property
        def vmMetadata(self) -> MetadataManager.VmMetadata: ...
        @vmMetadata.setter
        def vmMetadata(self, value: MetadataManager.VmMetadata):
            self._vmMetadata = value
        @property
        def error(self) -> vmodl.MethodFault: ...
        @error.setter
        def error(self, value: vmodl.MethodFault):
            self._error = value


    class VmMetadataOp(Enum):
        Update = "Update"
        Remove = "Remove"


class NetworkInfo(TargetInfo):
    @property
    def network(self) -> vim.Network.Summary: ...
    @network.setter
    def network(self, value: vim.Network.Summary):
        self._network = value
    @property
    def vswitch(self) -> str: ...
    @vswitch.setter
    def vswitch(self, value: str):
        self._vswitch = value


class NetworkShaperInfo(vmodl.DynamicData):
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def peakBps(self) -> long: ...
    @peakBps.setter
    def peakBps(self, value: long):
        self._peakBps = value
    @property
    def averageBps(self) -> long: ...
    @averageBps.setter
    def averageBps(self, value: long):
        self._averageBps = value
    @property
    def burstSize(self) -> long: ...
    @burstSize.setter
    def burstSize(self, value: long):
        self._burstSize = value


class OpaqueNetworkInfo(TargetInfo):
    @property
    def network(self) -> vim.OpaqueNetwork.Summary: ...
    @network.setter
    def network(self, value: vim.OpaqueNetwork.Summary):
        self._network = value
    @property
    def networkReservationSupported(self) -> bool: ...
    @networkReservationSupported.setter
    def networkReservationSupported(self, value: bool):
        self._networkReservationSupported = value


class ParallelInfo(TargetInfo): ...


class PciPassthroughInfo(TargetInfo):
    @property
    def pciDevice(self) -> vim.host.PciDevice: ...
    @pciDevice.setter
    def pciDevice(self, value: vim.host.PciDevice):
        self._pciDevice = value
    @property
    def systemId(self) -> str: ...
    @systemId.setter
    def systemId(self, value: str):
        self._systemId = value


class PciSharedGpuPassthroughInfo(TargetInfo):
    @property
    def vgpu(self) -> str: ...
    @vgpu.setter
    def vgpu(self, value: str):
        self._vgpu = value


class PrecisionClockInfo(TargetInfo):
    @property
    def systemClockProtocol(self) -> str: ...
    @systemClockProtocol.setter
    def systemClockProtocol(self, value: str):
        self._systemClockProtocol = value


class ProfileDetails(vmodl.DynamicData):
    @property
    def profile(self) -> List[ProfileSpec]: ...
    @profile.setter
    def profile(self, value: List[ProfileSpec]):
        self._profile = value
    @property
    def diskProfileDetails(self) -> List[ProfileDetails.DiskProfileDetails]: ...
    @diskProfileDetails.setter
    def diskProfileDetails(self, value: List[ProfileDetails.DiskProfileDetails]):
        self._diskProfileDetails = value


    class DiskProfileDetails(vmodl.DynamicData):
        @property
        def diskId(self) -> int: ...
        @diskId.setter
        def diskId(self, value: int):
            self._diskId = value
        @property
        def profile(self) -> List[ProfileSpec]: ...
        @profile.setter
        def profile(self, value: List[ProfileSpec]):
            self._profile = value


class ProfileRawData(vmodl.DynamicData):
    @property
    def extensionKey(self) -> str: ...
    @extensionKey.setter
    def extensionKey(self, value: str):
        self._extensionKey = value
    @property
    def objectData(self) -> str: ...
    @objectData.setter
    def objectData(self, value: str):
        self._objectData = value


class ProfileSpec(vmodl.DynamicData): ...


class PropertyRelation(vmodl.DynamicData):
    @property
    def key(self) -> vmodl.DynamicProperty: ...
    @key.setter
    def key(self, value: vmodl.DynamicProperty):
        self._key = value
    @property
    def relations(self) -> List[vmodl.DynamicProperty]: ...
    @relations.setter
    def relations(self, value: List[vmodl.DynamicProperty]):
        self._relations = value


class QuestionInfo(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str):
        self._text = value
    @property
    def choice(self) -> vim.option.ChoiceOption: ...
    @choice.setter
    def choice(self, value: vim.option.ChoiceOption):
        self._choice = value
    @property
    def message(self) -> List[Message]: ...
    @message.setter
    def message(self, value: List[Message]):
        self._message = value


class RelocateSpec(vmodl.DynamicData):
    @property
    def service(self) -> vim.ServiceLocator: ...
    @service.setter
    def service(self, value: vim.ServiceLocator):
        self._service = value
    @property
    def folder(self) -> vim.Folder: ...
    @folder.setter
    def folder(self, value: vim.Folder):
        self._folder = value
    @property
    def datastore(self) -> vim.Datastore: ...
    @datastore.setter
    def datastore(self, value: vim.Datastore):
        self._datastore = value
    @property
    def diskMoveType(self) -> str: ...
    @diskMoveType.setter
    def diskMoveType(self, value: str):
        self._diskMoveType = value
    @property
    def pool(self) -> vim.ResourcePool: ...
    @pool.setter
    def pool(self, value: vim.ResourcePool):
        self._pool = value
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def disk(self) -> List[RelocateSpec.DiskLocator]: ...
    @disk.setter
    def disk(self, value: List[RelocateSpec.DiskLocator]):
        self._disk = value
    @property
    def transform(self) -> RelocateSpec.Transformation | Literal['flat', 'sparse']: ...
    @transform.setter
    def transform(self, value: RelocateSpec.Transformation | Literal['flat', 'sparse']):
        self._transform = value
    @property
    def deviceChange(self) -> List[vim.vm.device.VirtualDeviceSpec]: ...
    @deviceChange.setter
    def deviceChange(self, value: List[vim.vm.device.VirtualDeviceSpec]):
        self._deviceChange = value
    @property
    def profile(self) -> List[ProfileSpec]: ...
    @profile.setter
    def profile(self, value: List[ProfileSpec]):
        self._profile = value
    @property
    def cryptoSpec(self) -> vim.encryption.CryptoSpec: ...
    @cryptoSpec.setter
    def cryptoSpec(self, value: vim.encryption.CryptoSpec):
        self._cryptoSpec = value


    class DiskLocator(vmodl.DynamicData):
        @property
        def diskId(self) -> int: ...
        @diskId.setter
        def diskId(self, value: int):
            self._diskId = value
        @property
        def datastore(self) -> vim.Datastore: ...
        @datastore.setter
        def datastore(self, value: vim.Datastore):
            self._datastore = value
        @property
        def diskMoveType(self) -> str: ...
        @diskMoveType.setter
        def diskMoveType(self, value: str):
            self._diskMoveType = value
        @property
        def diskBackingInfo(self) -> vim.vm.device.VirtualDevice.BackingInfo: ...
        @diskBackingInfo.setter
        def diskBackingInfo(self, value: vim.vm.device.VirtualDevice.BackingInfo):
            self._diskBackingInfo = value
        @property
        def profile(self) -> List[ProfileSpec]: ...
        @profile.setter
        def profile(self, value: List[ProfileSpec]):
            self._profile = value
        @property
        def backing(self) -> RelocateSpec.DiskLocator.BackingSpec: ...
        @backing.setter
        def backing(self, value: RelocateSpec.DiskLocator.BackingSpec):
            self._backing = value
        @property
        def filterSpec(self) -> List[BaseIndependentFilterSpec]: ...
        @filterSpec.setter
        def filterSpec(self, value: List[BaseIndependentFilterSpec]):
            self._filterSpec = value


        class BackingSpec(vmodl.DynamicData):
            @property
            def parent(self) -> RelocateSpec.DiskLocator.BackingSpec: ...
            @parent.setter
            def parent(self, value: RelocateSpec.DiskLocator.BackingSpec):
                self._parent = value
            @property
            def crypto(self) -> vim.encryption.CryptoSpec: ...
            @crypto.setter
            def crypto(self, value: vim.encryption.CryptoSpec):
                self._crypto = value


    class DiskMoveOptions(Enum):
        moveAllDiskBackingsAndAllowSharing = "moveAllDiskBackingsAndAllowSharing"
        moveAllDiskBackingsAndDisallowSharing = "moveAllDiskBackingsAndDisallowSharing"
        moveChildMostDiskBacking = "moveChildMostDiskBacking"
        createNewChildDiskBacking = "createNewChildDiskBacking"
        moveAllDiskBackingsAndConsolidate = "moveAllDiskBackingsAndConsolidate"


    class Transformation(Enum):
        flat = "flat"
        sparse = "sparse"


class ReplicationConfigSpec(vmodl.DynamicData):
    @property
    def generation(self) -> long: ...
    @generation.setter
    def generation(self, value: long):
        self._generation = value
    @property
    def vmReplicationId(self) -> str: ...
    @vmReplicationId.setter
    def vmReplicationId(self, value: str):
        self._vmReplicationId = value
    @property
    def destination(self) -> str: ...
    @destination.setter
    def destination(self, value: str):
        self._destination = value
    @property
    def port(self) -> int: ...
    @port.setter
    def port(self, value: int):
        self._port = value
    @property
    def rpo(self) -> long: ...
    @rpo.setter
    def rpo(self, value: long):
        self._rpo = value
    @property
    def quiesceGuestEnabled(self) -> bool: ...
    @quiesceGuestEnabled.setter
    def quiesceGuestEnabled(self, value: bool):
        self._quiesceGuestEnabled = value
    @property
    def paused(self) -> bool: ...
    @paused.setter
    def paused(self, value: bool):
        self._paused = value
    @property
    def oppUpdatesEnabled(self) -> bool: ...
    @oppUpdatesEnabled.setter
    def oppUpdatesEnabled(self, value: bool):
        self._oppUpdatesEnabled = value
    @property
    def netCompressionEnabled(self) -> bool: ...
    @netCompressionEnabled.setter
    def netCompressionEnabled(self, value: bool):
        self._netCompressionEnabled = value
    @property
    def netEncryptionEnabled(self) -> bool: ...
    @netEncryptionEnabled.setter
    def netEncryptionEnabled(self, value: bool):
        self._netEncryptionEnabled = value
    @property
    def encryptionDestination(self) -> str: ...
    @encryptionDestination.setter
    def encryptionDestination(self, value: str):
        self._encryptionDestination = value
    @property
    def encryptionPort(self) -> int: ...
    @encryptionPort.setter
    def encryptionPort(self, value: int):
        self._encryptionPort = value
    @property
    def remoteCertificateThumbprint(self) -> str: ...
    @remoteCertificateThumbprint.setter
    def remoteCertificateThumbprint(self, value: str):
        self._remoteCertificateThumbprint = value
    @property
    def dataSetsReplicationEnabled(self) -> bool: ...
    @dataSetsReplicationEnabled.setter
    def dataSetsReplicationEnabled(self, value: bool):
        self._dataSetsReplicationEnabled = value
    @property
    def disk(self) -> List[ReplicationConfigSpec.DiskSettings]: ...
    @disk.setter
    def disk(self, value: List[ReplicationConfigSpec.DiskSettings]):
        self._disk = value


    class DiskSettings(vmodl.DynamicData):
        @property
        def key(self) -> int: ...
        @key.setter
        def key(self, value: int):
            self._key = value
        @property
        def diskReplicationId(self) -> str: ...
        @diskReplicationId.setter
        def diskReplicationId(self, value: str):
            self._diskReplicationId = value


class RuntimeInfo(vmodl.DynamicData):
    @property
    def device(self) -> List[DeviceRuntimeInfo]: ...
    @device.setter
    def device(self, value: List[DeviceRuntimeInfo]):
        self._device = value
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def connectionState(self) -> vim.VirtualMachine.ConnectionState | Literal['connected', 'disconnected', 'orphaned', 'inaccessible', 'invalid']: ...
    @connectionState.setter
    def connectionState(self, value: vim.VirtualMachine.ConnectionState | Literal['connected', 'disconnected', 'orphaned', 'inaccessible', 'invalid']):
        self._connectionState = value
    @property
    def powerState(self) -> vim.VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended']: ...
    @powerState.setter
    def powerState(self, value: vim.VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended']):
        self._powerState = value
    @property
    def vmFailoverInProgress(self) -> bool: ...
    @vmFailoverInProgress.setter
    def vmFailoverInProgress(self, value: bool):
        self._vmFailoverInProgress = value
    @property
    def faultToleranceState(self) -> vim.VirtualMachine.FaultToleranceState | Literal['notConfigured', 'disabled', 'enabled', 'needSecondary', 'starting', 'running']: ...
    @faultToleranceState.setter
    def faultToleranceState(self, value: vim.VirtualMachine.FaultToleranceState | Literal['notConfigured', 'disabled', 'enabled', 'needSecondary', 'starting', 'running']):
        self._faultToleranceState = value
    @property
    def dasVmProtection(self) -> RuntimeInfo.DasProtectionState: ...
    @dasVmProtection.setter
    def dasVmProtection(self, value: RuntimeInfo.DasProtectionState):
        self._dasVmProtection = value
    @property
    def toolsInstallerMounted(self) -> bool: ...
    @toolsInstallerMounted.setter
    def toolsInstallerMounted(self, value: bool):
        self._toolsInstallerMounted = value
    @property
    def suspendTime(self) -> datetime: ...
    @suspendTime.setter
    def suspendTime(self, value: datetime):
        self._suspendTime = value
    @property
    def bootTime(self) -> datetime: ...
    @bootTime.setter
    def bootTime(self, value: datetime):
        self._bootTime = value
    @property
    def suspendInterval(self) -> long: ...
    @suspendInterval.setter
    def suspendInterval(self, value: long):
        self._suspendInterval = value
    @property
    def question(self) -> QuestionInfo: ...
    @question.setter
    def question(self, value: QuestionInfo):
        self._question = value
    @property
    def memoryOverhead(self) -> long: ...
    @memoryOverhead.setter
    def memoryOverhead(self, value: long):
        self._memoryOverhead = value
    @property
    def maxCpuUsage(self) -> int: ...
    @maxCpuUsage.setter
    def maxCpuUsage(self, value: int):
        self._maxCpuUsage = value
    @property
    def maxMemoryUsage(self) -> int: ...
    @maxMemoryUsage.setter
    def maxMemoryUsage(self, value: int):
        self._maxMemoryUsage = value
    @property
    def numMksConnections(self) -> int: ...
    @numMksConnections.setter
    def numMksConnections(self, value: int):
        self._numMksConnections = value
    @property
    def recordReplayState(self) -> vim.VirtualMachine.RecordReplayState | Literal['recording', 'replaying', 'inactive']: ...
    @recordReplayState.setter
    def recordReplayState(self, value: vim.VirtualMachine.RecordReplayState | Literal['recording', 'replaying', 'inactive']):
        self._recordReplayState = value
    @property
    def cleanPowerOff(self) -> bool: ...
    @cleanPowerOff.setter
    def cleanPowerOff(self, value: bool):
        self._cleanPowerOff = value
    @property
    def needSecondaryReason(self) -> str: ...
    @needSecondaryReason.setter
    def needSecondaryReason(self, value: str):
        self._needSecondaryReason = value
    @property
    def onlineStandby(self) -> bool: ...
    @onlineStandby.setter
    def onlineStandby(self, value: bool):
        self._onlineStandby = value
    @property
    def minRequiredEVCModeKey(self) -> str: ...
    @minRequiredEVCModeKey.setter
    def minRequiredEVCModeKey(self, value: str):
        self._minRequiredEVCModeKey = value
    @property
    def consolidationNeeded(self) -> bool: ...
    @consolidationNeeded.setter
    def consolidationNeeded(self, value: bool):
        self._consolidationNeeded = value
    @property
    def offlineFeatureRequirement(self) -> List[FeatureRequirement]: ...
    @offlineFeatureRequirement.setter
    def offlineFeatureRequirement(self, value: List[FeatureRequirement]):
        self._offlineFeatureRequirement = value
    @property
    def featureRequirement(self) -> List[FeatureRequirement]: ...
    @featureRequirement.setter
    def featureRequirement(self, value: List[FeatureRequirement]):
        self._featureRequirement = value
    @property
    def featureMask(self) -> List[vim.host.FeatureMask]: ...
    @featureMask.setter
    def featureMask(self, value: List[vim.host.FeatureMask]):
        self._featureMask = value
    @property
    def vFlashCacheAllocation(self) -> long: ...
    @vFlashCacheAllocation.setter
    def vFlashCacheAllocation(self, value: long):
        self._vFlashCacheAllocation = value
    @property
    def paused(self) -> bool: ...
    @paused.setter
    def paused(self, value: bool):
        self._paused = value
    @property
    def snapshotInBackground(self) -> bool: ...
    @snapshotInBackground.setter
    def snapshotInBackground(self, value: bool):
        self._snapshotInBackground = value
    @property
    def quiescedForkParent(self) -> bool: ...
    @quiescedForkParent.setter
    def quiescedForkParent(self, value: bool):
        self._quiescedForkParent = value
    @property
    def instantCloneFrozen(self) -> bool: ...
    @instantCloneFrozen.setter
    def instantCloneFrozen(self, value: bool):
        self._instantCloneFrozen = value
    @property
    def cryptoState(self) -> str: ...
    @cryptoState.setter
    def cryptoState(self, value: str):
        self._cryptoState = value
    @property
    def suspendedToMemory(self) -> bool: ...
    @suspendedToMemory.setter
    def suspendedToMemory(self, value: bool):
        self._suspendedToMemory = value
    @property
    def opNotificationTimeout(self) -> long: ...
    @opNotificationTimeout.setter
    def opNotificationTimeout(self, value: long):
        self._opNotificationTimeout = value
    @property
    def iommuActive(self) -> bool: ...
    @iommuActive.setter
    def iommuActive(self, value: bool):
        self._iommuActive = value


    class DasProtectionState(vmodl.DynamicData):
        @property
        def dasProtected(self) -> bool: ...
        @dasProtected.setter
        def dasProtected(self, value: bool):
            self._dasProtected = value


class ScheduledHardwareUpgradeInfo(vmodl.DynamicData):
    @property
    def upgradePolicy(self) -> str: ...
    @upgradePolicy.setter
    def upgradePolicy(self, value: str):
        self._upgradePolicy = value
    @property
    def versionKey(self) -> str: ...
    @versionKey.setter
    def versionKey(self, value: str):
        self._versionKey = value
    @property
    def scheduledHardwareUpgradeStatus(self) -> str: ...
    @scheduledHardwareUpgradeStatus.setter
    def scheduledHardwareUpgradeStatus(self, value: str):
        self._scheduledHardwareUpgradeStatus = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


    class HardwareUpgradePolicy(Enum):
        never = "never"
        onSoftPowerOff = "onSoftPowerOff"
        always = "always"


    class HardwareUpgradeStatus(Enum):
        none = "none"
        pending = "pending"
        success = "success"
        failed = "failed"


class ScsiDiskDeviceInfo(DiskDeviceInfo):
    @property
    def disk(self) -> vim.host.ScsiDisk: ...
    @disk.setter
    def disk(self, value: vim.host.ScsiDisk):
        self._disk = value
    @property
    def transportHint(self) -> str: ...
    @transportHint.setter
    def transportHint(self, value: str):
        self._transportHint = value
    @property
    def lunNumber(self) -> int: ...
    @lunNumber.setter
    def lunNumber(self, value: int):
        self._lunNumber = value


class ScsiPassthroughInfo(TargetInfo):
    @property
    def scsiClass(self) -> str: ...
    @scsiClass.setter
    def scsiClass(self, value: str):
        self._scsiClass = value
    @property
    def vendor(self) -> str: ...
    @vendor.setter
    def vendor(self, value: str):
        self._vendor = value
    @property
    def physicalUnitNumber(self) -> int: ...
    @physicalUnitNumber.setter
    def physicalUnitNumber(self, value: int):
        self._physicalUnitNumber = value


    class ScsiClass(Enum):
        disk = "disk"
        tape = "tape"
        printer = "printer"
        processor = "processor"
        worm = "worm"
        cdrom = "cdrom"
        scanner = "scanner"
        optical = "optical"
        media = "media"
        com = "com"
        raid = "raid"
        unknown = "unknown"


class SerialInfo(TargetInfo): ...


class SgxInfo(vmodl.DynamicData):
    @property
    def epcSize(self) -> long: ...
    @epcSize.setter
    def epcSize(self, value: long):
        self._epcSize = value
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
    def requireAttestation(self) -> bool: ...
    @requireAttestation.setter
    def requireAttestation(self, value: bool):
        self._requireAttestation = value


    class FlcModes(Enum):
        locked = "locked"
        unlocked = "unlocked"


class SgxTargetInfo(TargetInfo):
    @property
    def maxEpcSize(self) -> long: ...
    @maxEpcSize.setter
    def maxEpcSize(self, value: long):
        self._maxEpcSize = value
    @property
    def flcModes(self) -> List[str]: ...
    @flcModes.setter
    def flcModes(self, value: List[str]):
        self._flcModes = value
    @property
    def lePubKeyHashes(self) -> List[str]: ...
    @lePubKeyHashes.setter
    def lePubKeyHashes(self, value: List[str]):
        self._lePubKeyHashes = value
    @property
    def requireAttestationSupported(self) -> bool: ...
    @requireAttestationSupported.setter
    def requireAttestationSupported(self, value: bool):
        self._requireAttestationSupported = value


class SnapshotInfo(vmodl.DynamicData):
    @property
    def currentSnapshot(self) -> Snapshot: ...
    @currentSnapshot.setter
    def currentSnapshot(self, value: Snapshot):
        self._currentSnapshot = value
    @property
    def rootSnapshotList(self) -> List[SnapshotTree]: ...
    @rootSnapshotList.setter
    def rootSnapshotList(self, value: List[SnapshotTree]):
        self._rootSnapshotList = value


class SnapshotTree(vmodl.DynamicData):
    @property
    def snapshot(self) -> Snapshot: ...
    @snapshot.setter
    def snapshot(self, value: Snapshot):
        self._snapshot = value
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
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
    def id(self) -> int: ...
    @id.setter
    def id(self, value: int):
        self._id = value
    @property
    def createTime(self) -> datetime: ...
    @createTime.setter
    def createTime(self, value: datetime):
        self._createTime = value
    @property
    def state(self) -> vim.VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended']: ...
    @state.setter
    def state(self, value: vim.VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended']):
        self._state = value
    @property
    def quiesced(self) -> bool: ...
    @quiesced.setter
    def quiesced(self, value: bool):
        self._quiesced = value
    @property
    def backupManifest(self) -> str: ...
    @backupManifest.setter
    def backupManifest(self, value: str):
        self._backupManifest = value
    @property
    def childSnapshotList(self) -> List[SnapshotTree]: ...
    @childSnapshotList.setter
    def childSnapshotList(self, value: List[SnapshotTree]):
        self._childSnapshotList = value
    @property
    def replaySupported(self) -> bool: ...
    @replaySupported.setter
    def replaySupported(self, value: bool):
        self._replaySupported = value


class SoundInfo(TargetInfo): ...


class SriovDevicePoolInfo(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class SriovInfo(PciPassthroughInfo):
    @property
    def virtualFunction(self) -> bool: ...
    @virtualFunction.setter
    def virtualFunction(self, value: bool):
        self._virtualFunction = value
    @property
    def pnic(self) -> str: ...
    @pnic.setter
    def pnic(self, value: str):
        self._pnic = value
    @property
    def devicePool(self) -> SriovDevicePoolInfo: ...
    @devicePool.setter
    def devicePool(self, value: SriovDevicePoolInfo):
        self._devicePool = value


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


class StorageInfo(vmodl.DynamicData):
    @property
    def perDatastoreUsage(self) -> List[StorageInfo.UsageOnDatastore]: ...
    @perDatastoreUsage.setter
    def perDatastoreUsage(self, value: List[StorageInfo.UsageOnDatastore]):
        self._perDatastoreUsage = value
    @property
    def timestamp(self) -> datetime: ...
    @timestamp.setter
    def timestamp(self, value: datetime):
        self._timestamp = value


    class UsageOnDatastore(vmodl.DynamicData):
        @property
        def datastore(self) -> vim.Datastore: ...
        @datastore.setter
        def datastore(self, value: vim.Datastore):
            self._datastore = value
        @property
        def committed(self) -> long: ...
        @committed.setter
        def committed(self, value: long):
            self._committed = value
        @property
        def uncommitted(self) -> long: ...
        @uncommitted.setter
        def uncommitted(self, value: long):
            self._uncommitted = value
        @property
        def unshared(self) -> long: ...
        @unshared.setter
        def unshared(self, value: long):
            self._unshared = value


class Summary(vmodl.DynamicData):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def runtime(self) -> RuntimeInfo: ...
    @runtime.setter
    def runtime(self, value: RuntimeInfo):
        self._runtime = value
    @property
    def guest(self) -> Summary.GuestSummary: ...
    @guest.setter
    def guest(self, value: Summary.GuestSummary):
        self._guest = value
    @property
    def config(self) -> Summary.ConfigSummary: ...
    @config.setter
    def config(self, value: Summary.ConfigSummary):
        self._config = value
    @property
    def storage(self) -> Summary.StorageSummary: ...
    @storage.setter
    def storage(self, value: Summary.StorageSummary):
        self._storage = value
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
    def customValue(self) -> List[vim.CustomFieldsManager.Value]: ...
    @customValue.setter
    def customValue(self, value: List[vim.CustomFieldsManager.Value]):
        self._customValue = value


    class ConfigSummary(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def template(self) -> bool: ...
        @template.setter
        def template(self, value: bool):
            self._template = value
        @property
        def vmPathName(self) -> str: ...
        @vmPathName.setter
        def vmPathName(self, value: str):
            self._vmPathName = value
        @property
        def memorySizeMB(self) -> int: ...
        @memorySizeMB.setter
        def memorySizeMB(self, value: int):
            self._memorySizeMB = value
        @property
        def cpuReservation(self) -> int: ...
        @cpuReservation.setter
        def cpuReservation(self, value: int):
            self._cpuReservation = value
        @property
        def memoryReservation(self) -> int: ...
        @memoryReservation.setter
        def memoryReservation(self, value: int):
            self._memoryReservation = value
        @property
        def numCpu(self) -> int: ...
        @numCpu.setter
        def numCpu(self, value: int):
            self._numCpu = value
        @property
        def numEthernetCards(self) -> int: ...
        @numEthernetCards.setter
        def numEthernetCards(self, value: int):
            self._numEthernetCards = value
        @property
        def numVirtualDisks(self) -> int: ...
        @numVirtualDisks.setter
        def numVirtualDisks(self, value: int):
            self._numVirtualDisks = value
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def instanceUuid(self) -> str: ...
        @instanceUuid.setter
        def instanceUuid(self, value: str):
            self._instanceUuid = value
        @property
        def guestId(self) -> str: ...
        @guestId.setter
        def guestId(self, value: str):
            self._guestId = value
        @property
        def guestFullName(self) -> str: ...
        @guestFullName.setter
        def guestFullName(self, value: str):
            self._guestFullName = value
        @property
        def annotation(self) -> str: ...
        @annotation.setter
        def annotation(self, value: str):
            self._annotation = value
        @property
        def product(self) -> vim.vApp.ProductInfo: ...
        @product.setter
        def product(self, value: vim.vApp.ProductInfo):
            self._product = value
        @property
        def installBootRequired(self) -> bool: ...
        @installBootRequired.setter
        def installBootRequired(self, value: bool):
            self._installBootRequired = value
        @property
        def ftInfo(self) -> FaultToleranceConfigInfo: ...
        @ftInfo.setter
        def ftInfo(self, value: FaultToleranceConfigInfo):
            self._ftInfo = value
        @property
        def managedBy(self) -> vim.ext.ManagedByInfo: ...
        @managedBy.setter
        def managedBy(self, value: vim.ext.ManagedByInfo):
            self._managedBy = value
        @property
        def tpmPresent(self) -> bool: ...
        @tpmPresent.setter
        def tpmPresent(self, value: bool):
            self._tpmPresent = value
        @property
        def numVmiopBackings(self) -> int: ...
        @numVmiopBackings.setter
        def numVmiopBackings(self, value: int):
            self._numVmiopBackings = value
        @property
        def hwVersion(self) -> str: ...
        @hwVersion.setter
        def hwVersion(self, value: str):
            self._hwVersion = value


    class GuestSummary(vmodl.DynamicData):
        @property
        def guestId(self) -> str: ...
        @guestId.setter
        def guestId(self, value: str):
            self._guestId = value
        @property
        def guestFullName(self) -> str: ...
        @guestFullName.setter
        def guestFullName(self, value: str):
            self._guestFullName = value
        @property
        def toolsStatus(self) -> GuestInfo.ToolsStatus | Literal['toolsNotInstalled', 'toolsNotRunning', 'toolsOld', 'toolsOk']: ...
        @toolsStatus.setter
        def toolsStatus(self, value: GuestInfo.ToolsStatus | Literal['toolsNotInstalled', 'toolsNotRunning', 'toolsOld', 'toolsOk']):
            self._toolsStatus = value
        @property
        def toolsVersionStatus(self) -> str: ...
        @toolsVersionStatus.setter
        def toolsVersionStatus(self, value: str):
            self._toolsVersionStatus = value
        @property
        def toolsVersionStatus2(self) -> str: ...
        @toolsVersionStatus2.setter
        def toolsVersionStatus2(self, value: str):
            self._toolsVersionStatus2 = value
        @property
        def toolsRunningStatus(self) -> str: ...
        @toolsRunningStatus.setter
        def toolsRunningStatus(self, value: str):
            self._toolsRunningStatus = value
        @property
        def hostName(self) -> str: ...
        @hostName.setter
        def hostName(self, value: str):
            self._hostName = value
        @property
        def ipAddress(self) -> str: ...
        @ipAddress.setter
        def ipAddress(self, value: str):
            self._ipAddress = value
        @property
        def hwVersion(self) -> str: ...
        @hwVersion.setter
        def hwVersion(self, value: str):
            self._hwVersion = value


    class QuickStats(vmodl.DynamicData):
        @property
        def overallCpuUsage(self) -> int: ...
        @overallCpuUsage.setter
        def overallCpuUsage(self, value: int):
            self._overallCpuUsage = value
        @property
        def overallCpuDemand(self) -> int: ...
        @overallCpuDemand.setter
        def overallCpuDemand(self, value: int):
            self._overallCpuDemand = value
        @property
        def overallCpuReadiness(self) -> int: ...
        @overallCpuReadiness.setter
        def overallCpuReadiness(self, value: int):
            self._overallCpuReadiness = value
        @property
        def guestMemoryUsage(self) -> int: ...
        @guestMemoryUsage.setter
        def guestMemoryUsage(self, value: int):
            self._guestMemoryUsage = value
        @property
        def hostMemoryUsage(self) -> int: ...
        @hostMemoryUsage.setter
        def hostMemoryUsage(self, value: int):
            self._hostMemoryUsage = value
        @property
        def guestHeartbeatStatus(self) -> vim.ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']: ...
        @guestHeartbeatStatus.setter
        def guestHeartbeatStatus(self, value: vim.ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']):
            self._guestHeartbeatStatus = value
        @property
        def distributedCpuEntitlement(self) -> int: ...
        @distributedCpuEntitlement.setter
        def distributedCpuEntitlement(self, value: int):
            self._distributedCpuEntitlement = value
        @property
        def distributedMemoryEntitlement(self) -> int: ...
        @distributedMemoryEntitlement.setter
        def distributedMemoryEntitlement(self, value: int):
            self._distributedMemoryEntitlement = value
        @property
        def staticCpuEntitlement(self) -> int: ...
        @staticCpuEntitlement.setter
        def staticCpuEntitlement(self, value: int):
            self._staticCpuEntitlement = value
        @property
        def staticMemoryEntitlement(self) -> int: ...
        @staticMemoryEntitlement.setter
        def staticMemoryEntitlement(self, value: int):
            self._staticMemoryEntitlement = value
        @property
        def grantedMemory(self) -> int: ...
        @grantedMemory.setter
        def grantedMemory(self, value: int):
            self._grantedMemory = value
        @property
        def privateMemory(self) -> int: ...
        @privateMemory.setter
        def privateMemory(self, value: int):
            self._privateMemory = value
        @property
        def sharedMemory(self) -> int: ...
        @sharedMemory.setter
        def sharedMemory(self, value: int):
            self._sharedMemory = value
        @property
        def swappedMemory(self) -> int: ...
        @swappedMemory.setter
        def swappedMemory(self, value: int):
            self._swappedMemory = value
        @property
        def balloonedMemory(self) -> int: ...
        @balloonedMemory.setter
        def balloonedMemory(self, value: int):
            self._balloonedMemory = value
        @property
        def consumedOverheadMemory(self) -> int: ...
        @consumedOverheadMemory.setter
        def consumedOverheadMemory(self, value: int):
            self._consumedOverheadMemory = value
        @property
        def ftLogBandwidth(self) -> int: ...
        @ftLogBandwidth.setter
        def ftLogBandwidth(self, value: int):
            self._ftLogBandwidth = value
        @property
        def ftSecondaryLatency(self) -> int: ...
        @ftSecondaryLatency.setter
        def ftSecondaryLatency(self, value: int):
            self._ftSecondaryLatency = value
        @property
        def ftLatencyStatus(self) -> vim.ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']: ...
        @ftLatencyStatus.setter
        def ftLatencyStatus(self, value: vim.ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']):
            self._ftLatencyStatus = value
        @property
        def compressedMemory(self) -> long: ...
        @compressedMemory.setter
        def compressedMemory(self, value: long):
            self._compressedMemory = value
        @property
        def uptimeSeconds(self) -> int: ...
        @uptimeSeconds.setter
        def uptimeSeconds(self, value: int):
            self._uptimeSeconds = value
        @property
        def ssdSwappedMemory(self) -> long: ...
        @ssdSwappedMemory.setter
        def ssdSwappedMemory(self, value: long):
            self._ssdSwappedMemory = value
        @property
        def activeMemory(self) -> int: ...
        @activeMemory.setter
        def activeMemory(self, value: int):
            self._activeMemory = value
        @property
        def memoryTierStats(self) -> List[Summary.QuickStats.MemoryTierStats]: ...
        @memoryTierStats.setter
        def memoryTierStats(self, value: List[Summary.QuickStats.MemoryTierStats]):
            self._memoryTierStats = value


        class MemoryTierStats(vmodl.DynamicData):
            @property
            def memoryTierType(self) -> str: ...
            @memoryTierType.setter
            def memoryTierType(self, value: str):
                self._memoryTierType = value
            @property
            def readBandwidth(self) -> long: ...
            @readBandwidth.setter
            def readBandwidth(self, value: long):
                self._readBandwidth = value


    class StorageSummary(vmodl.DynamicData):
        @property
        def committed(self) -> long: ...
        @committed.setter
        def committed(self, value: long):
            self._committed = value
        @property
        def uncommitted(self) -> long: ...
        @uncommitted.setter
        def uncommitted(self, value: long):
            self._uncommitted = value
        @property
        def unshared(self) -> long: ...
        @unshared.setter
        def unshared(self, value: long):
            self._unshared = value
        @property
        def timestamp(self) -> datetime: ...
        @timestamp.setter
        def timestamp(self, value: datetime):
            self._timestamp = value


class TargetInfo(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def configurationTag(self) -> List[str]: ...
    @configurationTag.setter
    def configurationTag(self, value: List[str]):
        self._configurationTag = value


    class ConfigurationTag(Enum):
        compliant = "compliant"
        clusterWide = "clusterWide"


class ToolsConfigInfo(vmodl.DynamicData):
    @property
    def toolsVersion(self) -> int: ...
    @toolsVersion.setter
    def toolsVersion(self, value: int):
        self._toolsVersion = value
    @property
    def toolsInstallType(self) -> str: ...
    @toolsInstallType.setter
    def toolsInstallType(self, value: str):
        self._toolsInstallType = value
    @property
    def afterPowerOn(self) -> bool: ...
    @afterPowerOn.setter
    def afterPowerOn(self, value: bool):
        self._afterPowerOn = value
    @property
    def afterResume(self) -> bool: ...
    @afterResume.setter
    def afterResume(self, value: bool):
        self._afterResume = value
    @property
    def beforeGuestStandby(self) -> bool: ...
    @beforeGuestStandby.setter
    def beforeGuestStandby(self, value: bool):
        self._beforeGuestStandby = value
    @property
    def beforeGuestShutdown(self) -> bool: ...
    @beforeGuestShutdown.setter
    def beforeGuestShutdown(self, value: bool):
        self._beforeGuestShutdown = value
    @property
    def beforeGuestReboot(self) -> bool: ...
    @beforeGuestReboot.setter
    def beforeGuestReboot(self, value: bool):
        self._beforeGuestReboot = value
    @property
    def toolsUpgradePolicy(self) -> str: ...
    @toolsUpgradePolicy.setter
    def toolsUpgradePolicy(self, value: str):
        self._toolsUpgradePolicy = value
    @property
    def pendingCustomization(self) -> str: ...
    @pendingCustomization.setter
    def pendingCustomization(self, value: str):
        self._pendingCustomization = value
    @property
    def customizationKeyId(self) -> vim.encryption.CryptoKeyId: ...
    @customizationKeyId.setter
    def customizationKeyId(self, value: vim.encryption.CryptoKeyId):
        self._customizationKeyId = value
    @property
    def syncTimeWithHostAllowed(self) -> bool: ...
    @syncTimeWithHostAllowed.setter
    def syncTimeWithHostAllowed(self, value: bool):
        self._syncTimeWithHostAllowed = value
    @property
    def syncTimeWithHost(self) -> bool: ...
    @syncTimeWithHost.setter
    def syncTimeWithHost(self, value: bool):
        self._syncTimeWithHost = value
    @property
    def lastInstallInfo(self) -> ToolsConfigInfo.ToolsLastInstallInfo: ...
    @lastInstallInfo.setter
    def lastInstallInfo(self, value: ToolsConfigInfo.ToolsLastInstallInfo):
        self._lastInstallInfo = value


    class ToolsLastInstallInfo(vmodl.DynamicData):
        @property
        def counter(self) -> int: ...
        @counter.setter
        def counter(self, value: int):
            self._counter = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


    class UpgradePolicy(Enum):
        manual = "manual"
        upgradeAtPowerCycle = "upgradeAtPowerCycle"


class UsbInfo(TargetInfo):
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def vendor(self) -> int: ...
    @vendor.setter
    def vendor(self, value: int):
        self._vendor = value
    @property
    def product(self) -> int: ...
    @product.setter
    def product(self, value: int):
        self._product = value
    @property
    def physicalPath(self) -> str: ...
    @physicalPath.setter
    def physicalPath(self, value: str):
        self._physicalPath = value
    @property
    def family(self) -> List[str]: ...
    @family.setter
    def family(self, value: List[str]):
        self._family = value
    @property
    def speed(self) -> List[str]: ...
    @speed.setter
    def speed(self, value: List[str]):
        self._speed = value
    @property
    def summary(self) -> Summary: ...
    @summary.setter
    def summary(self, value: Summary):
        self._summary = value


    class Family(Enum):
        audio = "audio"
        hid = "hid"
        hid_bootable = "hid_bootable"
        physical = "physical"
        communication = "communication"
        imaging = "imaging"
        printer = "printer"
        storage = "storage"
        hub = "hub"
        smart_card = "smart_card"
        security = "security"
        video = "video"
        wireless = "wireless"
        bluetooth = "bluetooth"
        wusb = "wusb"
        pda = "pda"
        vendor_specific = "vendor_specific"
        other = "other"
        unknownFamily = "unknownFamily"


    class Speed(Enum):
        low = "low"
        full = "full"
        high = "high"
        superSpeed = "superSpeed"
        superSpeedPlus = "superSpeedPlus"
        superSpeed20Gbps = "superSpeed20Gbps"
        unknownSpeed = "unknownSpeed"


class UsbScanCodeSpec(vmodl.DynamicData):
    @property
    def keyEvents(self) -> List[UsbScanCodeSpec.KeyEvent]: ...
    @keyEvents.setter
    def keyEvents(self, value: List[UsbScanCodeSpec.KeyEvent]):
        self._keyEvents = value


    class KeyEvent(vmodl.DynamicData):
        @property
        def usbHidCode(self) -> int: ...
        @usbHidCode.setter
        def usbHidCode(self, value: int):
            self._usbHidCode = value
        @property
        def modifiers(self) -> UsbScanCodeSpec.ModifierType: ...
        @modifiers.setter
        def modifiers(self, value: UsbScanCodeSpec.ModifierType):
            self._modifiers = value


    class ModifierType(vmodl.DynamicData):
        @property
        def leftControl(self) -> bool: ...
        @leftControl.setter
        def leftControl(self, value: bool):
            self._leftControl = value
        @property
        def leftShift(self) -> bool: ...
        @leftShift.setter
        def leftShift(self, value: bool):
            self._leftShift = value
        @property
        def leftAlt(self) -> bool: ...
        @leftAlt.setter
        def leftAlt(self, value: bool):
            self._leftAlt = value
        @property
        def leftGui(self) -> bool: ...
        @leftGui.setter
        def leftGui(self, value: bool):
            self._leftGui = value
        @property
        def rightControl(self) -> bool: ...
        @rightControl.setter
        def rightControl(self, value: bool):
            self._rightControl = value
        @property
        def rightShift(self) -> bool: ...
        @rightShift.setter
        def rightShift(self, value: bool):
            self._rightShift = value
        @property
        def rightAlt(self) -> bool: ...
        @rightAlt.setter
        def rightAlt(self, value: bool):
            self._rightAlt = value
        @property
        def rightGui(self) -> bool: ...
        @rightGui.setter
        def rightGui(self, value: bool):
            self._rightGui = value


class VFlashModuleInfo(TargetInfo):
    @property
    def vFlashModule(self) -> vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption: ...
    @vFlashModule.setter
    def vFlashModule(self, value: vim.host.VFlashManager.VFlashCacheConfigInfo.VFlashModuleConfigOption):
        self._vFlashModule = value


class VcpuConfig(vmodl.DynamicData):
    @property
    def latencySensitivity(self) -> vim.LatencySensitivity: ...
    @latencySensitivity.setter
    def latencySensitivity(self, value: vim.LatencySensitivity):
        self._latencySensitivity = value


class VendorDeviceGroupInfo(TargetInfo):
    @property
    def deviceGroupName(self) -> str: ...
    @deviceGroupName.setter
    def deviceGroupName(self, value: str):
        self._deviceGroupName = value
    @property
    def deviceGroupDescription(self) -> str: ...
    @deviceGroupDescription.setter
    def deviceGroupDescription(self, value: str):
        self._deviceGroupDescription = value
    @property
    def componentDeviceInfo(self) -> List[VendorDeviceGroupInfo.ComponentDeviceInfo]: ...
    @componentDeviceInfo.setter
    def componentDeviceInfo(self, value: List[VendorDeviceGroupInfo.ComponentDeviceInfo]):
        self._componentDeviceInfo = value


    class ComponentDeviceInfo(vmodl.DynamicData):
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def vendorName(self) -> str: ...
        @vendorName.setter
        def vendorName(self, value: str):
            self._vendorName = value
        @property
        def deviceName(self) -> str: ...
        @deviceName.setter
        def deviceName(self, value: str):
            self._deviceName = value
        @property
        def isConfigurable(self) -> bool: ...
        @isConfigurable.setter
        def isConfigurable(self, value: bool):
            self._isConfigurable = value
        @property
        def device(self) -> vim.vm.device.VirtualDevice: ...
        @device.setter
        def device(self, value: vim.vm.device.VirtualDevice):
            self._device = value


        class ComponentType(Enum):
            pciPassthru = "pciPassthru"
            nvidiaVgpu = "nvidiaVgpu"
            sriovNic = "sriovNic"
            dvx = "dvx"


class VgpuDeviceInfo(TargetInfo):
    @property
    def deviceName(self) -> str: ...
    @deviceName.setter
    def deviceName(self, value: str):
        self._deviceName = value
    @property
    def deviceVendorId(self) -> long: ...
    @deviceVendorId.setter
    def deviceVendorId(self, value: long):
        self._deviceVendorId = value
    @property
    def maxFbSizeInGib(self) -> long: ...
    @maxFbSizeInGib.setter
    def maxFbSizeInGib(self, value: long):
        self._maxFbSizeInGib = value
    @property
    def timeSlicedCapable(self) -> bool: ...
    @timeSlicedCapable.setter
    def timeSlicedCapable(self, value: bool):
        self._timeSlicedCapable = value
    @property
    def migCapable(self) -> bool: ...
    @migCapable.setter
    def migCapable(self, value: bool):
        self._migCapable = value
    @property
    def computeProfileCapable(self) -> bool: ...
    @computeProfileCapable.setter
    def computeProfileCapable(self, value: bool):
        self._computeProfileCapable = value
    @property
    def quadroProfileCapable(self) -> bool: ...
    @quadroProfileCapable.setter
    def quadroProfileCapable(self, value: bool):
        self._quadroProfileCapable = value


class VgpuProfileInfo(TargetInfo):
    @property
    def profileName(self) -> str: ...
    @profileName.setter
    def profileName(self, value: str):
        self._profileName = value
    @property
    def deviceVendorId(self) -> long: ...
    @deviceVendorId.setter
    def deviceVendorId(self, value: long):
        self._deviceVendorId = value
    @property
    def fbSizeInGib(self) -> long: ...
    @fbSizeInGib.setter
    def fbSizeInGib(self, value: long):
        self._fbSizeInGib = value
    @property
    def profileSharing(self) -> str: ...
    @profileSharing.setter
    def profileSharing(self, value: str):
        self._profileSharing = value
    @property
    def profileClass(self) -> str: ...
    @profileClass.setter
    def profileClass(self, value: str):
        self._profileClass = value


    class ProfileClass(Enum):
        compute = "compute"
        quadro = "quadro"


    class ProfileSharing(Enum):
        timeSliced = "timeSliced"
        mig = "mig"


class VirtualDeviceGroups(vmodl.DynamicData):
    @property
    def deviceGroup(self) -> List[VirtualDeviceGroups.DeviceGroup]: ...
    @deviceGroup.setter
    def deviceGroup(self, value: List[VirtualDeviceGroups.DeviceGroup]):
        self._deviceGroup = value


    class DeviceGroup(vmodl.DynamicData):
        @property
        def groupInstanceKey(self) -> int: ...
        @groupInstanceKey.setter
        def groupInstanceKey(self, value: int):
            self._groupInstanceKey = value
        @property
        def deviceInfo(self) -> vim.Description: ...
        @deviceInfo.setter
        def deviceInfo(self, value: vim.Description):
            self._deviceInfo = value


    class VendorDeviceGroup(VirtualDeviceGroups.DeviceGroup):
        @property
        def deviceGroupName(self) -> str: ...
        @deviceGroupName.setter
        def deviceGroupName(self, value: str):
            self._deviceGroupName = value


class VirtualDeviceSwap(vmodl.DynamicData):
    @property
    def lsiToPvscsi(self) -> VirtualDeviceSwap.DeviceSwapInfo: ...
    @lsiToPvscsi.setter
    def lsiToPvscsi(self, value: VirtualDeviceSwap.DeviceSwapInfo):
        self._lsiToPvscsi = value


    class DeviceSwapInfo(vmodl.DynamicData):
        @property
        def enabled(self) -> bool: ...
        @enabled.setter
        def enabled(self, value: bool):
            self._enabled = value
        @property
        def applicable(self) -> bool: ...
        @applicable.setter
        def applicable(self, value: bool):
            self._applicable = value
        @property
        def status(self) -> str: ...
        @status.setter
        def status(self, value: str):
            self._status = value


    class DeviceSwapStatus(Enum):
        none = "none"
        scheduled = "scheduled"
        inprogress = "inprogress"
        failed = "failed"
        completed = "completed"


class VirtualHardware(vmodl.DynamicData):
    @property
    def numCPU(self) -> int: ...
    @numCPU.setter
    def numCPU(self, value: int):
        self._numCPU = value
    @property
    def numCoresPerSocket(self) -> int: ...
    @numCoresPerSocket.setter
    def numCoresPerSocket(self, value: int):
        self._numCoresPerSocket = value
    @property
    def autoCoresPerSocket(self) -> bool: ...
    @autoCoresPerSocket.setter
    def autoCoresPerSocket(self, value: bool):
        self._autoCoresPerSocket = value
    @property
    def memoryMB(self) -> int: ...
    @memoryMB.setter
    def memoryMB(self, value: int):
        self._memoryMB = value
    @property
    def virtualICH7MPresent(self) -> bool: ...
    @virtualICH7MPresent.setter
    def virtualICH7MPresent(self, value: bool):
        self._virtualICH7MPresent = value
    @property
    def virtualSMCPresent(self) -> bool: ...
    @virtualSMCPresent.setter
    def virtualSMCPresent(self, value: bool):
        self._virtualSMCPresent = value
    @property
    def device(self) -> List[vim.vm.device.VirtualDevice]: ...
    @device.setter
    def device(self, value: List[vim.vm.device.VirtualDevice]):
        self._device = value
    @property
    def motherboardLayout(self) -> str: ...
    @motherboardLayout.setter
    def motherboardLayout(self, value: str):
        self._motherboardLayout = value
    @property
    def simultaneousThreads(self) -> int: ...
    @simultaneousThreads.setter
    def simultaneousThreads(self, value: int):
        self._simultaneousThreads = value


    class MotherboardLayout(Enum):
        i440bxHostBridge = "i440bxHostBridge"
        acpiHostBridges = "acpiHostBridges"


class VirtualHardwareOption(vmodl.DynamicData):
    @property
    def hwVersion(self) -> int: ...
    @hwVersion.setter
    def hwVersion(self, value: int):
        self._hwVersion = value
    @property
    def virtualDeviceOption(self) -> List[vim.vm.device.VirtualDeviceOption]: ...
    @virtualDeviceOption.setter
    def virtualDeviceOption(self, value: List[vim.vm.device.VirtualDeviceOption]):
        self._virtualDeviceOption = value
    @property
    def deviceListReadonly(self) -> bool: ...
    @deviceListReadonly.setter
    def deviceListReadonly(self, value: bool):
        self._deviceListReadonly = value
    @property
    def numCPU(self) -> List[int]: ...
    @numCPU.setter
    def numCPU(self, value: List[int]):
        self._numCPU = value
    @property
    def numCoresPerSocket(self) -> vim.option.IntOption: ...
    @numCoresPerSocket.setter
    def numCoresPerSocket(self, value: vim.option.IntOption):
        self._numCoresPerSocket = value
    @property
    def autoCoresPerSocket(self) -> vim.option.BoolOption: ...
    @autoCoresPerSocket.setter
    def autoCoresPerSocket(self, value: vim.option.BoolOption):
        self._autoCoresPerSocket = value
    @property
    def numCpuReadonly(self) -> bool: ...
    @numCpuReadonly.setter
    def numCpuReadonly(self, value: bool):
        self._numCpuReadonly = value
    @property
    def memoryMB(self) -> vim.option.LongOption: ...
    @memoryMB.setter
    def memoryMB(self, value: vim.option.LongOption):
        self._memoryMB = value
    @property
    def numPCIControllers(self) -> vim.option.IntOption: ...
    @numPCIControllers.setter
    def numPCIControllers(self, value: vim.option.IntOption):
        self._numPCIControllers = value
    @property
    def numIDEControllers(self) -> vim.option.IntOption: ...
    @numIDEControllers.setter
    def numIDEControllers(self, value: vim.option.IntOption):
        self._numIDEControllers = value
    @property
    def numUSBControllers(self) -> vim.option.IntOption: ...
    @numUSBControllers.setter
    def numUSBControllers(self, value: vim.option.IntOption):
        self._numUSBControllers = value
    @property
    def numUSBXHCIControllers(self) -> vim.option.IntOption: ...
    @numUSBXHCIControllers.setter
    def numUSBXHCIControllers(self, value: vim.option.IntOption):
        self._numUSBXHCIControllers = value
    @property
    def numSIOControllers(self) -> vim.option.IntOption: ...
    @numSIOControllers.setter
    def numSIOControllers(self, value: vim.option.IntOption):
        self._numSIOControllers = value
    @property
    def numPS2Controllers(self) -> vim.option.IntOption: ...
    @numPS2Controllers.setter
    def numPS2Controllers(self, value: vim.option.IntOption):
        self._numPS2Controllers = value
    @property
    def licensingLimit(self) -> List[PropertyPath]: ...
    @licensingLimit.setter
    def licensingLimit(self, value: List[PropertyPath]):
        self._licensingLimit = value
    @property
    def numSupportedWwnPorts(self) -> vim.option.IntOption: ...
    @numSupportedWwnPorts.setter
    def numSupportedWwnPorts(self, value: vim.option.IntOption):
        self._numSupportedWwnPorts = value
    @property
    def numSupportedWwnNodes(self) -> vim.option.IntOption: ...
    @numSupportedWwnNodes.setter
    def numSupportedWwnNodes(self, value: vim.option.IntOption):
        self._numSupportedWwnNodes = value
    @property
    def resourceConfigOption(self) -> vim.ResourceConfigOption: ...
    @resourceConfigOption.setter
    def resourceConfigOption(self, value: vim.ResourceConfigOption):
        self._resourceConfigOption = value
    @property
    def numNVDIMMControllers(self) -> vim.option.IntOption: ...
    @numNVDIMMControllers.setter
    def numNVDIMMControllers(self, value: vim.option.IntOption):
        self._numNVDIMMControllers = value
    @property
    def numTPMDevices(self) -> vim.option.IntOption: ...
    @numTPMDevices.setter
    def numTPMDevices(self, value: vim.option.IntOption):
        self._numTPMDevices = value
    @property
    def numWDTDevices(self) -> vim.option.IntOption: ...
    @numWDTDevices.setter
    def numWDTDevices(self, value: vim.option.IntOption):
        self._numWDTDevices = value
    @property
    def numPrecisionClockDevices(self) -> vim.option.IntOption: ...
    @numPrecisionClockDevices.setter
    def numPrecisionClockDevices(self, value: vim.option.IntOption):
        self._numPrecisionClockDevices = value
    @property
    def epcMemoryMB(self) -> vim.option.LongOption: ...
    @epcMemoryMB.setter
    def epcMemoryMB(self, value: vim.option.LongOption):
        self._epcMemoryMB = value
    @property
    def acpiHostBridgesFirmware(self) -> List[str]: ...
    @acpiHostBridgesFirmware.setter
    def acpiHostBridgesFirmware(self, value: List[str]):
        self._acpiHostBridgesFirmware = value
    @property
    def numCpuSimultaneousThreads(self) -> vim.option.IntOption: ...
    @numCpuSimultaneousThreads.setter
    def numCpuSimultaneousThreads(self, value: vim.option.IntOption):
        self._numCpuSimultaneousThreads = value
    @property
    def numNumaNodes(self) -> vim.option.IntOption: ...
    @numNumaNodes.setter
    def numNumaNodes(self, value: vim.option.IntOption):
        self._numNumaNodes = value
    @property
    def numDeviceGroups(self) -> vim.option.IntOption: ...
    @numDeviceGroups.setter
    def numDeviceGroups(self, value: vim.option.IntOption):
        self._numDeviceGroups = value
    @property
    def deviceGroupTypes(self) -> List[type]: ...
    @deviceGroupTypes.setter
    def deviceGroupTypes(self, value: List[type]):
        self._deviceGroupTypes = value


class VirtualNuma(vmodl.DynamicData):
    @property
    def coresPerNumaNode(self) -> int: ...
    @coresPerNumaNode.setter
    def coresPerNumaNode(self, value: int):
        self._coresPerNumaNode = value
    @property
    def exposeVnumaOnCpuHotadd(self) -> bool: ...
    @exposeVnumaOnCpuHotadd.setter
    def exposeVnumaOnCpuHotadd(self, value: bool):
        self._exposeVnumaOnCpuHotadd = value


class VirtualNumaInfo(vmodl.DynamicData):
    @property
    def coresPerNumaNode(self) -> int: ...
    @coresPerNumaNode.setter
    def coresPerNumaNode(self, value: int):
        self._coresPerNumaNode = value
    @property
    def autoCoresPerNumaNode(self) -> bool: ...
    @autoCoresPerNumaNode.setter
    def autoCoresPerNumaNode(self, value: bool):
        self._autoCoresPerNumaNode = value
    @property
    def vnumaOnCpuHotaddExposed(self) -> bool: ...
    @vnumaOnCpuHotaddExposed.setter
    def vnumaOnCpuHotaddExposed(self, value: bool):
        self._vnumaOnCpuHotaddExposed = value


class VirtualPMem(vmodl.DynamicData):
    @property
    def snapshotMode(self) -> str: ...
    @snapshotMode.setter
    def snapshotMode(self, value: str):
        self._snapshotMode = value


    class SnapshotMode(Enum):
        independent_persistent = "independent_persistent"
        independent_eraseonrevert = "independent_eraseonrevert"


class VmImportSpec(vim.ImportSpec):
    @property
    def configSpec(self) -> ConfigSpec: ...
    @configSpec.setter
    def configSpec(self, value: ConfigSpec):
        self._configSpec = value
    @property
    def resPoolEntity(self) -> vim.ResourcePool: ...
    @resPoolEntity.setter
    def resPoolEntity(self, value: vim.ResourcePool):
        self._resPoolEntity = value


class WindowsQuiesceSpec(GuestQuiesceSpec):
    @property
    def vssBackupType(self) -> int: ...
    @vssBackupType.setter
    def vssBackupType(self, value: int):
        self._vssBackupType = value
    @property
    def vssBootableSystemState(self) -> bool: ...
    @vssBootableSystemState.setter
    def vssBootableSystemState(self, value: bool):
        self._vssBootableSystemState = value
    @property
    def vssPartialFileSupport(self) -> bool: ...
    @vssPartialFileSupport.setter
    def vssPartialFileSupport(self, value: bool):
        self._vssPartialFileSupport = value
    @property
    def vssBackupContext(self) -> str: ...
    @vssBackupContext.setter
    def vssBackupContext(self, value: str):
        self._vssBackupContext = value


    class VssBackupContext(Enum):
        ctx_auto = "ctx_auto"
        ctx_backup = "ctx_backup"
        ctx_file_share_backup = "ctx_file_share_backup"


class GuestQuiesce():


    class EndGuestQuiesceError(Enum):
        failure = "failure"