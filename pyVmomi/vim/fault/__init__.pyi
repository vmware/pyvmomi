from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, PropertyPath, long


class ActiveDirectoryFault(VimFault):
    @property
    def errorCode(self) -> int: ...


class ActiveVMsBlockingEVC(EVCConfigFault):
    @property
    def evcMode(self) -> str: ...
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @property
    def hostName(self) -> List[str]: ...


class AdminDisabled(HostConfigFault): ...


class AdminNotDisabled(HostConfigFault): ...


class AffinityConfigured(MigrationFault):
    @property
    def configuredAffinity(self) -> List[str]: ...


    class Affinity(Enum):
        memory = "memory"
        cpu = "cpu"


class AgentInstallFailed(HostConnectFault):
    @property
    def reason(self) -> str: ...
    @property
    def statusCode(self) -> int: ...
    @property
    def installerOutput(self) -> str: ...


    class Reason(Enum):
        NotEnoughSpaceOnDevice = "NotEnoughSpaceOnDevice"
        PrepareToUpgradeFailed = "PrepareToUpgradeFailed"
        AgentNotRunning = "AgentNotRunning"
        AgentNotReachable = "AgentNotReachable"
        InstallTimedout = "InstallTimedout"
        SignatureVerificationFailed = "SignatureVerificationFailed"
        AgentUploadFailed = "AgentUploadFailed"
        AgentUploadTimedout = "AgentUploadTimedout"
        UnknownInstallerError = "UnknownInstallerError"


class AlreadyBeingManaged(HostConnectFault):
    @property
    def ipAddress(self) -> str: ...


class AlreadyConnected(HostConnectFault):
    @property
    def name(self) -> str: ...


class AlreadyExists(VimFault):
    @property
    def name(self) -> str: ...


class AlreadyUpgraded(VimFault): ...


class AnswerFileUpdateFailed(VimFault):
    @property
    def failure(self) -> List[AnswerFileUpdateFailed.UpdateFailure]: ...


    class UpdateFailure(vmodl.DynamicData):
        @property
        def userInputPath(self) -> vim.profile.ProfilePropertyPath: ...
        @property
        def errMsg(self) -> vmodl.LocalizableMessage: ...


class ApplicationQuiesceFault(SnapshotFault): ...


class AuthMinimumAdminPermission(VimFault): ...


class BackupBlobReadFailure(DvsFault):
    @property
    def entityName(self) -> str: ...
    @property
    def entityType(self) -> str: ...
    @property
    def fault(self) -> vmodl.MethodFault: ...


class BackupBlobWriteFailure(DvsFault):
    @property
    def entityName(self) -> str: ...
    @property
    def entityType(self) -> str: ...
    @property
    def fault(self) -> vmodl.MethodFault: ...


class BlockedByFirewall(HostConfigFault): ...


class CAMServerRefusedConnection(InvalidCAMServer): ...


class CannotAccessFile(FileFault): ...


class CannotAccessLocalSource(VimFault): ...


class CannotAccessNetwork(CannotAccessVmDevice):
    @property
    def network(self) -> vim.Network: ...


class CannotAccessVmComponent(VmConfigFault): ...


class CannotAccessVmConfig(CannotAccessVmComponent):
    @property
    def reason(self) -> vmodl.MethodFault: ...


class CannotAccessVmDevice(CannotAccessVmComponent):
    @property
    def device(self) -> str: ...
    @property
    def backing(self) -> str: ...
    @property
    def connected(self) -> bool: ...


class CannotAccessVmDisk(CannotAccessVmDevice):
    @property
    def fault(self) -> vmodl.MethodFault: ...


class CannotAddHostWithFTVmAsStandalone(HostConnectFault): ...


class CannotAddHostWithFTVmToDifferentCluster(HostConnectFault): ...


class CannotAddHostWithFTVmToNonHACluster(HostConnectFault): ...


class CannotChangeDrsBehaviorForFtSecondary(VmFaultToleranceIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def vmName(self) -> str: ...


class CannotChangeHaSettingsForFtSecondary(VmFaultToleranceIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def vmName(self) -> str: ...


class CannotChangeVsanClusterUuid(VsanFault): ...


class CannotChangeVsanNodeUuid(VsanFault): ...


class CannotComputeFTCompatibleHosts(VmFaultToleranceIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def vmName(self) -> str: ...


class CannotCreateFile(FileFault): ...


class CannotDecryptPasswords(CustomizationFault): ...


class CannotDeleteFile(FileFault): ...


class CannotDisableDrsOnClustersWithVApps(vmodl.RuntimeFault): ...


class CannotDisableSnapshot(VmConfigFault): ...


class CannotDisconnectHostWithFaultToleranceVm(VimFault):
    @property
    def hostName(self) -> str: ...


class CannotEnableVmcpForCluster(VimFault):
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def hostName(self) -> str: ...
    @property
    def reason(self) -> str: ...


class CannotModifyConfigCpuRequirements(MigrationFault): ...


class CannotMoveFaultToleranceVm(VimFault):
    @property
    def moveType(self) -> str: ...
    @property
    def vmName(self) -> str: ...


    class MoveType(Enum):
        resourcePool = "resourcePool"
        cluster = "cluster"


class CannotMoveHostWithFaultToleranceVm(VimFault): ...


class CannotMoveVmWithDeltaDisk(MigrationFault):
    @property
    def device(self) -> str: ...


class CannotMoveVmWithNativeDeltaDisk(MigrationFault): ...


class CannotMoveVsanEnabledHost(VsanFault): ...


class CannotPlaceWithoutPrerequisiteMoves(VimFault): ...


class CannotPowerOffVmInCluster(InvalidState):
    @property
    def operation(self) -> str: ...
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def vmName(self) -> str: ...


    class Operation(Enum):
        suspend = "suspend"
        powerOff = "powerOff"
        guestShutdown = "guestShutdown"
        guestSuspend = "guestSuspend"


class CannotReconfigureVsanWhenHaEnabled(VsanFault): ...


class CannotUseNetwork(VmConfigFault):
    @property
    def device(self) -> str: ...
    @property
    def backing(self) -> str: ...
    @property
    def connected(self) -> bool: ...
    @property
    def reason(self) -> str: ...
    @property
    def network(self) -> vim.Network: ...


class ClockSkew(HostConfigFault): ...


class CloneFromSnapshotNotSupported(MigrationFault): ...


class CollectorAddressUnset(DvsFault): ...


class ConcurrentAccess(VimFault): ...


class ConflictingConfiguration(DvsFault):
    @property
    def configInConflict(self) -> List[ConflictingConfiguration.Config]: ...


    class Config(vmodl.DynamicData):
        @property
        def entity(self) -> vim.ManagedEntity: ...
        @property
        def propertyPath(self) -> str: ...


class ConflictingDatastoreFound(vmodl.RuntimeFault):
    @property
    def name(self) -> str: ...
    @property
    def url(self) -> str: ...


class ConnectedIso(OvfExport):
    @property
    def cdrom(self) -> vim.vm.device.VirtualCdrom: ...
    @property
    def filename(self) -> str: ...


class CpuCompatibilityUnknown(CpuIncompatible): ...


class CpuHotPlugNotSupported(VmConfigFault): ...


class CpuIncompatible(VirtualHardwareCompatibilityIssue):
    @property
    def level(self) -> int: ...
    @property
    def registerName(self) -> str: ...
    @property
    def registerBits(self) -> str: ...
    @property
    def desiredBits(self) -> str: ...
    @property
    def host(self) -> vim.HostSystem: ...


class CpuIncompatible1ECX(CpuIncompatible):
    @property
    def sse3(self) -> bool: ...
    @property
    def pclmulqdq(self) -> bool: ...
    @property
    def ssse3(self) -> bool: ...
    @property
    def sse41(self) -> bool: ...
    @property
    def sse42(self) -> bool: ...
    @property
    def aes(self) -> bool: ...
    @property
    def other(self) -> bool: ...
    @property
    def otherOnly(self) -> bool: ...


class CpuIncompatible81EDX(CpuIncompatible):
    @property
    def nx(self) -> bool: ...
    @property
    def ffxsr(self) -> bool: ...
    @property
    def rdtscp(self) -> bool: ...
    @property
    def lm(self) -> bool: ...
    @property
    def other(self) -> bool: ...
    @property
    def otherOnly(self) -> bool: ...


class CustomizationFault(VimFault): ...


class CustomizationPending(CustomizationFault): ...


class DVPortNotSupported(DeviceBackingNotSupported): ...


class DasConfigFault(VimFault):
    @property
    def reason(self) -> str: ...
    @property
    def output(self) -> str: ...
    @property
    def event(self) -> List[vim.event.Event]: ...


    class DasConfigFaultReason(Enum):
        HostNetworkMisconfiguration = "HostNetworkMisconfiguration"
        HostMisconfiguration = "HostMisconfiguration"
        InsufficientPrivileges = "InsufficientPrivileges"
        NoPrimaryAgentAvailable = "NoPrimaryAgentAvailable"
        Other = "Other"
        NoDatastoresConfigured = "NoDatastoresConfigured"
        CreateConfigVvolFailed = "CreateConfigVvolFailed"
        VSanNotSupportedOnHost = "VSanNotSupportedOnHost"
        DasNetworkMisconfiguration = "DasNetworkMisconfiguration"
        SetDesiredImageSpecFailed = "SetDesiredImageSpecFailed"
        ApplyHAVibsOnClusterFailed = "ApplyHAVibsOnClusterFailed"


class DatabaseError(vmodl.RuntimeFault): ...


class DatacenterMismatch(MigrationFault):
    @property
    def invalidArgument(self) -> List[DatacenterMismatch.Argument]: ...
    @property
    def expectedDatacenter(self) -> vim.Datacenter: ...


    class Argument(vmodl.DynamicData):
        @property
        def entity(self) -> vim.ManagedEntity: ...
        @property
        def inputDatacenter(self) -> vim.Datacenter: ...


class DatastoreNotWritableOnHost(InvalidDatastore):
    @property
    def host(self) -> vim.HostSystem: ...


class DeltaDiskFormatNotSupported(VmConfigFault):
    @property
    def datastore(self) -> List[vim.Datastore]: ...
    @property
    def deltaDiskFormat(self) -> str: ...


class DestinationSwitchFull(CannotAccessNetwork): ...


class DestinationVsanDisabled(CannotMoveVsanEnabledHost):
    @property
    def destinationCluster(self) -> str: ...


class DeviceBackingNotSupported(DeviceNotSupported):
    @property
    def backing(self) -> str: ...


class DeviceControllerNotSupported(DeviceNotSupported):
    @property
    def controller(self) -> str: ...


class DeviceHotPlugNotSupported(InvalidDeviceSpec): ...


class DeviceNotFound(InvalidDeviceSpec): ...


class DeviceNotSupported(VirtualHardwareCompatibilityIssue):
    @property
    def device(self) -> str: ...
    @property
    def reason(self) -> str: ...


class DeviceUnsupportedForVmPlatform(InvalidDeviceSpec): ...


class DeviceUnsupportedForVmVersion(InvalidDeviceSpec):
    @property
    def currentVersion(self) -> str: ...
    @property
    def expectedVersion(self) -> str: ...


class DigestNotSupported(DeviceNotSupported): ...


class DirectoryNotEmpty(FileFault): ...


class DisableAdminNotSupported(HostConfigFault): ...


class DisallowedChangeByService(vmodl.RuntimeFault):
    @property
    def serviceName(self) -> str: ...
    @property
    def disallowedChange(self) -> str: ...


    class DisallowedChange(Enum):
        hotExtendDisk = "hotExtendDisk"


class DisallowedDiskModeChange(InvalidDeviceSpec): ...


class DisallowedMigrationDeviceAttached(MigrationFault):
    @property
    def fault(self) -> vmodl.MethodFault: ...


class DisallowedOperationOnFailoverHost(vmodl.RuntimeFault):
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def hostname(self) -> str: ...


class DisconnectedHostsBlockingEVC(EVCConfigFault): ...


class DiskHasPartitions(VsanDiskFault): ...


class DiskIsLastRemainingNonSSD(VsanDiskFault): ...


class DiskIsNonLocal(VsanDiskFault): ...


class DiskIsUSB(VsanDiskFault): ...


class DiskMoveTypeNotSupported(MigrationFault): ...


class DiskNotSupported(VirtualHardwareCompatibilityIssue):
    @property
    def disk(self) -> int: ...


class DiskTooSmall(VsanDiskFault): ...


class DomainNotFound(ActiveDirectoryFault):
    @property
    def domainName(self) -> str: ...


class DrsDisabledOnVm(VimFault): ...


class DrsVmotionIncompatibleFault(VirtualHardwareCompatibilityIssue):
    @property
    def host(self) -> vim.HostSystem: ...


class DuplicateDisks(VsanDiskFault): ...


class DuplicateName(VimFault):
    @property
    def name(self) -> str: ...
    @property
    def object(self) -> ManagedObject: ...


class DuplicateVsanNetworkInterface(VsanFault):
    @property
    def device(self) -> str: ...


class DvsApplyOperationFault(DvsFault):
    @property
    def objectFault(self) -> List[DvsApplyOperationFault.FaultOnObject]: ...


    class FaultOnObject(vmodl.DynamicData):
        @property
        def objectId(self) -> str: ...
        @property
        def type(self) -> type: ...
        @property
        def fault(self) -> vmodl.MethodFault: ...


class DvsFault(VimFault): ...


class DvsNotAuthorized(DvsFault):
    @property
    def sessionExtensionKey(self) -> str: ...
    @property
    def dvsExtensionKey(self) -> str: ...


class DvsOperationBulkFault(DvsFault):
    @property
    def hostFault(self) -> List[DvsOperationBulkFault.FaultOnHost]: ...


    class FaultOnHost(vmodl.DynamicData):
        @property
        def host(self) -> vim.HostSystem: ...
        @property
        def fault(self) -> vmodl.MethodFault: ...


class DvsScopeViolated(DvsFault):
    @property
    def scope(self) -> List[vim.ManagedEntity]: ...
    @property
    def entity(self) -> vim.ManagedEntity: ...


class EVCAdmissionFailed(NotSupportedHostInCluster):
    @property
    def faults(self) -> List[vmodl.MethodFault]: ...


class EVCAdmissionFailedCPUFeaturesForMode(EVCAdmissionFailed):
    @property
    def currentEVCModeKey(self) -> str: ...


class EVCAdmissionFailedCPUModel(EVCAdmissionFailed): ...


class EVCAdmissionFailedCPUModelForMode(EVCAdmissionFailed):
    @property
    def currentEVCModeKey(self) -> str: ...


class EVCAdmissionFailedCPUVendor(EVCAdmissionFailed):
    @property
    def clusterCPUVendor(self) -> str: ...
    @property
    def hostCPUVendor(self) -> str: ...


class EVCAdmissionFailedCPUVendorUnknown(EVCAdmissionFailed): ...


class EVCAdmissionFailedHostDisconnected(EVCAdmissionFailed): ...


class EVCAdmissionFailedHostSoftware(EVCAdmissionFailed): ...


class EVCAdmissionFailedHostSoftwareForMode(EVCAdmissionFailed): ...


class EVCAdmissionFailedVmActive(EVCAdmissionFailed): ...


class EVCConfigFault(VimFault):
    @property
    def faults(self) -> List[vmodl.MethodFault]: ...


class EVCModeIllegalByVendor(EVCConfigFault):
    @property
    def clusterCPUVendor(self) -> str: ...
    @property
    def modeCPUVendor(self) -> str: ...


class EVCModeUnsupportedByHosts(EVCConfigFault):
    @property
    def evcMode(self) -> str: ...
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @property
    def hostName(self) -> List[str]: ...


class EVCUnsupportedByHostHardware(EVCConfigFault):
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @property
    def hostName(self) -> List[str]: ...


class EVCUnsupportedByHostSoftware(EVCConfigFault):
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @property
    def hostName(self) -> List[str]: ...


class EightHostLimitViolated(VmConfigFault): ...


class EncryptionKeyRequired(InvalidState):
    @property
    def requiredKey(self) -> List[vim.encryption.CryptoKeyId]: ...


class ExpiredAddonLicense(ExpiredFeatureLicense): ...


class ExpiredEditionLicense(ExpiredFeatureLicense): ...


class ExpiredFeatureLicense(NotEnoughLicenses):
    @property
    def feature(self) -> str: ...
    @property
    def count(self) -> int: ...
    @property
    def expirationDate(self) -> datetime: ...


class ExtendedFault(VimFault):
    @property
    def faultTypeId(self) -> str: ...
    @property
    def data(self) -> List[vim.KeyValue]: ...


class FailToEnableSPBM(NotEnoughLicenses):
    @property
    def cs(self) -> vim.ComputeResource: ...
    @property
    def csName(self) -> str: ...
    @property
    def hostLicenseStates(self) -> List[vim.ComputeResource.HostSPBMLicenseInfo]: ...


class FailToLockFaultToleranceVMs(vmodl.RuntimeFault):
    @property
    def vmName(self) -> str: ...
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def alreadyLockedVm(self) -> vim.VirtualMachine: ...


class FaultToleranceAntiAffinityViolated(MigrationFault):
    @property
    def hostName(self) -> str: ...
    @property
    def host(self) -> vim.HostSystem: ...


class FaultToleranceCannotEditMem(VmConfigFault):
    @property
    def vmName(self) -> str: ...
    @property
    def vm(self) -> vim.VirtualMachine: ...


class FaultToleranceCpuIncompatible(CpuIncompatible):
    @property
    def model(self) -> bool: ...
    @property
    def family(self) -> bool: ...
    @property
    def stepping(self) -> bool: ...


class FaultToleranceNeedsThickDisk(MigrationFault):
    @property
    def vmName(self) -> str: ...


class FaultToleranceNotLicensed(VmFaultToleranceIssue):
    @property
    def hostName(self) -> str: ...


class FaultToleranceNotSameBuild(MigrationFault):
    @property
    def build(self) -> str: ...


class FaultTolerancePrimaryPowerOnNotAttempted(VmFaultToleranceIssue):
    @property
    def secondaryVm(self) -> vim.VirtualMachine: ...
    @property
    def primaryVm(self) -> vim.VirtualMachine: ...


class FaultToleranceVmNotDasProtected(VimFault):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def vmName(self) -> str: ...


class FcoeFault(VimFault): ...


class FcoeFaultPnicHasNoPortSet(FcoeFault):
    @property
    def nicDevice(self) -> str: ...


class FeatureRequirementsNotMet(VirtualHardwareCompatibilityIssue):
    @property
    def featureRequirement(self) -> List[vim.vm.FeatureRequirement]: ...
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def host(self) -> vim.HostSystem: ...


class FileAlreadyExists(FileFault): ...


class FileBackedPortNotSupported(DeviceNotSupported): ...


class FileFault(VimFault):
    @property
    def file(self) -> str: ...


class FileLocked(FileFault): ...


class FileNameTooLong(FileFault): ...


class FileNotFound(FileFault): ...


class FileNotWritable(FileFault): ...


class FileTooLarge(FileFault):
    @property
    def datastore(self) -> str: ...
    @property
    def fileSize(self) -> long: ...
    @property
    def maxFileSize(self) -> long: ...


class FilesystemQuiesceFault(SnapshotFault): ...


class FilterInUse(ResourceInUse):
    @property
    def disk(self) -> List[vim.vm.device.VirtualDiskId]: ...


class FtIssuesOnHost(VmFaultToleranceIssue):
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def hostName(self) -> str: ...
    @property
    def errors(self) -> List[vmodl.MethodFault]: ...


    class HostSelectionType(Enum):
        user = "user"
        vc = "vc"
        drs = "drs"


class FullStorageVMotionNotSupported(MigrationFeatureNotSupported): ...


class GatewayConnectFault(HostConnectFault):
    @property
    def gatewayType(self) -> str: ...
    @property
    def gatewayId(self) -> str: ...
    @property
    def gatewayInfo(self) -> str: ...
    @property
    def details(self) -> vmodl.LocalizableMessage: ...


class GatewayHostNotReachable(GatewayToHostConnectFault): ...


class GatewayNotFound(GatewayConnectFault): ...


class GatewayNotReachable(GatewayConnectFault): ...


class GatewayOperationRefused(GatewayConnectFault): ...


class GatewayToHostAuthFault(GatewayToHostConnectFault):
    @property
    def invalidProperties(self) -> List[str]: ...
    @property
    def missingProperties(self) -> List[str]: ...


class GatewayToHostConnectFault(GatewayConnectFault):
    @property
    def hostname(self) -> str: ...
    @property
    def port(self) -> int: ...


class GatewayToHostTrustVerifyFault(GatewayToHostConnectFault):
    @property
    def verificationToken(self) -> str: ...
    @property
    def propertiesToVerify(self) -> List[vim.KeyValue]: ...


class GenericDrsFault(VimFault):
    @property
    def hostFaults(self) -> List[vmodl.MethodFault]: ...


class GenericVmConfigFault(VmConfigFault):
    @property
    def reason(self) -> str: ...


class GuestAuthenticationChallenge(GuestOperationsFault):
    @property
    def serverChallenge(self) -> vim.vm.guest.GuestAuthentication: ...
    @property
    def sessionID(self) -> long: ...


class GuestComponentsOutOfDate(GuestOperationsFault): ...


class GuestMultipleMappings(GuestOperationsFault): ...


class GuestOperationsFault(VimFault): ...


class GuestOperationsUnavailable(GuestOperationsFault): ...


class GuestPermissionDenied(GuestOperationsFault): ...


class GuestProcessNotFound(GuestOperationsFault):
    @property
    def pid(self) -> long: ...


class GuestRegistryFault(GuestOperationsFault):
    @property
    def windowsSystemErrorCode(self) -> long: ...


class GuestRegistryKeyAlreadyExists(GuestRegistryKeyFault): ...


class GuestRegistryKeyFault(GuestRegistryFault):
    @property
    def keyName(self) -> str: ...


class GuestRegistryKeyHasSubkeys(GuestRegistryKeyFault): ...


class GuestRegistryKeyInvalid(GuestRegistryKeyFault): ...


class GuestRegistryKeyParentVolatile(GuestRegistryKeyFault): ...


class GuestRegistryValueFault(GuestRegistryFault):
    @property
    def keyName(self) -> str: ...
    @property
    def valueName(self) -> str: ...


class GuestRegistryValueNotFound(GuestRegistryValueFault): ...


class HAErrorsAtDest(MigrationFault): ...


class HeterogenousHostsBlockingEVC(EVCConfigFault): ...


class HostAccessRestrictedToManagementServer(NotSupported):
    @property
    def managementServer(self) -> str: ...


class HostConfigFailed(HostConfigFault):
    @property
    def failure(self) -> List[vmodl.MethodFault]: ...


class HostConfigFault(VimFault): ...


class HostConnectFault(VimFault): ...


class HostHasComponentFailure(VimFault):
    @property
    def hostName(self) -> str: ...
    @property
    def componentType(self) -> str: ...
    @property
    def componentName(self) -> str: ...


    class HostComponentType(Enum):
        Datastore = "Datastore"


class HostInDomain(HostConfigFault): ...


class HostIncompatibleForFaultTolerance(VmFaultToleranceIssue):
    @property
    def hostName(self) -> str: ...
    @property
    def reason(self) -> str: ...


class HostIncompatibleForRecordReplay(VimFault):
    @property
    def hostName(self) -> str: ...
    @property
    def reason(self) -> str: ...


class HostInventoryFull(NotEnoughLicenses):
    @property
    def capacity(self) -> int: ...


class HostPowerOpFailed(VimFault): ...


class HostSpecificationOperationFailed(VimFault):
    @property
    def host(self) -> vim.HostSystem: ...


class HotSnapshotMoveNotSupported(SnapshotCopyNotSupported): ...


class HttpFault(VimFault):
    @property
    def statusCode(self) -> int: ...
    @property
    def statusMessage(self) -> str: ...


class IDEDiskNotSupported(DiskNotSupported): ...


class IORMNotSupportedHostOnDatastore(VimFault):
    @property
    def datastore(self) -> vim.Datastore: ...
    @property
    def datastoreName(self) -> str: ...
    @property
    def host(self) -> List[vim.HostSystem]: ...


class ImportHostAddFailure(DvsFault):
    @property
    def hostIp(self) -> List[str]: ...


class ImportOperationBulkFault(DvsFault):
    @property
    def importFaults(self) -> List[ImportOperationBulkFault.FaultOnImport]: ...


    class FaultOnImport(vmodl.DynamicData):
        @property
        def entityType(self) -> str: ...
        @property
        def key(self) -> str: ...
        @property
        def fault(self) -> vmodl.MethodFault: ...


class InUseFeatureManipulationDisallowed(NotEnoughLicenses): ...


class InaccessibleDatastore(InvalidDatastore):
    @property
    def detail(self) -> str: ...


class InaccessibleFTMetadataDatastore(InaccessibleDatastore): ...


class InaccessibleVFlashSource(VimFault):
    @property
    def hostName(self) -> str: ...


class IncompatibleDefaultDevice(MigrationFault):
    @property
    def device(self) -> str: ...


class IncompatibleHostForFtSecondary(VmFaultToleranceIssue):
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def error(self) -> List[vmodl.MethodFault]: ...


class IncompatibleHostForVmReplication(ReplicationFault):
    @property
    def vmName(self) -> str: ...
    @property
    def hostName(self) -> str: ...
    @property
    def reason(self) -> str: ...


    class IncompatibleReason(Enum):
        rpo = "rpo"
        netCompression = "netCompression"


class IncompatibleSetting(InvalidArgument):
    @property
    def conflictingProperty(self) -> PropertyPath: ...


class IncorrectFileType(FileFault): ...


class IncorrectHostInformation(NotEnoughLicenses): ...


class IndependentDiskVMotionNotSupported(MigrationFeatureNotSupported): ...


class InsufficientAgentVmsDeployed(InsufficientResourcesFault):
    @property
    def hostName(self) -> str: ...
    @property
    def requiredNumAgentVms(self) -> int: ...
    @property
    def currentNumAgentVms(self) -> int: ...


class InsufficientCpuResourcesFault(InsufficientResourcesFault):
    @property
    def unreserved(self) -> long: ...
    @property
    def requested(self) -> long: ...


class InsufficientDisks(VsanDiskFault): ...


class InsufficientFailoverResourcesFault(InsufficientResourcesFault): ...


class InsufficientGraphicsResourcesFault(InsufficientResourcesFault): ...


class InsufficientHostCapacityFault(InsufficientResourcesFault):
    @property
    def host(self) -> vim.HostSystem: ...


class InsufficientHostCpuCapacityFault(InsufficientHostCapacityFault):
    @property
    def unreserved(self) -> long: ...
    @property
    def requested(self) -> long: ...


class InsufficientHostMemoryCapacityFault(InsufficientHostCapacityFault):
    @property
    def unreserved(self) -> long: ...
    @property
    def requested(self) -> long: ...


class InsufficientMemoryResourcesFault(InsufficientResourcesFault):
    @property
    def unreserved(self) -> long: ...
    @property
    def requested(self) -> long: ...


class InsufficientNetworkCapacity(InsufficientResourcesFault): ...


class InsufficientNetworkResourcePoolCapacity(InsufficientResourcesFault):
    @property
    def dvsName(self) -> str: ...
    @property
    def dvsUuid(self) -> str: ...
    @property
    def resourcePoolKey(self) -> str: ...
    @property
    def available(self) -> long: ...
    @property
    def requested(self) -> long: ...
    @property
    def device(self) -> List[str]: ...


class InsufficientPerCpuCapacity(InsufficientHostCapacityFault): ...


class InsufficientResourcesFault(VimFault): ...


class InsufficientStandbyCpuResource(InsufficientStandbyResource):
    @property
    def available(self) -> long: ...
    @property
    def requested(self) -> long: ...


class InsufficientStandbyMemoryResource(InsufficientStandbyResource):
    @property
    def available(self) -> long: ...
    @property
    def requested(self) -> long: ...


class InsufficientStandbyResource(InsufficientResourcesFault): ...


class InsufficientStorageIops(VimFault):
    @property
    def unreservedIops(self) -> long: ...
    @property
    def requestedIops(self) -> long: ...
    @property
    def datastoreName(self) -> str: ...


class InsufficientStorageSpace(InsufficientResourcesFault): ...


class InsufficientVFlashResourcesFault(InsufficientResourcesFault):
    @property
    def freeSpaceInMB(self) -> long: ...
    @property
    def freeSpace(self) -> long: ...
    @property
    def requestedSpaceInMB(self) -> long: ...
    @property
    def requestedSpace(self) -> long: ...


class InvalidAffinitySettingFault(VimFault): ...


class InvalidBmcRole(VimFault): ...


class InvalidBundle(PlatformConfigFault): ...


class InvalidCAMCertificate(InvalidCAMServer): ...


class InvalidCAMServer(ActiveDirectoryFault):
    @property
    def camServer(self) -> str: ...


class InvalidClientCertificate(InvalidLogin): ...


class InvalidController(InvalidDeviceSpec):
    @property
    def controllerKey(self) -> int: ...


class InvalidDasConfigArgument(InvalidArgument):
    @property
    def entry(self) -> str: ...
    @property
    def clusterName(self) -> str: ...


    class EntryForInvalidArgument(Enum):
        admissionControl = "admissionControl"
        userHeartbeatDs = "userHeartbeatDs"
        vmConfig = "vmConfig"


class InvalidDasRestartPriorityForFtVm(InvalidArgument):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def vmName(self) -> str: ...


class InvalidDatastore(VimFault):
    @property
    def datastore(self) -> vim.Datastore: ...
    @property
    def name(self) -> str: ...


class InvalidDatastorePath(InvalidDatastore):
    @property
    def datastorePath(self) -> str: ...


class InvalidDatastoreState(InvalidState):
    @property
    def datastoreName(self) -> str: ...


class InvalidDeviceBacking(InvalidDeviceSpec): ...


class InvalidDeviceOperation(InvalidDeviceSpec):
    @property
    def badOp(self) -> vim.vm.device.VirtualDeviceSpec.Operation: ...
    @property
    def badFileOp(self) -> vim.vm.device.VirtualDeviceSpec.FileOperation: ...


class InvalidDeviceSpec(InvalidVmConfig):
    @property
    def deviceIndex(self) -> int: ...


class InvalidDiskFormat(InvalidFormat): ...


class InvalidDrsBehaviorForFtVm(InvalidArgument):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def vmName(self) -> str: ...


class InvalidEditionLicense(NotEnoughLicenses):
    @property
    def feature(self) -> str: ...


class InvalidEvent(VimFault): ...


class InvalidFolder(VimFault):
    @property
    def target(self) -> vim.ManagedEntity: ...


class InvalidFormat(VmConfigFault): ...


class InvalidGuestLogin(GuestOperationsFault): ...


class InvalidHostConnectionState(InvalidHostState): ...


class InvalidHostName(HostConfigFault): ...


class InvalidHostState(InvalidState):
    @property
    def host(self) -> vim.HostSystem: ...


class InvalidIndexArgument(InvalidArgument):
    @property
    def key(self) -> str: ...


class InvalidIpfixConfig(DvsFault):
    @property
    def property(self) -> PropertyPath: ...


class InvalidIpmiLoginInfo(VimFault): ...


class InvalidIpmiMacAddress(VimFault):
    @property
    def userProvidedMacAddress(self) -> str: ...
    @property
    def observedMacAddress(self) -> str: ...


class InvalidLicense(VimFault):
    @property
    def licenseContent(self) -> str: ...


class InvalidLocale(VimFault): ...


class InvalidLogin(VimFault): ...


class InvalidName(VimFault):
    @property
    def name(self) -> str: ...
    @property
    def entity(self) -> vim.ManagedEntity: ...


class InvalidNasCredentials(NasConfigFault):
    @property
    def userName(self) -> str: ...


class InvalidNetworkInType(VAppPropertyFault): ...


class InvalidNetworkResource(NasConfigFault):
    @property
    def remoteHost(self) -> str: ...
    @property
    def remotePath(self) -> str: ...


class InvalidOperationOnSecondaryVm(VmFaultToleranceIssue):
    @property
    def instanceUuid(self) -> str: ...


class InvalidPowerState(InvalidState):
    @property
    def requestedState(self) -> vim.VirtualMachine.PowerState: ...
    @property
    def existingState(self) -> vim.VirtualMachine.PowerState: ...


class InvalidPrivilege(VimFault):
    @property
    def privilege(self) -> str: ...


class InvalidProfileReferenceHost(vmodl.RuntimeFault):
    @property
    def reason(self) -> str: ...
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def profile(self) -> vim.profile.Profile: ...
    @property
    def profileName(self) -> str: ...


class InvalidPropertyType(VAppPropertyFault): ...


class InvalidPropertyValue(VAppPropertyFault): ...


class InvalidResourcePoolStructureFault(InsufficientResourcesFault): ...


class InvalidSnapshotFormat(InvalidFormat): ...


class InvalidState(VimFault): ...


class InvalidVmConfig(VmConfigFault):
    @property
    def property(self) -> PropertyPath: ...


class InvalidVmState(InvalidState):
    @property
    def vm(self) -> vim.VirtualMachine: ...


class InventoryHasStandardAloneHosts(NotEnoughLicenses):
    @property
    def hosts(self) -> List[str]: ...


class IpHostnameGeneratorError(CustomizationFault): ...


class IscsiFault(VimFault): ...


class IscsiFaultInvalidVnic(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...


class IscsiFaultPnicInUse(IscsiFault):
    @property
    def pnicDevice(self) -> str: ...


class IscsiFaultVnicAlreadyBound(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...


class IscsiFaultVnicHasActivePaths(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...


class IscsiFaultVnicHasMultipleUplinks(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...


class IscsiFaultVnicHasNoUplinks(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...


class IscsiFaultVnicHasWrongUplink(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...


class IscsiFaultVnicInUse(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...


class IscsiFaultVnicIsLastPath(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...


class IscsiFaultVnicNotBound(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...


class IscsiFaultVnicNotFound(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...


class KeyNotFound(VimFault):
    @property
    def key(self) -> str: ...


class LargeRDMConversionNotSupported(MigrationFault):
    @property
    def device(self) -> str: ...


class LargeRDMNotSupportedOnDatastore(VmConfigFault):
    @property
    def device(self) -> str: ...
    @property
    def datastore(self) -> vim.Datastore: ...
    @property
    def datastoreName(self) -> str: ...


class LegacyNetworkInterfaceInUse(CannotAccessNetwork): ...


class LicenseAssignmentFailed(vmodl.RuntimeFault):
    @property
    def reason(self) -> str: ...


class LicenseDowngradeDisallowed(NotEnoughLicenses):
    @property
    def edition(self) -> str: ...
    @property
    def entityId(self) -> str: ...
    @property
    def features(self) -> List[vmodl.KeyAnyValue]: ...


class LicenseEntityNotFound(VimFault):
    @property
    def entityId(self) -> str: ...


class LicenseExpired(NotEnoughLicenses):
    @property
    def licenseKey(self) -> str: ...


class LicenseKeyEntityMismatch(NotEnoughLicenses): ...


class LicenseRestricted(NotEnoughLicenses): ...


class LicenseServerUnavailable(VimFault):
    @property
    def licenseServer(self) -> str: ...


class LicenseSourceUnavailable(NotEnoughLicenses):
    @property
    def licenseSource(self) -> vim.LicenseManager.LicenseSource: ...


class LimitExceeded(VimFault):
    @property
    def property(self) -> PropertyPath: ...
    @property
    def limit(self) -> int: ...


class LinuxVolumeNotClean(CustomizationFault): ...


class LogBundlingFailed(VimFault): ...


class MaintenanceModeFileMove(MigrationFault): ...


class MemoryFileFormatNotSupportedByDatastore(UnsupportedDatastore):
    @property
    def datastoreName(self) -> str: ...
    @property
    def type(self) -> str: ...


class MemoryHotPlugNotSupported(VmConfigFault): ...


class MemorySizeNotRecommended(VirtualHardwareCompatibilityIssue):
    @property
    def memorySizeMB(self) -> int: ...
    @property
    def minMemorySizeMB(self) -> int: ...
    @property
    def maxMemorySizeMB(self) -> int: ...


class MemorySizeNotSupported(VirtualHardwareCompatibilityIssue):
    @property
    def memorySizeMB(self) -> int: ...
    @property
    def minMemorySizeMB(self) -> int: ...
    @property
    def maxMemorySizeMB(self) -> int: ...


class MemorySizeNotSupportedByDatastore(VirtualHardwareCompatibilityIssue):
    @property
    def datastore(self) -> vim.Datastore: ...
    @property
    def memorySizeMB(self) -> int: ...
    @property
    def maxMemorySizeMB(self) -> int: ...


class MemorySnapshotOnIndependentDisk(SnapshotFault): ...


class MethodAlreadyDisabledFault(vmodl.RuntimeFault):
    @property
    def sourceId(self) -> str: ...


class MethodDisabled(vmodl.RuntimeFault):
    @property
    def source(self) -> str: ...


class MigrationDisabled(MigrationFault): ...


class MigrationFault(VimFault): ...


class MigrationFeatureNotSupported(MigrationFault):
    @property
    def atSourceHost(self) -> bool: ...
    @property
    def failedHostName(self) -> str: ...
    @property
    def failedHost(self) -> vim.HostSystem: ...


class MigrationNotReady(MigrationFault):
    @property
    def reason(self) -> str: ...


class MismatchedBundle(VimFault):
    @property
    def bundleUuid(self) -> str: ...
    @property
    def hostUuid(self) -> str: ...
    @property
    def bundleBuildNumber(self) -> int: ...
    @property
    def hostBuildNumber(self) -> int: ...


class MismatchedNetworkPolicies(MigrationFault):
    @property
    def device(self) -> str: ...
    @property
    def backing(self) -> str: ...
    @property
    def connected(self) -> bool: ...


class MismatchedVMotionNetworkNames(MigrationFault):
    @property
    def sourceNetwork(self) -> str: ...
    @property
    def destNetwork(self) -> str: ...


class MissingBmcSupport(VimFault): ...


class MissingController(InvalidDeviceSpec): ...


class MissingIpPool(VAppPropertyFault): ...


class MissingLinuxCustResources(CustomizationFault): ...


class MissingNetworkIpConfig(VAppPropertyFault): ...


class MissingPowerOffConfiguration(VAppConfigFault): ...


class MissingPowerOnConfiguration(VAppConfigFault): ...


class MissingWindowsCustResources(CustomizationFault): ...


class MksConnectionLimitReached(InvalidState):
    @property
    def connectionLimit(self) -> int: ...


class MountError(CustomizationFault):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def diskIndex(self) -> int: ...


class MultiWriterNotSupported(DeviceNotSupported): ...


class MultipleCertificatesVerifyFault(HostConnectFault):
    @property
    def thumbprintData(self) -> List[MultipleCertificatesVerifyFault.ThumbprintData]: ...


    class ThumbprintData(vmodl.DynamicData):
        @property
        def port(self) -> int: ...
        @property
        def thumbprint(self) -> str: ...


class MultipleSnapshotsNotSupported(SnapshotFault): ...


class NamespaceFull(VimFault):
    @property
    def name(self) -> str: ...
    @property
    def currentMaxSize(self) -> long: ...
    @property
    def requiredSize(self) -> long: ...


class NamespaceLimitReached(VimFault):
    @property
    def limit(self) -> int: ...


class NamespaceWriteProtected(VimFault):
    @property
    def name(self) -> str: ...


class NasConfigFault(HostConfigFault):
    @property
    def name(self) -> str: ...


class NasConnectionLimitReached(NasConfigFault):
    @property
    def remoteHost(self) -> str: ...
    @property
    def remotePath(self) -> str: ...


class NasSessionCredentialConflict(NasConfigFault):
    @property
    def remoteHost(self) -> str: ...
    @property
    def remotePath(self) -> str: ...
    @property
    def userName(self) -> str: ...


class NasVolumeNotMounted(NasConfigFault):
    @property
    def remoteHost(self) -> str: ...
    @property
    def remotePath(self) -> str: ...


class NetworkCopyFault(FileFault): ...


class NetworkDisruptedAndConfigRolledBack(VimFault):
    @property
    def host(self) -> str: ...


class NetworkInaccessible(NasConfigFault): ...


class NetworksMayNotBeTheSame(MigrationFault):
    @property
    def name(self) -> str: ...


class NicSettingMismatch(CustomizationFault):
    @property
    def numberOfNicsInSpec(self) -> int: ...
    @property
    def numberOfNicsInVM(self) -> int: ...


class NoActiveHostInCluster(InvalidState):
    @property
    def computeResource(self) -> vim.ComputeResource: ...


class NoAvailableIp(VAppPropertyFault):
    @property
    def network(self) -> vim.Network: ...


class NoClientCertificate(VimFault): ...


class NoCompatibleDatastore(VimFault): ...


class NoCompatibleHardAffinityHost(VmConfigFault):
    @property
    def vmName(self) -> str: ...


class NoCompatibleHost(VimFault):
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @property
    def error(self) -> List[vmodl.MethodFault]: ...


class NoCompatibleHostWithAccessToDevice(NoCompatibleHost): ...


class NoCompatibleSoftAffinityHost(VmConfigFault):
    @property
    def vmName(self) -> str: ...


class NoConnectedDatastore(VimFault): ...


class NoDiskFound(VimFault): ...


class NoDiskSpace(FileFault):
    @property
    def datastore(self) -> str: ...


class NoDisksToCustomize(CustomizationFault): ...


class NoGateway(HostConfigFault): ...


class NoGuestHeartbeat(MigrationFault): ...


class NoHost(HostConnectFault):
    @property
    def name(self) -> str: ...


class NoHostSuitableForFtSecondary(VmFaultToleranceIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def vmName(self) -> str: ...


class NoLicenseServerConfigured(NotEnoughLicenses): ...


class NoPeerHostFound(HostPowerOpFailed): ...


class NoPermission(SecurityError):
    @property
    def object(self) -> ManagedObject: ...
    @property
    def privilegeId(self) -> str: ...
    @property
    def missingPrivileges(self) -> List[NoPermission.EntityPrivileges]: ...


    class EntityPrivileges(vmodl.DynamicData):
        @property
        def entity(self) -> ManagedObject: ...
        @property
        def privilegeIds(self) -> List[str]: ...


class NoPermissionOnAD(ActiveDirectoryFault): ...


class NoPermissionOnHost(HostConnectFault): ...


class NoPermissionOnNasVolume(NasConfigFault):
    @property
    def userName(self) -> str: ...


class NoSubjectName(VimFault): ...


class NoVcManagedIpConfigured(VAppPropertyFault): ...


class NoVirtualNic(HostConfigFault): ...


class NoVmInVApp(VAppConfigFault): ...


class NonADUserRequired(ActiveDirectoryFault): ...


class NonHomeRDMVMotionNotSupported(MigrationFeatureNotSupported):
    @property
    def device(self) -> str: ...


class NonPersistentDisksNotSupported(DeviceNotSupported): ...


class NonVmwareOuiMacNotSupportedHost(NotSupportedHost):
    @property
    def hostName(self) -> str: ...


class NotADirectory(FileFault): ...


class NotAFile(FileFault): ...


class NotAuthenticated(NoPermission): ...


class NotEnoughCpus(VirtualHardwareCompatibilityIssue):
    @property
    def numCpuDest(self) -> int: ...
    @property
    def numCpuVm(self) -> int: ...


class NotEnoughLogicalCpus(NotEnoughCpus):
    @property
    def host(self) -> vim.HostSystem: ...


class NotFound(VimFault): ...


class NotSupportedDeviceForFT(VmFaultToleranceIssue):
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def hostName(self) -> str: ...
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def vmName(self) -> str: ...
    @property
    def deviceType(self) -> str: ...
    @property
    def deviceLabel(self) -> str: ...


    class DeviceType(Enum):
        virtualVmxnet3 = "virtualVmxnet3"
        paraVirtualSCSIController = "paraVirtualSCSIController"


class NotSupportedHost(HostConnectFault):
    @property
    def productName(self) -> str: ...
    @property
    def productVersion(self) -> str: ...


class NotSupportedHostForChecksum(VimFault): ...


class NotSupportedHostForVFlash(NotSupportedHost):
    @property
    def hostName(self) -> str: ...


class NotSupportedHostForVmcp(NotSupportedHost):
    @property
    def hostName(self) -> str: ...


class NotSupportedHostForVmemFile(NotSupportedHost):
    @property
    def hostName(self) -> str: ...


class NotSupportedHostForVsan(NotSupportedHost):
    @property
    def hostName(self) -> str: ...


class NotSupportedHostInCluster(NotSupportedHost): ...


class NotSupportedHostInDvs(NotSupportedHost):
    @property
    def switchProductSpec(self) -> vim.dvs.ProductSpec: ...


class NotSupportedHostInHACluster(NotSupportedHost):
    @property
    def hostName(self) -> str: ...
    @property
    def build(self) -> str: ...


class NotUserConfigurableProperty(VAppPropertyFault): ...


class NumVirtualCoresPerSocketNotSupported(VirtualHardwareCompatibilityIssue):
    @property
    def maxSupportedCoresPerSocketDest(self) -> int: ...
    @property
    def numCoresPerSocketVm(self) -> int: ...


class NumVirtualCpusExceedsLimit(InsufficientResourcesFault):
    @property
    def maxSupportedVcpus(self) -> int: ...


class NumVirtualCpusIncompatible(VmConfigFault):
    @property
    def reason(self) -> str: ...
    @property
    def numCpu(self) -> int: ...


class NumVirtualCpusNotSupported(VirtualHardwareCompatibilityIssue):
    @property
    def maxSupportedVcpusDest(self) -> int: ...
    @property
    def numCpuVm(self) -> int: ...


class OperationDisabledByGuest(GuestOperationsFault): ...


class OperationDisallowedOnHost(vmodl.RuntimeFault): ...


class OperationNotSupportedByGuest(GuestOperationsFault): ...


class OutOfBounds(VimFault):
    @property
    def argumentName(self) -> PropertyPath: ...


class OvfAttribute(OvfInvalidPackage):
    @property
    def elementName(self) -> str: ...
    @property
    def attributeName(self) -> str: ...


class OvfConnectedDevice(OvfHardwareExport): ...


class OvfConnectedDeviceFloppy(OvfConnectedDevice):
    @property
    def filename(self) -> str: ...


class OvfConnectedDeviceIso(OvfConnectedDevice):
    @property
    def filename(self) -> str: ...


class OvfConstraint(OvfInvalidPackage):
    @property
    def name(self) -> str: ...


class OvfConsumerCallbackFault(OvfFault):
    @property
    def extensionKey(self) -> str: ...
    @property
    def extensionName(self) -> str: ...


class OvfConsumerCommunicationError(OvfConsumerCallbackFault):
    @property
    def description(self) -> str: ...


class OvfConsumerFault(OvfConsumerCallbackFault):
    @property
    def errorKey(self) -> str: ...
    @property
    def message(self) -> str: ...
    @property
    def params(self) -> List[vim.KeyValue]: ...


class OvfConsumerInvalidSection(OvfConsumerCallbackFault):
    @property
    def lineNumber(self) -> int: ...
    @property
    def description(self) -> str: ...


class OvfConsumerPowerOnFault(InvalidState):
    @property
    def extensionKey(self) -> str: ...
    @property
    def extensionName(self) -> str: ...
    @property
    def description(self) -> str: ...


class OvfConsumerUndeclaredSection(OvfConsumerCallbackFault):
    @property
    def qualifiedSectionType(self) -> str: ...


class OvfConsumerUndefinedPrefix(OvfConsumerCallbackFault):
    @property
    def prefix(self) -> str: ...


class OvfConsumerValidationFault(VmConfigFault):
    @property
    def extensionKey(self) -> str: ...
    @property
    def extensionName(self) -> str: ...
    @property
    def message(self) -> str: ...


class OvfCpuCompatibility(OvfImport):
    @property
    def registerName(self) -> str: ...
    @property
    def level(self) -> int: ...
    @property
    def registerValue(self) -> str: ...
    @property
    def desiredRegisterValue(self) -> str: ...


class OvfCpuCompatibilityCheckNotSupported(OvfImport): ...


class OvfDiskMappingNotFound(OvfSystemFault):
    @property
    def diskName(self) -> str: ...
    @property
    def vmName(self) -> str: ...


class OvfDiskOrderConstraint(OvfConstraint): ...


class OvfDuplicateElement(OvfElement): ...


class OvfDuplicatedElementBoundary(OvfElement):
    @property
    def boundary(self) -> str: ...


class OvfDuplicatedPropertyIdExport(OvfExport):
    @property
    def fqid(self) -> str: ...


class OvfDuplicatedPropertyIdImport(OvfExport): ...


class OvfElement(OvfInvalidPackage):
    @property
    def name(self) -> str: ...


class OvfElementInvalidValue(OvfElement):
    @property
    def value(self) -> str: ...


class OvfExport(OvfFault): ...


class OvfExportFailed(OvfExport): ...


class OvfFault(VimFault): ...


class OvfHardwareCheck(OvfImport): ...


class OvfHardwareExport(OvfExport):
    @property
    def device(self) -> vim.vm.device.VirtualDevice: ...
    @property
    def vmPath(self) -> str: ...


class OvfHostResourceConstraint(OvfConstraint):
    @property
    def value(self) -> str: ...


class OvfHostValueNotParsed(OvfSystemFault):
    @property
    def property(self) -> str: ...
    @property
    def value(self) -> str: ...


class OvfImport(OvfFault): ...


class OvfImportFailed(OvfImport): ...


class OvfInternalError(OvfSystemFault): ...


class OvfInvalidPackage(OvfFault):
    @property
    def lineNumber(self) -> int: ...


class OvfInvalidValue(OvfAttribute):
    @property
    def value(self) -> str: ...


class OvfInvalidValueConfiguration(OvfInvalidValue): ...


class OvfInvalidValueEmpty(OvfInvalidValue): ...


class OvfInvalidValueFormatMalformed(OvfInvalidValue): ...


class OvfInvalidValueReference(OvfInvalidValue): ...


class OvfInvalidVmName(OvfUnsupportedPackage):
    @property
    def name(self) -> str: ...


class OvfMappedOsId(OvfImport):
    @property
    def ovfId(self) -> int: ...
    @property
    def ovfDescription(self) -> str: ...
    @property
    def targetDescription(self) -> str: ...


class OvfMissingAttribute(OvfAttribute): ...


class OvfMissingElement(OvfElement): ...


class OvfMissingElementNormalBoundary(OvfMissingElement):
    @property
    def boundary(self) -> str: ...


class OvfMissingHardware(OvfImport):
    @property
    def name(self) -> str: ...
    @property
    def resourceType(self) -> int: ...


class OvfNetworkMappingNotSupported(OvfImport): ...


class OvfNoHostNic(OvfUnsupportedPackage): ...


class OvfNoSpaceOnController(OvfUnsupportedElement):
    @property
    def parent(self) -> str: ...


class OvfNoSupportedHardwareFamily(OvfUnsupportedPackage):
    @property
    def version(self) -> str: ...


class OvfProperty(OvfInvalidPackage):
    @property
    def type(self) -> str: ...
    @property
    def value(self) -> str: ...


class OvfPropertyExport(OvfExport):
    @property
    def type(self) -> str: ...
    @property
    def value(self) -> str: ...


class OvfPropertyNetwork(OvfProperty): ...


class OvfPropertyNetworkExport(OvfExport):
    @property
    def network(self) -> str: ...


class OvfPropertyQualifier(OvfProperty):
    @property
    def qualifier(self) -> str: ...


class OvfPropertyQualifierDuplicate(OvfProperty):
    @property
    def qualifier(self) -> str: ...


class OvfPropertyQualifierIgnored(OvfProperty):
    @property
    def qualifier(self) -> str: ...


class OvfPropertyType(OvfProperty): ...


class OvfPropertyValue(OvfProperty): ...


class OvfSystemFault(OvfFault): ...


class OvfToXmlUnsupportedElement(OvfSystemFault):
    @property
    def name(self) -> str: ...


class OvfUnableToExportDisk(OvfHardwareExport):
    @property
    def diskName(self) -> str: ...


class OvfUnexpectedElement(OvfElement): ...


class OvfUnknownDevice(OvfSystemFault):
    @property
    def device(self) -> vim.vm.device.VirtualDevice: ...
    @property
    def vmName(self) -> str: ...


class OvfUnknownDeviceBacking(OvfHardwareExport):
    @property
    def backing(self) -> vim.vm.device.VirtualDevice.BackingInfo: ...


class OvfUnknownEntity(OvfSystemFault):
    @property
    def lineNumber(self) -> int: ...


class OvfUnsupportedAttribute(OvfUnsupportedPackage):
    @property
    def elementName(self) -> str: ...
    @property
    def attributeName(self) -> str: ...


class OvfUnsupportedAttributeValue(OvfUnsupportedAttribute):
    @property
    def value(self) -> str: ...


class OvfUnsupportedDeviceBackingInfo(OvfSystemFault):
    @property
    def elementName(self) -> str: ...
    @property
    def instanceId(self) -> str: ...
    @property
    def deviceName(self) -> str: ...
    @property
    def backingName(self) -> str: ...


class OvfUnsupportedDeviceBackingOption(OvfSystemFault):
    @property
    def elementName(self) -> str: ...
    @property
    def instanceId(self) -> str: ...
    @property
    def deviceName(self) -> str: ...
    @property
    def backingName(self) -> str: ...


class OvfUnsupportedDeviceExport(OvfHardwareExport): ...


class OvfUnsupportedDiskProvisioning(OvfImport):
    @property
    def diskProvisioning(self) -> str: ...
    @property
    def supportedDiskProvisioning(self) -> str: ...


class OvfUnsupportedElement(OvfUnsupportedPackage):
    @property
    def name(self) -> str: ...


class OvfUnsupportedElementValue(OvfUnsupportedElement):
    @property
    def value(self) -> str: ...


class OvfUnsupportedPackage(OvfFault):
    @property
    def lineNumber(self) -> int: ...


class OvfUnsupportedSection(OvfUnsupportedElement):
    @property
    def info(self) -> str: ...


class OvfUnsupportedSubType(OvfUnsupportedPackage):
    @property
    def elementName(self) -> str: ...
    @property
    def instanceId(self) -> str: ...
    @property
    def deviceType(self) -> int: ...
    @property
    def deviceSubType(self) -> str: ...


class OvfUnsupportedType(OvfUnsupportedPackage):
    @property
    def name(self) -> str: ...
    @property
    def instanceId(self) -> str: ...
    @property
    def deviceType(self) -> int: ...


class OvfWrongElement(OvfElement): ...


class OvfWrongNamespace(OvfInvalidPackage):
    @property
    def namespaceName(self) -> str: ...


class OvfXmlFormat(OvfInvalidPackage):
    @property
    def description(self) -> str: ...


class PasswordExpired(InvalidLogin): ...


class PatchAlreadyInstalled(PatchNotApplicable): ...


class PatchBinariesNotFound(VimFault):
    @property
    def patchID(self) -> str: ...
    @property
    def binary(self) -> List[str]: ...


class PatchInstallFailed(PlatformConfigFault):
    @property
    def rolledBack(self) -> bool: ...


class PatchIntegrityError(PlatformConfigFault): ...


class PatchMetadataCorrupted(PatchMetadataInvalid): ...


class PatchMetadataInvalid(VimFault):
    @property
    def patchID(self) -> str: ...
    @property
    def metaData(self) -> List[str]: ...


class PatchMetadataNotFound(PatchMetadataInvalid): ...


class PatchMissingDependencies(PatchNotApplicable):
    @property
    def prerequisitePatch(self) -> List[str]: ...
    @property
    def prerequisiteLib(self) -> List[str]: ...


class PatchNotApplicable(VimFault):
    @property
    def patchID(self) -> str: ...


class PatchSuperseded(PatchNotApplicable):
    @property
    def supersede(self) -> List[str]: ...


class PhysCompatRDMNotSupported(RDMNotSupported): ...


class PlatformConfigFault(HostConfigFault):
    @property
    def text(self) -> str: ...


class PowerOnFtSecondaryFailed(VmFaultToleranceIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def vmName(self) -> str: ...
    @property
    def hostSelectionBy(self) -> FtIssuesOnHost.HostSelectionType: ...
    @property
    def hostErrors(self) -> List[vmodl.MethodFault]: ...
    @property
    def rootCause(self) -> vmodl.MethodFault: ...


class PowerOnFtSecondaryTimedout(Timedout):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def vmName(self) -> str: ...
    @property
    def timeout(self) -> int: ...


class ProfileUpdateFailed(VimFault):
    @property
    def failure(self) -> List[ProfileUpdateFailed.UpdateFailure]: ...
    @property
    def warnings(self) -> List[ProfileUpdateFailed.UpdateFailure]: ...


    class UpdateFailure(vmodl.DynamicData):
        @property
        def profilePath(self) -> vim.profile.ProfilePropertyPath: ...
        @property
        def errMsg(self) -> vmodl.LocalizableMessage: ...


class QuarantineModeFault(VmConfigFault):
    @property
    def vmName(self) -> str: ...
    @property
    def faultType(self) -> str: ...


    class FaultType(Enum):
        NoCompatibleNonQuarantinedHost = "NoCompatibleNonQuarantinedHost"
        CorrectionDisallowed = "CorrectionDisallowed"
        CorrectionImpact = "CorrectionImpact"


class QuestionPending(InvalidState):
    @property
    def text(self) -> str: ...


class QuiesceDatastoreIOForHAFailed(ResourceInUse):
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def hostName(self) -> str: ...
    @property
    def ds(self) -> vim.Datastore: ...
    @property
    def dsName(self) -> str: ...


class RDMConversionNotSupported(MigrationFault):
    @property
    def device(self) -> str: ...


class RDMNotPreserved(MigrationFault):
    @property
    def device(self) -> str: ...


class RDMNotSupported(DeviceNotSupported): ...


class RDMNotSupportedOnDatastore(VmConfigFault):
    @property
    def device(self) -> str: ...
    @property
    def datastore(self) -> vim.Datastore: ...
    @property
    def datastoreName(self) -> str: ...


class RDMPointsToInaccessibleDisk(CannotAccessVmDisk): ...


class RawDiskNotSupported(DeviceNotSupported): ...


class ReadHostResourcePoolTreeFailed(HostConnectFault): ...


class ReadOnlyDisksWithLegacyDestination(MigrationFault):
    @property
    def roDiskCount(self) -> int: ...
    @property
    def timeoutDanger(self) -> bool: ...


class RebootRequired(VimFault):
    @property
    def patch(self) -> str: ...


class RecordReplayDisabled(VimFault): ...


class RemoteDeviceNotSupported(DeviceNotSupported): ...


class RemoveFailed(VimFault): ...


class ReplicationConfigFault(ReplicationFault): ...


class ReplicationDiskConfigFault(ReplicationConfigFault):
    @property
    def reason(self) -> str: ...
    @property
    def vmRef(self) -> vim.VirtualMachine: ...
    @property
    def key(self) -> int: ...


    class ReasonForFault(Enum):
        diskNotFound = "diskNotFound"
        diskTypeNotSupported = "diskTypeNotSupported"
        invalidDiskKey = "invalidDiskKey"
        invalidDiskReplicationId = "invalidDiskReplicationId"
        duplicateDiskReplicationId = "duplicateDiskReplicationId"
        invalidPersistentFilePath = "invalidPersistentFilePath"
        reconfigureDiskReplicationIdNotAllowed = "reconfigureDiskReplicationIdNotAllowed"


class ReplicationFault(VimFault): ...


class ReplicationIncompatibleWithFT(ReplicationFault): ...


class ReplicationInvalidOptions(ReplicationFault):
    @property
    def options(self) -> str: ...
    @property
    def entity(self) -> vim.ManagedEntity: ...


class ReplicationNotSupportedOnHost(ReplicationFault): ...


class ReplicationVmConfigFault(ReplicationConfigFault):
    @property
    def reason(self) -> str: ...
    @property
    def vmRef(self) -> vim.VirtualMachine: ...


class ReplicationVmFault(ReplicationFault):
    @property
    def reason(self) -> str: ...
    @property
    def state(self) -> str: ...
    @property
    def instanceId(self) -> str: ...
    @property
    def vm(self) -> vim.VirtualMachine: ...


class ReplicationVmInProgressFault(ReplicationVmFault):
    @property
    def requestedActivity(self) -> str: ...
    @property
    def inProgressActivity(self) -> str: ...


    class Activity(Enum):
        fullSync = "fullSync"
        delta = "delta"


class ResourceInUse(VimFault):
    @property
    def type(self) -> type: ...
    @property
    def name(self) -> str: ...


class ResourceNotAvailable(VimFault):
    @property
    def containerType(self) -> type: ...
    @property
    def containerName(self) -> str: ...
    @property
    def type(self) -> type: ...


class RestrictedByAdministrator(vmodl.RuntimeFault):
    @property
    def details(self) -> str: ...


class RestrictedVersion(SecurityError): ...


class RollbackFailure(DvsFault):
    @property
    def entityName(self) -> str: ...
    @property
    def entityType(self) -> str: ...


class RuleViolation(VmConfigFault):
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def rule(self) -> vim.cluster.RuleInfo: ...


class SSLDisabledFault(HostConnectFault): ...


class SSLVerifyFault(HostConnectFault):
    @property
    def selfSigned(self) -> bool: ...
    @property
    def thumbprint(self) -> str: ...


class SSPIChallenge(VimFault):
    @property
    def base64Token(self) -> str: ...


class SecondaryVmAlreadyDisabled(VmFaultToleranceIssue):
    @property
    def instanceUuid(self) -> str: ...


class SecondaryVmAlreadyEnabled(VmFaultToleranceIssue):
    @property
    def instanceUuid(self) -> str: ...


class SecondaryVmAlreadyRegistered(VmFaultToleranceIssue):
    @property
    def instanceUuid(self) -> str: ...


class SecondaryVmNotRegistered(VmFaultToleranceIssue):
    @property
    def instanceUuid(self) -> str: ...


class SharedBusControllerNotSupported(DeviceNotSupported): ...


class ShrinkDiskFault(VimFault):
    @property
    def diskId(self) -> int: ...


class SnapshotCloneNotSupported(SnapshotCopyNotSupported): ...


class SnapshotCopyNotSupported(MigrationFault): ...


class SnapshotDisabled(SnapshotFault): ...


class SnapshotFault(VimFault): ...


class SnapshotIncompatibleDeviceInVm(SnapshotFault):
    @property
    def fault(self) -> vmodl.MethodFault: ...


class SnapshotLocked(SnapshotFault): ...


class SnapshotMoveFromNonHomeNotSupported(SnapshotCopyNotSupported): ...


class SnapshotMoveNotSupported(SnapshotCopyNotSupported): ...


class SnapshotMoveToNonHomeNotSupported(SnapshotCopyNotSupported): ...


class SnapshotNoChange(SnapshotFault): ...


class SnapshotRevertIssue(MigrationFault):
    @property
    def snapshotName(self) -> str: ...
    @property
    def event(self) -> List[vim.event.Event]: ...
    @property
    def errors(self) -> bool: ...


class SoftRuleVioCorrectionDisallowed(VmConfigFault):
    @property
    def vmName(self) -> str: ...


class SoftRuleVioCorrectionImpact(VmConfigFault):
    @property
    def vmName(self) -> str: ...


class SolutionUserRequired(SecurityError): ...


class SsdDiskNotAvailable(VimFault):
    @property
    def devicePath(self) -> str: ...


class StorageDrsCannotMoveDiskInMultiWriterMode(VimFault): ...


class StorageDrsCannotMoveFTVm(VimFault): ...


class StorageDrsCannotMoveIndependentDisk(VimFault): ...


class StorageDrsCannotMoveManuallyPlacedSwapFile(VimFault): ...


class StorageDrsCannotMoveManuallyPlacedVm(VimFault): ...


class StorageDrsCannotMoveSharedDisk(VimFault): ...


class StorageDrsCannotMoveTemplate(VimFault): ...


class StorageDrsCannotMoveVmInUserFolder(VimFault): ...


class StorageDrsCannotMoveVmWithMountedCDROM(VimFault): ...


class StorageDrsCannotMoveVmWithNoFilesInLayout(VimFault): ...


class StorageDrsDatacentersCannotShareDatastore(VimFault): ...


class StorageDrsDisabledOnVm(VimFault): ...


class StorageDrsHbrDiskNotMovable(VimFault):
    @property
    def nonMovableDiskIds(self) -> str: ...


class StorageDrsHmsMoveInProgress(VimFault): ...


class StorageDrsHmsUnreachable(VimFault): ...


class StorageDrsIolbDisabledInternally(VimFault): ...


class StorageDrsRelocateDisabled(VimFault): ...


class StorageDrsStaleHmsCollection(VimFault): ...


class StorageDrsUnableToMoveFiles(VimFault): ...


class StorageVMotionNotSupported(MigrationFeatureNotSupported): ...


class StorageVmotionIncompatible(VirtualHardwareCompatibilityIssue):
    @property
    def datastore(self) -> vim.Datastore: ...


class SuspendedRelocateNotSupported(MigrationFault): ...


class SwapDatastoreNotWritableOnHost(DatastoreNotWritableOnHost): ...


class SwapDatastoreUnset(VimFault): ...


class SwapPlacementOverrideNotSupported(InvalidVmConfig): ...


class SwitchIpUnset(DvsFault): ...


class SwitchNotInUpgradeMode(DvsFault): ...


class TaskInProgress(VimFault):
    @property
    def task(self) -> vim.Task: ...


class ThirdPartyLicenseAssignmentFailed(vmodl.RuntimeFault):
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def module(self) -> str: ...
    @property
    def reason(self) -> str: ...


class Timedout(VimFault): ...


class TooManyConcurrentNativeClones(FileFault): ...


class TooManyConsecutiveOverrides(VimFault): ...


class TooManyDevices(InvalidVmConfig): ...


class TooManyDisksOnLegacyHost(MigrationFault):
    @property
    def diskCount(self) -> int: ...
    @property
    def timeoutDanger(self) -> bool: ...


class TooManyGuestLogons(GuestOperationsFault): ...


class TooManyHosts(HostConnectFault): ...


class TooManyNativeCloneLevels(FileFault): ...


class TooManyNativeClonesOnFile(FileFault): ...


class TooManySnapshotLevels(SnapshotFault): ...


class ToolsAlreadyUpgraded(VmToolsUpgradeFault): ...


class ToolsAutoUpgradeNotSupported(VmToolsUpgradeFault): ...


class ToolsImageCopyFailed(VmToolsUpgradeFault): ...


class ToolsImageNotAvailable(VmToolsUpgradeFault): ...


class ToolsImageSignatureCheckFailed(VmToolsUpgradeFault): ...


class ToolsInstallationInProgress(MigrationFault): ...


class ToolsUnavailable(VimFault): ...


class ToolsUpgradeCancelled(VmToolsUpgradeFault): ...


class UnSupportedDatastoreForVFlash(UnsupportedDatastore):
    @property
    def datastoreName(self) -> str: ...
    @property
    def type(self) -> str: ...


class UncommittedUndoableDisk(MigrationFault): ...


class UnconfiguredPropertyValue(InvalidPropertyValue): ...


class UncustomizableGuest(CustomizationFault):
    @property
    def uncustomizableGuestOS(self) -> str: ...


class UnexpectedCustomizationFault(CustomizationFault): ...


class UnrecognizedHost(VimFault):
    @property
    def hostName(self) -> str: ...


class UnsharedSwapVMotionNotSupported(MigrationFeatureNotSupported): ...


class UnsupportedDatastore(VmConfigFault):
    @property
    def datastore(self) -> vim.Datastore: ...


class UnsupportedGuest(InvalidVmConfig):
    @property
    def unsupportedGuestOS(self) -> str: ...


class UnsupportedVimApiVersion(VimFault):
    @property
    def version(self) -> str: ...


class UnsupportedVmxLocation(VmConfigFault): ...


class UnusedVirtualDiskBlocksNotScrubbed(DeviceBackingNotSupported): ...


class UserNotFound(VimFault):
    @property
    def principal(self) -> str: ...
    @property
    def unresolved(self) -> bool: ...


class VAppConfigFault(VimFault): ...


class VAppNotRunning(VmConfigFault): ...


class VAppOperationInProgress(vmodl.RuntimeFault): ...


class VAppPropertyFault(VmConfigFault):
    @property
    def id(self) -> str: ...
    @property
    def category(self) -> str: ...
    @property
    def label(self) -> str: ...
    @property
    def type(self) -> str: ...
    @property
    def value(self) -> str: ...


class VAppTaskInProgress(TaskInProgress): ...


class VFlashCacheHotConfigNotSupported(VmConfigFault): ...


class VFlashModuleNotSupported(VmConfigFault):
    @property
    def vmName(self) -> str: ...
    @property
    def moduleName(self) -> str: ...
    @property
    def reason(self) -> str: ...
    @property
    def hostName(self) -> str: ...


class VFlashModuleVersionIncompatible(VimFault):
    @property
    def moduleName(self) -> str: ...
    @property
    def vmRequestModuleVersion(self) -> str: ...
    @property
    def hostMinSupportedVerson(self) -> str: ...
    @property
    def hostModuleVersion(self) -> str: ...


class VMINotSupported(DeviceNotSupported): ...


class VMOnConflictDVPort(CannotAccessNetwork): ...


class VMOnVirtualIntranet(CannotAccessNetwork): ...


class VMotionAcrossNetworkNotSupported(MigrationFeatureNotSupported): ...


class VMotionInterfaceIssue(MigrationFault):
    @property
    def atSourceHost(self) -> bool: ...
    @property
    def failedHost(self) -> str: ...
    @property
    def failedHostEntity(self) -> vim.HostSystem: ...


class VMotionLinkCapacityLow(VMotionInterfaceIssue):
    @property
    def network(self) -> str: ...


class VMotionLinkDown(VMotionInterfaceIssue):
    @property
    def network(self) -> str: ...


class VMotionNotConfigured(VMotionInterfaceIssue): ...


class VMotionNotLicensed(VMotionInterfaceIssue): ...


class VMotionNotSupported(VMotionInterfaceIssue): ...


class VMotionProtocolIncompatible(MigrationFault): ...


class VimFault(vmodl.MethodFault): ...


class VirtualDiskBlocksNotFullyProvisioned(DeviceBackingNotSupported): ...


class VirtualDiskModeNotSupported(DeviceNotSupported):
    @property
    def mode(self) -> str: ...


class VirtualEthernetCardNotSupported(DeviceNotSupported): ...


class VirtualHardwareCompatibilityIssue(VmConfigFault): ...


class VirtualHardwareVersionNotSupported(VirtualHardwareCompatibilityIssue):
    @property
    def hostName(self) -> str: ...
    @property
    def host(self) -> vim.HostSystem: ...


class VmAlreadyExistsInDatacenter(InvalidFolder):
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def hostname(self) -> str: ...
    @property
    def vm(self) -> List[vim.VirtualMachine]: ...


class VmConfigFault(VimFault): ...


class VmConfigIncompatibleForFaultTolerance(VmConfigFault):
    @property
    def fault(self) -> vmodl.MethodFault: ...


class VmConfigIncompatibleForRecordReplay(VmConfigFault):
    @property
    def fault(self) -> vmodl.MethodFault: ...


class VmFaultToleranceConfigIssue(VmFaultToleranceIssue):
    @property
    def reason(self) -> str: ...
    @property
    def entityName(self) -> str: ...
    @property
    def entity(self) -> vim.ManagedEntity: ...


    class ReasonForIssue(Enum):
        haNotEnabled = "haNotEnabled"
        moreThanOneSecondary = "moreThanOneSecondary"
        recordReplayNotSupported = "recordReplayNotSupported"
        replayNotSupported = "replayNotSupported"
        templateVm = "templateVm"
        multipleVCPU = "multipleVCPU"
        hostInactive = "hostInactive"
        ftUnsupportedHardware = "ftUnsupportedHardware"
        ftUnsupportedProduct = "ftUnsupportedProduct"
        missingVMotionNic = "missingVMotionNic"
        missingFTLoggingNic = "missingFTLoggingNic"
        thinDisk = "thinDisk"
        verifySSLCertificateFlagNotSet = "verifySSLCertificateFlagNotSet"
        hasSnapshots = "hasSnapshots"
        noConfig = "noConfig"
        ftSecondaryVm = "ftSecondaryVm"
        hasLocalDisk = "hasLocalDisk"
        esxAgentVm = "esxAgentVm"
        video3dEnabled = "video3dEnabled"
        hasUnsupportedDisk = "hasUnsupportedDisk"
        insufficientBandwidth = "insufficientBandwidth"
        hasNestedHVConfiguration = "hasNestedHVConfiguration"
        hasVFlashConfiguration = "hasVFlashConfiguration"
        unsupportedProduct = "unsupportedProduct"
        cpuHvUnsupported = "cpuHvUnsupported"
        cpuHwmmuUnsupported = "cpuHwmmuUnsupported"
        cpuHvDisabled = "cpuHvDisabled"
        hasEFIFirmware = "hasEFIFirmware"
        tooManyVCPUs = "tooManyVCPUs"
        tooMuchMemory = "tooMuchMemory"
        vMotionNotLicensed = "vMotionNotLicensed"
        ftNotLicensed = "ftNotLicensed"
        haAgentIssue = "haAgentIssue"
        unsupportedSPBM = "unsupportedSPBM"
        hasLinkedCloneDisk = "hasLinkedCloneDisk"
        unsupportedPMemHAFailOver = "unsupportedPMemHAFailOver"
        unsupportedEncryptedDisk = "unsupportedEncryptedDisk"


class VmFaultToleranceConfigIssueWrapper(VmFaultToleranceIssue):
    @property
    def entityName(self) -> str: ...
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @property
    def error(self) -> vmodl.MethodFault: ...


class VmFaultToleranceInvalidFileBacking(VmFaultToleranceIssue):
    @property
    def backingType(self) -> str: ...
    @property
    def backingFilename(self) -> str: ...


class VmFaultToleranceIssue(VimFault): ...


class VmFaultToleranceOpIssuesList(VmFaultToleranceIssue):
    @property
    def errors(self) -> List[vmodl.MethodFault]: ...
    @property
    def warnings(self) -> List[vmodl.MethodFault]: ...


class VmFaultToleranceTooManyFtVcpusOnHost(InsufficientResourcesFault):
    @property
    def hostName(self) -> str: ...
    @property
    def maxNumFtVcpus(self) -> int: ...


class VmFaultToleranceTooManyVMsOnHost(InsufficientResourcesFault):
    @property
    def hostName(self) -> str: ...
    @property
    def maxNumFtVms(self) -> int: ...


class VmHostAffinityRuleViolation(VmConfigFault):
    @property
    def vmName(self) -> str: ...
    @property
    def hostName(self) -> str: ...


class VmLimitLicense(NotEnoughLicenses):
    @property
    def limit(self) -> int: ...


class VmMetadataManagerFault(VimFault): ...


class VmMonitorIncompatibleForFaultTolerance(VimFault): ...


class VmPowerOnDisabled(InvalidState): ...


class VmSmpFaultToleranceTooManyVMsOnHost(InsufficientResourcesFault):
    @property
    def hostName(self) -> str: ...
    @property
    def maxNumSmpFtVms(self) -> int: ...


class VmToolsUpgradeFault(VimFault): ...


class VmValidateMaxDevice(VimFault):
    @property
    def device(self) -> str: ...
    @property
    def max(self) -> int: ...
    @property
    def count(self) -> int: ...


class VmWwnConflict(InvalidVmConfig):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def name(self) -> str: ...
    @property
    def wwn(self) -> long: ...


class VmfsAlreadyMounted(VmfsMountFault): ...


class VmfsAmbiguousMount(VmfsMountFault): ...


class VmfsMountFault(HostConfigFault):
    @property
    def uuid(self) -> str: ...


class VmotionInterfaceNotEnabled(HostPowerOpFailed): ...


class VolumeEditorError(CustomizationFault): ...


class VramLimitLicense(NotEnoughLicenses):
    @property
    def limit(self) -> int: ...


class VsanClusterUuidMismatch(CannotMoveVsanEnabledHost):
    @property
    def hostClusterUuid(self) -> str: ...
    @property
    def destinationClusterUuid(self) -> str: ...


class VsanDiskFault(VsanFault):
    @property
    def device(self) -> str: ...


class VsanFault(VimFault): ...


class VsanIncompatibleDiskMapping(VsanDiskFault): ...


class VspanDestPortConflict(DvsFault):
    @property
    def vspanSessionKey1(self) -> str: ...
    @property
    def vspanSessionKey2(self) -> str: ...
    @property
    def portKey(self) -> str: ...


class VspanPortConflict(DvsFault):
    @property
    def vspanSessionKey1(self) -> str: ...
    @property
    def vspanSessionKey2(self) -> str: ...
    @property
    def portKey(self) -> str: ...


class VspanPortMoveFault(DvsFault):
    @property
    def srcPortgroupName(self) -> str: ...
    @property
    def destPortgroupName(self) -> str: ...
    @property
    def portKey(self) -> str: ...


class VspanPortPromiscChangeFault(DvsFault):
    @property
    def portKey(self) -> str: ...


class VspanPortgroupPromiscChangeFault(DvsFault):
    @property
    def portgroupName(self) -> str: ...


class VspanPortgroupTypeChangeFault(DvsFault):
    @property
    def portgroupName(self) -> str: ...


class VspanPromiscuousPortNotSupported(DvsFault):
    @property
    def vspanSessionKey(self) -> str: ...
    @property
    def portKey(self) -> str: ...


class VspanSameSessionPortConflict(DvsFault):
    @property
    def vspanSessionKey(self) -> str: ...
    @property
    def portKey(self) -> str: ...


class WakeOnLanNotSupported(VirtualHardwareCompatibilityIssue): ...


class WakeOnLanNotSupportedByVmotionNIC(HostPowerOpFailed): ...


class WillLoseHAProtection(MigrationFault):
    @property
    def resolution(self) -> str: ...


    class Resolution(Enum):
        svmotion = "svmotion"
        relocate = "relocate"


class WillModifyConfigCpuRequirements(MigrationFault): ...


class WillResetSnapshotDirectory(MigrationFault): ...


class WipeDiskFault(VimFault): ...