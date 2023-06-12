from typing import List, Literal
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, PropertyPath, long
from pyVmomi.vmodl.fault import SecurityError


class ActiveDirectoryFault(VimFault):
    @property
    def errorCode(self) -> int: ...
    @errorCode.setter
    def errorCode(self, value: int):
        self._errorCode = value


class ActiveVMsBlockingEVC(EVCConfigFault):
    @property
    def evcMode(self) -> str: ...
    @evcMode.setter
    def evcMode(self, value: str):
        self._evcMode = value
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @host.setter
    def host(self, value: List[vim.HostSystem]):
        self._host = value
    @property
    def hostName(self) -> List[str]: ...
    @hostName.setter
    def hostName(self, value: List[str]):
        self._hostName = value


class AdminDisabled(HostConfigFault): ...


class AdminNotDisabled(HostConfigFault): ...


class AffinityConfigured(MigrationFault):
    @property
    def configuredAffinity(self) -> List[str]: ...
    @configuredAffinity.setter
    def configuredAffinity(self, value: List[str]):
        self._configuredAffinity = value


    class Affinity(Enum):
        memory = "memory"
        cpu = "cpu"


class AgentInstallFailed(HostConnectFault):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def statusCode(self) -> int: ...
    @statusCode.setter
    def statusCode(self, value: int):
        self._statusCode = value
    @property
    def installerOutput(self) -> str: ...
    @installerOutput.setter
    def installerOutput(self, value: str):
        self._installerOutput = value


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
    @ipAddress.setter
    def ipAddress(self, value: str):
        self._ipAddress = value


class AlreadyConnected(HostConnectFault):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class AlreadyExists(VimFault):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class AlreadyUpgraded(VimFault): ...


class AnswerFileUpdateFailed(VimFault):
    @property
    def failure(self) -> List[AnswerFileUpdateFailed.UpdateFailure]: ...
    @failure.setter
    def failure(self, value: List[AnswerFileUpdateFailed.UpdateFailure]):
        self._failure = value


    class UpdateFailure(vmodl.DynamicData):
        @property
        def userInputPath(self) -> vim.profile.ProfilePropertyPath: ...
        @userInputPath.setter
        def userInputPath(self, value: vim.profile.ProfilePropertyPath):
            self._userInputPath = value
        @property
        def errMsg(self) -> vmodl.LocalizableMessage: ...
        @errMsg.setter
        def errMsg(self, value: vmodl.LocalizableMessage):
            self._errMsg = value


class ApplicationQuiesceFault(SnapshotFault): ...


class AuthMinimumAdminPermission(VimFault): ...


class BackupBlobReadFailure(DvsFault):
    @property
    def entityName(self) -> str: ...
    @entityName.setter
    def entityName(self, value: str):
        self._entityName = value
    @property
    def entityType(self) -> str: ...
    @entityType.setter
    def entityType(self, value: str):
        self._entityType = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class BackupBlobWriteFailure(DvsFault):
    @property
    def entityName(self) -> str: ...
    @entityName.setter
    def entityName(self, value: str):
        self._entityName = value
    @property
    def entityType(self) -> str: ...
    @entityType.setter
    def entityType(self, value: str):
        self._entityType = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class BlockedByFirewall(HostConfigFault): ...


class CAMServerRefusedConnection(InvalidCAMServer): ...


class CannotAccessFile(FileFault): ...


class CannotAccessLocalSource(VimFault): ...


class CannotAccessNetwork(CannotAccessVmDevice):
    @property
    def network(self) -> vim.Network: ...
    @network.setter
    def network(self, value: vim.Network):
        self._network = value


class CannotAccessVmComponent(VmConfigFault): ...


class CannotAccessVmConfig(CannotAccessVmComponent):
    @property
    def reason(self) -> vmodl.MethodFault: ...
    @reason.setter
    def reason(self, value: vmodl.MethodFault):
        self._reason = value


class CannotAccessVmDevice(CannotAccessVmComponent):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value
    @property
    def backing(self) -> str: ...
    @backing.setter
    def backing(self, value: str):
        self._backing = value
    @property
    def connected(self) -> bool: ...
    @connected.setter
    def connected(self, value: bool):
        self._connected = value


class CannotAccessVmDisk(CannotAccessVmDevice):
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class CannotAddHostWithFTVmAsStandalone(HostConnectFault): ...


class CannotAddHostWithFTVmToDifferentCluster(HostConnectFault): ...


class CannotAddHostWithFTVmToNonHACluster(HostConnectFault): ...


class CannotChangeDrsBehaviorForFtSecondary(VmFaultToleranceIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class CannotChangeHaSettingsForFtSecondary(VmFaultToleranceIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class CannotChangeVsanClusterUuid(VsanFault): ...


class CannotChangeVsanNodeUuid(VsanFault): ...


class CannotComputeFTCompatibleHosts(VmFaultToleranceIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class CannotCreateFile(FileFault): ...


class CannotDecryptPasswords(CustomizationFault): ...


class CannotDeleteFile(FileFault): ...


class CannotDisableDrsOnClustersWithVApps(vmodl.RuntimeFault): ...


class CannotDisableSnapshot(VmConfigFault): ...


class CannotDisconnectHostWithFaultToleranceVm(VimFault):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value


class CannotEnableVmcpForCluster(VimFault):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class CannotModifyConfigCpuRequirements(MigrationFault): ...


class CannotMoveFaultToleranceVm(VimFault):
    @property
    def moveType(self) -> str: ...
    @moveType.setter
    def moveType(self, value: str):
        self._moveType = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


    class MoveType(Enum):
        resourcePool = "resourcePool"
        cluster = "cluster"


class CannotMoveHostWithFaultToleranceVm(VimFault): ...


class CannotMoveVmWithDeltaDisk(MigrationFault):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value


class CannotMoveVmWithNativeDeltaDisk(MigrationFault): ...


class CannotMoveVsanEnabledHost(VsanFault): ...


class CannotPlaceWithoutPrerequisiteMoves(VimFault): ...


class CannotPowerOffVmInCluster(InvalidState):
    @property
    def operation(self) -> str: ...
    @operation.setter
    def operation(self, value: str):
        self._operation = value
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


    class Operation(Enum):
        suspend = "suspend"
        powerOff = "powerOff"
        guestShutdown = "guestShutdown"
        guestSuspend = "guestSuspend"


class CannotReconfigureVsanWhenHaEnabled(VsanFault): ...


class CannotUseNetwork(VmConfigFault):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value
    @property
    def backing(self) -> str: ...
    @backing.setter
    def backing(self, value: str):
        self._backing = value
    @property
    def connected(self) -> bool: ...
    @connected.setter
    def connected(self, value: bool):
        self._connected = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def network(self) -> vim.Network: ...
    @network.setter
    def network(self, value: vim.Network):
        self._network = value


class ClockSkew(HostConfigFault): ...


class CloneFromSnapshotNotSupported(MigrationFault): ...


class CollectorAddressUnset(DvsFault): ...


class ConcurrentAccess(VimFault): ...


class ConflictingConfiguration(DvsFault):
    @property
    def configInConflict(self) -> List[ConflictingConfiguration.Config]: ...
    @configInConflict.setter
    def configInConflict(self, value: List[ConflictingConfiguration.Config]):
        self._configInConflict = value


    class Config(vmodl.DynamicData):
        @property
        def entity(self) -> vim.ManagedEntity: ...
        @entity.setter
        def entity(self, value: vim.ManagedEntity):
            self._entity = value
        @property
        def propertyPath(self) -> str: ...
        @propertyPath.setter
        def propertyPath(self, value: str):
            self._propertyPath = value


class ConflictingDatastoreFound(vmodl.RuntimeFault):
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


class ConnectedIso(OvfExport):
    @property
    def cdrom(self) -> vim.vm.device.VirtualCdrom: ...
    @cdrom.setter
    def cdrom(self, value: vim.vm.device.VirtualCdrom):
        self._cdrom = value
    @property
    def filename(self) -> str: ...
    @filename.setter
    def filename(self, value: str):
        self._filename = value


class CpuCompatibilityUnknown(CpuIncompatible): ...


class CpuHotPlugNotSupported(VmConfigFault): ...


class CpuIncompatible(VirtualHardwareCompatibilityIssue):
    @property
    def level(self) -> int: ...
    @level.setter
    def level(self, value: int):
        self._level = value
    @property
    def registerName(self) -> str: ...
    @registerName.setter
    def registerName(self, value: str):
        self._registerName = value
    @property
    def registerBits(self) -> str: ...
    @registerBits.setter
    def registerBits(self, value: str):
        self._registerBits = value
    @property
    def desiredBits(self) -> str: ...
    @desiredBits.setter
    def desiredBits(self, value: str):
        self._desiredBits = value
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value


class CpuIncompatible1ECX(CpuIncompatible):
    @property
    def sse3(self) -> bool: ...
    @sse3.setter
    def sse3(self, value: bool):
        self._sse3 = value
    @property
    def pclmulqdq(self) -> bool: ...
    @pclmulqdq.setter
    def pclmulqdq(self, value: bool):
        self._pclmulqdq = value
    @property
    def ssse3(self) -> bool: ...
    @ssse3.setter
    def ssse3(self, value: bool):
        self._ssse3 = value
    @property
    def sse41(self) -> bool: ...
    @sse41.setter
    def sse41(self, value: bool):
        self._sse41 = value
    @property
    def sse42(self) -> bool: ...
    @sse42.setter
    def sse42(self, value: bool):
        self._sse42 = value
    @property
    def aes(self) -> bool: ...
    @aes.setter
    def aes(self, value: bool):
        self._aes = value
    @property
    def other(self) -> bool: ...
    @other.setter
    def other(self, value: bool):
        self._other = value
    @property
    def otherOnly(self) -> bool: ...
    @otherOnly.setter
    def otherOnly(self, value: bool):
        self._otherOnly = value


class CpuIncompatible81EDX(CpuIncompatible):
    @property
    def nx(self) -> bool: ...
    @nx.setter
    def nx(self, value: bool):
        self._nx = value
    @property
    def ffxsr(self) -> bool: ...
    @ffxsr.setter
    def ffxsr(self, value: bool):
        self._ffxsr = value
    @property
    def rdtscp(self) -> bool: ...
    @rdtscp.setter
    def rdtscp(self, value: bool):
        self._rdtscp = value
    @property
    def lm(self) -> bool: ...
    @lm.setter
    def lm(self, value: bool):
        self._lm = value
    @property
    def other(self) -> bool: ...
    @other.setter
    def other(self, value: bool):
        self._other = value
    @property
    def otherOnly(self) -> bool: ...
    @otherOnly.setter
    def otherOnly(self, value: bool):
        self._otherOnly = value


class CustomizationFault(VimFault): ...


class CustomizationPending(CustomizationFault): ...


class DVPortNotSupported(DeviceBackingNotSupported): ...


class DasConfigFault(VimFault):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def output(self) -> str: ...
    @output.setter
    def output(self, value: str):
        self._output = value
    @property
    def event(self) -> List[vim.event.Event]: ...
    @event.setter
    def event(self, value: List[vim.event.Event]):
        self._event = value


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
    @invalidArgument.setter
    def invalidArgument(self, value: List[DatacenterMismatch.Argument]):
        self._invalidArgument = value
    @property
    def expectedDatacenter(self) -> vim.Datacenter: ...
    @expectedDatacenter.setter
    def expectedDatacenter(self, value: vim.Datacenter):
        self._expectedDatacenter = value


    class Argument(vmodl.DynamicData):
        @property
        def entity(self) -> vim.ManagedEntity: ...
        @entity.setter
        def entity(self, value: vim.ManagedEntity):
            self._entity = value
        @property
        def inputDatacenter(self) -> vim.Datacenter: ...
        @inputDatacenter.setter
        def inputDatacenter(self, value: vim.Datacenter):
            self._inputDatacenter = value


class DatastoreNotWritableOnHost(InvalidDatastore):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value


class DeltaDiskFormatNotSupported(VmConfigFault):
    @property
    def datastore(self) -> List[vim.Datastore]: ...
    @datastore.setter
    def datastore(self, value: List[vim.Datastore]):
        self._datastore = value
    @property
    def deltaDiskFormat(self) -> str: ...
    @deltaDiskFormat.setter
    def deltaDiskFormat(self, value: str):
        self._deltaDiskFormat = value


class DestinationSwitchFull(CannotAccessNetwork): ...


class DestinationVsanDisabled(CannotMoveVsanEnabledHost):
    @property
    def destinationCluster(self) -> str: ...
    @destinationCluster.setter
    def destinationCluster(self, value: str):
        self._destinationCluster = value


class DeviceBackingNotSupported(DeviceNotSupported):
    @property
    def backing(self) -> str: ...
    @backing.setter
    def backing(self, value: str):
        self._backing = value


class DeviceControllerNotSupported(DeviceNotSupported):
    @property
    def controller(self) -> str: ...
    @controller.setter
    def controller(self, value: str):
        self._controller = value


class DeviceHotPlugNotSupported(InvalidDeviceSpec): ...


class DeviceNotFound(InvalidDeviceSpec): ...


class DeviceNotSupported(VirtualHardwareCompatibilityIssue):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class DeviceUnsupportedForVmPlatform(InvalidDeviceSpec): ...


class DeviceUnsupportedForVmVersion(InvalidDeviceSpec):
    @property
    def currentVersion(self) -> str: ...
    @currentVersion.setter
    def currentVersion(self, value: str):
        self._currentVersion = value
    @property
    def expectedVersion(self) -> str: ...
    @expectedVersion.setter
    def expectedVersion(self, value: str):
        self._expectedVersion = value


class DigestNotSupported(DeviceNotSupported): ...


class DirectoryNotEmpty(FileFault): ...


class DisableAdminNotSupported(HostConfigFault): ...


class DisallowedChangeByService(vmodl.RuntimeFault):
    @property
    def serviceName(self) -> str: ...
    @serviceName.setter
    def serviceName(self, value: str):
        self._serviceName = value
    @property
    def disallowedChange(self) -> str: ...
    @disallowedChange.setter
    def disallowedChange(self, value: str):
        self._disallowedChange = value


    class DisallowedChange(Enum):
        hotExtendDisk = "hotExtendDisk"


class DisallowedDiskModeChange(InvalidDeviceSpec): ...


class DisallowedMigrationDeviceAttached(MigrationFault):
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class DisallowedOperationOnFailoverHost(vmodl.RuntimeFault):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def hostname(self) -> str: ...
    @hostname.setter
    def hostname(self, value: str):
        self._hostname = value


class DisconnectedHostsBlockingEVC(EVCConfigFault): ...


class DiskHasPartitions(VsanDiskFault): ...


class DiskIsLastRemainingNonSSD(VsanDiskFault): ...


class DiskIsNonLocal(VsanDiskFault): ...


class DiskIsUSB(VsanDiskFault): ...


class DiskMoveTypeNotSupported(MigrationFault): ...


class DiskNotSupported(VirtualHardwareCompatibilityIssue):
    @property
    def disk(self) -> int: ...
    @disk.setter
    def disk(self, value: int):
        self._disk = value


class DiskTooSmall(VsanDiskFault): ...


class DomainNotFound(ActiveDirectoryFault):
    @property
    def domainName(self) -> str: ...
    @domainName.setter
    def domainName(self, value: str):
        self._domainName = value


class DrsDisabledOnVm(VimFault): ...


class DrsVmotionIncompatibleFault(VirtualHardwareCompatibilityIssue):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value


class DuplicateDisks(VsanDiskFault): ...


class DuplicateName(VimFault):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def object(self) -> ManagedObject: ...
    @object.setter
    def object(self, value: ManagedObject):
        self._object = value


class DuplicateVsanNetworkInterface(VsanFault):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value


class DvsApplyOperationFault(DvsFault):
    @property
    def objectFault(self) -> List[DvsApplyOperationFault.FaultOnObject]: ...
    @objectFault.setter
    def objectFault(self, value: List[DvsApplyOperationFault.FaultOnObject]):
        self._objectFault = value


    class FaultOnObject(vmodl.DynamicData):
        @property
        def objectId(self) -> str: ...
        @objectId.setter
        def objectId(self, value: str):
            self._objectId = value
        @property
        def type(self) -> type: ...
        @type.setter
        def type(self, value: type):
            self._type = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


class DvsFault(VimFault): ...


class DvsNotAuthorized(DvsFault):
    @property
    def sessionExtensionKey(self) -> str: ...
    @sessionExtensionKey.setter
    def sessionExtensionKey(self, value: str):
        self._sessionExtensionKey = value
    @property
    def dvsExtensionKey(self) -> str: ...
    @dvsExtensionKey.setter
    def dvsExtensionKey(self, value: str):
        self._dvsExtensionKey = value


class DvsOperationBulkFault(DvsFault):
    @property
    def hostFault(self) -> List[DvsOperationBulkFault.FaultOnHost]: ...
    @hostFault.setter
    def hostFault(self, value: List[DvsOperationBulkFault.FaultOnHost]):
        self._hostFault = value


    class FaultOnHost(vmodl.DynamicData):
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


class DvsScopeViolated(DvsFault):
    @property
    def scope(self) -> List[vim.ManagedEntity]: ...
    @scope.setter
    def scope(self, value: List[vim.ManagedEntity]):
        self._scope = value
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @entity.setter
    def entity(self, value: vim.ManagedEntity):
        self._entity = value


class EVCAdmissionFailed(NotSupportedHostInCluster):
    @property
    def faults(self) -> List[vmodl.MethodFault]: ...
    @faults.setter
    def faults(self, value: List[vmodl.MethodFault]):
        self._faults = value


class EVCAdmissionFailedCPUFeaturesForMode(EVCAdmissionFailed):
    @property
    def currentEVCModeKey(self) -> str: ...
    @currentEVCModeKey.setter
    def currentEVCModeKey(self, value: str):
        self._currentEVCModeKey = value


class EVCAdmissionFailedCPUModel(EVCAdmissionFailed): ...


class EVCAdmissionFailedCPUModelForMode(EVCAdmissionFailed):
    @property
    def currentEVCModeKey(self) -> str: ...
    @currentEVCModeKey.setter
    def currentEVCModeKey(self, value: str):
        self._currentEVCModeKey = value


class EVCAdmissionFailedCPUVendor(EVCAdmissionFailed):
    @property
    def clusterCPUVendor(self) -> str: ...
    @clusterCPUVendor.setter
    def clusterCPUVendor(self, value: str):
        self._clusterCPUVendor = value
    @property
    def hostCPUVendor(self) -> str: ...
    @hostCPUVendor.setter
    def hostCPUVendor(self, value: str):
        self._hostCPUVendor = value


class EVCAdmissionFailedCPUVendorUnknown(EVCAdmissionFailed): ...


class EVCAdmissionFailedHostDisconnected(EVCAdmissionFailed): ...


class EVCAdmissionFailedHostSoftware(EVCAdmissionFailed): ...


class EVCAdmissionFailedHostSoftwareForMode(EVCAdmissionFailed): ...


class EVCAdmissionFailedVmActive(EVCAdmissionFailed): ...


class EVCConfigFault(VimFault):
    @property
    def faults(self) -> List[vmodl.MethodFault]: ...
    @faults.setter
    def faults(self, value: List[vmodl.MethodFault]):
        self._faults = value


class EVCModeIllegalByVendor(EVCConfigFault):
    @property
    def clusterCPUVendor(self) -> str: ...
    @clusterCPUVendor.setter
    def clusterCPUVendor(self, value: str):
        self._clusterCPUVendor = value
    @property
    def modeCPUVendor(self) -> str: ...
    @modeCPUVendor.setter
    def modeCPUVendor(self, value: str):
        self._modeCPUVendor = value


class EVCModeUnsupportedByHosts(EVCConfigFault):
    @property
    def evcMode(self) -> str: ...
    @evcMode.setter
    def evcMode(self, value: str):
        self._evcMode = value
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @host.setter
    def host(self, value: List[vim.HostSystem]):
        self._host = value
    @property
    def hostName(self) -> List[str]: ...
    @hostName.setter
    def hostName(self, value: List[str]):
        self._hostName = value


class EVCUnsupportedByHostHardware(EVCConfigFault):
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @host.setter
    def host(self, value: List[vim.HostSystem]):
        self._host = value
    @property
    def hostName(self) -> List[str]: ...
    @hostName.setter
    def hostName(self, value: List[str]):
        self._hostName = value


class EVCUnsupportedByHostSoftware(EVCConfigFault):
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @host.setter
    def host(self, value: List[vim.HostSystem]):
        self._host = value
    @property
    def hostName(self) -> List[str]: ...
    @hostName.setter
    def hostName(self, value: List[str]):
        self._hostName = value


class EightHostLimitViolated(VmConfigFault): ...


class EncryptionKeyRequired(InvalidState):
    @property
    def requiredKey(self) -> List[vim.encryption.CryptoKeyId]: ...
    @requiredKey.setter
    def requiredKey(self, value: List[vim.encryption.CryptoKeyId]):
        self._requiredKey = value


class ExpiredAddonLicense(ExpiredFeatureLicense): ...


class ExpiredEditionLicense(ExpiredFeatureLicense): ...


class ExpiredFeatureLicense(NotEnoughLicenses):
    @property
    def feature(self) -> str: ...
    @feature.setter
    def feature(self, value: str):
        self._feature = value
    @property
    def count(self) -> int: ...
    @count.setter
    def count(self, value: int):
        self._count = value
    @property
    def expirationDate(self) -> datetime: ...
    @expirationDate.setter
    def expirationDate(self, value: datetime):
        self._expirationDate = value


class ExtendedFault(VimFault):
    @property
    def faultTypeId(self) -> str: ...
    @faultTypeId.setter
    def faultTypeId(self, value: str):
        self._faultTypeId = value
    @property
    def data(self) -> List[vim.KeyValue]: ...
    @data.setter
    def data(self, value: List[vim.KeyValue]):
        self._data = value


class FailToEnableSPBM(NotEnoughLicenses):
    @property
    def cs(self) -> vim.ComputeResource: ...
    @cs.setter
    def cs(self, value: vim.ComputeResource):
        self._cs = value
    @property
    def csName(self) -> str: ...
    @csName.setter
    def csName(self, value: str):
        self._csName = value
    @property
    def hostLicenseStates(self) -> List[vim.ComputeResource.HostSPBMLicenseInfo]: ...
    @hostLicenseStates.setter
    def hostLicenseStates(self, value: List[vim.ComputeResource.HostSPBMLicenseInfo]):
        self._hostLicenseStates = value


class FailToLockFaultToleranceVMs(vmodl.RuntimeFault):
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def alreadyLockedVm(self) -> vim.VirtualMachine: ...
    @alreadyLockedVm.setter
    def alreadyLockedVm(self, value: vim.VirtualMachine):
        self._alreadyLockedVm = value


class FaultToleranceAntiAffinityViolated(MigrationFault):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value


class FaultToleranceCannotEditMem(VmConfigFault):
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value


class FaultToleranceCpuIncompatible(CpuIncompatible):
    @property
    def model(self) -> bool: ...
    @model.setter
    def model(self, value: bool):
        self._model = value
    @property
    def family(self) -> bool: ...
    @family.setter
    def family(self, value: bool):
        self._family = value
    @property
    def stepping(self) -> bool: ...
    @stepping.setter
    def stepping(self, value: bool):
        self._stepping = value


class FaultToleranceNeedsThickDisk(MigrationFault):
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class FaultToleranceNotLicensed(VmFaultToleranceIssue):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value


class FaultToleranceNotSameBuild(MigrationFault):
    @property
    def build(self) -> str: ...
    @build.setter
    def build(self, value: str):
        self._build = value


class FaultTolerancePrimaryPowerOnNotAttempted(VmFaultToleranceIssue):
    @property
    def secondaryVm(self) -> vim.VirtualMachine: ...
    @secondaryVm.setter
    def secondaryVm(self, value: vim.VirtualMachine):
        self._secondaryVm = value
    @property
    def primaryVm(self) -> vim.VirtualMachine: ...
    @primaryVm.setter
    def primaryVm(self, value: vim.VirtualMachine):
        self._primaryVm = value


class FaultToleranceVmNotDasProtected(VimFault):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class FcoeFault(VimFault): ...


class FcoeFaultPnicHasNoPortSet(FcoeFault):
    @property
    def nicDevice(self) -> str: ...
    @nicDevice.setter
    def nicDevice(self, value: str):
        self._nicDevice = value


class FeatureRequirementsNotMet(VirtualHardwareCompatibilityIssue):
    @property
    def featureRequirement(self) -> List[vim.vm.FeatureRequirement]: ...
    @featureRequirement.setter
    def featureRequirement(self, value: List[vim.vm.FeatureRequirement]):
        self._featureRequirement = value
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value


class FileAlreadyExists(FileFault): ...


class FileBackedPortNotSupported(DeviceNotSupported): ...


class FileFault(VimFault):
    @property
    def file(self) -> str: ...
    @file.setter
    def file(self, value: str):
        self._file = value


class FileLocked(FileFault): ...


class FileNameTooLong(FileFault): ...


class FileNotFound(FileFault): ...


class FileNotWritable(FileFault): ...


class FileTooLarge(FileFault):
    @property
    def datastore(self) -> str: ...
    @datastore.setter
    def datastore(self, value: str):
        self._datastore = value
    @property
    def fileSize(self) -> long: ...
    @fileSize.setter
    def fileSize(self, value: long):
        self._fileSize = value
    @property
    def maxFileSize(self) -> long: ...
    @maxFileSize.setter
    def maxFileSize(self, value: long):
        self._maxFileSize = value


class FilesystemQuiesceFault(SnapshotFault): ...


class FilterInUse(ResourceInUse):
    @property
    def disk(self) -> List[vim.vm.device.VirtualDiskId]: ...
    @disk.setter
    def disk(self, value: List[vim.vm.device.VirtualDiskId]):
        self._disk = value


class FtIssuesOnHost(VmFaultToleranceIssue):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def errors(self) -> List[vmodl.MethodFault]: ...
    @errors.setter
    def errors(self, value: List[vmodl.MethodFault]):
        self._errors = value


    class HostSelectionType(Enum):
        user = "user"
        vc = "vc"
        drs = "drs"


class FullStorageVMotionNotSupported(MigrationFeatureNotSupported): ...


class GatewayConnectFault(HostConnectFault):
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
    def gatewayInfo(self) -> str: ...
    @gatewayInfo.setter
    def gatewayInfo(self, value: str):
        self._gatewayInfo = value
    @property
    def details(self) -> vmodl.LocalizableMessage: ...
    @details.setter
    def details(self, value: vmodl.LocalizableMessage):
        self._details = value


class GatewayHostNotReachable(GatewayToHostConnectFault): ...


class GatewayNotFound(GatewayConnectFault): ...


class GatewayNotReachable(GatewayConnectFault): ...


class GatewayOperationRefused(GatewayConnectFault): ...


class GatewayToHostAuthFault(GatewayToHostConnectFault):
    @property
    def invalidProperties(self) -> List[str]: ...
    @invalidProperties.setter
    def invalidProperties(self, value: List[str]):
        self._invalidProperties = value
    @property
    def missingProperties(self) -> List[str]: ...
    @missingProperties.setter
    def missingProperties(self, value: List[str]):
        self._missingProperties = value


class GatewayToHostConnectFault(GatewayConnectFault):
    @property
    def hostname(self) -> str: ...
    @hostname.setter
    def hostname(self, value: str):
        self._hostname = value
    @property
    def port(self) -> int: ...
    @port.setter
    def port(self, value: int):
        self._port = value


class GatewayToHostTrustVerifyFault(GatewayToHostConnectFault):
    @property
    def verificationToken(self) -> str: ...
    @verificationToken.setter
    def verificationToken(self, value: str):
        self._verificationToken = value
    @property
    def propertiesToVerify(self) -> List[vim.KeyValue]: ...
    @propertiesToVerify.setter
    def propertiesToVerify(self, value: List[vim.KeyValue]):
        self._propertiesToVerify = value


class GenericDrsFault(VimFault):
    @property
    def hostFaults(self) -> List[vmodl.MethodFault]: ...
    @hostFaults.setter
    def hostFaults(self, value: List[vmodl.MethodFault]):
        self._hostFaults = value


class GenericVmConfigFault(VmConfigFault):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class GuestAuthenticationChallenge(GuestOperationsFault):
    @property
    def serverChallenge(self) -> vim.vm.guest.GuestAuthentication: ...
    @serverChallenge.setter
    def serverChallenge(self, value: vim.vm.guest.GuestAuthentication):
        self._serverChallenge = value
    @property
    def sessionID(self) -> long: ...
    @sessionID.setter
    def sessionID(self, value: long):
        self._sessionID = value


class GuestComponentsOutOfDate(GuestOperationsFault): ...


class GuestMultipleMappings(GuestOperationsFault): ...


class GuestOperationsFault(VimFault): ...


class GuestOperationsUnavailable(GuestOperationsFault): ...


class GuestPermissionDenied(GuestOperationsFault): ...


class GuestProcessNotFound(GuestOperationsFault):
    @property
    def pid(self) -> long: ...
    @pid.setter
    def pid(self, value: long):
        self._pid = value


class GuestRegistryFault(GuestOperationsFault):
    @property
    def windowsSystemErrorCode(self) -> long: ...
    @windowsSystemErrorCode.setter
    def windowsSystemErrorCode(self, value: long):
        self._windowsSystemErrorCode = value


class GuestRegistryKeyAlreadyExists(GuestRegistryKeyFault): ...


class GuestRegistryKeyFault(GuestRegistryFault):
    @property
    def keyName(self) -> str: ...
    @keyName.setter
    def keyName(self, value: str):
        self._keyName = value


class GuestRegistryKeyHasSubkeys(GuestRegistryKeyFault): ...


class GuestRegistryKeyInvalid(GuestRegistryKeyFault): ...


class GuestRegistryKeyParentVolatile(GuestRegistryKeyFault): ...


class GuestRegistryValueFault(GuestRegistryFault):
    @property
    def keyName(self) -> str: ...
    @keyName.setter
    def keyName(self, value: str):
        self._keyName = value
    @property
    def valueName(self) -> str: ...
    @valueName.setter
    def valueName(self, value: str):
        self._valueName = value


class GuestRegistryValueNotFound(GuestRegistryValueFault): ...


class HAErrorsAtDest(MigrationFault): ...


class HeterogenousHostsBlockingEVC(EVCConfigFault): ...


class HostAccessRestrictedToManagementServer(NotSupported):
    @property
    def managementServer(self) -> str: ...
    @managementServer.setter
    def managementServer(self, value: str):
        self._managementServer = value


class HostConfigFailed(HostConfigFault):
    @property
    def failure(self) -> List[vmodl.MethodFault]: ...
    @failure.setter
    def failure(self, value: List[vmodl.MethodFault]):
        self._failure = value


class HostConfigFault(VimFault): ...


class HostConnectFault(VimFault): ...


class HostHasComponentFailure(VimFault):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def componentType(self) -> str: ...
    @componentType.setter
    def componentType(self, value: str):
        self._componentType = value
    @property
    def componentName(self) -> str: ...
    @componentName.setter
    def componentName(self, value: str):
        self._componentName = value


    class HostComponentType(Enum):
        Datastore = "Datastore"


class HostInDomain(HostConfigFault): ...


class HostIncompatibleForFaultTolerance(VmFaultToleranceIssue):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class HostIncompatibleForRecordReplay(VimFault):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class HostInventoryFull(NotEnoughLicenses):
    @property
    def capacity(self) -> int: ...
    @capacity.setter
    def capacity(self, value: int):
        self._capacity = value


class HostPowerOpFailed(VimFault): ...


class HostSpecificationOperationFailed(VimFault):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value


class HotSnapshotMoveNotSupported(SnapshotCopyNotSupported): ...


class HttpFault(VimFault):
    @property
    def statusCode(self) -> int: ...
    @statusCode.setter
    def statusCode(self, value: int):
        self._statusCode = value
    @property
    def statusMessage(self) -> str: ...
    @statusMessage.setter
    def statusMessage(self, value: str):
        self._statusMessage = value


class IDEDiskNotSupported(DiskNotSupported): ...


class IORMNotSupportedHostOnDatastore(VimFault):
    @property
    def datastore(self) -> vim.Datastore: ...
    @datastore.setter
    def datastore(self, value: vim.Datastore):
        self._datastore = value
    @property
    def datastoreName(self) -> str: ...
    @datastoreName.setter
    def datastoreName(self, value: str):
        self._datastoreName = value
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @host.setter
    def host(self, value: List[vim.HostSystem]):
        self._host = value


class ImportHostAddFailure(DvsFault):
    @property
    def hostIp(self) -> List[str]: ...
    @hostIp.setter
    def hostIp(self, value: List[str]):
        self._hostIp = value


class ImportOperationBulkFault(DvsFault):
    @property
    def importFaults(self) -> List[ImportOperationBulkFault.FaultOnImport]: ...
    @importFaults.setter
    def importFaults(self, value: List[ImportOperationBulkFault.FaultOnImport]):
        self._importFaults = value


    class FaultOnImport(vmodl.DynamicData):
        @property
        def entityType(self) -> str: ...
        @entityType.setter
        def entityType(self, value: str):
            self._entityType = value
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


class InUseFeatureManipulationDisallowed(NotEnoughLicenses): ...


class InaccessibleDatastore(InvalidDatastore):
    @property
    def detail(self) -> str: ...
    @detail.setter
    def detail(self, value: str):
        self._detail = value


class InaccessibleFTMetadataDatastore(InaccessibleDatastore): ...


class InaccessibleVFlashSource(VimFault):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value


class IncompatibleDefaultDevice(MigrationFault):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value


class IncompatibleHostForFtSecondary(VmFaultToleranceIssue):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def error(self) -> List[vmodl.MethodFault]: ...
    @error.setter
    def error(self, value: List[vmodl.MethodFault]):
        self._error = value


class IncompatibleHostForVmReplication(ReplicationFault):
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


    class IncompatibleReason(Enum):
        rpo = "rpo"
        netCompression = "netCompression"


class IncompatibleSetting(InvalidArgument):
    @property
    def conflictingProperty(self) -> PropertyPath: ...
    @conflictingProperty.setter
    def conflictingProperty(self, value: PropertyPath):
        self._conflictingProperty = value


class IncorrectFileType(FileFault): ...


class IncorrectHostInformation(NotEnoughLicenses): ...


class IndependentDiskVMotionNotSupported(MigrationFeatureNotSupported): ...


class InsufficientAgentVmsDeployed(InsufficientResourcesFault):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def requiredNumAgentVms(self) -> int: ...
    @requiredNumAgentVms.setter
    def requiredNumAgentVms(self, value: int):
        self._requiredNumAgentVms = value
    @property
    def currentNumAgentVms(self) -> int: ...
    @currentNumAgentVms.setter
    def currentNumAgentVms(self, value: int):
        self._currentNumAgentVms = value


class InsufficientCpuResourcesFault(InsufficientResourcesFault):
    @property
    def unreserved(self) -> long: ...
    @unreserved.setter
    def unreserved(self, value: long):
        self._unreserved = value
    @property
    def requested(self) -> long: ...
    @requested.setter
    def requested(self, value: long):
        self._requested = value


class InsufficientDisks(VsanDiskFault): ...


class InsufficientFailoverResourcesFault(InsufficientResourcesFault): ...


class InsufficientGraphicsResourcesFault(InsufficientResourcesFault): ...


class InsufficientHostCapacityFault(InsufficientResourcesFault):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value


class InsufficientHostCpuCapacityFault(InsufficientHostCapacityFault):
    @property
    def unreserved(self) -> long: ...
    @unreserved.setter
    def unreserved(self, value: long):
        self._unreserved = value
    @property
    def requested(self) -> long: ...
    @requested.setter
    def requested(self, value: long):
        self._requested = value


class InsufficientHostMemoryCapacityFault(InsufficientHostCapacityFault):
    @property
    def unreserved(self) -> long: ...
    @unreserved.setter
    def unreserved(self, value: long):
        self._unreserved = value
    @property
    def requested(self) -> long: ...
    @requested.setter
    def requested(self, value: long):
        self._requested = value


class InsufficientMemoryResourcesFault(InsufficientResourcesFault):
    @property
    def unreserved(self) -> long: ...
    @unreserved.setter
    def unreserved(self, value: long):
        self._unreserved = value
    @property
    def requested(self) -> long: ...
    @requested.setter
    def requested(self, value: long):
        self._requested = value


class InsufficientNetworkCapacity(InsufficientResourcesFault): ...


class InsufficientNetworkResourcePoolCapacity(InsufficientResourcesFault):
    @property
    def dvsName(self) -> str: ...
    @dvsName.setter
    def dvsName(self, value: str):
        self._dvsName = value
    @property
    def dvsUuid(self) -> str: ...
    @dvsUuid.setter
    def dvsUuid(self, value: str):
        self._dvsUuid = value
    @property
    def resourcePoolKey(self) -> str: ...
    @resourcePoolKey.setter
    def resourcePoolKey(self, value: str):
        self._resourcePoolKey = value
    @property
    def available(self) -> long: ...
    @available.setter
    def available(self, value: long):
        self._available = value
    @property
    def requested(self) -> long: ...
    @requested.setter
    def requested(self, value: long):
        self._requested = value
    @property
    def device(self) -> List[str]: ...
    @device.setter
    def device(self, value: List[str]):
        self._device = value


class InsufficientPerCpuCapacity(InsufficientHostCapacityFault): ...


class InsufficientResourcesFault(VimFault): ...


class InsufficientStandbyCpuResource(InsufficientStandbyResource):
    @property
    def available(self) -> long: ...
    @available.setter
    def available(self, value: long):
        self._available = value
    @property
    def requested(self) -> long: ...
    @requested.setter
    def requested(self, value: long):
        self._requested = value


class InsufficientStandbyMemoryResource(InsufficientStandbyResource):
    @property
    def available(self) -> long: ...
    @available.setter
    def available(self, value: long):
        self._available = value
    @property
    def requested(self) -> long: ...
    @requested.setter
    def requested(self, value: long):
        self._requested = value


class InsufficientStandbyResource(InsufficientResourcesFault): ...


class InsufficientStorageIops(VimFault):
    @property
    def unreservedIops(self) -> long: ...
    @unreservedIops.setter
    def unreservedIops(self, value: long):
        self._unreservedIops = value
    @property
    def requestedIops(self) -> long: ...
    @requestedIops.setter
    def requestedIops(self, value: long):
        self._requestedIops = value
    @property
    def datastoreName(self) -> str: ...
    @datastoreName.setter
    def datastoreName(self, value: str):
        self._datastoreName = value


class InsufficientStorageSpace(InsufficientResourcesFault): ...


class InsufficientVFlashResourcesFault(InsufficientResourcesFault):
    @property
    def freeSpaceInMB(self) -> long: ...
    @freeSpaceInMB.setter
    def freeSpaceInMB(self, value: long):
        self._freeSpaceInMB = value
    @property
    def freeSpace(self) -> long: ...
    @freeSpace.setter
    def freeSpace(self, value: long):
        self._freeSpace = value
    @property
    def requestedSpaceInMB(self) -> long: ...
    @requestedSpaceInMB.setter
    def requestedSpaceInMB(self, value: long):
        self._requestedSpaceInMB = value
    @property
    def requestedSpace(self) -> long: ...
    @requestedSpace.setter
    def requestedSpace(self, value: long):
        self._requestedSpace = value


class InvalidAffinitySettingFault(VimFault): ...


class InvalidBmcRole(VimFault): ...


class InvalidBundle(PlatformConfigFault): ...


class InvalidCAMCertificate(InvalidCAMServer): ...


class InvalidCAMServer(ActiveDirectoryFault):
    @property
    def camServer(self) -> str: ...
    @camServer.setter
    def camServer(self, value: str):
        self._camServer = value


class InvalidClientCertificate(InvalidLogin): ...


class InvalidController(InvalidDeviceSpec):
    @property
    def controllerKey(self) -> int: ...
    @controllerKey.setter
    def controllerKey(self, value: int):
        self._controllerKey = value


class InvalidDasConfigArgument(InvalidArgument):
    @property
    def entry(self) -> str: ...
    @entry.setter
    def entry(self, value: str):
        self._entry = value
    @property
    def clusterName(self) -> str: ...
    @clusterName.setter
    def clusterName(self, value: str):
        self._clusterName = value


    class EntryForInvalidArgument(Enum):
        admissionControl = "admissionControl"
        userHeartbeatDs = "userHeartbeatDs"
        vmConfig = "vmConfig"


class InvalidDasRestartPriorityForFtVm(InvalidArgument):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class InvalidDatastore(VimFault):
    @property
    def datastore(self) -> vim.Datastore: ...
    @datastore.setter
    def datastore(self, value: vim.Datastore):
        self._datastore = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class InvalidDatastorePath(InvalidDatastore):
    @property
    def datastorePath(self) -> str: ...
    @datastorePath.setter
    def datastorePath(self, value: str):
        self._datastorePath = value


class InvalidDatastoreState(InvalidState):
    @property
    def datastoreName(self) -> str: ...
    @datastoreName.setter
    def datastoreName(self, value: str):
        self._datastoreName = value


class InvalidDeviceBacking(InvalidDeviceSpec): ...


class InvalidDeviceOperation(InvalidDeviceSpec):
    @property
    def badOp(self) -> vim.vm.device.VirtualDeviceSpec.Operation | Literal['add', 'remove', 'edit']: ...
    @badOp.setter
    def badOp(self, value: vim.vm.device.VirtualDeviceSpec.Operation | Literal['add', 'remove', 'edit']):
        self._badOp = value
    @property
    def badFileOp(self) -> vim.vm.device.VirtualDeviceSpec.FileOperation | Literal['create', 'destroy', 'replace']: ...
    @badFileOp.setter
    def badFileOp(self, value: vim.vm.device.VirtualDeviceSpec.FileOperation | Literal['create', 'destroy', 'replace']):
        self._badFileOp = value


class InvalidDeviceSpec(InvalidVmConfig):
    @property
    def deviceIndex(self) -> int: ...
    @deviceIndex.setter
    def deviceIndex(self, value: int):
        self._deviceIndex = value


class InvalidDiskFormat(InvalidFormat): ...


class InvalidDrsBehaviorForFtVm(InvalidArgument):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class InvalidEditionLicense(NotEnoughLicenses):
    @property
    def feature(self) -> str: ...
    @feature.setter
    def feature(self, value: str):
        self._feature = value


class InvalidEvent(VimFault): ...


class InvalidFolder(VimFault):
    @property
    def target(self) -> vim.ManagedEntity: ...
    @target.setter
    def target(self, value: vim.ManagedEntity):
        self._target = value


class InvalidFormat(VmConfigFault): ...


class InvalidGuestLogin(GuestOperationsFault): ...


class InvalidHostConnectionState(InvalidHostState): ...


class InvalidHostName(HostConfigFault): ...


class InvalidHostState(InvalidState):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value


class InvalidIndexArgument(InvalidArgument):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class InvalidIpfixConfig(DvsFault):
    @property
    def property(self) -> PropertyPath: ...
    @property.setter
    def property(self, value: PropertyPath):
        self._property = value


class InvalidIpmiLoginInfo(VimFault): ...


class InvalidIpmiMacAddress(VimFault):
    @property
    def userProvidedMacAddress(self) -> str: ...
    @userProvidedMacAddress.setter
    def userProvidedMacAddress(self, value: str):
        self._userProvidedMacAddress = value
    @property
    def observedMacAddress(self) -> str: ...
    @observedMacAddress.setter
    def observedMacAddress(self, value: str):
        self._observedMacAddress = value


class InvalidLicense(VimFault):
    @property
    def licenseContent(self) -> str: ...
    @licenseContent.setter
    def licenseContent(self, value: str):
        self._licenseContent = value


class InvalidLocale(VimFault): ...


class InvalidLogin(VimFault): ...


class InvalidName(VimFault):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @entity.setter
    def entity(self, value: vim.ManagedEntity):
        self._entity = value


class InvalidNasCredentials(NasConfigFault):
    @property
    def userName(self) -> str: ...
    @userName.setter
    def userName(self, value: str):
        self._userName = value


class InvalidNetworkInType(VAppPropertyFault): ...


class InvalidNetworkResource(NasConfigFault):
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


class InvalidOperationOnSecondaryVm(VmFaultToleranceIssue):
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value


class InvalidPowerState(InvalidState):
    @property
    def requestedState(self) -> vim.VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended']: ...
    @requestedState.setter
    def requestedState(self, value: vim.VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended']):
        self._requestedState = value
    @property
    def existingState(self) -> vim.VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended']: ...
    @existingState.setter
    def existingState(self, value: vim.VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended']):
        self._existingState = value


class InvalidPrivilege(VimFault):
    @property
    def privilege(self) -> str: ...
    @privilege.setter
    def privilege(self, value: str):
        self._privilege = value


class InvalidProfileReferenceHost(vmodl.RuntimeFault):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def profile(self) -> vim.profile.Profile: ...
    @profile.setter
    def profile(self, value: vim.profile.Profile):
        self._profile = value
    @property
    def profileName(self) -> str: ...
    @profileName.setter
    def profileName(self, value: str):
        self._profileName = value


class InvalidPropertyType(VAppPropertyFault): ...


class InvalidPropertyValue(VAppPropertyFault): ...


class InvalidResourcePoolStructureFault(InsufficientResourcesFault): ...


class InvalidSnapshotFormat(InvalidFormat): ...


class InvalidState(VimFault): ...


class InvalidVmConfig(VmConfigFault):
    @property
    def property(self) -> PropertyPath: ...
    @property.setter
    def property(self, value: PropertyPath):
        self._property = value


class InvalidVmState(InvalidState):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value


class InventoryHasStandardAloneHosts(NotEnoughLicenses):
    @property
    def hosts(self) -> List[str]: ...
    @hosts.setter
    def hosts(self, value: List[str]):
        self._hosts = value


class IpHostnameGeneratorError(CustomizationFault): ...


class IscsiFault(VimFault): ...


class IscsiFaultInvalidVnic(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...
    @vnicDevice.setter
    def vnicDevice(self, value: str):
        self._vnicDevice = value


class IscsiFaultPnicInUse(IscsiFault):
    @property
    def pnicDevice(self) -> str: ...
    @pnicDevice.setter
    def pnicDevice(self, value: str):
        self._pnicDevice = value


class IscsiFaultVnicAlreadyBound(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...
    @vnicDevice.setter
    def vnicDevice(self, value: str):
        self._vnicDevice = value


class IscsiFaultVnicHasActivePaths(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...
    @vnicDevice.setter
    def vnicDevice(self, value: str):
        self._vnicDevice = value


class IscsiFaultVnicHasMultipleUplinks(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...
    @vnicDevice.setter
    def vnicDevice(self, value: str):
        self._vnicDevice = value


class IscsiFaultVnicHasNoUplinks(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...
    @vnicDevice.setter
    def vnicDevice(self, value: str):
        self._vnicDevice = value


class IscsiFaultVnicHasWrongUplink(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...
    @vnicDevice.setter
    def vnicDevice(self, value: str):
        self._vnicDevice = value


class IscsiFaultVnicInUse(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...
    @vnicDevice.setter
    def vnicDevice(self, value: str):
        self._vnicDevice = value


class IscsiFaultVnicIsLastPath(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...
    @vnicDevice.setter
    def vnicDevice(self, value: str):
        self._vnicDevice = value


class IscsiFaultVnicNotBound(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...
    @vnicDevice.setter
    def vnicDevice(self, value: str):
        self._vnicDevice = value


class IscsiFaultVnicNotFound(IscsiFault):
    @property
    def vnicDevice(self) -> str: ...
    @vnicDevice.setter
    def vnicDevice(self, value: str):
        self._vnicDevice = value


class KeyNotFound(VimFault):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class LargeRDMConversionNotSupported(MigrationFault):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value


class LargeRDMNotSupportedOnDatastore(VmConfigFault):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value
    @property
    def datastore(self) -> vim.Datastore: ...
    @datastore.setter
    def datastore(self, value: vim.Datastore):
        self._datastore = value
    @property
    def datastoreName(self) -> str: ...
    @datastoreName.setter
    def datastoreName(self, value: str):
        self._datastoreName = value


class LegacyNetworkInterfaceInUse(CannotAccessNetwork): ...


class LicenseAssignmentFailed(vmodl.RuntimeFault):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class LicenseDowngradeDisallowed(NotEnoughLicenses):
    @property
    def edition(self) -> str: ...
    @edition.setter
    def edition(self, value: str):
        self._edition = value
    @property
    def entityId(self) -> str: ...
    @entityId.setter
    def entityId(self, value: str):
        self._entityId = value
    @property
    def features(self) -> List[vmodl.KeyAnyValue]: ...
    @features.setter
    def features(self, value: List[vmodl.KeyAnyValue]):
        self._features = value


class LicenseEntityNotFound(VimFault):
    @property
    def entityId(self) -> str: ...
    @entityId.setter
    def entityId(self, value: str):
        self._entityId = value


class LicenseExpired(NotEnoughLicenses):
    @property
    def licenseKey(self) -> str: ...
    @licenseKey.setter
    def licenseKey(self, value: str):
        self._licenseKey = value


class LicenseKeyEntityMismatch(NotEnoughLicenses): ...


class LicenseRestricted(NotEnoughLicenses): ...


class LicenseServerUnavailable(VimFault):
    @property
    def licenseServer(self) -> str: ...
    @licenseServer.setter
    def licenseServer(self, value: str):
        self._licenseServer = value


class LicenseSourceUnavailable(NotEnoughLicenses):
    @property
    def licenseSource(self) -> vim.LicenseManager.LicenseSource: ...
    @licenseSource.setter
    def licenseSource(self, value: vim.LicenseManager.LicenseSource):
        self._licenseSource = value


class LimitExceeded(VimFault):
    @property
    def property(self) -> PropertyPath: ...
    @property.setter
    def property(self, value: PropertyPath):
        self._property = value
    @property
    def limit(self) -> int: ...
    @limit.setter
    def limit(self, value: int):
        self._limit = value


class LinuxVolumeNotClean(CustomizationFault): ...


class LogBundlingFailed(VimFault): ...


class MaintenanceModeFileMove(MigrationFault): ...


class MemoryFileFormatNotSupportedByDatastore(UnsupportedDatastore):
    @property
    def datastoreName(self) -> str: ...
    @datastoreName.setter
    def datastoreName(self, value: str):
        self._datastoreName = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value


class MemoryHotPlugNotSupported(VmConfigFault): ...


class MemorySizeNotRecommended(VirtualHardwareCompatibilityIssue):
    @property
    def memorySizeMB(self) -> int: ...
    @memorySizeMB.setter
    def memorySizeMB(self, value: int):
        self._memorySizeMB = value
    @property
    def minMemorySizeMB(self) -> int: ...
    @minMemorySizeMB.setter
    def minMemorySizeMB(self, value: int):
        self._minMemorySizeMB = value
    @property
    def maxMemorySizeMB(self) -> int: ...
    @maxMemorySizeMB.setter
    def maxMemorySizeMB(self, value: int):
        self._maxMemorySizeMB = value


class MemorySizeNotSupported(VirtualHardwareCompatibilityIssue):
    @property
    def memorySizeMB(self) -> int: ...
    @memorySizeMB.setter
    def memorySizeMB(self, value: int):
        self._memorySizeMB = value
    @property
    def minMemorySizeMB(self) -> int: ...
    @minMemorySizeMB.setter
    def minMemorySizeMB(self, value: int):
        self._minMemorySizeMB = value
    @property
    def maxMemorySizeMB(self) -> int: ...
    @maxMemorySizeMB.setter
    def maxMemorySizeMB(self, value: int):
        self._maxMemorySizeMB = value


class MemorySizeNotSupportedByDatastore(VirtualHardwareCompatibilityIssue):
    @property
    def datastore(self) -> vim.Datastore: ...
    @datastore.setter
    def datastore(self, value: vim.Datastore):
        self._datastore = value
    @property
    def memorySizeMB(self) -> int: ...
    @memorySizeMB.setter
    def memorySizeMB(self, value: int):
        self._memorySizeMB = value
    @property
    def maxMemorySizeMB(self) -> int: ...
    @maxMemorySizeMB.setter
    def maxMemorySizeMB(self, value: int):
        self._maxMemorySizeMB = value


class MemorySnapshotOnIndependentDisk(SnapshotFault): ...


class MethodAlreadyDisabledFault(vmodl.RuntimeFault):
    @property
    def sourceId(self) -> str: ...
    @sourceId.setter
    def sourceId(self, value: str):
        self._sourceId = value


class MethodDisabled(vmodl.RuntimeFault):
    @property
    def source(self) -> str: ...
    @source.setter
    def source(self, value: str):
        self._source = value


class MigrationDisabled(MigrationFault): ...


class MigrationFault(VimFault): ...


class MigrationFeatureNotSupported(MigrationFault):
    @property
    def atSourceHost(self) -> bool: ...
    @atSourceHost.setter
    def atSourceHost(self, value: bool):
        self._atSourceHost = value
    @property
    def failedHostName(self) -> str: ...
    @failedHostName.setter
    def failedHostName(self, value: str):
        self._failedHostName = value
    @property
    def failedHost(self) -> vim.HostSystem: ...
    @failedHost.setter
    def failedHost(self, value: vim.HostSystem):
        self._failedHost = value


class MigrationNotReady(MigrationFault):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class MismatchedBundle(VimFault):
    @property
    def bundleUuid(self) -> str: ...
    @bundleUuid.setter
    def bundleUuid(self, value: str):
        self._bundleUuid = value
    @property
    def hostUuid(self) -> str: ...
    @hostUuid.setter
    def hostUuid(self, value: str):
        self._hostUuid = value
    @property
    def bundleBuildNumber(self) -> int: ...
    @bundleBuildNumber.setter
    def bundleBuildNumber(self, value: int):
        self._bundleBuildNumber = value
    @property
    def hostBuildNumber(self) -> int: ...
    @hostBuildNumber.setter
    def hostBuildNumber(self, value: int):
        self._hostBuildNumber = value


class MismatchedNetworkPolicies(MigrationFault):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value
    @property
    def backing(self) -> str: ...
    @backing.setter
    def backing(self, value: str):
        self._backing = value
    @property
    def connected(self) -> bool: ...
    @connected.setter
    def connected(self, value: bool):
        self._connected = value


class MismatchedVMotionNetworkNames(MigrationFault):
    @property
    def sourceNetwork(self) -> str: ...
    @sourceNetwork.setter
    def sourceNetwork(self, value: str):
        self._sourceNetwork = value
    @property
    def destNetwork(self) -> str: ...
    @destNetwork.setter
    def destNetwork(self, value: str):
        self._destNetwork = value


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
    @connectionLimit.setter
    def connectionLimit(self, value: int):
        self._connectionLimit = value


class MountError(CustomizationFault):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def diskIndex(self) -> int: ...
    @diskIndex.setter
    def diskIndex(self, value: int):
        self._diskIndex = value


class MultiWriterNotSupported(DeviceNotSupported): ...


class MultipleCertificatesVerifyFault(HostConnectFault):
    @property
    def thumbprintData(self) -> List[MultipleCertificatesVerifyFault.ThumbprintData]: ...
    @thumbprintData.setter
    def thumbprintData(self, value: List[MultipleCertificatesVerifyFault.ThumbprintData]):
        self._thumbprintData = value


    class ThumbprintData(vmodl.DynamicData):
        @property
        def port(self) -> int: ...
        @port.setter
        def port(self, value: int):
            self._port = value
        @property
        def thumbprint(self) -> str: ...
        @thumbprint.setter
        def thumbprint(self, value: str):
            self._thumbprint = value


class MultipleSnapshotsNotSupported(SnapshotFault): ...


class NamespaceFull(VimFault):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def currentMaxSize(self) -> long: ...
    @currentMaxSize.setter
    def currentMaxSize(self, value: long):
        self._currentMaxSize = value
    @property
    def requiredSize(self) -> long: ...
    @requiredSize.setter
    def requiredSize(self, value: long):
        self._requiredSize = value


class NamespaceLimitReached(VimFault):
    @property
    def limit(self) -> int: ...
    @limit.setter
    def limit(self, value: int):
        self._limit = value


class NamespaceWriteProtected(VimFault):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class NasConfigFault(HostConfigFault):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class NasConnectionLimitReached(NasConfigFault):
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


class NasSessionCredentialConflict(NasConfigFault):
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


class NasVolumeNotMounted(NasConfigFault):
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


class NetworkCopyFault(FileFault): ...


class NetworkDisruptedAndConfigRolledBack(VimFault):
    @property
    def host(self) -> str: ...
    @host.setter
    def host(self, value: str):
        self._host = value


class NetworkInaccessible(NasConfigFault): ...


class NetworksMayNotBeTheSame(MigrationFault):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class NicSettingMismatch(CustomizationFault):
    @property
    def numberOfNicsInSpec(self) -> int: ...
    @numberOfNicsInSpec.setter
    def numberOfNicsInSpec(self, value: int):
        self._numberOfNicsInSpec = value
    @property
    def numberOfNicsInVM(self) -> int: ...
    @numberOfNicsInVM.setter
    def numberOfNicsInVM(self, value: int):
        self._numberOfNicsInVM = value


class NoActiveHostInCluster(InvalidState):
    @property
    def computeResource(self) -> vim.ComputeResource: ...
    @computeResource.setter
    def computeResource(self, value: vim.ComputeResource):
        self._computeResource = value


class NoAvailableIp(VAppPropertyFault):
    @property
    def network(self) -> vim.Network: ...
    @network.setter
    def network(self, value: vim.Network):
        self._network = value


class NoClientCertificate(VimFault): ...


class NoCompatibleDatastore(VimFault): ...


class NoCompatibleHardAffinityHost(VmConfigFault):
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class NoCompatibleHost(VimFault):
    @property
    def host(self) -> List[vim.HostSystem]: ...
    @host.setter
    def host(self, value: List[vim.HostSystem]):
        self._host = value
    @property
    def error(self) -> List[vmodl.MethodFault]: ...
    @error.setter
    def error(self, value: List[vmodl.MethodFault]):
        self._error = value


class NoCompatibleHostWithAccessToDevice(NoCompatibleHost): ...


class NoCompatibleSoftAffinityHost(VmConfigFault):
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class NoConnectedDatastore(VimFault): ...


class NoDiskFound(VimFault): ...


class NoDiskSpace(FileFault):
    @property
    def datastore(self) -> str: ...
    @datastore.setter
    def datastore(self, value: str):
        self._datastore = value


class NoDisksToCustomize(CustomizationFault): ...


class NoGateway(HostConfigFault): ...


class NoGuestHeartbeat(MigrationFault): ...


class NoHost(HostConnectFault):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class NoHostSuitableForFtSecondary(VmFaultToleranceIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class NoLicenseServerConfigured(NotEnoughLicenses): ...


class NoPeerHostFound(HostPowerOpFailed): ...


class NoPermission(SecurityError):
    @property
    def object(self) -> ManagedObject: ...
    @object.setter
    def object(self, value: ManagedObject):
        self._object = value
    @property
    def privilegeId(self) -> str: ...
    @privilegeId.setter
    def privilegeId(self, value: str):
        self._privilegeId = value
    @property
    def missingPrivileges(self) -> List[NoPermission.EntityPrivileges]: ...
    @missingPrivileges.setter
    def missingPrivileges(self, value: List[NoPermission.EntityPrivileges]):
        self._missingPrivileges = value


    class EntityPrivileges(vmodl.DynamicData):
        @property
        def entity(self) -> ManagedObject: ...
        @entity.setter
        def entity(self, value: ManagedObject):
            self._entity = value
        @property
        def privilegeIds(self) -> List[str]: ...
        @privilegeIds.setter
        def privilegeIds(self, value: List[str]):
            self._privilegeIds = value


class NoPermissionOnAD(ActiveDirectoryFault): ...


class NoPermissionOnHost(HostConnectFault): ...


class NoPermissionOnNasVolume(NasConfigFault):
    @property
    def userName(self) -> str: ...
    @userName.setter
    def userName(self, value: str):
        self._userName = value


class NoSubjectName(VimFault): ...


class NoVcManagedIpConfigured(VAppPropertyFault): ...


class NoVirtualNic(HostConfigFault): ...


class NoVmInVApp(VAppConfigFault): ...


class NonADUserRequired(ActiveDirectoryFault): ...


class NonHomeRDMVMotionNotSupported(MigrationFeatureNotSupported):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value


class NonPersistentDisksNotSupported(DeviceNotSupported): ...


class NonVmwareOuiMacNotSupportedHost(NotSupportedHost):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value


class NotADirectory(FileFault): ...


class NotAFile(FileFault): ...


class NotAuthenticated(NoPermission): ...


class NotEnoughCpus(VirtualHardwareCompatibilityIssue):
    @property
    def numCpuDest(self) -> int: ...
    @numCpuDest.setter
    def numCpuDest(self, value: int):
        self._numCpuDest = value
    @property
    def numCpuVm(self) -> int: ...
    @numCpuVm.setter
    def numCpuVm(self, value: int):
        self._numCpuVm = value


class NotEnoughLogicalCpus(NotEnoughCpus):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value


class NotFound(VimFault): ...


class NotSupportedDeviceForFT(VmFaultToleranceIssue):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value
    @property
    def deviceType(self) -> str: ...
    @deviceType.setter
    def deviceType(self, value: str):
        self._deviceType = value
    @property
    def deviceLabel(self) -> str: ...
    @deviceLabel.setter
    def deviceLabel(self, value: str):
        self._deviceLabel = value


    class DeviceType(Enum):
        virtualVmxnet3 = "virtualVmxnet3"
        paraVirtualSCSIController = "paraVirtualSCSIController"


class NotSupportedHost(HostConnectFault):
    @property
    def productName(self) -> str: ...
    @productName.setter
    def productName(self, value: str):
        self._productName = value
    @property
    def productVersion(self) -> str: ...
    @productVersion.setter
    def productVersion(self, value: str):
        self._productVersion = value


class NotSupportedHostForChecksum(VimFault): ...


class NotSupportedHostForVFlash(NotSupportedHost):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value


class NotSupportedHostForVmcp(NotSupportedHost):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value


class NotSupportedHostForVmemFile(NotSupportedHost):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value


class NotSupportedHostForVsan(NotSupportedHost):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value


class NotSupportedHostInCluster(NotSupportedHost): ...


class NotSupportedHostInDvs(NotSupportedHost):
    @property
    def switchProductSpec(self) -> vim.dvs.ProductSpec: ...
    @switchProductSpec.setter
    def switchProductSpec(self, value: vim.dvs.ProductSpec):
        self._switchProductSpec = value


class NotSupportedHostInHACluster(NotSupportedHost):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def build(self) -> str: ...
    @build.setter
    def build(self, value: str):
        self._build = value


class NotUserConfigurableProperty(VAppPropertyFault): ...


class NumVirtualCoresPerSocketNotSupported(VirtualHardwareCompatibilityIssue):
    @property
    def maxSupportedCoresPerSocketDest(self) -> int: ...
    @maxSupportedCoresPerSocketDest.setter
    def maxSupportedCoresPerSocketDest(self, value: int):
        self._maxSupportedCoresPerSocketDest = value
    @property
    def numCoresPerSocketVm(self) -> int: ...
    @numCoresPerSocketVm.setter
    def numCoresPerSocketVm(self, value: int):
        self._numCoresPerSocketVm = value


class NumVirtualCpusExceedsLimit(InsufficientResourcesFault):
    @property
    def maxSupportedVcpus(self) -> int: ...
    @maxSupportedVcpus.setter
    def maxSupportedVcpus(self, value: int):
        self._maxSupportedVcpus = value


class NumVirtualCpusIncompatible(VmConfigFault):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def numCpu(self) -> int: ...
    @numCpu.setter
    def numCpu(self, value: int):
        self._numCpu = value


class NumVirtualCpusNotSupported(VirtualHardwareCompatibilityIssue):
    @property
    def maxSupportedVcpusDest(self) -> int: ...
    @maxSupportedVcpusDest.setter
    def maxSupportedVcpusDest(self, value: int):
        self._maxSupportedVcpusDest = value
    @property
    def numCpuVm(self) -> int: ...
    @numCpuVm.setter
    def numCpuVm(self, value: int):
        self._numCpuVm = value


class OperationDisabledByGuest(GuestOperationsFault): ...


class OperationDisallowedOnHost(vmodl.RuntimeFault): ...


class OperationNotSupportedByGuest(GuestOperationsFault): ...


class OutOfBounds(VimFault):
    @property
    def argumentName(self) -> PropertyPath: ...
    @argumentName.setter
    def argumentName(self, value: PropertyPath):
        self._argumentName = value


class OvfAttribute(OvfInvalidPackage):
    @property
    def elementName(self) -> str: ...
    @elementName.setter
    def elementName(self, value: str):
        self._elementName = value
    @property
    def attributeName(self) -> str: ...
    @attributeName.setter
    def attributeName(self, value: str):
        self._attributeName = value


class OvfConnectedDevice(OvfHardwareExport): ...


class OvfConnectedDeviceFloppy(OvfConnectedDevice):
    @property
    def filename(self) -> str: ...
    @filename.setter
    def filename(self, value: str):
        self._filename = value


class OvfConnectedDeviceIso(OvfConnectedDevice):
    @property
    def filename(self) -> str: ...
    @filename.setter
    def filename(self, value: str):
        self._filename = value


class OvfConstraint(OvfInvalidPackage):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class OvfConsumerCallbackFault(OvfFault):
    @property
    def extensionKey(self) -> str: ...
    @extensionKey.setter
    def extensionKey(self, value: str):
        self._extensionKey = value
    @property
    def extensionName(self) -> str: ...
    @extensionName.setter
    def extensionName(self, value: str):
        self._extensionName = value


class OvfConsumerCommunicationError(OvfConsumerCallbackFault):
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value


class OvfConsumerFault(OvfConsumerCallbackFault):
    @property
    def errorKey(self) -> str: ...
    @errorKey.setter
    def errorKey(self, value: str):
        self._errorKey = value
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str):
        self._message = value
    @property
    def params(self) -> List[vim.KeyValue]: ...
    @params.setter
    def params(self, value: List[vim.KeyValue]):
        self._params = value


class OvfConsumerInvalidSection(OvfConsumerCallbackFault):
    @property
    def lineNumber(self) -> int: ...
    @lineNumber.setter
    def lineNumber(self, value: int):
        self._lineNumber = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value


class OvfConsumerPowerOnFault(InvalidState):
    @property
    def extensionKey(self) -> str: ...
    @extensionKey.setter
    def extensionKey(self, value: str):
        self._extensionKey = value
    @property
    def extensionName(self) -> str: ...
    @extensionName.setter
    def extensionName(self, value: str):
        self._extensionName = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value


class OvfConsumerUndeclaredSection(OvfConsumerCallbackFault):
    @property
    def qualifiedSectionType(self) -> str: ...
    @qualifiedSectionType.setter
    def qualifiedSectionType(self, value: str):
        self._qualifiedSectionType = value


class OvfConsumerUndefinedPrefix(OvfConsumerCallbackFault):
    @property
    def prefix(self) -> str: ...
    @prefix.setter
    def prefix(self, value: str):
        self._prefix = value


class OvfConsumerValidationFault(VmConfigFault):
    @property
    def extensionKey(self) -> str: ...
    @extensionKey.setter
    def extensionKey(self, value: str):
        self._extensionKey = value
    @property
    def extensionName(self) -> str: ...
    @extensionName.setter
    def extensionName(self, value: str):
        self._extensionName = value
    @property
    def message(self) -> str: ...
    @message.setter
    def message(self, value: str):
        self._message = value


class OvfCpuCompatibility(OvfImport):
    @property
    def registerName(self) -> str: ...
    @registerName.setter
    def registerName(self, value: str):
        self._registerName = value
    @property
    def level(self) -> int: ...
    @level.setter
    def level(self, value: int):
        self._level = value
    @property
    def registerValue(self) -> str: ...
    @registerValue.setter
    def registerValue(self, value: str):
        self._registerValue = value
    @property
    def desiredRegisterValue(self) -> str: ...
    @desiredRegisterValue.setter
    def desiredRegisterValue(self, value: str):
        self._desiredRegisterValue = value


class OvfCpuCompatibilityCheckNotSupported(OvfImport): ...


class OvfDiskMappingNotFound(OvfSystemFault):
    @property
    def diskName(self) -> str: ...
    @diskName.setter
    def diskName(self, value: str):
        self._diskName = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class OvfDiskOrderConstraint(OvfConstraint): ...


class OvfDuplicateElement(OvfElement): ...


class OvfDuplicatedElementBoundary(OvfElement):
    @property
    def boundary(self) -> str: ...
    @boundary.setter
    def boundary(self, value: str):
        self._boundary = value


class OvfDuplicatedPropertyIdExport(OvfExport):
    @property
    def fqid(self) -> str: ...
    @fqid.setter
    def fqid(self, value: str):
        self._fqid = value


class OvfDuplicatedPropertyIdImport(OvfExport): ...


class OvfElement(OvfInvalidPackage):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class OvfElementInvalidValue(OvfElement):
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class OvfExport(OvfFault): ...


class OvfExportFailed(OvfExport): ...


class OvfFault(VimFault): ...


class OvfHardwareCheck(OvfImport): ...


class OvfHardwareExport(OvfExport):
    @property
    def device(self) -> vim.vm.device.VirtualDevice: ...
    @device.setter
    def device(self, value: vim.vm.device.VirtualDevice):
        self._device = value
    @property
    def vmPath(self) -> str: ...
    @vmPath.setter
    def vmPath(self, value: str):
        self._vmPath = value


class OvfHostResourceConstraint(OvfConstraint):
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class OvfHostValueNotParsed(OvfSystemFault):
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


class OvfImport(OvfFault): ...


class OvfImportFailed(OvfImport): ...


class OvfInternalError(OvfSystemFault): ...


class OvfInvalidPackage(OvfFault):
    @property
    def lineNumber(self) -> int: ...
    @lineNumber.setter
    def lineNumber(self, value: int):
        self._lineNumber = value


class OvfInvalidValue(OvfAttribute):
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class OvfInvalidValueConfiguration(OvfInvalidValue): ...


class OvfInvalidValueEmpty(OvfInvalidValue): ...


class OvfInvalidValueFormatMalformed(OvfInvalidValue): ...


class OvfInvalidValueReference(OvfInvalidValue): ...


class OvfInvalidVmName(OvfUnsupportedPackage):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class OvfMappedOsId(OvfImport):
    @property
    def ovfId(self) -> int: ...
    @ovfId.setter
    def ovfId(self, value: int):
        self._ovfId = value
    @property
    def ovfDescription(self) -> str: ...
    @ovfDescription.setter
    def ovfDescription(self, value: str):
        self._ovfDescription = value
    @property
    def targetDescription(self) -> str: ...
    @targetDescription.setter
    def targetDescription(self, value: str):
        self._targetDescription = value


class OvfMissingAttribute(OvfAttribute): ...


class OvfMissingElement(OvfElement): ...


class OvfMissingElementNormalBoundary(OvfMissingElement):
    @property
    def boundary(self) -> str: ...
    @boundary.setter
    def boundary(self, value: str):
        self._boundary = value


class OvfMissingHardware(OvfImport):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def resourceType(self) -> int: ...
    @resourceType.setter
    def resourceType(self, value: int):
        self._resourceType = value


class OvfNetworkMappingNotSupported(OvfImport): ...


class OvfNoHostNic(OvfUnsupportedPackage): ...


class OvfNoSpaceOnController(OvfUnsupportedElement):
    @property
    def parent(self) -> str: ...
    @parent.setter
    def parent(self, value: str):
        self._parent = value


class OvfNoSupportedHardwareFamily(OvfUnsupportedPackage):
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value


class OvfProperty(OvfInvalidPackage):
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class OvfPropertyExport(OvfExport):
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class OvfPropertyNetwork(OvfProperty): ...


class OvfPropertyNetworkExport(OvfExport):
    @property
    def network(self) -> str: ...
    @network.setter
    def network(self, value: str):
        self._network = value


class OvfPropertyQualifier(OvfProperty):
    @property
    def qualifier(self) -> str: ...
    @qualifier.setter
    def qualifier(self, value: str):
        self._qualifier = value


class OvfPropertyQualifierDuplicate(OvfProperty):
    @property
    def qualifier(self) -> str: ...
    @qualifier.setter
    def qualifier(self, value: str):
        self._qualifier = value


class OvfPropertyQualifierIgnored(OvfProperty):
    @property
    def qualifier(self) -> str: ...
    @qualifier.setter
    def qualifier(self, value: str):
        self._qualifier = value


class OvfPropertyType(OvfProperty): ...


class OvfPropertyValue(OvfProperty): ...


class OvfSystemFault(OvfFault): ...


class OvfToXmlUnsupportedElement(OvfSystemFault):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class OvfUnableToExportDisk(OvfHardwareExport):
    @property
    def diskName(self) -> str: ...
    @diskName.setter
    def diskName(self, value: str):
        self._diskName = value


class OvfUnexpectedElement(OvfElement): ...


class OvfUnknownDevice(OvfSystemFault):
    @property
    def device(self) -> vim.vm.device.VirtualDevice: ...
    @device.setter
    def device(self, value: vim.vm.device.VirtualDevice):
        self._device = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class OvfUnknownDeviceBacking(OvfHardwareExport):
    @property
    def backing(self) -> vim.vm.device.VirtualDevice.BackingInfo: ...
    @backing.setter
    def backing(self, value: vim.vm.device.VirtualDevice.BackingInfo):
        self._backing = value


class OvfUnknownEntity(OvfSystemFault):
    @property
    def lineNumber(self) -> int: ...
    @lineNumber.setter
    def lineNumber(self, value: int):
        self._lineNumber = value


class OvfUnsupportedAttribute(OvfUnsupportedPackage):
    @property
    def elementName(self) -> str: ...
    @elementName.setter
    def elementName(self, value: str):
        self._elementName = value
    @property
    def attributeName(self) -> str: ...
    @attributeName.setter
    def attributeName(self, value: str):
        self._attributeName = value


class OvfUnsupportedAttributeValue(OvfUnsupportedAttribute):
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class OvfUnsupportedDeviceBackingInfo(OvfSystemFault):
    @property
    def elementName(self) -> str: ...
    @elementName.setter
    def elementName(self, value: str):
        self._elementName = value
    @property
    def instanceId(self) -> str: ...
    @instanceId.setter
    def instanceId(self, value: str):
        self._instanceId = value
    @property
    def deviceName(self) -> str: ...
    @deviceName.setter
    def deviceName(self, value: str):
        self._deviceName = value
    @property
    def backingName(self) -> str: ...
    @backingName.setter
    def backingName(self, value: str):
        self._backingName = value


class OvfUnsupportedDeviceBackingOption(OvfSystemFault):
    @property
    def elementName(self) -> str: ...
    @elementName.setter
    def elementName(self, value: str):
        self._elementName = value
    @property
    def instanceId(self) -> str: ...
    @instanceId.setter
    def instanceId(self, value: str):
        self._instanceId = value
    @property
    def deviceName(self) -> str: ...
    @deviceName.setter
    def deviceName(self, value: str):
        self._deviceName = value
    @property
    def backingName(self) -> str: ...
    @backingName.setter
    def backingName(self, value: str):
        self._backingName = value


class OvfUnsupportedDeviceExport(OvfHardwareExport): ...


class OvfUnsupportedDiskProvisioning(OvfImport):
    @property
    def diskProvisioning(self) -> str: ...
    @diskProvisioning.setter
    def diskProvisioning(self, value: str):
        self._diskProvisioning = value
    @property
    def supportedDiskProvisioning(self) -> str: ...
    @supportedDiskProvisioning.setter
    def supportedDiskProvisioning(self, value: str):
        self._supportedDiskProvisioning = value


class OvfUnsupportedElement(OvfUnsupportedPackage):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class OvfUnsupportedElementValue(OvfUnsupportedElement):
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class OvfUnsupportedPackage(OvfFault):
    @property
    def lineNumber(self) -> int: ...
    @lineNumber.setter
    def lineNumber(self, value: int):
        self._lineNumber = value


class OvfUnsupportedSection(OvfUnsupportedElement):
    @property
    def info(self) -> str: ...
    @info.setter
    def info(self, value: str):
        self._info = value


class OvfUnsupportedSubType(OvfUnsupportedPackage):
    @property
    def elementName(self) -> str: ...
    @elementName.setter
    def elementName(self, value: str):
        self._elementName = value
    @property
    def instanceId(self) -> str: ...
    @instanceId.setter
    def instanceId(self, value: str):
        self._instanceId = value
    @property
    def deviceType(self) -> int: ...
    @deviceType.setter
    def deviceType(self, value: int):
        self._deviceType = value
    @property
    def deviceSubType(self) -> str: ...
    @deviceSubType.setter
    def deviceSubType(self, value: str):
        self._deviceSubType = value


class OvfUnsupportedType(OvfUnsupportedPackage):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def instanceId(self) -> str: ...
    @instanceId.setter
    def instanceId(self, value: str):
        self._instanceId = value
    @property
    def deviceType(self) -> int: ...
    @deviceType.setter
    def deviceType(self, value: int):
        self._deviceType = value


class OvfWrongElement(OvfElement): ...


class OvfWrongNamespace(OvfInvalidPackage):
    @property
    def namespaceName(self) -> str: ...
    @namespaceName.setter
    def namespaceName(self, value: str):
        self._namespaceName = value


class OvfXmlFormat(OvfInvalidPackage):
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value


class PasswordExpired(InvalidLogin): ...


class PatchAlreadyInstalled(PatchNotApplicable): ...


class PatchBinariesNotFound(VimFault):
    @property
    def patchID(self) -> str: ...
    @patchID.setter
    def patchID(self, value: str):
        self._patchID = value
    @property
    def binary(self) -> List[str]: ...
    @binary.setter
    def binary(self, value: List[str]):
        self._binary = value


class PatchInstallFailed(PlatformConfigFault):
    @property
    def rolledBack(self) -> bool: ...
    @rolledBack.setter
    def rolledBack(self, value: bool):
        self._rolledBack = value


class PatchIntegrityError(PlatformConfigFault): ...


class PatchMetadataCorrupted(PatchMetadataInvalid): ...


class PatchMetadataInvalid(VimFault):
    @property
    def patchID(self) -> str: ...
    @patchID.setter
    def patchID(self, value: str):
        self._patchID = value
    @property
    def metaData(self) -> List[str]: ...
    @metaData.setter
    def metaData(self, value: List[str]):
        self._metaData = value


class PatchMetadataNotFound(PatchMetadataInvalid): ...


class PatchMissingDependencies(PatchNotApplicable):
    @property
    def prerequisitePatch(self) -> List[str]: ...
    @prerequisitePatch.setter
    def prerequisitePatch(self, value: List[str]):
        self._prerequisitePatch = value
    @property
    def prerequisiteLib(self) -> List[str]: ...
    @prerequisiteLib.setter
    def prerequisiteLib(self, value: List[str]):
        self._prerequisiteLib = value


class PatchNotApplicable(VimFault):
    @property
    def patchID(self) -> str: ...
    @patchID.setter
    def patchID(self, value: str):
        self._patchID = value


class PatchSuperseded(PatchNotApplicable):
    @property
    def supersede(self) -> List[str]: ...
    @supersede.setter
    def supersede(self, value: List[str]):
        self._supersede = value


class PhysCompatRDMNotSupported(RDMNotSupported): ...


class PlatformConfigFault(HostConfigFault):
    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str):
        self._text = value


class PowerOnFtSecondaryFailed(VmFaultToleranceIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value
    @property
    def hostSelectionBy(self) -> FtIssuesOnHost.HostSelectionType | Literal['user', 'vc', 'drs']: ...
    @hostSelectionBy.setter
    def hostSelectionBy(self, value: FtIssuesOnHost.HostSelectionType | Literal['user', 'vc', 'drs']):
        self._hostSelectionBy = value
    @property
    def hostErrors(self) -> List[vmodl.MethodFault]: ...
    @hostErrors.setter
    def hostErrors(self, value: List[vmodl.MethodFault]):
        self._hostErrors = value
    @property
    def rootCause(self) -> vmodl.MethodFault: ...
    @rootCause.setter
    def rootCause(self, value: vmodl.MethodFault):
        self._rootCause = value


class PowerOnFtSecondaryTimedout(Timedout):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value
    @property
    def timeout(self) -> int: ...
    @timeout.setter
    def timeout(self, value: int):
        self._timeout = value


class ProfileUpdateFailed(VimFault):
    @property
    def failure(self) -> List[ProfileUpdateFailed.UpdateFailure]: ...
    @failure.setter
    def failure(self, value: List[ProfileUpdateFailed.UpdateFailure]):
        self._failure = value
    @property
    def warnings(self) -> List[ProfileUpdateFailed.UpdateFailure]: ...
    @warnings.setter
    def warnings(self, value: List[ProfileUpdateFailed.UpdateFailure]):
        self._warnings = value


    class UpdateFailure(vmodl.DynamicData):
        @property
        def profilePath(self) -> vim.profile.ProfilePropertyPath: ...
        @profilePath.setter
        def profilePath(self, value: vim.profile.ProfilePropertyPath):
            self._profilePath = value
        @property
        def errMsg(self) -> vmodl.LocalizableMessage: ...
        @errMsg.setter
        def errMsg(self, value: vmodl.LocalizableMessage):
            self._errMsg = value


class QuarantineModeFault(VmConfigFault):
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value
    @property
    def faultType(self) -> str: ...
    @faultType.setter
    def faultType(self, value: str):
        self._faultType = value


    class FaultType(Enum):
        NoCompatibleNonQuarantinedHost = "NoCompatibleNonQuarantinedHost"
        CorrectionDisallowed = "CorrectionDisallowed"
        CorrectionImpact = "CorrectionImpact"


class QuestionPending(InvalidState):
    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str):
        self._text = value


class QuiesceDatastoreIOForHAFailed(ResourceInUse):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def ds(self) -> vim.Datastore: ...
    @ds.setter
    def ds(self, value: vim.Datastore):
        self._ds = value
    @property
    def dsName(self) -> str: ...
    @dsName.setter
    def dsName(self, value: str):
        self._dsName = value


class RDMConversionNotSupported(MigrationFault):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value


class RDMNotPreserved(MigrationFault):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value


class RDMNotSupported(DeviceNotSupported): ...


class RDMNotSupportedOnDatastore(VmConfigFault):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value
    @property
    def datastore(self) -> vim.Datastore: ...
    @datastore.setter
    def datastore(self, value: vim.Datastore):
        self._datastore = value
    @property
    def datastoreName(self) -> str: ...
    @datastoreName.setter
    def datastoreName(self, value: str):
        self._datastoreName = value


class RDMPointsToInaccessibleDisk(CannotAccessVmDisk): ...


class RawDiskNotSupported(DeviceNotSupported): ...


class ReadHostResourcePoolTreeFailed(HostConnectFault): ...


class ReadOnlyDisksWithLegacyDestination(MigrationFault):
    @property
    def roDiskCount(self) -> int: ...
    @roDiskCount.setter
    def roDiskCount(self, value: int):
        self._roDiskCount = value
    @property
    def timeoutDanger(self) -> bool: ...
    @timeoutDanger.setter
    def timeoutDanger(self, value: bool):
        self._timeoutDanger = value


class RebootRequired(VimFault):
    @property
    def patch(self) -> str: ...
    @patch.setter
    def patch(self, value: str):
        self._patch = value


class RecordReplayDisabled(VimFault): ...


class RemoteDeviceNotSupported(DeviceNotSupported): ...


class RemoveFailed(VimFault): ...


class ReplicationConfigFault(ReplicationFault): ...


class ReplicationDiskConfigFault(ReplicationConfigFault):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def vmRef(self) -> vim.VirtualMachine: ...
    @vmRef.setter
    def vmRef(self, value: vim.VirtualMachine):
        self._vmRef = value
    @property
    def key(self) -> int: ...
    @key.setter
    def key(self, value: int):
        self._key = value


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
    @options.setter
    def options(self, value: str):
        self._options = value
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @entity.setter
    def entity(self, value: vim.ManagedEntity):
        self._entity = value


class ReplicationNotSupportedOnHost(ReplicationFault): ...


class ReplicationVmConfigFault(ReplicationConfigFault):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def vmRef(self) -> vim.VirtualMachine: ...
    @vmRef.setter
    def vmRef(self, value: vim.VirtualMachine):
        self._vmRef = value


class ReplicationVmFault(ReplicationFault):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def state(self) -> str: ...
    @state.setter
    def state(self, value: str):
        self._state = value
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


class ReplicationVmInProgressFault(ReplicationVmFault):
    @property
    def requestedActivity(self) -> str: ...
    @requestedActivity.setter
    def requestedActivity(self, value: str):
        self._requestedActivity = value
    @property
    def inProgressActivity(self) -> str: ...
    @inProgressActivity.setter
    def inProgressActivity(self, value: str):
        self._inProgressActivity = value


    class Activity(Enum):
        fullSync = "fullSync"
        delta = "delta"


class ResourceInUse(VimFault):
    @property
    def type(self) -> type: ...
    @type.setter
    def type(self, value: type):
        self._type = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value


class ResourceNotAvailable(VimFault):
    @property
    def containerType(self) -> type: ...
    @containerType.setter
    def containerType(self, value: type):
        self._containerType = value
    @property
    def containerName(self) -> str: ...
    @containerName.setter
    def containerName(self, value: str):
        self._containerName = value
    @property
    def type(self) -> type: ...
    @type.setter
    def type(self, value: type):
        self._type = value


class RestrictedByAdministrator(vmodl.RuntimeFault):
    @property
    def details(self) -> str: ...
    @details.setter
    def details(self, value: str):
        self._details = value


class RestrictedVersion(SecurityError): ...


class RollbackFailure(DvsFault):
    @property
    def entityName(self) -> str: ...
    @entityName.setter
    def entityName(self, value: str):
        self._entityName = value
    @property
    def entityType(self) -> str: ...
    @entityType.setter
    def entityType(self, value: str):
        self._entityType = value


class RuleViolation(VmConfigFault):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def rule(self) -> vim.cluster.RuleInfo: ...
    @rule.setter
    def rule(self, value: vim.cluster.RuleInfo):
        self._rule = value


class SSLDisabledFault(HostConnectFault): ...


class SSLVerifyFault(HostConnectFault):
    @property
    def selfSigned(self) -> bool: ...
    @selfSigned.setter
    def selfSigned(self, value: bool):
        self._selfSigned = value
    @property
    def thumbprint(self) -> str: ...
    @thumbprint.setter
    def thumbprint(self, value: str):
        self._thumbprint = value


class SSPIChallenge(VimFault):
    @property
    def base64Token(self) -> str: ...
    @base64Token.setter
    def base64Token(self, value: str):
        self._base64Token = value


class SecondaryVmAlreadyDisabled(VmFaultToleranceIssue):
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value


class SecondaryVmAlreadyEnabled(VmFaultToleranceIssue):
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value


class SecondaryVmAlreadyRegistered(VmFaultToleranceIssue):
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value


class SecondaryVmNotRegistered(VmFaultToleranceIssue):
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value


class SharedBusControllerNotSupported(DeviceNotSupported): ...


class ShrinkDiskFault(VimFault):
    @property
    def diskId(self) -> int: ...
    @diskId.setter
    def diskId(self, value: int):
        self._diskId = value


class SnapshotCloneNotSupported(SnapshotCopyNotSupported): ...


class SnapshotCopyNotSupported(MigrationFault): ...


class SnapshotDisabled(SnapshotFault): ...


class SnapshotFault(VimFault): ...


class SnapshotIncompatibleDeviceInVm(SnapshotFault):
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class SnapshotLocked(SnapshotFault): ...


class SnapshotMoveFromNonHomeNotSupported(SnapshotCopyNotSupported): ...


class SnapshotMoveNotSupported(SnapshotCopyNotSupported): ...


class SnapshotMoveToNonHomeNotSupported(SnapshotCopyNotSupported): ...


class SnapshotNoChange(SnapshotFault): ...


class SnapshotRevertIssue(MigrationFault):
    @property
    def snapshotName(self) -> str: ...
    @snapshotName.setter
    def snapshotName(self, value: str):
        self._snapshotName = value
    @property
    def event(self) -> List[vim.event.Event]: ...
    @event.setter
    def event(self, value: List[vim.event.Event]):
        self._event = value
    @property
    def errors(self) -> bool: ...
    @errors.setter
    def errors(self, value: bool):
        self._errors = value


class SoftRuleVioCorrectionDisallowed(VmConfigFault):
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class SoftRuleVioCorrectionImpact(VmConfigFault):
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value


class SolutionUserRequired(SecurityError): ...


class SsdDiskNotAvailable(VimFault):
    @property
    def devicePath(self) -> str: ...
    @devicePath.setter
    def devicePath(self, value: str):
        self._devicePath = value


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
    @nonMovableDiskIds.setter
    def nonMovableDiskIds(self, value: str):
        self._nonMovableDiskIds = value


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
    @datastore.setter
    def datastore(self, value: vim.Datastore):
        self._datastore = value


class SuspendedRelocateNotSupported(MigrationFault): ...


class SwapDatastoreNotWritableOnHost(DatastoreNotWritableOnHost): ...


class SwapDatastoreUnset(VimFault): ...


class SwapPlacementOverrideNotSupported(InvalidVmConfig): ...


class SwitchIpUnset(DvsFault): ...


class SwitchNotInUpgradeMode(DvsFault): ...


class TaskInProgress(VimFault):
    @property
    def task(self) -> vim.Task: ...
    @task.setter
    def task(self, value: vim.Task):
        self._task = value


class ThirdPartyLicenseAssignmentFailed(vmodl.RuntimeFault):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def module(self) -> str: ...
    @module.setter
    def module(self, value: str):
        self._module = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value


class Timedout(VimFault): ...


class TooManyConcurrentNativeClones(FileFault): ...


class TooManyConsecutiveOverrides(VimFault): ...


class TooManyDevices(InvalidVmConfig): ...


class TooManyDisksOnLegacyHost(MigrationFault):
    @property
    def diskCount(self) -> int: ...
    @diskCount.setter
    def diskCount(self, value: int):
        self._diskCount = value
    @property
    def timeoutDanger(self) -> bool: ...
    @timeoutDanger.setter
    def timeoutDanger(self, value: bool):
        self._timeoutDanger = value


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
    @datastoreName.setter
    def datastoreName(self, value: str):
        self._datastoreName = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value


class UncommittedUndoableDisk(MigrationFault): ...


class UnconfiguredPropertyValue(InvalidPropertyValue): ...


class UncustomizableGuest(CustomizationFault):
    @property
    def uncustomizableGuestOS(self) -> str: ...
    @uncustomizableGuestOS.setter
    def uncustomizableGuestOS(self, value: str):
        self._uncustomizableGuestOS = value


class UnexpectedCustomizationFault(CustomizationFault): ...


class UnrecognizedHost(VimFault):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value


class UnsharedSwapVMotionNotSupported(MigrationFeatureNotSupported): ...


class UnsupportedDatastore(VmConfigFault):
    @property
    def datastore(self) -> vim.Datastore: ...
    @datastore.setter
    def datastore(self, value: vim.Datastore):
        self._datastore = value


class UnsupportedGuest(InvalidVmConfig):
    @property
    def unsupportedGuestOS(self) -> str: ...
    @unsupportedGuestOS.setter
    def unsupportedGuestOS(self, value: str):
        self._unsupportedGuestOS = value


class UnsupportedVimApiVersion(VimFault):
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value


class UnsupportedVmxLocation(VmConfigFault): ...


class UnusedVirtualDiskBlocksNotScrubbed(DeviceBackingNotSupported): ...


class UserNotFound(VimFault):
    @property
    def principal(self) -> str: ...
    @principal.setter
    def principal(self, value: str):
        self._principal = value
    @property
    def unresolved(self) -> bool: ...
    @unresolved.setter
    def unresolved(self, value: bool):
        self._unresolved = value


class VAppConfigFault(VimFault): ...


class VAppNotRunning(VmConfigFault): ...


class VAppOperationInProgress(vmodl.RuntimeFault): ...


class VAppPropertyFault(VmConfigFault):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def category(self) -> str: ...
    @category.setter
    def category(self, value: str):
        self._category = value
    @property
    def label(self) -> str: ...
    @label.setter
    def label(self, value: str):
        self._label = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class VAppTaskInProgress(TaskInProgress): ...


class VFlashCacheHotConfigNotSupported(VmConfigFault): ...


class VFlashModuleNotSupported(VmConfigFault):
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value
    @property
    def moduleName(self) -> str: ...
    @moduleName.setter
    def moduleName(self, value: str):
        self._moduleName = value
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value


class VFlashModuleVersionIncompatible(VimFault):
    @property
    def moduleName(self) -> str: ...
    @moduleName.setter
    def moduleName(self, value: str):
        self._moduleName = value
    @property
    def vmRequestModuleVersion(self) -> str: ...
    @vmRequestModuleVersion.setter
    def vmRequestModuleVersion(self, value: str):
        self._vmRequestModuleVersion = value
    @property
    def hostMinSupportedVerson(self) -> str: ...
    @hostMinSupportedVerson.setter
    def hostMinSupportedVerson(self, value: str):
        self._hostMinSupportedVerson = value
    @property
    def hostModuleVersion(self) -> str: ...
    @hostModuleVersion.setter
    def hostModuleVersion(self, value: str):
        self._hostModuleVersion = value


class VMINotSupported(DeviceNotSupported): ...


class VMOnConflictDVPort(CannotAccessNetwork): ...


class VMOnVirtualIntranet(CannotAccessNetwork): ...


class VMotionAcrossNetworkNotSupported(MigrationFeatureNotSupported): ...


class VMotionInterfaceIssue(MigrationFault):
    @property
    def atSourceHost(self) -> bool: ...
    @atSourceHost.setter
    def atSourceHost(self, value: bool):
        self._atSourceHost = value
    @property
    def failedHost(self) -> str: ...
    @failedHost.setter
    def failedHost(self, value: str):
        self._failedHost = value
    @property
    def failedHostEntity(self) -> vim.HostSystem: ...
    @failedHostEntity.setter
    def failedHostEntity(self, value: vim.HostSystem):
        self._failedHostEntity = value


class VMotionLinkCapacityLow(VMotionInterfaceIssue):
    @property
    def network(self) -> str: ...
    @network.setter
    def network(self, value: str):
        self._network = value


class VMotionLinkDown(VMotionInterfaceIssue):
    @property
    def network(self) -> str: ...
    @network.setter
    def network(self, value: str):
        self._network = value


class VMotionNotConfigured(VMotionInterfaceIssue): ...


class VMotionNotLicensed(VMotionInterfaceIssue): ...


class VMotionNotSupported(VMotionInterfaceIssue): ...


class VMotionProtocolIncompatible(MigrationFault): ...


class VimFault(vmodl.MethodFault): ...


class VirtualDiskBlocksNotFullyProvisioned(DeviceBackingNotSupported): ...


class VirtualDiskModeNotSupported(DeviceNotSupported):
    @property
    def mode(self) -> str: ...
    @mode.setter
    def mode(self, value: str):
        self._mode = value


class VirtualEthernetCardNotSupported(DeviceNotSupported): ...


class VirtualHardwareCompatibilityIssue(VmConfigFault): ...


class VirtualHardwareVersionNotSupported(VirtualHardwareCompatibilityIssue):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value


class VmAlreadyExistsInDatacenter(InvalidFolder):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def hostname(self) -> str: ...
    @hostname.setter
    def hostname(self, value: str):
        self._hostname = value
    @property
    def vm(self) -> List[vim.VirtualMachine]: ...
    @vm.setter
    def vm(self, value: List[vim.VirtualMachine]):
        self._vm = value


class VmConfigFault(VimFault): ...


class VmConfigIncompatibleForFaultTolerance(VmConfigFault):
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class VmConfigIncompatibleForRecordReplay(VmConfigFault):
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


class VmFaultToleranceConfigIssue(VmFaultToleranceIssue):
    @property
    def reason(self) -> str: ...
    @reason.setter
    def reason(self, value: str):
        self._reason = value
    @property
    def entityName(self) -> str: ...
    @entityName.setter
    def entityName(self, value: str):
        self._entityName = value
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @entity.setter
    def entity(self, value: vim.ManagedEntity):
        self._entity = value


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
    @entityName.setter
    def entityName(self, value: str):
        self._entityName = value
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @entity.setter
    def entity(self, value: vim.ManagedEntity):
        self._entity = value
    @property
    def error(self) -> vmodl.MethodFault: ...
    @error.setter
    def error(self, value: vmodl.MethodFault):
        self._error = value


class VmFaultToleranceInvalidFileBacking(VmFaultToleranceIssue):
    @property
    def backingType(self) -> str: ...
    @backingType.setter
    def backingType(self, value: str):
        self._backingType = value
    @property
    def backingFilename(self) -> str: ...
    @backingFilename.setter
    def backingFilename(self, value: str):
        self._backingFilename = value


class VmFaultToleranceIssue(VimFault): ...


class VmFaultToleranceOpIssuesList(VmFaultToleranceIssue):
    @property
    def errors(self) -> List[vmodl.MethodFault]: ...
    @errors.setter
    def errors(self, value: List[vmodl.MethodFault]):
        self._errors = value
    @property
    def warnings(self) -> List[vmodl.MethodFault]: ...
    @warnings.setter
    def warnings(self, value: List[vmodl.MethodFault]):
        self._warnings = value


class VmFaultToleranceTooManyFtVcpusOnHost(InsufficientResourcesFault):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def maxNumFtVcpus(self) -> int: ...
    @maxNumFtVcpus.setter
    def maxNumFtVcpus(self, value: int):
        self._maxNumFtVcpus = value


class VmFaultToleranceTooManyVMsOnHost(InsufficientResourcesFault):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def maxNumFtVms(self) -> int: ...
    @maxNumFtVms.setter
    def maxNumFtVms(self, value: int):
        self._maxNumFtVms = value


class VmHostAffinityRuleViolation(VmConfigFault):
    @property
    def vmName(self) -> str: ...
    @vmName.setter
    def vmName(self, value: str):
        self._vmName = value
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value


class VmLimitLicense(NotEnoughLicenses):
    @property
    def limit(self) -> int: ...
    @limit.setter
    def limit(self, value: int):
        self._limit = value


class VmMetadataManagerFault(VimFault): ...


class VmMonitorIncompatibleForFaultTolerance(VimFault): ...


class VmPowerOnDisabled(InvalidState): ...


class VmSmpFaultToleranceTooManyVMsOnHost(InsufficientResourcesFault):
    @property
    def hostName(self) -> str: ...
    @hostName.setter
    def hostName(self, value: str):
        self._hostName = value
    @property
    def maxNumSmpFtVms(self) -> int: ...
    @maxNumSmpFtVms.setter
    def maxNumSmpFtVms(self, value: int):
        self._maxNumSmpFtVms = value


class VmToolsUpgradeFault(VimFault): ...


class VmValidateMaxDevice(VimFault):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value
    @property
    def max(self) -> int: ...
    @max.setter
    def max(self, value: int):
        self._max = value
    @property
    def count(self) -> int: ...
    @count.setter
    def count(self, value: int):
        self._count = value


class VmWwnConflict(InvalidVmConfig):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def wwn(self) -> long: ...
    @wwn.setter
    def wwn(self, value: long):
        self._wwn = value


class VmfsAlreadyMounted(VmfsMountFault): ...


class VmfsAmbiguousMount(VmfsMountFault): ...


class VmfsMountFault(HostConfigFault):
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value


class VmotionInterfaceNotEnabled(HostPowerOpFailed): ...


class VolumeEditorError(CustomizationFault): ...


class VramLimitLicense(NotEnoughLicenses):
    @property
    def limit(self) -> int: ...
    @limit.setter
    def limit(self, value: int):
        self._limit = value


class VsanClusterUuidMismatch(CannotMoveVsanEnabledHost):
    @property
    def hostClusterUuid(self) -> str: ...
    @hostClusterUuid.setter
    def hostClusterUuid(self, value: str):
        self._hostClusterUuid = value
    @property
    def destinationClusterUuid(self) -> str: ...
    @destinationClusterUuid.setter
    def destinationClusterUuid(self, value: str):
        self._destinationClusterUuid = value


class VsanDiskFault(VsanFault):
    @property
    def device(self) -> str: ...
    @device.setter
    def device(self, value: str):
        self._device = value


class VsanFault(VimFault): ...


class VsanIncompatibleDiskMapping(VsanDiskFault): ...


class VspanDestPortConflict(DvsFault):
    @property
    def vspanSessionKey1(self) -> str: ...
    @vspanSessionKey1.setter
    def vspanSessionKey1(self, value: str):
        self._vspanSessionKey1 = value
    @property
    def vspanSessionKey2(self) -> str: ...
    @vspanSessionKey2.setter
    def vspanSessionKey2(self, value: str):
        self._vspanSessionKey2 = value
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value


class VspanPortConflict(DvsFault):
    @property
    def vspanSessionKey1(self) -> str: ...
    @vspanSessionKey1.setter
    def vspanSessionKey1(self, value: str):
        self._vspanSessionKey1 = value
    @property
    def vspanSessionKey2(self) -> str: ...
    @vspanSessionKey2.setter
    def vspanSessionKey2(self, value: str):
        self._vspanSessionKey2 = value
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value


class VspanPortMoveFault(DvsFault):
    @property
    def srcPortgroupName(self) -> str: ...
    @srcPortgroupName.setter
    def srcPortgroupName(self, value: str):
        self._srcPortgroupName = value
    @property
    def destPortgroupName(self) -> str: ...
    @destPortgroupName.setter
    def destPortgroupName(self, value: str):
        self._destPortgroupName = value
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value


class VspanPortPromiscChangeFault(DvsFault):
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value


class VspanPortgroupPromiscChangeFault(DvsFault):
    @property
    def portgroupName(self) -> str: ...
    @portgroupName.setter
    def portgroupName(self, value: str):
        self._portgroupName = value


class VspanPortgroupTypeChangeFault(DvsFault):
    @property
    def portgroupName(self) -> str: ...
    @portgroupName.setter
    def portgroupName(self, value: str):
        self._portgroupName = value


class VspanPromiscuousPortNotSupported(DvsFault):
    @property
    def vspanSessionKey(self) -> str: ...
    @vspanSessionKey.setter
    def vspanSessionKey(self, value: str):
        self._vspanSessionKey = value
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value


class VspanSameSessionPortConflict(DvsFault):
    @property
    def vspanSessionKey(self) -> str: ...
    @vspanSessionKey.setter
    def vspanSessionKey(self, value: str):
        self._vspanSessionKey = value
    @property
    def portKey(self) -> str: ...
    @portKey.setter
    def portKey(self, value: str):
        self._portKey = value


class WakeOnLanNotSupported(VirtualHardwareCompatibilityIssue): ...


class WakeOnLanNotSupportedByVmotionNIC(HostPowerOpFailed): ...


class WillLoseHAProtection(MigrationFault):
    @property
    def resolution(self) -> str: ...
    @resolution.setter
    def resolution(self, value: str):
        self._resolution = value


    class Resolution(Enum):
        svmotion = "svmotion"
        relocate = "relocate"


class WillModifyConfigCpuRequirements(MigrationFault): ...


class WillResetSnapshotDirectory(MigrationFault): ...


class WipeDiskFault(VimFault): ...
