from typing import List, Literal
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedMethod, ManagedObject, NoneType, byte, double, long, short
from . import action, alarm, cluster, dvs, encryption, event, ext, fault, host, net, option, profile, scheduler, storageDrs, tenant, vcha, view, vm, vsan, vslm


class AuthorizationManager(ManagedObject):
    @property
    def privilegeList(self) -> List[AuthorizationManager.Privilege]: ...
    @property
    def roleList(self) -> List[AuthorizationManager.Role]: ...
    @property
    def description(self) -> AuthorizationDescription: ...
    def AddRole(self, name: str, privIds: List[str]) -> int: ...
    def RemoveRole(self, roleId: int, failIfUsed: bool) -> NoneType: ...
    def UpdateRole(self, roleId: int, newName: str, privIds: List[str]) -> NoneType: ...
    def MergePermissions(self, srcRoleId: int, dstRoleId: int) -> NoneType: ...
    def RetrieveRolePermissions(self, roleId: int) -> List[AuthorizationManager.Permission]: ...
    def RetrieveEntityPermissions(self, entity: ManagedEntity, inherited: bool) -> List[AuthorizationManager.Permission]: ...
    def RetrieveAllPermissions(self) -> List[AuthorizationManager.Permission]: ...
    def SetEntityPermissions(self, entity: ManagedEntity, permission: List[AuthorizationManager.Permission]) -> NoneType: ...
    def ResetEntityPermissions(self, entity: ManagedEntity, permission: List[AuthorizationManager.Permission]) -> NoneType: ...
    def RemoveEntityPermission(self, entity: ManagedEntity, user: str, isGroup: bool) -> NoneType: ...
    def HasPrivilegeOnEntity(self, entity: ManagedEntity, sessionId: str, privId: List[str]) -> List[bool]: ...
    def HasPrivilegeOnEntities(self, entity: List[ManagedEntity], sessionId: str, privId: List[str]) -> List[AuthorizationManager.EntityPrivilege]: ...
    def HasUserPrivilegeOnEntities(self, entities: List[ManagedObject], userName: str, privId: List[str]) -> List[AuthorizationManager.EntityPrivilege]: ...
    def FetchUserPrivilegeOnEntities(self, entities: List[ManagedEntity], userName: str) -> List[AuthorizationManager.UserPrivilegeResult]: ...


    class EntityPrivilege(vmodl.DynamicData):
        @property
        def entity(self) -> ManagedEntity: ...
        @entity.setter
        def entity(self, value: ManagedEntity):
            self._entity = value
        @property
        def privAvailability(self) -> List[AuthorizationManager.PrivilegeAvailability]: ...
        @privAvailability.setter
        def privAvailability(self, value: List[AuthorizationManager.PrivilegeAvailability]):
            self._privAvailability = value


    class Permission(vmodl.DynamicData):
        @property
        def entity(self) -> ManagedEntity: ...
        @entity.setter
        def entity(self, value: ManagedEntity):
            self._entity = value
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
        def roleId(self) -> int: ...
        @roleId.setter
        def roleId(self, value: int):
            self._roleId = value
        @property
        def propagate(self) -> bool: ...
        @propagate.setter
        def propagate(self, value: bool):
            self._propagate = value


    class Privilege(vmodl.DynamicData):
        @property
        def privId(self) -> str: ...
        @privId.setter
        def privId(self, value: str):
            self._privId = value
        @property
        def onParent(self) -> bool: ...
        @onParent.setter
        def onParent(self, value: bool):
            self._onParent = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def privGroupName(self) -> str: ...
        @privGroupName.setter
        def privGroupName(self, value: str):
            self._privGroupName = value


    class PrivilegeAvailability(vmodl.DynamicData):
        @property
        def privId(self) -> str: ...
        @privId.setter
        def privId(self, value: str):
            self._privId = value
        @property
        def isGranted(self) -> bool: ...
        @isGranted.setter
        def isGranted(self, value: bool):
            self._isGranted = value


    class Role(vmodl.DynamicData):
        @property
        def roleId(self) -> int: ...
        @roleId.setter
        def roleId(self, value: int):
            self._roleId = value
        @property
        def system(self) -> bool: ...
        @system.setter
        def system(self, value: bool):
            self._system = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def info(self) -> Description: ...
        @info.setter
        def info(self, value: Description):
            self._info = value
        @property
        def privilege(self) -> List[str]: ...
        @privilege.setter
        def privilege(self, value: List[str]):
            self._privilege = value


    class UserPrivilegeResult(vmodl.DynamicData):
        @property
        def entity(self) -> ManagedEntity: ...
        @entity.setter
        def entity(self, value: ManagedEntity):
            self._entity = value
        @property
        def privileges(self) -> List[str]: ...
        @privileges.setter
        def privileges(self, value: List[str]):
            self._privileges = value


class CertificateManager(ManagedObject):
    def RefreshCACertificatesAndCRLs(self, host: List[HostSystem]) -> Task: ...
    def RefreshCertificates(self, host: List[HostSystem]) -> Task: ...
    def RevokeCertificates(self, host: List[HostSystem]) -> Task: ...


class ClusterComputeResource(ComputeResource):
    @property
    def configuration(self) -> cluster.ConfigInfo: ...
    @property
    def recommendation(self) -> List[cluster.Recommendation]: ...
    @property
    def drsRecommendation(self) -> List[cluster.DrsRecommendation]: ...
    @property
    def summaryEx(self) -> ClusterComputeResource.Summary: ...
    @property
    def hciConfig(self) -> ClusterComputeResource.HCIConfigInfo: ...
    @property
    def migrationHistory(self) -> List[cluster.DrsMigration]: ...
    @property
    def actionHistory(self) -> List[cluster.ActionHistory]: ...
    @property
    def drsFault(self) -> List[cluster.DrsFaults]: ...
    def ConfigureHCI(self, clusterSpec: ClusterComputeResource.HCIConfigSpec, hostInputs: List[ClusterComputeResource.HostConfigurationInput]) -> Task: ...
    def ExtendHCI(self, hostInputs: List[ClusterComputeResource.HostConfigurationInput], vSanConfigSpec: SDDCBase) -> Task: ...
    def AbandonHciWorkflow(self) -> NoneType: ...
    def ValidateHCIConfiguration(self, hciConfigSpec: ClusterComputeResource.HCIConfigSpec, hosts: List[HostSystem]) -> List[ClusterComputeResource.ValidationResultBase]: ...
    def Reconfigure(self, spec: cluster.ConfigSpec, modify: bool) -> Task: ...
    def ApplyRecommendation(self, key: str) -> NoneType: ...
    def CancelRecommendation(self, key: str) -> NoneType: ...
    def RecommendHostsForVm(self, vm: VirtualMachine, pool: ResourcePool) -> List[cluster.HostRecommendation]: ...
    def AddHost(self, spec: host.ConnectSpec, asConnected: bool, resourcePool: ResourcePool, license: str) -> Task: ...
    def MoveInto(self, host: List[HostSystem]) -> Task: ...
    def MoveHostInto(self, host: HostSystem, resourcePool: ResourcePool) -> Task: ...
    def RefreshRecommendation(self) -> NoneType: ...
    def EvcManager(self) -> cluster.EVCManager: ...
    def RetrieveDasAdvancedRuntimeInfo(self) -> cluster.DasAdvancedRuntimeInfo: ...
    def EnterMaintenanceMode(self, host: List[HostSystem], option: List[option.OptionValue]) -> cluster.EnterMaintenanceResult: ...
    def PlaceVm(self, placementSpec: cluster.PlacementSpec) -> cluster.PlacementResult: ...
    def FindRulesForVm(self, vm: VirtualMachine) -> List[cluster.RuleInfo]: ...
    def StampAllRulesWithUuid(self) -> Task: ...
    def GetResourceUsage(self) -> cluster.ResourceUsageSummary: ...
    def SetCryptoMode(self, cryptoMode: str) -> NoneType: ...
    def GetSystemVMsRestrictedDatastores(self) -> List[Datastore]: ...


    class ClusterConfigResult(vmodl.DynamicData):
        @property
        def failedHosts(self) -> List[Folder.FailedHostResult]: ...
        @failedHosts.setter
        def failedHosts(self, value: List[Folder.FailedHostResult]):
            self._failedHosts = value
        @property
        def configuredHosts(self) -> List[HostSystem]: ...
        @configuredHosts.setter
        def configuredHosts(self, value: List[HostSystem]):
            self._configuredHosts = value


    class DVSConfigurationValidation(ClusterComputeResource.ValidationResultBase):
        @property
        def isDvsValid(self) -> bool: ...
        @isDvsValid.setter
        def isDvsValid(self, value: bool):
            self._isDvsValid = value
        @property
        def isDvpgValid(self) -> bool: ...
        @isDvpgValid.setter
        def isDvpgValid(self, value: bool):
            self._isDvpgValid = value


    class DVSSetting(vmodl.DynamicData):
        @property
        def dvSwitch(self) -> DistributedVirtualSwitch: ...
        @dvSwitch.setter
        def dvSwitch(self, value: DistributedVirtualSwitch):
            self._dvSwitch = value
        @property
        def pnicDevices(self) -> List[str]: ...
        @pnicDevices.setter
        def pnicDevices(self, value: List[str]):
            self._pnicDevices = value
        @property
        def dvPortgroupSetting(self) -> List[ClusterComputeResource.DVSSetting.DVPortgroupToServiceMapping]: ...
        @dvPortgroupSetting.setter
        def dvPortgroupSetting(self, value: List[ClusterComputeResource.DVSSetting.DVPortgroupToServiceMapping]):
            self._dvPortgroupSetting = value


        class DVPortgroupToServiceMapping(vmodl.DynamicData):
            @property
            def dvPortgroup(self) -> dvs.DistributedVirtualPortgroup: ...
            @dvPortgroup.setter
            def dvPortgroup(self, value: dvs.DistributedVirtualPortgroup):
                self._dvPortgroup = value
            @property
            def service(self) -> str: ...
            @service.setter
            def service(self, value: str):
                self._service = value


    class DvsProfile(vmodl.DynamicData):
        @property
        def dvsName(self) -> str: ...
        @dvsName.setter
        def dvsName(self, value: str):
            self._dvsName = value
        @property
        def dvSwitch(self) -> DistributedVirtualSwitch: ...
        @dvSwitch.setter
        def dvSwitch(self, value: DistributedVirtualSwitch):
            self._dvSwitch = value
        @property
        def pnicDevices(self) -> List[str]: ...
        @pnicDevices.setter
        def pnicDevices(self, value: List[str]):
            self._pnicDevices = value
        @property
        def dvPortgroupMapping(self) -> List[ClusterComputeResource.DvsProfile.DVPortgroupSpecToServiceMapping]: ...
        @dvPortgroupMapping.setter
        def dvPortgroupMapping(self, value: List[ClusterComputeResource.DvsProfile.DVPortgroupSpecToServiceMapping]):
            self._dvPortgroupMapping = value


        class DVPortgroupSpecToServiceMapping(vmodl.DynamicData):
            @property
            def dvPortgroupSpec(self) -> dvs.DistributedVirtualPortgroup.ConfigSpec: ...
            @dvPortgroupSpec.setter
            def dvPortgroupSpec(self, value: dvs.DistributedVirtualPortgroup.ConfigSpec):
                self._dvPortgroupSpec = value
            @property
            def dvPortgroup(self) -> dvs.DistributedVirtualPortgroup: ...
            @dvPortgroup.setter
            def dvPortgroup(self, value: dvs.DistributedVirtualPortgroup):
                self._dvPortgroup = value
            @property
            def service(self) -> str: ...
            @service.setter
            def service(self, value: str):
                self._service = value


    class HCIConfigInfo(vmodl.DynamicData):
        @property
        def workflowState(self) -> str: ...
        @workflowState.setter
        def workflowState(self, value: str):
            self._workflowState = value
        @property
        def dvsSetting(self) -> List[ClusterComputeResource.DVSSetting]: ...
        @dvsSetting.setter
        def dvsSetting(self, value: List[ClusterComputeResource.DVSSetting]):
            self._dvsSetting = value
        @property
        def configuredHosts(self) -> List[HostSystem]: ...
        @configuredHosts.setter
        def configuredHosts(self, value: List[HostSystem]):
            self._configuredHosts = value
        @property
        def hostConfigProfile(self) -> ClusterComputeResource.HostConfigurationProfile: ...
        @hostConfigProfile.setter
        def hostConfigProfile(self, value: ClusterComputeResource.HostConfigurationProfile):
            self._hostConfigProfile = value


    class HCIConfigSpec(vmodl.DynamicData):
        @property
        def dvsProf(self) -> List[ClusterComputeResource.DvsProfile]: ...
        @dvsProf.setter
        def dvsProf(self, value: List[ClusterComputeResource.DvsProfile]):
            self._dvsProf = value
        @property
        def hostConfigProfile(self) -> ClusterComputeResource.HostConfigurationProfile: ...
        @hostConfigProfile.setter
        def hostConfigProfile(self, value: ClusterComputeResource.HostConfigurationProfile):
            self._hostConfigProfile = value
        @property
        def vSanConfigSpec(self) -> SDDCBase: ...
        @vSanConfigSpec.setter
        def vSanConfigSpec(self, value: SDDCBase):
            self._vSanConfigSpec = value
        @property
        def vcProf(self) -> ClusterComputeResource.VCProfile: ...
        @vcProf.setter
        def vcProf(self, value: ClusterComputeResource.VCProfile):
            self._vcProf = value


    class HostConfigurationInput(vmodl.DynamicData):
        @property
        def host(self) -> HostSystem: ...
        @host.setter
        def host(self, value: HostSystem):
            self._host = value
        @property
        def hostVmkNics(self) -> List[ClusterComputeResource.HostVmkNicInfo]: ...
        @hostVmkNics.setter
        def hostVmkNics(self, value: List[ClusterComputeResource.HostVmkNicInfo]):
            self._hostVmkNics = value
        @property
        def allowedInNonMaintenanceMode(self) -> bool: ...
        @allowedInNonMaintenanceMode.setter
        def allowedInNonMaintenanceMode(self, value: bool):
            self._allowedInNonMaintenanceMode = value


    class HostConfigurationProfile(vmodl.DynamicData):
        @property
        def dateTimeConfig(self) -> host.DateTimeConfig: ...
        @dateTimeConfig.setter
        def dateTimeConfig(self, value: host.DateTimeConfig):
            self._dateTimeConfig = value
        @property
        def lockdownMode(self) -> host.HostAccessManager.LockdownMode | Literal['lockdownDisabled', 'lockdownNormal', 'lockdownStrict']: ...
        @lockdownMode.setter
        def lockdownMode(self, value: host.HostAccessManager.LockdownMode | Literal['lockdownDisabled', 'lockdownNormal', 'lockdownStrict']):
            self._lockdownMode = value


    class HostConfigurationValidation(ClusterComputeResource.ValidationResultBase):
        @property
        def host(self) -> HostSystem: ...
        @host.setter
        def host(self, value: HostSystem):
            self._host = value
        @property
        def isDvsSettingValid(self) -> bool: ...
        @isDvsSettingValid.setter
        def isDvsSettingValid(self, value: bool):
            self._isDvsSettingValid = value
        @property
        def isVmknicSettingValid(self) -> bool: ...
        @isVmknicSettingValid.setter
        def isVmknicSettingValid(self, value: bool):
            self._isVmknicSettingValid = value
        @property
        def isNtpSettingValid(self) -> bool: ...
        @isNtpSettingValid.setter
        def isNtpSettingValid(self, value: bool):
            self._isNtpSettingValid = value
        @property
        def isLockdownModeValid(self) -> bool: ...
        @isLockdownModeValid.setter
        def isLockdownModeValid(self, value: bool):
            self._isLockdownModeValid = value


    class HostVmkNicInfo(vmodl.DynamicData):
        @property
        def nicSpec(self) -> host.VirtualNic.Specification: ...
        @nicSpec.setter
        def nicSpec(self, value: host.VirtualNic.Specification):
            self._nicSpec = value
        @property
        def service(self) -> str: ...
        @service.setter
        def service(self, value: str):
            self._service = value


    class Summary(ComputeResource.Summary):
        @property
        def currentFailoverLevel(self) -> int: ...
        @currentFailoverLevel.setter
        def currentFailoverLevel(self, value: int):
            self._currentFailoverLevel = value
        @property
        def admissionControlInfo(self) -> cluster.DasAdmissionControlInfo: ...
        @admissionControlInfo.setter
        def admissionControlInfo(self, value: cluster.DasAdmissionControlInfo):
            self._admissionControlInfo = value
        @property
        def numVmotions(self) -> int: ...
        @numVmotions.setter
        def numVmotions(self, value: int):
            self._numVmotions = value
        @property
        def targetBalance(self) -> int: ...
        @targetBalance.setter
        def targetBalance(self, value: int):
            self._targetBalance = value
        @property
        def currentBalance(self) -> int: ...
        @currentBalance.setter
        def currentBalance(self, value: int):
            self._currentBalance = value
        @property
        def drsScore(self) -> int: ...
        @drsScore.setter
        def drsScore(self, value: int):
            self._drsScore = value
        @property
        def numVmsPerDrsScoreBucket(self) -> List[int]: ...
        @numVmsPerDrsScoreBucket.setter
        def numVmsPerDrsScoreBucket(self, value: List[int]):
            self._numVmsPerDrsScoreBucket = value
        @property
        def usageSummary(self) -> cluster.UsageSummary: ...
        @usageSummary.setter
        def usageSummary(self, value: cluster.UsageSummary):
            self._usageSummary = value
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
        def dasData(self) -> cluster.DasData: ...
        @dasData.setter
        def dasData(self, value: cluster.DasData):
            self._dasData = value
        @property
        def clusterMaintenanceModeStatus(self) -> str: ...
        @clusterMaintenanceModeStatus.setter
        def clusterMaintenanceModeStatus(self, value: str):
            self._clusterMaintenanceModeStatus = value
        @property
        def vcsHealthStatus(self) -> str: ...
        @vcsHealthStatus.setter
        def vcsHealthStatus(self, value: str):
            self._vcsHealthStatus = value
        @property
        def vcsSlots(self) -> List[ClusterComputeResource.VcsSlots]: ...
        @vcsSlots.setter
        def vcsSlots(self, value: List[ClusterComputeResource.VcsSlots]):
            self._vcsSlots = value


    class VCProfile(vmodl.DynamicData):
        @property
        def clusterSpec(self) -> cluster.ConfigSpecEx: ...
        @clusterSpec.setter
        def clusterSpec(self, value: cluster.ConfigSpecEx):
            self._clusterSpec = value
        @property
        def evcModeKey(self) -> str: ...
        @evcModeKey.setter
        def evcModeKey(self, value: str):
            self._evcModeKey = value
        @property
        def evcGraphicsModeKey(self) -> str: ...
        @evcGraphicsModeKey.setter
        def evcGraphicsModeKey(self, value: str):
            self._evcGraphicsModeKey = value


    class ValidationResultBase(vmodl.DynamicData):
        @property
        def info(self) -> List[vmodl.LocalizableMessage]: ...
        @info.setter
        def info(self, value: List[vmodl.LocalizableMessage]):
            self._info = value


    class VcsSlots(vmodl.DynamicData):
        @property
        def systemId(self) -> str: ...
        @systemId.setter
        def systemId(self, value: str):
            self._systemId = value
        @property
        def host(self) -> HostSystem: ...
        @host.setter
        def host(self, value: HostSystem):
            self._host = value
        @property
        def datastore(self) -> List[Datastore]: ...
        @datastore.setter
        def datastore(self, value: List[Datastore]):
            self._datastore = value
        @property
        def totalSlots(self) -> int: ...
        @totalSlots.setter
        def totalSlots(self, value: int):
            self._totalSlots = value


    class HCIWorkflowState(Enum):
        in_progress = "in_progress"
        done = "done"
        invalid = "invalid"


    class VcsHealthStatus(Enum):
        healthy = "healthy"
        degraded = "degraded"
        nonhealthy = "nonhealthy"


class ComputeResource(ManagedEntity):
    @property
    def resourcePool(self) -> ResourcePool: ...
    @property
    def host(self) -> List[HostSystem]: ...
    @property
    def datastore(self) -> List[Datastore]: ...
    @property
    def network(self) -> List[Network]: ...
    @property
    def summary(self) -> ComputeResource.Summary: ...
    @property
    def environmentBrowser(self) -> EnvironmentBrowser: ...
    @property
    def configurationEx(self) -> ComputeResource.ConfigInfo: ...
    @property
    def lifecycleManaged(self) -> bool: ...
    @property
    def configManagerEnabled(self) -> bool: ...
    def ReconfigureEx(self, spec: ComputeResource.ConfigSpec, modify: bool) -> Task: ...


    class ConfigInfo(vmodl.DynamicData):
        @property
        def vmSwapPlacement(self) -> str: ...
        @vmSwapPlacement.setter
        def vmSwapPlacement(self, value: str):
            self._vmSwapPlacement = value
        @property
        def spbmEnabled(self) -> bool: ...
        @spbmEnabled.setter
        def spbmEnabled(self, value: bool):
            self._spbmEnabled = value
        @property
        def defaultHardwareVersionKey(self) -> str: ...
        @defaultHardwareVersionKey.setter
        def defaultHardwareVersionKey(self, value: str):
            self._defaultHardwareVersionKey = value
        @property
        def maximumHardwareVersionKey(self) -> str: ...
        @maximumHardwareVersionKey.setter
        def maximumHardwareVersionKey(self, value: str):
            self._maximumHardwareVersionKey = value


    class ConfigSpec(vmodl.DynamicData):
        @property
        def vmSwapPlacement(self) -> str: ...
        @vmSwapPlacement.setter
        def vmSwapPlacement(self, value: str):
            self._vmSwapPlacement = value
        @property
        def spbmEnabled(self) -> bool: ...
        @spbmEnabled.setter
        def spbmEnabled(self, value: bool):
            self._spbmEnabled = value
        @property
        def defaultHardwareVersionKey(self) -> str: ...
        @defaultHardwareVersionKey.setter
        def defaultHardwareVersionKey(self, value: str):
            self._defaultHardwareVersionKey = value
        @property
        def desiredSoftwareSpec(self) -> DesiredSoftwareSpec: ...
        @desiredSoftwareSpec.setter
        def desiredSoftwareSpec(self, value: DesiredSoftwareSpec):
            self._desiredSoftwareSpec = value
        @property
        def maximumHardwareVersionKey(self) -> str: ...
        @maximumHardwareVersionKey.setter
        def maximumHardwareVersionKey(self, value: str):
            self._maximumHardwareVersionKey = value
        @property
        def enableConfigManager(self) -> bool: ...
        @enableConfigManager.setter
        def enableConfigManager(self, value: bool):
            self._enableConfigManager = value


    class HostSPBMLicenseInfo(vmodl.DynamicData):
        @property
        def host(self) -> HostSystem: ...
        @host.setter
        def host(self, value: HostSystem):
            self._host = value
        @property
        def licenseState(self) -> ComputeResource.HostSPBMLicenseInfo.HostSPBMLicenseState | Literal['licensed', 'unlicensed', 'unknown']: ...
        @licenseState.setter
        def licenseState(self, value: ComputeResource.HostSPBMLicenseInfo.HostSPBMLicenseState | Literal['licensed', 'unlicensed', 'unknown']):
            self._licenseState = value


        class HostSPBMLicenseState(Enum):
            licensed = "licensed"
            unlicensed = "unlicensed"
            unknown = "unknown"


    class Summary(vmodl.DynamicData):
        @property
        def totalCpu(self) -> int: ...
        @totalCpu.setter
        def totalCpu(self, value: int):
            self._totalCpu = value
        @property
        def totalMemory(self) -> long: ...
        @totalMemory.setter
        def totalMemory(self, value: long):
            self._totalMemory = value
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
        def effectiveCpu(self) -> int: ...
        @effectiveCpu.setter
        def effectiveCpu(self, value: int):
            self._effectiveCpu = value
        @property
        def effectiveMemory(self) -> long: ...
        @effectiveMemory.setter
        def effectiveMemory(self, value: long):
            self._effectiveMemory = value
        @property
        def numHosts(self) -> int: ...
        @numHosts.setter
        def numHosts(self, value: int):
            self._numHosts = value
        @property
        def numEffectiveHosts(self) -> int: ...
        @numEffectiveHosts.setter
        def numEffectiveHosts(self, value: int):
            self._numEffectiveHosts = value
        @property
        def overallStatus(self) -> ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']: ...
        @overallStatus.setter
        def overallStatus(self, value: ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']):
            self._overallStatus = value


class CustomFieldsManager(ManagedObject):
    @property
    def field(self) -> List[CustomFieldsManager.FieldDef]: ...
    def AddFieldDefinition(self, name: str, moType: type, fieldDefPolicy: PrivilegePolicyDef, fieldPolicy: PrivilegePolicyDef) -> CustomFieldsManager.FieldDef: ...
    def RemoveFieldDefinition(self, key: int) -> NoneType: ...
    def RenameFieldDefinition(self, key: int, name: str) -> NoneType: ...
    def SetField(self, entity: ManagedEntity, key: int, value: str) -> NoneType: ...


    class FieldDef(vmodl.DynamicData):
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
        def type(self) -> type: ...
        @type.setter
        def type(self, value: type):
            self._type = value
        @property
        def managedObjectType(self) -> type: ...
        @managedObjectType.setter
        def managedObjectType(self, value: type):
            self._managedObjectType = value
        @property
        def fieldDefPrivileges(self) -> PrivilegePolicyDef: ...
        @fieldDefPrivileges.setter
        def fieldDefPrivileges(self, value: PrivilegePolicyDef):
            self._fieldDefPrivileges = value
        @property
        def fieldInstancePrivileges(self) -> PrivilegePolicyDef: ...
        @fieldInstancePrivileges.setter
        def fieldInstancePrivileges(self, value: PrivilegePolicyDef):
            self._fieldInstancePrivileges = value


    class StringValue(CustomFieldsManager.Value):
        @property
        def value(self) -> str: ...
        @value.setter
        def value(self, value: str):
            self._value = value


    class Value(vmodl.DynamicData):
        @property
        def key(self) -> int: ...
        @key.setter
        def key(self, value: int):
            self._key = value


class CustomizationSpecManager(ManagedObject):
    @property
    def info(self) -> List[CustomizationSpecInfo]: ...
    @property
    def encryptionKey(self) -> List[byte]: ...
    def Exists(self, name: str) -> bool: ...
    def Get(self, name: str) -> CustomizationSpecItem: ...
    def Create(self, item: CustomizationSpecItem) -> NoneType: ...
    def Overwrite(self, item: CustomizationSpecItem) -> NoneType: ...
    def Delete(self, name: str) -> NoneType: ...
    def Duplicate(self, name: str, newName: str) -> NoneType: ...
    def Rename(self, name: str, newName: str) -> NoneType: ...
    def SpecItemToXml(self, item: CustomizationSpecItem) -> str: ...
    def XmlToSpecItem(self, specItemXml: str) -> CustomizationSpecItem: ...
    def CheckResources(self, guestOs: str) -> NoneType: ...


class Datacenter(ManagedEntity):
    @property
    def vmFolder(self) -> Folder: ...
    @property
    def hostFolder(self) -> Folder: ...
    @property
    def datastoreFolder(self) -> Folder: ...
    @property
    def networkFolder(self) -> Folder: ...
    @property
    def datastore(self) -> List[Datastore]: ...
    @property
    def network(self) -> List[Network]: ...
    @property
    def configuration(self) -> Datacenter.ConfigInfo: ...
    def BatchQueryConnectInfo(self, hostSpecs: List[host.ConnectSpec]) -> List[Datacenter.BasicConnectInfo]: ...
    def QueryConnectionInfo(self, hostname: str, port: int, username: str, password: str, sslThumbprint: str) -> host.ConnectInfo: ...
    def QueryConnectionInfoViaSpec(self, spec: host.ConnectSpec) -> host.ConnectInfo: ...
    def PowerOnVm(self, vm: List[VirtualMachine], option: List[option.OptionValue]) -> Task: ...
    def QueryConfigOptionDescriptor(self) -> List[vm.ConfigOptionDescriptor]: ...
    def Reconfigure(self, spec: Datacenter.ConfigSpec, modify: bool) -> Task: ...


    class BasicConnectInfo(vmodl.DynamicData):
        @property
        def hostname(self) -> str: ...
        @hostname.setter
        def hostname(self, value: str):
            self._hostname = value
        @property
        def error(self) -> vmodl.MethodFault: ...
        @error.setter
        def error(self, value: vmodl.MethodFault):
            self._error = value
        @property
        def serverIp(self) -> str: ...
        @serverIp.setter
        def serverIp(self, value: str):
            self._serverIp = value
        @property
        def numVm(self) -> int: ...
        @numVm.setter
        def numVm(self, value: int):
            self._numVm = value
        @property
        def numPoweredOnVm(self) -> int: ...
        @numPoweredOnVm.setter
        def numPoweredOnVm(self, value: int):
            self._numPoweredOnVm = value
        @property
        def hostProductInfo(self) -> AboutInfo: ...
        @hostProductInfo.setter
        def hostProductInfo(self, value: AboutInfo):
            self._hostProductInfo = value
        @property
        def hardwareVendor(self) -> str: ...
        @hardwareVendor.setter
        def hardwareVendor(self, value: str):
            self._hardwareVendor = value
        @property
        def hardwareModel(self) -> str: ...
        @hardwareModel.setter
        def hardwareModel(self, value: str):
            self._hardwareModel = value


    class ConfigInfo(vmodl.DynamicData):
        @property
        def defaultHardwareVersionKey(self) -> str: ...
        @defaultHardwareVersionKey.setter
        def defaultHardwareVersionKey(self, value: str):
            self._defaultHardwareVersionKey = value
        @property
        def maximumHardwareVersionKey(self) -> str: ...
        @maximumHardwareVersionKey.setter
        def maximumHardwareVersionKey(self, value: str):
            self._maximumHardwareVersionKey = value


    class ConfigSpec(vmodl.DynamicData):
        @property
        def defaultHardwareVersionKey(self) -> str: ...
        @defaultHardwareVersionKey.setter
        def defaultHardwareVersionKey(self, value: str):
            self._defaultHardwareVersionKey = value
        @property
        def maximumHardwareVersionKey(self) -> str: ...
        @maximumHardwareVersionKey.setter
        def maximumHardwareVersionKey(self, value: str):
            self._maximumHardwareVersionKey = value


class Datastore(ManagedEntity):
    @property
    def info(self) -> Datastore.Info: ...
    @property
    def summary(self) -> Datastore.Summary: ...
    @property
    def host(self) -> List[Datastore.HostMount]: ...
    @property
    def vm(self) -> List[VirtualMachine]: ...
    @property
    def browser(self) -> host.DatastoreBrowser: ...
    @property
    def capability(self) -> Datastore.Capability: ...
    @property
    def iormConfiguration(self) -> StorageResourceManager.IORMConfigInfo: ...
    def Refresh(self) -> NoneType: ...
    def RefreshStorageInfo(self) -> NoneType: ...
    def UpdateVirtualMachineFiles(self, mountPathDatastoreMapping: List[Datastore.MountPathDatastorePair]) -> Task: ...
    def RenameDatastore(self, newName: str) -> NoneType: ...
    def DestroyDatastore(self) -> NoneType: ...
    def EnterMaintenanceMode(self) -> storageDrs.StoragePlacementResult: ...
    def ExitMaintenanceMode(self) -> Task: ...
    def IsClusteredVmdkEnabled(self) -> bool: ...
    def UpdateVVolVirtualMachineFiles(self, failoverPair: List[Datastore.VVolContainerFailoverPair]) -> Task: ...


    class Capability(vmodl.DynamicData):
        @property
        def directoryHierarchySupported(self) -> bool: ...
        @directoryHierarchySupported.setter
        def directoryHierarchySupported(self, value: bool):
            self._directoryHierarchySupported = value
        @property
        def rawDiskMappingsSupported(self) -> bool: ...
        @rawDiskMappingsSupported.setter
        def rawDiskMappingsSupported(self, value: bool):
            self._rawDiskMappingsSupported = value
        @property
        def perFileThinProvisioningSupported(self) -> bool: ...
        @perFileThinProvisioningSupported.setter
        def perFileThinProvisioningSupported(self, value: bool):
            self._perFileThinProvisioningSupported = value
        @property
        def storageIORMSupported(self) -> bool: ...
        @storageIORMSupported.setter
        def storageIORMSupported(self, value: bool):
            self._storageIORMSupported = value
        @property
        def nativeSnapshotSupported(self) -> bool: ...
        @nativeSnapshotSupported.setter
        def nativeSnapshotSupported(self, value: bool):
            self._nativeSnapshotSupported = value
        @property
        def topLevelDirectoryCreateSupported(self) -> bool: ...
        @topLevelDirectoryCreateSupported.setter
        def topLevelDirectoryCreateSupported(self, value: bool):
            self._topLevelDirectoryCreateSupported = value
        @property
        def seSparseSupported(self) -> bool: ...
        @seSparseSupported.setter
        def seSparseSupported(self, value: bool):
            self._seSparseSupported = value
        @property
        def vmfsSparseSupported(self) -> bool: ...
        @vmfsSparseSupported.setter
        def vmfsSparseSupported(self, value: bool):
            self._vmfsSparseSupported = value
        @property
        def vsanSparseSupported(self) -> bool: ...
        @vsanSparseSupported.setter
        def vsanSparseSupported(self, value: bool):
            self._vsanSparseSupported = value
        @property
        def upitSupported(self) -> bool: ...
        @upitSupported.setter
        def upitSupported(self, value: bool):
            self._upitSupported = value
        @property
        def vmdkExpandSupported(self) -> bool: ...
        @vmdkExpandSupported.setter
        def vmdkExpandSupported(self, value: bool):
            self._vmdkExpandSupported = value
        @property
        def clusteredVmdkSupported(self) -> bool: ...
        @clusteredVmdkSupported.setter
        def clusteredVmdkSupported(self, value: bool):
            self._clusteredVmdkSupported = value


    class HostMount(vmodl.DynamicData):
        @property
        def key(self) -> HostSystem: ...
        @key.setter
        def key(self, value: HostSystem):
            self._key = value
        @property
        def mountInfo(self) -> host.MountInfo: ...
        @mountInfo.setter
        def mountInfo(self, value: host.MountInfo):
            self._mountInfo = value


    class Info(vmodl.DynamicData):
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
        @property
        def freeSpace(self) -> long: ...
        @freeSpace.setter
        def freeSpace(self, value: long):
            self._freeSpace = value
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
        def maxMemoryFileSize(self) -> long: ...
        @maxMemoryFileSize.setter
        def maxMemoryFileSize(self, value: long):
            self._maxMemoryFileSize = value
        @property
        def timestamp(self) -> datetime: ...
        @timestamp.setter
        def timestamp(self, value: datetime):
            self._timestamp = value
        @property
        def containerId(self) -> str: ...
        @containerId.setter
        def containerId(self, value: str):
            self._containerId = value
        @property
        def aliasOf(self) -> str: ...
        @aliasOf.setter
        def aliasOf(self, value: str):
            self._aliasOf = value


    class MountPathDatastorePair(vmodl.DynamicData):
        @property
        def oldMountPath(self) -> str: ...
        @oldMountPath.setter
        def oldMountPath(self, value: str):
            self._oldMountPath = value
        @property
        def datastore(self) -> Datastore: ...
        @datastore.setter
        def datastore(self, value: Datastore):
            self._datastore = value


    class Summary(vmodl.DynamicData):
        @property
        def datastore(self) -> Datastore: ...
        @datastore.setter
        def datastore(self, value: Datastore):
            self._datastore = value
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
        def uncommitted(self) -> long: ...
        @uncommitted.setter
        def uncommitted(self, value: long):
            self._uncommitted = value
        @property
        def accessible(self) -> bool: ...
        @accessible.setter
        def accessible(self, value: bool):
            self._accessible = value
        @property
        def multipleHostAccess(self) -> bool: ...
        @multipleHostAccess.setter
        def multipleHostAccess(self, value: bool):
            self._multipleHostAccess = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def maintenanceMode(self) -> str: ...
        @maintenanceMode.setter
        def maintenanceMode(self, value: str):
            self._maintenanceMode = value


        class MaintenanceModeState(Enum):
            normal = "normal"
            enteringMaintenance = "enteringMaintenance"
            inMaintenance = "inMaintenance"


    class VVolContainerFailoverPair(vmodl.DynamicData):
        @property
        def srcContainer(self) -> str: ...
        @srcContainer.setter
        def srcContainer(self, value: str):
            self._srcContainer = value
        @property
        def tgtContainer(self) -> str: ...
        @tgtContainer.setter
        def tgtContainer(self, value: str):
            self._tgtContainer = value
        @property
        def vvolMapping(self) -> List[KeyValue]: ...
        @vvolMapping.setter
        def vvolMapping(self, value: List[KeyValue]):
            self._vvolMapping = value


    class Accessible(Enum):
        True
        False


class DatastoreNamespaceManager(ManagedObject):
    def CreateDirectory(self, datastore: Datastore, displayName: str, policy: str, size: long) -> str: ...
    def DeleteDirectory(self, datacenter: Datacenter, datastorePath: str) -> NoneType: ...
    def ConvertNamespacePathToUuidPath(self, datacenter: Datacenter, namespaceUrl: str) -> str: ...
    def IncreaseDirectorySize(self, datacenter: Datacenter, stableName: str, size: long) -> NoneType: ...
    def QueryDirectoryInfo(self, datacenter: Datacenter, stableName: str) -> DatastoreNamespaceManager.DirectoryInfo: ...


    class DirectoryInfo(vmodl.DynamicData):
        @property
        def capacity(self) -> long: ...
        @capacity.setter
        def capacity(self, value: long):
            self._capacity = value
        @property
        def used(self) -> long: ...
        @used.setter
        def used(self, value: long):
            self._used = value


class DiagnosticManager(ManagedObject):
    def QueryDescriptions(self, host: HostSystem) -> List[DiagnosticManager.LogDescriptor]: ...
    def Browse(self, host: HostSystem, key: str, start: int, lines: int) -> DiagnosticManager.LogHeader: ...
    def GenerateLogBundles(self, includeDefault: bool, host: List[HostSystem]) -> Task: ...
    def FetchAuditRecords(self, token: str) -> DiagnosticManager.AuditRecordResult: ...
    def EmitSyslogMark(self, message: str) -> NoneType: ...


    class AuditRecordResult(vmodl.DynamicData):
        @property
        def records(self) -> List[str]: ...
        @records.setter
        def records(self, value: List[str]):
            self._records = value
        @property
        def nextToken(self) -> str: ...
        @nextToken.setter
        def nextToken(self, value: str):
            self._nextToken = value


    class BundleInfo(vmodl.DynamicData):
        @property
        def system(self) -> HostSystem: ...
        @system.setter
        def system(self, value: HostSystem):
            self._system = value
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value


    class LogDescriptor(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def fileName(self) -> str: ...
        @fileName.setter
        def fileName(self, value: str):
            self._fileName = value
        @property
        def creator(self) -> str: ...
        @creator.setter
        def creator(self, value: str):
            self._creator = value
        @property
        def format(self) -> str: ...
        @format.setter
        def format(self, value: str):
            self._format = value
        @property
        def mimeType(self) -> str: ...
        @mimeType.setter
        def mimeType(self, value: str):
            self._mimeType = value
        @property
        def info(self) -> Description: ...
        @info.setter
        def info(self, value: Description):
            self._info = value


        class Creator(Enum):
            vpxd = "vpxd"
            vpxa = "vpxa"
            hostd = "hostd"
            serverd = "serverd"
            install = "install"
            vpxClient = "vpxClient"
            recordLog = "recordLog"


        class Format(Enum):
            plain = "plain"


    class LogHeader(vmodl.DynamicData):
        @property
        def lineStart(self) -> int: ...
        @lineStart.setter
        def lineStart(self, value: int):
            self._lineStart = value
        @property
        def lineEnd(self) -> int: ...
        @lineEnd.setter
        def lineEnd(self, value: int):
            self._lineEnd = value
        @property
        def lineText(self) -> List[str]: ...
        @lineText.setter
        def lineText(self, value: List[str]):
            self._lineText = value


class DistributedVirtualSwitch(ManagedEntity):
    @property
    def uuid(self) -> str: ...
    @property
    def capability(self) -> DistributedVirtualSwitch.Capability: ...
    @property
    def summary(self) -> DistributedVirtualSwitch.Summary: ...
    @property
    def config(self) -> DistributedVirtualSwitch.ConfigInfo: ...
    @property
    def networkResourcePool(self) -> List[dvs.NetworkResourcePool]: ...
    @property
    def portgroup(self) -> List[dvs.DistributedVirtualPortgroup]: ...
    @property
    def runtime(self) -> DistributedVirtualSwitch.RuntimeInfo: ...
    def FetchPortKeys(self, criteria: dvs.PortCriteria) -> List[str]: ...
    def FetchPorts(self, criteria: dvs.PortCriteria) -> List[dvs.DistributedVirtualPort]: ...
    def QueryUsedVlanId(self) -> List[int]: ...
    def Reconfigure(self, spec: DistributedVirtualSwitch.ConfigSpec) -> Task: ...
    def PerformProductSpecOperation(self, operation: str, productSpec: dvs.ProductSpec) -> Task: ...
    def Merge(self, dvs: DistributedVirtualSwitch) -> Task: ...
    def AddPortgroups(self, spec: List[dvs.DistributedVirtualPortgroup.ConfigSpec]) -> Task: ...
    def MovePort(self, portKey: List[str], destinationPortgroupKey: str) -> Task: ...
    def UpdateCapability(self, capability: DistributedVirtualSwitch.Capability) -> NoneType: ...
    def ReconfigurePort(self, port: List[dvs.DistributedVirtualPort.ConfigSpec]) -> Task: ...
    def RefreshPortState(self, portKeys: List[str]) -> NoneType: ...
    def RectifyHost(self, hosts: List[HostSystem]) -> Task: ...
    def UpdateNetworkResourcePool(self, configSpec: List[dvs.NetworkResourcePool.ConfigSpec]) -> NoneType: ...
    def AddNetworkResourcePool(self, configSpec: List[dvs.NetworkResourcePool.ConfigSpec]) -> NoneType: ...
    def RemoveNetworkResourcePool(self, key: List[str]) -> NoneType: ...
    def ReconfigureVmVnicNetworkResourcePool(self, configSpec: List[dvs.VmVnicNetworkResourcePool.ConfigSpec]) -> Task: ...
    def EnableNetworkResourceManagement(self, enable: bool) -> NoneType: ...
    def Rollback(self, entityBackup: dvs.EntityBackup.Config) -> Task: ...
    def AddPortgroup(self, spec: dvs.DistributedVirtualPortgroup.ConfigSpec) -> Task: ...
    def UpdateHealthCheckConfig(self, healthCheckConfig: List[DistributedVirtualSwitch.HealthCheckConfig]) -> Task: ...
    def LookupPortgroup(self, portgroupKey: str) -> dvs.DistributedVirtualPortgroup: ...


    class BackupRestoreCapability(vmodl.DynamicData):
        @property
        def backupRestoreSupported(self) -> bool: ...
        @backupRestoreSupported.setter
        def backupRestoreSupported(self, value: bool):
            self._backupRestoreSupported = value


    class Capability(vmodl.DynamicData):
        @property
        def dvsOperationSupported(self) -> bool: ...
        @dvsOperationSupported.setter
        def dvsOperationSupported(self, value: bool):
            self._dvsOperationSupported = value
        @property
        def dvPortGroupOperationSupported(self) -> bool: ...
        @dvPortGroupOperationSupported.setter
        def dvPortGroupOperationSupported(self, value: bool):
            self._dvPortGroupOperationSupported = value
        @property
        def dvPortOperationSupported(self) -> bool: ...
        @dvPortOperationSupported.setter
        def dvPortOperationSupported(self, value: bool):
            self._dvPortOperationSupported = value
        @property
        def compatibleHostComponentProductInfo(self) -> List[dvs.HostProductSpec]: ...
        @compatibleHostComponentProductInfo.setter
        def compatibleHostComponentProductInfo(self, value: List[dvs.HostProductSpec]):
            self._compatibleHostComponentProductInfo = value
        @property
        def featuresSupported(self) -> DistributedVirtualSwitch.FeatureCapability: ...
        @featuresSupported.setter
        def featuresSupported(self, value: DistributedVirtualSwitch.FeatureCapability):
            self._featuresSupported = value


    class ConfigInfo(vmodl.DynamicData):
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def numStandalonePorts(self) -> int: ...
        @numStandalonePorts.setter
        def numStandalonePorts(self, value: int):
            self._numStandalonePorts = value
        @property
        def numPorts(self) -> int: ...
        @numPorts.setter
        def numPorts(self, value: int):
            self._numPorts = value
        @property
        def maxPorts(self) -> int: ...
        @maxPorts.setter
        def maxPorts(self, value: int):
            self._maxPorts = value
        @property
        def uplinkPortPolicy(self) -> DistributedVirtualSwitch.UplinkPortPolicy: ...
        @uplinkPortPolicy.setter
        def uplinkPortPolicy(self, value: DistributedVirtualSwitch.UplinkPortPolicy):
            self._uplinkPortPolicy = value
        @property
        def uplinkPortgroup(self) -> List[dvs.DistributedVirtualPortgroup]: ...
        @uplinkPortgroup.setter
        def uplinkPortgroup(self, value: List[dvs.DistributedVirtualPortgroup]):
            self._uplinkPortgroup = value
        @property
        def defaultPortConfig(self) -> dvs.DistributedVirtualPort.Setting: ...
        @defaultPortConfig.setter
        def defaultPortConfig(self, value: dvs.DistributedVirtualPort.Setting):
            self._defaultPortConfig = value
        @property
        def host(self) -> List[dvs.HostMember]: ...
        @host.setter
        def host(self, value: List[dvs.HostMember]):
            self._host = value
        @property
        def productInfo(self) -> dvs.ProductSpec: ...
        @productInfo.setter
        def productInfo(self, value: dvs.ProductSpec):
            self._productInfo = value
        @property
        def targetInfo(self) -> dvs.ProductSpec: ...
        @targetInfo.setter
        def targetInfo(self, value: dvs.ProductSpec):
            self._targetInfo = value
        @property
        def extensionKey(self) -> str: ...
        @extensionKey.setter
        def extensionKey(self, value: str):
            self._extensionKey = value
        @property
        def vendorSpecificConfig(self) -> List[dvs.KeyedOpaqueBlob]: ...
        @vendorSpecificConfig.setter
        def vendorSpecificConfig(self, value: List[dvs.KeyedOpaqueBlob]):
            self._vendorSpecificConfig = value
        @property
        def policy(self) -> DistributedVirtualSwitch.SwitchPolicy: ...
        @policy.setter
        def policy(self, value: DistributedVirtualSwitch.SwitchPolicy):
            self._policy = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value
        @property
        def configVersion(self) -> str: ...
        @configVersion.setter
        def configVersion(self, value: str):
            self._configVersion = value
        @property
        def contact(self) -> DistributedVirtualSwitch.ContactInfo: ...
        @contact.setter
        def contact(self, value: DistributedVirtualSwitch.ContactInfo):
            self._contact = value
        @property
        def switchIpAddress(self) -> str: ...
        @switchIpAddress.setter
        def switchIpAddress(self, value: str):
            self._switchIpAddress = value
        @property
        def createTime(self) -> datetime: ...
        @createTime.setter
        def createTime(self, value: datetime):
            self._createTime = value
        @property
        def networkResourceManagementEnabled(self) -> bool: ...
        @networkResourceManagementEnabled.setter
        def networkResourceManagementEnabled(self, value: bool):
            self._networkResourceManagementEnabled = value
        @property
        def defaultProxySwitchMaxNumPorts(self) -> int: ...
        @defaultProxySwitchMaxNumPorts.setter
        def defaultProxySwitchMaxNumPorts(self, value: int):
            self._defaultProxySwitchMaxNumPorts = value
        @property
        def healthCheckConfig(self) -> List[DistributedVirtualSwitch.HealthCheckConfig]: ...
        @healthCheckConfig.setter
        def healthCheckConfig(self, value: List[DistributedVirtualSwitch.HealthCheckConfig]):
            self._healthCheckConfig = value
        @property
        def infrastructureTrafficResourceConfig(self) -> List[DistributedVirtualSwitch.HostInfrastructureTrafficResource]: ...
        @infrastructureTrafficResourceConfig.setter
        def infrastructureTrafficResourceConfig(self, value: List[DistributedVirtualSwitch.HostInfrastructureTrafficResource]):
            self._infrastructureTrafficResourceConfig = value
        @property
        def netResourcePoolTrafficResourceConfig(self) -> List[DistributedVirtualSwitch.HostInfrastructureTrafficResource]: ...
        @netResourcePoolTrafficResourceConfig.setter
        def netResourcePoolTrafficResourceConfig(self, value: List[DistributedVirtualSwitch.HostInfrastructureTrafficResource]):
            self._netResourcePoolTrafficResourceConfig = value
        @property
        def networkResourceControlVersion(self) -> str: ...
        @networkResourceControlVersion.setter
        def networkResourceControlVersion(self, value: str):
            self._networkResourceControlVersion = value
        @property
        def vmVnicNetworkResourcePool(self) -> List[dvs.VmVnicNetworkResourcePool]: ...
        @vmVnicNetworkResourcePool.setter
        def vmVnicNetworkResourcePool(self, value: List[dvs.VmVnicNetworkResourcePool]):
            self._vmVnicNetworkResourcePool = value
        @property
        def pnicCapacityRatioForReservation(self) -> int: ...
        @pnicCapacityRatioForReservation.setter
        def pnicCapacityRatioForReservation(self, value: int):
            self._pnicCapacityRatioForReservation = value


    class ConfigSpec(vmodl.DynamicData):
        @property
        def configVersion(self) -> str: ...
        @configVersion.setter
        def configVersion(self, value: str):
            self._configVersion = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def numStandalonePorts(self) -> int: ...
        @numStandalonePorts.setter
        def numStandalonePorts(self, value: int):
            self._numStandalonePorts = value
        @property
        def maxPorts(self) -> int: ...
        @maxPorts.setter
        def maxPorts(self, value: int):
            self._maxPorts = value
        @property
        def uplinkPortPolicy(self) -> DistributedVirtualSwitch.UplinkPortPolicy: ...
        @uplinkPortPolicy.setter
        def uplinkPortPolicy(self, value: DistributedVirtualSwitch.UplinkPortPolicy):
            self._uplinkPortPolicy = value
        @property
        def uplinkPortgroup(self) -> List[dvs.DistributedVirtualPortgroup]: ...
        @uplinkPortgroup.setter
        def uplinkPortgroup(self, value: List[dvs.DistributedVirtualPortgroup]):
            self._uplinkPortgroup = value
        @property
        def defaultPortConfig(self) -> dvs.DistributedVirtualPort.Setting: ...
        @defaultPortConfig.setter
        def defaultPortConfig(self, value: dvs.DistributedVirtualPort.Setting):
            self._defaultPortConfig = value
        @property
        def host(self) -> List[dvs.HostMember.ConfigSpec]: ...
        @host.setter
        def host(self, value: List[dvs.HostMember.ConfigSpec]):
            self._host = value
        @property
        def extensionKey(self) -> str: ...
        @extensionKey.setter
        def extensionKey(self, value: str):
            self._extensionKey = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value
        @property
        def policy(self) -> DistributedVirtualSwitch.SwitchPolicy: ...
        @policy.setter
        def policy(self, value: DistributedVirtualSwitch.SwitchPolicy):
            self._policy = value
        @property
        def vendorSpecificConfig(self) -> List[dvs.KeyedOpaqueBlob]: ...
        @vendorSpecificConfig.setter
        def vendorSpecificConfig(self, value: List[dvs.KeyedOpaqueBlob]):
            self._vendorSpecificConfig = value
        @property
        def contact(self) -> DistributedVirtualSwitch.ContactInfo: ...
        @contact.setter
        def contact(self, value: DistributedVirtualSwitch.ContactInfo):
            self._contact = value
        @property
        def switchIpAddress(self) -> str: ...
        @switchIpAddress.setter
        def switchIpAddress(self, value: str):
            self._switchIpAddress = value
        @property
        def defaultProxySwitchMaxNumPorts(self) -> int: ...
        @defaultProxySwitchMaxNumPorts.setter
        def defaultProxySwitchMaxNumPorts(self, value: int):
            self._defaultProxySwitchMaxNumPorts = value
        @property
        def infrastructureTrafficResourceConfig(self) -> List[DistributedVirtualSwitch.HostInfrastructureTrafficResource]: ...
        @infrastructureTrafficResourceConfig.setter
        def infrastructureTrafficResourceConfig(self, value: List[DistributedVirtualSwitch.HostInfrastructureTrafficResource]):
            self._infrastructureTrafficResourceConfig = value
        @property
        def netResourcePoolTrafficResourceConfig(self) -> List[DistributedVirtualSwitch.HostInfrastructureTrafficResource]: ...
        @netResourcePoolTrafficResourceConfig.setter
        def netResourcePoolTrafficResourceConfig(self, value: List[DistributedVirtualSwitch.HostInfrastructureTrafficResource]):
            self._netResourcePoolTrafficResourceConfig = value
        @property
        def networkResourceControlVersion(self) -> str: ...
        @networkResourceControlVersion.setter
        def networkResourceControlVersion(self, value: str):
            self._networkResourceControlVersion = value


    class ContactInfo(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def contact(self) -> str: ...
        @contact.setter
        def contact(self, value: str):
            self._contact = value


    class CreateSpec(vmodl.DynamicData):
        @property
        def configSpec(self) -> DistributedVirtualSwitch.ConfigSpec: ...
        @configSpec.setter
        def configSpec(self, value: DistributedVirtualSwitch.ConfigSpec):
            self._configSpec = value
        @property
        def productInfo(self) -> dvs.ProductSpec: ...
        @productInfo.setter
        def productInfo(self, value: dvs.ProductSpec):
            self._productInfo = value
        @property
        def capability(self) -> DistributedVirtualSwitch.Capability: ...
        @capability.setter
        def capability(self, value: DistributedVirtualSwitch.Capability):
            self._capability = value


    class FeatureCapability(vmodl.DynamicData):
        @property
        def networkResourceManagementSupported(self) -> bool: ...
        @networkResourceManagementSupported.setter
        def networkResourceManagementSupported(self, value: bool):
            self._networkResourceManagementSupported = value
        @property
        def vmDirectPathGen2Supported(self) -> bool: ...
        @vmDirectPathGen2Supported.setter
        def vmDirectPathGen2Supported(self, value: bool):
            self._vmDirectPathGen2Supported = value
        @property
        def nicTeamingPolicy(self) -> List[str]: ...
        @nicTeamingPolicy.setter
        def nicTeamingPolicy(self, value: List[str]):
            self._nicTeamingPolicy = value
        @property
        def networkResourcePoolHighShareValue(self) -> int: ...
        @networkResourcePoolHighShareValue.setter
        def networkResourcePoolHighShareValue(self, value: int):
            self._networkResourcePoolHighShareValue = value
        @property
        def networkResourceManagementCapability(self) -> DistributedVirtualSwitch.NetworkResourceManagementCapability: ...
        @networkResourceManagementCapability.setter
        def networkResourceManagementCapability(self, value: DistributedVirtualSwitch.NetworkResourceManagementCapability):
            self._networkResourceManagementCapability = value
        @property
        def healthCheckCapability(self) -> DistributedVirtualSwitch.HealthCheckFeatureCapability: ...
        @healthCheckCapability.setter
        def healthCheckCapability(self, value: DistributedVirtualSwitch.HealthCheckFeatureCapability):
            self._healthCheckCapability = value
        @property
        def rollbackCapability(self) -> DistributedVirtualSwitch.RollbackCapability: ...
        @rollbackCapability.setter
        def rollbackCapability(self, value: DistributedVirtualSwitch.RollbackCapability):
            self._rollbackCapability = value
        @property
        def backupRestoreCapability(self) -> DistributedVirtualSwitch.BackupRestoreCapability: ...
        @backupRestoreCapability.setter
        def backupRestoreCapability(self, value: DistributedVirtualSwitch.BackupRestoreCapability):
            self._backupRestoreCapability = value
        @property
        def networkFilterSupported(self) -> bool: ...
        @networkFilterSupported.setter
        def networkFilterSupported(self, value: bool):
            self._networkFilterSupported = value
        @property
        def macLearningSupported(self) -> bool: ...
        @macLearningSupported.setter
        def macLearningSupported(self, value: bool):
            self._macLearningSupported = value


    class HealthCheckConfig(vmodl.DynamicData):
        @property
        def enable(self) -> bool: ...
        @enable.setter
        def enable(self, value: bool):
            self._enable = value
        @property
        def interval(self) -> int: ...
        @interval.setter
        def interval(self, value: int):
            self._interval = value


    class HealthCheckFeatureCapability(vmodl.DynamicData): ...


    class HostInfrastructureTrafficResource(vmodl.DynamicData):
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
        def allocationInfo(self) -> DistributedVirtualSwitch.HostInfrastructureTrafficResource.ResourceAllocation: ...
        @allocationInfo.setter
        def allocationInfo(self, value: DistributedVirtualSwitch.HostInfrastructureTrafficResource.ResourceAllocation):
            self._allocationInfo = value


        class ResourceAllocation(vmodl.DynamicData):
            @property
            def limit(self) -> long: ...
            @limit.setter
            def limit(self, value: long):
                self._limit = value
            @property
            def shares(self) -> SharesInfo: ...
            @shares.setter
            def shares(self, value: SharesInfo):
                self._shares = value
            @property
            def reservation(self) -> long: ...
            @reservation.setter
            def reservation(self, value: long):
                self._reservation = value


    class NameArrayUplinkPortPolicy(DistributedVirtualSwitch.UplinkPortPolicy):
        @property
        def uplinkPortName(self) -> List[str]: ...
        @uplinkPortName.setter
        def uplinkPortName(self, value: List[str]):
            self._uplinkPortName = value


    class NetworkResourceManagementCapability(vmodl.DynamicData):
        @property
        def networkResourceManagementSupported(self) -> bool: ...
        @networkResourceManagementSupported.setter
        def networkResourceManagementSupported(self, value: bool):
            self._networkResourceManagementSupported = value
        @property
        def networkResourcePoolHighShareValue(self) -> int: ...
        @networkResourcePoolHighShareValue.setter
        def networkResourcePoolHighShareValue(self, value: int):
            self._networkResourcePoolHighShareValue = value
        @property
        def qosSupported(self) -> bool: ...
        @qosSupported.setter
        def qosSupported(self, value: bool):
            self._qosSupported = value
        @property
        def userDefinedNetworkResourcePoolsSupported(self) -> bool: ...
        @userDefinedNetworkResourcePoolsSupported.setter
        def userDefinedNetworkResourcePoolsSupported(self, value: bool):
            self._userDefinedNetworkResourcePoolsSupported = value
        @property
        def networkResourceControlVersion3Supported(self) -> bool: ...
        @networkResourceControlVersion3Supported.setter
        def networkResourceControlVersion3Supported(self, value: bool):
            self._networkResourceControlVersion3Supported = value
        @property
        def userDefinedInfraTrafficPoolSupported(self) -> bool: ...
        @userDefinedInfraTrafficPoolSupported.setter
        def userDefinedInfraTrafficPoolSupported(self, value: bool):
            self._userDefinedInfraTrafficPoolSupported = value


    class ResourceRuntimeInfo(vmodl.DynamicData):
        @property
        def capacity(self) -> int: ...
        @capacity.setter
        def capacity(self, value: int):
            self._capacity = value
        @property
        def usage(self) -> int: ...
        @usage.setter
        def usage(self, value: int):
            self._usage = value
        @property
        def available(self) -> int: ...
        @available.setter
        def available(self, value: int):
            self._available = value
        @property
        def allocatedResource(self) -> List[dvs.VmVnicNetworkResourcePool.VnicAllocatedResource]: ...
        @allocatedResource.setter
        def allocatedResource(self, value: List[dvs.VmVnicNetworkResourcePool.VnicAllocatedResource]):
            self._allocatedResource = value
        @property
        def vmVnicNetworkResourcePoolRuntime(self) -> List[dvs.VmVnicNetworkResourcePool.RuntimeInfo]: ...
        @vmVnicNetworkResourcePoolRuntime.setter
        def vmVnicNetworkResourcePoolRuntime(self, value: List[dvs.VmVnicNetworkResourcePool.RuntimeInfo]):
            self._vmVnicNetworkResourcePoolRuntime = value


    class RollbackCapability(vmodl.DynamicData):
        @property
        def rollbackSupported(self) -> bool: ...
        @rollbackSupported.setter
        def rollbackSupported(self, value: bool):
            self._rollbackSupported = value


    class RuntimeInfo(vmodl.DynamicData):
        @property
        def hostMemberRuntime(self) -> List[dvs.HostMember.RuntimeInfo]: ...
        @hostMemberRuntime.setter
        def hostMemberRuntime(self, value: List[dvs.HostMember.RuntimeInfo]):
            self._hostMemberRuntime = value
        @property
        def resourceRuntimeInfo(self) -> DistributedVirtualSwitch.ResourceRuntimeInfo: ...
        @resourceRuntimeInfo.setter
        def resourceRuntimeInfo(self, value: DistributedVirtualSwitch.ResourceRuntimeInfo):
            self._resourceRuntimeInfo = value


    class Summary(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def uuid(self) -> str: ...
        @uuid.setter
        def uuid(self, value: str):
            self._uuid = value
        @property
        def numPorts(self) -> int: ...
        @numPorts.setter
        def numPorts(self, value: int):
            self._numPorts = value
        @property
        def productInfo(self) -> dvs.ProductSpec: ...
        @productInfo.setter
        def productInfo(self, value: dvs.ProductSpec):
            self._productInfo = value
        @property
        def hostMember(self) -> List[HostSystem]: ...
        @hostMember.setter
        def hostMember(self, value: List[HostSystem]):
            self._hostMember = value
        @property
        def vm(self) -> List[VirtualMachine]: ...
        @vm.setter
        def vm(self, value: List[VirtualMachine]):
            self._vm = value
        @property
        def host(self) -> List[HostSystem]: ...
        @host.setter
        def host(self, value: List[HostSystem]):
            self._host = value
        @property
        def portgroupName(self) -> List[str]: ...
        @portgroupName.setter
        def portgroupName(self, value: List[str]):
            self._portgroupName = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value
        @property
        def contact(self) -> DistributedVirtualSwitch.ContactInfo: ...
        @contact.setter
        def contact(self, value: DistributedVirtualSwitch.ContactInfo):
            self._contact = value
        @property
        def numHosts(self) -> int: ...
        @numHosts.setter
        def numHosts(self, value: int):
            self._numHosts = value


    class SwitchPolicy(vmodl.DynamicData):
        @property
        def autoPreInstallAllowed(self) -> bool: ...
        @autoPreInstallAllowed.setter
        def autoPreInstallAllowed(self, value: bool):
            self._autoPreInstallAllowed = value
        @property
        def autoUpgradeAllowed(self) -> bool: ...
        @autoUpgradeAllowed.setter
        def autoUpgradeAllowed(self, value: bool):
            self._autoUpgradeAllowed = value
        @property
        def partialUpgradeAllowed(self) -> bool: ...
        @partialUpgradeAllowed.setter
        def partialUpgradeAllowed(self, value: bool):
            self._partialUpgradeAllowed = value


    class UplinkPortPolicy(vmodl.DynamicData): ...


    class HostInfrastructureTrafficClass(Enum):
        management = "management"
        faultTolerance = "faultTolerance"
        vmotion = "vmotion"
        virtualMachine = "virtualMachine"
        iSCSI = "iSCSI"
        nfs = "nfs"
        hbr = "hbr"
        vsan = "vsan"
        vdp = "vdp"
        backupNfc = "backupNfc"
        nvmetcp = "nvmetcp"


    class NetworkResourceControlVersion(Enum):
        version2 = "version2"
        version3 = "version3"


    class NicTeamingPolicyMode(Enum):
        loadbalance_ip = "loadbalance_ip"
        loadbalance_srcmac = "loadbalance_srcmac"
        loadbalance_srcid = "loadbalance_srcid"
        failover_explicit = "failover_explicit"
        loadbalance_loadbased = "loadbalance_loadbased"


    class ProductSpecOperationType(Enum):
        preInstall = "preInstall"
        upgrade = "upgrade"
        notifyAvailableUpgrade = "notifyAvailableUpgrade"
        proceedWithUpgrade = "proceedWithUpgrade"
        updateBundleInfo = "updateBundleInfo"


class EnvironmentBrowser(ManagedObject):
    @property
    def datastoreBrowser(self) -> host.DatastoreBrowser: ...
    def QueryConfigOptionDescriptor(self) -> List[vm.ConfigOptionDescriptor]: ...
    def QueryConfigOption(self, key: str, host: HostSystem) -> vm.ConfigOption: ...
    def QueryConfigOptionEx(self, spec: EnvironmentBrowser.ConfigOptionQuerySpec) -> vm.ConfigOption: ...
    def QueryConfigTarget(self, host: HostSystem) -> vm.ConfigTarget: ...
    def QueryTargetCapabilities(self, host: HostSystem) -> host.Capability: ...


    class ConfigOptionQuerySpec(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def host(self) -> HostSystem: ...
        @host.setter
        def host(self, value: HostSystem):
            self._host = value
        @property
        def guestId(self) -> List[str]: ...
        @guestId.setter
        def guestId(self, value: List[str]):
            self._guestId = value


class ExtensibleManagedObject(ManagedObject):
    @property
    def value(self) -> List[CustomFieldsManager.Value]: ...
    @property
    def availableField(self) -> List[CustomFieldsManager.FieldDef]: ...
    def SetCustomValue(self, key: str, value: str) -> NoneType: ...


class ExtensionManager(ManagedObject):
    @property
    def extensionList(self) -> List[Extension]: ...
    def UnregisterExtension(self, extensionKey: str) -> NoneType: ...
    def FindExtension(self, extensionKey: str) -> Extension: ...
    def RegisterExtension(self, extension: Extension) -> NoneType: ...
    def UpdateExtension(self, extension: Extension) -> NoneType: ...
    def GetPublicKey(self) -> str: ...
    def SetPublicKey(self, extensionKey: str, publicKey: str) -> NoneType: ...
    def SetCertificate(self, extensionKey: str, certificatePem: str) -> NoneType: ...
    def QueryManagedBy(self, extensionKey: str) -> List[ManagedEntity]: ...
    def QueryExtensionIpAllocationUsage(self, extensionKeys: List[str]) -> List[ExtensionManager.IpAllocationUsage]: ...


    class IpAllocationUsage(vmodl.DynamicData):
        @property
        def extensionKey(self) -> str: ...
        @extensionKey.setter
        def extensionKey(self, value: str):
            self._extensionKey = value
        @property
        def numAddresses(self) -> int: ...
        @numAddresses.setter
        def numAddresses(self, value: int):
            self._numAddresses = value


class FileManager(ManagedObject):
    def MoveFile(self, sourceName: str, sourceDatacenter: Datacenter, destinationName: str, destinationDatacenter: Datacenter, force: bool) -> Task: ...
    def CopyFile(self, sourceName: str, sourceDatacenter: Datacenter, destinationName: str, destinationDatacenter: Datacenter, force: bool) -> Task: ...
    def DeleteFile(self, name: str, datacenter: Datacenter) -> Task: ...
    def MakeDirectory(self, name: str, datacenter: Datacenter, createParentDirectories: bool) -> NoneType: ...
    def ChangeOwner(self, name: str, datacenter: Datacenter, owner: str) -> NoneType: ...


class Folder(ManagedEntity):
    @property
    def childType(self) -> List[type]: ...
    @property
    def childEntity(self) -> List[ManagedEntity]: ...
    @property
    def namespace(self) -> str: ...
    def CreateFolder(self, name: str) -> Folder: ...
    def MoveInto(self, list: List[ManagedEntity]) -> Task: ...
    def CreateVm(self, config: vm.ConfigSpec, pool: ResourcePool, host: HostSystem) -> Task: ...
    def RegisterVm(self, path: str, name: str, asTemplate: bool, pool: ResourcePool, host: HostSystem) -> Task: ...
    def CreateCluster(self, name: str, spec: cluster.ConfigSpec) -> ClusterComputeResource: ...
    def CreateClusterEx(self, name: str, spec: cluster.ConfigSpecEx) -> ClusterComputeResource: ...
    def AddStandaloneHost(self, spec: host.ConnectSpec, compResSpec: ComputeResource.ConfigSpec, addConnected: bool, license: str) -> Task: ...
    def CreateDatacenter(self, name: str) -> Datacenter: ...
    def UnregisterAndDestroy(self) -> Task: ...
    def CreateDistributedVirtualSwitch(self, spec: DistributedVirtualSwitch.CreateSpec) -> Task: ...
    def CreateStoragePod(self, name: str) -> StoragePod: ...
    def BatchAddStandaloneHosts(self, newHosts: List[Folder.NewHostSpec], compResSpec: ComputeResource.ConfigSpec, addConnected: bool) -> Task: ...
    def BatchAddHostsToCluster(self, cluster: ClusterComputeResource, newHosts: List[Folder.NewHostSpec], existingHosts: List[HostSystem], compResSpec: ComputeResource.ConfigSpec, desiredState: str) -> Task: ...


    class BatchAddHostsToClusterResult(vmodl.DynamicData):
        @property
        def hostsAddedToCluster(self) -> List[HostSystem]: ...
        @hostsAddedToCluster.setter
        def hostsAddedToCluster(self, value: List[HostSystem]):
            self._hostsAddedToCluster = value
        @property
        def hostsFailedInventoryAdd(self) -> List[Folder.FailedHostResult]: ...
        @hostsFailedInventoryAdd.setter
        def hostsFailedInventoryAdd(self, value: List[Folder.FailedHostResult]):
            self._hostsFailedInventoryAdd = value
        @property
        def hostsFailedMoveToCluster(self) -> List[Folder.FailedHostResult]: ...
        @hostsFailedMoveToCluster.setter
        def hostsFailedMoveToCluster(self, value: List[Folder.FailedHostResult]):
            self._hostsFailedMoveToCluster = value


    class BatchAddStandaloneHostsResult(vmodl.DynamicData):
        @property
        def addedHosts(self) -> List[HostSystem]: ...
        @addedHosts.setter
        def addedHosts(self, value: List[HostSystem]):
            self._addedHosts = value
        @property
        def hostsFailedInventoryAdd(self) -> List[Folder.FailedHostResult]: ...
        @hostsFailedInventoryAdd.setter
        def hostsFailedInventoryAdd(self, value: List[Folder.FailedHostResult]):
            self._hostsFailedInventoryAdd = value


    class FailedHostResult(vmodl.DynamicData):
        @property
        def hostName(self) -> str: ...
        @hostName.setter
        def hostName(self, value: str):
            self._hostName = value
        @property
        def host(self) -> HostSystem: ...
        @host.setter
        def host(self, value: HostSystem):
            self._host = value
        @property
        def context(self) -> vmodl.LocalizableMessage: ...
        @context.setter
        def context(self, value: vmodl.LocalizableMessage):
            self._context = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


    class NewHostSpec(vmodl.DynamicData):
        @property
        def hostCnxSpec(self) -> host.ConnectSpec: ...
        @hostCnxSpec.setter
        def hostCnxSpec(self, value: host.ConnectSpec):
            self._hostCnxSpec = value
        @property
        def esxLicense(self) -> str: ...
        @esxLicense.setter
        def esxLicense(self, value: str):
            self._esxLicense = value


    class DesiredHostState(Enum):
        maintenance = "maintenance"
        non_maintenance = "non_maintenance"


class HealthUpdateManager(ManagedObject):
    def RegisterProvider(self, name: str, healthUpdateInfo: List[HealthUpdateInfo]) -> str: ...
    def UnregisterProvider(self, providerId: str) -> NoneType: ...
    def QueryProviderList(self) -> List[str]: ...
    def HasProvider(self, id: str) -> bool: ...
    def QueryProviderName(self, id: str) -> str: ...
    def QueryHealthUpdateInfos(self, providerId: str) -> List[HealthUpdateInfo]: ...
    def AddMonitoredEntities(self, providerId: str, entities: List[ManagedEntity]) -> NoneType: ...
    def RemoveMonitoredEntities(self, providerId: str, entities: List[ManagedEntity]) -> NoneType: ...
    def QueryMonitoredEntities(self, providerId: str) -> List[ManagedEntity]: ...
    def HasMonitoredEntity(self, providerId: str, entity: ManagedEntity) -> bool: ...
    def QueryUnmonitoredHosts(self, providerId: str, cluster: ClusterComputeResource) -> List[HostSystem]: ...
    def PostHealthUpdates(self, providerId: str, updates: List[HealthUpdate]) -> NoneType: ...
    def QueryHealthUpdates(self, providerId: str) -> List[HealthUpdate]: ...
    def AddFilter(self, providerId: str, filterName: str, infoIds: List[str]) -> str: ...
    def QueryFilterList(self, providerId: str) -> List[str]: ...
    def QueryFilterName(self, filterId: str) -> str: ...
    def QueryFilterInfoIds(self, filterId: str) -> List[str]: ...
    def QueryFilterEntities(self, filterId: str) -> List[ManagedEntity]: ...
    def AddFilterEntities(self, filterId: str, entities: List[ManagedEntity]) -> NoneType: ...
    def RemoveFilterEntities(self, filterId: str, entities: List[ManagedEntity]) -> NoneType: ...
    def RemoveFilter(self, filterId: str) -> NoneType: ...


class HistoryCollector(ManagedObject):
    @property
    def filter(self) -> object: ...
    def SetLatestPageSize(self, maxCount: int) -> NoneType: ...
    def Rewind(self) -> NoneType: ...
    def Reset(self) -> NoneType: ...
    def Remove(self) -> NoneType: ...


class HostSystem(ManagedEntity):
    @property
    def runtime(self) -> host.RuntimeInfo: ...
    @property
    def summary(self) -> host.Summary: ...
    @property
    def hardware(self) -> host.HardwareInfo: ...
    @property
    def capability(self) -> host.Capability: ...
    @property
    def licensableResource(self) -> LicenseManager.LicensableResourceInfo: ...
    @property
    def remediationState(self) -> HostSystem.RemediationState: ...
    @property
    def precheckRemediationResult(self) -> profile.host.ProfileManager.ApplyHostConfigSpec: ...
    @property
    def remediationResult(self) -> profile.host.ProfileManager.ApplyHostConfigResult: ...
    @property
    def complianceCheckState(self) -> HostSystem.ComplianceCheckState: ...
    @property
    def complianceCheckResult(self) -> profile.ComplianceResult: ...
    @property
    def configManager(self) -> host.ConfigManager: ...
    @property
    def config(self) -> host.ConfigInfo: ...
    @property
    def vm(self) -> List[VirtualMachine]: ...
    @property
    def datastore(self) -> List[Datastore]: ...
    @property
    def network(self) -> List[Network]: ...
    @property
    def datastoreBrowser(self) -> host.DatastoreBrowser: ...
    @property
    def systemResources(self) -> host.SystemResourceInfo: ...
    @property
    def answerFileValidationState(self) -> profile.host.AnswerFileStatusResult: ...
    @property
    def answerFileValidationResult(self) -> profile.host.AnswerFileStatusResult: ...
    def QueryTpmAttestationReport(self) -> host.TpmAttestationReport: ...
    def QueryConnectionInfo(self) -> host.ConnectInfo: ...
    def UpdateSystemResources(self, resourceInfo: host.SystemResourceInfo) -> NoneType: ...
    def UpdateSystemSwapConfiguration(self, sysSwapConfig: host.SystemSwapConfiguration) -> NoneType: ...
    def Reconnect(self, cnxSpec: host.ConnectSpec, reconnectSpec: HostSystem.ReconnectSpec) -> Task: ...
    def Disconnect(self) -> Task: ...
    def EnterMaintenanceMode(self, timeout: int, evacuatePoweredOffVms: bool, maintenanceSpec: host.MaintenanceSpec) -> Task: ...
    def ExitMaintenanceMode(self, timeout: int) -> Task: ...
    def Reboot(self, force: bool) -> Task: ...
    def Shutdown(self, force: bool) -> Task: ...
    def EnterStandbyMode(self, timeoutSec: int, evacuatePoweredOffVms: bool) -> Task: ...
    def ExitStandbyMode(self, timeoutSec: int) -> Task: ...
    def QueryOverhead(self, memorySize: long, videoRamSize: int, numVcpus: int) -> long: ...
    def QueryOverheadEx(self, vmConfigInfo: vm.ConfigInfo) -> long: ...
    def ReconfigureDAS(self) -> Task: ...
    def UpdateFlags(self, flagInfo: host.FlagInfo) -> NoneType: ...
    def EnterLockdownMode(self) -> NoneType: ...
    def ExitLockdownMode(self) -> NoneType: ...
    def AcquireCimServicesTicket(self) -> HostServiceTicket: ...
    def UpdateIpmi(self, ipmiInfo: host.IpmiInfo) -> NoneType: ...
    def RetrieveHardwareUptime(self) -> long: ...
    def PrepareCrypto(self) -> NoneType: ...
    def EnableCrypto(self, keyPlain: encryption.CryptoKeyPlain) -> NoneType: ...
    def ConfigureCryptoKey(self, keyId: encryption.CryptoKeyId) -> NoneType: ...
    def QueryProductLockerLocation(self) -> str: ...
    def UpdateProductLockerLocation(self, path: str) -> Task: ...
    def RetrieveFreeEpcMemory(self) -> long: ...


    class ComplianceCheckState(vmodl.DynamicData):
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value
        @property
        def checkTime(self) -> datetime: ...
        @checkTime.setter
        def checkTime(self, value: datetime):
            self._checkTime = value


    class ReconnectSpec(vmodl.DynamicData):
        @property
        def syncState(self) -> bool: ...
        @syncState.setter
        def syncState(self, value: bool):
            self._syncState = value


    class RemediationState(vmodl.DynamicData):
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value
        @property
        def operationTime(self) -> datetime: ...
        @operationTime.setter
        def operationTime(self, value: datetime):
            self._operationTime = value


    class ConnectionState(Enum):
        connected = "connected"
        notResponding = "notResponding"
        disconnected = "disconnected"


    class CryptoState(Enum):
        incapable = "incapable"
        prepared = "prepared"
        safe = "safe"
        pendingIncapable = "pendingIncapable"


    class PowerState(Enum):
        poweredOn = "poweredOn"
        poweredOff = "poweredOff"
        standBy = "standBy"
        unknown = "unknown"


    class StandbyMode(Enum):
        entering = "entering"
        exiting = "exiting"
        # "in" is available at runtime but excluded from the type hints to pass static code checks.
        # in = "in"
        none = "none"


class HttpNfcLease(ManagedObject):
    @property
    def initializeProgress(self) -> int: ...
    @property
    def transferProgress(self) -> int: ...
    @property
    def mode(self) -> str: ...
    @property
    def capabilities(self) -> HttpNfcLease.Capabilities: ...
    @property
    def info(self) -> HttpNfcLease.Info: ...
    @property
    def state(self) -> HttpNfcLease.State | Literal['initializing', 'ready', 'done', 'error']: ...
    @property
    def error(self) -> vmodl.MethodFault: ...
    def GetManifest(self) -> List[HttpNfcLease.ManifestEntry]: ...
    def SetManifestChecksumType(self, deviceUrlsToChecksumTypes: List[KeyValue]) -> NoneType: ...
    def Complete(self) -> NoneType: ...
    def Abort(self, fault: vmodl.MethodFault) -> NoneType: ...
    def Progress(self, percent: int) -> NoneType: ...
    def PullFromUrls(self, files: List[HttpNfcLease.SourceFile]) -> Task: ...
    def ProbeUrls(self, files: List[HttpNfcLease.SourceFile], timeout: int) -> List[HttpNfcLease.ProbeResult]: ...


    class Capabilities(vmodl.DynamicData):
        @property
        def pullModeSupported(self) -> bool: ...
        @pullModeSupported.setter
        def pullModeSupported(self, value: bool):
            self._pullModeSupported = value
        @property
        def corsSupported(self) -> bool: ...
        @corsSupported.setter
        def corsSupported(self, value: bool):
            self._corsSupported = value


    class DatastoreLeaseInfo(vmodl.DynamicData):
        @property
        def datastoreKey(self) -> str: ...
        @datastoreKey.setter
        def datastoreKey(self, value: str):
            self._datastoreKey = value
        @property
        def hosts(self) -> List[HttpNfcLease.HostInfo]: ...
        @hosts.setter
        def hosts(self, value: List[HttpNfcLease.HostInfo]):
            self._hosts = value


    class DeviceUrl(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def importKey(self) -> str: ...
        @importKey.setter
        def importKey(self, value: str):
            self._importKey = value
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value
        @property
        def sslThumbprint(self) -> str: ...
        @sslThumbprint.setter
        def sslThumbprint(self, value: str):
            self._sslThumbprint = value
        @property
        def disk(self) -> bool: ...
        @disk.setter
        def disk(self, value: bool):
            self._disk = value
        @property
        def targetId(self) -> str: ...
        @targetId.setter
        def targetId(self, value: str):
            self._targetId = value
        @property
        def datastoreKey(self) -> str: ...
        @datastoreKey.setter
        def datastoreKey(self, value: str):
            self._datastoreKey = value
        @property
        def fileSize(self) -> long: ...
        @fileSize.setter
        def fileSize(self, value: long):
            self._fileSize = value


    class HostInfo(vmodl.DynamicData):
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value
        @property
        def sslThumbprint(self) -> str: ...
        @sslThumbprint.setter
        def sslThumbprint(self, value: str):
            self._sslThumbprint = value


    class Info(vmodl.DynamicData):
        @property
        def lease(self) -> HttpNfcLease: ...
        @lease.setter
        def lease(self, value: HttpNfcLease):
            self._lease = value
        @property
        def entity(self) -> ManagedEntity: ...
        @entity.setter
        def entity(self, value: ManagedEntity):
            self._entity = value
        @property
        def deviceUrl(self) -> List[HttpNfcLease.DeviceUrl]: ...
        @deviceUrl.setter
        def deviceUrl(self, value: List[HttpNfcLease.DeviceUrl]):
            self._deviceUrl = value
        @property
        def totalDiskCapacityInKB(self) -> long: ...
        @totalDiskCapacityInKB.setter
        def totalDiskCapacityInKB(self, value: long):
            self._totalDiskCapacityInKB = value
        @property
        def leaseTimeout(self) -> int: ...
        @leaseTimeout.setter
        def leaseTimeout(self, value: int):
            self._leaseTimeout = value
        @property
        def hostMap(self) -> List[HttpNfcLease.DatastoreLeaseInfo]: ...
        @hostMap.setter
        def hostMap(self, value: List[HttpNfcLease.DatastoreLeaseInfo]):
            self._hostMap = value


    class ManifestEntry(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def sha1(self) -> str: ...
        @sha1.setter
        def sha1(self, value: str):
            self._sha1 = value
        @property
        def checksum(self) -> str: ...
        @checksum.setter
        def checksum(self, value: str):
            self._checksum = value
        @property
        def checksumType(self) -> str: ...
        @checksumType.setter
        def checksumType(self, value: str):
            self._checksumType = value
        @property
        def size(self) -> long: ...
        @size.setter
        def size(self, value: long):
            self._size = value
        @property
        def disk(self) -> bool: ...
        @disk.setter
        def disk(self, value: bool):
            self._disk = value
        @property
        def capacity(self) -> long: ...
        @capacity.setter
        def capacity(self, value: long):
            self._capacity = value
        @property
        def populatedSize(self) -> long: ...
        @populatedSize.setter
        def populatedSize(self, value: long):
            self._populatedSize = value


        class ChecksumType(Enum):
            sha1 = "sha1"
            sha256 = "sha256"


    class ProbeResult(vmodl.DynamicData):
        @property
        def serverAccessible(self) -> bool: ...
        @serverAccessible.setter
        def serverAccessible(self, value: bool):
            self._serverAccessible = value


    class SourceFile(vmodl.DynamicData):
        @property
        def targetDeviceId(self) -> str: ...
        @targetDeviceId.setter
        def targetDeviceId(self, value: str):
            self._targetDeviceId = value
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value
        @property
        def memberName(self) -> str: ...
        @memberName.setter
        def memberName(self, value: str):
            self._memberName = value
        @property
        def create(self) -> bool: ...
        @create.setter
        def create(self, value: bool):
            self._create = value
        @property
        def sslThumbprint(self) -> str: ...
        @sslThumbprint.setter
        def sslThumbprint(self, value: str):
            self._sslThumbprint = value
        @property
        def httpHeaders(self) -> List[KeyValue]: ...
        @httpHeaders.setter
        def httpHeaders(self, value: List[KeyValue]):
            self._httpHeaders = value
        @property
        def size(self) -> long: ...
        @size.setter
        def size(self, value: long):
            self._size = value


    class Mode(Enum):
        pushOrGet = "pushOrGet"
        pull = "pull"


class IoFilterManager(ManagedObject):
    def InstallIoFilter(self, vibUrl: str, compRes: ComputeResource) -> Task: ...
    def UninstallIoFilter(self, filterId: str, compRes: ComputeResource) -> Task: ...
    def UpgradeIoFilter(self, filterId: str, compRes: ComputeResource, vibUrl: str) -> Task: ...
    def QueryIssue(self, filterId: str, compRes: ComputeResource) -> IoFilterManager.QueryIssueResult: ...
    def QueryIoFilterInfo(self, compRes: ComputeResource) -> List[IoFilterManager.ClusterIoFilterInfo]: ...
    def ResolveInstallationErrorsOnHost(self, filterId: str, host: HostSystem) -> Task: ...
    def ResolveInstallationErrorsOnCluster(self, filterId: str, cluster: ClusterComputeResource) -> Task: ...
    def QueryDisksUsingFilter(self, filterId: str, compRes: ComputeResource) -> List[vm.device.VirtualDiskId]: ...


    class ClusterIoFilterInfo(IoFilterManager.IoFilterInfo):
        @property
        def opType(self) -> str: ...
        @opType.setter
        def opType(self, value: str):
            self._opType = value
        @property
        def vibUrl(self) -> str: ...
        @vibUrl.setter
        def vibUrl(self, value: str):
            self._vibUrl = value


    class HostIoFilterInfo(IoFilterManager.IoFilterInfo):
        @property
        def available(self) -> bool: ...
        @available.setter
        def available(self, value: bool):
            self._available = value


    class IoFilterInfo(vmodl.DynamicData):
        @property
        def id(self) -> str: ...
        @id.setter
        def id(self, value: str):
            self._id = value
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
        def summary(self) -> str: ...
        @summary.setter
        def summary(self, value: str):
            self._summary = value
        @property
        def releaseDate(self) -> str: ...
        @releaseDate.setter
        def releaseDate(self, value: str):
            self._releaseDate = value


    class QueryIssueResult(vmodl.DynamicData):
        @property
        def opType(self) -> str: ...
        @opType.setter
        def opType(self, value: str):
            self._opType = value
        @property
        def hostIssue(self) -> List[IoFilterManager.QueryIssueResult.HostIssue]: ...
        @hostIssue.setter
        def hostIssue(self, value: List[IoFilterManager.QueryIssueResult.HostIssue]):
            self._hostIssue = value


        class HostIssue(vmodl.DynamicData):
            @property
            def host(self) -> HostSystem: ...
            @host.setter
            def host(self, value: HostSystem):
                self._host = value
            @property
            def issue(self) -> List[vmodl.MethodFault]: ...
            @issue.setter
            def issue(self, value: List[vmodl.MethodFault]):
                self._issue = value


    class IoFilterType(Enum):
        cache = "cache"
        replication = "replication"
        encryption = "encryption"
        compression = "compression"
        inspection = "inspection"
        datastoreIoControl = "datastoreIoControl"
        dataProvider = "dataProvider"
        dataCapture = "dataCapture"


    class OperationType(Enum):
        install = "install"
        uninstall = "uninstall"
        upgrade = "upgrade"


class IpPoolManager(ManagedObject):
    def QueryIpPools(self, dc: Datacenter) -> List[vApp.IpPool]: ...
    def CreateIpPool(self, dc: Datacenter, pool: vApp.IpPool) -> int: ...
    def UpdateIpPool(self, dc: Datacenter, pool: vApp.IpPool) -> NoneType: ...
    def DestroyIpPool(self, dc: Datacenter, id: int, force: bool) -> NoneType: ...
    def AllocateIpv4Address(self, dc: Datacenter, poolId: int, allocationId: str) -> str: ...
    def AllocateIpv6Address(self, dc: Datacenter, poolId: int, allocationId: str) -> str: ...
    def ReleaseIpAllocation(self, dc: Datacenter, poolId: int, allocationId: str) -> NoneType: ...
    def QueryIPAllocations(self, dc: Datacenter, poolId: int, extensionKey: str) -> List[IpPoolManager.IpAllocation]: ...


    class IpAllocation(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @ipAddress.setter
        def ipAddress(self, value: str):
            self._ipAddress = value
        @property
        def allocationId(self) -> str: ...
        @allocationId.setter
        def allocationId(self, value: str):
            self._allocationId = value


class LicenseAssignmentManager(ManagedObject):
    def UpdateAssignedLicense(self, entity: str, licenseKey: str, entityDisplayName: str) -> LicenseManager.LicenseInfo: ...
    def RemoveAssignedLicense(self, entityId: str) -> NoneType: ...
    def QueryAssignedLicenses(self, entityId: str) -> List[LicenseAssignmentManager.LicenseAssignment]: ...


    class LicenseAssignment(vmodl.DynamicData):
        @property
        def entityId(self) -> str: ...
        @entityId.setter
        def entityId(self, value: str):
            self._entityId = value
        @property
        def scope(self) -> str: ...
        @scope.setter
        def scope(self, value: str):
            self._scope = value
        @property
        def entityDisplayName(self) -> str: ...
        @entityDisplayName.setter
        def entityDisplayName(self, value: str):
            self._entityDisplayName = value
        @property
        def assignedLicense(self) -> LicenseManager.LicenseInfo: ...
        @assignedLicense.setter
        def assignedLicense(self, value: LicenseManager.LicenseInfo):
            self._assignedLicense = value
        @property
        def properties(self) -> List[vmodl.KeyAnyValue]: ...
        @properties.setter
        def properties(self, value: List[vmodl.KeyAnyValue]):
            self._properties = value


class LicenseManager(ManagedObject):
    @property
    def source(self) -> LicenseManager.LicenseSource: ...
    @property
    def sourceAvailable(self) -> bool: ...
    @property
    def diagnostics(self) -> LicenseManager.DiagnosticInfo: ...
    @property
    def featureInfo(self) -> List[LicenseManager.FeatureInfo]: ...
    @property
    def licensedEdition(self) -> str: ...
    @property
    def licenses(self) -> List[LicenseManager.LicenseInfo]: ...
    @property
    def licenseAssignmentManager(self) -> LicenseAssignmentManager: ...
    @property
    def evaluation(self) -> LicenseManager.EvaluationInfo: ...
    def QuerySupportedFeatures(self, host: HostSystem) -> List[LicenseManager.FeatureInfo]: ...
    def QuerySourceAvailability(self, host: HostSystem) -> List[LicenseManager.AvailabilityInfo]: ...
    def QueryUsage(self, host: HostSystem) -> LicenseManager.LicenseUsageInfo: ...
    def SetEdition(self, host: HostSystem, featureKey: str) -> NoneType: ...
    def CheckFeature(self, host: HostSystem, featureKey: str) -> bool: ...
    def Enable(self, host: HostSystem, featureKey: str) -> bool: ...
    def Disable(self, host: HostSystem, featureKey: str) -> bool: ...
    def ConfigureSource(self, host: HostSystem, licenseSource: LicenseManager.LicenseSource) -> NoneType: ...
    def UpdateLicense(self, licenseKey: str, labels: List[KeyValue]) -> LicenseManager.LicenseInfo: ...
    def AddLicense(self, licenseKey: str, labels: List[KeyValue]) -> LicenseManager.LicenseInfo: ...
    def RemoveLicense(self, licenseKey: str) -> NoneType: ...
    def DecodeLicense(self, licenseKey: str) -> LicenseManager.LicenseInfo: ...
    def UpdateLabel(self, licenseKey: str, labelKey: str, labelValue: str) -> NoneType: ...
    def RemoveLabel(self, licenseKey: str, labelKey: str) -> NoneType: ...


    class AvailabilityInfo(vmodl.DynamicData):
        @property
        def feature(self) -> LicenseManager.FeatureInfo: ...
        @feature.setter
        def feature(self, value: LicenseManager.FeatureInfo):
            self._feature = value
        @property
        def total(self) -> int: ...
        @total.setter
        def total(self, value: int):
            self._total = value
        @property
        def available(self) -> int: ...
        @available.setter
        def available(self, value: int):
            self._available = value


    class DiagnosticInfo(vmodl.DynamicData):
        @property
        def sourceLastChanged(self) -> datetime: ...
        @sourceLastChanged.setter
        def sourceLastChanged(self, value: datetime):
            self._sourceLastChanged = value
        @property
        def sourceLost(self) -> str: ...
        @sourceLost.setter
        def sourceLost(self, value: str):
            self._sourceLost = value
        @property
        def sourceLatency(self) -> float: ...
        @sourceLatency.setter
        def sourceLatency(self, value: float):
            self._sourceLatency = value
        @property
        def licenseRequests(self) -> str: ...
        @licenseRequests.setter
        def licenseRequests(self, value: str):
            self._licenseRequests = value
        @property
        def licenseRequestFailures(self) -> str: ...
        @licenseRequestFailures.setter
        def licenseRequestFailures(self, value: str):
            self._licenseRequestFailures = value
        @property
        def licenseFeatureUnknowns(self) -> str: ...
        @licenseFeatureUnknowns.setter
        def licenseFeatureUnknowns(self, value: str):
            self._licenseFeatureUnknowns = value
        @property
        def opState(self) -> LicenseManager.LicenseState | Literal['initializing', 'normal', 'marginal', 'fault']: ...
        @opState.setter
        def opState(self, value: LicenseManager.LicenseState | Literal['initializing', 'normal', 'marginal', 'fault']):
            self._opState = value
        @property
        def lastStatusUpdate(self) -> datetime: ...
        @lastStatusUpdate.setter
        def lastStatusUpdate(self, value: datetime):
            self._lastStatusUpdate = value
        @property
        def opFailureMessage(self) -> str: ...
        @opFailureMessage.setter
        def opFailureMessage(self, value: str):
            self._opFailureMessage = value


    class EvaluationInfo(vmodl.DynamicData):
        @property
        def properties(self) -> List[vmodl.KeyAnyValue]: ...
        @properties.setter
        def properties(self, value: List[vmodl.KeyAnyValue]):
            self._properties = value


    class EvaluationLicense(LicenseManager.LicenseSource):
        @property
        def remainingHours(self) -> long: ...
        @remainingHours.setter
        def remainingHours(self, value: long):
            self._remainingHours = value


    class FeatureInfo(vmodl.DynamicData):
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
        def featureDescription(self) -> str: ...
        @featureDescription.setter
        def featureDescription(self, value: str):
            self._featureDescription = value
        @property
        def state(self) -> LicenseManager.FeatureInfo.State | Literal['enabled', 'disabled', 'optional']: ...
        @state.setter
        def state(self, value: LicenseManager.FeatureInfo.State | Literal['enabled', 'disabled', 'optional']):
            self._state = value
        @property
        def costUnit(self) -> str: ...
        @costUnit.setter
        def costUnit(self, value: str):
            self._costUnit = value
        @property
        def sourceRestriction(self) -> str: ...
        @sourceRestriction.setter
        def sourceRestriction(self, value: str):
            self._sourceRestriction = value
        @property
        def dependentKey(self) -> List[str]: ...
        @dependentKey.setter
        def dependentKey(self, value: List[str]):
            self._dependentKey = value
        @property
        def edition(self) -> bool: ...
        @edition.setter
        def edition(self, value: bool):
            self._edition = value
        @property
        def expiresOn(self) -> datetime: ...
        @expiresOn.setter
        def expiresOn(self, value: datetime):
            self._expiresOn = value


        class CostUnit(Enum):
            host = "host"
            cpuCore = "cpuCore"
            cpuPackage = "cpuPackage"
            server = "server"
            vm = "vm"


        class SourceRestriction(Enum):
            unrestricted = "unrestricted"
            served = "served"
            file = "file"


    class LicensableResourceInfo(vmodl.DynamicData):
        @property
        def resource(self) -> List[vmodl.KeyAnyValue]: ...
        @resource.setter
        def resource(self, value: List[vmodl.KeyAnyValue]):
            self._resource = value


        class ResourceKey(Enum):
            numCpuPackages = "numCpuPackages"
            numCpuCores = "numCpuCores"
            memorySize = "memorySize"
            memoryForVms = "memoryForVms"
            numVmsStarted = "numVmsStarted"
            numVmsStarting = "numVmsStarting"


    class LicenseInfo(vmodl.DynamicData):
        @property
        def licenseKey(self) -> str: ...
        @licenseKey.setter
        def licenseKey(self, value: str):
            self._licenseKey = value
        @property
        def editionKey(self) -> str: ...
        @editionKey.setter
        def editionKey(self, value: str):
            self._editionKey = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def total(self) -> int: ...
        @total.setter
        def total(self, value: int):
            self._total = value
        @property
        def used(self) -> int: ...
        @used.setter
        def used(self, value: int):
            self._used = value
        @property
        def costUnit(self) -> str: ...
        @costUnit.setter
        def costUnit(self, value: str):
            self._costUnit = value
        @property
        def properties(self) -> List[vmodl.KeyAnyValue]: ...
        @properties.setter
        def properties(self, value: List[vmodl.KeyAnyValue]):
            self._properties = value
        @property
        def labels(self) -> List[KeyValue]: ...
        @labels.setter
        def labels(self, value: List[KeyValue]):
            self._labels = value


    class LicenseServer(LicenseManager.LicenseSource):
        @property
        def licenseServer(self) -> str: ...
        @licenseServer.setter
        def licenseServer(self, value: str):
            self._licenseServer = value


    class LicenseSource(vmodl.DynamicData): ...


    class LicenseUsageInfo(vmodl.DynamicData):
        @property
        def source(self) -> LicenseManager.LicenseSource: ...
        @source.setter
        def source(self, value: LicenseManager.LicenseSource):
            self._source = value
        @property
        def sourceAvailable(self) -> bool: ...
        @sourceAvailable.setter
        def sourceAvailable(self, value: bool):
            self._sourceAvailable = value
        @property
        def reservationInfo(self) -> List[LicenseManager.ReservationInfo]: ...
        @reservationInfo.setter
        def reservationInfo(self, value: List[LicenseManager.ReservationInfo]):
            self._reservationInfo = value
        @property
        def featureInfo(self) -> List[LicenseManager.FeatureInfo]: ...
        @featureInfo.setter
        def featureInfo(self, value: List[LicenseManager.FeatureInfo]):
            self._featureInfo = value


    class LocalLicense(LicenseManager.LicenseSource):
        @property
        def licenseKeys(self) -> str: ...
        @licenseKeys.setter
        def licenseKeys(self, value: str):
            self._licenseKeys = value


    class ReservationInfo(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value
        @property
        def state(self) -> LicenseManager.ReservationInfo.State | Literal['notUsed', 'noLicense', 'unlicensedUse', 'licensed']: ...
        @state.setter
        def state(self, value: LicenseManager.ReservationInfo.State | Literal['notUsed', 'noLicense', 'unlicensedUse', 'licensed']):
            self._state = value
        @property
        def required(self) -> int: ...
        @required.setter
        def required(self, value: int):
            self._required = value


    class LicenseKey(Enum):
        esxFull = "esxFull"
        esxVmtn = "esxVmtn"
        esxExpress = "esxExpress"
        san = "san"
        iscsi = "iscsi"
        nas = "nas"
        vsmp = "vsmp"
        backup = "backup"
        vc = "vc"
        vcExpress = "vcExpress"
        esxHost = "esxHost"
        gsxHost = "gsxHost"
        serverHost = "serverHost"
        drsPower = "drsPower"
        vmotion = "vmotion"
        drs = "drs"
        das = "das"


    class LicenseState(Enum):
        initializing = "initializing"
        normal = "normal"
        marginal = "marginal"
        fault = "fault"


class LocalizationManager(ManagedObject):
    @property
    def catalog(self) -> List[LocalizationManager.MessageCatalog]: ...


    class MessageCatalog(vmodl.DynamicData):
        @property
        def moduleName(self) -> str: ...
        @moduleName.setter
        def moduleName(self, value: str):
            self._moduleName = value
        @property
        def catalogName(self) -> str: ...
        @catalogName.setter
        def catalogName(self, value: str):
            self._catalogName = value
        @property
        def locale(self) -> str: ...
        @locale.setter
        def locale(self, value: str):
            self._locale = value
        @property
        def catalogUri(self) -> str: ...
        @catalogUri.setter
        def catalogUri(self, value: str):
            self._catalogUri = value
        @property
        def lastModified(self) -> datetime: ...
        @lastModified.setter
        def lastModified(self, value: datetime):
            self._lastModified = value
        @property
        def md5sum(self) -> str: ...
        @md5sum.setter
        def md5sum(self, value: str):
            self._md5sum = value
        @property
        def version(self) -> str: ...
        @version.setter
        def version(self, value: str):
            self._version = value


class ManagedEntity(ExtensibleManagedObject):
    @property
    def parent(self) -> ManagedEntity: ...
    @property
    def customValue(self) -> List[CustomFieldsManager.Value]: ...
    @property
    def overallStatus(self) -> ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']: ...
    @property
    def configStatus(self) -> ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']: ...
    @property
    def configIssue(self) -> List[event.Event]: ...
    @property
    def effectiveRole(self) -> List[int]: ...
    @property
    def permission(self) -> List[AuthorizationManager.Permission]: ...
    @property
    def name(self) -> str: ...
    @property
    def disabledMethod(self) -> List[ManagedMethod]: ...
    @property
    def recentTask(self) -> List[Task]: ...
    @property
    def declaredAlarmState(self) -> List[alarm.AlarmState]: ...
    @property
    def triggeredAlarmState(self) -> List[alarm.AlarmState]: ...
    @property
    def alarmActionsEnabled(self) -> bool: ...
    @property
    def tag(self) -> List[Tag]: ...
    def Reload(self) -> NoneType: ...
    def Rename(self, newName: str) -> Task: ...
    def Destroy(self) -> Task: ...


    class Status(Enum):
        gray = "gray"
        green = "green"
        yellow = "yellow"
        red = "red"


class Network(ManagedEntity):
    @property
    def summary(self) -> Network.Summary: ...
    @property
    def host(self) -> List[HostSystem]: ...
    @property
    def vm(self) -> List[VirtualMachine]: ...
    def DestroyNetwork(self) -> NoneType: ...


    class Summary(vmodl.DynamicData):
        @property
        def network(self) -> Network: ...
        @network.setter
        def network(self, value: Network):
            self._network = value
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def accessible(self) -> bool: ...
        @accessible.setter
        def accessible(self, value: bool):
            self._accessible = value
        @property
        def ipPoolName(self) -> str: ...
        @ipPoolName.setter
        def ipPoolName(self, value: str):
            self._ipPoolName = value
        @property
        def ipPoolId(self) -> int: ...
        @ipPoolId.setter
        def ipPoolId(self, value: int):
            self._ipPoolId = value


class OpaqueNetwork(Network):
    @property
    def capability(self) -> OpaqueNetwork.Capability: ...
    @property
    def extraConfig(self) -> List[option.OptionValue]: ...


    class Capability(vmodl.DynamicData):
        @property
        def networkReservationSupported(self) -> bool: ...
        @networkReservationSupported.setter
        def networkReservationSupported(self, value: bool):
            self._networkReservationSupported = value


    class Summary(Network.Summary):
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


class OverheadMemoryManager(ManagedObject):
    def LookupVmOverheadMemory(self, vm: VirtualMachine, host: HostSystem) -> long: ...


class OvfManager(ManagedObject):
    @property
    def ovfImportOption(self) -> List[OvfManager.OvfOptionInfo]: ...
    @property
    def ovfExportOption(self) -> List[OvfManager.OvfOptionInfo]: ...
    def ValidateHost(self, ovfDescriptor: str, host: HostSystem, vhp: OvfManager.ValidateHostParams) -> OvfManager.ValidateHostResult: ...
    def ParseDescriptor(self, ovfDescriptor: str, pdp: OvfManager.ParseDescriptorParams) -> OvfManager.ParseDescriptorResult: ...
    def CreateImportSpec(self, ovfDescriptor: str, resourcePool: ResourcePool, datastore: Datastore, cisp: OvfManager.CreateImportSpecParams) -> OvfManager.CreateImportSpecResult: ...
    def CreateDescriptor(self, obj: ManagedEntity, cdp: OvfManager.CreateDescriptorParams) -> OvfManager.CreateDescriptorResult: ...


    class CommonParams(vmodl.DynamicData):
        @property
        def locale(self) -> str: ...
        @locale.setter
        def locale(self, value: str):
            self._locale = value
        @property
        def deploymentOption(self) -> str: ...
        @deploymentOption.setter
        def deploymentOption(self, value: str):
            self._deploymentOption = value
        @property
        def msgBundle(self) -> List[KeyValue]: ...
        @msgBundle.setter
        def msgBundle(self, value: List[KeyValue]):
            self._msgBundle = value
        @property
        def importOption(self) -> List[str]: ...
        @importOption.setter
        def importOption(self, value: List[str]):
            self._importOption = value


    class CreateDescriptorParams(vmodl.DynamicData):
        @property
        def ovfFiles(self) -> List[OvfManager.OvfFile]: ...
        @ovfFiles.setter
        def ovfFiles(self, value: List[OvfManager.OvfFile]):
            self._ovfFiles = value
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
        def includeImageFiles(self) -> bool: ...
        @includeImageFiles.setter
        def includeImageFiles(self, value: bool):
            self._includeImageFiles = value
        @property
        def exportOption(self) -> List[str]: ...
        @exportOption.setter
        def exportOption(self, value: List[str]):
            self._exportOption = value
        @property
        def snapshot(self) -> vm.Snapshot: ...
        @snapshot.setter
        def snapshot(self, value: vm.Snapshot):
            self._snapshot = value


    class CreateDescriptorResult(vmodl.DynamicData):
        @property
        def ovfDescriptor(self) -> str: ...
        @ovfDescriptor.setter
        def ovfDescriptor(self, value: str):
            self._ovfDescriptor = value
        @property
        def error(self) -> List[vmodl.MethodFault]: ...
        @error.setter
        def error(self, value: List[vmodl.MethodFault]):
            self._error = value
        @property
        def warning(self) -> List[vmodl.MethodFault]: ...
        @warning.setter
        def warning(self, value: List[vmodl.MethodFault]):
            self._warning = value
        @property
        def includeImageFiles(self) -> bool: ...
        @includeImageFiles.setter
        def includeImageFiles(self, value: bool):
            self._includeImageFiles = value


    class CreateImportSpecParams(OvfManager.CommonParams):
        @property
        def entityName(self) -> str: ...
        @entityName.setter
        def entityName(self, value: str):
            self._entityName = value
        @property
        def hostSystem(self) -> HostSystem: ...
        @hostSystem.setter
        def hostSystem(self, value: HostSystem):
            self._hostSystem = value
        @property
        def networkMapping(self) -> List[OvfManager.NetworkMapping]: ...
        @networkMapping.setter
        def networkMapping(self, value: List[OvfManager.NetworkMapping]):
            self._networkMapping = value
        @property
        def ipAllocationPolicy(self) -> str: ...
        @ipAllocationPolicy.setter
        def ipAllocationPolicy(self, value: str):
            self._ipAllocationPolicy = value
        @property
        def ipProtocol(self) -> str: ...
        @ipProtocol.setter
        def ipProtocol(self, value: str):
            self._ipProtocol = value
        @property
        def propertyMapping(self) -> List[KeyValue]: ...
        @propertyMapping.setter
        def propertyMapping(self, value: List[KeyValue]):
            self._propertyMapping = value
        @property
        def resourceMapping(self) -> List[OvfManager.ResourceMap]: ...
        @resourceMapping.setter
        def resourceMapping(self, value: List[OvfManager.ResourceMap]):
            self._resourceMapping = value
        @property
        def diskProvisioning(self) -> str: ...
        @diskProvisioning.setter
        def diskProvisioning(self, value: str):
            self._diskProvisioning = value
        @property
        def instantiationOst(self) -> OvfConsumer.OstNode: ...
        @instantiationOst.setter
        def instantiationOst(self, value: OvfConsumer.OstNode):
            self._instantiationOst = value


        class DiskProvisioningType(Enum):
            monolithicSparse = "monolithicSparse"
            monolithicFlat = "monolithicFlat"
            twoGbMaxExtentSparse = "twoGbMaxExtentSparse"
            twoGbMaxExtentFlat = "twoGbMaxExtentFlat"
            thin = "thin"
            thick = "thick"
            seSparse = "seSparse"
            eagerZeroedThick = "eagerZeroedThick"
            sparse = "sparse"
            flat = "flat"


    class CreateImportSpecResult(vmodl.DynamicData):
        @property
        def importSpec(self) -> ImportSpec: ...
        @importSpec.setter
        def importSpec(self, value: ImportSpec):
            self._importSpec = value
        @property
        def fileItem(self) -> List[OvfManager.FileItem]: ...
        @fileItem.setter
        def fileItem(self, value: List[OvfManager.FileItem]):
            self._fileItem = value
        @property
        def warning(self) -> List[vmodl.MethodFault]: ...
        @warning.setter
        def warning(self, value: List[vmodl.MethodFault]):
            self._warning = value
        @property
        def error(self) -> List[vmodl.MethodFault]: ...
        @error.setter
        def error(self, value: List[vmodl.MethodFault]):
            self._error = value


    class DeploymentOption(vmodl.DynamicData):
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
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value


    class FileItem(vmodl.DynamicData):
        @property
        def deviceId(self) -> str: ...
        @deviceId.setter
        def deviceId(self, value: str):
            self._deviceId = value
        @property
        def path(self) -> str: ...
        @path.setter
        def path(self, value: str):
            self._path = value
        @property
        def compressionMethod(self) -> str: ...
        @compressionMethod.setter
        def compressionMethod(self, value: str):
            self._compressionMethod = value
        @property
        def chunkSize(self) -> long: ...
        @chunkSize.setter
        def chunkSize(self, value: long):
            self._chunkSize = value
        @property
        def size(self) -> long: ...
        @size.setter
        def size(self, value: long):
            self._size = value
        @property
        def cimType(self) -> int: ...
        @cimType.setter
        def cimType(self, value: int):
            self._cimType = value
        @property
        def create(self) -> bool: ...
        @create.setter
        def create(self, value: bool):
            self._create = value


    class NetworkInfo(vmodl.DynamicData):
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


    class NetworkMapping(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def network(self) -> Network: ...
        @network.setter
        def network(self, value: Network):
            self._network = value


    class OvfFile(vmodl.DynamicData):
        @property
        def deviceId(self) -> str: ...
        @deviceId.setter
        def deviceId(self, value: str):
            self._deviceId = value
        @property
        def path(self) -> str: ...
        @path.setter
        def path(self, value: str):
            self._path = value
        @property
        def compressionMethod(self) -> str: ...
        @compressionMethod.setter
        def compressionMethod(self, value: str):
            self._compressionMethod = value
        @property
        def chunkSize(self) -> long: ...
        @chunkSize.setter
        def chunkSize(self, value: long):
            self._chunkSize = value
        @property
        def size(self) -> long: ...
        @size.setter
        def size(self, value: long):
            self._size = value
        @property
        def capacity(self) -> long: ...
        @capacity.setter
        def capacity(self, value: long):
            self._capacity = value
        @property
        def populatedSize(self) -> long: ...
        @populatedSize.setter
        def populatedSize(self, value: long):
            self._populatedSize = value


    class OvfOptionInfo(vmodl.DynamicData):
        @property
        def option(self) -> str: ...
        @option.setter
        def option(self, value: str):
            self._option = value
        @property
        def description(self) -> vmodl.LocalizableMessage: ...
        @description.setter
        def description(self, value: vmodl.LocalizableMessage):
            self._description = value


    class ParseDescriptorParams(OvfManager.CommonParams): ...


    class ParseDescriptorResult(vmodl.DynamicData):
        @property
        def eula(self) -> List[str]: ...
        @eula.setter
        def eula(self, value: List[str]):
            self._eula = value
        @property
        def network(self) -> List[OvfManager.NetworkInfo]: ...
        @network.setter
        def network(self, value: List[OvfManager.NetworkInfo]):
            self._network = value
        @property
        def ipAllocationScheme(self) -> List[str]: ...
        @ipAllocationScheme.setter
        def ipAllocationScheme(self, value: List[str]):
            self._ipAllocationScheme = value
        @property
        def ipProtocols(self) -> List[str]: ...
        @ipProtocols.setter
        def ipProtocols(self, value: List[str]):
            self._ipProtocols = value
        @property
        def property(self) -> List[vApp.PropertyInfo]: ...
        @property.setter
        def property(self, value: List[vApp.PropertyInfo]):
            self._property = value
        @property
        def productInfo(self) -> vApp.ProductInfo: ...
        @productInfo.setter
        def productInfo(self, value: vApp.ProductInfo):
            self._productInfo = value
        @property
        def annotation(self) -> str: ...
        @annotation.setter
        def annotation(self, value: str):
            self._annotation = value
        @property
        def approximateDownloadSize(self) -> long: ...
        @approximateDownloadSize.setter
        def approximateDownloadSize(self, value: long):
            self._approximateDownloadSize = value
        @property
        def approximateFlatDeploymentSize(self) -> long: ...
        @approximateFlatDeploymentSize.setter
        def approximateFlatDeploymentSize(self, value: long):
            self._approximateFlatDeploymentSize = value
        @property
        def approximateSparseDeploymentSize(self) -> long: ...
        @approximateSparseDeploymentSize.setter
        def approximateSparseDeploymentSize(self, value: long):
            self._approximateSparseDeploymentSize = value
        @property
        def defaultEntityName(self) -> str: ...
        @defaultEntityName.setter
        def defaultEntityName(self, value: str):
            self._defaultEntityName = value
        @property
        def virtualApp(self) -> bool: ...
        @virtualApp.setter
        def virtualApp(self, value: bool):
            self._virtualApp = value
        @property
        def deploymentOption(self) -> List[OvfManager.DeploymentOption]: ...
        @deploymentOption.setter
        def deploymentOption(self, value: List[OvfManager.DeploymentOption]):
            self._deploymentOption = value
        @property
        def defaultDeploymentOption(self) -> str: ...
        @defaultDeploymentOption.setter
        def defaultDeploymentOption(self, value: str):
            self._defaultDeploymentOption = value
        @property
        def entityName(self) -> List[KeyValue]: ...
        @entityName.setter
        def entityName(self, value: List[KeyValue]):
            self._entityName = value
        @property
        def annotatedOst(self) -> OvfConsumer.OstNode: ...
        @annotatedOst.setter
        def annotatedOst(self, value: OvfConsumer.OstNode):
            self._annotatedOst = value
        @property
        def error(self) -> List[vmodl.MethodFault]: ...
        @error.setter
        def error(self, value: List[vmodl.MethodFault]):
            self._error = value
        @property
        def warning(self) -> List[vmodl.MethodFault]: ...
        @warning.setter
        def warning(self, value: List[vmodl.MethodFault]):
            self._warning = value


    class ResourceMap(vmodl.DynamicData):
        @property
        def source(self) -> str: ...
        @source.setter
        def source(self, value: str):
            self._source = value
        @property
        def parent(self) -> ResourcePool: ...
        @parent.setter
        def parent(self, value: ResourcePool):
            self._parent = value
        @property
        def resourceSpec(self) -> ResourceConfigSpec: ...
        @resourceSpec.setter
        def resourceSpec(self, value: ResourceConfigSpec):
            self._resourceSpec = value
        @property
        def datastore(self) -> Datastore: ...
        @datastore.setter
        def datastore(self, value: Datastore):
            self._datastore = value


    class ValidateHostParams(OvfManager.CommonParams): ...


    class ValidateHostResult(vmodl.DynamicData):
        @property
        def downloadSize(self) -> long: ...
        @downloadSize.setter
        def downloadSize(self, value: long):
            self._downloadSize = value
        @property
        def flatDeploymentSize(self) -> long: ...
        @flatDeploymentSize.setter
        def flatDeploymentSize(self, value: long):
            self._flatDeploymentSize = value
        @property
        def sparseDeploymentSize(self) -> long: ...
        @sparseDeploymentSize.setter
        def sparseDeploymentSize(self, value: long):
            self._sparseDeploymentSize = value
        @property
        def error(self) -> List[vmodl.MethodFault]: ...
        @error.setter
        def error(self, value: List[vmodl.MethodFault]):
            self._error = value
        @property
        def warning(self) -> List[vmodl.MethodFault]: ...
        @warning.setter
        def warning(self, value: List[vmodl.MethodFault]):
            self._warning = value
        @property
        def supportedDiskProvisioning(self) -> List[str]: ...
        @supportedDiskProvisioning.setter
        def supportedDiskProvisioning(self, value: List[str]):
            self._supportedDiskProvisioning = value


class PerformanceManager(ManagedObject):
    @property
    def description(self) -> PerformanceDescription: ...
    @property
    def historicalInterval(self) -> List[HistoricalInterval]: ...
    @property
    def perfCounter(self) -> List[PerformanceManager.CounterInfo]: ...
    def QueryProviderSummary(self, entity: ManagedObject) -> PerformanceManager.ProviderSummary: ...
    def QueryAvailableMetric(self, entity: ManagedObject, beginTime: datetime, endTime: datetime, intervalId: int) -> List[PerformanceManager.MetricId]: ...
    def QueryCounter(self, counterId: List[int]) -> List[PerformanceManager.CounterInfo]: ...
    def QueryCounterByLevel(self, level: int) -> List[PerformanceManager.CounterInfo]: ...
    def QueryStats(self, querySpec: List[PerformanceManager.QuerySpec]) -> List[PerformanceManager.EntityMetricBase]: ...
    def QueryCompositeStats(self, querySpec: PerformanceManager.QuerySpec) -> PerformanceManager.CompositeEntityMetric: ...
    def CreateHistoricalInterval(self, intervalId: HistoricalInterval) -> NoneType: ...
    def RemoveHistoricalInterval(self, samplePeriod: int) -> NoneType: ...
    def UpdateHistoricalInterval(self, interval: HistoricalInterval) -> NoneType: ...
    def UpdateCounterLevelMapping(self, counterLevelMap: List[PerformanceManager.CounterLevelMapping]) -> NoneType: ...
    def ResetCounterLevelMapping(self, counters: List[int]) -> NoneType: ...


    class CompositeEntityMetric(vmodl.DynamicData):
        @property
        def entity(self) -> PerformanceManager.EntityMetricBase: ...
        @entity.setter
        def entity(self, value: PerformanceManager.EntityMetricBase):
            self._entity = value
        @property
        def childEntity(self) -> List[PerformanceManager.EntityMetricBase]: ...
        @childEntity.setter
        def childEntity(self, value: List[PerformanceManager.EntityMetricBase]):
            self._childEntity = value


    class CounterInfo(vmodl.DynamicData):
        @property
        def key(self) -> int: ...
        @key.setter
        def key(self, value: int):
            self._key = value
        @property
        def nameInfo(self) -> ElementDescription: ...
        @nameInfo.setter
        def nameInfo(self, value: ElementDescription):
            self._nameInfo = value
        @property
        def groupInfo(self) -> ElementDescription: ...
        @groupInfo.setter
        def groupInfo(self, value: ElementDescription):
            self._groupInfo = value
        @property
        def unitInfo(self) -> ElementDescription: ...
        @unitInfo.setter
        def unitInfo(self, value: ElementDescription):
            self._unitInfo = value
        @property
        def rollupType(self) -> PerformanceManager.CounterInfo.RollupType | Literal['average', 'maximum', 'minimum', 'latest', 'summation', 'none']: ...
        @rollupType.setter
        def rollupType(self, value: PerformanceManager.CounterInfo.RollupType | Literal['average', 'maximum', 'minimum', 'latest', 'summation', 'none']):
            self._rollupType = value
        @property
        def statsType(self) -> PerformanceManager.CounterInfo.StatsType | Literal['absolute', 'delta', 'rate']: ...
        @statsType.setter
        def statsType(self, value: PerformanceManager.CounterInfo.StatsType | Literal['absolute', 'delta', 'rate']):
            self._statsType = value
        @property
        def level(self) -> int: ...
        @level.setter
        def level(self, value: int):
            self._level = value
        @property
        def perDeviceLevel(self) -> int: ...
        @perDeviceLevel.setter
        def perDeviceLevel(self, value: int):
            self._perDeviceLevel = value
        @property
        def associatedCounterId(self) -> List[int]: ...
        @associatedCounterId.setter
        def associatedCounterId(self, value: List[int]):
            self._associatedCounterId = value


        class RollupType(Enum):
            average = "average"
            maximum = "maximum"
            minimum = "minimum"
            latest = "latest"
            summation = "summation"
            none = "none"


        class StatsType(Enum):
            absolute = "absolute"
            delta = "delta"
            rate = "rate"


        class Unit(Enum):
            percent = "percent"
            kiloBytes = "kiloBytes"
            megaBytes = "megaBytes"
            megaHertz = "megaHertz"
            number = "number"
            microsecond = "microsecond"
            millisecond = "millisecond"
            second = "second"
            kiloBytesPerSecond = "kiloBytesPerSecond"
            megaBytesPerSecond = "megaBytesPerSecond"
            watt = "watt"
            joule = "joule"
            teraBytes = "teraBytes"
            celsius = "celsius"
            mgCO2eqPerHour = "mgCO2eqPerHour"
            nanosecond = "nanosecond"


    class CounterLevelMapping(vmodl.DynamicData):
        @property
        def counterId(self) -> int: ...
        @counterId.setter
        def counterId(self, value: int):
            self._counterId = value
        @property
        def aggregateLevel(self) -> int: ...
        @aggregateLevel.setter
        def aggregateLevel(self, value: int):
            self._aggregateLevel = value
        @property
        def perDeviceLevel(self) -> int: ...
        @perDeviceLevel.setter
        def perDeviceLevel(self, value: int):
            self._perDeviceLevel = value


    class EntityMetric(PerformanceManager.EntityMetricBase):
        @property
        def sampleInfo(self) -> List[PerformanceManager.SampleInfo]: ...
        @sampleInfo.setter
        def sampleInfo(self, value: List[PerformanceManager.SampleInfo]):
            self._sampleInfo = value
        @property
        def value(self) -> List[PerformanceManager.MetricSeries]: ...
        @value.setter
        def value(self, value: List[PerformanceManager.MetricSeries]):
            self._value = value


    class EntityMetricBase(vmodl.DynamicData):
        @property
        def entity(self) -> ManagedObject: ...
        @entity.setter
        def entity(self, value: ManagedObject):
            self._entity = value


    class EntityMetricCSV(PerformanceManager.EntityMetricBase):
        @property
        def sampleInfoCSV(self) -> str: ...
        @sampleInfoCSV.setter
        def sampleInfoCSV(self, value: str):
            self._sampleInfoCSV = value
        @property
        def value(self) -> List[PerformanceManager.MetricSeriesCSV]: ...
        @value.setter
        def value(self, value: List[PerformanceManager.MetricSeriesCSV]):
            self._value = value


    class IntSeries(PerformanceManager.MetricSeries):
        @property
        def value(self) -> List[long]: ...
        @value.setter
        def value(self, value: List[long]):
            self._value = value


    class MetricId(vmodl.DynamicData):
        @property
        def counterId(self) -> int: ...
        @counterId.setter
        def counterId(self, value: int):
            self._counterId = value
        @property
        def instance(self) -> str: ...
        @instance.setter
        def instance(self, value: str):
            self._instance = value


    class MetricSeries(vmodl.DynamicData):
        @property
        def id(self) -> PerformanceManager.MetricId: ...
        @id.setter
        def id(self, value: PerformanceManager.MetricId):
            self._id = value


    class MetricSeriesCSV(PerformanceManager.MetricSeries):
        @property
        def value(self) -> str: ...
        @value.setter
        def value(self, value: str):
            self._value = value


    class ProviderSummary(vmodl.DynamicData):
        @property
        def entity(self) -> ManagedObject: ...
        @entity.setter
        def entity(self, value: ManagedObject):
            self._entity = value
        @property
        def currentSupported(self) -> bool: ...
        @currentSupported.setter
        def currentSupported(self, value: bool):
            self._currentSupported = value
        @property
        def summarySupported(self) -> bool: ...
        @summarySupported.setter
        def summarySupported(self, value: bool):
            self._summarySupported = value
        @property
        def refreshRate(self) -> int: ...
        @refreshRate.setter
        def refreshRate(self, value: int):
            self._refreshRate = value


    class QuerySpec(vmodl.DynamicData):
        @property
        def entity(self) -> ManagedObject: ...
        @entity.setter
        def entity(self, value: ManagedObject):
            self._entity = value
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
        def maxSample(self) -> int: ...
        @maxSample.setter
        def maxSample(self, value: int):
            self._maxSample = value
        @property
        def metricId(self) -> List[PerformanceManager.MetricId]: ...
        @metricId.setter
        def metricId(self, value: List[PerformanceManager.MetricId]):
            self._metricId = value
        @property
        def intervalId(self) -> int: ...
        @intervalId.setter
        def intervalId(self, value: int):
            self._intervalId = value
        @property
        def format(self) -> str: ...
        @format.setter
        def format(self, value: str):
            self._format = value


    class SampleInfo(vmodl.DynamicData):
        @property
        def timestamp(self) -> datetime: ...
        @timestamp.setter
        def timestamp(self, value: datetime):
            self._timestamp = value
        @property
        def interval(self) -> int: ...
        @interval.setter
        def interval(self, value: int):
            self._interval = value


class ResourcePlanningManager(ManagedObject):
    def EstimateDatabaseSize(self, dbSizeParam: ResourcePlanningManager.DatabaseSizeParam) -> ResourcePlanningManager.DatabaseSizeEstimate: ...


    class DatabaseSizeEstimate(vmodl.DynamicData):
        @property
        def size(self) -> long: ...
        @size.setter
        def size(self, value: long):
            self._size = value


    class DatabaseSizeParam(vmodl.DynamicData):
        @property
        def inventoryDesc(self) -> ResourcePlanningManager.InventoryDescription: ...
        @inventoryDesc.setter
        def inventoryDesc(self, value: ResourcePlanningManager.InventoryDescription):
            self._inventoryDesc = value
        @property
        def perfStatsDesc(self) -> ResourcePlanningManager.PerfStatsDescription: ...
        @perfStatsDesc.setter
        def perfStatsDesc(self, value: ResourcePlanningManager.PerfStatsDescription):
            self._perfStatsDesc = value


    class InventoryDescription(vmodl.DynamicData):
        @property
        def numHosts(self) -> int: ...
        @numHosts.setter
        def numHosts(self, value: int):
            self._numHosts = value
        @property
        def numVirtualMachines(self) -> int: ...
        @numVirtualMachines.setter
        def numVirtualMachines(self, value: int):
            self._numVirtualMachines = value
        @property
        def numResourcePools(self) -> int: ...
        @numResourcePools.setter
        def numResourcePools(self, value: int):
            self._numResourcePools = value
        @property
        def numClusters(self) -> int: ...
        @numClusters.setter
        def numClusters(self, value: int):
            self._numClusters = value
        @property
        def numCpuDev(self) -> int: ...
        @numCpuDev.setter
        def numCpuDev(self, value: int):
            self._numCpuDev = value
        @property
        def numNetDev(self) -> int: ...
        @numNetDev.setter
        def numNetDev(self, value: int):
            self._numNetDev = value
        @property
        def numDiskDev(self) -> int: ...
        @numDiskDev.setter
        def numDiskDev(self, value: int):
            self._numDiskDev = value
        @property
        def numvCpuDev(self) -> int: ...
        @numvCpuDev.setter
        def numvCpuDev(self, value: int):
            self._numvCpuDev = value
        @property
        def numvNetDev(self) -> int: ...
        @numvNetDev.setter
        def numvNetDev(self, value: int):
            self._numvNetDev = value
        @property
        def numvDiskDev(self) -> int: ...
        @numvDiskDev.setter
        def numvDiskDev(self, value: int):
            self._numvDiskDev = value


    class PerfStatsDescription(vmodl.DynamicData):
        @property
        def intervals(self) -> List[HistoricalInterval]: ...
        @intervals.setter
        def intervals(self, value: List[HistoricalInterval]):
            self._intervals = value


class ResourcePool(ManagedEntity):
    @property
    def summary(self) -> ResourcePool.Summary: ...
    @property
    def runtime(self) -> ResourcePool.RuntimeInfo: ...
    @property
    def owner(self) -> ComputeResource: ...
    @property
    def resourcePool(self) -> List[ResourcePool]: ...
    @property
    def vm(self) -> List[VirtualMachine]: ...
    @property
    def config(self) -> ResourceConfigSpec: ...
    @property
    def namespace(self) -> str: ...
    @property
    def childConfiguration(self) -> List[ResourceConfigSpec]: ...
    def UpdateConfig(self, name: str, config: ResourceConfigSpec) -> NoneType: ...
    def MoveInto(self, list: List[ManagedEntity]) -> NoneType: ...
    def UpdateChildResourceConfiguration(self, spec: List[ResourceConfigSpec]) -> NoneType: ...
    def CreateResourcePool(self, name: str, spec: ResourceConfigSpec) -> ResourcePool: ...
    def DestroyChildren(self) -> NoneType: ...
    def CreateVApp(self, name: str, resSpec: ResourceConfigSpec, configSpec: vApp.VAppConfigSpec, vmFolder: Folder) -> VirtualApp: ...
    def CreateVm(self, config: vm.ConfigSpec, host: HostSystem) -> Task: ...
    def RegisterVm(self, path: str, name: str, host: HostSystem) -> Task: ...
    def ImportVApp(self, spec: ImportSpec, folder: Folder, host: HostSystem) -> HttpNfcLease: ...
    def QueryResourceConfigOption(self) -> ResourceConfigOption: ...
    def RefreshRuntime(self) -> NoneType: ...


    class ResourceUsage(vmodl.DynamicData):
        @property
        def reservationUsed(self) -> long: ...
        @reservationUsed.setter
        def reservationUsed(self, value: long):
            self._reservationUsed = value
        @property
        def reservationUsedForVm(self) -> long: ...
        @reservationUsedForVm.setter
        def reservationUsedForVm(self, value: long):
            self._reservationUsedForVm = value
        @property
        def unreservedForPool(self) -> long: ...
        @unreservedForPool.setter
        def unreservedForPool(self, value: long):
            self._unreservedForPool = value
        @property
        def unreservedForVm(self) -> long: ...
        @unreservedForVm.setter
        def unreservedForVm(self, value: long):
            self._unreservedForVm = value
        @property
        def overallUsage(self) -> long: ...
        @overallUsage.setter
        def overallUsage(self, value: long):
            self._overallUsage = value
        @property
        def maxUsage(self) -> long: ...
        @maxUsage.setter
        def maxUsage(self, value: long):
            self._maxUsage = value


    class RuntimeInfo(vmodl.DynamicData):
        @property
        def memory(self) -> ResourcePool.ResourceUsage: ...
        @memory.setter
        def memory(self, value: ResourcePool.ResourceUsage):
            self._memory = value
        @property
        def cpu(self) -> ResourcePool.ResourceUsage: ...
        @cpu.setter
        def cpu(self, value: ResourcePool.ResourceUsage):
            self._cpu = value
        @property
        def overallStatus(self) -> ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']: ...
        @overallStatus.setter
        def overallStatus(self, value: ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']):
            self._overallStatus = value
        @property
        def sharesScalable(self) -> str: ...
        @sharesScalable.setter
        def sharesScalable(self, value: str):
            self._sharesScalable = value


    class Summary(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def config(self) -> ResourceConfigSpec: ...
        @config.setter
        def config(self, value: ResourceConfigSpec):
            self._config = value
        @property
        def runtime(self) -> ResourcePool.RuntimeInfo: ...
        @runtime.setter
        def runtime(self, value: ResourcePool.RuntimeInfo):
            self._runtime = value
        @property
        def quickStats(self) -> ResourcePool.Summary.QuickStats: ...
        @quickStats.setter
        def quickStats(self, value: ResourcePool.Summary.QuickStats):
            self._quickStats = value
        @property
        def configuredMemoryMB(self) -> int: ...
        @configuredMemoryMB.setter
        def configuredMemoryMB(self, value: int):
            self._configuredMemoryMB = value


        class QuickStats(vmodl.DynamicData):
            @property
            def overallCpuUsage(self) -> long: ...
            @overallCpuUsage.setter
            def overallCpuUsage(self, value: long):
                self._overallCpuUsage = value
            @property
            def overallCpuDemand(self) -> long: ...
            @overallCpuDemand.setter
            def overallCpuDemand(self, value: long):
                self._overallCpuDemand = value
            @property
            def guestMemoryUsage(self) -> long: ...
            @guestMemoryUsage.setter
            def guestMemoryUsage(self, value: long):
                self._guestMemoryUsage = value
            @property
            def hostMemoryUsage(self) -> long: ...
            @hostMemoryUsage.setter
            def hostMemoryUsage(self, value: long):
                self._hostMemoryUsage = value
            @property
            def distributedCpuEntitlement(self) -> long: ...
            @distributedCpuEntitlement.setter
            def distributedCpuEntitlement(self, value: long):
                self._distributedCpuEntitlement = value
            @property
            def distributedMemoryEntitlement(self) -> long: ...
            @distributedMemoryEntitlement.setter
            def distributedMemoryEntitlement(self, value: long):
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
            def privateMemory(self) -> long: ...
            @privateMemory.setter
            def privateMemory(self, value: long):
                self._privateMemory = value
            @property
            def sharedMemory(self) -> long: ...
            @sharedMemory.setter
            def sharedMemory(self, value: long):
                self._sharedMemory = value
            @property
            def swappedMemory(self) -> long: ...
            @swappedMemory.setter
            def swappedMemory(self, value: long):
                self._swappedMemory = value
            @property
            def balloonedMemory(self) -> long: ...
            @balloonedMemory.setter
            def balloonedMemory(self, value: long):
                self._balloonedMemory = value
            @property
            def overheadMemory(self) -> long: ...
            @overheadMemory.setter
            def overheadMemory(self, value: long):
                self._overheadMemory = value
            @property
            def consumedOverheadMemory(self) -> long: ...
            @consumedOverheadMemory.setter
            def consumedOverheadMemory(self, value: long):
                self._consumedOverheadMemory = value
            @property
            def compressedMemory(self) -> long: ...
            @compressedMemory.setter
            def compressedMemory(self, value: long):
                self._compressedMemory = value


class SearchIndex(ManagedObject):
    def FindByUuid(self, datacenter: Datacenter, uuid: str, vmSearch: bool, instanceUuid: bool) -> ManagedEntity: ...
    def FindByDatastorePath(self, datacenter: Datacenter, path: str) -> VirtualMachine: ...
    def FindByDnsName(self, datacenter: Datacenter, dnsName: str, vmSearch: bool) -> ManagedEntity: ...
    def FindByIp(self, datacenter: Datacenter, ip: str, vmSearch: bool) -> ManagedEntity: ...
    def FindByInventoryPath(self, inventoryPath: str) -> ManagedEntity: ...
    def FindChild(self, entity: ManagedEntity, name: str) -> ManagedEntity: ...
    def FindAllByUuid(self, datacenter: Datacenter, uuid: str, vmSearch: bool, instanceUuid: bool) -> List[ManagedEntity]: ...
    def FindAllByDnsName(self, datacenter: Datacenter, dnsName: str, vmSearch: bool) -> List[ManagedEntity]: ...
    def FindAllByIp(self, datacenter: Datacenter, ip: str, vmSearch: bool) -> List[ManagedEntity]: ...


class ServiceInstance(ManagedObject):
    @property
    def serverClock(self) -> datetime: ...
    @property
    def capability(self) -> Capability: ...
    @property
    def content(self) -> ServiceInstanceContent: ...
    def CurrentTime(self) -> datetime: ...
    def RetrieveContent(self) -> ServiceInstanceContent: ...
    def ValidateMigration(self, vm: List[VirtualMachine], state: VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended'], testType: List[str], pool: ResourcePool, host: HostSystem) -> List[event.Event]: ...
    def QueryVMotionCompatibility(self, vm: VirtualMachine, host: List[HostSystem], compatibility: List[str]) -> List[ServiceInstance.HostVMotionCompatibility]: ...
    def RetrieveProductComponents(self) -> List[ServiceInstance.ProductComponentInfo]: ...


    class HostVMotionCompatibility(vmodl.DynamicData):
        @property
        def host(self) -> HostSystem: ...
        @host.setter
        def host(self, value: HostSystem):
            self._host = value
        @property
        def compatibility(self) -> List[str]: ...
        @compatibility.setter
        def compatibility(self, value: List[str]):
            self._compatibility = value


    class ProductComponentInfo(vmodl.DynamicData):
        @property
        def id(self) -> str: ...
        @id.setter
        def id(self, value: str):
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
        def release(self) -> int: ...
        @release.setter
        def release(self, value: int):
            self._release = value


    class VMotionCompatibilityType(Enum):
        cpu = "cpu"
        software = "software"


    class ValidateMigrationTestType(Enum):
        sourceTests = "sourceTests"
        compatibilityTests = "compatibilityTests"
        diskAccessibilityTests = "diskAccessibilityTests"
        resourceTests = "resourceTests"


class ServiceManager(ManagedObject):
    @property
    def service(self) -> List[ServiceManager.ServiceInfo]: ...
    def QueryServiceList(self, serviceName: str, location: List[str]) -> List[ServiceManager.ServiceInfo]: ...


    class ServiceInfo(vmodl.DynamicData):
        @property
        def serviceName(self) -> str: ...
        @serviceName.setter
        def serviceName(self, value: str):
            self._serviceName = value
        @property
        def location(self) -> List[str]: ...
        @location.setter
        def location(self, value: List[str]):
            self._location = value
        @property
        def service(self) -> ManagedObject: ...
        @service.setter
        def service(self, value: ManagedObject):
            self._service = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value


class SessionManager(ManagedObject):
    @property
    def sessionList(self) -> List[UserSession]: ...
    @property
    def currentSession(self) -> UserSession: ...
    @property
    def message(self) -> str: ...
    @property
    def messageLocaleList(self) -> List[str]: ...
    @property
    def supportedLocaleList(self) -> List[str]: ...
    @property
    def defaultLocale(self) -> str: ...
    def UpdateMessage(self, message: str) -> NoneType: ...
    def LoginByToken(self, locale: str) -> UserSession: ...
    def Login(self, userName: str, password: str, locale: str) -> UserSession: ...
    def LoginBySSPI(self, base64Token: str, locale: str) -> UserSession: ...
    def Logout(self) -> NoneType: ...
    def AcquireLocalTicket(self, userName: str) -> SessionManager.LocalTicket: ...
    def AcquireGenericServiceTicket(self, spec: SessionManager.ServiceRequestSpec) -> SessionManager.GenericServiceTicket: ...
    def Terminate(self, sessionId: List[str]) -> NoneType: ...
    def SetLocale(self, locale: str) -> NoneType: ...
    def LoginExtensionBySubjectName(self, extensionKey: str, locale: str) -> UserSession: ...
    def LoginExtensionByCertificate(self, extensionKey: str, locale: str) -> UserSession: ...
    def ImpersonateUser(self, userName: str, locale: str) -> UserSession: ...
    def SessionIsActive(self, sessionID: str, userName: str) -> bool: ...
    def AcquireCloneTicket(self) -> str: ...
    def CloneSession(self, cloneTicket: str) -> UserSession: ...


    class GenericServiceTicket(vmodl.DynamicData):
        @property
        def id(self) -> str: ...
        @id.setter
        def id(self, value: str):
            self._id = value
        @property
        def hostName(self) -> str: ...
        @hostName.setter
        def hostName(self, value: str):
            self._hostName = value
        @property
        def sslThumbprint(self) -> str: ...
        @sslThumbprint.setter
        def sslThumbprint(self, value: str):
            self._sslThumbprint = value
        @property
        def certThumbprintList(self) -> List[vm.CertThumbprint]: ...
        @certThumbprintList.setter
        def certThumbprintList(self, value: List[vm.CertThumbprint]):
            self._certThumbprintList = value
        @property
        def ticketType(self) -> str: ...
        @ticketType.setter
        def ticketType(self, value: str):
            self._ticketType = value


        class TicketType(Enum):
            HttpNfcServiceTicket = "HttpNfcServiceTicket"
            HostServiceTicket = "HostServiceTicket"
            VcServiceTicket = "VcServiceTicket"


    class HttpServiceRequestSpec(SessionManager.ServiceRequestSpec):
        @property
        def method(self) -> str: ...
        @method.setter
        def method(self, value: str):
            self._method = value
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value


        class Method(Enum):
            httpOptions = "httpOptions"
            httpGet = "httpGet"
            httpHead = "httpHead"
            httpPost = "httpPost"
            httpPut = "httpPut"
            httpDelete = "httpDelete"
            httpTrace = "httpTrace"
            httpConnect = "httpConnect"


    class LocalTicket(vmodl.DynamicData):
        @property
        def userName(self) -> str: ...
        @userName.setter
        def userName(self, value: str):
            self._userName = value
        @property
        def passwordFilePath(self) -> str: ...
        @passwordFilePath.setter
        def passwordFilePath(self, value: str):
            self._passwordFilePath = value


    class ServiceRequestSpec(vmodl.DynamicData): ...


    class VmomiServiceRequestSpec(SessionManager.ServiceRequestSpec):
        @property
        def method(self) -> ManagedMethod: ...
        @method.setter
        def method(self, value: ManagedMethod):
            self._method = value


class SimpleCommand(ManagedObject):
    @property
    def encodingType(self) -> SimpleCommand.Encoding | Literal['CSV', 'HEX', 'STRING']: ...
    @property
    def entity(self) -> ServiceManager.ServiceInfo: ...
    def Execute(self, arguments: List[str]) -> str: ...


    class Encoding(Enum):
        CSV = "CSV"
        HEX = "HEX"
        STRING = "STRING"


class SiteInfoManager(ManagedObject):
    def GetSiteInfo(self) -> SiteInfo: ...


class StoragePod(Folder):
    @property
    def summary(self) -> StoragePod.Summary: ...
    @property
    def podStorageDrsEntry(self) -> StorageResourceManager.PodStorageDrsEntry: ...


    class Summary(vmodl.DynamicData):
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
        @property
        def freeSpace(self) -> long: ...
        @freeSpace.setter
        def freeSpace(self, value: long):
            self._freeSpace = value


class StorageQueryManager(ManagedObject):
    def QueryHostsWithAttachedLun(self, lunUuid: str) -> List[HostSystem]: ...


class StorageResourceManager(ManagedObject):
    def ConfigureDatastoreIORM(self, datastore: Datastore, spec: StorageResourceManager.IORMConfigSpec) -> Task: ...
    def QueryIORMConfigOption(self, host: HostSystem) -> StorageResourceManager.IORMConfigOption: ...
    def QueryDatastorePerformanceSummary(self, datastore: Datastore) -> List[StorageResourceManager.StoragePerformanceSummary]: ...
    def ApplyRecommendationToPod(self, pod: StoragePod, key: str) -> Task: ...
    def ApplyRecommendation(self, key: List[str]) -> Task: ...
    def CancelRecommendation(self, key: List[str]) -> NoneType: ...
    def RefreshRecommendation(self, pod: StoragePod) -> NoneType: ...
    def RefreshRecommendationsForPod(self, pod: StoragePod) -> Task: ...
    def ConfigureStorageDrsForPod(self, pod: StoragePod, spec: storageDrs.ConfigSpec, modify: bool) -> Task: ...
    def ValidateStoragePodConfig(self, pod: StoragePod, spec: storageDrs.ConfigSpec) -> vmodl.MethodFault: ...
    def RecommendDatastores(self, storageSpec: storageDrs.StoragePlacementSpec) -> storageDrs.StoragePlacementResult: ...


    class IOAllocationInfo(vmodl.DynamicData):
        @property
        def limit(self) -> long: ...
        @limit.setter
        def limit(self, value: long):
            self._limit = value
        @property
        def shares(self) -> SharesInfo: ...
        @shares.setter
        def shares(self, value: SharesInfo):
            self._shares = value
        @property
        def reservation(self) -> int: ...
        @reservation.setter
        def reservation(self, value: int):
            self._reservation = value


    class IOAllocationOption(vmodl.DynamicData):
        @property
        def limitOption(self) -> option.LongOption: ...
        @limitOption.setter
        def limitOption(self, value: option.LongOption):
            self._limitOption = value
        @property
        def sharesOption(self) -> SharesOption: ...
        @sharesOption.setter
        def sharesOption(self, value: SharesOption):
            self._sharesOption = value


    class IORMConfigInfo(vmodl.DynamicData):
        @property
        def enabled(self) -> bool: ...
        @enabled.setter
        def enabled(self, value: bool):
            self._enabled = value
        @property
        def congestionThresholdMode(self) -> str: ...
        @congestionThresholdMode.setter
        def congestionThresholdMode(self, value: str):
            self._congestionThresholdMode = value
        @property
        def congestionThreshold(self) -> int: ...
        @congestionThreshold.setter
        def congestionThreshold(self, value: int):
            self._congestionThreshold = value
        @property
        def percentOfPeakThroughput(self) -> int: ...
        @percentOfPeakThroughput.setter
        def percentOfPeakThroughput(self, value: int):
            self._percentOfPeakThroughput = value
        @property
        def statsCollectionEnabled(self) -> bool: ...
        @statsCollectionEnabled.setter
        def statsCollectionEnabled(self, value: bool):
            self._statsCollectionEnabled = value
        @property
        def reservationEnabled(self) -> bool: ...
        @reservationEnabled.setter
        def reservationEnabled(self, value: bool):
            self._reservationEnabled = value
        @property
        def statsAggregationDisabled(self) -> bool: ...
        @statsAggregationDisabled.setter
        def statsAggregationDisabled(self, value: bool):
            self._statsAggregationDisabled = value
        @property
        def reservableIopsThreshold(self) -> int: ...
        @reservableIopsThreshold.setter
        def reservableIopsThreshold(self, value: int):
            self._reservableIopsThreshold = value


    class IORMConfigOption(vmodl.DynamicData):
        @property
        def enabledOption(self) -> option.BoolOption: ...
        @enabledOption.setter
        def enabledOption(self, value: option.BoolOption):
            self._enabledOption = value
        @property
        def congestionThresholdOption(self) -> option.IntOption: ...
        @congestionThresholdOption.setter
        def congestionThresholdOption(self, value: option.IntOption):
            self._congestionThresholdOption = value
        @property
        def statsCollectionEnabledOption(self) -> option.BoolOption: ...
        @statsCollectionEnabledOption.setter
        def statsCollectionEnabledOption(self, value: option.BoolOption):
            self._statsCollectionEnabledOption = value
        @property
        def reservationEnabledOption(self) -> option.BoolOption: ...
        @reservationEnabledOption.setter
        def reservationEnabledOption(self, value: option.BoolOption):
            self._reservationEnabledOption = value


    class IORMConfigSpec(vmodl.DynamicData):
        @property
        def enabled(self) -> bool: ...
        @enabled.setter
        def enabled(self, value: bool):
            self._enabled = value
        @property
        def congestionThresholdMode(self) -> str: ...
        @congestionThresholdMode.setter
        def congestionThresholdMode(self, value: str):
            self._congestionThresholdMode = value
        @property
        def congestionThreshold(self) -> int: ...
        @congestionThreshold.setter
        def congestionThreshold(self, value: int):
            self._congestionThreshold = value
        @property
        def percentOfPeakThroughput(self) -> int: ...
        @percentOfPeakThroughput.setter
        def percentOfPeakThroughput(self, value: int):
            self._percentOfPeakThroughput = value
        @property
        def statsCollectionEnabled(self) -> bool: ...
        @statsCollectionEnabled.setter
        def statsCollectionEnabled(self, value: bool):
            self._statsCollectionEnabled = value
        @property
        def reservationEnabled(self) -> bool: ...
        @reservationEnabled.setter
        def reservationEnabled(self, value: bool):
            self._reservationEnabled = value
        @property
        def statsAggregationDisabled(self) -> bool: ...
        @statsAggregationDisabled.setter
        def statsAggregationDisabled(self, value: bool):
            self._statsAggregationDisabled = value
        @property
        def reservableIopsThreshold(self) -> int: ...
        @reservableIopsThreshold.setter
        def reservableIopsThreshold(self, value: int):
            self._reservableIopsThreshold = value


    class PodStorageDrsEntry(vmodl.DynamicData):
        @property
        def storageDrsConfig(self) -> storageDrs.ConfigInfo: ...
        @storageDrsConfig.setter
        def storageDrsConfig(self, value: storageDrs.ConfigInfo):
            self._storageDrsConfig = value
        @property
        def recommendation(self) -> List[cluster.Recommendation]: ...
        @recommendation.setter
        def recommendation(self, value: List[cluster.Recommendation]):
            self._recommendation = value
        @property
        def drsFault(self) -> List[cluster.DrsFaults]: ...
        @drsFault.setter
        def drsFault(self, value: List[cluster.DrsFaults]):
            self._drsFault = value
        @property
        def actionHistory(self) -> List[cluster.ActionHistory]: ...
        @actionHistory.setter
        def actionHistory(self, value: List[cluster.ActionHistory]):
            self._actionHistory = value


    class StoragePerformanceSummary(vmodl.DynamicData):
        @property
        def interval(self) -> int: ...
        @interval.setter
        def interval(self, value: int):
            self._interval = value
        @property
        def percentile(self) -> List[int]: ...
        @percentile.setter
        def percentile(self, value: List[int]):
            self._percentile = value
        @property
        def datastoreReadLatency(self) -> List[double]: ...
        @datastoreReadLatency.setter
        def datastoreReadLatency(self, value: List[double]):
            self._datastoreReadLatency = value
        @property
        def datastoreWriteLatency(self) -> List[double]: ...
        @datastoreWriteLatency.setter
        def datastoreWriteLatency(self, value: List[double]):
            self._datastoreWriteLatency = value
        @property
        def datastoreVmLatency(self) -> List[double]: ...
        @datastoreVmLatency.setter
        def datastoreVmLatency(self, value: List[double]):
            self._datastoreVmLatency = value
        @property
        def datastoreReadIops(self) -> List[double]: ...
        @datastoreReadIops.setter
        def datastoreReadIops(self, value: List[double]):
            self._datastoreReadIops = value
        @property
        def datastoreWriteIops(self) -> List[double]: ...
        @datastoreWriteIops.setter
        def datastoreWriteIops(self, value: List[double]):
            self._datastoreWriteIops = value
        @property
        def siocActivityDuration(self) -> int: ...
        @siocActivityDuration.setter
        def siocActivityDuration(self, value: int):
            self._siocActivityDuration = value


    class StorageProfileStatistics(vmodl.DynamicData):
        @property
        def profileId(self) -> str: ...
        @profileId.setter
        def profileId(self, value: str):
            self._profileId = value
        @property
        def totalSpaceMB(self) -> long: ...
        @totalSpaceMB.setter
        def totalSpaceMB(self, value: long):
            self._totalSpaceMB = value
        @property
        def usedSpaceMB(self) -> long: ...
        @usedSpaceMB.setter
        def usedSpaceMB(self, value: long):
            self._usedSpaceMB = value


    class CongestionThresholdMode(Enum):
        automatic = "automatic"
        manual = "manual"


class Task(ExtensibleManagedObject):
    @property
    def info(self) -> TaskInfo: ...
    def Cancel(self) -> NoneType: ...
    def UpdateProgress(self, percentDone: int) -> NoneType: ...
    def SetState(self, state: TaskInfo.State | Literal['queued', 'running', 'success', 'error'], result: object, fault: vmodl.MethodFault) -> NoneType: ...
    def UpdateDescription(self, description: vmodl.LocalizableMessage) -> NoneType: ...


class TaskHistoryCollector(HistoryCollector):
    @property
    def latestPage(self) -> List[TaskInfo]: ...
    def ReadNext(self, maxCount: int) -> List[TaskInfo]: ...
    def ReadPrev(self, maxCount: int) -> List[TaskInfo]: ...


class TaskManager(ManagedObject):
    @property
    def recentTask(self) -> List[Task]: ...
    @property
    def description(self) -> TaskDescription: ...
    @property
    def maxCollector(self) -> int: ...
    def CreateCollector(self, filter: TaskFilterSpec) -> TaskHistoryCollector: ...
    def CreateTask(self, obj: ManagedObject, taskTypeId: str, initiatedBy: str, cancelable: bool, parentTaskKey: str, activationId: str) -> TaskInfo: ...


class UserDirectory(ManagedObject):
    @property
    def domainList(self) -> List[str]: ...
    def RetrieveUserGroups(self, domain: str, searchStr: str, belongsToGroup: str, belongsToUser: str, exactMatch: bool, findUsers: bool, findGroups: bool) -> List[UserSearchResult]: ...


class VirtualApp(ResourcePool):
    @property
    def parentFolder(self) -> Folder: ...
    @property
    def datastore(self) -> List[Datastore]: ...
    @property
    def network(self) -> List[Network]: ...
    @property
    def vAppConfig(self) -> vApp.VAppConfigInfo: ...
    @property
    def parentVApp(self) -> ManagedEntity: ...
    @property
    def childLink(self) -> List[VirtualApp.LinkInfo]: ...
    def UpdateVAppConfig(self, spec: vApp.VAppConfigSpec) -> NoneType: ...
    def UpdateLinkedChildren(self, addChangeSet: List[VirtualApp.LinkInfo], removeSet: List[ManagedEntity]) -> NoneType: ...
    def Clone(self, name: str, target: ResourcePool, spec: vApp.CloneSpec) -> Task: ...
    def ExportVApp(self) -> HttpNfcLease: ...
    def PowerOn(self) -> Task: ...
    def PowerOff(self, force: bool) -> Task: ...
    def Suspend(self) -> Task: ...
    def Unregister(self) -> Task: ...


    class LinkInfo(vmodl.DynamicData):
        @property
        def key(self) -> ManagedEntity: ...
        @key.setter
        def key(self, value: ManagedEntity):
            self._key = value
        @property
        def destroyWithParent(self) -> bool: ...
        @destroyWithParent.setter
        def destroyWithParent(self, value: bool):
            self._destroyWithParent = value


    class Summary(ResourcePool.Summary):
        @property
        def product(self) -> vApp.ProductInfo: ...
        @product.setter
        def product(self, value: vApp.ProductInfo):
            self._product = value
        @property
        def vAppState(self) -> VirtualApp.VAppState | Literal['started', 'stopped', 'starting', 'stopping']: ...
        @vAppState.setter
        def vAppState(self, value: VirtualApp.VAppState | Literal['started', 'stopped', 'starting', 'stopping']):
            self._vAppState = value
        @property
        def suspended(self) -> bool: ...
        @suspended.setter
        def suspended(self, value: bool):
            self._suspended = value
        @property
        def installBootRequired(self) -> bool: ...
        @installBootRequired.setter
        def installBootRequired(self, value: bool):
            self._installBootRequired = value
        @property
        def instanceUuid(self) -> str: ...
        @instanceUuid.setter
        def instanceUuid(self, value: str):
            self._instanceUuid = value


    class VAppState(Enum):
        started = "started"
        stopped = "stopped"
        starting = "starting"
        stopping = "stopping"


class VirtualDiskManager(ManagedObject):
    def CreateVirtualDisk(self, name: str, datacenter: Datacenter, spec: VirtualDiskManager.VirtualDiskSpec) -> Task: ...
    def DeleteVirtualDisk(self, name: str, datacenter: Datacenter) -> Task: ...
    def MoveVirtualDisk(self, sourceName: str, sourceDatacenter: Datacenter, destName: str, destDatacenter: Datacenter, force: bool, profile: List[vm.ProfileSpec]) -> Task: ...
    def CopyVirtualDisk(self, sourceName: str, sourceDatacenter: Datacenter, destName: str, destDatacenter: Datacenter, destSpec: VirtualDiskManager.VirtualDiskSpec, force: bool) -> Task: ...
    def ExtendVirtualDisk(self, name: str, datacenter: Datacenter, newCapacityKb: long, eagerZero: bool) -> Task: ...
    def QueryVirtualDiskFragmentation(self, name: str, datacenter: Datacenter) -> int: ...
    def DefragmentVirtualDisk(self, name: str, datacenter: Datacenter) -> Task: ...
    def ShrinkVirtualDisk(self, name: str, datacenter: Datacenter, copy: bool) -> Task: ...
    def InflateVirtualDisk(self, name: str, datacenter: Datacenter) -> Task: ...
    def EagerZeroVirtualDisk(self, name: str, datacenter: Datacenter) -> Task: ...
    def ZeroFillVirtualDisk(self, name: str, datacenter: Datacenter) -> Task: ...
    def SetVirtualDiskUuid(self, name: str, datacenter: Datacenter, uuid: str) -> NoneType: ...
    def QueryVirtualDiskUuid(self, name: str, datacenter: Datacenter) -> str: ...
    def QueryVirtualDiskGeometry(self, name: str, datacenter: Datacenter) -> host.DiskDimensions.Chs: ...
    def ImportUnmanagedSnapshot(self, vdisk: str, datacenter: Datacenter, vvolId: str) -> NoneType: ...
    def ReleaseManagedSnapshot(self, vdisk: str, datacenter: Datacenter) -> NoneType: ...


    class DeviceBackedVirtualDiskSpec(VirtualDiskManager.VirtualDiskSpec):
        @property
        def device(self) -> str: ...
        @device.setter
        def device(self, value: str):
            self._device = value


    class FileBackedVirtualDiskSpec(VirtualDiskManager.VirtualDiskSpec):
        @property
        def capacityKb(self) -> long: ...
        @capacityKb.setter
        def capacityKb(self, value: long):
            self._capacityKb = value
        @property
        def profile(self) -> List[vm.ProfileSpec]: ...
        @profile.setter
        def profile(self, value: List[vm.ProfileSpec]):
            self._profile = value
        @property
        def crypto(self) -> encryption.CryptoSpec: ...
        @crypto.setter
        def crypto(self, value: encryption.CryptoSpec):
            self._crypto = value


    class SeSparseVirtualDiskSpec(VirtualDiskManager.FileBackedVirtualDiskSpec):
        @property
        def grainSizeKb(self) -> int: ...
        @grainSizeKb.setter
        def grainSizeKb(self, value: int):
            self._grainSizeKb = value


    class VirtualDiskSpec(vmodl.DynamicData):
        @property
        def diskType(self) -> str: ...
        @diskType.setter
        def diskType(self, value: str):
            self._diskType = value
        @property
        def adapterType(self) -> str: ...
        @adapterType.setter
        def adapterType(self, value: str):
            self._adapterType = value


    class VirtualDiskAdapterType(Enum):
        ide = "ide"
        busLogic = "busLogic"
        lsiLogic = "lsiLogic"


    class VirtualDiskType(Enum):
        preallocated = "preallocated"
        thin = "thin"
        seSparse = "seSparse"
        rdm = "rdm"
        rdmp = "rdmp"
        raw = "raw"
        delta = "delta"
        sparse2Gb = "sparse2Gb"
        thick2Gb = "thick2Gb"
        eagerZeroedThick = "eagerZeroedThick"
        sparseMonolithic = "sparseMonolithic"
        flatMonolithic = "flatMonolithic"
        thick = "thick"


class VirtualMachine(ManagedEntity):
    @property
    def capability(self) -> vm.Capability: ...
    @property
    def config(self) -> vm.ConfigInfo: ...
    @property
    def layout(self) -> vm.FileLayout: ...
    @property
    def layoutEx(self) -> vm.FileLayoutEx: ...
    @property
    def storage(self) -> vm.StorageInfo: ...
    @property
    def environmentBrowser(self) -> EnvironmentBrowser: ...
    @property
    def resourcePool(self) -> ResourcePool: ...
    @property
    def parentVApp(self) -> ManagedEntity: ...
    @property
    def resourceConfig(self) -> ResourceConfigSpec: ...
    @property
    def runtime(self) -> vm.RuntimeInfo: ...
    @property
    def guest(self) -> vm.GuestInfo: ...
    @property
    def summary(self) -> vm.Summary: ...
    @property
    def datastore(self) -> List[Datastore]: ...
    @property
    def network(self) -> List[Network]: ...
    @property
    def snapshot(self) -> vm.SnapshotInfo: ...
    @property
    def rootSnapshot(self) -> List[vm.Snapshot]: ...
    @property
    def guestHeartbeatStatus(self) -> ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']: ...
    def RefreshStorageInfo(self) -> NoneType: ...
    def CreateSnapshot(self, name: str, description: str, memory: bool, quiesce: bool) -> Task: ...
    def CreateSnapshotEx(self, name: str, description: str, memory: bool, quiesceSpec: vm.GuestQuiesceSpec) -> Task: ...
    def RevertToCurrentSnapshot(self, host: HostSystem, suppressPowerOn: bool) -> Task: ...
    def RemoveAllSnapshots(self, consolidate: bool) -> Task: ...
    def ConsolidateDisks(self) -> Task: ...
    def EstimateStorageRequirementForConsolidate(self) -> Task: ...
    def Reconfigure(self, spec: vm.ConfigSpec) -> Task: ...
    def UpgradeVirtualHardware(self, version: str) -> Task: ...
    def ExtractOvfEnvironment(self) -> str: ...
    def PowerOn(self, host: HostSystem) -> Task: ...
    def PowerOff(self) -> Task: ...
    def Suspend(self) -> Task: ...
    def Reset(self) -> Task: ...
    def ShutdownGuest(self) -> NoneType: ...
    def RebootGuest(self) -> NoneType: ...
    def StandbyGuest(self) -> NoneType: ...
    def Answer(self, questionId: str, answerChoice: str) -> NoneType: ...
    def Customize(self, spec: vm.customization.Specification) -> Task: ...
    def CheckCustomizationSpec(self, spec: vm.customization.Specification) -> NoneType: ...
    def Migrate(self, pool: ResourcePool, host: HostSystem, priority: VirtualMachine.MovePriority | Literal['lowPriority', 'highPriority', 'defaultPriority'], state: VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended']) -> Task: ...
    def Relocate(self, spec: vm.RelocateSpec, priority: VirtualMachine.MovePriority | Literal['lowPriority', 'highPriority', 'defaultPriority']) -> Task: ...
    def Clone(self, folder: Folder, name: str, spec: vm.CloneSpec) -> Task: ...
    def InstantClone(self, spec: vm.InstantCloneSpec) -> Task: ...
    def ExportVm(self) -> HttpNfcLease: ...
    def MarkAsTemplate(self) -> NoneType: ...
    def MarkAsVirtualMachine(self, pool: ResourcePool, host: HostSystem) -> NoneType: ...
    def Unregister(self) -> NoneType: ...
    def ResetGuestInformation(self) -> NoneType: ...
    def MountToolsInstaller(self) -> NoneType: ...
    def UnmountToolsInstaller(self) -> NoneType: ...
    def UpgradeTools(self, installerOptions: str) -> Task: ...
    def AcquireMksTicket(self) -> VirtualMachine.MksTicket: ...
    def QueryConnections(self) -> List[VirtualMachine.Connection]: ...
    def DropConnections(self, listOfConnections: List[VirtualMachine.Connection]) -> bool: ...
    def AcquireTicket(self, ticketType: str) -> VirtualMachine.Ticket: ...
    def SetScreenResolution(self, width: int, height: int) -> NoneType: ...
    def DefragmentAllDisks(self) -> NoneType: ...
    def CreateSecondary(self, host: HostSystem) -> Task: ...
    def CreateSecondaryEx(self, host: HostSystem, spec: vm.FaultToleranceConfigSpec) -> Task: ...
    def TurnOffFaultTolerance(self) -> Task: ...
    def MakePrimary(self, vm: VirtualMachine) -> Task: ...
    def TerminateFaultTolerantVM(self, vm: VirtualMachine) -> Task: ...
    def DisableSecondary(self, vm: VirtualMachine) -> Task: ...
    def EnableSecondary(self, vm: VirtualMachine, host: HostSystem) -> Task: ...
    def SetDisplayTopology(self, displays: List[VirtualMachine.DisplayTopology]) -> NoneType: ...
    def StartRecording(self, name: str, description: str) -> Task: ...
    def StopRecording(self) -> Task: ...
    def StartReplaying(self, replaySnapshot: vm.Snapshot) -> Task: ...
    def StopReplaying(self) -> Task: ...
    def PromoteDisks(self, unlink: bool, disks: List[vm.device.VirtualDisk]) -> Task: ...
    def CreateScreenshot(self) -> Task: ...
    def PutUsbScanCodes(self, spec: vm.UsbScanCodeSpec) -> int: ...
    def QueryChangedDiskAreas(self, snapshot: vm.Snapshot, deviceKey: int, startOffset: long, changeId: str) -> VirtualMachine.DiskChangeInfo: ...
    def QueryUnownedFiles(self) -> List[str]: ...
    def ReloadFromPath(self, configurationPath: str) -> Task: ...
    def QueryFaultToleranceCompatibility(self) -> List[vmodl.MethodFault]: ...
    def QueryFaultToleranceCompatibilityEx(self, forLegacyFt: bool) -> List[vmodl.MethodFault]: ...
    def Terminate(self) -> NoneType: ...
    def SendNMI(self) -> NoneType: ...
    def AttachDisk(self, diskId: vslm.ID, datastore: Datastore, controllerKey: int, unitNumber: int) -> Task: ...
    def DetachDisk(self, diskId: vslm.ID) -> Task: ...
    def ApplyEvcMode(self, mask: List[host.FeatureMask], completeMasks: bool) -> Task: ...
    def CryptoUnlock(self) -> Task: ...


    class Connection(vmodl.DynamicData):
        @property
        def label(self) -> str: ...
        @label.setter
        def label(self, value: str):
            self._label = value
        @property
        def client(self) -> str: ...
        @client.setter
        def client(self, value: str):
            self._client = value
        @property
        def userName(self) -> str: ...
        @userName.setter
        def userName(self, value: str):
            self._userName = value


    class DiskChangeInfo(vmodl.DynamicData):
        @property
        def startOffset(self) -> long: ...
        @startOffset.setter
        def startOffset(self, value: long):
            self._startOffset = value
        @property
        def length(self) -> long: ...
        @length.setter
        def length(self, value: long):
            self._length = value
        @property
        def changedArea(self) -> List[VirtualMachine.DiskChangeInfo.DiskChangeExtent]: ...
        @changedArea.setter
        def changedArea(self, value: List[VirtualMachine.DiskChangeInfo.DiskChangeExtent]):
            self._changedArea = value


        class DiskChangeExtent(vmodl.DynamicData):
            @property
            def start(self) -> long: ...
            @start.setter
            def start(self, value: long):
                self._start = value
            @property
            def length(self) -> long: ...
            @length.setter
            def length(self, value: long):
                self._length = value


    class DisplayTopology(vmodl.DynamicData):
        @property
        def x(self) -> int: ...
        @x.setter
        def x(self, value: int):
            self._x = value
        @property
        def y(self) -> int: ...
        @y.setter
        def y(self, value: int):
            self._y = value
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


    class MksConnection(VirtualMachine.Connection): ...


    class MksTicket(vmodl.DynamicData):
        @property
        def ticket(self) -> str: ...
        @ticket.setter
        def ticket(self, value: str):
            self._ticket = value
        @property
        def cfgFile(self) -> str: ...
        @cfgFile.setter
        def cfgFile(self, value: str):
            self._cfgFile = value
        @property
        def host(self) -> str: ...
        @host.setter
        def host(self, value: str):
            self._host = value
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


    class StorageRequirement(vmodl.DynamicData):
        @property
        def datastore(self) -> Datastore: ...
        @datastore.setter
        def datastore(self, value: Datastore):
            self._datastore = value
        @property
        def freeSpaceRequiredInKb(self) -> long: ...
        @freeSpaceRequiredInKb.setter
        def freeSpaceRequiredInKb(self, value: long):
            self._freeSpaceRequiredInKb = value


    class Ticket(vmodl.DynamicData):
        @property
        def ticket(self) -> str: ...
        @ticket.setter
        def ticket(self, value: str):
            self._ticket = value
        @property
        def cfgFile(self) -> str: ...
        @cfgFile.setter
        def cfgFile(self, value: str):
            self._cfgFile = value
        @property
        def host(self) -> str: ...
        @host.setter
        def host(self, value: str):
            self._host = value
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
        def certThumbprintList(self) -> List[vm.CertThumbprint]: ...
        @certThumbprintList.setter
        def certThumbprintList(self, value: List[vm.CertThumbprint]):
            self._certThumbprintList = value
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value


    class WipeResult(vmodl.DynamicData):
        @property
        def diskId(self) -> int: ...
        @diskId.setter
        def diskId(self, value: int):
            self._diskId = value
        @property
        def shrinkableDiskSpace(self) -> long: ...
        @shrinkableDiskSpace.setter
        def shrinkableDiskSpace(self, value: long):
            self._shrinkableDiskSpace = value


    class AppHeartbeatStatusType(Enum):
        appStatusGray = "appStatusGray"
        appStatusGreen = "appStatusGreen"
        appStatusRed = "appStatusRed"


    class FaultToleranceState(Enum):
        notConfigured = "notConfigured"
        disabled = "disabled"
        enabled = "enabled"
        needSecondary = "needSecondary"
        starting = "starting"
        running = "running"


    class FaultToleranceType(Enum):
        unset = "unset"
        recordReplay = "recordReplay"
        checkpointing = "checkpointing"


    class MovePriority(Enum):
        lowPriority = "lowPriority"
        highPriority = "highPriority"
        defaultPriority = "defaultPriority"


    class NeedSecondaryReason(Enum):
        initializing = "initializing"
        divergence = "divergence"
        lostConnection = "lostConnection"
        partialHardwareFailure = "partialHardwareFailure"
        userAction = "userAction"
        checkpointError = "checkpointError"
        other = "other"


    class RecordReplayState(Enum):
        recording = "recording"
        replaying = "replaying"
        inactive = "inactive"


class VirtualizationManager(ManagedObject): ...


class VsanUpgradeSystem(ManagedObject):
    def PerformUpgradePreflightCheck(self, cluster: ClusterComputeResource, downgradeFormat: bool) -> VsanUpgradeSystem.PreflightCheckResult: ...
    def QueryUpgradeStatus(self, cluster: ClusterComputeResource) -> VsanUpgradeSystem.UpgradeStatus: ...
    def PerformUpgrade(self, cluster: ClusterComputeResource, performObjectUpgrade: bool, downgradeFormat: bool, allowReducedRedundancy: bool, excludeHosts: List[HostSystem]) -> Task: ...


    class APIBrokenIssue(VsanUpgradeSystem.PreflightCheckIssue):
        @property
        def hosts(self) -> List[HostSystem]: ...
        @hosts.setter
        def hosts(self, value: List[HostSystem]):
            self._hosts = value


    class AutoClaimEnabledOnHostsIssue(VsanUpgradeSystem.PreflightCheckIssue):
        @property
        def hosts(self) -> List[HostSystem]: ...
        @hosts.setter
        def hosts(self, value: List[HostSystem]):
            self._hosts = value


    class HostsDisconnectedIssue(VsanUpgradeSystem.PreflightCheckIssue):
        @property
        def hosts(self) -> List[HostSystem]: ...
        @hosts.setter
        def hosts(self, value: List[HostSystem]):
            self._hosts = value


    class MissingHostsInClusterIssue(VsanUpgradeSystem.PreflightCheckIssue):
        @property
        def hosts(self) -> List[HostSystem]: ...
        @hosts.setter
        def hosts(self, value: List[HostSystem]):
            self._hosts = value


    class NetworkPartitionInfo(vmodl.DynamicData):
        @property
        def hosts(self) -> List[HostSystem]: ...
        @hosts.setter
        def hosts(self, value: List[HostSystem]):
            self._hosts = value


    class NetworkPartitionIssue(VsanUpgradeSystem.PreflightCheckIssue):
        @property
        def partitions(self) -> List[VsanUpgradeSystem.NetworkPartitionInfo]: ...
        @partitions.setter
        def partitions(self, value: List[VsanUpgradeSystem.NetworkPartitionInfo]):
            self._partitions = value


    class NotEnoughFreeCapacityIssue(VsanUpgradeSystem.PreflightCheckIssue):
        @property
        def reducedRedundancyUpgradePossible(self) -> bool: ...
        @reducedRedundancyUpgradePossible.setter
        def reducedRedundancyUpgradePossible(self, value: bool):
            self._reducedRedundancyUpgradePossible = value


    class PreflightCheckIssue(vmodl.DynamicData):
        @property
        def msg(self) -> str: ...
        @msg.setter
        def msg(self, value: str):
            self._msg = value


    class PreflightCheckResult(vmodl.DynamicData):
        @property
        def issues(self) -> List[VsanUpgradeSystem.PreflightCheckIssue]: ...
        @issues.setter
        def issues(self, value: List[VsanUpgradeSystem.PreflightCheckIssue]):
            self._issues = value
        @property
        def diskMappingToRestore(self) -> vsan.host.DiskMapping: ...
        @diskMappingToRestore.setter
        def diskMappingToRestore(self, value: vsan.host.DiskMapping):
            self._diskMappingToRestore = value


    class RogueHostsInClusterIssue(VsanUpgradeSystem.PreflightCheckIssue):
        @property
        def uuids(self) -> List[str]: ...
        @uuids.setter
        def uuids(self, value: List[str]):
            self._uuids = value


    class UpgradeHistoryDiskGroupOp(VsanUpgradeSystem.UpgradeHistoryItem):
        @property
        def operation(self) -> str: ...
        @operation.setter
        def operation(self, value: str):
            self._operation = value
        @property
        def diskMapping(self) -> vsan.host.DiskMapping: ...
        @diskMapping.setter
        def diskMapping(self, value: vsan.host.DiskMapping):
            self._diskMapping = value


    class UpgradeHistoryItem(vmodl.DynamicData):
        @property
        def timestamp(self) -> datetime: ...
        @timestamp.setter
        def timestamp(self, value: datetime):
            self._timestamp = value
        @property
        def host(self) -> HostSystem: ...
        @host.setter
        def host(self, value: HostSystem):
            self._host = value
        @property
        def message(self) -> str: ...
        @message.setter
        def message(self, value: str):
            self._message = value
        @property
        def task(self) -> Task: ...
        @task.setter
        def task(self, value: Task):
            self._task = value


    class UpgradeHistoryPreflightFail(VsanUpgradeSystem.UpgradeHistoryItem):
        @property
        def preflightResult(self) -> VsanUpgradeSystem.PreflightCheckResult: ...
        @preflightResult.setter
        def preflightResult(self, value: VsanUpgradeSystem.PreflightCheckResult):
            self._preflightResult = value


    class UpgradeStatus(vmodl.DynamicData):
        @property
        def inProgress(self) -> bool: ...
        @inProgress.setter
        def inProgress(self, value: bool):
            self._inProgress = value
        @property
        def history(self) -> List[VsanUpgradeSystem.UpgradeHistoryItem]: ...
        @history.setter
        def history(self, value: List[VsanUpgradeSystem.UpgradeHistoryItem]):
            self._history = value
        @property
        def aborted(self) -> bool: ...
        @aborted.setter
        def aborted(self, value: bool):
            self._aborted = value
        @property
        def completed(self) -> bool: ...
        @completed.setter
        def completed(self, value: bool):
            self._completed = value
        @property
        def progress(self) -> int: ...
        @progress.setter
        def progress(self, value: int):
            self._progress = value


    class V2ObjectsPresentDuringDowngradeIssue(VsanUpgradeSystem.PreflightCheckIssue):
        @property
        def uuids(self) -> List[str]: ...
        @uuids.setter
        def uuids(self, value: List[str]):
            self._uuids = value


    class WrongEsxVersionIssue(VsanUpgradeSystem.PreflightCheckIssue):
        @property
        def hosts(self) -> List[HostSystem]: ...
        @hosts.setter
        def hosts(self, value: List[HostSystem]):
            self._hosts = value


    class UpgradeHistoryDiskGroupOpType(Enum):
        add = "add"
        remove = "remove"


class AboutInfo(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def fullName(self) -> str: ...
    @fullName.setter
    def fullName(self, value: str):
        self._fullName = value
    @property
    def vendor(self) -> str: ...
    @vendor.setter
    def vendor(self, value: str):
        self._vendor = value
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value
    @property
    def patchLevel(self) -> str: ...
    @patchLevel.setter
    def patchLevel(self, value: str):
        self._patchLevel = value
    @property
    def build(self) -> str: ...
    @build.setter
    def build(self, value: str):
        self._build = value
    @property
    def localeVersion(self) -> str: ...
    @localeVersion.setter
    def localeVersion(self, value: str):
        self._localeVersion = value
    @property
    def localeBuild(self) -> str: ...
    @localeBuild.setter
    def localeBuild(self, value: str):
        self._localeBuild = value
    @property
    def osType(self) -> str: ...
    @osType.setter
    def osType(self, value: str):
        self._osType = value
    @property
    def productLineId(self) -> str: ...
    @productLineId.setter
    def productLineId(self, value: str):
        self._productLineId = value
    @property
    def apiType(self) -> str: ...
    @apiType.setter
    def apiType(self, value: str):
        self._apiType = value
    @property
    def apiVersion(self) -> str: ...
    @apiVersion.setter
    def apiVersion(self, value: str):
        self._apiVersion = value
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value
    @property
    def licenseProductName(self) -> str: ...
    @licenseProductName.setter
    def licenseProductName(self, value: str):
        self._licenseProductName = value
    @property
    def licenseProductVersion(self) -> str: ...
    @licenseProductVersion.setter
    def licenseProductVersion(self, value: str):
        self._licenseProductVersion = value


class AuthorizationDescription(vmodl.DynamicData):
    @property
    def privilege(self) -> List[ElementDescription]: ...
    @privilege.setter
    def privilege(self, value: List[ElementDescription]):
        self._privilege = value
    @property
    def privilegeGroup(self) -> List[ElementDescription]: ...
    @privilegeGroup.setter
    def privilegeGroup(self, value: List[ElementDescription]):
        self._privilegeGroup = value


class BatchResult(vmodl.DynamicData):
    @property
    def result(self) -> str: ...
    @result.setter
    def result(self, value: str):
        self._result = value
    @property
    def hostKey(self) -> str: ...
    @hostKey.setter
    def hostKey(self, value: str):
        self._hostKey = value
    @property
    def ds(self) -> Datastore: ...
    @ds.setter
    def ds(self, value: Datastore):
        self._ds = value
    @property
    def fault(self) -> vmodl.MethodFault: ...
    @fault.setter
    def fault(self, value: vmodl.MethodFault):
        self._fault = value


    class Result(Enum):
        success = "success"
        fail = "fail"


class BoolPolicy(InheritablePolicy):
    @property
    def value(self) -> bool: ...
    @value.setter
    def value(self, value: bool):
        self._value = value


class Capability(vmodl.DynamicData):
    @property
    def provisioningSupported(self) -> bool: ...
    @provisioningSupported.setter
    def provisioningSupported(self, value: bool):
        self._provisioningSupported = value
    @property
    def multiHostSupported(self) -> bool: ...
    @multiHostSupported.setter
    def multiHostSupported(self, value: bool):
        self._multiHostSupported = value
    @property
    def userShellAccessSupported(self) -> bool: ...
    @userShellAccessSupported.setter
    def userShellAccessSupported(self, value: bool):
        self._userShellAccessSupported = value
    @property
    def supportedEVCMode(self) -> List[EVCMode]: ...
    @supportedEVCMode.setter
    def supportedEVCMode(self, value: List[EVCMode]):
        self._supportedEVCMode = value
    @property
    def supportedEVCGraphicsMode(self) -> List[FeatureEVCMode]: ...
    @supportedEVCGraphicsMode.setter
    def supportedEVCGraphicsMode(self, value: List[FeatureEVCMode]):
        self._supportedEVCGraphicsMode = value
    @property
    def networkBackupAndRestoreSupported(self) -> bool: ...
    @networkBackupAndRestoreSupported.setter
    def networkBackupAndRestoreSupported(self, value: bool):
        self._networkBackupAndRestoreSupported = value
    @property
    def ftDrsWithoutEvcSupported(self) -> bool: ...
    @ftDrsWithoutEvcSupported.setter
    def ftDrsWithoutEvcSupported(self, value: bool):
        self._ftDrsWithoutEvcSupported = value
    @property
    def hciWorkflowSupported(self) -> bool: ...
    @hciWorkflowSupported.setter
    def hciWorkflowSupported(self, value: bool):
        self._hciWorkflowSupported = value
    @property
    def computePolicyVersion(self) -> int: ...
    @computePolicyVersion.setter
    def computePolicyVersion(self, value: int):
        self._computePolicyVersion = value
    @property
    def clusterPlacementSupported(self) -> bool: ...
    @clusterPlacementSupported.setter
    def clusterPlacementSupported(self, value: bool):
        self._clusterPlacementSupported = value
    @property
    def lifecycleManagementSupported(self) -> bool: ...
    @lifecycleManagementSupported.setter
    def lifecycleManagementSupported(self, value: bool):
        self._lifecycleManagementSupported = value
    @property
    def hostSeedingSupported(self) -> bool: ...
    @hostSeedingSupported.setter
    def hostSeedingSupported(self, value: bool):
        self._hostSeedingSupported = value
    @property
    def scalableSharesSupported(self) -> bool: ...
    @scalableSharesSupported.setter
    def scalableSharesSupported(self, value: bool):
        self._scalableSharesSupported = value
    @property
    def hadcsSupported(self) -> bool: ...
    @hadcsSupported.setter
    def hadcsSupported(self, value: bool):
        self._hadcsSupported = value
    @property
    def configMgmtSupported(self) -> bool: ...
    @configMgmtSupported.setter
    def configMgmtSupported(self, value: bool):
        self._configMgmtSupported = value


class CustomizationSpecInfo(vmodl.DynamicData):
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
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def changeVersion(self) -> str: ...
    @changeVersion.setter
    def changeVersion(self, value: str):
        self._changeVersion = value
    @property
    def lastUpdateTime(self) -> datetime: ...
    @lastUpdateTime.setter
    def lastUpdateTime(self, value: datetime):
        self._lastUpdateTime = value


class CustomizationSpecItem(vmodl.DynamicData):
    @property
    def info(self) -> CustomizationSpecInfo: ...
    @info.setter
    def info(self, value: CustomizationSpecInfo):
        self._info = value
    @property
    def spec(self) -> vm.customization.Specification: ...
    @spec.setter
    def spec(self, value: vm.customization.Specification):
        self._spec = value


class Description(vmodl.DynamicData):
    @property
    def label(self) -> str: ...
    @label.setter
    def label(self, value: str):
        self._label = value
    @property
    def summary(self) -> str: ...
    @summary.setter
    def summary(self, value: str):
        self._summary = value


class DesiredSoftwareSpec(vmodl.DynamicData):
    @property
    def baseImageSpec(self) -> DesiredSoftwareSpec.BaseImageSpec: ...
    @baseImageSpec.setter
    def baseImageSpec(self, value: DesiredSoftwareSpec.BaseImageSpec):
        self._baseImageSpec = value
    @property
    def vendorAddOnSpec(self) -> DesiredSoftwareSpec.VendorAddOnSpec: ...
    @vendorAddOnSpec.setter
    def vendorAddOnSpec(self, value: DesiredSoftwareSpec.VendorAddOnSpec):
        self._vendorAddOnSpec = value
    @property
    def components(self) -> List[DesiredSoftwareSpec.ComponentSpec]: ...
    @components.setter
    def components(self, value: List[DesiredSoftwareSpec.ComponentSpec]):
        self._components = value


    class BaseImageSpec(vmodl.DynamicData):
        @property
        def version(self) -> str: ...
        @version.setter
        def version(self, value: str):
            self._version = value


    class ComponentSpec(vmodl.DynamicData):
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


    class VendorAddOnSpec(vmodl.DynamicData):
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


class EVCMode(ElementDescription):
    @property
    def guaranteedCPUFeatures(self) -> List[host.CpuIdInfo]: ...
    @guaranteedCPUFeatures.setter
    def guaranteedCPUFeatures(self, value: List[host.CpuIdInfo]):
        self._guaranteedCPUFeatures = value
    @property
    def featureCapability(self) -> List[host.FeatureCapability]: ...
    @featureCapability.setter
    def featureCapability(self, value: List[host.FeatureCapability]):
        self._featureCapability = value
    @property
    def featureMask(self) -> List[host.FeatureMask]: ...
    @featureMask.setter
    def featureMask(self, value: List[host.FeatureMask]):
        self._featureMask = value
    @property
    def featureRequirement(self) -> List[vm.FeatureRequirement]: ...
    @featureRequirement.setter
    def featureRequirement(self, value: List[vm.FeatureRequirement]):
        self._featureRequirement = value
    @property
    def vendor(self) -> str: ...
    @vendor.setter
    def vendor(self, value: str):
        self._vendor = value
    @property
    def track(self) -> List[str]: ...
    @track.setter
    def track(self, value: List[str]):
        self._track = value
    @property
    def vendorTier(self) -> int: ...
    @vendorTier.setter
    def vendorTier(self, value: int):
        self._vendorTier = value


class ElementDescription(Description):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class EnumDescription(vmodl.DynamicData):
    @property
    def key(self) -> type: ...
    @key.setter
    def key(self, value: type):
        self._key = value
    @property
    def tags(self) -> List[ElementDescription]: ...
    @tags.setter
    def tags(self, value: List[ElementDescription]):
        self._tags = value


class ExtendedDescription(Description):
    @property
    def messageCatalogKeyPrefix(self) -> str: ...
    @messageCatalogKeyPrefix.setter
    def messageCatalogKeyPrefix(self, value: str):
        self._messageCatalogKeyPrefix = value
    @property
    def messageArg(self) -> List[vmodl.KeyAnyValue]: ...
    @messageArg.setter
    def messageArg(self, value: List[vmodl.KeyAnyValue]):
        self._messageArg = value


class ExtendedElementDescription(ElementDescription):
    @property
    def messageCatalogKeyPrefix(self) -> str: ...
    @messageCatalogKeyPrefix.setter
    def messageCatalogKeyPrefix(self, value: str):
        self._messageCatalogKeyPrefix = value
    @property
    def messageArg(self) -> List[vmodl.KeyAnyValue]: ...
    @messageArg.setter
    def messageArg(self, value: List[vmodl.KeyAnyValue]):
        self._messageArg = value


class Extension(vmodl.DynamicData):
    @property
    def description(self) -> Description: ...
    @description.setter
    def description(self, value: Description):
        self._description = value
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def company(self) -> str: ...
    @company.setter
    def company(self, value: str):
        self._company = value
    @property
    def type(self) -> str: ...
    @type.setter
    def type(self, value: str):
        self._type = value
    @property
    def version(self) -> str: ...
    @version.setter
    def version(self, value: str):
        self._version = value
    @property
    def subjectName(self) -> str: ...
    @subjectName.setter
    def subjectName(self, value: str):
        self._subjectName = value
    @property
    def server(self) -> List[Extension.ServerInfo]: ...
    @server.setter
    def server(self, value: List[Extension.ServerInfo]):
        self._server = value
    @property
    def client(self) -> List[Extension.ClientInfo]: ...
    @client.setter
    def client(self, value: List[Extension.ClientInfo]):
        self._client = value
    @property
    def taskList(self) -> List[Extension.TaskTypeInfo]: ...
    @taskList.setter
    def taskList(self, value: List[Extension.TaskTypeInfo]):
        self._taskList = value
    @property
    def eventList(self) -> List[Extension.EventTypeInfo]: ...
    @eventList.setter
    def eventList(self, value: List[Extension.EventTypeInfo]):
        self._eventList = value
    @property
    def faultList(self) -> List[Extension.FaultTypeInfo]: ...
    @faultList.setter
    def faultList(self, value: List[Extension.FaultTypeInfo]):
        self._faultList = value
    @property
    def privilegeList(self) -> List[Extension.PrivilegeInfo]: ...
    @privilegeList.setter
    def privilegeList(self, value: List[Extension.PrivilegeInfo]):
        self._privilegeList = value
    @property
    def resourceList(self) -> List[Extension.ResourceInfo]: ...
    @resourceList.setter
    def resourceList(self, value: List[Extension.ResourceInfo]):
        self._resourceList = value
    @property
    def lastHeartbeatTime(self) -> datetime: ...
    @lastHeartbeatTime.setter
    def lastHeartbeatTime(self, value: datetime):
        self._lastHeartbeatTime = value
    @property
    def healthInfo(self) -> Extension.HealthInfo: ...
    @healthInfo.setter
    def healthInfo(self, value: Extension.HealthInfo):
        self._healthInfo = value
    @property
    def ovfConsumerInfo(self) -> Extension.OvfConsumerInfo: ...
    @ovfConsumerInfo.setter
    def ovfConsumerInfo(self, value: Extension.OvfConsumerInfo):
        self._ovfConsumerInfo = value
    @property
    def extendedProductInfo(self) -> ext.ExtendedProductInfo: ...
    @extendedProductInfo.setter
    def extendedProductInfo(self, value: ext.ExtendedProductInfo):
        self._extendedProductInfo = value
    @property
    def managedEntityInfo(self) -> List[ext.ManagedEntityInfo]: ...
    @managedEntityInfo.setter
    def managedEntityInfo(self, value: List[ext.ManagedEntityInfo]):
        self._managedEntityInfo = value
    @property
    def shownInSolutionManager(self) -> bool: ...
    @shownInSolutionManager.setter
    def shownInSolutionManager(self, value: bool):
        self._shownInSolutionManager = value
    @property
    def solutionManagerInfo(self) -> ext.SolutionManagerInfo: ...
    @solutionManagerInfo.setter
    def solutionManagerInfo(self, value: ext.SolutionManagerInfo):
        self._solutionManagerInfo = value


    class ClientInfo(vmodl.DynamicData):
        @property
        def version(self) -> str: ...
        @version.setter
        def version(self, value: str):
            self._version = value
        @property
        def description(self) -> Description: ...
        @description.setter
        def description(self, value: Description):
            self._description = value
        @property
        def company(self) -> str: ...
        @company.setter
        def company(self, value: str):
            self._company = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value


    class EventTypeInfo(vmodl.DynamicData):
        @property
        def eventID(self) -> str: ...
        @eventID.setter
        def eventID(self, value: str):
            self._eventID = value
        @property
        def eventTypeSchema(self) -> str: ...
        @eventTypeSchema.setter
        def eventTypeSchema(self, value: str):
            self._eventTypeSchema = value


    class FaultTypeInfo(vmodl.DynamicData):
        @property
        def faultID(self) -> str: ...
        @faultID.setter
        def faultID(self, value: str):
            self._faultID = value


    class HealthInfo(vmodl.DynamicData):
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value


    class OvfConsumerInfo(vmodl.DynamicData):
        @property
        def callbackUrl(self) -> str: ...
        @callbackUrl.setter
        def callbackUrl(self, value: str):
            self._callbackUrl = value
        @property
        def sectionType(self) -> List[str]: ...
        @sectionType.setter
        def sectionType(self, value: List[str]):
            self._sectionType = value


    class PrivilegeInfo(vmodl.DynamicData):
        @property
        def privID(self) -> str: ...
        @privID.setter
        def privID(self, value: str):
            self._privID = value
        @property
        def privGroupName(self) -> str: ...
        @privGroupName.setter
        def privGroupName(self, value: str):
            self._privGroupName = value


    class ResourceInfo(vmodl.DynamicData):
        @property
        def locale(self) -> str: ...
        @locale.setter
        def locale(self, value: str):
            self._locale = value
        @property
        def module(self) -> str: ...
        @module.setter
        def module(self, value: str):
            self._module = value
        @property
        def data(self) -> List[KeyValue]: ...
        @data.setter
        def data(self, value: List[KeyValue]):
            self._data = value


    class ServerInfo(vmodl.DynamicData):
        @property
        def url(self) -> str: ...
        @url.setter
        def url(self, value: str):
            self._url = value
        @property
        def description(self) -> Description: ...
        @description.setter
        def description(self, value: Description):
            self._description = value
        @property
        def company(self) -> str: ...
        @company.setter
        def company(self, value: str):
            self._company = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def adminEmail(self) -> List[str]: ...
        @adminEmail.setter
        def adminEmail(self, value: List[str]):
            self._adminEmail = value
        @property
        def serverThumbprint(self) -> str: ...
        @serverThumbprint.setter
        def serverThumbprint(self, value: str):
            self._serverThumbprint = value


    class TaskTypeInfo(vmodl.DynamicData):
        @property
        def taskID(self) -> str: ...
        @taskID.setter
        def taskID(self, value: str):
            self._taskID = value


class FaultsByHost(vmodl.DynamicData):
    @property
    def host(self) -> HostSystem: ...
    @host.setter
    def host(self, value: HostSystem):
        self._host = value
    @property
    def faults(self) -> List[vmodl.MethodFault]: ...
    @faults.setter
    def faults(self, value: List[vmodl.MethodFault]):
        self._faults = value


class FaultsByVM(vmodl.DynamicData):
    @property
    def vm(self) -> VirtualMachine: ...
    @vm.setter
    def vm(self, value: VirtualMachine):
        self._vm = value
    @property
    def faults(self) -> List[vmodl.MethodFault]: ...
    @faults.setter
    def faults(self, value: List[vmodl.MethodFault]):
        self._faults = value


class FeatureEVCMode(ElementDescription):
    @property
    def mask(self) -> List[host.FeatureMask]: ...
    @mask.setter
    def mask(self, value: List[host.FeatureMask]):
        self._mask = value
    @property
    def capability(self) -> List[host.FeatureCapability]: ...
    @capability.setter
    def capability(self, value: List[host.FeatureCapability]):
        self._capability = value
    @property
    def requirement(self) -> List[vm.FeatureRequirement]: ...
    @requirement.setter
    def requirement(self, value: List[vm.FeatureRequirement]):
        self._requirement = value


class HbrManager():


    class ReplicationVmInfo(vmodl.DynamicData):
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value
        @property
        def progressInfo(self) -> HbrManager.ReplicationVmInfo.ProgressInfo: ...
        @progressInfo.setter
        def progressInfo(self, value: HbrManager.ReplicationVmInfo.ProgressInfo):
            self._progressInfo = value
        @property
        def imageId(self) -> str: ...
        @imageId.setter
        def imageId(self, value: str):
            self._imageId = value
        @property
        def lastError(self) -> vmodl.MethodFault: ...
        @lastError.setter
        def lastError(self, value: vmodl.MethodFault):
            self._lastError = value


        class ProgressInfo(vmodl.DynamicData):
            @property
            def progress(self) -> int: ...
            @progress.setter
            def progress(self, value: int):
                self._progress = value
            @property
            def bytesTransferred(self) -> long: ...
            @bytesTransferred.setter
            def bytesTransferred(self, value: long):
                self._bytesTransferred = value
            @property
            def bytesToTransfer(self) -> long: ...
            @bytesToTransfer.setter
            def bytesToTransfer(self, value: long):
                self._bytesToTransfer = value
            @property
            def checksumTotalBytes(self) -> long: ...
            @checksumTotalBytes.setter
            def checksumTotalBytes(self, value: long):
                self._checksumTotalBytes = value
            @property
            def checksumComparedBytes(self) -> long: ...
            @checksumComparedBytes.setter
            def checksumComparedBytes(self, value: long):
                self._checksumComparedBytes = value


        class State(Enum):
            none = "none"
            paused = "paused"
            syncing = "syncing"
            idle = "idle"
            active = "active"
            error = "error"


    class VmReplicationCapability(vmodl.DynamicData):
        @property
        def vm(self) -> VirtualMachine: ...
        @vm.setter
        def vm(self, value: VirtualMachine):
            self._vm = value
        @property
        def supportedQuiesceMode(self) -> str: ...
        @supportedQuiesceMode.setter
        def supportedQuiesceMode(self, value: str):
            self._supportedQuiesceMode = value
        @property
        def compressionSupported(self) -> bool: ...
        @compressionSupported.setter
        def compressionSupported(self, value: bool):
            self._compressionSupported = value
        @property
        def maxSupportedSourceDiskCapacity(self) -> long: ...
        @maxSupportedSourceDiskCapacity.setter
        def maxSupportedSourceDiskCapacity(self, value: long):
            self._maxSupportedSourceDiskCapacity = value
        @property
        def minRpo(self) -> long: ...
        @minRpo.setter
        def minRpo(self, value: long):
            self._minRpo = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


        class QuiesceMode(Enum):
            application = "application"
            filesystem = "filesystem"
            none = "none"


class HealthUpdate(vmodl.DynamicData):
    @property
    def entity(self) -> ManagedEntity: ...
    @entity.setter
    def entity(self, value: ManagedEntity):
        self._entity = value
    @property
    def healthUpdateInfoId(self) -> str: ...
    @healthUpdateInfoId.setter
    def healthUpdateInfoId(self, value: str):
        self._healthUpdateInfoId = value
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def status(self) -> ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']: ...
    @status.setter
    def status(self, value: ManagedEntity.Status | Literal['gray', 'green', 'yellow', 'red']):
        self._status = value
    @property
    def remediation(self) -> str: ...
    @remediation.setter
    def remediation(self, value: str):
        self._remediation = value


class HealthUpdateInfo(vmodl.DynamicData):
    @property
    def id(self) -> str: ...
    @id.setter
    def id(self, value: str):
        self._id = value
    @property
    def componentType(self) -> str: ...
    @componentType.setter
    def componentType(self, value: str):
        self._componentType = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value


    class ComponentType(Enum):
        Memory = "Memory"
        Power = "Power"
        Fan = "Fan"
        Network = "Network"
        Storage = "Storage"


class HistoricalInterval(vmodl.DynamicData):
    @property
    def key(self) -> int: ...
    @key.setter
    def key(self, value: int):
        self._key = value
    @property
    def samplingPeriod(self) -> int: ...
    @samplingPeriod.setter
    def samplingPeriod(self, value: int):
        self._samplingPeriod = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def length(self) -> int: ...
    @length.setter
    def length(self, value: int):
        self._length = value
    @property
    def level(self) -> int: ...
    @level.setter
    def level(self, value: int):
        self._level = value
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value


class HostServiceTicket(vmodl.DynamicData):
    @property
    def host(self) -> str: ...
    @host.setter
    def host(self, value: str):
        self._host = value
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
    def service(self) -> str: ...
    @service.setter
    def service(self, value: str):
        self._service = value
    @property
    def serviceVersion(self) -> str: ...
    @serviceVersion.setter
    def serviceVersion(self, value: str):
        self._serviceVersion = value
    @property
    def sessionId(self) -> str: ...
    @sessionId.setter
    def sessionId(self, value: str):
        self._sessionId = value


class ImportSpec(vmodl.DynamicData):
    @property
    def entityConfig(self) -> vApp.EntityConfigInfo: ...
    @entityConfig.setter
    def entityConfig(self, value: vApp.EntityConfigInfo):
        self._entityConfig = value
    @property
    def instantiationOst(self) -> OvfConsumer.OstNode: ...
    @instantiationOst.setter
    def instantiationOst(self, value: OvfConsumer.OstNode):
        self._instantiationOst = value


class InheritablePolicy(vmodl.DynamicData):
    @property
    def inherited(self) -> bool: ...
    @inherited.setter
    def inherited(self, value: bool):
        self._inherited = value


class IntExpression(NegatableExpression):
    @property
    def value(self) -> int: ...
    @value.setter
    def value(self, value: int):
        self._value = value


class IntPolicy(InheritablePolicy):
    @property
    def value(self) -> int: ...
    @value.setter
    def value(self, value: int):
        self._value = value


class IpAddress(NegatableExpression): ...


class IpRange(IpAddress):
    @property
    def addressPrefix(self) -> str: ...
    @addressPrefix.setter
    def addressPrefix(self, value: str):
        self._addressPrefix = value
    @property
    def prefixLength(self) -> int: ...
    @prefixLength.setter
    def prefixLength(self, value: int):
        self._prefixLength = value


class KeyValue(vmodl.DynamicData):
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


class LatencySensitivity(vmodl.DynamicData):
    @property
    def level(self) -> LatencySensitivity.SensitivityLevel | Literal['low', 'normal', 'medium', 'high', 'custom']: ...
    @level.setter
    def level(self, value: LatencySensitivity.SensitivityLevel | Literal['low', 'normal', 'medium', 'high', 'custom']):
        self._level = value
    @property
    def sensitivity(self) -> int: ...
    @sensitivity.setter
    def sensitivity(self, value: int):
        self._sensitivity = value


    class SensitivityLevel(Enum):
        low = "low"
        normal = "normal"
        medium = "medium"
        high = "high"
        custom = "custom"


class LongPolicy(InheritablePolicy):
    @property
    def value(self) -> long: ...
    @value.setter
    def value(self, value: long):
        self._value = value


class MacAddress(NegatableExpression): ...


class MacRange(MacAddress):
    @property
    def address(self) -> str: ...
    @address.setter
    def address(self, value: str):
        self._address = value
    @property
    def mask(self) -> str: ...
    @mask.setter
    def mask(self, value: str):
        self._mask = value


class MethodDescription(Description):
    @property
    def key(self) -> ManagedMethod: ...
    @key.setter
    def key(self, value: ManagedMethod):
        self._key = value


class NegatableExpression(vmodl.DynamicData):
    @property
    def negate(self) -> bool: ...
    @negate.setter
    def negate(self, value: bool):
        self._negate = value


class NumericRange(vmodl.DynamicData):
    @property
    def start(self) -> int: ...
    @start.setter
    def start(self, value: int):
        self._start = value
    @property
    def end(self) -> int: ...
    @end.setter
    def end(self, value: int):
        self._end = value


class OvfConsumer():


    class OstNode(vmodl.DynamicData):
        @property
        def id(self) -> str: ...
        @id.setter
        def id(self, value: str):
            self._id = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def section(self) -> List[OvfConsumer.OvfSection]: ...
        @section.setter
        def section(self, value: List[OvfConsumer.OvfSection]):
            self._section = value
        @property
        def child(self) -> List[OvfConsumer.OstNode]: ...
        @child.setter
        def child(self, value: List[OvfConsumer.OstNode]):
            self._child = value
        @property
        def entity(self) -> ManagedEntity: ...
        @entity.setter
        def entity(self, value: ManagedEntity):
            self._entity = value


    class OvfSection(vmodl.DynamicData):
        @property
        def lineNumber(self) -> int: ...
        @lineNumber.setter
        def lineNumber(self, value: int):
            self._lineNumber = value
        @property
        def xml(self) -> str: ...
        @xml.setter
        def xml(self, value: str):
            self._xml = value


    class OstNodeType(Enum):
        envelope = "envelope"
        virtualSystem = "virtualSystem"
        virtualSystemCollection = "virtualSystemCollection"


class PasswordField(vmodl.DynamicData):
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class PerformanceDescription(vmodl.DynamicData):
    @property
    def counterType(self) -> List[ElementDescription]: ...
    @counterType.setter
    def counterType(self, value: List[ElementDescription]):
        self._counterType = value
    @property
    def statsType(self) -> List[ElementDescription]: ...
    @statsType.setter
    def statsType(self, value: List[ElementDescription]):
        self._statsType = value


class PosixUserSearchResult(UserSearchResult):
    @property
    def id(self) -> int: ...
    @id.setter
    def id(self, value: int):
        self._id = value
    @property
    def shellAccess(self) -> bool: ...
    @shellAccess.setter
    def shellAccess(self, value: bool):
        self._shellAccess = value


class PrivilegePolicyDef(vmodl.DynamicData):
    @property
    def createPrivilege(self) -> str: ...
    @createPrivilege.setter
    def createPrivilege(self, value: str):
        self._createPrivilege = value
    @property
    def readPrivilege(self) -> str: ...
    @readPrivilege.setter
    def readPrivilege(self, value: str):
        self._readPrivilege = value
    @property
    def updatePrivilege(self) -> str: ...
    @updatePrivilege.setter
    def updatePrivilege(self, value: str):
        self._updatePrivilege = value
    @property
    def deletePrivilege(self) -> str: ...
    @deletePrivilege.setter
    def deletePrivilege(self, value: str):
        self._deletePrivilege = value


class ResourceAllocationInfo(vmodl.DynamicData):
    @property
    def reservation(self) -> long: ...
    @reservation.setter
    def reservation(self, value: long):
        self._reservation = value
    @property
    def expandableReservation(self) -> bool: ...
    @expandableReservation.setter
    def expandableReservation(self, value: bool):
        self._expandableReservation = value
    @property
    def limit(self) -> long: ...
    @limit.setter
    def limit(self, value: long):
        self._limit = value
    @property
    def shares(self) -> SharesInfo: ...
    @shares.setter
    def shares(self, value: SharesInfo):
        self._shares = value
    @property
    def overheadLimit(self) -> long: ...
    @overheadLimit.setter
    def overheadLimit(self, value: long):
        self._overheadLimit = value


class ResourceAllocationOption(vmodl.DynamicData):
    @property
    def sharesOption(self) -> SharesOption: ...
    @sharesOption.setter
    def sharesOption(self, value: SharesOption):
        self._sharesOption = value


class ResourceConfigOption(vmodl.DynamicData):
    @property
    def cpuAllocationOption(self) -> ResourceAllocationOption: ...
    @cpuAllocationOption.setter
    def cpuAllocationOption(self, value: ResourceAllocationOption):
        self._cpuAllocationOption = value
    @property
    def memoryAllocationOption(self) -> ResourceAllocationOption: ...
    @memoryAllocationOption.setter
    def memoryAllocationOption(self, value: ResourceAllocationOption):
        self._memoryAllocationOption = value


class ResourceConfigSpec(vmodl.DynamicData):
    @property
    def entity(self) -> ManagedEntity: ...
    @entity.setter
    def entity(self, value: ManagedEntity):
        self._entity = value
    @property
    def changeVersion(self) -> str: ...
    @changeVersion.setter
    def changeVersion(self, value: str):
        self._changeVersion = value
    @property
    def lastModified(self) -> datetime: ...
    @lastModified.setter
    def lastModified(self, value: datetime):
        self._lastModified = value
    @property
    def cpuAllocation(self) -> ResourceAllocationInfo: ...
    @cpuAllocation.setter
    def cpuAllocation(self, value: ResourceAllocationInfo):
        self._cpuAllocation = value
    @property
    def memoryAllocation(self) -> ResourceAllocationInfo: ...
    @memoryAllocation.setter
    def memoryAllocation(self, value: ResourceAllocationInfo):
        self._memoryAllocation = value
    @property
    def scaleDescendantsShares(self) -> str: ...
    @scaleDescendantsShares.setter
    def scaleDescendantsShares(self, value: str):
        self._scaleDescendantsShares = value


    class ScaleSharesBehavior(Enum):
        disabled = "disabled"
        scaleCpuAndMemoryShares = "scaleCpuAndMemoryShares"


class SDDCBase(vmodl.DynamicData): ...


class SelectionSet(vmodl.DynamicData): ...


class ServiceInstanceContent(vmodl.DynamicData):
    @property
    def rootFolder(self) -> Folder: ...
    @rootFolder.setter
    def rootFolder(self, value: Folder):
        self._rootFolder = value
    @property
    def propertyCollector(self) -> vmodl.query.PropertyCollector: ...
    @propertyCollector.setter
    def propertyCollector(self, value: vmodl.query.PropertyCollector):
        self._propertyCollector = value
    @property
    def viewManager(self) -> view.ViewManager: ...
    @viewManager.setter
    def viewManager(self, value: view.ViewManager):
        self._viewManager = value
    @property
    def about(self) -> AboutInfo: ...
    @about.setter
    def about(self, value: AboutInfo):
        self._about = value
    @property
    def setting(self) -> option.OptionManager: ...
    @setting.setter
    def setting(self, value: option.OptionManager):
        self._setting = value
    @property
    def userDirectory(self) -> UserDirectory: ...
    @userDirectory.setter
    def userDirectory(self, value: UserDirectory):
        self._userDirectory = value
    @property
    def sessionManager(self) -> SessionManager: ...
    @sessionManager.setter
    def sessionManager(self, value: SessionManager):
        self._sessionManager = value
    @property
    def authorizationManager(self) -> AuthorizationManager: ...
    @authorizationManager.setter
    def authorizationManager(self, value: AuthorizationManager):
        self._authorizationManager = value
    @property
    def serviceManager(self) -> ServiceManager: ...
    @serviceManager.setter
    def serviceManager(self, value: ServiceManager):
        self._serviceManager = value
    @property
    def perfManager(self) -> PerformanceManager: ...
    @perfManager.setter
    def perfManager(self, value: PerformanceManager):
        self._perfManager = value
    @property
    def scheduledTaskManager(self) -> scheduler.ScheduledTaskManager: ...
    @scheduledTaskManager.setter
    def scheduledTaskManager(self, value: scheduler.ScheduledTaskManager):
        self._scheduledTaskManager = value
    @property
    def alarmManager(self) -> alarm.AlarmManager: ...
    @alarmManager.setter
    def alarmManager(self, value: alarm.AlarmManager):
        self._alarmManager = value
    @property
    def eventManager(self) -> event.EventManager: ...
    @eventManager.setter
    def eventManager(self, value: event.EventManager):
        self._eventManager = value
    @property
    def taskManager(self) -> TaskManager: ...
    @taskManager.setter
    def taskManager(self, value: TaskManager):
        self._taskManager = value
    @property
    def extensionManager(self) -> ExtensionManager: ...
    @extensionManager.setter
    def extensionManager(self, value: ExtensionManager):
        self._extensionManager = value
    @property
    def customizationSpecManager(self) -> CustomizationSpecManager: ...
    @customizationSpecManager.setter
    def customizationSpecManager(self, value: CustomizationSpecManager):
        self._customizationSpecManager = value
    @property
    def guestCustomizationManager(self) -> vm.GuestCustomizationManager: ...
    @guestCustomizationManager.setter
    def guestCustomizationManager(self, value: vm.GuestCustomizationManager):
        self._guestCustomizationManager = value
    @property
    def customFieldsManager(self) -> CustomFieldsManager: ...
    @customFieldsManager.setter
    def customFieldsManager(self, value: CustomFieldsManager):
        self._customFieldsManager = value
    @property
    def accountManager(self) -> host.LocalAccountManager: ...
    @accountManager.setter
    def accountManager(self, value: host.LocalAccountManager):
        self._accountManager = value
    @property
    def diagnosticManager(self) -> DiagnosticManager: ...
    @diagnosticManager.setter
    def diagnosticManager(self, value: DiagnosticManager):
        self._diagnosticManager = value
    @property
    def licenseManager(self) -> LicenseManager: ...
    @licenseManager.setter
    def licenseManager(self, value: LicenseManager):
        self._licenseManager = value
    @property
    def searchIndex(self) -> SearchIndex: ...
    @searchIndex.setter
    def searchIndex(self, value: SearchIndex):
        self._searchIndex = value
    @property
    def fileManager(self) -> FileManager: ...
    @fileManager.setter
    def fileManager(self, value: FileManager):
        self._fileManager = value
    @property
    def datastoreNamespaceManager(self) -> DatastoreNamespaceManager: ...
    @datastoreNamespaceManager.setter
    def datastoreNamespaceManager(self, value: DatastoreNamespaceManager):
        self._datastoreNamespaceManager = value
    @property
    def virtualDiskManager(self) -> VirtualDiskManager: ...
    @virtualDiskManager.setter
    def virtualDiskManager(self, value: VirtualDiskManager):
        self._virtualDiskManager = value
    @property
    def virtualizationManager(self) -> VirtualizationManager: ...
    @virtualizationManager.setter
    def virtualizationManager(self, value: VirtualizationManager):
        self._virtualizationManager = value
    @property
    def snmpSystem(self) -> host.SnmpSystem: ...
    @snmpSystem.setter
    def snmpSystem(self, value: host.SnmpSystem):
        self._snmpSystem = value
    @property
    def vmProvisioningChecker(self) -> vm.check.ProvisioningChecker: ...
    @vmProvisioningChecker.setter
    def vmProvisioningChecker(self, value: vm.check.ProvisioningChecker):
        self._vmProvisioningChecker = value
    @property
    def vmCompatibilityChecker(self) -> vm.check.CompatibilityChecker: ...
    @vmCompatibilityChecker.setter
    def vmCompatibilityChecker(self, value: vm.check.CompatibilityChecker):
        self._vmCompatibilityChecker = value
    @property
    def ovfManager(self) -> OvfManager: ...
    @ovfManager.setter
    def ovfManager(self, value: OvfManager):
        self._ovfManager = value
    @property
    def ipPoolManager(self) -> IpPoolManager: ...
    @ipPoolManager.setter
    def ipPoolManager(self, value: IpPoolManager):
        self._ipPoolManager = value
    @property
    def dvSwitchManager(self) -> dvs.DistributedVirtualSwitchManager: ...
    @dvSwitchManager.setter
    def dvSwitchManager(self, value: dvs.DistributedVirtualSwitchManager):
        self._dvSwitchManager = value
    @property
    def hostProfileManager(self) -> profile.host.ProfileManager: ...
    @hostProfileManager.setter
    def hostProfileManager(self, value: profile.host.ProfileManager):
        self._hostProfileManager = value
    @property
    def clusterProfileManager(self) -> profile.cluster.ProfileManager: ...
    @clusterProfileManager.setter
    def clusterProfileManager(self, value: profile.cluster.ProfileManager):
        self._clusterProfileManager = value
    @property
    def complianceManager(self) -> profile.ComplianceManager: ...
    @complianceManager.setter
    def complianceManager(self, value: profile.ComplianceManager):
        self._complianceManager = value
    @property
    def localizationManager(self) -> LocalizationManager: ...
    @localizationManager.setter
    def localizationManager(self, value: LocalizationManager):
        self._localizationManager = value
    @property
    def storageResourceManager(self) -> StorageResourceManager: ...
    @storageResourceManager.setter
    def storageResourceManager(self, value: StorageResourceManager):
        self._storageResourceManager = value
    @property
    def guestOperationsManager(self) -> vm.guest.GuestOperationsManager: ...
    @guestOperationsManager.setter
    def guestOperationsManager(self, value: vm.guest.GuestOperationsManager):
        self._guestOperationsManager = value
    @property
    def overheadMemoryManager(self) -> OverheadMemoryManager: ...
    @overheadMemoryManager.setter
    def overheadMemoryManager(self, value: OverheadMemoryManager):
        self._overheadMemoryManager = value
    @property
    def certificateManager(self) -> CertificateManager: ...
    @certificateManager.setter
    def certificateManager(self, value: CertificateManager):
        self._certificateManager = value
    @property
    def ioFilterManager(self) -> IoFilterManager: ...
    @ioFilterManager.setter
    def ioFilterManager(self, value: IoFilterManager):
        self._ioFilterManager = value
    @property
    def vStorageObjectManager(self) -> vslm.VStorageObjectManagerBase: ...
    @vStorageObjectManager.setter
    def vStorageObjectManager(self, value: vslm.VStorageObjectManagerBase):
        self._vStorageObjectManager = value
    @property
    def hostSpecManager(self) -> profile.host.HostSpecificationManager: ...
    @hostSpecManager.setter
    def hostSpecManager(self, value: profile.host.HostSpecificationManager):
        self._hostSpecManager = value
    @property
    def cryptoManager(self) -> encryption.CryptoManager: ...
    @cryptoManager.setter
    def cryptoManager(self, value: encryption.CryptoManager):
        self._cryptoManager = value
    @property
    def healthUpdateManager(self) -> HealthUpdateManager: ...
    @healthUpdateManager.setter
    def healthUpdateManager(self, value: HealthUpdateManager):
        self._healthUpdateManager = value
    @property
    def failoverClusterConfigurator(self) -> vcha.FailoverClusterConfigurator: ...
    @failoverClusterConfigurator.setter
    def failoverClusterConfigurator(self, value: vcha.FailoverClusterConfigurator):
        self._failoverClusterConfigurator = value
    @property
    def failoverClusterManager(self) -> vcha.FailoverClusterManager: ...
    @failoverClusterManager.setter
    def failoverClusterManager(self, value: vcha.FailoverClusterManager):
        self._failoverClusterManager = value
    @property
    def tenantManager(self) -> tenant.TenantManager: ...
    @tenantManager.setter
    def tenantManager(self, value: tenant.TenantManager):
        self._tenantManager = value
    @property
    def siteInfoManager(self) -> SiteInfoManager: ...
    @siteInfoManager.setter
    def siteInfoManager(self, value: SiteInfoManager):
        self._siteInfoManager = value
    @property
    def storageQueryManager(self) -> StorageQueryManager: ...
    @storageQueryManager.setter
    def storageQueryManager(self, value: StorageQueryManager):
        self._storageQueryManager = value


class ServiceLocator(vmodl.DynamicData):
    @property
    def instanceUuid(self) -> str: ...
    @instanceUuid.setter
    def instanceUuid(self, value: str):
        self._instanceUuid = value
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, value: str):
        self._url = value
    @property
    def credential(self) -> ServiceLocator.Credential: ...
    @credential.setter
    def credential(self, value: ServiceLocator.Credential):
        self._credential = value
    @property
    def sslThumbprint(self) -> str: ...
    @sslThumbprint.setter
    def sslThumbprint(self, value: str):
        self._sslThumbprint = value


    class Credential(vmodl.DynamicData): ...


    class NamePassword(ServiceLocator.Credential):
        @property
        def username(self) -> str: ...
        @username.setter
        def username(self, value: str):
            self._username = value
        @property
        def password(self) -> str: ...
        @password.setter
        def password(self, value: str):
            self._password = value


    class SAMLCredential(ServiceLocator.Credential):
        @property
        def token(self) -> str: ...
        @token.setter
        def token(self, value: str):
            self._token = value


class SharesInfo(vmodl.DynamicData):
    @property
    def shares(self) -> int: ...
    @shares.setter
    def shares(self, value: int):
        self._shares = value
    @property
    def level(self) -> SharesInfo.Level | Literal['low', 'normal', 'high', 'custom']: ...
    @level.setter
    def level(self, value: SharesInfo.Level | Literal['low', 'normal', 'high', 'custom']):
        self._level = value


    class Level(Enum):
        low = "low"
        normal = "normal"
        high = "high"
        custom = "custom"


class SharesOption(vmodl.DynamicData):
    @property
    def sharesOption(self) -> option.IntOption: ...
    @sharesOption.setter
    def sharesOption(self, value: option.IntOption):
        self._sharesOption = value
    @property
    def defaultLevel(self) -> SharesInfo.Level | Literal['low', 'normal', 'high', 'custom']: ...
    @defaultLevel.setter
    def defaultLevel(self, value: SharesInfo.Level | Literal['low', 'normal', 'high', 'custom']):
        self._defaultLevel = value


class SingleIp(IpAddress):
    @property
    def address(self) -> str: ...
    @address.setter
    def address(self, value: str):
        self._address = value


class SingleMac(MacAddress):
    @property
    def address(self) -> str: ...
    @address.setter
    def address(self, value: str):
        self._address = value


class SiteInfo(vmodl.DynamicData): ...


class StringExpression(NegatableExpression):
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class StringPolicy(InheritablePolicy):
    @property
    def value(self) -> str: ...
    @value.setter
    def value(self, value: str):
        self._value = value


class Tag(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class TaskDescription(vmodl.DynamicData):
    @property
    def methodInfo(self) -> List[ElementDescription]: ...
    @methodInfo.setter
    def methodInfo(self, value: List[ElementDescription]):
        self._methodInfo = value
    @property
    def state(self) -> List[ElementDescription]: ...
    @state.setter
    def state(self, value: List[ElementDescription]):
        self._state = value
    @property
    def reason(self) -> List[TypeDescription]: ...
    @reason.setter
    def reason(self, value: List[TypeDescription]):
        self._reason = value


class TaskFilterSpec(vmodl.DynamicData):
    @property
    def entity(self) -> TaskFilterSpec.ByEntity: ...
    @entity.setter
    def entity(self, value: TaskFilterSpec.ByEntity):
        self._entity = value
    @property
    def time(self) -> TaskFilterSpec.ByTime: ...
    @time.setter
    def time(self, value: TaskFilterSpec.ByTime):
        self._time = value
    @property
    def userName(self) -> TaskFilterSpec.ByUsername: ...
    @userName.setter
    def userName(self, value: TaskFilterSpec.ByUsername):
        self._userName = value
    @property
    def activationId(self) -> List[str]: ...
    @activationId.setter
    def activationId(self, value: List[str]):
        self._activationId = value
    @property
    def state(self) -> List[TaskInfo.State]: ...
    @state.setter
    def state(self, value: List[TaskInfo.State]):
        self._state = value
    @property
    def alarm(self) -> alarm.Alarm: ...
    @alarm.setter
    def alarm(self, value: alarm.Alarm):
        self._alarm = value
    @property
    def scheduledTask(self) -> scheduler.ScheduledTask: ...
    @scheduledTask.setter
    def scheduledTask(self, value: scheduler.ScheduledTask):
        self._scheduledTask = value
    @property
    def eventChainId(self) -> List[int]: ...
    @eventChainId.setter
    def eventChainId(self, value: List[int]):
        self._eventChainId = value
    @property
    def tag(self) -> List[str]: ...
    @tag.setter
    def tag(self, value: List[str]):
        self._tag = value
    @property
    def parentTaskKey(self) -> List[str]: ...
    @parentTaskKey.setter
    def parentTaskKey(self, value: List[str]):
        self._parentTaskKey = value
    @property
    def rootTaskKey(self) -> List[str]: ...
    @rootTaskKey.setter
    def rootTaskKey(self, value: List[str]):
        self._rootTaskKey = value


    class ByEntity(vmodl.DynamicData):
        @property
        def entity(self) -> ManagedEntity: ...
        @entity.setter
        def entity(self, value: ManagedEntity):
            self._entity = value
        @property
        def recursion(self) -> TaskFilterSpec.RecursionOption | Literal['self', 'children', 'all']: ...
        @recursion.setter
        def recursion(self, value: TaskFilterSpec.RecursionOption | Literal['self', 'children', 'all']):
            self._recursion = value


    class ByTime(vmodl.DynamicData):
        @property
        def timeType(self) -> TaskFilterSpec.TimeOption | Literal['queuedTime', 'startedTime', 'completedTime']: ...
        @timeType.setter
        def timeType(self, value: TaskFilterSpec.TimeOption | Literal['queuedTime', 'startedTime', 'completedTime']):
            self._timeType = value
        @property
        def beginTime(self) -> datetime: ...
        @beginTime.setter
        def beginTime(self, value: datetime):
            self._beginTime = value
        @property
        def endTime(self) -> datetime: ...
        @endTime.setter
        def endTime(self, value: datetime):
            self._endTime = value


    class ByUsername(vmodl.DynamicData):
        @property
        def systemUser(self) -> bool: ...
        @systemUser.setter
        def systemUser(self, value: bool):
            self._systemUser = value
        @property
        def userList(self) -> List[str]: ...
        @userList.setter
        def userList(self, value: List[str]):
            self._userList = value


    class RecursionOption(Enum):
        self = "self"
        children = "children"
        all = "all"


    class TimeOption(Enum):
        queuedTime = "queuedTime"
        startedTime = "startedTime"
        completedTime = "completedTime"


class TaskInfo(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def task(self) -> Task: ...
    @task.setter
    def task(self, value: Task):
        self._task = value
    @property
    def description(self) -> vmodl.LocalizableMessage: ...
    @description.setter
    def description(self, value: vmodl.LocalizableMessage):
        self._description = value
    @property
    def name(self) -> ManagedMethod: ...
    @name.setter
    def name(self, value: ManagedMethod):
        self._name = value
    @property
    def descriptionId(self) -> str: ...
    @descriptionId.setter
    def descriptionId(self, value: str):
        self._descriptionId = value
    @property
    def entity(self) -> ManagedEntity: ...
    @entity.setter
    def entity(self, value: ManagedEntity):
        self._entity = value
    @property
    def entityName(self) -> str: ...
    @entityName.setter
    def entityName(self, value: str):
        self._entityName = value
    @property
    def locked(self) -> List[ManagedEntity]: ...
    @locked.setter
    def locked(self, value: List[ManagedEntity]):
        self._locked = value
    @property
    def state(self) -> TaskInfo.State | Literal['queued', 'running', 'success', 'error']: ...
    @state.setter
    def state(self, value: TaskInfo.State | Literal['queued', 'running', 'success', 'error']):
        self._state = value
    @property
    def cancelled(self) -> bool: ...
    @cancelled.setter
    def cancelled(self, value: bool):
        self._cancelled = value
    @property
    def cancelable(self) -> bool: ...
    @cancelable.setter
    def cancelable(self, value: bool):
        self._cancelable = value
    @property
    def error(self) -> vmodl.MethodFault: ...
    @error.setter
    def error(self, value: vmodl.MethodFault):
        self._error = value
    @property
    def result(self) -> object: ...
    @result.setter
    def result(self, value: object):
        self._result = value
    @property
    def progress(self) -> int: ...
    @progress.setter
    def progress(self, value: int):
        self._progress = value
    @property
    def progressDetails(self) -> List[vmodl.KeyAnyValue]: ...
    @progressDetails.setter
    def progressDetails(self, value: List[vmodl.KeyAnyValue]):
        self._progressDetails = value
    @property
    def reason(self) -> TaskReason: ...
    @reason.setter
    def reason(self, value: TaskReason):
        self._reason = value
    @property
    def queueTime(self) -> datetime: ...
    @queueTime.setter
    def queueTime(self, value: datetime):
        self._queueTime = value
    @property
    def startTime(self) -> datetime: ...
    @startTime.setter
    def startTime(self, value: datetime):
        self._startTime = value
    @property
    def completeTime(self) -> datetime: ...
    @completeTime.setter
    def completeTime(self, value: datetime):
        self._completeTime = value
    @property
    def eventChainId(self) -> int: ...
    @eventChainId.setter
    def eventChainId(self, value: int):
        self._eventChainId = value
    @property
    def changeTag(self) -> str: ...
    @changeTag.setter
    def changeTag(self, value: str):
        self._changeTag = value
    @property
    def parentTaskKey(self) -> str: ...
    @parentTaskKey.setter
    def parentTaskKey(self, value: str):
        self._parentTaskKey = value
    @property
    def rootTaskKey(self) -> str: ...
    @rootTaskKey.setter
    def rootTaskKey(self, value: str):
        self._rootTaskKey = value
    @property
    def activationId(self) -> str: ...
    @activationId.setter
    def activationId(self, value: str):
        self._activationId = value


class TaskReason(vmodl.DynamicData): ...


class TaskReasonAlarm(TaskReason):
    @property
    def alarmName(self) -> str: ...
    @alarmName.setter
    def alarmName(self, value: str):
        self._alarmName = value
    @property
    def alarm(self) -> alarm.Alarm: ...
    @alarm.setter
    def alarm(self, value: alarm.Alarm):
        self._alarm = value
    @property
    def entityName(self) -> str: ...
    @entityName.setter
    def entityName(self, value: str):
        self._entityName = value
    @property
    def entity(self) -> ManagedEntity: ...
    @entity.setter
    def entity(self, value: ManagedEntity):
        self._entity = value


class TaskReasonSchedule(TaskReason):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def scheduledTask(self) -> scheduler.ScheduledTask: ...
    @scheduledTask.setter
    def scheduledTask(self, value: scheduler.ScheduledTask):
        self._scheduledTask = value


class TaskReasonSystem(TaskReason): ...


class TaskReasonUser(TaskReason):
    @property
    def userName(self) -> str: ...
    @userName.setter
    def userName(self, value: str):
        self._userName = value


class TypeDescription(Description):
    @property
    def key(self) -> type: ...
    @key.setter
    def key(self, value: type):
        self._key = value


class UpdateVirtualMachineFilesResult(vmodl.DynamicData):
    @property
    def failedVmFile(self) -> List[UpdateVirtualMachineFilesResult.FailedVmFileInfo]: ...
    @failedVmFile.setter
    def failedVmFile(self, value: List[UpdateVirtualMachineFilesResult.FailedVmFileInfo]):
        self._failedVmFile = value


    class FailedVmFileInfo(vmodl.DynamicData):
        @property
        def vmFile(self) -> str: ...
        @vmFile.setter
        def vmFile(self, value: str):
            self._vmFile = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


class UserSearchResult(vmodl.DynamicData):
    @property
    def principal(self) -> str: ...
    @principal.setter
    def principal(self, value: str):
        self._principal = value
    @property
    def fullName(self) -> str: ...
    @fullName.setter
    def fullName(self, value: str):
        self._fullName = value
    @property
    def group(self) -> bool: ...
    @group.setter
    def group(self, value: bool):
        self._group = value


class UserSession(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def userName(self) -> str: ...
    @userName.setter
    def userName(self, value: str):
        self._userName = value
    @property
    def fullName(self) -> str: ...
    @fullName.setter
    def fullName(self, value: str):
        self._fullName = value
    @property
    def loginTime(self) -> datetime: ...
    @loginTime.setter
    def loginTime(self, value: datetime):
        self._loginTime = value
    @property
    def lastActiveTime(self) -> datetime: ...
    @lastActiveTime.setter
    def lastActiveTime(self, value: datetime):
        self._lastActiveTime = value
    @property
    def locale(self) -> str: ...
    @locale.setter
    def locale(self, value: str):
        self._locale = value
    @property
    def messageLocale(self) -> str: ...
    @messageLocale.setter
    def messageLocale(self, value: str):
        self._messageLocale = value
    @property
    def extensionSession(self) -> bool: ...
    @extensionSession.setter
    def extensionSession(self, value: bool):
        self._extensionSession = value
    @property
    def ipAddress(self) -> str: ...
    @ipAddress.setter
    def ipAddress(self, value: str):
        self._ipAddress = value
    @property
    def userAgent(self) -> str: ...
    @userAgent.setter
    def userAgent(self, value: str):
        self._userAgent = value
    @property
    def callCount(self) -> long: ...
    @callCount.setter
    def callCount(self, value: long):
        self._callCount = value


class VVolVmConfigFileUpdateResult(vmodl.DynamicData):
    @property
    def succeededVmConfigFile(self) -> List[KeyValue]: ...
    @succeededVmConfigFile.setter
    def succeededVmConfigFile(self, value: List[KeyValue]):
        self._succeededVmConfigFile = value
    @property
    def failedVmConfigFile(self) -> List[VVolVmConfigFileUpdateResult.FailedVmConfigFileInfo]: ...
    @failedVmConfigFile.setter
    def failedVmConfigFile(self, value: List[VVolVmConfigFileUpdateResult.FailedVmConfigFileInfo]):
        self._failedVmConfigFile = value


    class FailedVmConfigFileInfo(vmodl.DynamicData):
        @property
        def targetConfigVVolId(self) -> str: ...
        @targetConfigVVolId.setter
        def targetConfigVVolId(self, value: str):
            self._targetConfigVVolId = value
        @property
        def dsPath(self) -> str: ...
        @dsPath.setter
        def dsPath(self, value: str):
            self._dsPath = value
        @property
        def fault(self) -> vmodl.MethodFault: ...
        @fault.setter
        def fault(self, value: vmodl.MethodFault):
            self._fault = value


class VasaStorageArray(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def uuid(self) -> str: ...
    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value
    @property
    def vendorId(self) -> str: ...
    @vendorId.setter
    def vendorId(self, value: str):
        self._vendorId = value
    @property
    def modelId(self) -> str: ...
    @modelId.setter
    def modelId(self, value: str):
        self._modelId = value
    @property
    def discoverySvcInfo(self) -> List[VasaStorageArray.DiscoverySvcInfo]: ...
    @discoverySvcInfo.setter
    def discoverySvcInfo(self, value: List[VasaStorageArray.DiscoverySvcInfo]):
        self._discoverySvcInfo = value


    class DiscoveryFcTransport(vmodl.DynamicData):
        @property
        def nodeWwn(self) -> str: ...
        @nodeWwn.setter
        def nodeWwn(self, value: str):
            self._nodeWwn = value
        @property
        def portWwn(self) -> str: ...
        @portWwn.setter
        def portWwn(self, value: str):
            self._portWwn = value


    class DiscoveryIpTransport(vmodl.DynamicData):
        @property
        def ipAddress(self) -> str: ...
        @ipAddress.setter
        def ipAddress(self, value: str):
            self._ipAddress = value
        @property
        def portNumber(self) -> str: ...
        @portNumber.setter
        def portNumber(self, value: str):
            self._portNumber = value


    class DiscoverySvcInfo(vmodl.DynamicData):
        @property
        def portType(self) -> str: ...
        @portType.setter
        def portType(self, value: str):
            self._portType = value
        @property
        def svcNqn(self) -> str: ...
        @svcNqn.setter
        def svcNqn(self, value: str):
            self._svcNqn = value
        @property
        def ipInfo(self) -> VasaStorageArray.DiscoveryIpTransport: ...
        @ipInfo.setter
        def ipInfo(self, value: VasaStorageArray.DiscoveryIpTransport):
            self._ipInfo = value
        @property
        def fcInfo(self) -> VasaStorageArray.DiscoveryFcTransport: ...
        @fcInfo.setter
        def fcInfo(self, value: VasaStorageArray.DiscoveryFcTransport):
            self._fcInfo = value


class VasaVvolManager():


    class VasaProviderContainerSpec(vmodl.DynamicData):
        @property
        def vasaProviderInfo(self) -> List[VimVasaProviderInfo]: ...
        @vasaProviderInfo.setter
        def vasaProviderInfo(self, value: List[VimVasaProviderInfo]):
            self._vasaProviderInfo = value
        @property
        def scId(self) -> str: ...
        @scId.setter
        def scId(self, value: str):
            self._scId = value
        @property
        def deleted(self) -> bool: ...
        @deleted.setter
        def deleted(self, value: bool):
            self._deleted = value


class VimVasaProvider(vmodl.DynamicData):
    @property
    def uid(self) -> str: ...
    @uid.setter
    def uid(self, value: str):
        self._uid = value
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, value: str):
        self._url = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def selfSignedCertificate(self) -> str: ...
    @selfSignedCertificate.setter
    def selfSignedCertificate(self, value: str):
        self._selfSignedCertificate = value
    @property
    def vhostConfig(self) -> VimVasaProvider.VirtualHostConfig: ...
    @vhostConfig.setter
    def vhostConfig(self, value: VimVasaProvider.VirtualHostConfig):
        self._vhostConfig = value
    @property
    def versionId(self) -> int: ...
    @versionId.setter
    def versionId(self, value: int):
        self._versionId = value


    class StatePerArray(vmodl.DynamicData):
        @property
        def priority(self) -> int: ...
        @priority.setter
        def priority(self, value: int):
            self._priority = value
        @property
        def arrayId(self) -> str: ...
        @arrayId.setter
        def arrayId(self, value: str):
            self._arrayId = value
        @property
        def active(self) -> bool: ...
        @active.setter
        def active(self, value: bool):
            self._active = value


    class VirtualHostConfig(vmodl.DynamicData):
        @property
        def vhostName(self) -> str: ...
        @vhostName.setter
        def vhostName(self, value: str):
            self._vhostName = value
        @property
        def serviceHost(self) -> str: ...
        @serviceHost.setter
        def serviceHost(self, value: str):
            self._serviceHost = value
        @property
        def servicePort(self) -> int: ...
        @servicePort.setter
        def servicePort(self, value: int):
            self._servicePort = value


class VimVasaProviderInfo(vmodl.DynamicData):
    @property
    def provider(self) -> VimVasaProvider: ...
    @provider.setter
    def provider(self, value: VimVasaProvider):
        self._provider = value
    @property
    def arrayState(self) -> List[VimVasaProvider.StatePerArray]: ...
    @arrayState.setter
    def arrayState(self, value: List[VimVasaProvider.StatePerArray]):
        self._arrayState = value


class vApp():


    class CloneSpec(vmodl.DynamicData):
        @property
        def location(self) -> Datastore: ...
        @location.setter
        def location(self, value: Datastore):
            self._location = value
        @property
        def host(self) -> HostSystem: ...
        @host.setter
        def host(self, value: HostSystem):
            self._host = value
        @property
        def resourceSpec(self) -> ResourceConfigSpec: ...
        @resourceSpec.setter
        def resourceSpec(self, value: ResourceConfigSpec):
            self._resourceSpec = value
        @property
        def vmFolder(self) -> Folder: ...
        @vmFolder.setter
        def vmFolder(self, value: Folder):
            self._vmFolder = value
        @property
        def networkMapping(self) -> List[vApp.CloneSpec.NetworkMappingPair]: ...
        @networkMapping.setter
        def networkMapping(self, value: List[vApp.CloneSpec.NetworkMappingPair]):
            self._networkMapping = value
        @property
        def property(self) -> List[KeyValue]: ...
        @property.setter
        def property(self, value: List[KeyValue]):
            self._property = value
        @property
        def resourceMapping(self) -> List[vApp.CloneSpec.ResourceMap]: ...
        @resourceMapping.setter
        def resourceMapping(self, value: List[vApp.CloneSpec.ResourceMap]):
            self._resourceMapping = value
        @property
        def provisioning(self) -> str: ...
        @provisioning.setter
        def provisioning(self, value: str):
            self._provisioning = value


        class NetworkMappingPair(vmodl.DynamicData):
            @property
            def source(self) -> Network: ...
            @source.setter
            def source(self, value: Network):
                self._source = value
            @property
            def destination(self) -> Network: ...
            @destination.setter
            def destination(self, value: Network):
                self._destination = value


        class ResourceMap(vmodl.DynamicData):
            @property
            def source(self) -> ManagedEntity: ...
            @source.setter
            def source(self, value: ManagedEntity):
                self._source = value
            @property
            def parent(self) -> ResourcePool: ...
            @parent.setter
            def parent(self, value: ResourcePool):
                self._parent = value
            @property
            def resourceSpec(self) -> ResourceConfigSpec: ...
            @resourceSpec.setter
            def resourceSpec(self, value: ResourceConfigSpec):
                self._resourceSpec = value
            @property
            def location(self) -> Datastore: ...
            @location.setter
            def location(self, value: Datastore):
                self._location = value


        class ProvisioningType(Enum):
            sameAsSource = "sameAsSource"
            thin = "thin"
            thick = "thick"


    class EntityConfigInfo(vmodl.DynamicData):
        @property
        def key(self) -> ManagedEntity: ...
        @key.setter
        def key(self, value: ManagedEntity):
            self._key = value
        @property
        def tag(self) -> str: ...
        @tag.setter
        def tag(self, value: str):
            self._tag = value
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
        def waitingForGuest(self) -> bool: ...
        @waitingForGuest.setter
        def waitingForGuest(self, value: bool):
            self._waitingForGuest = value
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
        @property
        def destroyWithParent(self) -> bool: ...
        @destroyWithParent.setter
        def destroyWithParent(self, value: bool):
            self._destroyWithParent = value


        class Action(Enum):
            none = "none"
            powerOn = "powerOn"
            powerOff = "powerOff"
            guestShutdown = "guestShutdown"
            suspend = "suspend"


    class IPAssignmentInfo(vmodl.DynamicData):
        @property
        def supportedAllocationScheme(self) -> List[str]: ...
        @supportedAllocationScheme.setter
        def supportedAllocationScheme(self, value: List[str]):
            self._supportedAllocationScheme = value
        @property
        def ipAllocationPolicy(self) -> str: ...
        @ipAllocationPolicy.setter
        def ipAllocationPolicy(self, value: str):
            self._ipAllocationPolicy = value
        @property
        def supportedIpProtocol(self) -> List[str]: ...
        @supportedIpProtocol.setter
        def supportedIpProtocol(self, value: List[str]):
            self._supportedIpProtocol = value
        @property
        def ipProtocol(self) -> str: ...
        @ipProtocol.setter
        def ipProtocol(self, value: str):
            self._ipProtocol = value


        class AllocationSchemes(Enum):
            dhcp = "dhcp"
            ovfenv = "ovfenv"


        class IpAllocationPolicy(Enum):
            dhcpPolicy = "dhcpPolicy"
            transientPolicy = "transientPolicy"
            fixedPolicy = "fixedPolicy"
            fixedAllocatedPolicy = "fixedAllocatedPolicy"


        class Protocols(Enum):
            IPv4 = "IPv4"
            IPv6 = "IPv6"


    class IpPool(vmodl.DynamicData):
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
        def ipv4Config(self) -> vApp.IpPool.IpPoolConfigInfo: ...
        @ipv4Config.setter
        def ipv4Config(self, value: vApp.IpPool.IpPoolConfigInfo):
            self._ipv4Config = value
        @property
        def ipv6Config(self) -> vApp.IpPool.IpPoolConfigInfo: ...
        @ipv6Config.setter
        def ipv6Config(self, value: vApp.IpPool.IpPoolConfigInfo):
            self._ipv6Config = value
        @property
        def dnsDomain(self) -> str: ...
        @dnsDomain.setter
        def dnsDomain(self, value: str):
            self._dnsDomain = value
        @property
        def dnsSearchPath(self) -> str: ...
        @dnsSearchPath.setter
        def dnsSearchPath(self, value: str):
            self._dnsSearchPath = value
        @property
        def hostPrefix(self) -> str: ...
        @hostPrefix.setter
        def hostPrefix(self, value: str):
            self._hostPrefix = value
        @property
        def httpProxy(self) -> str: ...
        @httpProxy.setter
        def httpProxy(self, value: str):
            self._httpProxy = value
        @property
        def networkAssociation(self) -> List[vApp.IpPool.Association]: ...
        @networkAssociation.setter
        def networkAssociation(self, value: List[vApp.IpPool.Association]):
            self._networkAssociation = value
        @property
        def availableIpv4Addresses(self) -> int: ...
        @availableIpv4Addresses.setter
        def availableIpv4Addresses(self, value: int):
            self._availableIpv4Addresses = value
        @property
        def availableIpv6Addresses(self) -> int: ...
        @availableIpv6Addresses.setter
        def availableIpv6Addresses(self, value: int):
            self._availableIpv6Addresses = value
        @property
        def allocatedIpv4Addresses(self) -> int: ...
        @allocatedIpv4Addresses.setter
        def allocatedIpv4Addresses(self, value: int):
            self._allocatedIpv4Addresses = value
        @property
        def allocatedIpv6Addresses(self) -> int: ...
        @allocatedIpv6Addresses.setter
        def allocatedIpv6Addresses(self, value: int):
            self._allocatedIpv6Addresses = value


        class Association(vmodl.DynamicData):
            @property
            def network(self) -> Network: ...
            @network.setter
            def network(self, value: Network):
                self._network = value
            @property
            def networkName(self) -> str: ...
            @networkName.setter
            def networkName(self, value: str):
                self._networkName = value


        class IpPoolConfigInfo(vmodl.DynamicData):
            @property
            def subnetAddress(self) -> str: ...
            @subnetAddress.setter
            def subnetAddress(self, value: str):
                self._subnetAddress = value
            @property
            def netmask(self) -> str: ...
            @netmask.setter
            def netmask(self, value: str):
                self._netmask = value
            @property
            def gateway(self) -> str: ...
            @gateway.setter
            def gateway(self, value: str):
                self._gateway = value
            @property
            def range(self) -> str: ...
            @range.setter
            def range(self, value: str):
                self._range = value
            @property
            def dns(self) -> List[str]: ...
            @dns.setter
            def dns(self, value: List[str]):
                self._dns = value
            @property
            def dhcpServerAvailable(self) -> bool: ...
            @dhcpServerAvailable.setter
            def dhcpServerAvailable(self, value: bool):
                self._dhcpServerAvailable = value
            @property
            def ipPoolEnabled(self) -> bool: ...
            @ipPoolEnabled.setter
            def ipPoolEnabled(self, value: bool):
                self._ipPoolEnabled = value


    class OvfSectionInfo(vmodl.DynamicData):
        @property
        def key(self) -> int: ...
        @key.setter
        def key(self, value: int):
            self._key = value
        @property
        def namespace(self) -> str: ...
        @namespace.setter
        def namespace(self, value: str):
            self._namespace = value
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def atEnvelopeLevel(self) -> bool: ...
        @atEnvelopeLevel.setter
        def atEnvelopeLevel(self, value: bool):
            self._atEnvelopeLevel = value
        @property
        def contents(self) -> str: ...
        @contents.setter
        def contents(self, value: str):
            self._contents = value


    class OvfSectionSpec(option.ArrayUpdateSpec):
        @property
        def info(self) -> vApp.OvfSectionInfo: ...
        @info.setter
        def info(self, value: vApp.OvfSectionInfo):
            self._info = value


    class ProductInfo(vmodl.DynamicData):
        @property
        def key(self) -> int: ...
        @key.setter
        def key(self, value: int):
            self._key = value
        @property
        def classId(self) -> str: ...
        @classId.setter
        def classId(self, value: str):
            self._classId = value
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
        def vendor(self) -> str: ...
        @vendor.setter
        def vendor(self, value: str):
            self._vendor = value
        @property
        def version(self) -> str: ...
        @version.setter
        def version(self, value: str):
            self._version = value
        @property
        def fullVersion(self) -> str: ...
        @fullVersion.setter
        def fullVersion(self, value: str):
            self._fullVersion = value
        @property
        def vendorUrl(self) -> str: ...
        @vendorUrl.setter
        def vendorUrl(self, value: str):
            self._vendorUrl = value
        @property
        def productUrl(self) -> str: ...
        @productUrl.setter
        def productUrl(self, value: str):
            self._productUrl = value
        @property
        def appUrl(self) -> str: ...
        @appUrl.setter
        def appUrl(self, value: str):
            self._appUrl = value


    class ProductSpec(option.ArrayUpdateSpec):
        @property
        def info(self) -> vApp.ProductInfo: ...
        @info.setter
        def info(self, value: vApp.ProductInfo):
            self._info = value


    class PropertyInfo(vmodl.DynamicData):
        @property
        def key(self) -> int: ...
        @key.setter
        def key(self, value: int):
            self._key = value
        @property
        def classId(self) -> str: ...
        @classId.setter
        def classId(self, value: str):
            self._classId = value
        @property
        def instanceId(self) -> str: ...
        @instanceId.setter
        def instanceId(self, value: str):
            self._instanceId = value
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
        def typeReference(self) -> str: ...
        @typeReference.setter
        def typeReference(self, value: str):
            self._typeReference = value
        @property
        def userConfigurable(self) -> bool: ...
        @userConfigurable.setter
        def userConfigurable(self, value: bool):
            self._userConfigurable = value
        @property
        def defaultValue(self) -> str: ...
        @defaultValue.setter
        def defaultValue(self, value: str):
            self._defaultValue = value
        @property
        def value(self) -> str: ...
        @value.setter
        def value(self, value: str):
            self._value = value
        @property
        def description(self) -> str: ...
        @description.setter
        def description(self, value: str):
            self._description = value


    class PropertySpec(option.ArrayUpdateSpec):
        @property
        def info(self) -> vApp.PropertyInfo: ...
        @info.setter
        def info(self, value: vApp.PropertyInfo):
            self._info = value


    class VAppConfigInfo(vApp.VmConfigInfo):
        @property
        def entityConfig(self) -> List[vApp.EntityConfigInfo]: ...
        @entityConfig.setter
        def entityConfig(self, value: List[vApp.EntityConfigInfo]):
            self._entityConfig = value
        @property
        def annotation(self) -> str: ...
        @annotation.setter
        def annotation(self, value: str):
            self._annotation = value
        @property
        def instanceUuid(self) -> str: ...
        @instanceUuid.setter
        def instanceUuid(self, value: str):
            self._instanceUuid = value
        @property
        def managedBy(self) -> ext.ManagedByInfo: ...
        @managedBy.setter
        def managedBy(self, value: ext.ManagedByInfo):
            self._managedBy = value


    class VAppConfigSpec(vApp.VmConfigSpec):
        @property
        def entityConfig(self) -> List[vApp.EntityConfigInfo]: ...
        @entityConfig.setter
        def entityConfig(self, value: List[vApp.EntityConfigInfo]):
            self._entityConfig = value
        @property
        def annotation(self) -> str: ...
        @annotation.setter
        def annotation(self, value: str):
            self._annotation = value
        @property
        def instanceUuid(self) -> str: ...
        @instanceUuid.setter
        def instanceUuid(self, value: str):
            self._instanceUuid = value
        @property
        def managedBy(self) -> ext.ManagedByInfo: ...
        @managedBy.setter
        def managedBy(self, value: ext.ManagedByInfo):
            self._managedBy = value


    class VAppImportSpec(ImportSpec):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def vAppConfigSpec(self) -> vApp.VAppConfigSpec: ...
        @vAppConfigSpec.setter
        def vAppConfigSpec(self, value: vApp.VAppConfigSpec):
            self._vAppConfigSpec = value
        @property
        def resourcePoolSpec(self) -> ResourceConfigSpec: ...
        @resourcePoolSpec.setter
        def resourcePoolSpec(self, value: ResourceConfigSpec):
            self._resourcePoolSpec = value
        @property
        def child(self) -> List[ImportSpec]: ...
        @child.setter
        def child(self, value: List[ImportSpec]):
            self._child = value


    class VmConfigInfo(vmodl.DynamicData):
        @property
        def product(self) -> List[vApp.ProductInfo]: ...
        @product.setter
        def product(self, value: List[vApp.ProductInfo]):
            self._product = value
        @property
        def property(self) -> List[vApp.PropertyInfo]: ...
        @property.setter
        def property(self, value: List[vApp.PropertyInfo]):
            self._property = value
        @property
        def ipAssignment(self) -> vApp.IPAssignmentInfo: ...
        @ipAssignment.setter
        def ipAssignment(self, value: vApp.IPAssignmentInfo):
            self._ipAssignment = value
        @property
        def eula(self) -> List[str]: ...
        @eula.setter
        def eula(self, value: List[str]):
            self._eula = value
        @property
        def ovfSection(self) -> List[vApp.OvfSectionInfo]: ...
        @ovfSection.setter
        def ovfSection(self, value: List[vApp.OvfSectionInfo]):
            self._ovfSection = value
        @property
        def ovfEnvironmentTransport(self) -> List[str]: ...
        @ovfEnvironmentTransport.setter
        def ovfEnvironmentTransport(self, value: List[str]):
            self._ovfEnvironmentTransport = value
        @property
        def installBootRequired(self) -> bool: ...
        @installBootRequired.setter
        def installBootRequired(self, value: bool):
            self._installBootRequired = value
        @property
        def installBootStopDelay(self) -> int: ...
        @installBootStopDelay.setter
        def installBootStopDelay(self, value: int):
            self._installBootStopDelay = value


    class VmConfigSpec(vmodl.DynamicData):
        @property
        def product(self) -> List[vApp.ProductSpec]: ...
        @product.setter
        def product(self, value: List[vApp.ProductSpec]):
            self._product = value
        @property
        def property(self) -> List[vApp.PropertySpec]: ...
        @property.setter
        def property(self, value: List[vApp.PropertySpec]):
            self._property = value
        @property
        def ipAssignment(self) -> vApp.IPAssignmentInfo: ...
        @ipAssignment.setter
        def ipAssignment(self, value: vApp.IPAssignmentInfo):
            self._ipAssignment = value
        @property
        def eula(self) -> List[str]: ...
        @eula.setter
        def eula(self, value: List[str]):
            self._eula = value
        @property
        def ovfSection(self) -> List[vApp.OvfSectionSpec]: ...
        @ovfSection.setter
        def ovfSection(self, value: List[vApp.OvfSectionSpec]):
            self._ovfSection = value
        @property
        def ovfEnvironmentTransport(self) -> List[str]: ...
        @ovfEnvironmentTransport.setter
        def ovfEnvironmentTransport(self, value: List[str]):
            self._ovfEnvironmentTransport = value
        @property
        def installBootRequired(self) -> bool: ...
        @installBootRequired.setter
        def installBootRequired(self, value: bool):
            self._installBootRequired = value
        @property
        def installBootStopDelay(self) -> int: ...
        @installBootStopDelay.setter
        def installBootStopDelay(self, value: int):
            self._installBootStopDelay = value


class DrsStatsManager():


    class InjectorWorkload():


        class CorrelationState(Enum):
            Correlated = "Correlated"
            Uncorrelated = "Uncorrelated"