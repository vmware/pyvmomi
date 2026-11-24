# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import action as action
from . import alarm as alarm
from . import cluster as cluster
from . import cns as cns
from . import dvs as dvs
from . import encryption as encryption
from . import event as event
from . import ext as ext
from . import fault as fault
from . import host as host
from . import net as net
from . import option as option
from . import profile as profile
from . import scheduler as scheduler
from . import storageDrs as storageDrs
from . import tenant as tenant
from . import vApp as vApp
from . import vcha as vcha
from . import view as view
from . import vm as vm
from . import vsan as vsan
from . import vslm as vslm

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vmodl
import pyVmomi.vim.alarm
import pyVmomi.vim.cluster
import pyVmomi.vim.dvs
import pyVmomi.vim.encryption
import pyVmomi.vim.event
import pyVmomi.vim.ext
import pyVmomi.vim.host
import pyVmomi.vim.option
import pyVmomi.vim.profile
import pyVmomi.vim.scheduler
import pyVmomi.vim.storageDrs
import pyVmomi.vim.tenant
import pyVmomi.vim.vApp
import pyVmomi.vim.vcha
import pyVmomi.vim.view
import pyVmomi.vim.vm
import pyVmomi.vim.vsan
import pyVmomi.vim.vslm
import pyVmomi.vmodl.query
import pyVmomi.vim.profile.cluster
import pyVmomi.vim.profile.host
import pyVmomi.vim.vm.check
import pyVmomi.vim.vm.customization
import pyVmomi.vim.vm.device
import pyVmomi.vim.vm.guest
import pyVmomi.vim.vsan.host



class AboutInfo(pyVmomi.vmodl.DynamicData):
   name: str
   fullName: str
   vendor: str
   version: str
   patchLevel: _typing.Optional[str] = None
   build: str
   localeVersion: _typing.Optional[str] = None
   localeBuild: _typing.Optional[str] = None
   osType: str
   productLineId: str
   apiType: str
   apiVersion: str
   instanceUuid: _typing.Optional[str] = None
   licenseProductName: _typing.Optional[str] = None
   licenseProductVersion: _typing.Optional[str] = None


class AuthorizationDescription(pyVmomi.vmodl.DynamicData):
   privilege: list[ElementDescription] = []
   privilegeGroup: list[ElementDescription] = []


class AuthorizationManager(pyVmomi.VmomiSupport.ManagedObject):
   class Permission(pyVmomi.vmodl.DynamicData):
      entity: _typing.Optional[ManagedEntity] = None
      principal: str
      group: bool
      roleId: int
      propagate: bool

   class Role(pyVmomi.vmodl.DynamicData):
      roleId: int
      system: bool
      name: str
      info: Description
      privilege: list[str] = []

   class Privilege(pyVmomi.vmodl.DynamicData):
      privId: str
      onParent: bool
      name: str
      privGroupName: str

   class PrivilegeAvailability(pyVmomi.vmodl.DynamicData):
      privId: str
      isGranted: bool

   class EntityPrivilege(pyVmomi.vmodl.DynamicData):
      entity: ManagedEntity
      privAvailability: list[PrivilegeAvailability] = []

   class UserPrivilegeResult(pyVmomi.vmodl.DynamicData):
      entity: ManagedEntity
      privileges: list[str] = []

   @property
   def privilegeList(self) -> list[Privilege]: ...
   @property
   def roleList(self) -> list[Role]: ...
   @property
   def description(self) -> AuthorizationDescription: ...

   def AddRole(self, name: str, privIds: list[str]) -> int: ...
   def RemoveRole(self, roleId: int, failIfUsed: bool) -> None: ...
   def UpdateRole(self, roleId: int, newName: str, privIds: list[str]) -> None: ...
   def MergePermissions(self, srcRoleId: int, dstRoleId: int) -> None: ...
   def RetrieveRolePermissions(self, roleId: int) -> list[Permission]: ...
   def RetrieveEntityPermissions(self, entity: ManagedEntity, inherited: bool) -> list[Permission]: ...
   def RetrieveAllPermissions(self) -> list[Permission]: ...
   def SetEntityPermissions(self, entity: ManagedEntity, permission: list[Permission]) -> None: ...
   def ResetEntityPermissions(self, entity: ManagedEntity, permission: list[Permission]) -> None: ...
   def RemoveEntityPermission(self, entity: ManagedEntity, user: str, isGroup: bool) -> None: ...
   def HasPrivilegeOnEntity(self, entity: ManagedEntity, sessionId: str, privId: list[str]) -> list[bool]: ...
   def HasPrivilegeOnEntities(self, entity: list[ManagedEntity], sessionId: str, privId: list[str]) -> list[EntityPrivilege]: ...
   def HasUserPrivilegeOnEntities(self, entities: list[pyVmomi.VmomiSupport.ManagedObject], userName: str, privId: list[str]) -> list[EntityPrivilege]: ...
   def FetchUserPrivilegeOnEntities(self, entities: list[ManagedEntity], userName: str) -> list[UserPrivilegeResult]: ...


class BatchResult(pyVmomi.vmodl.DynamicData):
   class Result(pyVmomi.VmomiSupport.Enum):
      success: _typing.ClassVar['Result'] = 'success'
      fail: _typing.ClassVar['Result'] = 'fail'

   result: str
   hostKey: str
   ds: _typing.Optional[Datastore] = None
   fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None


class BoolPolicy(InheritablePolicy):
   value: _typing.Optional[bool] = None


class Capability(pyVmomi.vmodl.DynamicData):
   provisioningSupported: bool
   multiHostSupported: bool
   userShellAccessSupported: bool
   supportedEVCMode: list[EVCMode] = []
   supportedEVCGraphicsMode: list[FeatureEVCMode] = []
   networkBackupAndRestoreSupported: _typing.Optional[bool] = None
   ftDrsWithoutEvcSupported: _typing.Optional[bool] = None
   hciWorkflowSupported: _typing.Optional[bool] = None
   computePolicyVersion: _typing.Optional[int] = None
   clusterPlacementSupported: _typing.Optional[bool] = None
   lifecycleManagementSupported: _typing.Optional[bool] = None
   hostSeedingSupported: _typing.Optional[bool] = None
   scalableSharesSupported: _typing.Optional[bool] = None
   hadcsSupported: _typing.Optional[bool] = None
   configMgmtSupported: _typing.Optional[bool] = None


class CertificateManager(pyVmomi.VmomiSupport.ManagedObject):
   def RefreshCACertificatesAndCRLs(self, host: list[HostSystem]) -> Task: ...
   def RefreshCertificates(self, host: list[HostSystem]) -> Task: ...
   def RevokeCertificates(self, host: list[HostSystem]) -> Task: ...


class ClusterComputeResource(ComputeResource):
   class Summary(ComputeResource.Summary):
      currentFailoverLevel: int
      admissionControlInfo: _typing.Optional[pyVmomi.vim.cluster.DasAdmissionControlInfo] = None
      numVmotions: int
      targetBalance: _typing.Optional[int] = None
      currentBalance: _typing.Optional[int] = None
      drsScore: _typing.Optional[int] = None
      numVmsPerDrsScoreBucket: list[int] = []
      usageSummary: _typing.Optional[pyVmomi.vim.cluster.UsageSummary] = None
      currentEVCModeKey: _typing.Optional[str] = None
      currentEVCGraphicsModeKey: _typing.Optional[str] = None
      dasData: _typing.Optional[pyVmomi.vim.cluster.DasData] = None
      clusterMaintenanceModeStatus: _typing.Optional[str] = None
      vcsHealthStatus: _typing.Optional[str] = None
      vcsSlots: list[VcsSlots] = []

   class DVSSetting(pyVmomi.vmodl.DynamicData):
      class DVPortgroupToServiceMapping(pyVmomi.vmodl.DynamicData):
         dvPortgroup: pyVmomi.vim.dvs.DistributedVirtualPortgroup
         service: str

      dvSwitch: DistributedVirtualSwitch
      pnicDevices: list[str] = []
      dvPortgroupSetting: list[DVPortgroupToServiceMapping] = []

   class HCIWorkflowState(pyVmomi.VmomiSupport.Enum):
      in_progress: _typing.ClassVar['HCIWorkflowState'] = 'in_progress'
      done: _typing.ClassVar['HCIWorkflowState'] = 'done'
      invalid: _typing.ClassVar['HCIWorkflowState'] = 'invalid'

   class HostConfigurationProfile(pyVmomi.vmodl.DynamicData):
      dateTimeConfig: _typing.Optional[pyVmomi.vim.host.DateTimeConfig] = None
      lockdownMode: _typing.Optional[pyVmomi.vim.host.HostAccessManager.LockdownMode] = None

   class HCIConfigInfo(pyVmomi.vmodl.DynamicData):
      workflowState: str
      dvsSetting: list[DVSSetting] = []
      configuredHosts: list[HostSystem] = []
      hostConfigProfile: _typing.Optional[HostConfigurationProfile] = None

   class ClusterConfigResult(pyVmomi.vmodl.DynamicData):
      failedHosts: list[Folder.FailedHostResult] = []
      configuredHosts: list[HostSystem] = []

   class DvsProfile(pyVmomi.vmodl.DynamicData):
      class DVPortgroupSpecToServiceMapping(pyVmomi.vmodl.DynamicData):
         dvPortgroupSpec: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigSpec] = None
         dvPortgroup: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPortgroup] = None
         service: str

      dvsName: _typing.Optional[str] = None
      dvSwitch: _typing.Optional[DistributedVirtualSwitch] = None
      pnicDevices: list[str] = []
      dvPortgroupMapping: list[DVPortgroupSpecToServiceMapping] = []

   class VCProfile(pyVmomi.vmodl.DynamicData):
      clusterSpec: _typing.Optional[pyVmomi.vim.cluster.ConfigSpecEx] = None
      evcModeKey: _typing.Optional[str] = None
      evcGraphicsModeKey: _typing.Optional[str] = None

   class HCIConfigSpec(pyVmomi.vmodl.DynamicData):
      dvsProf: list[DvsProfile] = []
      hostConfigProfile: _typing.Optional[HostConfigurationProfile] = None
      vSanConfigSpec: _typing.Optional[SDDCBase] = None
      vcProf: _typing.Optional[VCProfile] = None

   class HostVmkNicInfo(pyVmomi.vmodl.DynamicData):
      nicSpec: pyVmomi.vim.host.VirtualNic.Specification
      service: str

   class HostConfigurationInput(pyVmomi.vmodl.DynamicData):
      host: HostSystem
      hostVmkNics: list[HostVmkNicInfo] = []
      allowedInNonMaintenanceMode: _typing.Optional[bool] = None

   class ValidationResultBase(pyVmomi.vmodl.DynamicData):
      info: list[pyVmomi.vmodl.LocalizableMessage] = []

   class HostConfigurationValidation(ValidationResultBase):
      host: HostSystem
      isDvsSettingValid: _typing.Optional[bool] = None
      isVmknicSettingValid: _typing.Optional[bool] = None
      isNtpSettingValid: _typing.Optional[bool] = None
      isLockdownModeValid: _typing.Optional[bool] = None

   class DVSConfigurationValidation(ValidationResultBase):
      isDvsValid: bool
      isDvpgValid: bool

   class HostEvacuationInfo(pyVmomi.vmodl.DynamicData):
      host: HostSystem
      action: list[pyVmomi.vim.option.OptionValue] = []

   class MaintenanceInfo(pyVmomi.vmodl.DynamicData):
      partialMMId: _typing.Optional[str] = None
      hostEvacInfo: list[HostEvacuationInfo] = []

   class CryptoModePolicy(pyVmomi.vmodl.DynamicData):
      keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId] = None
      providerId: _typing.Optional[pyVmomi.vim.encryption.KeyProviderId] = None

   class VcsHealthStatus(pyVmomi.VmomiSupport.Enum):
      healthy: _typing.ClassVar['VcsHealthStatus'] = 'healthy'
      degraded: _typing.ClassVar['VcsHealthStatus'] = 'degraded'
      nonhealthy: _typing.ClassVar['VcsHealthStatus'] = 'nonhealthy'

   class VcsSlots(pyVmomi.vmodl.DynamicData):
      systemId: _typing.Optional[str] = None
      host: HostSystem
      datastore: list[Datastore] = []
      totalSlots: int

   @property
   def configuration(self) -> pyVmomi.vim.cluster.ConfigInfo: ...
   @property
   def recommendation(self) -> list[pyVmomi.vim.cluster.Recommendation]: ...
   @property
   def drsRecommendation(self) -> list[pyVmomi.vim.cluster.DrsRecommendation]: ...
   @property
   def summaryEx(self) -> Summary: ...
   @property
   def hciConfig(self) -> _typing.Optional[HCIConfigInfo]: ...
   @property
   def migrationHistory(self) -> list[pyVmomi.vim.cluster.DrsMigration]: ...
   @property
   def actionHistory(self) -> list[pyVmomi.vim.cluster.ActionHistory]: ...
   @property
   def drsFault(self) -> list[pyVmomi.vim.cluster.DrsFaults]: ...

   def ConfigureHCI(self, clusterSpec: HCIConfigSpec, hostInputs: list[HostConfigurationInput]) -> Task: ...
   def ExtendHCI(self, hostInputs: list[HostConfigurationInput], vSanConfigSpec: _typing.Optional[SDDCBase]) -> Task: ...
   def AbandonHciWorkflow(self) -> None: ...
   def ValidateHCIConfiguration(self, hciConfigSpec: _typing.Optional[HCIConfigSpec], hosts: list[HostSystem]) -> list[ValidationResultBase]: ...
   def Reconfigure(self, spec: pyVmomi.vim.cluster.ConfigSpec, modify: bool) -> Task: ...
   def ApplyRecommendation(self, key: str) -> None: ...
   def CancelRecommendation(self, key: str) -> None: ...
   def RecommendHostsForVm(self, vm: VirtualMachine, pool: _typing.Optional[ResourcePool]) -> list[pyVmomi.vim.cluster.HostRecommendation]: ...
   def AddHost(self, spec: pyVmomi.vim.host.ConnectSpec, asConnected: bool, resourcePool: _typing.Optional[ResourcePool], license: _typing.Optional[str]) -> Task: ...
   def MoveInto(self, host: list[HostSystem]) -> Task: ...
   def MoveHostInto(self, host: HostSystem, resourcePool: _typing.Optional[ResourcePool]) -> Task: ...
   def RefreshRecommendation(self) -> None: ...
   def EvcManager(self) -> _typing.Optional[pyVmomi.vim.cluster.EVCManager]: ...
   def RetrieveDasAdvancedRuntimeInfo(self) -> _typing.Optional[pyVmomi.vim.cluster.DasAdvancedRuntimeInfo]: ...
   def EnterMaintenanceMode(self, host: list[HostSystem], option: list[pyVmomi.vim.option.OptionValue], info: _typing.Optional[MaintenanceInfo]) -> pyVmomi.vim.cluster.EnterMaintenanceResult: ...
   def PlaceVm(self, placementSpec: pyVmomi.vim.cluster.PlacementSpec) -> pyVmomi.vim.cluster.PlacementResult: ...
   def FindRulesForVm(self, vm: VirtualMachine) -> list[pyVmomi.vim.cluster.RuleInfo]: ...
   def StampAllRulesWithUuid(self) -> Task: ...
   def GetResourceUsage(self) -> pyVmomi.vim.cluster.ResourceUsageSummary: ...
   def SetCryptoMode(self, cryptoMode: str, policy: _typing.Optional[CryptoModePolicy]) -> None: ...
   def GetSystemVMsRestrictedDatastores(self) -> list[Datastore]: ...


class ComputeResource(ManagedEntity):
   class Summary(pyVmomi.vmodl.DynamicData):
      totalCpu: int
      totalMemory: pyVmomi.VmomiSupport.long
      numCpuCores: pyVmomi.VmomiSupport.short
      numCpuThreads: pyVmomi.VmomiSupport.short
      effectiveCpu: int
      effectiveMemory: pyVmomi.VmomiSupport.long
      numHosts: int
      numEffectiveHosts: int
      overallStatus: ManagedEntity.Status

   class NetworkBootMode(pyVmomi.VmomiSupport.Enum):
      bootstrap: _typing.ClassVar['NetworkBootMode'] = 'bootstrap'
      stateless: _typing.ClassVar['NetworkBootMode'] = 'stateless'

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      vmSwapPlacement: str
      spbmEnabled: _typing.Optional[bool] = None
      defaultHardwareVersionKey: _typing.Optional[str] = None
      maximumHardwareVersionKey: _typing.Optional[str] = None

   class HostSPBMLicenseInfo(pyVmomi.vmodl.DynamicData):
      class HostSPBMLicenseState(pyVmomi.VmomiSupport.Enum):
         licensed: _typing.ClassVar['HostSPBMLicenseState'] = 'licensed'
         unlicensed: _typing.ClassVar['HostSPBMLicenseState'] = 'unlicensed'
         unknown: _typing.ClassVar['HostSPBMLicenseState'] = 'unknown'

      host: HostSystem
      licenseState: HostSPBMLicenseState

   class HostSeedSpec(pyVmomi.vmodl.DynamicData):
      class SingleHostSpec(pyVmomi.vmodl.DynamicData):
         newHostCnxSpec: _typing.Optional[pyVmomi.vim.host.ConnectSpec] = None
         existingHost: _typing.Optional[HostSystem] = None

      singleHostSpec: SingleHostSpec

   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      vmSwapPlacement: _typing.Optional[str] = None
      spbmEnabled: _typing.Optional[bool] = None
      defaultHardwareVersionKey: _typing.Optional[str] = None
      desiredSoftwareSpec: _typing.Optional[DesiredSoftwareSpec] = None
      maximumHardwareVersionKey: _typing.Optional[str] = None
      enableConfigManager: _typing.Optional[bool] = None
      hostSeedSpec: _typing.Optional[HostSeedSpec] = None
      softwareSpecId: _typing.Optional[str] = None
      networkBootMode: _typing.Optional[str] = None

   @property
   def resourcePool(self) -> _typing.Optional[ResourcePool]: ...
   @property
   def host(self) -> list[HostSystem]: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def environmentBrowser(self) -> _typing.Optional[EnvironmentBrowser]: ...
   @property
   def configurationEx(self) -> ConfigInfo: ...
   @property
   def lifecycleManaged(self) -> _typing.Optional[bool]: ...
   @property
   def configManagerEnabled(self) -> _typing.Optional[bool]: ...
   @property
   def networkBootMode(self) -> _typing.Optional[str]: ...

   def EnableNetworkBoot(self, networkBootMode: str) -> Task: ...
   def DisableNetworkBoot(self) -> Task: ...
   def ReconfigureEx(self, spec: ConfigSpec, modify: bool) -> Task: ...

class ConfigSpecOperation:
   pass


class CustomFieldsManager(pyVmomi.VmomiSupport.ManagedObject):
   class FieldDef(pyVmomi.vmodl.DynamicData):
      key: int
      name: str
      type: type
      managedObjectType: _typing.Optional[type] = None
      fieldDefPrivileges: _typing.Optional[PrivilegePolicyDef] = None
      fieldInstancePrivileges: _typing.Optional[PrivilegePolicyDef] = None

   class Value(pyVmomi.vmodl.DynamicData):
      key: int

   class StringValue(Value):
      value: str

   @property
   def field(self) -> list[FieldDef]: ...

   def AddFieldDefinition(self, name: str, moType: _typing.Optional[type], fieldDefPolicy: _typing.Optional[PrivilegePolicyDef], fieldPolicy: _typing.Optional[PrivilegePolicyDef]) -> FieldDef: ...
   def RemoveFieldDefinition(self, key: int) -> None: ...
   def RenameFieldDefinition(self, key: int, name: str) -> None: ...
   def SetField(self, entity: ManagedEntity, key: int, value: str) -> None: ...


class CustomizationSpecInfo(pyVmomi.vmodl.DynamicData):
   name: str
   description: str
   type: str
   changeVersion: _typing.Optional[str] = None
   lastUpdateTime: _typing.Optional[_datetime.datetime] = None


class CustomizationSpecItem(pyVmomi.vmodl.DynamicData):
   info: CustomizationSpecInfo
   spec: pyVmomi.vim.vm.customization.Specification


class CustomizationSpecManager(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def info(self) -> list[CustomizationSpecInfo]: ...
   @property
   def encryptionKey(self) -> list[pyVmomi.VmomiSupport.byte]: ...

   def Exists(self, name: str) -> bool: ...
   def Get(self, name: str) -> CustomizationSpecItem: ...
   def Create(self, item: CustomizationSpecItem) -> None: ...
   def Overwrite(self, item: CustomizationSpecItem) -> None: ...
   def Delete(self, name: str) -> None: ...
   def Duplicate(self, name: str, newName: str) -> None: ...
   def Rename(self, name: str, newName: str) -> None: ...
   def SpecItemToXml(self, item: CustomizationSpecItem) -> str: ...
   def XmlToSpecItem(self, specItemXml: str) -> CustomizationSpecItem: ...
   def CheckResources(self, guestOs: str) -> None: ...
   def IsGuestOsCustomizable(self, guestId: str) -> bool: ...


class Datacenter(ManagedEntity):
   class BasicConnectInfo(pyVmomi.vmodl.DynamicData):
      hostname: _typing.Optional[str] = None
      error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
      serverIp: _typing.Optional[str] = None
      numVm: _typing.Optional[int] = None
      numPoweredOnVm: _typing.Optional[int] = None
      hostProductInfo: _typing.Optional[AboutInfo] = None
      hardwareVendor: _typing.Optional[str] = None
      hardwareModel: _typing.Optional[str] = None

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      defaultHardwareVersionKey: _typing.Optional[str] = None
      maximumHardwareVersionKey: _typing.Optional[str] = None

   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      defaultHardwareVersionKey: _typing.Optional[str] = None
      maximumHardwareVersionKey: _typing.Optional[str] = None

   @property
   def vmFolder(self) -> Folder: ...
   @property
   def hostFolder(self) -> Folder: ...
   @property
   def datastoreFolder(self) -> Folder: ...
   @property
   def networkFolder(self) -> Folder: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def configuration(self) -> ConfigInfo: ...

   def BatchQueryConnectInfo(self, hostSpecs: list[pyVmomi.vim.host.ConnectSpec]) -> list[BasicConnectInfo]: ...
   def QueryConnectionInfo(self, hostname: str, port: int, username: str, password: str, sslThumbprint: _typing.Optional[str], sslCertificate: _typing.Optional[str]) -> pyVmomi.vim.host.ConnectInfo: ...
   def QueryConnectionInfoViaSpec(self, spec: pyVmomi.vim.host.ConnectSpec) -> pyVmomi.vim.host.ConnectInfo: ...
   def PowerOnVm(self, vm: list[VirtualMachine], option: list[pyVmomi.vim.option.OptionValue]) -> Task: ...
   def QueryConfigOptionDescriptor(self) -> list[pyVmomi.vim.vm.ConfigOptionDescriptor]: ...
   def Reconfigure(self, spec: ConfigSpec, modify: bool) -> Task: ...


class Datastore(ManagedEntity):
   class Accessible(pyVmomi.VmomiSupport.Enum):
      # Reserved python keyword: commenting out.
      # True: _typing.ClassVar['Accessible'] = 'True'
      # Reserved python keyword: commenting out.
      # False: _typing.ClassVar['Accessible'] = 'False'
      pass

   class SectorFormat(pyVmomi.VmomiSupport.Enum):
      native_512: _typing.ClassVar['SectorFormat'] = 'native_512'
      emulated_512: _typing.ClassVar['SectorFormat'] = 'emulated_512'
      native_4k: _typing.ClassVar['SectorFormat'] = 'native_4k'

   class Summary(pyVmomi.vmodl.DynamicData):
      class MaintenanceModeState(pyVmomi.VmomiSupport.Enum):
         normal: _typing.ClassVar['MaintenanceModeState'] = 'normal'
         enteringMaintenance: _typing.ClassVar['MaintenanceModeState'] = 'enteringMaintenance'
         inMaintenance: _typing.ClassVar['MaintenanceModeState'] = 'inMaintenance'

      datastore: _typing.Optional[Datastore] = None
      name: str
      url: str
      capacity: pyVmomi.VmomiSupport.long
      freeSpace: pyVmomi.VmomiSupport.long
      uncommitted: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      accessible: bool
      multipleHostAccess: _typing.Optional[bool] = None
      type: str
      maintenanceMode: _typing.Optional[str] = None

   class Info(pyVmomi.vmodl.DynamicData):
      name: str
      url: str
      freeSpace: pyVmomi.VmomiSupport.long
      maxFileSize: pyVmomi.VmomiSupport.long
      maxVirtualDiskCapacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      maxMemoryFileSize: pyVmomi.VmomiSupport.long
      timestamp: _typing.Optional[_datetime.datetime] = None
      containerId: _typing.Optional[str] = None
      aliasOf: _typing.Optional[str] = None
      supportedVDiskFormats: list[str] = []
      logicalSectorSize: _typing.Optional[int] = None
      physicalSectorSize: _typing.Optional[int] = None

   class Capability(pyVmomi.vmodl.DynamicData):
      directoryHierarchySupported: bool
      rawDiskMappingsSupported: bool
      perFileThinProvisioningSupported: bool
      storageIORMSupported: bool
      nativeSnapshotSupported: bool
      topLevelDirectoryCreateSupported: _typing.Optional[bool] = None
      seSparseSupported: _typing.Optional[bool] = None
      vmfsSparseSupported: _typing.Optional[bool] = None
      vsanSparseSupported: _typing.Optional[bool] = None
      upitSupported: _typing.Optional[bool] = None
      vmdkExpandSupported: _typing.Optional[bool] = None
      clusteredVmdkSupported: _typing.Optional[bool] = None

   class HostMount(pyVmomi.vmodl.DynamicData):
      key: HostSystem
      mountInfo: pyVmomi.vim.host.MountInfo

   class MountPathDatastorePair(pyVmomi.vmodl.DynamicData):
      oldMountPath: str
      datastore: Datastore

   class VVolContainerFailoverPair(pyVmomi.vmodl.DynamicData):
      srcContainer: _typing.Optional[str] = None
      tgtContainer: str
      vvolMapping: list[KeyValue] = []

   @property
   def info(self) -> Info: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def host(self) -> list[HostMount]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...
   @property
   def browser(self) -> pyVmomi.vim.host.DatastoreBrowser: ...
   @property
   def capability(self) -> Capability: ...
   @property
   def iormConfiguration(self) -> _typing.Optional[StorageResourceManager.IORMConfigInfo]: ...

   def Refresh(self) -> None: ...
   def RefreshStorageInfo(self) -> None: ...
   def UpdateVirtualMachineFiles(self, mountPathDatastoreMapping: list[MountPathDatastorePair]) -> Task: ...
   def RenameDatastore(self, newName: str) -> None: ...
   def DestroyDatastore(self) -> None: ...
   def EnterMaintenanceMode(self) -> pyVmomi.vim.storageDrs.StoragePlacementResult: ...
   def ExitMaintenanceMode(self) -> Task: ...
   def IsClusteredVmdkEnabled(self) -> bool: ...
   def UpdateVVolVirtualMachineFiles(self, failoverPair: list[VVolContainerFailoverPair]) -> Task: ...


class DatastoreNamespaceManager(pyVmomi.VmomiSupport.ManagedObject):
   class DirectoryInfo(pyVmomi.vmodl.DynamicData):
      capacity: pyVmomi.VmomiSupport.long
      used: pyVmomi.VmomiSupport.long

   def CreateDirectory(self, datastore: Datastore, displayName: _typing.Optional[str], policy: _typing.Optional[str], size: _typing.Optional[pyVmomi.VmomiSupport.long]) -> str: ...
   def DeleteDirectory(self, datacenter: _typing.Optional[Datacenter], datastorePath: str) -> None: ...
   def ConvertNamespacePathToUuidPath(self, datacenter: _typing.Optional[Datacenter], namespaceUrl: str) -> str: ...
   def IncreaseDirectorySize(self, datacenter: _typing.Optional[Datacenter], stableName: str, size: pyVmomi.VmomiSupport.long) -> None: ...
   def QueryDirectoryInfo(self, datacenter: _typing.Optional[Datacenter], stableName: str) -> DirectoryInfo: ...


class Description(pyVmomi.vmodl.DynamicData):
   label: str
   summary: str


class DesiredSoftwareSpec(pyVmomi.vmodl.DynamicData):
   class BaseImageSpec(pyVmomi.vmodl.DynamicData):
      version: str

   class VendorAddOnSpec(pyVmomi.vmodl.DynamicData):
      name: str
      version: str

   class ComponentSpec(pyVmomi.vmodl.DynamicData):
      name: str
      version: _typing.Optional[str] = None

   baseImageSpec: BaseImageSpec
   vendorAddOnSpec: _typing.Optional[VendorAddOnSpec] = None
   components: list[ComponentSpec] = []
   removedComponents: list[str] = []


class DiagnosticManager(pyVmomi.VmomiSupport.ManagedObject):
   class LogDescriptor(pyVmomi.vmodl.DynamicData):
      class Creator(pyVmomi.VmomiSupport.Enum):
         vpxd: _typing.ClassVar['Creator'] = 'vpxd'
         vpxa: _typing.ClassVar['Creator'] = 'vpxa'
         hostd: _typing.ClassVar['Creator'] = 'hostd'
         serverd: _typing.ClassVar['Creator'] = 'serverd'
         install: _typing.ClassVar['Creator'] = 'install'
         vpxClient: _typing.ClassVar['Creator'] = 'vpxClient'
         recordLog: _typing.ClassVar['Creator'] = 'recordLog'

      class Format(pyVmomi.VmomiSupport.Enum):
         plain: _typing.ClassVar['Format'] = 'plain'

      key: str
      fileName: str
      creator: str
      format: str
      mimeType: str
      info: Description

   class LogHeader(pyVmomi.vmodl.DynamicData):
      lineStart: int
      lineEnd: int
      lineText: list[str] = []

   class BundleInfo(pyVmomi.vmodl.DynamicData):
      system: _typing.Optional[HostSystem] = None
      url: str

   class AuditRecordResult(pyVmomi.vmodl.DynamicData):
      records: list[str] = []
      nextToken: str

   def QueryDescriptions(self, host: _typing.Optional[HostSystem]) -> list[LogDescriptor]: ...
   def Browse(self, host: _typing.Optional[HostSystem], key: str, start: _typing.Optional[int], lines: _typing.Optional[int]) -> LogHeader: ...
   def GenerateLogBundles(self, includeDefault: bool, host: list[HostSystem]) -> Task: ...
   def FetchAuditRecords(self, token: _typing.Optional[str]) -> AuditRecordResult: ...
   def EmitSyslogMark(self, message: str) -> None: ...


class DirectPathProfileManager(pyVmomi.VmomiSupport.ManagedObject):
   class DirectPathConfig(pyVmomi.vmodl.DynamicData):
      pass

   class VmiopDirectPathConfig(DirectPathConfig):
      vgpuProfile: str

   class DvxDirectPathConfig(DirectPathConfig):
      dvxBacking: pyVmomi.vim.vm.device.VirtualPCIPassthrough.DvxBackingInfo

   class DynamicDirectPathConfig(DirectPathConfig):
      dynamicDirectPathBacking: pyVmomi.vim.vm.device.VirtualPCIPassthrough.DynamicBackingInfo

   class VirtualDeviceGroupDirectPathConfig(DirectPathConfig):
      deviceGroupName: str

   class CreateSpec(pyVmomi.vmodl.DynamicData):
      name: str
      description: _typing.Optional[str] = None
      deviceConfig: DirectPathConfig

   class UpdateSpec(pyVmomi.vmodl.DynamicData):
      name: _typing.Optional[str] = None
      description: _typing.Optional[str] = None

   class FilterSpec(pyVmomi.vmodl.DynamicData):
      ids: list[str] = []
      names: list[str] = []
      clusters: list[ClusterComputeResource] = []

   class DirectPathProfileInfo(pyVmomi.vmodl.DynamicData):
      id: str
      name: str
      description: _typing.Optional[str] = None
      vendorName: str
      deviceConfig: DirectPathConfig

   class TargetEntity(pyVmomi.vmodl.DynamicData):
      pass

   class TargetHost(TargetEntity):
      host: HostSystem

   class TargetCluster(TargetEntity):
      cluster: ClusterComputeResource

   class CapacityQuerySpec(pyVmomi.vmodl.DynamicData):
      pass

   class CapacityQueryById(CapacityQuerySpec):
      id: str

   class CapacityQueryByName(CapacityQuerySpec):
      name: str

   class CapacityQueryByDeviceConfig(CapacityQuerySpec):
      deviceConfig: DirectPathConfig

   class CapacityResult(pyVmomi.vmodl.DynamicData):
      pass

   class CapacityInfo(CapacityResult):
      profile: DirectPathProfileInfo
      consumed: int
      remaining: int
      max: int
      unusedReservation: int

   class CapacityUnknown(CapacityResult):
      querySpec: CapacityQuerySpec
      faultList: list[pyVmomi.vmodl.MethodFault] = []

   def CreateDirectPathProfile(self, spec: CreateSpec) -> str: ...
   def UpdateDirectPathProfile(self, id: str, spec: UpdateSpec) -> None: ...
   def DeleteDirectPathProfile(self, id: str) -> None: ...
   def ListDirectPathProfiles(self, filterSpec: FilterSpec) -> list[DirectPathProfileInfo]: ...
   def QueryDirectPathProfileCapacity(self, target: TargetEntity, querySpec: list[CapacityQuerySpec]) -> list[CapacityResult]: ...


class DistributedVirtualSwitch(ManagedEntity):
   class ProductSpecOperationType(pyVmomi.VmomiSupport.Enum):
      preInstall: _typing.ClassVar['ProductSpecOperationType'] = 'preInstall'
      upgrade: _typing.ClassVar['ProductSpecOperationType'] = 'upgrade'
      notifyAvailableUpgrade: _typing.ClassVar['ProductSpecOperationType'] = 'notifyAvailableUpgrade'
      proceedWithUpgrade: _typing.ClassVar['ProductSpecOperationType'] = 'proceedWithUpgrade'
      updateBundleInfo: _typing.ClassVar['ProductSpecOperationType'] = 'updateBundleInfo'

   class ContactInfo(pyVmomi.vmodl.DynamicData):
      name: _typing.Optional[str] = None
      contact: _typing.Optional[str] = None

   class NicTeamingPolicyMode(pyVmomi.VmomiSupport.Enum):
      loadbalance_ip: _typing.ClassVar['NicTeamingPolicyMode'] = 'loadbalance_ip'
      loadbalance_srcmac: _typing.ClassVar['NicTeamingPolicyMode'] = 'loadbalance_srcmac'
      loadbalance_srcid: _typing.ClassVar['NicTeamingPolicyMode'] = 'loadbalance_srcid'
      failover_explicit: _typing.ClassVar['NicTeamingPolicyMode'] = 'failover_explicit'
      loadbalance_loadbased: _typing.ClassVar['NicTeamingPolicyMode'] = 'loadbalance_loadbased'

   class NetworkResourceManagementCapability(pyVmomi.vmodl.DynamicData):
      networkResourceManagementSupported: bool
      networkResourcePoolHighShareValue: int
      qosSupported: bool
      userDefinedNetworkResourcePoolsSupported: bool
      networkResourceControlVersion3Supported: _typing.Optional[bool] = None
      userDefinedInfraTrafficPoolSupported: _typing.Optional[bool] = None

   class RollbackCapability(pyVmomi.vmodl.DynamicData):
      rollbackSupported: bool

   class BackupRestoreCapability(pyVmomi.vmodl.DynamicData):
      backupRestoreSupported: bool

   class FeatureCapability(pyVmomi.vmodl.DynamicData):
      networkResourceManagementSupported: bool
      vmDirectPathGen2Supported: _typing.Optional[bool] = None
      nicTeamingPolicy: list[str] = []
      networkResourcePoolHighShareValue: _typing.Optional[int] = None
      networkResourceManagementCapability: _typing.Optional[NetworkResourceManagementCapability] = None
      healthCheckCapability: _typing.Optional[HealthCheckFeatureCapability] = None
      rollbackCapability: _typing.Optional[RollbackCapability] = None
      backupRestoreCapability: _typing.Optional[BackupRestoreCapability] = None
      networkFilterSupported: _typing.Optional[bool] = None
      macLearningSupported: _typing.Optional[bool] = None

   class HealthCheckFeatureCapability(pyVmomi.vmodl.DynamicData):
      pass

   class Capability(pyVmomi.vmodl.DynamicData):
      dvsOperationSupported: _typing.Optional[bool] = None
      dvPortGroupOperationSupported: _typing.Optional[bool] = None
      dvPortOperationSupported: _typing.Optional[bool] = None
      compatibleHostComponentProductInfo: list[pyVmomi.vim.dvs.HostProductSpec] = []
      featuresSupported: _typing.Optional[FeatureCapability] = None

   class Summary(pyVmomi.vmodl.DynamicData):
      name: str
      uuid: str
      numPorts: int
      productInfo: _typing.Optional[pyVmomi.vim.dvs.ProductSpec] = None
      hostMember: list[HostSystem] = []
      vm: list[VirtualMachine] = []
      host: list[HostSystem] = []
      portgroupName: list[str] = []
      description: _typing.Optional[str] = None
      contact: _typing.Optional[ContactInfo] = None
      numHosts: _typing.Optional[int] = None

   class SwitchPolicy(pyVmomi.vmodl.DynamicData):
      autoPreInstallAllowed: _typing.Optional[bool] = None
      autoUpgradeAllowed: _typing.Optional[bool] = None
      partialUpgradeAllowed: _typing.Optional[bool] = None

   class UplinkPortPolicy(pyVmomi.vmodl.DynamicData):
      pass

   class NameArrayUplinkPortPolicy(UplinkPortPolicy):
      uplinkPortName: list[str] = []

   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      configVersion: _typing.Optional[str] = None
      name: _typing.Optional[str] = None
      numStandalonePorts: _typing.Optional[int] = None
      maxPorts: _typing.Optional[int] = None
      uplinkPortPolicy: _typing.Optional[UplinkPortPolicy] = None
      uplinkPortgroup: list[pyVmomi.vim.dvs.DistributedVirtualPortgroup] = []
      defaultPortConfig: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPort.Setting] = None
      host: list[pyVmomi.vim.dvs.HostMember.ConfigSpec] = []
      extensionKey: _typing.Optional[str] = None
      description: _typing.Optional[str] = None
      policy: _typing.Optional[SwitchPolicy] = None
      vendorSpecificConfig: list[pyVmomi.vim.dvs.KeyedOpaqueBlob] = []
      contact: _typing.Optional[ContactInfo] = None
      switchIpAddress: _typing.Optional[str] = None
      defaultProxySwitchMaxNumPorts: _typing.Optional[int] = None
      infrastructureTrafficResourceConfig: list[HostInfrastructureTrafficResource] = []
      netResourcePoolTrafficResourceConfig: list[HostInfrastructureTrafficResource] = []
      networkResourceControlVersion: _typing.Optional[str] = None

   class CreateSpec(pyVmomi.vmodl.DynamicData):
      configSpec: ConfigSpec
      productInfo: _typing.Optional[pyVmomi.vim.dvs.ProductSpec] = None
      capability: _typing.Optional[Capability] = None

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      uuid: str
      name: str
      numStandalonePorts: int
      numPorts: int
      maxPorts: int
      uplinkPortPolicy: UplinkPortPolicy
      uplinkPortgroup: list[pyVmomi.vim.dvs.DistributedVirtualPortgroup] = []
      defaultPortConfig: pyVmomi.vim.dvs.DistributedVirtualPort.Setting
      host: list[pyVmomi.vim.dvs.HostMember] = []
      productInfo: pyVmomi.vim.dvs.ProductSpec
      targetInfo: _typing.Optional[pyVmomi.vim.dvs.ProductSpec] = None
      extensionKey: _typing.Optional[str] = None
      vendorSpecificConfig: list[pyVmomi.vim.dvs.KeyedOpaqueBlob] = []
      policy: _typing.Optional[SwitchPolicy] = None
      description: _typing.Optional[str] = None
      configVersion: str
      contact: ContactInfo
      switchIpAddress: _typing.Optional[str] = None
      createTime: _datetime.datetime
      networkResourceManagementEnabled: bool
      defaultProxySwitchMaxNumPorts: _typing.Optional[int] = None
      healthCheckConfig: list[HealthCheckConfig] = []
      infrastructureTrafficResourceConfig: list[HostInfrastructureTrafficResource] = []
      netResourcePoolTrafficResourceConfig: list[HostInfrastructureTrafficResource] = []
      networkResourceControlVersion: _typing.Optional[str] = None
      vmVnicNetworkResourcePool: list[pyVmomi.vim.dvs.VmVnicNetworkResourcePool] = []
      pnicCapacityRatioForReservation: _typing.Optional[int] = None

   class NetworkResourceControlVersion(pyVmomi.VmomiSupport.Enum):
      version2: _typing.ClassVar['NetworkResourceControlVersion'] = 'version2'
      version3: _typing.ClassVar['NetworkResourceControlVersion'] = 'version3'

   class HostInfrastructureTrafficClass(pyVmomi.VmomiSupport.Enum):
      management: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'management'
      faultTolerance: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'faultTolerance'
      vmotion: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'vmotion'
      virtualMachine: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'virtualMachine'
      iSCSI: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'iSCSI'
      nfs: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'nfs'
      hbr: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'hbr'
      vsan: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'vsan'
      vdp: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'vdp'
      backupNfc: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'backupNfc'
      nvmetcp: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'nvmetcp'
      provisioning: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'provisioning'
      vSANiSCSI: _typing.ClassVar['HostInfrastructureTrafficClass'] = 'vSANiSCSI'

   class HostInfrastructureTrafficResource(pyVmomi.vmodl.DynamicData):
      class ResourceAllocation(pyVmomi.vmodl.DynamicData):
         limit: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         shares: _typing.Optional[SharesInfo] = None
         reservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None

      key: str
      description: _typing.Optional[str] = None
      allocationInfo: ResourceAllocation

   class HealthCheckConfig(pyVmomi.vmodl.DynamicData):
      enable: _typing.Optional[bool] = None
      interval: _typing.Optional[int] = None

   class ResourceRuntimeInfo(pyVmomi.vmodl.DynamicData):
      capacity: _typing.Optional[int] = None
      usage: _typing.Optional[int] = None
      available: _typing.Optional[int] = None
      allocatedResource: list[pyVmomi.vim.dvs.VmVnicNetworkResourcePool.VnicAllocatedResource] = []
      vmVnicNetworkResourcePoolRuntime: list[pyVmomi.vim.dvs.VmVnicNetworkResourcePool.RuntimeInfo] = []

   class RuntimeInfo(pyVmomi.vmodl.DynamicData):
      hostMemberRuntime: list[pyVmomi.vim.dvs.HostMember.RuntimeInfo] = []
      resourceRuntimeInfo: _typing.Optional[ResourceRuntimeInfo] = None

   @property
   def uuid(self) -> str: ...
   @property
   def capability(self) -> Capability: ...
   @property
   def summary(self) -> Summary: ...
   @property
   def config(self) -> ConfigInfo: ...
   @property
   def networkResourcePool(self) -> list[pyVmomi.vim.dvs.NetworkResourcePool]: ...
   @property
   def portgroup(self) -> list[pyVmomi.vim.dvs.DistributedVirtualPortgroup]: ...
   @property
   def runtime(self) -> _typing.Optional[RuntimeInfo]: ...

   def FetchPortKeys(self, criteria: _typing.Optional[pyVmomi.vim.dvs.PortCriteria]) -> list[str]: ...
   def FetchPorts(self, criteria: _typing.Optional[pyVmomi.vim.dvs.PortCriteria]) -> list[pyVmomi.vim.dvs.DistributedVirtualPort]: ...
   def QueryUsedVlanId(self) -> list[int]: ...
   def Reconfigure(self, spec: ConfigSpec) -> Task: ...
   def PerformProductSpecOperation(self, operation: str, productSpec: _typing.Optional[pyVmomi.vim.dvs.ProductSpec]) -> Task: ...
   def Merge(self, dvs: DistributedVirtualSwitch) -> Task: ...
   def AddPortgroups(self, spec: list[pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigSpec]) -> Task: ...
   def MovePort(self, portKey: list[str], destinationPortgroupKey: _typing.Optional[str]) -> Task: ...
   def UpdateCapability(self, capability: Capability) -> None: ...
   def ReconfigurePort(self, port: list[pyVmomi.vim.dvs.DistributedVirtualPort.ConfigSpec]) -> Task: ...
   def RefreshPortState(self, portKeys: list[str]) -> None: ...
   def RectifyHost(self, hosts: list[HostSystem]) -> Task: ...
   def UpdateNetworkResourcePool(self, configSpec: list[pyVmomi.vim.dvs.NetworkResourcePool.ConfigSpec]) -> None: ...
   def AddNetworkResourcePool(self, configSpec: list[pyVmomi.vim.dvs.NetworkResourcePool.ConfigSpec]) -> None: ...
   def RemoveNetworkResourcePool(self, key: list[str]) -> None: ...
   def ReconfigureVmVnicNetworkResourcePool(self, configSpec: list[pyVmomi.vim.dvs.VmVnicNetworkResourcePool.ConfigSpec]) -> Task: ...
   def EnableNetworkResourceManagement(self, enable: bool) -> None: ...
   def Rollback(self, entityBackup: _typing.Optional[pyVmomi.vim.dvs.EntityBackup.Config]) -> Task: ...
   def AddPortgroup(self, spec: pyVmomi.vim.dvs.DistributedVirtualPortgroup.ConfigSpec) -> Task: ...
   def UpdateHealthCheckConfig(self, healthCheckConfig: list[HealthCheckConfig]) -> Task: ...
   def LookupPortgroup(self, portgroupKey: str) -> _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualPortgroup]: ...


class EVCMode(ElementDescription):
   guaranteedCPUFeatures: list[pyVmomi.vim.host.CpuIdInfo] = []
   featureCapability: list[pyVmomi.vim.host.FeatureCapability] = []
   featureMask: list[pyVmomi.vim.host.FeatureMask] = []
   featureRequirement: list[pyVmomi.vim.vm.FeatureRequirement] = []
   vendor: str
   track: list[str] = []
   vendorTier: int

class ElementDescription(Description):
   key: str


class EnumDescription(pyVmomi.vmodl.DynamicData):
   key: type
   tags: list[ElementDescription] = []


class EnvironmentBrowser(pyVmomi.VmomiSupport.ManagedObject):
   class ConfigOptionQuerySpec(pyVmomi.vmodl.DynamicData):
      key: _typing.Optional[str] = None
      host: _typing.Optional[HostSystem] = None
      guestId: list[str] = []

   @property
   def datastoreBrowser(self) -> _typing.Optional[pyVmomi.vim.host.DatastoreBrowser]: ...

   def QueryConfigOptionDescriptor(self) -> list[pyVmomi.vim.vm.ConfigOptionDescriptor]: ...
   def QueryConfigOption(self, key: _typing.Optional[str], host: _typing.Optional[HostSystem]) -> _typing.Optional[pyVmomi.vim.vm.ConfigOption]: ...
   def QueryConfigOptionEx(self, spec: _typing.Optional[ConfigOptionQuerySpec]) -> _typing.Optional[pyVmomi.vim.vm.ConfigOption]: ...
   def QueryConfigTarget(self, host: _typing.Optional[HostSystem]) -> _typing.Optional[pyVmomi.vim.vm.ConfigTarget]: ...
   def QueryTargetCapabilities(self, host: _typing.Optional[HostSystem]) -> _typing.Optional[pyVmomi.vim.host.Capability]: ...


class ExtendedDescription(Description):
   messageCatalogKeyPrefix: str
   messageArg: list[pyVmomi.vmodl.KeyAnyValue] = []


class ExtendedElementDescription(ElementDescription):
   messageCatalogKeyPrefix: str
   messageArg: list[pyVmomi.vmodl.KeyAnyValue] = []


class ExtensibleManagedObject(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def value(self) -> list[CustomFieldsManager.Value]: ...
   @property
   def availableField(self) -> list[CustomFieldsManager.FieldDef]: ...

   def SetCustomValue(self, key: str, value: str) -> None: ...


class Extension(pyVmomi.vmodl.DynamicData):
   class ServerInfo(pyVmomi.vmodl.DynamicData):
      url: str
      description: Description
      company: str
      type: str
      adminEmail: list[str] = []
      serverThumbprint: _typing.Optional[str] = None
      serverCertificate: _typing.Optional[str] = None

   class ClientInfo(pyVmomi.vmodl.DynamicData):
      version: str
      description: Description
      company: str
      type: str
      url: str

   class TaskTypeInfo(pyVmomi.vmodl.DynamicData):
      taskID: str

   class EventTypeInfo(pyVmomi.vmodl.DynamicData):
      eventID: str
      eventTypeSchema: _typing.Optional[str] = None

   class FaultTypeInfo(pyVmomi.vmodl.DynamicData):
      faultID: str

   class PrivilegeInfo(pyVmomi.vmodl.DynamicData):
      privID: str
      privGroupName: str

   class ResourceInfo(pyVmomi.vmodl.DynamicData):
      locale: str
      module: str
      data: list[KeyValue] = []

   class HealthInfo(pyVmomi.vmodl.DynamicData):
      url: str

   class OvfConsumerInfo(pyVmomi.vmodl.DynamicData):
      callbackUrl: str
      sectionType: list[str] = []

   description: Description
   key: str
   company: _typing.Optional[str] = None
   type: _typing.Optional[str] = None
   version: str
   subjectName: _typing.Optional[str] = None
   server: list[ServerInfo] = []
   client: list[ClientInfo] = []
   taskList: list[TaskTypeInfo] = []
   eventList: list[EventTypeInfo] = []
   faultList: list[FaultTypeInfo] = []
   privilegeList: list[PrivilegeInfo] = []
   resourceList: list[ResourceInfo] = []
   lastHeartbeatTime: _datetime.datetime
   healthInfo: _typing.Optional[HealthInfo] = None
   ovfConsumerInfo: _typing.Optional[OvfConsumerInfo] = None
   extendedProductInfo: _typing.Optional[pyVmomi.vim.ext.ExtendedProductInfo] = None
   managedEntityInfo: list[pyVmomi.vim.ext.ManagedEntityInfo] = []
   shownInSolutionManager: _typing.Optional[bool] = None
   solutionManagerInfo: _typing.Optional[pyVmomi.vim.ext.SolutionManagerInfo] = None


class ExtensionManager(pyVmomi.VmomiSupport.ManagedObject):
   class IpAllocationUsage(pyVmomi.vmodl.DynamicData):
      extensionKey: str
      numAddresses: int

   @property
   def extensionList(self) -> list[Extension]: ...

   def UnregisterExtension(self, extensionKey: str) -> None: ...
   def FindExtension(self, extensionKey: str) -> _typing.Optional[Extension]: ...
   def RegisterExtension(self, extension: Extension) -> None: ...
   def UpdateExtension(self, extension: Extension) -> None: ...
   def GetPublicKey(self) -> str: ...
   def SetPublicKey(self, extensionKey: str, publicKey: str) -> None: ...
   def SetCertificate(self, extensionKey: str, certificatePem: _typing.Optional[str]) -> None: ...
   def SetServiceAccount(self, extensionKey: str, serviceAccount: str) -> None: ...
   def QueryManagedBy(self, extensionKey: str) -> list[ManagedEntity]: ...
   def QueryExtensionIpAllocationUsage(self, extensionKeys: list[str]) -> list[IpAllocationUsage]: ...


class FaultsByHost(pyVmomi.vmodl.DynamicData):
   host: HostSystem
   faults: list[pyVmomi.vmodl.MethodFault] = []


class FaultsByVM(pyVmomi.vmodl.DynamicData):
   vm: VirtualMachine
   faults: list[pyVmomi.vmodl.MethodFault] = []


class FeatureEVCMode(ElementDescription):
   mask: list[pyVmomi.vim.host.FeatureMask] = []
   capability: list[pyVmomi.vim.host.FeatureCapability] = []
   requirement: list[pyVmomi.vim.vm.FeatureRequirement] = []


class FileManager(pyVmomi.VmomiSupport.ManagedObject):
   class FileLockInfo(pyVmomi.vmodl.DynamicData):
      filePath: str
      host: str
      mac: str
      id: str
      worldName: str
      ownerId: _typing.Optional[str] = None
      lockMode: str
      acquired: _typing.Optional[_datetime.datetime] = None
      heartbeat: _typing.Optional[_datetime.datetime] = None
      refCount: _typing.Optional[int] = None

   class FileLockInfoResult(pyVmomi.vmodl.DynamicData):
      lockInfo: list[FileLockInfo] = []
      fault: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

   def MoveFile(self, sourceName: str, sourceDatacenter: _typing.Optional[Datacenter], destinationName: str, destinationDatacenter: _typing.Optional[Datacenter], force: _typing.Optional[bool]) -> Task: ...
   def CopyFile(self, sourceName: str, sourceDatacenter: _typing.Optional[Datacenter], destinationName: str, destinationDatacenter: _typing.Optional[Datacenter], force: _typing.Optional[bool]) -> Task: ...
   def DeleteFile(self, name: str, datacenter: _typing.Optional[Datacenter]) -> Task: ...
   def MakeDirectory(self, name: str, datacenter: _typing.Optional[Datacenter], createParentDirectories: _typing.Optional[bool]) -> None: ...
   def ChangeOwner(self, name: str, datacenter: _typing.Optional[Datacenter], owner: str) -> None: ...
   def QueryFileLockInfo(self, path: str, host: _typing.Optional[HostSystem]) -> FileLockInfoResult: ...


class Folder(ManagedEntity):
   class DesiredHostState(pyVmomi.VmomiSupport.Enum):
      maintenance: _typing.ClassVar['DesiredHostState'] = 'maintenance'
      non_maintenance: _typing.ClassVar['DesiredHostState'] = 'non_maintenance'

   class NewHostSpec(pyVmomi.vmodl.DynamicData):
      hostCnxSpec: pyVmomi.vim.host.ConnectSpec
      esxLicense: _typing.Optional[str] = None

   class FailedHostResult(pyVmomi.vmodl.DynamicData):
      hostName: _typing.Optional[str] = None
      host: _typing.Optional[HostSystem] = None
      context: pyVmomi.vmodl.LocalizableMessage
      fault: pyVmomi.vmodl.MethodFault

   class BatchAddStandaloneHostsResult(pyVmomi.vmodl.DynamicData):
      addedHosts: list[HostSystem] = []
      hostsFailedInventoryAdd: list[FailedHostResult] = []

   class BatchAddHostsToClusterResult(pyVmomi.vmodl.DynamicData):
      hostsAddedToCluster: list[HostSystem] = []
      hostsFailedInventoryAdd: list[FailedHostResult] = []
      hostsFailedMoveToCluster: list[FailedHostResult] = []

   class ExternallyManagedFolderType(pyVmomi.VmomiSupport.Enum):
      PROJECT_ROOT: _typing.ClassVar['ExternallyManagedFolderType'] = 'PROJECT_ROOT'
      PROJECT: _typing.ClassVar['ExternallyManagedFolderType'] = 'PROJECT'
      VPC_ROOT: _typing.ClassVar['ExternallyManagedFolderType'] = 'VPC_ROOT'
      VPC: _typing.ClassVar['ExternallyManagedFolderType'] = 'VPC'
      SUBNET: _typing.ClassVar['ExternallyManagedFolderType'] = 'SUBNET'
      SEGMENT: _typing.ClassVar['ExternallyManagedFolderType'] = 'SEGMENT'
      SUPERVISOR: _typing.ClassVar['ExternallyManagedFolderType'] = 'SUPERVISOR'
      VSPHERE_POD: _typing.ClassVar['ExternallyManagedFolderType'] = 'VSPHERE_POD'

   class ExternallyManagedFolderInfo(pyVmomi.vmodl.DynamicData):
      id: str
      type: str

   @property
   def childType(self) -> list[type]: ...
   @property
   def childEntity(self) -> list[ManagedEntity]: ...
   @property
   def namespace(self) -> _typing.Optional[str]: ...
   @property
   def externallyManagedFolderInfo(self) -> _typing.Optional[ExternallyManagedFolderInfo]: ...

   def CreateFolder(self, name: str) -> Folder: ...
   def MoveInto(self, list: list[ManagedEntity]) -> Task: ...
   def CreateVm(self, config: pyVmomi.vim.vm.ConfigSpec, pool: ResourcePool, host: _typing.Optional[HostSystem]) -> Task: ...
   def RegisterVm(self, path: str, name: _typing.Optional[str], asTemplate: bool, pool: _typing.Optional[ResourcePool], host: _typing.Optional[HostSystem]) -> Task: ...
   def CreateCluster(self, name: str, spec: pyVmomi.vim.cluster.ConfigSpec) -> ClusterComputeResource: ...
   def CreateClusterEx(self, name: str, spec: pyVmomi.vim.cluster.ConfigSpecEx) -> ClusterComputeResource: ...
   def AddStandaloneHost(self, spec: pyVmomi.vim.host.ConnectSpec, compResSpec: _typing.Optional[ComputeResource.ConfigSpec], addConnected: bool, license: _typing.Optional[str]) -> Task: ...
   def CreateDatacenter(self, name: str) -> Datacenter: ...
   def UnregisterAndDestroy(self) -> Task: ...
   def CreateDistributedVirtualSwitch(self, spec: DistributedVirtualSwitch.CreateSpec) -> Task: ...
   def CreateStoragePod(self, name: str) -> StoragePod: ...
   def BatchAddStandaloneHosts(self, newHosts: list[NewHostSpec], compResSpec: _typing.Optional[ComputeResource.ConfigSpec], addConnected: bool) -> Task: ...
   def BatchAddHostsToCluster(self, cluster: ClusterComputeResource, newHosts: list[NewHostSpec], existingHosts: list[HostSystem], compResSpec: _typing.Optional[ComputeResource.ConfigSpec], desiredState: _typing.Optional[str]) -> Task: ...


class HbrReplicationTargetSpec(pyVmomi.vmodl.DynamicData):
   pass


class HbrTargetSpec(pyVmomi.vmodl.DynamicData):
   targetIP: str
   certificate: str


class HbrTargetSpecReplacement(HbrReplicationTargetSpec):
   spec: list[HbrTargetSpec] = []


class HealthUpdate(pyVmomi.vmodl.DynamicData):
   entity: ManagedEntity
   healthUpdateInfoId: str
   id: str
   status: ManagedEntity.Status
   remediation: str


class HealthUpdateInfo(pyVmomi.vmodl.DynamicData):
   class ComponentType(pyVmomi.VmomiSupport.Enum):
      Memory: _typing.ClassVar['ComponentType'] = 'Memory'
      Power: _typing.ClassVar['ComponentType'] = 'Power'
      Fan: _typing.ClassVar['ComponentType'] = 'Fan'
      Network: _typing.ClassVar['ComponentType'] = 'Network'
      Storage: _typing.ClassVar['ComponentType'] = 'Storage'

   id: str
   componentType: str
   description: str


class HealthUpdateManager(pyVmomi.VmomiSupport.ManagedObject):
   def RegisterProvider(self, name: str, healthUpdateInfo: list[HealthUpdateInfo]) -> str: ...
   def UnregisterProvider(self, providerId: str) -> None: ...
   def QueryProviderList(self) -> list[str]: ...
   def HasProvider(self, id: str) -> bool: ...
   def QueryProviderName(self, id: str) -> str: ...
   def QueryHealthUpdateInfos(self, providerId: str) -> list[HealthUpdateInfo]: ...
   def AddMonitoredEntities(self, providerId: str, entities: list[ManagedEntity]) -> None: ...
   def RemoveMonitoredEntities(self, providerId: str, entities: list[ManagedEntity]) -> None: ...
   def QueryMonitoredEntities(self, providerId: str) -> list[ManagedEntity]: ...
   def HasMonitoredEntity(self, providerId: str, entity: ManagedEntity) -> bool: ...
   def QueryUnmonitoredHosts(self, providerId: str, cluster: ClusterComputeResource) -> list[HostSystem]: ...
   def PostHealthUpdates(self, providerId: str, updates: list[HealthUpdate]) -> None: ...
   def QueryHealthUpdates(self, providerId: str) -> list[HealthUpdate]: ...
   def AddFilter(self, providerId: str, filterName: str, infoIds: list[str]) -> str: ...
   def QueryFilterList(self, providerId: str) -> list[str]: ...
   def QueryFilterName(self, filterId: str) -> str: ...
   def QueryFilterInfoIds(self, filterId: str) -> list[str]: ...
   def QueryFilterEntities(self, filterId: str) -> list[ManagedEntity]: ...
   def AddFilterEntities(self, filterId: str, entities: list[ManagedEntity]) -> None: ...
   def RemoveFilterEntities(self, filterId: str, entities: list[ManagedEntity]) -> None: ...
   def RemoveFilter(self, filterId: str) -> None: ...


class HistoricalInterval(pyVmomi.vmodl.DynamicData):
   key: int
   samplingPeriod: int
   name: str
   length: int
   level: _typing.Optional[int] = None
   enabled: bool


class HistoryCollector(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def filter(self) -> object: ...

   def SetLatestPageSize(self, maxCount: int) -> None: ...
   def Rewind(self) -> None: ...
   def Reset(self) -> None: ...
   def Remove(self) -> None: ...


class HostServiceTicket(pyVmomi.vmodl.DynamicData):
   host: _typing.Optional[str] = None
   port: _typing.Optional[int] = None
   sslThumbprint: _typing.Optional[str] = None
   sslCertificate: _typing.Optional[str] = None
   service: str
   serviceVersion: str
   sessionId: str


class HostSystem(ManagedEntity):
   class ConnectionState(pyVmomi.VmomiSupport.Enum):
      connected: _typing.ClassVar['ConnectionState'] = 'connected'
      notResponding: _typing.ClassVar['ConnectionState'] = 'notResponding'
      disconnected: _typing.ClassVar['ConnectionState'] = 'disconnected'

   class PowerState(pyVmomi.VmomiSupport.Enum):
      poweredOn: _typing.ClassVar['PowerState'] = 'poweredOn'
      poweredOff: _typing.ClassVar['PowerState'] = 'poweredOff'
      standBy: _typing.ClassVar['PowerState'] = 'standBy'
      unknown: _typing.ClassVar['PowerState'] = 'unknown'

   class StandbyMode(pyVmomi.VmomiSupport.Enum):
      entering: _typing.ClassVar['StandbyMode'] = 'entering'
      exiting: _typing.ClassVar['StandbyMode'] = 'exiting'
      # Reserved python keyword: commenting out.
      # in: _typing.ClassVar['StandbyMode'] = 'in'
      none: _typing.ClassVar['StandbyMode'] = 'none'

   class CryptoState(pyVmomi.VmomiSupport.Enum):
      incapable: _typing.ClassVar['CryptoState'] = 'incapable'
      prepared: _typing.ClassVar['CryptoState'] = 'prepared'
      safe: _typing.ClassVar['CryptoState'] = 'safe'
      pendingIncapable: _typing.ClassVar['CryptoState'] = 'pendingIncapable'

   class RemediationState(pyVmomi.vmodl.DynamicData):
      class State(pyVmomi.VmomiSupport.Enum):
         remediationReady: _typing.ClassVar['State'] = 'remediationReady'
         precheckRemediationRunning: _typing.ClassVar['State'] = 'precheckRemediationRunning'
         precheckRemediationComplete: _typing.ClassVar['State'] = 'precheckRemediationComplete'
         precheckRemediationFailed: _typing.ClassVar['State'] = 'precheckRemediationFailed'
         remediationRunning: _typing.ClassVar['State'] = 'remediationRunning'
         remediationFailed: _typing.ClassVar['State'] = 'remediationFailed'

      state: str
      operationTime: _datetime.datetime

   class ComplianceCheckState(pyVmomi.vmodl.DynamicData):
      state: str
      checkTime: _datetime.datetime

   class ReconnectSpec(pyVmomi.vmodl.DynamicData):
      syncState: _typing.Optional[bool] = None

   @property
   def runtime(self) -> pyVmomi.vim.host.RuntimeInfo: ...
   @property
   def summary(self) -> pyVmomi.vim.host.Summary: ...
   @property
   def hardware(self) -> _typing.Optional[pyVmomi.vim.host.HardwareInfo]: ...
   @property
   def capability(self) -> _typing.Optional[pyVmomi.vim.host.Capability]: ...
   @property
   def licensableResource(self) -> LicenseManager.LicensableResourceInfo: ...
   @property
   def remediationState(self) -> _typing.Optional[RemediationState]: ...
   @property
   def precheckRemediationResult(self) -> _typing.Optional[pyVmomi.vim.profile.host.ProfileManager.ApplyHostConfigSpec]: ...
   @property
   def remediationResult(self) -> _typing.Optional[pyVmomi.vim.profile.host.ProfileManager.ApplyHostConfigResult]: ...
   @property
   def complianceCheckState(self) -> _typing.Optional[ComplianceCheckState]: ...
   @property
   def complianceCheckResult(self) -> _typing.Optional[pyVmomi.vim.profile.ComplianceResult]: ...
   @property
   def configManager(self) -> pyVmomi.vim.host.ConfigManager: ...
   @property
   def config(self) -> _typing.Optional[pyVmomi.vim.host.ConfigInfo]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def datastoreBrowser(self) -> pyVmomi.vim.host.DatastoreBrowser: ...
   @property
   def systemResources(self) -> _typing.Optional[pyVmomi.vim.host.SystemResourceInfo]: ...
   @property
   def answerFileValidationState(self) -> _typing.Optional[pyVmomi.vim.profile.host.AnswerFileStatusResult]: ...
   @property
   def answerFileValidationResult(self) -> _typing.Optional[pyVmomi.vim.profile.host.AnswerFileStatusResult]: ...

   def QueryTpmAttestationReport(self) -> _typing.Optional[pyVmomi.vim.host.TpmAttestationReport]: ...
   def QueryConnectionInfo(self) -> pyVmomi.vim.host.ConnectInfo: ...
   def UpdateSystemResources(self, resourceInfo: pyVmomi.vim.host.SystemResourceInfo) -> None: ...
   def UpdateSystemSwapConfiguration(self, sysSwapConfig: pyVmomi.vim.host.SystemSwapConfiguration) -> None: ...
   def Reconnect(self, cnxSpec: _typing.Optional[pyVmomi.vim.host.ConnectSpec], reconnectSpec: _typing.Optional[ReconnectSpec]) -> Task: ...
   def Disconnect(self) -> Task: ...
   def EnterMaintenanceMode(self, timeout: int, evacuatePoweredOffVms: _typing.Optional[bool], maintenanceSpec: _typing.Optional[pyVmomi.vim.host.MaintenanceSpec]) -> Task: ...
   def ExitMaintenanceMode(self, timeout: int) -> Task: ...
   def Reboot(self, force: bool) -> Task: ...
   def Shutdown(self, force: bool) -> Task: ...
   def EnterStandbyMode(self, timeoutSec: int, evacuatePoweredOffVms: _typing.Optional[bool]) -> Task: ...
   def ExitStandbyMode(self, timeoutSec: int) -> Task: ...
   def QueryOverhead(self, memorySize: pyVmomi.VmomiSupport.long, videoRamSize: _typing.Optional[int], numVcpus: int) -> pyVmomi.VmomiSupport.long: ...
   def QueryOverheadEx(self, vmConfigInfo: pyVmomi.vim.vm.ConfigInfo) -> pyVmomi.VmomiSupport.long: ...
   def ReconfigureDAS(self) -> Task: ...
   def UpdateFlags(self, flagInfo: pyVmomi.vim.host.FlagInfo) -> None: ...
   def EnterLockdownMode(self) -> None: ...
   def ExitLockdownMode(self) -> None: ...
   def AcquireCimServicesTicket(self) -> HostServiceTicket: ...
   def UpdateIpmi(self, ipmiInfo: pyVmomi.vim.host.IpmiInfo) -> None: ...
   def RetrieveHardwareUptime(self) -> pyVmomi.VmomiSupport.long: ...
   def PrepareCrypto(self) -> None: ...
   def EnableCrypto(self, keyPlain: pyVmomi.vim.encryption.CryptoKeyPlain) -> None: ...
   def ConfigureCryptoKey(self, keyId: _typing.Optional[pyVmomi.vim.encryption.CryptoKeyId]) -> None: ...
   def QueryProductLockerLocation(self) -> str: ...
   def UpdateProductLockerLocation(self, path: str) -> Task: ...
   def RetrieveFreeEpcMemory(self) -> pyVmomi.VmomiSupport.long: ...


class HttpNfcLease(pyVmomi.VmomiSupport.ManagedObject):
   class State(pyVmomi.VmomiSupport.Enum):
      initializing: _typing.ClassVar['State'] = 'initializing'
      ready: _typing.ClassVar['State'] = 'ready'
      done: _typing.ClassVar['State'] = 'done'
      error: _typing.ClassVar['State'] = 'error'

   class Mode(pyVmomi.VmomiSupport.Enum):
      pushOrGet: _typing.ClassVar['Mode'] = 'pushOrGet'
      pull: _typing.ClassVar['Mode'] = 'pull'

   class DatastoreLeaseInfo(pyVmomi.vmodl.DynamicData):
      datastoreKey: str
      hosts: list[HostInfo] = []

   class HostInfo(pyVmomi.vmodl.DynamicData):
      url: str
      sslThumbprint: str

   class Info(pyVmomi.vmodl.DynamicData):
      lease: HttpNfcLease
      entity: ManagedEntity
      deviceUrl: list[DeviceUrl] = []
      totalDiskCapacityInKB: pyVmomi.VmomiSupport.long
      leaseTimeout: int
      hostMap: list[DatastoreLeaseInfo] = []

   class DeviceUrl(pyVmomi.vmodl.DynamicData):
      key: str
      importKey: str
      url: str
      sslThumbprint: str
      sslCertificate: _typing.Optional[str] = None
      disk: _typing.Optional[bool] = None
      targetId: _typing.Optional[str] = None
      datastoreKey: _typing.Optional[str] = None
      fileSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class ManifestEntry(pyVmomi.vmodl.DynamicData):
      class ChecksumType(pyVmomi.VmomiSupport.Enum):
         sha1: _typing.ClassVar['ChecksumType'] = 'sha1'
         sha256: _typing.ClassVar['ChecksumType'] = 'sha256'

      key: str
      sha1: str
      checksum: _typing.Optional[str] = None
      checksumType: _typing.Optional[str] = None
      size: pyVmomi.VmomiSupport.long
      disk: bool
      capacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      populatedSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class SourceFile(pyVmomi.vmodl.DynamicData):
      targetDeviceId: str
      url: str
      memberName: _typing.Optional[str] = None
      create: bool
      sslThumbprint: _typing.Optional[str] = None
      sslCertificate: _typing.Optional[str] = None
      httpHeaders: list[KeyValue] = []
      size: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class Capabilities(pyVmomi.vmodl.DynamicData):
      pullModeSupported: bool
      corsSupported: bool

   class ProbeResult(pyVmomi.vmodl.DynamicData):
      serverAccessible: bool

   @property
   def initializeProgress(self) -> int: ...
   @property
   def transferProgress(self) -> int: ...
   @property
   def mode(self) -> str: ...
   @property
   def capabilities(self) -> Capabilities: ...
   @property
   def info(self) -> _typing.Optional[Info]: ...
   @property
   def state(self) -> State: ...
   @property
   def error(self) -> _typing.Optional[pyVmomi.vmodl.MethodFault]: ...

   def GetManifest(self) -> list[ManifestEntry]: ...
   def SetManifestChecksumType(self, deviceUrlsToChecksumTypes: list[KeyValue]) -> None: ...
   def Complete(self) -> None: ...
   def Abort(self, fault: _typing.Optional[pyVmomi.vmodl.MethodFault]) -> None: ...
   def Progress(self, percent: int) -> None: ...
   def PullFromUrls(self, files: list[SourceFile]) -> Task: ...
   def ProbeUrls(self, files: list[SourceFile], timeout: _typing.Optional[int]) -> list[ProbeResult]: ...


class ImportSpec(pyVmomi.vmodl.DynamicData):
   entityConfig: _typing.Optional[pyVmomi.vim.vApp.EntityConfigInfo] = None
   instantiationOst: _typing.Optional[OvfConsumer.OstNode] = None


class InheritablePolicy(pyVmomi.vmodl.DynamicData):
   inherited: bool


class IntExpression(NegatableExpression):
   value: _typing.Optional[int] = None


class IntPolicy(InheritablePolicy):
   value: _typing.Optional[int] = None


class IoFilterManager(pyVmomi.VmomiSupport.ManagedObject):
   class IoFilterInfo(pyVmomi.vmodl.DynamicData):
      id: str
      name: str
      vendor: str
      version: str
      type: _typing.Optional[str] = None
      summary: _typing.Optional[str] = None
      releaseDate: _typing.Optional[str] = None

   class HostIoFilterInfo(IoFilterInfo):
      available: bool

   class OperationType(pyVmomi.VmomiSupport.Enum):
      install: _typing.ClassVar['OperationType'] = 'install'
      uninstall: _typing.ClassVar['OperationType'] = 'uninstall'
      upgrade: _typing.ClassVar['OperationType'] = 'upgrade'

   class ClusterIoFilterInfo(IoFilterInfo):
      opType: str
      vibUrl: _typing.Optional[str] = None

   class IoFilterType(pyVmomi.VmomiSupport.Enum):
      cache: _typing.ClassVar['IoFilterType'] = 'cache'
      replication: _typing.ClassVar['IoFilterType'] = 'replication'
      encryption: _typing.ClassVar['IoFilterType'] = 'encryption'
      compression: _typing.ClassVar['IoFilterType'] = 'compression'
      inspection: _typing.ClassVar['IoFilterType'] = 'inspection'
      datastoreIoControl: _typing.ClassVar['IoFilterType'] = 'datastoreIoControl'
      dataProvider: _typing.ClassVar['IoFilterType'] = 'dataProvider'
      dataCapture: _typing.ClassVar['IoFilterType'] = 'dataCapture'

   class SslTrust(pyVmomi.vmodl.DynamicData):
      pass

   class PinnedCertificate(SslTrust):
      sslCertificate: str

   class UntrustedCertificate(SslTrust):
      pass

   class QueryIssueResult(pyVmomi.vmodl.DynamicData):
      class HostIssue(pyVmomi.vmodl.DynamicData):
         host: HostSystem
         issue: list[pyVmomi.vmodl.MethodFault] = []

      opType: str
      hostIssue: list[HostIssue] = []

   def InstallIoFilter(self, vibUrl: str, compRes: ComputeResource, vibSslTrust: _typing.Optional[SslTrust]) -> Task: ...
   def UninstallIoFilter(self, filterId: str, compRes: ComputeResource) -> Task: ...
   def UpgradeIoFilter(self, filterId: str, compRes: ComputeResource, vibUrl: str, vibSslTrust: _typing.Optional[SslTrust]) -> Task: ...
   def QueryIssue(self, filterId: str, compRes: ComputeResource) -> QueryIssueResult: ...
   def QueryIoFilterInfo(self, compRes: ComputeResource) -> list[ClusterIoFilterInfo]: ...
   def ResolveInstallationErrorsOnHost(self, filterId: str, host: HostSystem) -> Task: ...
   def ResolveInstallationErrorsOnCluster(self, filterId: str, cluster: ClusterComputeResource) -> Task: ...
   def QueryDisksUsingFilter(self, filterId: str, compRes: ComputeResource) -> list[pyVmomi.vim.vm.device.VirtualDiskId]: ...
   def InitiateTransitionToVLCM(self, cluster: ClusterComputeResource) -> Task: ...

class IpAddress(NegatableExpression):
   pass


class IpPoolManager(pyVmomi.VmomiSupport.ManagedObject):
   class IpAllocation(pyVmomi.vmodl.DynamicData):
      ipAddress: str
      allocationId: str

   def QueryIpPools(self, dc: Datacenter) -> list[pyVmomi.vim.vApp.IpPool]: ...
   def CreateIpPool(self, dc: Datacenter, pool: pyVmomi.vim.vApp.IpPool) -> int: ...
   def UpdateIpPool(self, dc: Datacenter, pool: pyVmomi.vim.vApp.IpPool) -> None: ...
   def DestroyIpPool(self, dc: Datacenter, id: int, force: bool) -> None: ...
   def AllocateIpv4Address(self, dc: Datacenter, poolId: int, allocationId: str) -> str: ...
   def AllocateIpv6Address(self, dc: Datacenter, poolId: int, allocationId: str) -> str: ...
   def ReleaseIpAllocation(self, dc: Datacenter, poolId: int, allocationId: str) -> None: ...
   def QueryIPAllocations(self, dc: Datacenter, poolId: int, extensionKey: str) -> list[IpAllocation]: ...


class IpRange(IpAddress):
   addressPrefix: str
   prefixLength: _typing.Optional[int] = None


class KeyValue(pyVmomi.vmodl.DynamicData):
   key: str
   value: str


class LatencySensitivity(pyVmomi.vmodl.DynamicData):
   class SensitivityLevel(pyVmomi.VmomiSupport.Enum):
      low: _typing.ClassVar['SensitivityLevel'] = 'low'
      normal: _typing.ClassVar['SensitivityLevel'] = 'normal'
      medium: _typing.ClassVar['SensitivityLevel'] = 'medium'
      high: _typing.ClassVar['SensitivityLevel'] = 'high'
      custom: _typing.ClassVar['SensitivityLevel'] = 'custom'

   level: SensitivityLevel
   sensitivity: _typing.Optional[int] = None


class LicenseAssignmentManager(pyVmomi.VmomiSupport.ManagedObject):
   class LicenseAssignment(pyVmomi.vmodl.DynamicData):
      entityId: str
      scope: _typing.Optional[str] = None
      entityDisplayName: _typing.Optional[str] = None
      assignedLicense: LicenseManager.LicenseInfo
      properties: list[pyVmomi.vmodl.KeyAnyValue] = []

   def UpdateAssignedLicense(self, entity: str, licenseKey: str, entityDisplayName: _typing.Optional[str]) -> LicenseManager.LicenseInfo: ...
   def RemoveAssignedLicense(self, entityId: str) -> None: ...
   def QueryAssignedLicenses(self, entityId: _typing.Optional[str]) -> list[LicenseAssignment]: ...


class LicenseManager(pyVmomi.VmomiSupport.ManagedObject):
   class LicenseState(pyVmomi.VmomiSupport.Enum):
      initializing: _typing.ClassVar['LicenseState'] = 'initializing'
      normal: _typing.ClassVar['LicenseState'] = 'normal'
      marginal: _typing.ClassVar['LicenseState'] = 'marginal'
      fault: _typing.ClassVar['LicenseState'] = 'fault'

   class LicenseKey(pyVmomi.VmomiSupport.Enum):
      esxFull: _typing.ClassVar['LicenseKey'] = 'esxFull'
      esxVmtn: _typing.ClassVar['LicenseKey'] = 'esxVmtn'
      esxExpress: _typing.ClassVar['LicenseKey'] = 'esxExpress'
      san: _typing.ClassVar['LicenseKey'] = 'san'
      iscsi: _typing.ClassVar['LicenseKey'] = 'iscsi'
      nas: _typing.ClassVar['LicenseKey'] = 'nas'
      vsmp: _typing.ClassVar['LicenseKey'] = 'vsmp'
      backup: _typing.ClassVar['LicenseKey'] = 'backup'
      vc: _typing.ClassVar['LicenseKey'] = 'vc'
      vcExpress: _typing.ClassVar['LicenseKey'] = 'vcExpress'
      esxHost: _typing.ClassVar['LicenseKey'] = 'esxHost'
      gsxHost: _typing.ClassVar['LicenseKey'] = 'gsxHost'
      serverHost: _typing.ClassVar['LicenseKey'] = 'serverHost'
      drsPower: _typing.ClassVar['LicenseKey'] = 'drsPower'
      vmotion: _typing.ClassVar['LicenseKey'] = 'vmotion'
      drs: _typing.ClassVar['LicenseKey'] = 'drs'
      das: _typing.ClassVar['LicenseKey'] = 'das'

   class LicenseSource(pyVmomi.vmodl.DynamicData):
      pass

   class LicenseServer(LicenseSource):
      licenseServer: str

   class LocalLicense(LicenseSource):
      licenseKeys: str

   class EvaluationLicense(LicenseSource):
      remainingHours: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class FeatureInfo(pyVmomi.vmodl.DynamicData):
      class CostUnit(pyVmomi.VmomiSupport.Enum):
         host: _typing.ClassVar['CostUnit'] = 'host'
         cpuCore: _typing.ClassVar['CostUnit'] = 'cpuCore'
         cpuPackage: _typing.ClassVar['CostUnit'] = 'cpuPackage'
         server: _typing.ClassVar['CostUnit'] = 'server'
         vm: _typing.ClassVar['CostUnit'] = 'vm'

      class State(pyVmomi.VmomiSupport.Enum):
         enabled: _typing.ClassVar['State'] = 'enabled'
         disabled: _typing.ClassVar['State'] = 'disabled'
         optional: _typing.ClassVar['State'] = 'optional'

      class SourceRestriction(pyVmomi.VmomiSupport.Enum):
         unrestricted: _typing.ClassVar['SourceRestriction'] = 'unrestricted'
         served: _typing.ClassVar['SourceRestriction'] = 'served'
         file: _typing.ClassVar['SourceRestriction'] = 'file'

      key: str
      featureName: str
      featureDescription: _typing.Optional[str] = None
      state: _typing.Optional[State] = None
      costUnit: str
      sourceRestriction: _typing.Optional[str] = None
      dependentKey: list[str] = []
      edition: _typing.Optional[bool] = None
      expiresOn: _typing.Optional[_datetime.datetime] = None

   class ReservationInfo(pyVmomi.vmodl.DynamicData):
      class State(pyVmomi.VmomiSupport.Enum):
         notUsed: _typing.ClassVar['State'] = 'notUsed'
         noLicense: _typing.ClassVar['State'] = 'noLicense'
         unlicensedUse: _typing.ClassVar['State'] = 'unlicensedUse'
         licensed: _typing.ClassVar['State'] = 'licensed'

      key: str
      state: State
      required: int

   class AvailabilityInfo(pyVmomi.vmodl.DynamicData):
      feature: FeatureInfo
      total: int
      available: int

   class DiagnosticInfo(pyVmomi.vmodl.DynamicData):
      sourceLastChanged: _datetime.datetime
      sourceLost: str
      sourceLatency: float
      licenseRequests: str
      licenseRequestFailures: str
      licenseFeatureUnknowns: str
      opState: LicenseState
      lastStatusUpdate: _datetime.datetime
      opFailureMessage: str

   class LicenseUsageInfo(pyVmomi.vmodl.DynamicData):
      source: LicenseSource
      sourceAvailable: bool
      reservationInfo: list[ReservationInfo] = []
      featureInfo: list[FeatureInfo] = []

   class EvaluationInfo(pyVmomi.vmodl.DynamicData):
      properties: list[pyVmomi.vmodl.KeyAnyValue] = []

   class LicensableResourceInfo(pyVmomi.vmodl.DynamicData):
      class ResourceKey(pyVmomi.VmomiSupport.Enum):
         numCpuPackages: _typing.ClassVar['ResourceKey'] = 'numCpuPackages'
         numCpuCores: _typing.ClassVar['ResourceKey'] = 'numCpuCores'
         memorySize: _typing.ClassVar['ResourceKey'] = 'memorySize'
         memoryForVms: _typing.ClassVar['ResourceKey'] = 'memoryForVms'
         numVmsStarted: _typing.ClassVar['ResourceKey'] = 'numVmsStarted'
         numVmsStarting: _typing.ClassVar['ResourceKey'] = 'numVmsStarting'
         vsanCapacity: _typing.ClassVar['ResourceKey'] = 'vsanCapacity'

      resource: list[pyVmomi.vmodl.KeyAnyValue] = []

   class LicenseInfo(pyVmomi.vmodl.DynamicData):
      licenseKey: str
      editionKey: str
      name: str
      total: int
      used: _typing.Optional[int] = None
      costUnit: str
      properties: list[pyVmomi.vmodl.KeyAnyValue] = []
      labels: list[KeyValue] = []

   @property
   def source(self) -> LicenseSource: ...
   @property
   def sourceAvailable(self) -> bool: ...
   @property
   def diagnostics(self) -> _typing.Optional[DiagnosticInfo]: ...
   @property
   def featureInfo(self) -> list[FeatureInfo]: ...
   @property
   def licensedEdition(self) -> str: ...
   @property
   def licenses(self) -> list[LicenseInfo]: ...
   @property
   def licenseAssignmentManager(self) -> _typing.Optional[LicenseAssignmentManager]: ...
   @property
   def evaluation(self) -> EvaluationInfo: ...

   def QuerySupportedFeatures(self, host: _typing.Optional[HostSystem]) -> list[FeatureInfo]: ...
   def QuerySourceAvailability(self, host: _typing.Optional[HostSystem]) -> list[AvailabilityInfo]: ...
   def QueryUsage(self, host: _typing.Optional[HostSystem]) -> LicenseUsageInfo: ...
   def SetEdition(self, host: _typing.Optional[HostSystem], featureKey: _typing.Optional[str]) -> None: ...
   def CheckFeature(self, host: _typing.Optional[HostSystem], featureKey: str) -> bool: ...
   def Enable(self, host: _typing.Optional[HostSystem], featureKey: str) -> bool: ...
   def Disable(self, host: _typing.Optional[HostSystem], featureKey: str) -> bool: ...
   def ConfigureSource(self, host: _typing.Optional[HostSystem], licenseSource: LicenseSource) -> None: ...
   def UpdateLicense(self, licenseKey: str, labels: list[KeyValue]) -> LicenseInfo: ...
   def AddLicense(self, licenseKey: str, labels: list[KeyValue]) -> LicenseInfo: ...
   def RemoveLicense(self, licenseKey: str) -> None: ...
   def DecodeLicense(self, licenseKey: str) -> LicenseInfo: ...
   def UpdateLabel(self, licenseKey: str, labelKey: str, labelValue: str) -> None: ...
   def RemoveLabel(self, licenseKey: str, labelKey: str) -> None: ...


class LocalizationManager(pyVmomi.VmomiSupport.ManagedObject):
   class MessageCatalog(pyVmomi.vmodl.DynamicData):
      moduleName: str
      catalogName: str
      locale: str
      catalogUri: str
      lastModified: _typing.Optional[_datetime.datetime] = None
      md5sum: _typing.Optional[str] = None
      version: _typing.Optional[str] = None

   @property
   def catalog(self) -> list[MessageCatalog]: ...


class LongPolicy(InheritablePolicy):
   value: _typing.Optional[pyVmomi.VmomiSupport.long] = None

class MacAddress(NegatableExpression):
   pass

class MacRange(MacAddress):
   address: str
   mask: str


class ManagedEntity(ExtensibleManagedObject):
   class Status(pyVmomi.VmomiSupport.Enum):
      gray: _typing.ClassVar['Status'] = 'gray'
      green: _typing.ClassVar['Status'] = 'green'
      yellow: _typing.ClassVar['Status'] = 'yellow'
      red: _typing.ClassVar['Status'] = 'red'

   @property
   def parent(self) -> _typing.Optional[ManagedEntity]: ...
   @property
   def customValue(self) -> list[CustomFieldsManager.Value]: ...
   @property
   def overallStatus(self) -> Status: ...
   @property
   def configStatus(self) -> Status: ...
   @property
   def configIssue(self) -> list[pyVmomi.vim.event.Event]: ...
   @property
   def effectiveRole(self) -> list[int]: ...
   @property
   def permission(self) -> list[AuthorizationManager.Permission]: ...
   @property
   def name(self) -> str: ...
   @property
   def disabledMethod(self) -> list[pyVmomi.VmomiSupport.ManagedMethod]: ...
   @property
   def recentTask(self) -> list[Task]: ...
   @property
   def declaredAlarmState(self) -> list[pyVmomi.vim.alarm.AlarmState]: ...
   @property
   def triggeredAlarmState(self) -> list[pyVmomi.vim.alarm.AlarmState]: ...
   @property
   def alarmActionsEnabled(self) -> _typing.Optional[bool]: ...
   @property
   def tag(self) -> list[Tag]: ...

   def Reload(self) -> None: ...
   def Rename(self, newName: str) -> Task: ...
   def Destroy(self) -> Task: ...


class MethodDescription(Description):
   key: pyVmomi.VmomiSupport.ManagedMethod


class NegatableExpression(pyVmomi.vmodl.DynamicData):
   negate: _typing.Optional[bool] = None


class Network(ManagedEntity):
   class Summary(pyVmomi.vmodl.DynamicData):
      network: _typing.Optional[Network] = None
      name: str
      accessible: bool
      ipPoolName: str
      ipPoolId: _typing.Optional[int] = None

   @property
   def summary(self) -> Summary: ...
   @property
   def host(self) -> list[HostSystem]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...

   def DestroyNetwork(self) -> None: ...


class NumericRange(pyVmomi.vmodl.DynamicData):
   start: int
   end: int


class OpaqueNetwork(Network):
   class Summary(Network.Summary):
      opaqueNetworkId: str
      opaqueNetworkType: str

   class Capability(pyVmomi.vmodl.DynamicData):
      networkReservationSupported: bool

   @property
   def capability(self) -> _typing.Optional[Capability]: ...
   @property
   def extraConfig(self) -> list[pyVmomi.vim.option.OptionValue]: ...


class OverheadMemoryManager(pyVmomi.VmomiSupport.ManagedObject):
   def LookupVmOverheadMemory(self, vm: VirtualMachine, host: HostSystem) -> pyVmomi.VmomiSupport.long: ...


class OvfManager(pyVmomi.VmomiSupport.ManagedObject):
   class OvfOptionInfo(pyVmomi.vmodl.DynamicData):
      option: str
      description: pyVmomi.vmodl.LocalizableMessage

   class DeploymentOption(pyVmomi.vmodl.DynamicData):
      key: str
      label: str
      description: str

   class CommonParams(pyVmomi.vmodl.DynamicData):
      locale: str
      deploymentOption: str
      msgBundle: list[KeyValue] = []
      importOption: list[str] = []

   class ValidateHostParams(CommonParams):
      pass

   class ValidateHostResult(pyVmomi.vmodl.DynamicData):
      downloadSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      flatDeploymentSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      sparseDeploymentSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      error: list[pyVmomi.vmodl.MethodFault] = []
      warning: list[pyVmomi.vmodl.MethodFault] = []
      supportedDiskProvisioning: list[str] = []

   class ParseDescriptorParams(CommonParams):
      pass

   class ParseDescriptorResult(pyVmomi.vmodl.DynamicData):
      eula: list[str] = []
      network: list[NetworkInfo] = []
      ipAllocationScheme: list[str] = []
      ipProtocols: list[str] = []
      property: list[pyVmomi.vim.vApp.PropertyInfo] = []
      productInfo: _typing.Optional[pyVmomi.vim.vApp.ProductInfo] = None
      annotation: str
      approximateDownloadSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      approximateFlatDeploymentSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      approximateSparseDeploymentSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      defaultEntityName: str
      virtualApp: bool
      deploymentOption: list[DeploymentOption] = []
      defaultDeploymentOption: str
      entityName: list[KeyValue] = []
      annotatedOst: _typing.Optional[OvfConsumer.OstNode] = None
      error: list[pyVmomi.vmodl.MethodFault] = []
      warning: list[pyVmomi.vmodl.MethodFault] = []

   class NetworkInfo(pyVmomi.vmodl.DynamicData):
      name: str
      description: str

   class CreateImportSpecParams(CommonParams):
      class DiskProvisioningType(pyVmomi.VmomiSupport.Enum):
         monolithicSparse: _typing.ClassVar['DiskProvisioningType'] = 'monolithicSparse'
         monolithicFlat: _typing.ClassVar['DiskProvisioningType'] = 'monolithicFlat'
         twoGbMaxExtentSparse: _typing.ClassVar['DiskProvisioningType'] = 'twoGbMaxExtentSparse'
         twoGbMaxExtentFlat: _typing.ClassVar['DiskProvisioningType'] = 'twoGbMaxExtentFlat'
         thin: _typing.ClassVar['DiskProvisioningType'] = 'thin'
         thick: _typing.ClassVar['DiskProvisioningType'] = 'thick'
         seSparse: _typing.ClassVar['DiskProvisioningType'] = 'seSparse'
         eagerZeroedThick: _typing.ClassVar['DiskProvisioningType'] = 'eagerZeroedThick'
         sparse: _typing.ClassVar['DiskProvisioningType'] = 'sparse'
         flat: _typing.ClassVar['DiskProvisioningType'] = 'flat'

      entityName: str
      hostSystem: _typing.Optional[HostSystem] = None
      networkMapping: list[NetworkMapping] = []
      ipAllocationPolicy: _typing.Optional[str] = None
      ipProtocol: _typing.Optional[str] = None
      propertyMapping: list[KeyValue] = []
      resourceMapping: list[ResourceMap] = []
      diskProvisioning: _typing.Optional[str] = None
      instantiationOst: _typing.Optional[OvfConsumer.OstNode] = None

   class ResourceMap(pyVmomi.vmodl.DynamicData):
      source: str
      parent: _typing.Optional[ResourcePool] = None
      resourceSpec: _typing.Optional[ResourceConfigSpec] = None
      datastore: _typing.Optional[Datastore] = None

   class NetworkMapping(pyVmomi.vmodl.DynamicData):
      name: str
      network: Network

   class DatastoreMapping(pyVmomi.vmodl.DynamicData):
      diskId: str
      datastore: Datastore

   class StorageProfileMapping(pyVmomi.vmodl.DynamicData):
      diskId: str
      storageProfileId: str

   class CreateImportSpecResult(pyVmomi.vmodl.DynamicData):
      importSpec: _typing.Optional[ImportSpec] = None
      fileItem: list[FileItem] = []
      warning: list[pyVmomi.vmodl.MethodFault] = []
      error: list[pyVmomi.vmodl.MethodFault] = []

   class FileItem(pyVmomi.vmodl.DynamicData):
      deviceId: str
      path: str
      compressionMethod: _typing.Optional[str] = None
      chunkSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      size: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      cimType: int
      create: bool

   class CreateDescriptorParams(pyVmomi.vmodl.DynamicData):
      ovfFiles: list[OvfFile] = []
      name: _typing.Optional[str] = None
      description: _typing.Optional[str] = None
      includeImageFiles: _typing.Optional[bool] = None
      exportOption: list[str] = []
      snapshot: _typing.Optional[pyVmomi.vim.vm.Snapshot] = None

   class CreateDescriptorResult(pyVmomi.vmodl.DynamicData):
      ovfDescriptor: str
      error: list[pyVmomi.vmodl.MethodFault] = []
      warning: list[pyVmomi.vmodl.MethodFault] = []
      includeImageFiles: _typing.Optional[bool] = None

   class OvfFile(pyVmomi.vmodl.DynamicData):
      deviceId: str
      path: str
      compressionMethod: _typing.Optional[str] = None
      chunkSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      size: pyVmomi.VmomiSupport.long
      capacity: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      populatedSize: _typing.Optional[pyVmomi.VmomiSupport.long] = None

   class OvfImportParams(CreateImportSpecParams):
      pushMode: _typing.Optional[bool] = None
      signatureRequired: _typing.Optional[bool] = None
      skipManifestCheck: _typing.Optional[bool] = None
      powerOn: _typing.Optional[bool] = None
      customHttpHeaders: list[KeyValue] = []
      sourceCertificate: _typing.Optional[str] = None
      datastoreMappings: list[DatastoreMapping] = []
      vmProfile: _typing.Optional[str] = None
      diskProfiles: list[StorageProfileMapping] = []

   @property
   def ovfImportOption(self) -> list[OvfOptionInfo]: ...
   @property
   def ovfExportOption(self) -> list[OvfOptionInfo]: ...

   def ValidateHost(self, ovfDescriptor: str, host: HostSystem, vhp: ValidateHostParams) -> ValidateHostResult: ...
   def ParseDescriptor(self, ovfDescriptor: str, pdp: ParseDescriptorParams) -> ParseDescriptorResult: ...
   def CreateImportSpec(self, ovfDescriptor: str, resourcePool: ResourcePool, datastore: Datastore, cisp: CreateImportSpecParams) -> CreateImportSpecResult: ...
   def CreateDescriptor(self, obj: ManagedEntity, cdp: CreateDescriptorParams) -> CreateDescriptorResult: ...


class PasswordField(pyVmomi.vmodl.DynamicData):
   value: str


class PerformanceDescription(pyVmomi.vmodl.DynamicData):
   counterType: list[ElementDescription] = []
   statsType: list[ElementDescription] = []


class PerformanceManager(pyVmomi.VmomiSupport.ManagedObject):
   class Format(pyVmomi.VmomiSupport.Enum):
      normal: _typing.ClassVar['Format'] = 'normal'
      csv: _typing.ClassVar['Format'] = 'csv'

   class ProviderSummary(pyVmomi.vmodl.DynamicData):
      entity: pyVmomi.VmomiSupport.ManagedObject
      currentSupported: bool
      summarySupported: bool
      refreshRate: _typing.Optional[int] = None

   class CounterInfo(pyVmomi.vmodl.DynamicData):
      class RollupType(pyVmomi.VmomiSupport.Enum):
         average: _typing.ClassVar['RollupType'] = 'average'
         maximum: _typing.ClassVar['RollupType'] = 'maximum'
         minimum: _typing.ClassVar['RollupType'] = 'minimum'
         latest: _typing.ClassVar['RollupType'] = 'latest'
         summation: _typing.ClassVar['RollupType'] = 'summation'
         none: _typing.ClassVar['RollupType'] = 'none'

      class StatsType(pyVmomi.VmomiSupport.Enum):
         absolute: _typing.ClassVar['StatsType'] = 'absolute'
         delta: _typing.ClassVar['StatsType'] = 'delta'
         rate: _typing.ClassVar['StatsType'] = 'rate'

      class Unit(pyVmomi.VmomiSupport.Enum):
         percent: _typing.ClassVar['Unit'] = 'percent'
         kiloBytes: _typing.ClassVar['Unit'] = 'kiloBytes'
         megaBytes: _typing.ClassVar['Unit'] = 'megaBytes'
         gigaBytes: _typing.ClassVar['Unit'] = 'gigaBytes'
         megaHertz: _typing.ClassVar['Unit'] = 'megaHertz'
         number: _typing.ClassVar['Unit'] = 'number'
         microsecond: _typing.ClassVar['Unit'] = 'microsecond'
         millisecond: _typing.ClassVar['Unit'] = 'millisecond'
         second: _typing.ClassVar['Unit'] = 'second'
         kiloBytesPerSecond: _typing.ClassVar['Unit'] = 'kiloBytesPerSecond'
         megaBytesPerSecond: _typing.ClassVar['Unit'] = 'megaBytesPerSecond'
         watt: _typing.ClassVar['Unit'] = 'watt'
         joule: _typing.ClassVar['Unit'] = 'joule'
         teraBytes: _typing.ClassVar['Unit'] = 'teraBytes'
         celsius: _typing.ClassVar['Unit'] = 'celsius'
         nanosecond: _typing.ClassVar['Unit'] = 'nanosecond'

      key: int
      nameInfo: ElementDescription
      groupInfo: ElementDescription
      unitInfo: ElementDescription
      rollupType: RollupType
      statsType: StatsType
      level: _typing.Optional[int] = None
      perDeviceLevel: _typing.Optional[int] = None
      associatedCounterId: list[int] = []

   class MetricId(pyVmomi.vmodl.DynamicData):
      counterId: int
      instance: str

   class QuerySpec(pyVmomi.vmodl.DynamicData):
      entity: pyVmomi.VmomiSupport.ManagedObject
      startTime: _typing.Optional[_datetime.datetime] = None
      endTime: _typing.Optional[_datetime.datetime] = None
      maxSample: _typing.Optional[int] = None
      metricId: list[MetricId] = []
      intervalId: _typing.Optional[int] = None
      format: _typing.Optional[str] = None

   class SampleInfo(pyVmomi.vmodl.DynamicData):
      timestamp: _datetime.datetime
      interval: int

   class MetricSeries(pyVmomi.vmodl.DynamicData):
      id: MetricId

   class IntSeries(MetricSeries):
      value: list[pyVmomi.VmomiSupport.long] = []

   class MetricSeriesCSV(MetricSeries):
      value: _typing.Optional[str] = None

   class EntityMetricBase(pyVmomi.vmodl.DynamicData):
      entity: pyVmomi.VmomiSupport.ManagedObject

   class EntityMetric(EntityMetricBase):
      sampleInfo: list[SampleInfo] = []
      value: list[MetricSeries] = []

   class EntityMetricCSV(EntityMetricBase):
      sampleInfoCSV: str
      value: list[MetricSeriesCSV] = []

   class CompositeEntityMetric(pyVmomi.vmodl.DynamicData):
      entity: _typing.Optional[EntityMetricBase] = None
      childEntity: list[EntityMetricBase] = []

   class CounterLevelMapping(pyVmomi.vmodl.DynamicData):
      counterId: int
      aggregateLevel: _typing.Optional[int] = None
      perDeviceLevel: _typing.Optional[int] = None

   @property
   def description(self) -> PerformanceDescription: ...
   @property
   def historicalInterval(self) -> list[HistoricalInterval]: ...
   @property
   def perfCounter(self) -> list[CounterInfo]: ...

   def QueryProviderSummary(self, entity: pyVmomi.VmomiSupport.ManagedObject) -> ProviderSummary: ...
   def QueryAvailableMetric(self, entity: pyVmomi.VmomiSupport.ManagedObject, beginTime: _typing.Optional[_datetime.datetime], endTime: _typing.Optional[_datetime.datetime], intervalId: _typing.Optional[int]) -> list[MetricId]: ...
   def QueryCounter(self, counterId: list[int]) -> list[CounterInfo]: ...
   def QueryCounterByLevel(self, level: int) -> list[CounterInfo]: ...
   def QueryStats(self, querySpec: list[QuerySpec]) -> list[EntityMetricBase]: ...
   def QueryCompositeStats(self, querySpec: QuerySpec) -> CompositeEntityMetric: ...
   def CreateHistoricalInterval(self, intervalId: HistoricalInterval) -> None: ...
   def RemoveHistoricalInterval(self, samplePeriod: int) -> None: ...
   def UpdateHistoricalInterval(self, interval: HistoricalInterval) -> None: ...
   def UpdateCounterLevelMapping(self, counterLevelMap: list[CounterLevelMapping]) -> None: ...
   def ResetCounterLevelMapping(self, counters: list[int]) -> None: ...


class PosixUserSearchResult(UserSearchResult):
   id: int
   shellAccess: _typing.Optional[bool] = None
   lastPasswordChange: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   maximumPasswordAge: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class PrivilegePolicyDef(pyVmomi.vmodl.DynamicData):
   createPrivilege: str
   readPrivilege: str
   updatePrivilege: str
   deletePrivilege: str


class ResourceAllocationInfo(pyVmomi.vmodl.DynamicData):
   reservation: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   expandableReservation: _typing.Optional[bool] = None
   limit: _typing.Optional[pyVmomi.VmomiSupport.long] = None
   shares: _typing.Optional[SharesInfo] = None
   overheadLimit: _typing.Optional[pyVmomi.VmomiSupport.long] = None


class ResourceAllocationOption(pyVmomi.vmodl.DynamicData):
   sharesOption: SharesOption


class ResourceConfigOption(pyVmomi.vmodl.DynamicData):
   cpuAllocationOption: ResourceAllocationOption
   memoryAllocationOption: ResourceAllocationOption


class ResourceConfigSpec(pyVmomi.vmodl.DynamicData):
   class ScaleSharesBehavior(pyVmomi.VmomiSupport.Enum):
      disabled: _typing.ClassVar['ScaleSharesBehavior'] = 'disabled'
      scaleCpuAndMemoryShares: _typing.ClassVar['ScaleSharesBehavior'] = 'scaleCpuAndMemoryShares'

   entity: _typing.Optional[ManagedEntity] = None
   changeVersion: _typing.Optional[str] = None
   lastModified: _typing.Optional[_datetime.datetime] = None
   cpuAllocation: ResourceAllocationInfo
   memoryAllocation: ResourceAllocationInfo
   scaleDescendantsShares: _typing.Optional[str] = None


class ResourcePlanningManager(pyVmomi.VmomiSupport.ManagedObject):
   class DatabaseSizeParam(pyVmomi.vmodl.DynamicData):
      inventoryDesc: InventoryDescription
      perfStatsDesc: _typing.Optional[PerfStatsDescription] = None

   class InventoryDescription(pyVmomi.vmodl.DynamicData):
      numHosts: int
      numVirtualMachines: int
      numResourcePools: _typing.Optional[int] = None
      numClusters: _typing.Optional[int] = None
      numCpuDev: _typing.Optional[int] = None
      numNetDev: _typing.Optional[int] = None
      numDiskDev: _typing.Optional[int] = None
      numvCpuDev: _typing.Optional[int] = None
      numvNetDev: _typing.Optional[int] = None
      numvDiskDev: _typing.Optional[int] = None

   class PerfStatsDescription(pyVmomi.vmodl.DynamicData):
      intervals: list[HistoricalInterval] = []

   class DatabaseSizeEstimate(pyVmomi.vmodl.DynamicData):
      size: pyVmomi.VmomiSupport.long

   def EstimateDatabaseSize(self, dbSizeParam: DatabaseSizeParam) -> DatabaseSizeEstimate: ...


class ResourcePool(ManagedEntity):
   class ResourceUsage(pyVmomi.vmodl.DynamicData):
      reservationUsed: pyVmomi.VmomiSupport.long
      reservationUsedForVm: pyVmomi.VmomiSupport.long
      unreservedForPool: pyVmomi.VmomiSupport.long
      unreservedForVm: pyVmomi.VmomiSupport.long
      overallUsage: pyVmomi.VmomiSupport.long
      maxUsage: pyVmomi.VmomiSupport.long

   class RuntimeInfo(pyVmomi.vmodl.DynamicData):
      memory: ResourceUsage
      cpu: ResourceUsage
      overallStatus: ManagedEntity.Status
      sharesScalable: _typing.Optional[str] = None

   class Summary(pyVmomi.vmodl.DynamicData):
      class QuickStats(pyVmomi.vmodl.DynamicData):
         overallCpuUsage: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         overallCpuDemand: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         guestMemoryUsage: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         hostMemoryUsage: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         distributedCpuEntitlement: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         distributedMemoryEntitlement: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         staticCpuEntitlement: _typing.Optional[int] = None
         staticMemoryEntitlement: _typing.Optional[int] = None
         privateMemory: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         sharedMemory: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         swappedMemory: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         balloonedMemory: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         overheadMemory: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         consumedOverheadMemory: _typing.Optional[pyVmomi.VmomiSupport.long] = None
         compressedMemory: _typing.Optional[pyVmomi.VmomiSupport.long] = None

      name: str
      config: ResourceConfigSpec
      runtime: RuntimeInfo
      quickStats: _typing.Optional[QuickStats] = None
      configuredMemoryMB: _typing.Optional[int] = None

   @property
   def summary(self) -> Summary: ...
   @property
   def runtime(self) -> RuntimeInfo: ...
   @property
   def owner(self) -> ComputeResource: ...
   @property
   def resourcePool(self) -> list[ResourcePool]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...
   @property
   def config(self) -> ResourceConfigSpec: ...
   @property
   def namespace(self) -> _typing.Optional[str]: ...
   @property
   def childConfiguration(self) -> list[ResourceConfigSpec]: ...

   def UpdateConfig(self, name: _typing.Optional[str], config: _typing.Optional[ResourceConfigSpec]) -> None: ...
   def MoveInto(self, list: list[ManagedEntity]) -> None: ...
   def UpdateChildResourceConfiguration(self, spec: list[ResourceConfigSpec]) -> None: ...
   def CreateResourcePool(self, name: str, spec: ResourceConfigSpec) -> ResourcePool: ...
   def DestroyChildren(self) -> None: ...
   def CreateVApp(self, name: str, resSpec: ResourceConfigSpec, configSpec: pyVmomi.vim.vApp.VAppConfigSpec, vmFolder: _typing.Optional[Folder]) -> VirtualApp: ...
   def CreateVm(self, config: pyVmomi.vim.vm.ConfigSpec, host: _typing.Optional[HostSystem]) -> Task: ...
   def RegisterVm(self, path: str, name: _typing.Optional[str], host: _typing.Optional[HostSystem]) -> Task: ...
   def ImportVApp(self, spec: ImportSpec, folder: _typing.Optional[Folder], host: _typing.Optional[HostSystem]) -> HttpNfcLease: ...
   def QueryResourceConfigOption(self) -> ResourceConfigOption: ...
   def RefreshRuntime(self) -> None: ...


class SDDCBase(pyVmomi.vmodl.DynamicData):
   pass


class SearchIndex(pyVmomi.VmomiSupport.ManagedObject):
   class QuerySpec(pyVmomi.vmodl.DynamicData):
      class ResourceType(pyVmomi.VmomiSupport.Enum):
         ClusterComputeResource: _typing.ClassVar['ResourceType'] = 'ClusterComputeResource'
         ComputeResource: _typing.ClassVar['ResourceType'] = 'ComputeResource'
         Datacenter: _typing.ClassVar['ResourceType'] = 'Datacenter'
         Datastore: _typing.ClassVar['ResourceType'] = 'Datastore'
         DistributedVirtualPortgroup: _typing.ClassVar['ResourceType'] = 'DistributedVirtualPortgroup'
         DistributedVirtualSwitch: _typing.ClassVar['ResourceType'] = 'DistributedVirtualSwitch'
         Folder: _typing.ClassVar['ResourceType'] = 'Folder'
         HostSystem: _typing.ClassVar['ResourceType'] = 'HostSystem'
         Network: _typing.ClassVar['ResourceType'] = 'Network'
         OpaqueNetwork: _typing.ClassVar['ResourceType'] = 'OpaqueNetwork'
         ResourcePool: _typing.ClassVar['ResourceType'] = 'ResourcePool'
         ServiceInstance: _typing.ClassVar['ResourceType'] = 'ServiceInstance'
         StoragePod: _typing.ClassVar['ResourceType'] = 'StoragePod'
         VirtualApp: _typing.ClassVar['ResourceType'] = 'VirtualApp'
         VirtualMachine: _typing.ClassVar['ResourceType'] = 'VirtualMachine'
         VmwareDistributedVirtualSwitch: _typing.ClassVar['ResourceType'] = 'VmwareDistributedVirtualSwitch'

      properties: list[str] = []
      resourceType: str
      filters: list[Filter] = []
      returnTotalCount: _typing.Optional[bool] = None
      limit: _typing.Optional[int] = None

   class IterationSpec(pyVmomi.vmodl.DynamicData):
      marker: _typing.Optional[str] = None
      limit: _typing.Optional[int] = None

   class Filter(pyVmomi.vmodl.DynamicData):
      predicates: list[Predicate] = []

   class Predicate(pyVmomi.vmodl.DynamicData):
      class ComparisonOperator(pyVmomi.VmomiSupport.Enum):
         Equal: _typing.ClassVar['ComparisonOperator'] = 'Equal'
         NotEqual: _typing.ClassVar['ComparisonOperator'] = 'NotEqual'
         Greater: _typing.ClassVar['ComparisonOperator'] = 'Greater'
         GreaterOrEqual: _typing.ClassVar['ComparisonOperator'] = 'GreaterOrEqual'
         Less: _typing.ClassVar['ComparisonOperator'] = 'Less'
         LessOrEqual: _typing.ClassVar['ComparisonOperator'] = 'LessOrEqual'
         In: _typing.ClassVar['ComparisonOperator'] = 'In'
         NotIn: _typing.ClassVar['ComparisonOperator'] = 'NotIn'
         Like: _typing.ClassVar['ComparisonOperator'] = 'Like'
         NotLike: _typing.ClassVar['ComparisonOperator'] = 'NotLike'

      class ArrayOperator(pyVmomi.VmomiSupport.Enum):
         AllElements: _typing.ClassVar['ArrayOperator'] = 'AllElements'
         AnyElement: _typing.ClassVar['ArrayOperator'] = 'AnyElement'

      propertyPath: str
      operator: str
      arrayOperator: _typing.Optional[str] = None
      comparableValue: _typing.Optional[object] = None
      comparableList: list[object] = []

   class ResultSet(pyVmomi.vmodl.DynamicData):
      properties: list[str] = []
      items: list[ResourceItem] = []
      totalCount: _typing.Optional[int] = None
      marker: _typing.Optional[str] = None

   class ResourceItem(pyVmomi.vmodl.DynamicData):
      propertyValues: list[OptionalValue] = []

   class OptionalValue(pyVmomi.vmodl.DynamicData):
      value: _typing.Optional[object] = None

   def FindByUuid(self, datacenter: _typing.Optional[Datacenter], uuid: str, vmSearch: bool, instanceUuid: _typing.Optional[bool]) -> _typing.Optional[ManagedEntity]: ...
   def FindByDatastorePath(self, datacenter: Datacenter, path: str) -> _typing.Optional[VirtualMachine]: ...
   def FindByDnsName(self, datacenter: _typing.Optional[Datacenter], dnsName: str, vmSearch: bool) -> _typing.Optional[ManagedEntity]: ...
   def FindByIp(self, datacenter: _typing.Optional[Datacenter], ip: str, vmSearch: bool) -> _typing.Optional[ManagedEntity]: ...
   def FindByInventoryPath(self, inventoryPath: str) -> _typing.Optional[ManagedEntity]: ...
   def FindChild(self, entity: ManagedEntity, name: str) -> _typing.Optional[ManagedEntity]: ...
   def FindAllByUuid(self, datacenter: _typing.Optional[Datacenter], uuid: str, vmSearch: bool, instanceUuid: _typing.Optional[bool]) -> list[ManagedEntity]: ...
   def FindAllByDnsName(self, datacenter: _typing.Optional[Datacenter], dnsName: str, vmSearch: bool) -> list[ManagedEntity]: ...
   def FindAllByIp(self, datacenter: _typing.Optional[Datacenter], ip: str, vmSearch: bool) -> list[ManagedEntity]: ...
   def Query(self, querySpec: QuerySpec) -> ResultSet: ...
   def QueryNext(self, iterationSpec: IterationSpec) -> ResultSet: ...


class SelectionSet(pyVmomi.vmodl.DynamicData):
   pass


class ServiceInstance(pyVmomi.VmomiSupport.ManagedObject):
   class ValidateMigrationTestType(pyVmomi.VmomiSupport.Enum):
      sourceTests: _typing.ClassVar['ValidateMigrationTestType'] = 'sourceTests'
      compatibilityTests: _typing.ClassVar['ValidateMigrationTestType'] = 'compatibilityTests'
      diskAccessibilityTests: _typing.ClassVar['ValidateMigrationTestType'] = 'diskAccessibilityTests'
      resourceTests: _typing.ClassVar['ValidateMigrationTestType'] = 'resourceTests'

   class VMotionCompatibilityType(pyVmomi.VmomiSupport.Enum):
      cpu: _typing.ClassVar['VMotionCompatibilityType'] = 'cpu'
      software: _typing.ClassVar['VMotionCompatibilityType'] = 'software'

   class HostVMotionCompatibility(pyVmomi.vmodl.DynamicData):
      host: HostSystem
      compatibility: list[str] = []

   class ProductComponentInfo(pyVmomi.vmodl.DynamicData):
      id: str
      name: str
      version: str
      release: int

   @property
   def serverClock(self) -> _datetime.datetime: ...
   @property
   def capability(self) -> Capability: ...
   @property
   def content(self) -> ServiceInstanceContent: ...

   def CurrentTime(self) -> _datetime.datetime: ...
   def RetrieveContent(self) -> ServiceInstanceContent: ...
   def ValidateMigration(self, vm: list[VirtualMachine], state: _typing.Optional[VirtualMachine.PowerState], testType: list[str], pool: _typing.Optional[ResourcePool], host: _typing.Optional[HostSystem]) -> list[pyVmomi.vim.event.Event]: ...
   def QueryVMotionCompatibility(self, vm: VirtualMachine, host: list[HostSystem], compatibility: list[str]) -> list[HostVMotionCompatibility]: ...
   def RetrieveProductComponents(self) -> list[ProductComponentInfo]: ...


class ServiceInstanceContent(pyVmomi.vmodl.DynamicData):
   rootFolder: Folder
   propertyCollector: pyVmomi.vmodl.query.PropertyCollector
   viewManager: _typing.Optional[pyVmomi.vim.view.ViewManager] = None
   about: AboutInfo
   setting: _typing.Optional[pyVmomi.vim.option.OptionManager] = None
   userDirectory: _typing.Optional[UserDirectory] = None
   sessionManager: _typing.Optional[SessionManager] = None
   authorizationManager: _typing.Optional[AuthorizationManager] = None
   serviceManager: _typing.Optional[ServiceManager] = None
   perfManager: _typing.Optional[PerformanceManager] = None
   scheduledTaskManager: _typing.Optional[pyVmomi.vim.scheduler.ScheduledTaskManager] = None
   alarmManager: _typing.Optional[pyVmomi.vim.alarm.AlarmManager] = None
   eventManager: _typing.Optional[pyVmomi.vim.event.EventManager] = None
   taskManager: _typing.Optional[TaskManager] = None
   extensionManager: _typing.Optional[ExtensionManager] = None
   customizationSpecManager: _typing.Optional[CustomizationSpecManager] = None
   guestCustomizationManager: _typing.Optional[pyVmomi.vim.vm.GuestCustomizationManager] = None
   customFieldsManager: _typing.Optional[CustomFieldsManager] = None
   accountManager: _typing.Optional[pyVmomi.vim.host.LocalAccountManager] = None
   diagnosticManager: _typing.Optional[DiagnosticManager] = None
   licenseManager: _typing.Optional[LicenseManager] = None
   searchIndex: _typing.Optional[SearchIndex] = None
   fileManager: _typing.Optional[FileManager] = None
   datastoreNamespaceManager: _typing.Optional[DatastoreNamespaceManager] = None
   virtualDiskManager: _typing.Optional[VirtualDiskManager] = None
   virtualizationManager: _typing.Optional[VirtualizationManager] = None
   snmpSystem: _typing.Optional[pyVmomi.vim.host.SnmpSystem] = None
   vmProvisioningChecker: _typing.Optional[pyVmomi.vim.vm.check.ProvisioningChecker] = None
   vmCompatibilityChecker: _typing.Optional[pyVmomi.vim.vm.check.CompatibilityChecker] = None
   ovfManager: _typing.Optional[OvfManager] = None
   ipPoolManager: _typing.Optional[IpPoolManager] = None
   dvSwitchManager: _typing.Optional[pyVmomi.vim.dvs.DistributedVirtualSwitchManager] = None
   hostProfileManager: _typing.Optional[pyVmomi.vim.profile.host.ProfileManager] = None
   clusterProfileManager: _typing.Optional[pyVmomi.vim.profile.cluster.ProfileManager] = None
   complianceManager: _typing.Optional[pyVmomi.vim.profile.ComplianceManager] = None
   localizationManager: _typing.Optional[LocalizationManager] = None
   storageResourceManager: _typing.Optional[StorageResourceManager] = None
   guestOperationsManager: _typing.Optional[pyVmomi.vim.vm.guest.GuestOperationsManager] = None
   overheadMemoryManager: _typing.Optional[OverheadMemoryManager] = None
   certificateManager: _typing.Optional[CertificateManager] = None
   ioFilterManager: _typing.Optional[IoFilterManager] = None
   vStorageObjectManager: _typing.Optional[pyVmomi.vim.vslm.VStorageObjectManagerBase] = None
   hostSpecManager: _typing.Optional[pyVmomi.vim.profile.host.HostSpecificationManager] = None
   cryptoManager: _typing.Optional[pyVmomi.vim.encryption.CryptoManager] = None
   healthUpdateManager: _typing.Optional[HealthUpdateManager] = None
   failoverClusterConfigurator: _typing.Optional[pyVmomi.vim.vcha.FailoverClusterConfigurator] = None
   failoverClusterManager: _typing.Optional[pyVmomi.vim.vcha.FailoverClusterManager] = None
   tenantManager: _typing.Optional[pyVmomi.vim.tenant.TenantManager] = None
   siteInfoManager: _typing.Optional[SiteInfoManager] = None
   storageQueryManager: _typing.Optional[StorageQueryManager] = None
   directPathProfileManager: _typing.Optional[DirectPathProfileManager] = None


class ServiceLocator(pyVmomi.vmodl.DynamicData):
   class Credential(pyVmomi.vmodl.DynamicData):
      pass

   class NamePassword(Credential):
      username: str
      password: str

   class SAMLCredential(Credential):
      token: _typing.Optional[str] = None

   instanceUuid: str
   url: str
   credential: Credential
   sslThumbprint: _typing.Optional[str] = None
   sslCertificate: _typing.Optional[str] = None


class ServiceManager(pyVmomi.VmomiSupport.ManagedObject):
   class ServiceInfo(pyVmomi.vmodl.DynamicData):
      serviceName: str
      location: list[str] = []
      service: pyVmomi.VmomiSupport.ManagedObject
      description: str

   @property
   def service(self) -> list[ServiceInfo]: ...

   def QueryServiceList(self, serviceName: _typing.Optional[str], location: list[str]) -> list[ServiceInfo]: ...


class SessionManager(pyVmomi.VmomiSupport.ManagedObject):
   class LocalTicket(pyVmomi.vmodl.DynamicData):
      userName: str
      passwordFilePath: str

   class GenericServiceTicket(pyVmomi.vmodl.DynamicData):
      class TicketType(pyVmomi.VmomiSupport.Enum):
         HttpNfcServiceTicket: _typing.ClassVar['TicketType'] = 'HttpNfcServiceTicket'
         HostServiceTicket: _typing.ClassVar['TicketType'] = 'HostServiceTicket'
         VcServiceTicket: _typing.ClassVar['TicketType'] = 'VcServiceTicket'

      id: str
      hostName: _typing.Optional[str] = None
      sslThumbprint: _typing.Optional[str] = None
      certThumbprintList: list[pyVmomi.vim.vm.CertThumbprint] = []
      sslCertificate: _typing.Optional[str] = None
      ticketType: _typing.Optional[str] = None

   class ServiceRequestSpec(pyVmomi.vmodl.DynamicData):
      pass

   class VmomiServiceRequestSpec(ServiceRequestSpec):
      method: pyVmomi.VmomiSupport.ManagedMethod

   class HttpServiceRequestSpec(ServiceRequestSpec):
      class Method(pyVmomi.VmomiSupport.Enum):
         httpOptions: _typing.ClassVar['Method'] = 'httpOptions'
         httpGet: _typing.ClassVar['Method'] = 'httpGet'
         httpHead: _typing.ClassVar['Method'] = 'httpHead'
         httpPost: _typing.ClassVar['Method'] = 'httpPost'
         httpPut: _typing.ClassVar['Method'] = 'httpPut'
         httpDelete: _typing.ClassVar['Method'] = 'httpDelete'
         httpTrace: _typing.ClassVar['Method'] = 'httpTrace'
         httpConnect: _typing.ClassVar['Method'] = 'httpConnect'

      method: _typing.Optional[str] = None
      url: str

   @property
   def sessionList(self) -> list[UserSession]: ...
   @property
   def currentSession(self) -> _typing.Optional[UserSession]: ...
   @property
   def message(self) -> _typing.Optional[str]: ...
   @property
   def messageLocaleList(self) -> list[str]: ...
   @property
   def supportedLocaleList(self) -> list[str]: ...
   @property
   def defaultLocale(self) -> str: ...

   def UpdateMessage(self, message: str) -> None: ...
   def LoginByToken(self, locale: _typing.Optional[str]) -> UserSession: ...
   def Login(self, userName: str, password: str, locale: _typing.Optional[str]) -> UserSession: ...
   def LoginBySSPI(self, base64Token: str, locale: _typing.Optional[str]) -> UserSession: ...
   def Logout(self) -> None: ...
   def AcquireLocalTicket(self, userName: str) -> LocalTicket: ...
   def AcquireGenericServiceTicket(self, spec: ServiceRequestSpec) -> GenericServiceTicket: ...
   def Terminate(self, sessionId: list[str]) -> None: ...
   def SetLocale(self, locale: str) -> None: ...
   def LoginExtensionBySubjectName(self, extensionKey: str, locale: _typing.Optional[str]) -> UserSession: ...
   def LoginExtensionByCertificate(self, extensionKey: str, locale: _typing.Optional[str]) -> UserSession: ...
   def ImpersonateUser(self, userName: str, locale: _typing.Optional[str]) -> UserSession: ...
   def SessionIsActive(self, sessionID: str, userName: str) -> bool: ...
   def AcquireCloneTicket(self) -> str: ...
   def CloneSession(self, cloneTicket: str) -> UserSession: ...


class SharesInfo(pyVmomi.vmodl.DynamicData):
   class Level(pyVmomi.VmomiSupport.Enum):
      low: _typing.ClassVar['Level'] = 'low'
      normal: _typing.ClassVar['Level'] = 'normal'
      high: _typing.ClassVar['Level'] = 'high'
      custom: _typing.ClassVar['Level'] = 'custom'

   shares: int
   level: Level


class SharesOption(pyVmomi.vmodl.DynamicData):
   sharesOption: pyVmomi.vim.option.IntOption
   defaultLevel: SharesInfo.Level


class SimpleCommand(pyVmomi.VmomiSupport.ManagedObject):
   class Encoding(pyVmomi.VmomiSupport.Enum):
      CSV: _typing.ClassVar['Encoding'] = 'CSV'
      HEX: _typing.ClassVar['Encoding'] = 'HEX'
      STRING: _typing.ClassVar['Encoding'] = 'STRING'

   @property
   def encodingType(self) -> Encoding: ...
   @property
   def entity(self) -> ServiceManager.ServiceInfo: ...

   def Execute(self, arguments: list[str]) -> str: ...

class SingleIp(IpAddress):
   address: str

class SingleMac(MacAddress):
   address: str


class SiteInfo(pyVmomi.vmodl.DynamicData):
   pass


class SiteInfoManager(pyVmomi.VmomiSupport.ManagedObject):
   def GetSiteInfo(self) -> SiteInfo: ...


class StoragePod(Folder):
   class Summary(pyVmomi.vmodl.DynamicData):
      name: str
      capacity: pyVmomi.VmomiSupport.long
      freeSpace: pyVmomi.VmomiSupport.long

   @property
   def summary(self) -> _typing.Optional[Summary]: ...
   @property
   def podStorageDrsEntry(self) -> _typing.Optional[StorageResourceManager.PodStorageDrsEntry]: ...


class StorageQueryManager(pyVmomi.VmomiSupport.ManagedObject):
   def QueryHostsWithAttachedLun(self, lunUuid: str) -> list[HostSystem]: ...


class StorageResourceManager(pyVmomi.VmomiSupport.ManagedObject):
   class IOAllocationInfo(pyVmomi.vmodl.DynamicData):
      limit: _typing.Optional[pyVmomi.VmomiSupport.long] = None
      shares: _typing.Optional[SharesInfo] = None
      reservation: _typing.Optional[int] = None

   class IOAllocationOption(pyVmomi.vmodl.DynamicData):
      limitOption: pyVmomi.vim.option.LongOption
      sharesOption: SharesOption

   class CongestionThresholdMode(pyVmomi.VmomiSupport.Enum):
      automatic: _typing.ClassVar['CongestionThresholdMode'] = 'automatic'
      manual: _typing.ClassVar['CongestionThresholdMode'] = 'manual'

   class IORMConfigInfo(pyVmomi.vmodl.DynamicData):
      enabled: bool
      congestionThresholdMode: str
      congestionThreshold: int
      percentOfPeakThroughput: _typing.Optional[int] = None
      statsCollectionEnabled: bool
      reservationEnabled: bool
      statsAggregationDisabled: _typing.Optional[bool] = None
      reservableIopsThreshold: _typing.Optional[int] = None

   class IORMConfigSpec(pyVmomi.vmodl.DynamicData):
      enabled: _typing.Optional[bool] = None
      congestionThresholdMode: _typing.Optional[str] = None
      congestionThreshold: _typing.Optional[int] = None
      percentOfPeakThroughput: _typing.Optional[int] = None
      statsCollectionEnabled: _typing.Optional[bool] = None
      reservationEnabled: _typing.Optional[bool] = None
      statsAggregationDisabled: _typing.Optional[bool] = None
      reservableIopsThreshold: _typing.Optional[int] = None

   class IORMConfigOption(pyVmomi.vmodl.DynamicData):
      enabledOption: pyVmomi.vim.option.BoolOption
      congestionThresholdOption: pyVmomi.vim.option.IntOption
      statsCollectionEnabledOption: pyVmomi.vim.option.BoolOption
      reservationEnabledOption: pyVmomi.vim.option.BoolOption

   class StoragePerformanceSummary(pyVmomi.vmodl.DynamicData):
      interval: int
      percentile: list[int] = []
      datastoreReadLatency: list[pyVmomi.VmomiSupport.double] = []
      datastoreWriteLatency: list[pyVmomi.VmomiSupport.double] = []
      datastoreVmLatency: list[pyVmomi.VmomiSupport.double] = []
      datastoreReadIops: list[pyVmomi.VmomiSupport.double] = []
      datastoreWriteIops: list[pyVmomi.VmomiSupport.double] = []
      siocActivityDuration: int

   class PodStorageDrsEntry(pyVmomi.vmodl.DynamicData):
      storageDrsConfig: pyVmomi.vim.storageDrs.ConfigInfo
      recommendation: list[pyVmomi.vim.cluster.Recommendation] = []
      drsFault: list[pyVmomi.vim.cluster.DrsFaults] = []
      actionHistory: list[pyVmomi.vim.cluster.ActionHistory] = []

   class StorageProfileStatistics(pyVmomi.vmodl.DynamicData):
      profileId: str
      totalSpaceMB: pyVmomi.VmomiSupport.long
      usedSpaceMB: pyVmomi.VmomiSupport.long

   def ConfigureDatastoreIORM(self, datastore: Datastore, spec: IORMConfigSpec) -> Task: ...
   def QueryIORMConfigOption(self, host: HostSystem) -> IORMConfigOption: ...
   def QueryDatastorePerformanceSummary(self, datastore: Datastore) -> list[StoragePerformanceSummary]: ...
   def ApplyRecommendationToPod(self, pod: StoragePod, key: str) -> Task: ...
   def ApplyRecommendation(self, key: list[str]) -> Task: ...
   def CancelRecommendation(self, key: list[str]) -> None: ...
   def RefreshRecommendation(self, pod: StoragePod) -> None: ...
   def RefreshRecommendationsForPod(self, pod: StoragePod) -> Task: ...
   def ConfigureStorageDrsForPod(self, pod: StoragePod, spec: pyVmomi.vim.storageDrs.ConfigSpec, modify: bool) -> Task: ...
   def ValidateStoragePodConfig(self, pod: StoragePod, spec: pyVmomi.vim.storageDrs.ConfigSpec) -> _typing.Optional[pyVmomi.vmodl.MethodFault]: ...
   def RecommendDatastores(self, storageSpec: pyVmomi.vim.storageDrs.StoragePlacementSpec) -> pyVmomi.vim.storageDrs.StoragePlacementResult: ...


class StringExpression(NegatableExpression):
   value: _typing.Optional[str] = None


class StringPolicy(InheritablePolicy):
   value: _typing.Optional[str] = None


class Tag(pyVmomi.vmodl.DynamicData):
   key: str


class TagId(pyVmomi.vmodl.DynamicData):
   class NameId(pyVmomi.vmodl.DynamicData):
      tag: str
      category: str

   nameId: _typing.Optional[NameId] = None
   uuid: _typing.Optional[str] = None


class TagSpec(pyVmomi.vim.option.ArrayUpdateSpec):
   id: TagId


class Task(ExtensibleManagedObject):
   @property
   def info(self) -> TaskInfo: ...

   def Cancel(self) -> None: ...
   def UpdateProgress(self, percentDone: int) -> None: ...
   def SetState(self, state: TaskInfo.State, result: _typing.Optional[object], fault: _typing.Optional[pyVmomi.vmodl.MethodFault]) -> None: ...
   def UpdateDescription(self, description: pyVmomi.vmodl.LocalizableMessage) -> None: ...


class TaskDescription(pyVmomi.vmodl.DynamicData):
   methodInfo: list[ElementDescription] = []
   state: list[ElementDescription] = []
   reason: list[TypeDescription] = []


class TaskFilterSpec(pyVmomi.vmodl.DynamicData):
   class RecursionOption(pyVmomi.VmomiSupport.Enum):
      self: _typing.ClassVar['RecursionOption'] = 'self'
      children: _typing.ClassVar['RecursionOption'] = 'children'
      all: _typing.ClassVar['RecursionOption'] = 'all'

   class TimeOption(pyVmomi.VmomiSupport.Enum):
      queuedTime: _typing.ClassVar['TimeOption'] = 'queuedTime'
      startedTime: _typing.ClassVar['TimeOption'] = 'startedTime'
      completedTime: _typing.ClassVar['TimeOption'] = 'completedTime'

   class ByEntity(pyVmomi.vmodl.DynamicData):
      entity: ManagedEntity
      recursion: RecursionOption

   class ByTime(pyVmomi.vmodl.DynamicData):
      timeType: TimeOption
      beginTime: _typing.Optional[_datetime.datetime] = None
      endTime: _typing.Optional[_datetime.datetime] = None

   class ByUsername(pyVmomi.vmodl.DynamicData):
      systemUser: bool
      userList: list[str] = []

   entity: _typing.Optional[ByEntity] = None
   time: _typing.Optional[ByTime] = None
   userName: _typing.Optional[ByUsername] = None
   activationId: list[str] = []
   state: list[TaskInfo.State] = []
   alarm: _typing.Optional[pyVmomi.vim.alarm.Alarm] = None
   scheduledTask: _typing.Optional[pyVmomi.vim.scheduler.ScheduledTask] = None
   eventChainId: list[int] = []
   tag: list[str] = []
   parentTaskKey: list[str] = []
   rootTaskKey: list[str] = []


class TaskHistoryCollector(HistoryCollector):
   @property
   def latestPage(self) -> list[TaskInfo]: ...

   def ReadNext(self, maxCount: int) -> list[TaskInfo]: ...
   def ReadPrev(self, maxCount: int) -> list[TaskInfo]: ...


class TaskInfo(pyVmomi.vmodl.DynamicData):
   class State(pyVmomi.VmomiSupport.Enum):
      queued: _typing.ClassVar['State'] = 'queued'
      running: _typing.ClassVar['State'] = 'running'
      success: _typing.ClassVar['State'] = 'success'
      error: _typing.ClassVar['State'] = 'error'

   key: str
   task: Task
   description: _typing.Optional[pyVmomi.vmodl.LocalizableMessage] = None
   name: _typing.Optional[pyVmomi.VmomiSupport.ManagedMethod] = None
   descriptionId: str
   entity: _typing.Optional[ManagedEntity] = None
   entityName: _typing.Optional[str] = None
   locked: list[ManagedEntity] = []
   state: State
   cancelled: bool
   cancelable: bool
   error: _typing.Optional[pyVmomi.vmodl.MethodFault] = None
   result: _typing.Optional[object] = None
   progress: _typing.Optional[int] = None
   progressDetails: list[pyVmomi.vmodl.KeyAnyValue] = []
   reason: TaskReason
   queueTime: _datetime.datetime
   startTime: _typing.Optional[_datetime.datetime] = None
   completeTime: _typing.Optional[_datetime.datetime] = None
   eventChainId: int
   changeTag: _typing.Optional[str] = None
   parentTaskKey: _typing.Optional[str] = None
   rootTaskKey: _typing.Optional[str] = None
   activationId: _typing.Optional[str] = None


class TaskInfoFilterSpec(pyVmomi.vmodl.DynamicData):
   class FilterTaskResults(pyVmomi.vmodl.DynamicData):
      removeAll: _typing.Optional[bool] = None
      descriptionIds: list[str] = []
      filterIn: _typing.Optional[bool] = None

   filterTaskResults: _typing.Optional[FilterTaskResults] = None


class TaskManager(pyVmomi.VmomiSupport.ManagedObject):
   class TaskViewSpec(pyVmomi.vmodl.DynamicData):
      pass

   class ViewByStartId(TaskViewSpec):
      count: int
      startId: str

   @property
   def recentTask(self) -> list[Task]: ...
   @property
   def description(self) -> TaskDescription: ...
   @property
   def maxCollector(self) -> int: ...

   def CreateCollector(self, filter: TaskFilterSpec) -> TaskHistoryCollector: ...
   def CreateCollectorWithInfoFilter(self, filter: TaskFilterSpec, infoFilter: _typing.Optional[TaskInfoFilterSpec]) -> TaskHistoryCollector: ...
   def CreateTask(self, obj: pyVmomi.VmomiSupport.ManagedObject, taskTypeId: str, initiatedBy: _typing.Optional[str], cancelable: bool, parentTaskKey: _typing.Optional[str], activationId: _typing.Optional[str]) -> TaskInfo: ...
   def ReadNextTasksByViewSpec(self, viewSpec: TaskViewSpec, filterSpec: TaskFilterSpec, infoFilterSpec: _typing.Optional[TaskInfoFilterSpec]) -> list[TaskInfo]: ...


class TaskReason(pyVmomi.vmodl.DynamicData):
   pass


class TaskReasonAlarm(TaskReason):
   alarmName: str
   alarm: pyVmomi.vim.alarm.Alarm
   entityName: str
   entity: ManagedEntity


class TaskReasonSchedule(TaskReason):
   name: str
   scheduledTask: pyVmomi.vim.scheduler.ScheduledTask

class TaskReasonSystem(TaskReason):
   pass

class TaskReasonUser(TaskReason):
   userName: str


class TransitGateway(ManagedEntity):
   class CreateSpec(pyVmomi.vmodl.DynamicData):
      ID: str
      name: str

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      ID: str
      name: str

   class ConfigSpec(pyVmomi.vmodl.DynamicData):
      name: _typing.Optional[str] = None

   @property
   def config(self) -> ConfigInfo: ...

class TypeDescription(Description):
   key: type


class UpdateVirtualMachineFilesResult(pyVmomi.vmodl.DynamicData):
   class FailedVmFileInfo(pyVmomi.vmodl.DynamicData):
      vmFile: str
      fault: pyVmomi.vmodl.MethodFault

   failedVmFile: list[FailedVmFileInfo] = []


class UserDirectory(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def domainList(self) -> list[str]: ...

   def RetrieveUserGroups(self, domain: _typing.Optional[str], searchStr: str, belongsToGroup: _typing.Optional[str], belongsToUser: _typing.Optional[str], exactMatch: bool, findUsers: bool, findGroups: bool) -> list[UserSearchResult]: ...


class UserSearchResult(pyVmomi.vmodl.DynamicData):
   principal: str
   fullName: _typing.Optional[str] = None
   group: bool


class UserSession(pyVmomi.vmodl.DynamicData):
   key: str
   userName: str
   fullName: str
   loginTime: _datetime.datetime
   lastActiveTime: _datetime.datetime
   locale: str
   messageLocale: str
   extensionSession: bool
   ipAddress: str
   userAgent: str
   callCount: pyVmomi.VmomiSupport.long


class VVolVmConfigFileUpdateResult(pyVmomi.vmodl.DynamicData):
   class FailedVmConfigFileInfo(pyVmomi.vmodl.DynamicData):
      targetConfigVVolId: str
      dsPath: _typing.Optional[str] = None
      fault: pyVmomi.vmodl.MethodFault

   succeededVmConfigFile: list[KeyValue] = []
   failedVmConfigFile: list[FailedVmConfigFileInfo] = []


class VasaStorageArray(pyVmomi.vmodl.DynamicData):
   class DiscoverySvcInfo(pyVmomi.vmodl.DynamicData):
      portType: str
      svcNqn: str
      ipInfo: _typing.Optional[DiscoveryIpTransport] = None
      fcInfo: _typing.Optional[DiscoveryFcTransport] = None

   class DiscoveryFcTransport(pyVmomi.vmodl.DynamicData):
      nodeWwn: str
      portWwn: str

   class DiscoveryIpTransport(pyVmomi.vmodl.DynamicData):
      ipAddress: str
      portNumber: _typing.Optional[str] = None

   name: str
   uuid: str
   vendorId: str
   modelId: str
   discoverySvcInfo: list[DiscoverySvcInfo] = []


class VimVasaProvider(pyVmomi.vmodl.DynamicData):
   class StatePerArray(pyVmomi.vmodl.DynamicData):
      priority: int
      arrayId: str
      active: bool

   class VirtualHostConfig(pyVmomi.vmodl.DynamicData):
      vhostName: _typing.Optional[str] = None
      serviceHost: str
      servicePort: _typing.Optional[int] = None

   uid: _typing.Optional[str] = None
   url: str
   name: _typing.Optional[str] = None
   selfSignedCertificate: _typing.Optional[str] = None
   vhostConfig: _typing.Optional[VirtualHostConfig] = None
   versionId: _typing.Optional[int] = None


class VimVasaProviderInfo(pyVmomi.vmodl.DynamicData):
   provider: VimVasaProvider
   arrayState: list[VimVasaProvider.StatePerArray] = []


class VirtualApp(ResourcePool):
   class VAppState(pyVmomi.VmomiSupport.Enum):
      started: _typing.ClassVar['VAppState'] = 'started'
      stopped: _typing.ClassVar['VAppState'] = 'stopped'
      starting: _typing.ClassVar['VAppState'] = 'starting'
      stopping: _typing.ClassVar['VAppState'] = 'stopping'

   class Summary(ResourcePool.Summary):
      product: _typing.Optional[pyVmomi.vim.vApp.ProductInfo] = None
      vAppState: _typing.Optional[VAppState] = None
      suspended: _typing.Optional[bool] = None
      installBootRequired: _typing.Optional[bool] = None
      instanceUuid: _typing.Optional[str] = None

   class LinkInfo(pyVmomi.vmodl.DynamicData):
      key: ManagedEntity
      destroyWithParent: _typing.Optional[bool] = None

   @property
   def parentFolder(self) -> _typing.Optional[Folder]: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def vAppConfig(self) -> _typing.Optional[pyVmomi.vim.vApp.VAppConfigInfo]: ...
   @property
   def parentVApp(self) -> _typing.Optional[ManagedEntity]: ...
   @property
   def childLink(self) -> list[LinkInfo]: ...

   def UpdateVAppConfig(self, spec: pyVmomi.vim.vApp.VAppConfigSpec) -> None: ...
   def UpdateLinkedChildren(self, addChangeSet: list[LinkInfo], removeSet: list[ManagedEntity]) -> None: ...
   def Clone(self, name: str, target: ResourcePool, spec: pyVmomi.vim.vApp.CloneSpec) -> Task: ...
   def ExportVApp(self) -> HttpNfcLease: ...
   def PowerOn(self) -> Task: ...
   def PowerOff(self, force: bool) -> Task: ...
   def Suspend(self) -> Task: ...
   def Unregister(self) -> Task: ...


class VirtualDiskManager(pyVmomi.VmomiSupport.ManagedObject):
   class VirtualDiskType(pyVmomi.VmomiSupport.Enum):
      preallocated: _typing.ClassVar['VirtualDiskType'] = 'preallocated'
      thin: _typing.ClassVar['VirtualDiskType'] = 'thin'
      seSparse: _typing.ClassVar['VirtualDiskType'] = 'seSparse'
      rdm: _typing.ClassVar['VirtualDiskType'] = 'rdm'
      rdmp: _typing.ClassVar['VirtualDiskType'] = 'rdmp'
      raw: _typing.ClassVar['VirtualDiskType'] = 'raw'
      delta: _typing.ClassVar['VirtualDiskType'] = 'delta'
      sparse2Gb: _typing.ClassVar['VirtualDiskType'] = 'sparse2Gb'
      thick2Gb: _typing.ClassVar['VirtualDiskType'] = 'thick2Gb'
      eagerZeroedThick: _typing.ClassVar['VirtualDiskType'] = 'eagerZeroedThick'
      sparseMonolithic: _typing.ClassVar['VirtualDiskType'] = 'sparseMonolithic'
      flatMonolithic: _typing.ClassVar['VirtualDiskType'] = 'flatMonolithic'
      thick: _typing.ClassVar['VirtualDiskType'] = 'thick'

   class VirtualDiskAdapterType(pyVmomi.VmomiSupport.Enum):
      ide: _typing.ClassVar['VirtualDiskAdapterType'] = 'ide'
      busLogic: _typing.ClassVar['VirtualDiskAdapterType'] = 'busLogic'
      lsiLogic: _typing.ClassVar['VirtualDiskAdapterType'] = 'lsiLogic'

   class VirtualDiskSpec(pyVmomi.vmodl.DynamicData):
      diskType: str
      adapterType: str

   class FileBackedVirtualDiskSpec(VirtualDiskSpec):
      capacityKb: pyVmomi.VmomiSupport.long
      profile: list[pyVmomi.vim.vm.ProfileSpec] = []
      crypto: _typing.Optional[pyVmomi.vim.encryption.CryptoSpec] = None
      sectorFormat: _typing.Optional[str] = None

   class SeSparseVirtualDiskSpec(FileBackedVirtualDiskSpec):
      grainSizeKb: _typing.Optional[int] = None

   class DeviceBackedVirtualDiskSpec(VirtualDiskSpec):
      device: str

   def CreateVirtualDisk(self, name: str, datacenter: _typing.Optional[Datacenter], spec: VirtualDiskSpec) -> Task: ...
   def DeleteVirtualDisk(self, name: str, datacenter: _typing.Optional[Datacenter]) -> Task: ...
   def MoveVirtualDisk(self, sourceName: str, sourceDatacenter: _typing.Optional[Datacenter], destName: str, destDatacenter: _typing.Optional[Datacenter], force: _typing.Optional[bool], profile: list[pyVmomi.vim.vm.ProfileSpec]) -> Task: ...
   def CopyVirtualDisk(self, sourceName: str, sourceDatacenter: _typing.Optional[Datacenter], destName: str, destDatacenter: _typing.Optional[Datacenter], destSpec: _typing.Optional[VirtualDiskSpec], force: _typing.Optional[bool]) -> Task: ...
   def ExtendVirtualDisk(self, name: str, datacenter: _typing.Optional[Datacenter], newCapacityKb: pyVmomi.VmomiSupport.long, eagerZero: _typing.Optional[bool]) -> Task: ...
   def QueryVirtualDiskFragmentation(self, name: str, datacenter: _typing.Optional[Datacenter]) -> int: ...
   def DefragmentVirtualDisk(self, name: str, datacenter: _typing.Optional[Datacenter]) -> Task: ...
   def ShrinkVirtualDisk(self, name: str, datacenter: _typing.Optional[Datacenter], copy: _typing.Optional[bool]) -> Task: ...
   def InflateVirtualDisk(self, name: str, datacenter: _typing.Optional[Datacenter]) -> Task: ...
   def EagerZeroVirtualDisk(self, name: str, datacenter: _typing.Optional[Datacenter]) -> Task: ...
   def ZeroFillVirtualDisk(self, name: str, datacenter: _typing.Optional[Datacenter]) -> Task: ...
   def SetVirtualDiskUuid(self, name: str, datacenter: _typing.Optional[Datacenter], uuid: str) -> None: ...
   def QueryVirtualDiskUuid(self, name: str, datacenter: _typing.Optional[Datacenter]) -> str: ...
   def QueryVirtualDiskGeometry(self, name: str, datacenter: _typing.Optional[Datacenter]) -> pyVmomi.vim.host.DiskDimensions.Chs: ...
   def ImportUnmanagedSnapshot(self, vdisk: str, datacenter: _typing.Optional[Datacenter], vvolId: str) -> None: ...
   def ReleaseManagedSnapshot(self, vdisk: str, datacenter: _typing.Optional[Datacenter]) -> None: ...


class VirtualMachine(ManagedEntity):
   class StorageRequirement(pyVmomi.vmodl.DynamicData):
      datastore: Datastore
      freeSpaceRequiredInKb: pyVmomi.VmomiSupport.long

   class PowerState(pyVmomi.VmomiSupport.Enum):
      poweredOff: _typing.ClassVar['PowerState'] = 'poweredOff'
      poweredOn: _typing.ClassVar['PowerState'] = 'poweredOn'
      suspended: _typing.ClassVar['PowerState'] = 'suspended'

   class AppHeartbeatStatusType(pyVmomi.VmomiSupport.Enum):
      appStatusGray: _typing.ClassVar['AppHeartbeatStatusType'] = 'appStatusGray'
      appStatusGreen: _typing.ClassVar['AppHeartbeatStatusType'] = 'appStatusGreen'
      appStatusRed: _typing.ClassVar['AppHeartbeatStatusType'] = 'appStatusRed'

   class ConnectionState(pyVmomi.VmomiSupport.Enum):
      connected: _typing.ClassVar['ConnectionState'] = 'connected'
      disconnected: _typing.ClassVar['ConnectionState'] = 'disconnected'
      orphaned: _typing.ClassVar['ConnectionState'] = 'orphaned'
      inaccessible: _typing.ClassVar['ConnectionState'] = 'inaccessible'
      invalid: _typing.ClassVar['ConnectionState'] = 'invalid'

   class CryptoState(pyVmomi.VmomiSupport.Enum):
      unlocked: _typing.ClassVar['CryptoState'] = 'unlocked'
      locked: _typing.ClassVar['CryptoState'] = 'locked'

   class MovePriority(pyVmomi.VmomiSupport.Enum):
      lowPriority: _typing.ClassVar['MovePriority'] = 'lowPriority'
      highPriority: _typing.ClassVar['MovePriority'] = 'highPriority'
      defaultPriority: _typing.ClassVar['MovePriority'] = 'defaultPriority'

   class Ticket(pyVmomi.vmodl.DynamicData):
      ticket: str
      cfgFile: str
      host: _typing.Optional[str] = None
      port: _typing.Optional[int] = None
      sslThumbprint: _typing.Optional[str] = None
      certThumbprintList: list[pyVmomi.vim.vm.CertThumbprint] = []
      sslCertificate: _typing.Optional[str] = None
      url: _typing.Optional[str] = None

   class MksTicket(pyVmomi.vmodl.DynamicData):
      ticket: str
      cfgFile: str
      host: _typing.Optional[str] = None
      port: _typing.Optional[int] = None
      sslThumbprint: _typing.Optional[str] = None

   class FaultToleranceState(pyVmomi.VmomiSupport.Enum):
      notConfigured: _typing.ClassVar['FaultToleranceState'] = 'notConfigured'
      disabled: _typing.ClassVar['FaultToleranceState'] = 'disabled'
      enabled: _typing.ClassVar['FaultToleranceState'] = 'enabled'
      needSecondary: _typing.ClassVar['FaultToleranceState'] = 'needSecondary'
      starting: _typing.ClassVar['FaultToleranceState'] = 'starting'
      running: _typing.ClassVar['FaultToleranceState'] = 'running'

   class RecordReplayState(pyVmomi.VmomiSupport.Enum):
      recording: _typing.ClassVar['RecordReplayState'] = 'recording'
      replaying: _typing.ClassVar['RecordReplayState'] = 'replaying'
      inactive: _typing.ClassVar['RecordReplayState'] = 'inactive'

   class NeedSecondaryReason(pyVmomi.VmomiSupport.Enum):
      initializing: _typing.ClassVar['NeedSecondaryReason'] = 'initializing'
      divergence: _typing.ClassVar['NeedSecondaryReason'] = 'divergence'
      lostConnection: _typing.ClassVar['NeedSecondaryReason'] = 'lostConnection'
      partialHardwareFailure: _typing.ClassVar['NeedSecondaryReason'] = 'partialHardwareFailure'
      userAction: _typing.ClassVar['NeedSecondaryReason'] = 'userAction'
      checkpointError: _typing.ClassVar['NeedSecondaryReason'] = 'checkpointError'
      other: _typing.ClassVar['NeedSecondaryReason'] = 'other'

   class FaultToleranceType(pyVmomi.VmomiSupport.Enum):
      unset: _typing.ClassVar['FaultToleranceType'] = 'unset'
      recordReplay: _typing.ClassVar['FaultToleranceType'] = 'recordReplay'
      checkpointing: _typing.ClassVar['FaultToleranceType'] = 'checkpointing'

   class Connection(pyVmomi.vmodl.DynamicData):
      label: str
      client: str
      userName: str

   class MksConnection(Connection):
      pass

   class TicketType(pyVmomi.VmomiSupport.Enum):
      mks: _typing.ClassVar['TicketType'] = 'mks'
      device: _typing.ClassVar['TicketType'] = 'device'
      guestControl: _typing.ClassVar['TicketType'] = 'guestControl'
      dnd: _typing.ClassVar['TicketType'] = 'dnd'
      webmks: _typing.ClassVar['TicketType'] = 'webmks'
      guestIntegrity: _typing.ClassVar['TicketType'] = 'guestIntegrity'
      webRemoteDevice: _typing.ClassVar['TicketType'] = 'webRemoteDevice'

   class DisplayTopology(pyVmomi.vmodl.DynamicData):
      x: int
      y: int
      width: int
      height: int

   class DiskChangeInfo(pyVmomi.vmodl.DynamicData):
      class DiskChangeExtent(pyVmomi.vmodl.DynamicData):
         start: pyVmomi.VmomiSupport.long
         length: pyVmomi.VmomiSupport.long

      startOffset: pyVmomi.VmomiSupport.long
      length: pyVmomi.VmomiSupport.long
      changedArea: list[DiskChangeExtent] = []

   class WipeResult(pyVmomi.vmodl.DynamicData):
      diskId: int
      shrinkableDiskSpace: pyVmomi.VmomiSupport.long

   @property
   def capability(self) -> pyVmomi.vim.vm.Capability: ...
   @property
   def config(self) -> _typing.Optional[pyVmomi.vim.vm.ConfigInfo]: ...
   @property
   def layout(self) -> _typing.Optional[pyVmomi.vim.vm.FileLayout]: ...
   @property
   def layoutEx(self) -> _typing.Optional[pyVmomi.vim.vm.FileLayoutEx]: ...
   @property
   def storage(self) -> _typing.Optional[pyVmomi.vim.vm.StorageInfo]: ...
   @property
   def environmentBrowser(self) -> EnvironmentBrowser: ...
   @property
   def resourcePool(self) -> _typing.Optional[ResourcePool]: ...
   @property
   def parentVApp(self) -> _typing.Optional[ManagedEntity]: ...
   @property
   def resourceConfig(self) -> _typing.Optional[ResourceConfigSpec]: ...
   @property
   def runtime(self) -> pyVmomi.vim.vm.RuntimeInfo: ...
   @property
   def guest(self) -> _typing.Optional[pyVmomi.vim.vm.GuestInfo]: ...
   @property
   def summary(self) -> pyVmomi.vim.vm.Summary: ...
   @property
   def datastore(self) -> list[Datastore]: ...
   @property
   def network(self) -> list[Network]: ...
   @property
   def snapshot(self) -> _typing.Optional[pyVmomi.vim.vm.SnapshotInfo]: ...
   @property
   def rootSnapshot(self) -> list[pyVmomi.vim.vm.Snapshot]: ...
   @property
   def guestHeartbeatStatus(self) -> ManagedEntity.Status: ...

   def RefreshStorageInfo(self) -> None: ...
   def CreateSnapshot(self, name: str, description: _typing.Optional[str], memory: bool, quiesce: bool) -> Task: ...
   def CreateSnapshotEx(self, name: str, description: _typing.Optional[str], memory: bool, quiesceSpec: _typing.Optional[pyVmomi.vim.vm.GuestQuiesceSpec]) -> Task: ...
   def RevertToCurrentSnapshot(self, host: _typing.Optional[HostSystem], suppressPowerOn: _typing.Optional[bool]) -> Task: ...
   def RemoveAllSnapshots(self, consolidate: _typing.Optional[bool], spec: _typing.Optional[pyVmomi.vim.vm.SnapshotSelectionSpec]) -> Task: ...
   def ConsolidateDisks(self) -> Task: ...
   def EstimateStorageRequirementForConsolidate(self) -> Task: ...
   def Reconfigure(self, spec: pyVmomi.vim.vm.ConfigSpec) -> Task: ...
   def UpgradeVirtualHardware(self, version: _typing.Optional[str]) -> Task: ...
   def ExtractOvfEnvironment(self) -> str: ...
   def PowerOn(self, host: _typing.Optional[HostSystem]) -> Task: ...
   def PowerOff(self) -> Task: ...
   def Suspend(self) -> Task: ...
   def Reset(self) -> Task: ...
   def ShutdownGuest(self) -> None: ...
   def RebootGuest(self) -> None: ...
   def StandbyGuest(self) -> None: ...
   def Answer(self, questionId: str, answerChoice: str) -> None: ...
   def Customize(self, spec: pyVmomi.vim.vm.customization.Specification) -> Task: ...
   def CheckCustomizationSpec(self, spec: pyVmomi.vim.vm.customization.Specification) -> None: ...
   def Migrate(self, pool: _typing.Optional[ResourcePool], host: _typing.Optional[HostSystem], priority: MovePriority, state: _typing.Optional[PowerState]) -> Task: ...
   def Relocate(self, spec: pyVmomi.vim.vm.RelocateSpec, priority: _typing.Optional[MovePriority]) -> Task: ...
   def Clone(self, folder: Folder, name: str, spec: pyVmomi.vim.vm.CloneSpec) -> Task: ...
   def InstantClone(self, spec: pyVmomi.vim.vm.InstantCloneSpec) -> Task: ...
   def ExportVm(self) -> HttpNfcLease: ...
   def MarkAsTemplate(self) -> None: ...
   def MarkAsVirtualMachine(self, pool: ResourcePool, host: _typing.Optional[HostSystem]) -> None: ...
   def Unregister(self) -> None: ...
   def ResetGuestInformation(self) -> None: ...
   def MountToolsInstaller(self) -> None: ...
   def UnmountToolsInstaller(self) -> None: ...
   def UpgradeTools(self, installerOptions: _typing.Optional[str]) -> Task: ...
   def AcquireMksTicket(self) -> MksTicket: ...
   def QueryConnections(self) -> list[Connection]: ...
   def DropConnections(self, listOfConnections: list[Connection]) -> bool: ...
   def AcquireTicket(self, ticketType: str) -> Ticket: ...
   def SetScreenResolution(self, width: int, height: int) -> None: ...
   def DefragmentAllDisks(self) -> None: ...
   def CreateSecondary(self, host: _typing.Optional[HostSystem]) -> Task: ...
   def CreateSecondaryEx(self, host: _typing.Optional[HostSystem], spec: _typing.Optional[pyVmomi.vim.vm.FaultToleranceConfigSpec]) -> Task: ...
   def TurnOffFaultTolerance(self) -> Task: ...
   def MakePrimary(self, vm: VirtualMachine) -> Task: ...
   def TerminateFaultTolerantVM(self, vm: _typing.Optional[VirtualMachine]) -> Task: ...
   def DisableSecondary(self, vm: VirtualMachine) -> Task: ...
   def EnableSecondary(self, vm: VirtualMachine, host: _typing.Optional[HostSystem]) -> Task: ...
   def SetDisplayTopology(self, displays: list[DisplayTopology]) -> None: ...
   def StartRecording(self, name: str, description: _typing.Optional[str]) -> Task: ...
   def StopRecording(self) -> Task: ...
   def StartReplaying(self, replaySnapshot: pyVmomi.vim.vm.Snapshot) -> Task: ...
   def StopReplaying(self) -> Task: ...
   def PromoteDisks(self, unlink: bool, disks: list[pyVmomi.vim.vm.device.VirtualDisk]) -> Task: ...
   def CreateScreenshot(self) -> Task: ...
   def PutUsbScanCodes(self, spec: pyVmomi.vim.vm.UsbScanCodeSpec) -> int: ...
   def QueryChangedDiskAreas(self, snapshot: _typing.Optional[pyVmomi.vim.vm.Snapshot], deviceKey: int, startOffset: pyVmomi.VmomiSupport.long, changeId: str) -> DiskChangeInfo: ...
   def QueryUnownedFiles(self) -> list[str]: ...
   def ReloadFromPath(self, configurationPath: str) -> Task: ...
   def QueryFaultToleranceCompatibility(self) -> list[pyVmomi.vmodl.MethodFault]: ...
   def QueryFaultToleranceCompatibilityEx(self, forLegacyFt: _typing.Optional[bool]) -> list[pyVmomi.vmodl.MethodFault]: ...
   def Terminate(self) -> None: ...
   def SendNMI(self) -> None: ...
   def AttachDisk(self, diskId: pyVmomi.vim.vslm.ID, datastore: Datastore, controllerKey: _typing.Optional[int], unitNumber: _typing.Optional[int]) -> Task: ...
   def DetachDisk(self, diskId: pyVmomi.vim.vslm.ID) -> Task: ...
   def ApplyEvcMode(self, mask: list[pyVmomi.vim.host.FeatureMask], completeMasks: _typing.Optional[bool]) -> Task: ...
   def CryptoUnlock(self) -> Task: ...
   def RepairVmDiskChains(self) -> Task: ...


class VirtualizationManager(pyVmomi.VmomiSupport.ManagedObject):
   pass


class VsanComparator(pyVmomi.vmodl.DynamicData):
   pass


class VsanCompositeConstraint(VsanResourceConstraint):
   nestedConstraints: list[VsanResourceConstraint] = []
   conjoiner: _typing.Optional[str] = None

class VsanCompositeConstraintConjoinerEnum:
   pass


class VsanDataObfuscationRule(pyVmomi.vmodl.DynamicData):
   pass


class VsanJsonComparator(VsanComparator):
   comparator: _typing.Optional[str] = None
   comparableValue: _typing.Optional[pyVmomi.vmodl.KeyAnyValue] = None


class VsanJsonFilterRule(pyVmomi.vmodl.DynamicData):
   filterComparator: _typing.Optional[VsanComparator] = None
   comparablePath: list[str] = []
   keysWithStrVal: list[str] = []
   propertyName: _typing.Optional[str] = None


class VsanMassCollector(pyVmomi.VmomiSupport.ManagedObject):
   def VsanRetrieveProperties(self, massCollectorSpecs: list[VsanMassCollectorSpec]) -> list[pyVmomi.vmodl.query.PropertyCollector.ObjectContent]: ...

class VsanMassCollectorObjectCollectionEnum:
   pass


class VsanMassCollectorPropertyParams(pyVmomi.vmodl.DynamicData):
   propertyName: _typing.Optional[str] = None
   propertyParams: list[pyVmomi.vmodl.KeyAnyValue] = []


class VsanMassCollectorSpec(pyVmomi.vmodl.DynamicData):
   objects: list[pyVmomi.VmomiSupport.ManagedObject] = []
   objectCollection: _typing.Optional[str] = None
   properties: list[str] = []
   propertiesParams: list[VsanMassCollectorPropertyParams] = []
   constraint: _typing.Optional[VsanResourceConstraint] = None


class VsanNestJsonComparator(VsanComparator):
   nestedComparators: list[VsanJsonComparator] = []
   conjoiner: _typing.Optional[str] = None


class VsanObjectTypeRule(pyVmomi.vmodl.DynamicData):
   objectType: _typing.Optional[str] = None
   attributes: list[str] = []


class VsanPhoneHomeSystem(pyVmomi.VmomiSupport.ManagedObject):
   def VsanPerformOnlineHealthCheck(self, cluster: ClusterComputeResource) -> Task: ...
   def QueryVsanCloudHealthStatus(self) -> _typing.Optional[pyVmomi.vim.vsan.VsanCloudHealthStatus]: ...
   def VsanQueryObjectSnapshotsInfo(self, cluster: ClusterComputeResource) -> _typing.Optional[str]: ...
   def VsanQueryNvmeCriticalWarningStats(self, cluster: ClusterComputeResource) -> _typing.Optional[str]: ...
   def VsanQueryZdomScrubberData(self, cluster: ClusterComputeResource) -> _typing.Optional[str]: ...
   def VsanQueryLSOMwbsize(self, cluster: ClusterComputeResource) -> _typing.Optional[str]: ...


class VsanPropertyConstraint(VsanResourceConstraint):
   propertyName: _typing.Optional[str] = None
   comparator: _typing.Optional[str] = None
   comparableValue: _typing.Optional[pyVmomi.vmodl.KeyAnyValue] = None

class VsanPropertyConstraintComparatorEnum:
   pass


class VsanRegexBasedRule(pyVmomi.vmodl.DynamicData):
   rules: list[str] = []


class VsanResourceConstraint(pyVmomi.vmodl.DynamicData):
   targetType: _typing.Optional[str] = None


class VsanUpgradeSystem(pyVmomi.VmomiSupport.ManagedObject):
   class PreflightCheckIssue(pyVmomi.vmodl.DynamicData):
      msg: str

   class HostsDisconnectedIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class MissingHostsInClusterIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class RogueHostsInClusterIssue(PreflightCheckIssue):
      uuids: list[str] = []

   class WrongEsxVersionIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class AutoClaimEnabledOnHostsIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class APIBrokenIssue(PreflightCheckIssue):
      hosts: list[HostSystem] = []

   class V2ObjectsPresentDuringDowngradeIssue(PreflightCheckIssue):
      uuids: list[str] = []

   class NotEnoughFreeCapacityIssue(PreflightCheckIssue):
      reducedRedundancyUpgradePossible: bool

   class NetworkPartitionInfo(pyVmomi.vmodl.DynamicData):
      hosts: list[HostSystem] = []

   class NetworkPartitionIssue(PreflightCheckIssue):
      partitions: list[NetworkPartitionInfo] = []

   class PreflightCheckResult(pyVmomi.vmodl.DynamicData):
      issues: list[PreflightCheckIssue] = []
      diskMappingToRestore: _typing.Optional[pyVmomi.vim.vsan.host.DiskMapping] = None

   class UpgradeHistoryItem(pyVmomi.vmodl.DynamicData):
      timestamp: _datetime.datetime
      host: _typing.Optional[HostSystem] = None
      message: str
      task: _typing.Optional[Task] = None

   class UpgradeHistoryDiskGroupOpType(pyVmomi.VmomiSupport.Enum):
      add: _typing.ClassVar['UpgradeHistoryDiskGroupOpType'] = 'add'
      remove: _typing.ClassVar['UpgradeHistoryDiskGroupOpType'] = 'remove'

   class UpgradeHistoryDiskGroupOp(UpgradeHistoryItem):
      operation: str
      diskMapping: pyVmomi.vim.vsan.host.DiskMapping

   class UpgradeHistoryPreflightFail(UpgradeHistoryItem):
      preflightResult: PreflightCheckResult

   class UpgradeStatus(pyVmomi.vmodl.DynamicData):
      inProgress: bool
      history: list[UpgradeHistoryItem] = []
      aborted: _typing.Optional[bool] = None
      completed: _typing.Optional[bool] = None
      progress: _typing.Optional[int] = None

   def PerformUpgradePreflightCheck(self, cluster: ClusterComputeResource, downgradeFormat: _typing.Optional[bool]) -> PreflightCheckResult: ...
   def QueryUpgradeStatus(self, cluster: ClusterComputeResource) -> UpgradeStatus: ...
   def PerformUpgrade(self, cluster: ClusterComputeResource, performObjectUpgrade: _typing.Optional[bool], downgradeFormat: _typing.Optional[bool], allowReducedRedundancy: _typing.Optional[bool], excludeHosts: list[HostSystem]) -> Task: ...


class VsanUpgradeSystemEx(pyVmomi.VmomiSupport.ManagedObject):
   def PerformUpgrade(self, cluster: ClusterComputeResource, performObjectUpgrade: _typing.Optional[bool], downgradeFormat: _typing.Optional[bool], allowReducedRedundancy: _typing.Optional[bool], excludeHosts: list[HostSystem], spec: _typing.Optional[pyVmomi.vim.cluster.VsanDiskFormatConversionSpec]) -> Task: ...
   def PerformUpgradePreflightAsyncCheck(self, cluster: ClusterComputeResource, downgradeFormat: _typing.Optional[bool], spec: _typing.Optional[pyVmomi.vim.cluster.VsanDiskFormatConversionSpec]) -> Task: ...
   def PerformUpgradePreflightCheck(self, cluster: ClusterComputeResource, downgradeFormat: _typing.Optional[bool], spec: _typing.Optional[pyVmomi.vim.cluster.VsanDiskFormatConversionSpec]) -> pyVmomi.vim.cluster.VsanDiskFormatConversionCheckResult: ...
   def RetrieveSupportedFormatVersion(self, cluster: ClusterComputeResource) -> int: ...
   def QueryUpgradeStatus(self, cluster: ClusterComputeResource) -> pyVmomi.vim.cluster.VsanUpgradeStatusEx: ...
