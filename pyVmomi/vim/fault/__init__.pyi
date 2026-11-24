# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.cluster
import pyVmomi.vim.cns
import pyVmomi.vim.dvs
import pyVmomi.vim.encryption
import pyVmomi.vim.event
import pyVmomi.vim.profile
import pyVmomi.vim.vm
import pyVmomi.vmodl.fault
import pyVmomi.vim.vm.device
import pyVmomi.vim.vm.guest



class ActiveDirectoryFault(VimFault):
   errorCode: _typing.Optional[int] = None


class ActiveVMsBlockingEVC(EVCConfigFault):
   evcMode: _typing.Optional[str] = None
   host: list[pyVmomi.vim.HostSystem] = []
   hostName: list[str] = []

class AdminDisabled(HostConfigFault):
   pass

class AdminNotDisabled(HostConfigFault):
   pass


class AffinityConfigured(MigrationFault):
   class Affinity(pyVmomi.VmomiSupport.Enum):
      memory: _typing.ClassVar['Affinity'] = 'memory'
      cpu: _typing.ClassVar['Affinity'] = 'cpu'

   configuredAffinity: list[str] = []


class AgentInstallFailed(HostConnectFault):
   class Reason(pyVmomi.VmomiSupport.Enum):
      NotEnoughSpaceOnDevice: _typing.ClassVar['Reason'] = 'NotEnoughSpaceOnDevice'
      PrepareToUpgradeFailed: _typing.ClassVar['Reason'] = 'PrepareToUpgradeFailed'
      AgentNotRunning: _typing.ClassVar['Reason'] = 'AgentNotRunning'
      AgentNotReachable: _typing.ClassVar['Reason'] = 'AgentNotReachable'
      InstallTimedout: _typing.ClassVar['Reason'] = 'InstallTimedout'
      SignatureVerificationFailed: _typing.ClassVar['Reason'] = 'SignatureVerificationFailed'
      AgentUploadFailed: _typing.ClassVar['Reason'] = 'AgentUploadFailed'
      AgentUploadTimedout: _typing.ClassVar['Reason'] = 'AgentUploadTimedout'
      UnknownInstallerError: _typing.ClassVar['Reason'] = 'UnknownInstallerError'

   reason: _typing.Optional[str] = None
   statusCode: _typing.Optional[int] = None
   installerOutput: _typing.Optional[str] = None

class AlreadyBeingManaged(HostConnectFault):
   ipAddress: str

class AlreadyConnected(HostConnectFault):
   name: str


class AlreadyExists(VimFault):
   name: _typing.Optional[str] = None

class AlreadyUpgraded(VimFault):
   pass


class AnswerFileUpdateFailed(VimFault):
   class UpdateFailure(pyVmomi.vmodl.DynamicData):
      userInputPath: pyVmomi.vim.profile.ProfilePropertyPath
      errMsg: pyVmomi.vmodl.LocalizableMessage

   failure: list[UpdateFailure] = []

class ApplicationQuiesceFault(SnapshotFault):
   pass

class AuthMinimumAdminPermission(VimFault):
   pass


class BackupBlobReadFailure(DvsFault):
   entityName: str
   entityType: str
   fault: pyVmomi.vmodl.MethodFault


class BackupBlobWriteFailure(DvsFault):
   entityName: str
   entityType: str
   fault: pyVmomi.vmodl.MethodFault

class BlockedByFirewall(HostConfigFault):
   pass

class CAMServerRefusedConnection(InvalidCAMServer):
   pass

class CannotAccessFile(FileFault):
   pass

class CannotAccessLocalSource(VimFault):
   pass


class CannotAccessNetwork(CannotAccessVmDevice):
   network: _typing.Optional[pyVmomi.vim.Network] = None

class CannotAccessVmComponent(VmConfigFault):
   pass


class CannotAccessVmConfig(CannotAccessVmComponent):
   reason: pyVmomi.vmodl.MethodFault

class CannotAccessVmDevice(CannotAccessVmComponent):
   device: str
   backing: str
   connected: bool


class CannotAccessVmDisk(CannotAccessVmDevice):
   fault: pyVmomi.vmodl.MethodFault

class CannotAddHostWithFTVmAsStandalone(HostConnectFault):
   pass

class CannotAddHostWithFTVmToDifferentCluster(HostConnectFault):
   pass

class CannotAddHostWithFTVmToNonHACluster(HostConnectFault):
   pass


class CannotChangeDrsBehaviorForFtSecondary(VmFaultToleranceIssue):
   vm: pyVmomi.vim.VirtualMachine
   vmName: str


class CannotChangeHaSettingsForFtSecondary(VmFaultToleranceIssue):
   vm: pyVmomi.vim.VirtualMachine
   vmName: str

class CannotChangeVsanClusterUuid(VsanFault):
   pass

class CannotChangeVsanNodeUuid(VsanFault):
   pass


class CannotComputeFTCompatibleHosts(VmFaultToleranceIssue):
   vm: pyVmomi.vim.VirtualMachine
   vmName: str

class CannotCreateFile(FileFault):
   pass

class CannotDecryptPasswords(CustomizationFault):
   pass

class CannotDeleteFile(FileFault):
   pass


class CannotDisableDrsOnClustersWithVApps(pyVmomi.vmodl.RuntimeFault):
   pass

class CannotDisableSnapshot(VmConfigFault):
   pass

class CannotDisconnectHostWithFaultToleranceVm(VimFault):
   hostName: str


class CannotEnableVmcpForCluster(VimFault):
   class Reason(pyVmomi.VmomiSupport.Enum):
      APDTimeoutDisabled: _typing.ClassVar['Reason'] = 'APDTimeoutDisabled'

   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   hostName: _typing.Optional[str] = None
   reason: _typing.Optional[str] = None

class CannotModifyConfigCpuRequirements(MigrationFault):
   pass


class CannotMoveFaultToleranceVm(VimFault):
   class MoveType(pyVmomi.VmomiSupport.Enum):
      resourcePool: _typing.ClassVar['MoveType'] = 'resourcePool'
      cluster: _typing.ClassVar['MoveType'] = 'cluster'

   moveType: str
   vmName: str

class CannotMoveHostWithFaultToleranceVm(VimFault):
   pass

class CannotMoveVmWithDeltaDisk(MigrationFault):
   device: str

class CannotMoveVmWithNativeDeltaDisk(MigrationFault):
   pass

class CannotMoveVsanEnabledHost(VsanFault):
   pass

class CannotPlaceWithoutPrerequisiteMoves(VimFault):
   pass


class CannotPowerOffVmInCluster(InvalidState):
   class Operation(pyVmomi.VmomiSupport.Enum):
      suspend: _typing.ClassVar['Operation'] = 'suspend'
      powerOff: _typing.ClassVar['Operation'] = 'powerOff'
      guestShutdown: _typing.ClassVar['Operation'] = 'guestShutdown'
      guestSuspend: _typing.ClassVar['Operation'] = 'guestSuspend'

   operation: str
   vm: pyVmomi.vim.VirtualMachine
   vmName: str

class CannotReconfigureVsanWhenHaEnabled(VsanFault):
   pass


class CannotUseNetwork(VmConfigFault):
   class Reason(pyVmomi.VmomiSupport.Enum):
      NetworkReservationNotSupported: _typing.ClassVar['Reason'] = 'NetworkReservationNotSupported'
      MismatchedNetworkPolicies: _typing.ClassVar['Reason'] = 'MismatchedNetworkPolicies'
      MismatchedDvsVersionOrVendor: _typing.ClassVar['Reason'] = 'MismatchedDvsVersionOrVendor'
      VMotionToUnsupportedNetworkType: _typing.ClassVar['Reason'] = 'VMotionToUnsupportedNetworkType'
      NetworkUnderMaintenance: _typing.ClassVar['Reason'] = 'NetworkUnderMaintenance'
      MismatchedEnsMode: _typing.ClassVar['Reason'] = 'MismatchedEnsMode'
      MismatchedRealTimeDvs: _typing.ClassVar['Reason'] = 'MismatchedRealTimeDvs'
      NsxNetworkAvailabilityDegraded: _typing.ClassVar['Reason'] = 'NsxNetworkAvailabilityDegraded'

   device: str
   backing: str
   connected: bool
   reason: str
   network: _typing.Optional[pyVmomi.vim.Network] = None

class ClockSkew(HostConfigFault):
   pass

class CloneFromSnapshotNotSupported(MigrationFault):
   pass


class CnsAlreadyRegisteredFault(CnsFault):
   volumeId: pyVmomi.vim.cns.VolumeId

class CnsFault(VimFault):
   reason: str


class CnsInCompatibleFault(CnsPlacementFault):
   errors: list[pyVmomi.vmodl.MethodFault] = []

class CnsMissingControllerFault(CnsFault):
   pass


class CnsMissingPrivilegeFault(CnsPlacementFault):
   privileges: list[str] = []


class CnsNotRegisteredFault(CnsFault):
   volumeId: pyVmomi.vim.cns.VolumeId

class CnsPlacementFault(CnsFault):
   pass

class CnsRankedLowerFault(CnsPlacementFault):
   pass


class CnsSnapshotNotFoundFault(CnsFault):
   volumeId: _typing.Optional[pyVmomi.vim.cns.VolumeId] = None
   SnapshotId: pyVmomi.vim.cns.SnapshotId


class CnsVolumeAlreadyExistsFault(CnsFault):
   volumeId: pyVmomi.vim.cns.VolumeId
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None


class CnsVolumeNotFoundFault(CnsFault):
   volumeId: pyVmomi.vim.cns.VolumeId

class CollectorAddressUnset(DvsFault):
   pass

class ConcurrentAccess(VimFault):
   pass


class ConflictingConfiguration(DvsFault):
   class Config(pyVmomi.vmodl.DynamicData):
      entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
      propertyPath: str

   configInConflict: list[Config] = []


class ConflictingDatastoreFound(pyVmomi.vmodl.RuntimeFault):
   name: str
   url: str


class ConnectedIso(OvfExport):
   cdrom: pyVmomi.vim.vm.device.VirtualCdrom
   filename: str

class CpuCompatibilityUnknown(CpuIncompatible):
   pass

class CpuHotPlugNotSupported(VmConfigFault):
   pass


class CpuIncompatible(VirtualHardwareCompatibilityIssue):
   level: int
   registerName: str
   registerBits: _typing.Optional[str] = None
   desiredBits: _typing.Optional[str] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None

class CpuIncompatible1ECX(CpuIncompatible):
   sse3: bool
   pclmulqdq: bool
   ssse3: bool
   sse41: bool
   sse42: bool
   aes: bool
   other: bool
   otherOnly: bool

class CpuIncompatible81EDX(CpuIncompatible):
   nx: bool
   ffxsr: bool
   rdtscp: bool
   lm: bool
   other: bool
   otherOnly: bool

class CustomizationFault(VimFault):
   pass

class CustomizationPending(CustomizationFault):
   pass

class DVPortNotSupported(DeviceBackingNotSupported):
   pass


class DasConfigFault(VimFault):
   class DasConfigFaultReason(pyVmomi.VmomiSupport.Enum):
      HostNetworkMisconfiguration: _typing.ClassVar['DasConfigFaultReason'] = 'HostNetworkMisconfiguration'
      HostMisconfiguration: _typing.ClassVar['DasConfigFaultReason'] = 'HostMisconfiguration'
      InsufficientPrivileges: _typing.ClassVar['DasConfigFaultReason'] = 'InsufficientPrivileges'
      NoPrimaryAgentAvailable: _typing.ClassVar['DasConfigFaultReason'] = 'NoPrimaryAgentAvailable'
      Other: _typing.ClassVar['DasConfigFaultReason'] = 'Other'
      NoDatastoresConfigured: _typing.ClassVar['DasConfigFaultReason'] = 'NoDatastoresConfigured'
      CreateConfigVvolFailed: _typing.ClassVar['DasConfigFaultReason'] = 'CreateConfigVvolFailed'
      VSanNotSupportedOnHost: _typing.ClassVar['DasConfigFaultReason'] = 'VSanNotSupportedOnHost'
      DasNetworkMisconfiguration: _typing.ClassVar['DasConfigFaultReason'] = 'DasNetworkMisconfiguration'
      SetDesiredImageSpecFailed: _typing.ClassVar['DasConfigFaultReason'] = 'SetDesiredImageSpecFailed'
      ApplyHAVibsOnClusterFailed: _typing.ClassVar['DasConfigFaultReason'] = 'ApplyHAVibsOnClusterFailed'

   reason: _typing.Optional[str] = None
   output: _typing.Optional[str] = None
   event: list[pyVmomi.vim.event.Event] = []


class DatabaseError(pyVmomi.vmodl.RuntimeFault):
   pass


class DatacenterMismatch(MigrationFault):
   class Argument(pyVmomi.vmodl.DynamicData):
      entity: pyVmomi.vim.ManagedEntity
      inputDatacenter: _typing.Optional[pyVmomi.vim.Datacenter] = None

   invalidArgument: list[Argument] = []
   expectedDatacenter: pyVmomi.vim.Datacenter


class DatastoreNotWritableOnHost(InvalidDatastore):
   host: pyVmomi.vim.HostSystem


class DeltaDiskFormatNotSupported(VmConfigFault):
   datastore: list[pyVmomi.vim.Datastore] = []
   deltaDiskFormat: str

class DestinationSwitchFull(CannotAccessNetwork):
   pass

class DestinationVsanDisabled(CannotMoveVsanEnabledHost):
   destinationCluster: str

class DeviceBackingNotSupported(DeviceNotSupported):
   backing: str

class DeviceControllerNotSupported(DeviceNotSupported):
   controller: str

class DeviceHotPlugNotSupported(InvalidDeviceSpec):
   pass

class DeviceNotFound(InvalidDeviceSpec):
   pass


class DeviceNotSupported(VirtualHardwareCompatibilityIssue):
   class Reason(pyVmomi.VmomiSupport.Enum):
      host: _typing.ClassVar['Reason'] = 'host'
      guest: _typing.ClassVar['Reason'] = 'guest'
      ft: _typing.ClassVar['Reason'] = 'ft'

   device: str
   reason: _typing.Optional[str] = None

class DeviceUnsupportedForVmPlatform(InvalidDeviceSpec):
   pass

class DeviceUnsupportedForVmVersion(InvalidDeviceSpec):
   currentVersion: str
   expectedVersion: str

class DigestNotSupported(DeviceNotSupported):
   pass

class DirectoryNotEmpty(FileFault):
   pass

class DisableAdminNotSupported(HostConfigFault):
   pass


class DisallowedChangeByService(pyVmomi.vmodl.RuntimeFault):
   class DisallowedChange(pyVmomi.VmomiSupport.Enum):
      hotExtendDisk: _typing.ClassVar['DisallowedChange'] = 'hotExtendDisk'

   serviceName: str
   disallowedChange: _typing.Optional[str] = None

class DisallowedDiskModeChange(InvalidDeviceSpec):
   pass


class DisallowedMigrationDeviceAttached(MigrationFault):
   fault: pyVmomi.vmodl.MethodFault


class DisallowedOperationOnFailoverHost(pyVmomi.vmodl.RuntimeFault):
   host: pyVmomi.vim.HostSystem
   hostname: str

class DisconnectedHostsBlockingEVC(EVCConfigFault):
   pass

class DiskHasPartitions(VsanDiskFault):
   pass

class DiskIsLastRemainingNonSSD(VsanDiskFault):
   pass

class DiskIsNonLocal(VsanDiskFault):
   pass

class DiskIsUSB(VsanDiskFault):
   pass

class DiskMoveTypeNotSupported(MigrationFault):
   pass

class DiskNotSupported(VirtualHardwareCompatibilityIssue):
   disk: int

class DiskTooSmall(VsanDiskFault):
   pass

class DomainNotFound(ActiveDirectoryFault):
   domainName: str

class DrsDisabledOnVm(VimFault):
   pass


class DrsVmotionIncompatibleFault(VirtualHardwareCompatibilityIssue):
   host: pyVmomi.vim.HostSystem

class DuplicateDisks(VsanDiskFault):
   pass


class DuplicateName(VimFault):
   name: str
   object: pyVmomi.VmomiSupport.ManagedObject

class DuplicateVsanNetworkInterface(VsanFault):
   device: str


class DvsApplyOperationFault(DvsFault):
   class FaultOnObject(pyVmomi.vmodl.DynamicData):
      objectId: str
      type: type
      fault: pyVmomi.vmodl.MethodFault

   objectFault: list[FaultOnObject] = []

class DvsFault(VimFault):
   pass


class DvsNotAuthorized(DvsFault):
   sessionExtensionKey: _typing.Optional[str] = None
   dvsExtensionKey: _typing.Optional[str] = None


class DvsOperationBulkFault(DvsFault):
   class FaultOnHost(pyVmomi.vmodl.DynamicData):
      host: pyVmomi.vim.HostSystem
      fault: pyVmomi.vmodl.MethodFault

   hostFault: list[FaultOnHost] = []


class DvsScopeViolated(DvsFault):
   scope: list[pyVmomi.vim.ManagedEntity] = []
   entity: pyVmomi.vim.ManagedEntity


class EVCAdmissionFailed(NotSupportedHostInCluster):
   faults: list[pyVmomi.vmodl.MethodFault] = []

class EVCAdmissionFailedCPUFeaturesForMode(EVCAdmissionFailed):
   currentEVCModeKey: str

class EVCAdmissionFailedCPUModel(EVCAdmissionFailed):
   pass

class EVCAdmissionFailedCPUModelForMode(EVCAdmissionFailed):
   currentEVCModeKey: str

class EVCAdmissionFailedCPUVendor(EVCAdmissionFailed):
   clusterCPUVendor: str
   hostCPUVendor: str

class EVCAdmissionFailedCPUVendorUnknown(EVCAdmissionFailed):
   pass

class EVCAdmissionFailedHostDisconnected(EVCAdmissionFailed):
   pass

class EVCAdmissionFailedHostSoftware(EVCAdmissionFailed):
   pass

class EVCAdmissionFailedHostSoftwareForMode(EVCAdmissionFailed):
   pass

class EVCAdmissionFailedVmActive(EVCAdmissionFailed):
   pass


class EVCConfigFault(VimFault):
   faults: list[pyVmomi.vmodl.MethodFault] = []

class EVCModeIllegalByVendor(EVCConfigFault):
   clusterCPUVendor: str
   modeCPUVendor: str


class EVCModeUnsupportedByHosts(EVCConfigFault):
   evcMode: _typing.Optional[str] = None
   host: list[pyVmomi.vim.HostSystem] = []
   hostName: list[str] = []


class EVCUnsupportedByHostHardware(EVCConfigFault):
   host: list[pyVmomi.vim.HostSystem] = []
   hostName: list[str] = []


class EVCUnsupportedByHostSoftware(EVCConfigFault):
   host: list[pyVmomi.vim.HostSystem] = []
   hostName: list[str] = []

class EightHostLimitViolated(VmConfigFault):
   pass


class EncryptionKeyRequired(InvalidState):
   requiredKey: list[pyVmomi.vim.encryption.CryptoKeyId] = []

class ExpiredAddonLicense(ExpiredFeatureLicense):
   pass

class ExpiredEditionLicense(ExpiredFeatureLicense):
   pass


class ExpiredFeatureLicense(pyVmomi.vmodl.fault.NotEnoughLicenses):
   feature: str
   count: int
   expirationDate: _datetime.datetime


class ExtendedFault(VimFault):
   faultTypeId: str
   data: list[pyVmomi.vim.KeyValue] = []


class FailToEnableSPBM(pyVmomi.vmodl.fault.NotEnoughLicenses):
   cs: pyVmomi.vim.ComputeResource
   csName: str
   hostLicenseStates: list[pyVmomi.vim.ComputeResource.HostSPBMLicenseInfo] = []


class FailToLockFaultToleranceVMs(pyVmomi.vmodl.RuntimeFault):
   vmName: str
   vm: pyVmomi.vim.VirtualMachine
   alreadyLockedVm: pyVmomi.vim.VirtualMachine


class FaultToleranceAntiAffinityViolated(MigrationFault):
   hostName: str
   host: pyVmomi.vim.HostSystem


class FaultToleranceCannotEditMem(VmConfigFault):
   vmName: str
   vm: pyVmomi.vim.VirtualMachine

class FaultToleranceCpuIncompatible(CpuIncompatible):
   model: bool
   family: bool
   stepping: bool

class FaultToleranceNeedsThickDisk(MigrationFault):
   vmName: str


class FaultToleranceNotLicensed(VmFaultToleranceIssue):
   hostName: _typing.Optional[str] = None

class FaultToleranceNotSameBuild(MigrationFault):
   build: str


class FaultTolerancePrimaryPowerOnNotAttempted(VmFaultToleranceIssue):
   secondaryVm: pyVmomi.vim.VirtualMachine
   primaryVm: pyVmomi.vim.VirtualMachine


class FaultToleranceVmNotDasProtected(VimFault):
   vm: pyVmomi.vim.VirtualMachine
   vmName: str

class FcoeFault(VimFault):
   pass

class FcoeFaultPnicHasNoPortSet(FcoeFault):
   nicDevice: str


class FeatureRequirementsNotMet(VirtualHardwareCompatibilityIssue):
   featureRequirement: list[pyVmomi.vim.vm.FeatureRequirement] = []
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None

class FileAlreadyExists(FileFault):
   pass

class FileBackedPortNotSupported(DeviceNotSupported):
   pass

class FileFault(VimFault):
   file: str

class FileLocked(FileFault):
   pass

class FileNameTooLong(FileFault):
   pass

class FileNotFound(FileFault):
   pass

class FileNotWritable(FileFault):
   pass


class FileTooLarge(FileFault):
   datastore: str
   fileSize: pyVmomi.VmomiSupport.long
   maxFileSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None

class FilesystemQuiesceFault(SnapshotFault):
   pass


class FilterInUse(ResourceInUse):
   disk: list[pyVmomi.vim.vm.device.VirtualDiskId] = []


class FtIssuesOnHost(VmFaultToleranceIssue):
   class HostSelectionType(pyVmomi.VmomiSupport.Enum):
      user: _typing.ClassVar['HostSelectionType'] = 'user'
      vc: _typing.ClassVar['HostSelectionType'] = 'vc'
      drs: _typing.ClassVar['HostSelectionType'] = 'drs'

   host: pyVmomi.vim.HostSystem
   hostName: str
   errors: list[pyVmomi.vmodl.MethodFault] = []

class FtVmHostRuleViolation(VmConfigFault):
   vmName: str
   hostName: str
   hostGroup: str

class FullStorageVMotionNotSupported(MigrationFeatureNotSupported):
   pass


class GatewayConnectFault(HostConnectFault):
   gatewayType: str
   gatewayId: str
   gatewayInfo: str
   details: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None

class GatewayHostNotReachable(GatewayToHostConnectFault):
   pass

class GatewayNotFound(GatewayConnectFault):
   pass

class GatewayNotReachable(GatewayConnectFault):
   pass

class GatewayOperationRefused(GatewayConnectFault):
   pass

class GatewayToHostAuthFault(GatewayToHostConnectFault):
   invalidProperties: list[str] = []
   missingProperties: list[str] = []


class GatewayToHostConnectFault(GatewayConnectFault):
   hostname: str
   port: _typing.Optional[int] = None


class GatewayToHostTrustVerifyFault(GatewayToHostConnectFault):
   verificationToken: str
   propertiesToVerify: list[pyVmomi.vim.KeyValue] = []


class GenericDrsFault(VimFault):
   hostFaults: list[pyVmomi.vmodl.MethodFault] = []

class GenericVmConfigFault(VmConfigFault):
   reason: str


class GuestAuthenticationChallenge(GuestOperationsFault):
   serverChallenge: pyVmomi.vim.vm.guest.GuestAuthentication
   sessionID: pyVmomi.VmomiSupport.long

class GuestComponentsOutOfDate(GuestOperationsFault):
   pass

class GuestMultipleMappings(GuestOperationsFault):
   pass

class GuestOperationsFault(VimFault):
   pass

class GuestOperationsUnavailable(GuestOperationsFault):
   pass

class GuestPermissionDenied(GuestOperationsFault):
   pass


class GuestProcessNotFound(GuestOperationsFault):
   pid: pyVmomi.VmomiSupport.long


class GuestRegistryFault(GuestOperationsFault):
   windowsSystemErrorCode: pyVmomi.VmomiSupport.long

class GuestRegistryKeyAlreadyExists(GuestRegistryKeyFault):
   pass

class GuestRegistryKeyFault(GuestRegistryFault):
   keyName: str

class GuestRegistryKeyHasSubkeys(GuestRegistryKeyFault):
   pass

class GuestRegistryKeyInvalid(GuestRegistryKeyFault):
   pass

class GuestRegistryKeyParentVolatile(GuestRegistryKeyFault):
   pass

class GuestRegistryValueFault(GuestRegistryFault):
   keyName: str
   valueName: str

class GuestRegistryValueNotFound(GuestRegistryValueFault):
   pass

class HAErrorsAtDest(MigrationFault):
   pass

class HeterogenousHostsBlockingEVC(EVCConfigFault):
   pass


class HostAccessRestrictedToManagementServer(pyVmomi.vmodl.fault.NotSupported):
   managementServer: str


class HostConfigFailed(HostConfigFault):
   failure: list[pyVmomi.vmodl.MethodFault] = []

class HostConfigFault(VimFault):
   pass

class HostConnectFault(VimFault):
   pass


class HostHasComponentFailure(VimFault):
   class HostComponentType(pyVmomi.VmomiSupport.Enum):
      Datastore: _typing.ClassVar['HostComponentType'] = 'Datastore'

   hostName: str
   componentType: str
   componentName: str

class HostInDomain(HostConfigFault):
   pass


class HostIncompatibleForFaultTolerance(VmFaultToleranceIssue):
   class Reason(pyVmomi.VmomiSupport.Enum):
      product: _typing.ClassVar['Reason'] = 'product'
      processor: _typing.ClassVar['Reason'] = 'processor'

   hostName: _typing.Optional[str] = None
   reason: _typing.Optional[str] = None


class HostIncompatibleForRecordReplay(VimFault):
   class Reason(pyVmomi.VmomiSupport.Enum):
      product: _typing.ClassVar['Reason'] = 'product'
      processor: _typing.ClassVar['Reason'] = 'processor'

   hostName: _typing.Optional[str] = None
   reason: _typing.Optional[str] = None


class HostInventoryFull(pyVmomi.vmodl.fault.NotEnoughLicenses):
   capacity: int

class HostPowerOpFailed(VimFault):
   pass


class HostSpecificationOperationFailed(VimFault):
   host: pyVmomi.vim.HostSystem

class HotSnapshotMoveNotSupported(SnapshotCopyNotSupported):
   pass

class HttpFault(VimFault):
   statusCode: int
   statusMessage: str

class IDEDiskNotSupported(DiskNotSupported):
   pass


class IORMNotSupportedHostOnDatastore(VimFault):
   datastore: pyVmomi.vim.Datastore
   datastoreName: str
   host: list[pyVmomi.vim.HostSystem] = []

class ImportHostAddFailure(DvsFault):
   hostIp: list[str] = []


class ImportOperationBulkFault(DvsFault):
   class FaultOnImport(pyVmomi.vmodl.DynamicData):
      entityType: _typing.Optional[str] = None
      key: _typing.Optional[str] = None
      fault: pyVmomi.vmodl.MethodFault

   importFaults: list[FaultOnImport] = []


class InUseFeatureManipulationDisallowed(pyVmomi.vmodl.fault.NotEnoughLicenses):
   pass


class InaccessibleDatastore(InvalidDatastore):
   detail: _typing.Optional[str] = None

class InaccessibleFTMetadataDatastore(InaccessibleDatastore):
   pass

class InaccessibleVFlashSource(VimFault):
   hostName: str

class IncompatibleDefaultDevice(MigrationFault):
   device: str


class IncompatibleHostForFtSecondary(VmFaultToleranceIssue):
   host: pyVmomi.vim.HostSystem
   error: list[pyVmomi.vmodl.MethodFault] = []


class IncompatibleHostForVmReplication(ReplicationFault):
   class IncompatibleReason(pyVmomi.VmomiSupport.Enum):
      rpo: _typing.ClassVar['IncompatibleReason'] = 'rpo'
      netCompression: _typing.ClassVar['IncompatibleReason'] = 'netCompression'

   vmName: str
   hostName: str
   reason: str


class IncompatibleSetting(pyVmomi.vmodl.fault.InvalidArgument):
   conflictingProperty: pyVmomi.VmomiSupport.PropertyPath

class IncorrectFileType(FileFault):
   pass


class IncorrectHostInformation(pyVmomi.vmodl.fault.NotEnoughLicenses):
   pass

class IndependentDiskVMotionNotSupported(MigrationFeatureNotSupported):
   pass

class InsufficientAgentVmsDeployed(InsufficientResourcesFault):
   hostName: str
   requiredNumAgentVms: int
   currentNumAgentVms: int


class InsufficientCpuResourcesFault(InsufficientResourcesFault):
   unreserved: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long

class InsufficientDisks(VsanDiskFault):
   pass

class InsufficientFailoverResourcesFault(InsufficientResourcesFault):
   pass

class InsufficientGraphicsResourcesFault(InsufficientResourcesFault):
   pass


class InsufficientHostCapacityFault(InsufficientResourcesFault):
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None


class InsufficientHostCpuCapacityFault(InsufficientHostCapacityFault):
   unreserved: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long


class InsufficientHostMemoryCapacityFault(InsufficientHostCapacityFault):
   unreserved: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long


class InsufficientMemoryResourcesFault(InsufficientResourcesFault):
   unreserved: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long

class InsufficientNetworkCapacity(InsufficientResourcesFault):
   pass


class InsufficientNetworkResourcePoolCapacity(InsufficientResourcesFault):
   dvsName: str
   dvsUuid: str
   resourcePoolKey: str
   available: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long
   device: list[str] = []

class InsufficientPerCpuCapacity(InsufficientHostCapacityFault):
   pass

class InsufficientResourcesFault(VimFault):
   pass


class InsufficientStandbyCpuResource(InsufficientStandbyResource):
   available: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long


class InsufficientStandbyMemoryResource(InsufficientStandbyResource):
   available: pyVmomi.VmomiSupport.long
   requested: pyVmomi.VmomiSupport.long

class InsufficientStandbyResource(InsufficientResourcesFault):
   pass


class InsufficientStorageIops(VimFault):
   unreservedIops: pyVmomi.VmomiSupport.long
   requestedIops: pyVmomi.VmomiSupport.long
   datastoreName: str

class InsufficientStorageSpace(InsufficientResourcesFault):
   pass


class InsufficientVFlashResourcesFault(InsufficientResourcesFault):
   freeSpaceInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   freeSpace: pyVmomi.VmomiSupport.long
   requestedSpaceInMB: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   requestedSpace: pyVmomi.VmomiSupport.long

class InvalidAffinitySettingFault(VimFault):
   pass

class InvalidBmcRole(VimFault):
   pass

class InvalidBundle(PlatformConfigFault):
   pass

class InvalidCAMCertificate(InvalidCAMServer):
   pass

class InvalidCAMServer(ActiveDirectoryFault):
   camServer: str

class InvalidClientCertificate(InvalidLogin):
   pass

class InvalidController(InvalidDeviceSpec):
   controllerKey: int


class InvalidDasConfigArgument(pyVmomi.vmodl.fault.InvalidArgument):
   class EntryForInvalidArgument(pyVmomi.VmomiSupport.Enum):
      admissionControl: _typing.ClassVar['EntryForInvalidArgument'] = 'admissionControl'
      userHeartbeatDs: _typing.ClassVar['EntryForInvalidArgument'] = 'userHeartbeatDs'
      vmConfig: _typing.ClassVar['EntryForInvalidArgument'] = 'vmConfig'

   entry: _typing.Optional[str] = None
   clusterName: _typing.Optional[str] = None


class InvalidDasRestartPriorityForFtVm(pyVmomi.vmodl.fault.InvalidArgument):
   vm: pyVmomi.vim.VirtualMachine
   vmName: str


class InvalidDatastore(VimFault):
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None
   name: _typing.Optional[str] = None

class InvalidDatastorePath(InvalidDatastore):
   datastorePath: str


class InvalidDatastoreState(InvalidState):
   datastoreName: _typing.Optional[str] = None

class InvalidDeviceBacking(InvalidDeviceSpec):
   pass


class InvalidDeviceOperation(InvalidDeviceSpec):
   badOp: _typing.Optional[pyVmomi.vim.vm.device.VirtualDeviceSpec.Operation] = None
   badFileOp: _typing.Optional[pyVmomi.vim.vm.device.VirtualDeviceSpec.FileOperation] = None

class InvalidDeviceSpec(InvalidVmConfig):
   deviceIndex: int

class InvalidDiskFormat(InvalidFormat):
   pass


class InvalidDrsBehaviorForFtVm(pyVmomi.vmodl.fault.InvalidArgument):
   vm: pyVmomi.vim.VirtualMachine
   vmName: str


class InvalidEditionLicense(pyVmomi.vmodl.fault.NotEnoughLicenses):
   feature: str

class InvalidEvent(VimFault):
   pass


class InvalidFolder(VimFault):
   target: pyVmomi.vim.ManagedEntity

class InvalidFormat(VmConfigFault):
   pass

class InvalidGuestLogin(GuestOperationsFault):
   pass

class InvalidHostConnectionState(InvalidHostState):
   pass

class InvalidHostName(HostConfigFault):
   pass


class InvalidHostState(InvalidState):
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None


class InvalidIndexArgument(pyVmomi.vmodl.fault.InvalidArgument):
   key: str


class InvalidIpfixConfig(DvsFault):
   property: _typing.Optional[pyVmomi.VmomiSupport.PropertyPath] = None

class InvalidIpmiLoginInfo(VimFault):
   pass

class InvalidIpmiMacAddress(VimFault):
   userProvidedMacAddress: str
   observedMacAddress: str

class InvalidLicense(VimFault):
   licenseContent: str

class InvalidLocale(VimFault):
   pass

class InvalidLogin(VimFault):
   pass


class InvalidName(VimFault):
   name: str
   entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None

class InvalidNasCredentials(NasConfigFault):
   userName: str

class InvalidNetworkInType(VAppPropertyFault):
   pass

class InvalidNetworkResource(NasConfigFault):
   remoteHost: str
   remotePath: str

class InvalidOperationOnSecondaryVm(VmFaultToleranceIssue):
   instanceUuid: str


class InvalidPowerState(InvalidState):
   requestedState: _typing.Optional[pyVmomi.vim.VirtualMachine.PowerState] = None
   existingState: pyVmomi.vim.VirtualMachine.PowerState

class InvalidPrivilege(VimFault):
   privilege: str


class InvalidProfileReferenceHost(pyVmomi.vmodl.RuntimeFault):
   class Reason(pyVmomi.VmomiSupport.Enum):
      incompatibleVersion: _typing.ClassVar['Reason'] = 'incompatibleVersion'
      missingReferenceHost: _typing.ClassVar['Reason'] = 'missingReferenceHost'

   reason: _typing.Optional[str] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   profile: _typing.Optional[pyVmomi.vim.profile.Profile] = None
   profileName: _typing.Optional[str] = None

class InvalidPropertyType(VAppPropertyFault):
   pass

class InvalidPropertyValue(VAppPropertyFault):
   pass

class InvalidResourcePoolStructureFault(InsufficientResourcesFault):
   pass


class InvalidScheduledTask(pyVmomi.vmodl.RuntimeFault):
   pass

class InvalidSnapshotFormat(InvalidFormat):
   pass

class InvalidState(VimFault):
   pass


class InvalidVmConfig(VmConfigFault):
   property: _typing.Optional[pyVmomi.VmomiSupport.PropertyPath] = None


class InvalidVmState(InvalidState):
   vm: pyVmomi.vim.VirtualMachine


class InventoryHasStandardAloneHosts(pyVmomi.vmodl.fault.NotEnoughLicenses):
   hosts: list[str] = []

class IpHostnameGeneratorError(CustomizationFault):
   pass

class IscsiFault(VimFault):
   pass

class IscsiFaultInvalidVnic(IscsiFault):
   vnicDevice: str

class IscsiFaultPnicInUse(IscsiFault):
   pnicDevice: str

class IscsiFaultVnicAlreadyBound(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicHasActivePaths(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicHasMultipleUplinks(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicHasNoUplinks(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicHasWrongUplink(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicInUse(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicIsLastPath(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicNotBound(IscsiFault):
   vnicDevice: str

class IscsiFaultVnicNotFound(IscsiFault):
   vnicDevice: str

class KeyNotFound(VimFault):
   key: str

class LargeRDMConversionNotSupported(MigrationFault):
   device: str


class LargeRDMNotSupportedOnDatastore(VmConfigFault):
   device: str
   datastore: pyVmomi.vim.Datastore
   datastoreName: str

class LegacyNetworkInterfaceInUse(CannotAccessNetwork):
   pass


class LicenseAssignmentFailed(pyVmomi.vmodl.RuntimeFault):
   class Reason(pyVmomi.VmomiSupport.Enum):
      keyEntityMismatch: _typing.ClassVar['Reason'] = 'keyEntityMismatch'
      downgradeDisallowed: _typing.ClassVar['Reason'] = 'downgradeDisallowed'
      inventoryNotManageableByVirtualCenter: _typing.ClassVar['Reason'] = 'inventoryNotManageableByVirtualCenter'
      hostsUnmanageableByVirtualCenterWithoutLicenseServer: _typing.ClassVar['Reason'] = 'hostsUnmanageableByVirtualCenterWithoutLicenseServer'

   reason: _typing.Optional[str] = None


class LicenseDowngradeDisallowed(pyVmomi.vmodl.fault.NotEnoughLicenses):
   edition: str
   entityId: str
   features: list[pyVmomi.vmodl.KeyAnyValue] = []

class LicenseEntityNotFound(VimFault):
   entityId: str


class LicenseExpired(pyVmomi.vmodl.fault.NotEnoughLicenses):
   licenseKey: str


class LicenseKeyEntityMismatch(pyVmomi.vmodl.fault.NotEnoughLicenses):
   pass


class LicenseRestricted(pyVmomi.vmodl.fault.NotEnoughLicenses):
   pass

class LicenseServerUnavailable(VimFault):
   licenseServer: str


class LicenseSourceUnavailable(pyVmomi.vmodl.fault.NotEnoughLicenses):
   licenseSource: pyVmomi.vim.LicenseManager.LicenseSource


class LimitExceeded(VimFault):
   property: _typing.Optional[pyVmomi.VmomiSupport.PropertyPath] = None
   limit: _typing.Optional[int] = None

class LinuxVolumeNotClean(CustomizationFault):
   pass

class LogBundlingFailed(VimFault):
   pass

class MaintenanceModeFileMove(MigrationFault):
   pass

class MemoryFileFormatNotSupportedByDatastore(UnsupportedDatastore):
   datastoreName: str
   type: str

class MemoryHotPlugNotSupported(VmConfigFault):
   pass

class MemorySizeNotRecommended(VirtualHardwareCompatibilityIssue):
   memorySizeMB: int
   minMemorySizeMB: int
   maxMemorySizeMB: int

class MemorySizeNotSupported(VirtualHardwareCompatibilityIssue):
   memorySizeMB: int
   minMemorySizeMB: int
   maxMemorySizeMB: int


class MemorySizeNotSupportedByDatastore(VirtualHardwareCompatibilityIssue):
   datastore: pyVmomi.vim.Datastore
   memorySizeMB: int
   maxMemorySizeMB: int

class MemorySnapshotOnIndependentDisk(SnapshotFault):
   pass


class MethodAlreadyDisabledFault(pyVmomi.vmodl.RuntimeFault):
   sourceId: str


class MethodDisabled(pyVmomi.vmodl.RuntimeFault):
   source: _typing.Optional[str] = None

class MigrationDisabled(MigrationFault):
   pass

class MigrationFault(VimFault):
   pass


class MigrationFeatureNotSupported(MigrationFault):
   atSourceHost: bool
   failedHostName: str
   failedHost: pyVmomi.vim.HostSystem

class MigrationNotReady(MigrationFault):
   reason: str

class MismatchedBundle(VimFault):
   bundleUuid: str
   hostUuid: str
   bundleBuildNumber: int
   hostBuildNumber: int

class MismatchedNetworkPolicies(MigrationFault):
   device: str
   backing: str
   connected: bool

class MismatchedVMotionNetworkNames(MigrationFault):
   sourceNetwork: str
   destNetwork: str

class MissingBmcSupport(VimFault):
   pass

class MissingController(InvalidDeviceSpec):
   pass

class MissingIpPool(VAppPropertyFault):
   pass

class MissingLinuxCustResources(CustomizationFault):
   pass

class MissingNetworkIpConfig(VAppPropertyFault):
   pass

class MissingPowerOffConfiguration(VAppConfigFault):
   pass

class MissingPowerOnConfiguration(VAppConfigFault):
   pass

class MissingWindowsCustResources(CustomizationFault):
   pass

class MksConnectionLimitReached(InvalidState):
   connectionLimit: int


class MountError(CustomizationFault):
   vm: pyVmomi.vim.VirtualMachine
   diskIndex: int

class MultiWriterNotSupported(DeviceNotSupported):
   pass


class MultipleCertificatesVerifyFault(HostConnectFault):
   class ThumbprintData(pyVmomi.vmodl.DynamicData):
      port: int
      thumbprint: str

   thumbprintData: list[ThumbprintData] = []

class MultipleSnapshotsNotSupported(SnapshotFault):
   pass


class NamespaceFull(VimFault):
   name: str
   currentMaxSize: pyVmomi.VmomiSupport.long
   requiredSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class NamespaceLimitReached(VimFault):
   limit: _typing.Optional[int] = None

class NamespaceWriteProtected(VimFault):
   name: str

class NasConfigFault(HostConfigFault):
   name: str

class NasConnectionLimitReached(NasConfigFault):
   remoteHost: str
   remotePath: str

class NasSessionCredentialConflict(NasConfigFault):
   remoteHost: str
   remotePath: str
   userName: str

class NasVolumeNotMounted(NasConfigFault):
   remoteHost: str
   remotePath: str

class NetworkCopyFault(FileFault):
   pass

class NetworkDisruptedAndConfigRolledBack(VimFault):
   host: str

class NetworkInaccessible(NasConfigFault):
   pass


class NetworksMayNotBeTheSame(MigrationFault):
   name: _typing.Optional[str] = None

class NicSettingMismatch(CustomizationFault):
   numberOfNicsInSpec: int
   numberOfNicsInVM: int


class NoActiveHostInCluster(InvalidState):
   computeResource: pyVmomi.vim.ComputeResource


class NoAvailableIp(VAppPropertyFault):
   network: pyVmomi.vim.Network

class NoClientCertificate(VimFault):
   pass

class NoCompatibleDatastore(VimFault):
   pass

class NoCompatibleHardAffinityHost(VmConfigFault):
   vmName: str


class NoCompatibleHost(VimFault):
   host: list[pyVmomi.vim.HostSystem] = []
   error: list[pyVmomi.vmodl.MethodFault] = []

class NoCompatibleHostWithAccessToDevice(NoCompatibleHost):
   pass

class NoCompatibleSoftAffinityHost(VmConfigFault):
   vmName: str

class NoConnectedDatastore(VimFault):
   pass

class NoDiskFound(VimFault):
   pass

class NoDiskSpace(FileFault):
   datastore: str

class NoDisksToCustomize(CustomizationFault):
   pass

class NoGateway(HostConfigFault):
   pass

class NoGuestHeartbeat(MigrationFault):
   pass


class NoHost(HostConnectFault):
   name: _typing.Optional[str] = None


class NoHostSuitableForFtSecondary(VmFaultToleranceIssue):
   vm: pyVmomi.vim.VirtualMachine
   vmName: str


class NoLicenseServerConfigured(pyVmomi.vmodl.fault.NotEnoughLicenses):
   pass

class NoPeerHostFound(HostPowerOpFailed):
   pass


class NoPermission(pyVmomi.vmodl.fault.SecurityError):
   class EntityPrivileges(pyVmomi.vmodl.DynamicData):
      entity: pyVmomi.VmomiSupport.ManagedObject
      privilegeIds: list[str] = []

   object: _typing.Optional[pyVmomi.VmomiSupport.ManagedObject] = None
   privilegeId: _typing.Optional[str] = None
   missingPrivileges: list[EntityPrivileges] = []

class NoPermissionOnAD(ActiveDirectoryFault):
   pass

class NoPermissionOnHost(HostConnectFault):
   pass


class NoPermissionOnNasVolume(NasConfigFault):
   userName: _typing.Optional[str] = None

class NoSubjectName(VimFault):
   pass

class NoVcManagedIpConfigured(VAppPropertyFault):
   pass

class NoVirtualNic(HostConfigFault):
   pass

class NoVmInVApp(VAppConfigFault):
   pass

class NonADUserRequired(ActiveDirectoryFault):
   pass

class NonHomeRDMVMotionNotSupported(MigrationFeatureNotSupported):
   device: str

class NonPersistentDisksNotSupported(DeviceNotSupported):
   pass

class NonVmwareOuiMacNotSupportedHost(NotSupportedHost):
   hostName: str

class NotADirectory(FileFault):
   pass

class NotAFile(FileFault):
   pass

class NotAuthenticated(NoPermission):
   pass

class NotEnoughCpus(VirtualHardwareCompatibilityIssue):
   numCpuDest: int
   numCpuVm: int


class NotEnoughLogicalCpus(NotEnoughCpus):
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None

class NotFound(VimFault):
   pass


class NotSupportedDeviceForFT(VmFaultToleranceIssue):
   class DeviceType(pyVmomi.VmomiSupport.Enum):
      virtualVmxnet3: _typing.ClassVar['DeviceType'] = 'virtualVmxnet3'
      paraVirtualSCSIController: _typing.ClassVar['DeviceType'] = 'paraVirtualSCSIController'

   host: pyVmomi.vim.HostSystem
   hostName: _typing.Optional[str] = None
   vm: pyVmomi.vim.VirtualMachine
   vmName: _typing.Optional[str] = None
   deviceType: str
   deviceLabel: _typing.Optional[str] = None


class NotSupportedHost(HostConnectFault):
   productName: _typing.Optional[str] = None
   productVersion: _typing.Optional[str] = None

class NotSupportedHostForChecksum(VimFault):
   pass

class NotSupportedHostForVFlash(NotSupportedHost):
   hostName: str

class NotSupportedHostForVmcp(NotSupportedHost):
   hostName: str

class NotSupportedHostForVmemFile(NotSupportedHost):
   hostName: str

class NotSupportedHostForVsan(NotSupportedHost):
   hostName: str

class NotSupportedHostInCluster(NotSupportedHost):
   pass


class NotSupportedHostInDvs(NotSupportedHost):
   switchProductSpec: pyVmomi.vim.dvs.ProductSpec

class NotSupportedHostInHACluster(NotSupportedHost):
   hostName: str
   build: str

class NotUserConfigurableProperty(VAppPropertyFault):
   pass

class NumVirtualCoresPerSocketNotSupported(VirtualHardwareCompatibilityIssue):
   maxSupportedCoresPerSocketDest: int
   numCoresPerSocketVm: int

class NumVirtualCpusExceedsLimit(InsufficientResourcesFault):
   maxSupportedVcpus: int


class NumVirtualCpusIncompatible(VmConfigFault):
   class Reason(pyVmomi.VmomiSupport.Enum):
      recordReplay: _typing.ClassVar['Reason'] = 'recordReplay'
      faultTolerance: _typing.ClassVar['Reason'] = 'faultTolerance'

   reason: str
   numCpu: int

class NumVirtualCpusNotSupported(VirtualHardwareCompatibilityIssue):
   maxSupportedVcpusDest: int
   numCpuVm: int

class OperationDisabledByGuest(GuestOperationsFault):
   pass


class OperationDisallowedOnHost(pyVmomi.vmodl.RuntimeFault):
   pass

class OperationNotSupportedByGuest(GuestOperationsFault):
   pass


class OutOfBounds(VimFault):
   argumentName: pyVmomi.VmomiSupport.PropertyPath

class OvfAttribute(OvfInvalidPackage):
   elementName: str
   attributeName: str

class OvfConnectedDevice(OvfHardwareExport):
   pass

class OvfConnectedDeviceFloppy(OvfConnectedDevice):
   filename: str

class OvfConnectedDeviceIso(OvfConnectedDevice):
   filename: str

class OvfConstraint(OvfInvalidPackage):
   name: str

class OvfConsumerCallbackFault(OvfFault):
   extensionKey: str
   extensionName: str

class OvfConsumerCommunicationError(OvfConsumerCallbackFault):
   description: str


class OvfConsumerFault(OvfConsumerCallbackFault):
   errorKey: str
   message: str
   params: list[pyVmomi.vim.KeyValue] = []

class OvfConsumerInvalidSection(OvfConsumerCallbackFault):
   lineNumber: int
   description: str

class OvfConsumerPowerOnFault(InvalidState):
   extensionKey: str
   extensionName: str
   description: str

class OvfConsumerUndeclaredSection(OvfConsumerCallbackFault):
   qualifiedSectionType: str

class OvfConsumerUndefinedPrefix(OvfConsumerCallbackFault):
   prefix: str

class OvfConsumerValidationFault(VmConfigFault):
   extensionKey: str
   extensionName: str
   message: str

class OvfCpuCompatibility(OvfImport):
   registerName: str
   level: int
   registerValue: str
   desiredRegisterValue: str

class OvfCpuCompatibilityCheckNotSupported(OvfImport):
   pass

class OvfDiskMappingNotFound(OvfSystemFault):
   diskName: str
   vmName: str

class OvfDiskOrderConstraint(OvfConstraint):
   pass

class OvfDuplicateElement(OvfElement):
   pass

class OvfDuplicatedElementBoundary(OvfElement):
   boundary: str

class OvfDuplicatedPropertyIdExport(OvfExport):
   fqid: str

class OvfDuplicatedPropertyIdImport(OvfExport):
   pass

class OvfElement(OvfInvalidPackage):
   name: str

class OvfElementInvalidValue(OvfElement):
   value: str

class OvfExport(OvfFault):
   pass

class OvfExportFailed(OvfExport):
   pass

class OvfFault(VimFault):
   pass

class OvfHardwareCheck(OvfImport):
   pass


class OvfHardwareExport(OvfExport):
   device: _typing.Optional[pyVmomi.vim.vm.device.VirtualDevice] = None
   vmPath: str

class OvfHostResourceConstraint(OvfConstraint):
   value: str

class OvfHostValueNotParsed(OvfSystemFault):
   property: str
   value: str

class OvfImport(OvfFault):
   pass

class OvfImportFailed(OvfImport):
   pass

class OvfInternalError(OvfSystemFault):
   pass

class OvfInvalidPackage(OvfFault):
   lineNumber: int

class OvfInvalidValue(OvfAttribute):
   value: str

class OvfInvalidValueConfiguration(OvfInvalidValue):
   pass

class OvfInvalidValueEmpty(OvfInvalidValue):
   pass

class OvfInvalidValueFormatMalformed(OvfInvalidValue):
   pass

class OvfInvalidValueReference(OvfInvalidValue):
   pass

class OvfInvalidVmName(OvfUnsupportedPackage):
   name: str

class OvfMappedOsId(OvfImport):
   ovfId: int
   ovfDescription: str
   targetDescription: str

class OvfMissingAttribute(OvfAttribute):
   pass

class OvfMissingElement(OvfElement):
   pass

class OvfMissingElementNormalBoundary(OvfMissingElement):
   boundary: str

class OvfMissingHardware(OvfImport):
   name: str
   resourceType: int

class OvfNetworkMappingNotSupported(OvfImport):
   pass

class OvfNoHostNic(OvfUnsupportedPackage):
   pass

class OvfNoSpaceOnController(OvfUnsupportedElement):
   parent: str

class OvfNoSupportedHardwareFamily(OvfUnsupportedPackage):
   version: str

class OvfProperty(OvfInvalidPackage):
   type: str
   value: str

class OvfPropertyExport(OvfExport):
   type: str
   value: str

class OvfPropertyNetwork(OvfProperty):
   pass

class OvfPropertyNetworkExport(OvfExport):
   network: str

class OvfPropertyQualifier(OvfProperty):
   qualifier: str

class OvfPropertyQualifierDuplicate(OvfProperty):
   qualifier: str

class OvfPropertyQualifierIgnored(OvfProperty):
   qualifier: str

class OvfPropertyType(OvfProperty):
   pass

class OvfPropertyValue(OvfProperty):
   pass

class OvfSystemFault(OvfFault):
   pass


class OvfToXmlUnsupportedElement(OvfSystemFault):
   name: _typing.Optional[str] = None

class OvfUnableToExportDisk(OvfHardwareExport):
   diskName: str

class OvfUnexpectedElement(OvfElement):
   pass


class OvfUnknownDevice(OvfSystemFault):
   device: _typing.Optional[pyVmomi.vim.vm.device.VirtualDevice] = None
   vmName: str


class OvfUnknownDeviceBacking(OvfHardwareExport):
   backing: pyVmomi.vim.vm.device.VirtualDevice.BackingInfo

class OvfUnknownEntity(OvfSystemFault):
   lineNumber: int

class OvfUnsupportedAttribute(OvfUnsupportedPackage):
   elementName: str
   attributeName: str

class OvfUnsupportedAttributeValue(OvfUnsupportedAttribute):
   value: str


class OvfUnsupportedDeviceBackingInfo(OvfSystemFault):
   elementName: _typing.Optional[str] = None
   instanceId: _typing.Optional[str] = None
   deviceName: str
   backingName: _typing.Optional[str] = None


class OvfUnsupportedDeviceBackingOption(OvfSystemFault):
   elementName: _typing.Optional[str] = None
   instanceId: _typing.Optional[str] = None
   deviceName: str
   backingName: _typing.Optional[str] = None

class OvfUnsupportedDeviceExport(OvfHardwareExport):
   pass

class OvfUnsupportedDiskProvisioning(OvfImport):
   diskProvisioning: str
   supportedDiskProvisioning: str

class OvfUnsupportedElement(OvfUnsupportedPackage):
   name: str

class OvfUnsupportedElementValue(OvfUnsupportedElement):
   value: str


class OvfUnsupportedPackage(OvfFault):
   lineNumber: _typing.Optional[int] = None

class OvfUnsupportedSection(OvfUnsupportedElement):
   info: str

class OvfUnsupportedSubType(OvfUnsupportedPackage):
   elementName: str
   instanceId: str
   deviceType: int
   deviceSubType: str

class OvfUnsupportedType(OvfUnsupportedPackage):
   name: str
   instanceId: str
   deviceType: int

class OvfWrongElement(OvfElement):
   pass

class OvfWrongNamespace(OvfInvalidPackage):
   namespaceName: str

class OvfXmlFormat(OvfInvalidPackage):
   description: str

class PasswordExpired(InvalidLogin):
   pass

class PatchAlreadyInstalled(PatchNotApplicable):
   pass


class PatchBinariesNotFound(VimFault):
   patchID: str
   binary: list[str] = []

class PatchInstallFailed(PlatformConfigFault):
   rolledBack: bool

class PatchIntegrityError(PlatformConfigFault):
   pass

class PatchMetadataCorrupted(PatchMetadataInvalid):
   pass


class PatchMetadataInvalid(VimFault):
   patchID: str
   metaData: list[str] = []

class PatchMetadataNotFound(PatchMetadataInvalid):
   pass


class PatchMissingDependencies(PatchNotApplicable):
   prerequisitePatch: list[str] = []
   prerequisiteLib: list[str] = []

class PatchNotApplicable(VimFault):
   patchID: str


class PatchSuperseded(PatchNotApplicable):
   supersede: list[str] = []

class PhysCompatRDMNotSupported(RDMNotSupported):
   pass

class PlatformConfigFault(HostConfigFault):
   text: str


class PowerOnFtSecondaryFailed(VmFaultToleranceIssue):
   vm: pyVmomi.vim.VirtualMachine
   vmName: str
   hostSelectionBy: FtIssuesOnHost.HostSelectionType
   hostErrors: list[pyVmomi.vmodl.MethodFault] = []
   rootCause: pyVmomi.vmodl.MethodFault


class PowerOnFtSecondaryTimedout(Timedout):
   vm: pyVmomi.vim.VirtualMachine
   vmName: str
   timeout: int


class ProfileUpdateFailed(VimFault):
   class UpdateFailure(pyVmomi.vmodl.DynamicData):
      profilePath: pyVmomi.vim.profile.ProfilePropertyPath
      errMsg: pyVmomi.vmodl.LocalizableMessage

   failure: list[UpdateFailure] = []
   warnings: list[UpdateFailure] = []


class QuarantineModeFault(VmConfigFault):
   class FaultType(pyVmomi.VmomiSupport.Enum):
      NoCompatibleNonQuarantinedHost: _typing.ClassVar['FaultType'] = 'NoCompatibleNonQuarantinedHost'
      CorrectionDisallowed: _typing.ClassVar['FaultType'] = 'CorrectionDisallowed'
      CorrectionImpact: _typing.ClassVar['FaultType'] = 'CorrectionImpact'

   vmName: str
   faultType: str

class QuestionPending(InvalidState):
   text: str


class QuiesceDatastoreIOForHAFailed(ResourceInUse):
   host: pyVmomi.vim.HostSystem
   hostName: str
   ds: pyVmomi.vim.Datastore
   dsName: str

class RDMConversionNotSupported(MigrationFault):
   device: str

class RDMNotPreserved(MigrationFault):
   device: str

class RDMNotSupported(DeviceNotSupported):
   pass


class RDMNotSupportedOnDatastore(VmConfigFault):
   device: str
   datastore: pyVmomi.vim.Datastore
   datastoreName: str

class RDMPointsToInaccessibleDisk(CannotAccessVmDisk):
   pass

class RawDiskNotSupported(DeviceNotSupported):
   pass

class ReadHostResourcePoolTreeFailed(HostConnectFault):
   pass

class ReadOnlyDisksWithLegacyDestination(MigrationFault):
   roDiskCount: int
   timeoutDanger: bool


class RebootRequired(VimFault):
   patch: _typing.Optional[str] = None

class RecordReplayDisabled(VimFault):
   pass

class RemoteDeviceNotSupported(DeviceNotSupported):
   pass

class RemoveFailed(VimFault):
   pass

class ReplicationConfigFault(ReplicationFault):
   pass


class ReplicationDiskConfigFault(ReplicationConfigFault):
   class ReasonForFault(pyVmomi.VmomiSupport.Enum):
      diskNotFound: _typing.ClassVar['ReasonForFault'] = 'diskNotFound'
      diskTypeNotSupported: _typing.ClassVar['ReasonForFault'] = 'diskTypeNotSupported'
      invalidDiskKey: _typing.ClassVar['ReasonForFault'] = 'invalidDiskKey'
      invalidDiskReplicationId: _typing.ClassVar['ReasonForFault'] = 'invalidDiskReplicationId'
      duplicateDiskReplicationId: _typing.ClassVar['ReasonForFault'] = 'duplicateDiskReplicationId'
      invalidPersistentFilePath: _typing.ClassVar['ReasonForFault'] = 'invalidPersistentFilePath'
      reconfigureDiskReplicationIdNotAllowed: _typing.ClassVar['ReasonForFault'] = 'reconfigureDiskReplicationIdNotAllowed'

   reason: _typing.Optional[str] = None
   vmRef: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   key: _typing.Optional[int] = None

class ReplicationFault(VimFault):
   pass

class ReplicationIncompatibleWithFT(ReplicationFault):
   pass


class ReplicationInvalidOptions(ReplicationFault):
   options: str
   entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None

class ReplicationNotSupportedOnHost(ReplicationFault):
   pass


class ReplicationVmConfigFault(ReplicationConfigFault):
   class ReasonForFault(pyVmomi.VmomiSupport.Enum):
      incompatibleHwVersion: _typing.ClassVar['ReasonForFault'] = 'incompatibleHwVersion'
      invalidVmReplicationId: _typing.ClassVar['ReasonForFault'] = 'invalidVmReplicationId'
      invalidGenerationNumber: _typing.ClassVar['ReasonForFault'] = 'invalidGenerationNumber'
      outOfBoundsRpoValue: _typing.ClassVar['ReasonForFault'] = 'outOfBoundsRpoValue'
      invalidDestinationIpAddress: _typing.ClassVar['ReasonForFault'] = 'invalidDestinationIpAddress'
      invalidDestinationPort: _typing.ClassVar['ReasonForFault'] = 'invalidDestinationPort'
      invalidExtraVmOptions: _typing.ClassVar['ReasonForFault'] = 'invalidExtraVmOptions'
      staleGenerationNumber: _typing.ClassVar['ReasonForFault'] = 'staleGenerationNumber'
      reconfigureVmReplicationIdNotAllowed: _typing.ClassVar['ReasonForFault'] = 'reconfigureVmReplicationIdNotAllowed'
      cannotRetrieveVmReplicationConfiguration: _typing.ClassVar['ReasonForFault'] = 'cannotRetrieveVmReplicationConfiguration'
      replicationAlreadyEnabled: _typing.ClassVar['ReasonForFault'] = 'replicationAlreadyEnabled'
      invalidPriorConfiguration: _typing.ClassVar['ReasonForFault'] = 'invalidPriorConfiguration'
      replicationNotEnabled: _typing.ClassVar['ReasonForFault'] = 'replicationNotEnabled'
      replicationConfigurationFailed: _typing.ClassVar['ReasonForFault'] = 'replicationConfigurationFailed'
      encryptedVm: _typing.ClassVar['ReasonForFault'] = 'encryptedVm'
      invalidThumbprint: _typing.ClassVar['ReasonForFault'] = 'invalidThumbprint'
      incompatibleDevice: _typing.ClassVar['ReasonForFault'] = 'incompatibleDevice'

   reason: _typing.Optional[str] = None
   vmRef: _typing.Optional[pyVmomi.vim.VirtualMachine] = None


class ReplicationVmFault(ReplicationFault):
   class ReasonForFault(pyVmomi.VmomiSupport.Enum):
      notConfigured: _typing.ClassVar['ReasonForFault'] = 'notConfigured'
      poweredOff: _typing.ClassVar['ReasonForFault'] = 'poweredOff'
      suspended: _typing.ClassVar['ReasonForFault'] = 'suspended'
      poweredOn: _typing.ClassVar['ReasonForFault'] = 'poweredOn'
      offlineReplicating: _typing.ClassVar['ReasonForFault'] = 'offlineReplicating'
      invalidState: _typing.ClassVar['ReasonForFault'] = 'invalidState'
      invalidInstanceId: _typing.ClassVar['ReasonForFault'] = 'invalidInstanceId'
      closeDiskError: _typing.ClassVar['ReasonForFault'] = 'closeDiskError'
      groupExist: _typing.ClassVar['ReasonForFault'] = 'groupExist'

   reason: str
   state: _typing.Optional[str] = None
   instanceId: _typing.Optional[str] = None
   vm: pyVmomi.vim.VirtualMachine


class ReplicationVmInProgressFault(ReplicationVmFault):
   class Activity(pyVmomi.VmomiSupport.Enum):
      fullSync: _typing.ClassVar['Activity'] = 'fullSync'
      delta: _typing.ClassVar['Activity'] = 'delta'

   requestedActivity: str
   inProgressActivity: str


class ResourceInUse(VimFault):
   type: _typing.Optional[type] = None
   name: _typing.Optional[str] = None


class ResourceNotAvailable(VimFault):
   containerType: _typing.Optional[type] = None
   containerName: _typing.Optional[str] = None
   type: _typing.Optional[type] = None


class RestrictedByAdministrator(pyVmomi.vmodl.RuntimeFault):
   details: str


class RestrictedVersion(pyVmomi.vmodl.fault.SecurityError):
   pass

class RollbackFailure(DvsFault):
   entityName: str
   entityType: str


class RuleViolation(VmConfigFault):
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   rule: pyVmomi.vim.cluster.RuleInfo

class SSLDisabledFault(HostConnectFault):
   pass


class SSLVerifyFault(HostConnectFault):
   selfSigned: bool
   thumbprint: _typing.Optional[str] = None
   certificate: _typing.Optional[str] = None

class SSPIChallenge(VimFault):
   base64Token: str

class SecondaryVmAlreadyDisabled(VmFaultToleranceIssue):
   instanceUuid: str

class SecondaryVmAlreadyEnabled(VmFaultToleranceIssue):
   instanceUuid: str

class SecondaryVmAlreadyRegistered(VmFaultToleranceIssue):
   instanceUuid: str

class SecondaryVmNotRegistered(VmFaultToleranceIssue):
   instanceUuid: str

class SharedBusControllerNotSupported(DeviceNotSupported):
   pass


class ShrinkDiskFault(VimFault):
   diskId: _typing.Optional[int] = None

class SnapshotCloneNotSupported(SnapshotCopyNotSupported):
   pass

class SnapshotCopyNotSupported(MigrationFault):
   pass

class SnapshotDisabled(SnapshotFault):
   pass

class SnapshotFault(VimFault):
   pass


class SnapshotIncompatibleDeviceInVm(SnapshotFault):
   fault: pyVmomi.vmodl.MethodFault

class SnapshotLocked(SnapshotFault):
   pass

class SnapshotMoveFromNonHomeNotSupported(SnapshotCopyNotSupported):
   pass

class SnapshotMoveNotSupported(SnapshotCopyNotSupported):
   pass

class SnapshotMoveToNonHomeNotSupported(SnapshotCopyNotSupported):
   pass

class SnapshotNoChange(SnapshotFault):
   pass


class SnapshotRevertIssue(MigrationFault):
   snapshotName: _typing.Optional[str] = None
   event: list[pyVmomi.vim.event.Event] = []
   errors: bool

class SoftRuleVioCorrectionDisallowed(VmConfigFault):
   vmName: str

class SoftRuleVioCorrectionImpact(VmConfigFault):
   vmName: str


class SolutionUserRequired(pyVmomi.vmodl.fault.SecurityError):
   pass

class SsdDiskNotAvailable(VimFault):
   devicePath: str

class StorageDrsCannotMoveDiskInMultiWriterMode(VimFault):
   pass

class StorageDrsCannotMoveFTVm(VimFault):
   pass

class StorageDrsCannotMoveIndependentDisk(VimFault):
   pass

class StorageDrsCannotMoveManuallyPlacedSwapFile(VimFault):
   pass

class StorageDrsCannotMoveManuallyPlacedVm(VimFault):
   pass

class StorageDrsCannotMoveSharedDisk(VimFault):
   pass

class StorageDrsCannotMoveTemplate(VimFault):
   pass

class StorageDrsCannotMoveVmInUserFolder(VimFault):
   pass

class StorageDrsCannotMoveVmWithMountedCDROM(VimFault):
   pass

class StorageDrsCannotMoveVmWithNoFilesInLayout(VimFault):
   pass

class StorageDrsDatacentersCannotShareDatastore(VimFault):
   pass

class StorageDrsDisabledOnVm(VimFault):
   pass

class StorageDrsHbrDiskNotMovable(VimFault):
   nonMovableDiskIds: str

class StorageDrsHmsMoveInProgress(VimFault):
   pass

class StorageDrsHmsUnreachable(VimFault):
   pass

class StorageDrsIolbDisabledInternally(VimFault):
   pass

class StorageDrsRelocateDisabled(VimFault):
   pass

class StorageDrsStaleHmsCollection(VimFault):
   pass

class StorageDrsUnableToMoveFiles(VimFault):
   pass

class StorageVMotionNotSupported(MigrationFeatureNotSupported):
   pass


class StorageVmotionIncompatible(VirtualHardwareCompatibilityIssue):
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None

class SuspendedRelocateNotSupported(MigrationFault):
   pass

class SwapDatastoreNotWritableOnHost(DatastoreNotWritableOnHost):
   pass

class SwapDatastoreUnset(VimFault):
   pass

class SwapPlacementOverrideNotSupported(InvalidVmConfig):
   pass

class SwitchIpUnset(DvsFault):
   pass

class SwitchNotInUpgradeMode(DvsFault):
   pass


class TaskInProgress(VimFault):
   task: pyVmomi.vim.Task


class ThirdPartyLicenseAssignmentFailed(pyVmomi.vmodl.RuntimeFault):
   class Reason(pyVmomi.VmomiSupport.Enum):
      licenseAssignmentFailed: _typing.ClassVar['Reason'] = 'licenseAssignmentFailed'
      moduleNotInstalled: _typing.ClassVar['Reason'] = 'moduleNotInstalled'

   host: pyVmomi.vim.HostSystem
   module: str
   reason: _typing.Optional[str] = None

class Timedout(VimFault):
   pass

class TooManyConcurrentNativeClones(FileFault):
   pass

class TooManyConsecutiveOverrides(VimFault):
   pass

class TooManyDevices(InvalidVmConfig):
   pass

class TooManyDisksOnLegacyHost(MigrationFault):
   diskCount: int
   timeoutDanger: bool

class TooManyGuestLogons(GuestOperationsFault):
   pass

class TooManyHosts(HostConnectFault):
   pass

class TooManyNativeCloneLevels(FileFault):
   pass

class TooManyNativeClonesOnFile(FileFault):
   pass

class TooManySnapshotLevels(SnapshotFault):
   pass

class ToolsAlreadyUpgraded(VmToolsUpgradeFault):
   pass

class ToolsAutoUpgradeNotSupported(VmToolsUpgradeFault):
   pass

class ToolsImageCopyFailed(VmToolsUpgradeFault):
   pass

class ToolsImageNotAvailable(VmToolsUpgradeFault):
   pass

class ToolsImageSignatureCheckFailed(VmToolsUpgradeFault):
   pass

class ToolsInstallationInProgress(MigrationFault):
   pass

class ToolsUnavailable(VimFault):
   pass

class ToolsUpgradeCancelled(VmToolsUpgradeFault):
   pass

class UnSupportedDatastoreForVFlash(UnsupportedDatastore):
   datastoreName: str
   type: str

class UncommittedUndoableDisk(MigrationFault):
   pass

class UnconfiguredPropertyValue(InvalidPropertyValue):
   pass

class UncustomizableGuest(CustomizationFault):
   uncustomizableGuestOS: str

class UnexpectedCustomizationFault(CustomizationFault):
   pass

class UnrecognizedHost(VimFault):
   hostName: str

class UnsharedSwapVMotionNotSupported(MigrationFeatureNotSupported):
   pass


class UnsupportedDatastore(VmConfigFault):
   datastore: _typing.Optional[pyVmomi.vim.Datastore] = None

class UnsupportedGuest(InvalidVmConfig):
   unsupportedGuestOS: str


class UnsupportedVimApiVersion(VimFault):
   version: _typing.Optional[str] = None

class UnsupportedVmxLocation(VmConfigFault):
   pass

class UnusedVirtualDiskBlocksNotScrubbed(DeviceBackingNotSupported):
   pass

class UserNotFound(VimFault):
   principal: str
   unresolved: bool

class VAppConfigFault(VimFault):
   pass

class VAppNotRunning(VmConfigFault):
   pass


class VAppOperationInProgress(pyVmomi.vmodl.RuntimeFault):
   pass

class VAppPropertyFault(VmConfigFault):
   id: str
   category: str
   label: str
   type: str
   value: str

class VAppTaskInProgress(TaskInProgress):
   pass

class VFlashCacheHotConfigNotSupported(VmConfigFault):
   pass


class VFlashModuleNotSupported(VmConfigFault):
   class Reason(pyVmomi.VmomiSupport.Enum):
      CacheModeNotSupported: _typing.ClassVar['Reason'] = 'CacheModeNotSupported'
      CacheConsistencyTypeNotSupported: _typing.ClassVar['Reason'] = 'CacheConsistencyTypeNotSupported'
      CacheBlockSizeNotSupported: _typing.ClassVar['Reason'] = 'CacheBlockSizeNotSupported'
      CacheReservationNotSupported: _typing.ClassVar['Reason'] = 'CacheReservationNotSupported'
      DiskSizeNotSupported: _typing.ClassVar['Reason'] = 'DiskSizeNotSupported'

   vmName: str
   moduleName: str
   reason: str
   hostName: str

class VFlashModuleVersionIncompatible(VimFault):
   moduleName: str
   vmRequestModuleVersion: str
   hostMinSupportedVerson: str
   hostModuleVersion: str

class VMINotSupported(DeviceNotSupported):
   pass

class VMOnConflictDVPort(CannotAccessNetwork):
   pass

class VMOnVirtualIntranet(CannotAccessNetwork):
   pass

class VMotionAcrossNetworkNotSupported(MigrationFeatureNotSupported):
   pass


class VMotionInterfaceIssue(MigrationFault):
   atSourceHost: bool
   failedHost: str
   failedHostEntity: _typing.Optional[pyVmomi.vim.HostSystem] = None

class VMotionLinkCapacityLow(VMotionInterfaceIssue):
   network: str

class VMotionLinkDown(VMotionInterfaceIssue):
   network: str

class VMotionNotConfigured(VMotionInterfaceIssue):
   pass

class VMotionNotLicensed(VMotionInterfaceIssue):
   pass

class VMotionNotSupported(VMotionInterfaceIssue):
   pass

class VMotionProtocolIncompatible(MigrationFault):
   pass


class VimFault(pyVmomi.vmodl.MethodFault):
   pass

class VirtualDiskBlocksNotFullyProvisioned(DeviceBackingNotSupported):
   pass

class VirtualDiskModeNotSupported(DeviceNotSupported):
   mode: str

class VirtualEthernetCardNotSupported(DeviceNotSupported):
   pass

class VirtualHardwareCompatibilityIssue(VmConfigFault):
   pass


class VirtualHardwareVersionNotSupported(VirtualHardwareCompatibilityIssue):
   hostName: str
   host: pyVmomi.vim.HostSystem


class VmAlreadyExistsInDatacenter(InvalidFolder):
   host: pyVmomi.vim.HostSystem
   hostname: str
   vm: list[pyVmomi.vim.VirtualMachine] = []

class VmConfigFault(VimFault):
   pass


class VmConfigIncompatibleForFaultTolerance(VmConfigFault):
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VmConfigIncompatibleForRecordReplay(VmConfigFault):
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VmFaultToleranceConfigIssue(VmFaultToleranceIssue):
   class ReasonForIssue(pyVmomi.VmomiSupport.Enum):
      haNotEnabled: _typing.ClassVar['ReasonForIssue'] = 'haNotEnabled'
      moreThanOneSecondary: _typing.ClassVar['ReasonForIssue'] = 'moreThanOneSecondary'
      recordReplayNotSupported: _typing.ClassVar['ReasonForIssue'] = 'recordReplayNotSupported'
      replayNotSupported: _typing.ClassVar['ReasonForIssue'] = 'replayNotSupported'
      templateVm: _typing.ClassVar['ReasonForIssue'] = 'templateVm'
      multipleVCPU: _typing.ClassVar['ReasonForIssue'] = 'multipleVCPU'
      hostInactive: _typing.ClassVar['ReasonForIssue'] = 'hostInactive'
      ftUnsupportedHardware: _typing.ClassVar['ReasonForIssue'] = 'ftUnsupportedHardware'
      ftUnsupportedProduct: _typing.ClassVar['ReasonForIssue'] = 'ftUnsupportedProduct'
      missingVMotionNic: _typing.ClassVar['ReasonForIssue'] = 'missingVMotionNic'
      missingFTLoggingNic: _typing.ClassVar['ReasonForIssue'] = 'missingFTLoggingNic'
      thinDisk: _typing.ClassVar['ReasonForIssue'] = 'thinDisk'
      verifySSLCertificateFlagNotSet: _typing.ClassVar['ReasonForIssue'] = 'verifySSLCertificateFlagNotSet'
      hasSnapshots: _typing.ClassVar['ReasonForIssue'] = 'hasSnapshots'
      noConfig: _typing.ClassVar['ReasonForIssue'] = 'noConfig'
      ftSecondaryVm: _typing.ClassVar['ReasonForIssue'] = 'ftSecondaryVm'
      hasLocalDisk: _typing.ClassVar['ReasonForIssue'] = 'hasLocalDisk'
      esxAgentVm: _typing.ClassVar['ReasonForIssue'] = 'esxAgentVm'
      video3dEnabled: _typing.ClassVar['ReasonForIssue'] = 'video3dEnabled'
      hasUnsupportedDisk: _typing.ClassVar['ReasonForIssue'] = 'hasUnsupportedDisk'
      insufficientBandwidth: _typing.ClassVar['ReasonForIssue'] = 'insufficientBandwidth'
      hasNestedHVConfiguration: _typing.ClassVar['ReasonForIssue'] = 'hasNestedHVConfiguration'
      hasVFlashConfiguration: _typing.ClassVar['ReasonForIssue'] = 'hasVFlashConfiguration'
      unsupportedProduct: _typing.ClassVar['ReasonForIssue'] = 'unsupportedProduct'
      cpuHvUnsupported: _typing.ClassVar['ReasonForIssue'] = 'cpuHvUnsupported'
      cpuHwmmuUnsupported: _typing.ClassVar['ReasonForIssue'] = 'cpuHwmmuUnsupported'
      cpuHvDisabled: _typing.ClassVar['ReasonForIssue'] = 'cpuHvDisabled'
      hasEFIFirmware: _typing.ClassVar['ReasonForIssue'] = 'hasEFIFirmware'
      tooManyVCPUs: _typing.ClassVar['ReasonForIssue'] = 'tooManyVCPUs'
      tooMuchMemory: _typing.ClassVar['ReasonForIssue'] = 'tooMuchMemory'
      vMotionNotLicensed: _typing.ClassVar['ReasonForIssue'] = 'vMotionNotLicensed'
      ftNotLicensed: _typing.ClassVar['ReasonForIssue'] = 'ftNotLicensed'
      haAgentIssue: _typing.ClassVar['ReasonForIssue'] = 'haAgentIssue'
      unsupportedSPBM: _typing.ClassVar['ReasonForIssue'] = 'unsupportedSPBM'
      hasLinkedCloneDisk: _typing.ClassVar['ReasonForIssue'] = 'hasLinkedCloneDisk'
      unsupportedPMemHAFailOver: _typing.ClassVar['ReasonForIssue'] = 'unsupportedPMemHAFailOver'
      unsupportedEncryptedDisk: _typing.ClassVar['ReasonForIssue'] = 'unsupportedEncryptedDisk'
      ftMetroClusterNotEditable: _typing.ClassVar['ReasonForIssue'] = 'ftMetroClusterNotEditable'
      noHostGroupConfigured: _typing.ClassVar['ReasonForIssue'] = 'noHostGroupConfigured'

   reason: _typing.Optional[str] = None
   entityName: _typing.Optional[str] = None
   entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None


class VmFaultToleranceConfigIssueWrapper(VmFaultToleranceIssue):
   entityName: _typing.Optional[str] = None
   entity: _typing.Optional[pyVmomi.vim.ManagedEntity] = None
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class VmFaultToleranceInvalidFileBacking(VmFaultToleranceIssue):
   class DeviceType(pyVmomi.VmomiSupport.Enum):
      virtualFloppy: _typing.ClassVar['DeviceType'] = 'virtualFloppy'
      virtualCdrom: _typing.ClassVar['DeviceType'] = 'virtualCdrom'
      virtualSerialPort: _typing.ClassVar['DeviceType'] = 'virtualSerialPort'
      virtualParallelPort: _typing.ClassVar['DeviceType'] = 'virtualParallelPort'
      virtualDisk: _typing.ClassVar['DeviceType'] = 'virtualDisk'

   backingType: _typing.Optional[str] = None
   backingFilename: _typing.Optional[str] = None

class VmFaultToleranceIssue(VimFault):
   pass


class VmFaultToleranceOpIssuesList(VmFaultToleranceIssue):
   errors: list[pyVmomi.vmodl.MethodFault] = []
   warnings: list[pyVmomi.vmodl.MethodFault] = []


class VmFaultToleranceTooManyFtVcpusOnHost(InsufficientResourcesFault):
   hostName: _typing.Optional[str] = None
   maxNumFtVcpus: int


class VmFaultToleranceTooManyVMsOnHost(InsufficientResourcesFault):
   hostName: _typing.Optional[str] = None
   maxNumFtVms: int

class VmHostAffinityRuleViolation(VmConfigFault):
   vmName: str
   hostName: str


class VmLimitLicense(pyVmomi.vmodl.fault.NotEnoughLicenses):
   limit: int

class VmMetadataManagerFault(VimFault):
   pass

class VmMonitorIncompatibleForFaultTolerance(VimFault):
   pass

class VmPowerOnDisabled(InvalidState):
   pass


class VmSmpFaultToleranceTooManyVMsOnHost(InsufficientResourcesFault):
   hostName: _typing.Optional[str] = None
   maxNumSmpFtVms: int

class VmToolsUpgradeFault(VimFault):
   pass

class VmValidateMaxDevice(VimFault):
   device: str
   max: int
   count: int


class VmWwnConflict(InvalidVmConfig):
   vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
   host: _typing.Optional[pyVmomi.vim.HostSystem] = None
   name: _typing.Optional[str] = None
   wwn: _typing.Optional[pyVmomi.VmomiSupport.long] = None

class VmfsAlreadyMounted(VmfsMountFault):
   pass

class VmfsAmbiguousMount(VmfsMountFault):
   pass

class VmfsMountFault(HostConfigFault):
   uuid: str

class VmotionInterfaceNotEnabled(HostPowerOpFailed):
   pass

class VolumeEditorError(CustomizationFault):
   pass


class VramLimitLicense(pyVmomi.vmodl.fault.NotEnoughLicenses):
   limit: int

class VsanClusterUuidMismatch(CannotMoveVsanEnabledHost):
   hostClusterUuid: str
   destinationClusterUuid: str


class VsanDiskFault(VsanFault):
   device: _typing.Optional[str] = None

class VsanFault(VimFault):
   pass

class VsanIncompatibleDiskMapping(VsanDiskFault):
   pass


class VsanNodeNotMaster(VimFault):
   vsanMasterUuid: _typing.Optional[str] = None
   cmmdsMasterButNotStatsMaster: _typing.Optional[bool] = None

class VsanSslVerifyCertFault(SSLVerifyFault):
   cert: str

class VspanDestPortConflict(DvsFault):
   vspanSessionKey1: str
   vspanSessionKey2: str
   portKey: str

class VspanPortConflict(DvsFault):
   vspanSessionKey1: str
   vspanSessionKey2: str
   portKey: str

class VspanPortMoveFault(DvsFault):
   srcPortgroupName: str
   destPortgroupName: str
   portKey: str

class VspanPortPromiscChangeFault(DvsFault):
   portKey: str

class VspanPortgroupPromiscChangeFault(DvsFault):
   portgroupName: str

class VspanPortgroupTypeChangeFault(DvsFault):
   portgroupName: str

class VspanPromiscuousPortNotSupported(DvsFault):
   vspanSessionKey: str
   portKey: str

class VspanSameSessionPortConflict(DvsFault):
   vspanSessionKey: str
   portKey: str

class WakeOnLanNotSupported(VirtualHardwareCompatibilityIssue):
   pass

class WakeOnLanNotSupportedByVmotionNIC(HostPowerOpFailed):
   pass


class WillLoseHAProtection(MigrationFault):
   class Resolution(pyVmomi.VmomiSupport.Enum):
      svmotion: _typing.ClassVar['Resolution'] = 'svmotion'
      relocate: _typing.ClassVar['Resolution'] = 'relocate'

   resolution: str

class WillModifyConfigCpuRequirements(MigrationFault):
   pass

class WillResetSnapshotDirectory(MigrationFault):
   pass

class WipeDiskFault(VimFault):
   pass
