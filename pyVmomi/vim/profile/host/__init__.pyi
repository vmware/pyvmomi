# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.fault
import pyVmomi.vim.host
import pyVmomi.vim.profile



class ActiveDirectoryProfile(pyVmomi.vim.profile.ApplyProfile):
   pass


class AnswerFile(pyVmomi.vmodl.DynamicData):
   userInput: list[pyVmomi.vim.profile.DeferredPolicyOptionParameter] = []
   createdTime: _datetime.datetime
   modifiedTime: _datetime.datetime


class AnswerFileStatusResult(pyVmomi.vmodl.DynamicData):
   class AnswerFileStatusError(pyVmomi.vmodl.DynamicData):
      userInputPath: pyVmomi.vim.profile.ProfilePropertyPath
      errMsg: pyVmomi.vmodl.LocalizableMessage

   checkedTime: _datetime.datetime
   host: pyVmomi.vim.HostSystem
   status: str
   error: list[AnswerFileStatusError] = []


class AuthenticationProfile(pyVmomi.vim.profile.ApplyProfile):
   activeDirectory: _typing.Optional[ActiveDirectoryProfile] = None


class DateTimeProfile(pyVmomi.vim.profile.ApplyProfile):
   pass

class DvsHostVNicProfile(DvsVNicProfile):
   pass


class DvsProfile(pyVmomi.vim.profile.ApplyProfile):
   key: str
   name: str
   uplink: list[PnicUplinkProfile] = []

class DvsServiceConsoleVNicProfile(DvsVNicProfile):
   pass


class DvsVNicProfile(pyVmomi.vim.profile.ApplyProfile):
   key: str
   ipConfig: IpAddressProfile


class ExecuteResult(pyVmomi.vmodl.DynamicData):
   class Status(pyVmomi.VmomiSupport.Enum):
      success: _typing.ClassVar['Status'] = 'success'
      needInput: _typing.ClassVar['Status'] = 'needInput'
      error: _typing.ClassVar['Status'] = 'error'

   class ExecuteError(pyVmomi.vmodl.DynamicData):
      path: _typing.Optional[pyVmomi.vim.profile.ProfilePropertyPath] = None
      message: pyVmomi.vmodl.LocalizableMessage

   status: str
   configSpec: _typing.Optional[pyVmomi.vim.host.ConfigSpec] = None
   inapplicablePath: list[pyVmomi.VmomiSupport.PropertyPath] = []
   requireInput: list[pyVmomi.vim.profile.DeferredPolicyOptionParameter] = []
   error: list[ExecuteError] = []


class FirewallProfile(pyVmomi.vim.profile.ApplyProfile):
   class RulesetProfile(pyVmomi.vim.profile.ApplyProfile):
      key: str

   ruleset: list[RulesetProfile] = []


class HostApplyProfile(pyVmomi.vim.profile.ApplyProfile):
   memory: _typing.Optional[HostMemoryProfile] = None
   storage: _typing.Optional[StorageProfile] = None
   network: _typing.Optional[NetworkProfile] = None
   datetime: _typing.Optional[DateTimeProfile] = None
   firewall: _typing.Optional[FirewallProfile] = None
   security: _typing.Optional[SecurityProfile] = None
   service: list[ServiceProfile] = []
   option: list[OptionProfile] = []
   userAccount: list[UserProfile] = []
   usergroupAccount: list[UserGroupProfile] = []
   authentication: _typing.Optional[AuthenticationProfile] = None


class HostMemoryProfile(pyVmomi.vim.profile.ApplyProfile):
   pass

class HostPortGroupProfile(PortGroupProfile):
   ipConfig: IpAddressProfile


class HostProfile(pyVmomi.vim.profile.Profile):
   class ConfigInfo(pyVmomi.vim.profile.Profile.ConfigInfo):
      applyProfile: _typing.Optional[HostApplyProfile] = None
      defaultComplyProfile: _typing.Optional[pyVmomi.vim.profile.ComplianceProfile] = None
      defaultComplyLocator: list[pyVmomi.vim.profile.ComplianceLocator] = []
      customComplyProfile: _typing.Optional[pyVmomi.vim.profile.ComplianceProfile] = None
      disabledExpressionList: list[str] = []
      description: _typing.Optional[pyVmomi.vim.profile.Profile.Description] = None

   class ConfigSpec(pyVmomi.vim.profile.Profile.CreateSpec):
      pass

   class SerializedHostProfileSpec(pyVmomi.vim.profile.Profile.SerializedCreateSpec):
      validatorHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
      validating: _typing.Optional[bool] = None

   class CompleteConfigSpec(ConfigSpec):
      applyProfile: _typing.Optional[HostApplyProfile] = None
      customComplyProfile: _typing.Optional[pyVmomi.vim.profile.ComplianceProfile] = None
      disabledExpressionListChanged: bool
      disabledExpressionList: list[str] = []
      validatorHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
      validating: _typing.Optional[bool] = None
      hostConfig: _typing.Optional[ConfigInfo] = None

   class HostBasedConfigSpec(ConfigSpec):
      host: pyVmomi.vim.HostSystem
      useHostProfileEngine: _typing.Optional[bool] = None

   class ValidationState(pyVmomi.VmomiSupport.Enum):
      Ready: _typing.ClassVar['ValidationState'] = 'Ready'
      Running: _typing.ClassVar['ValidationState'] = 'Running'
      Failed: _typing.ClassVar['ValidationState'] = 'Failed'

   class ValidationFailureInfo(pyVmomi.vmodl.DynamicData):
      class UpdateType(pyVmomi.VmomiSupport.Enum):
         HostBased: _typing.ClassVar['UpdateType'] = 'HostBased'
         Import: _typing.ClassVar['UpdateType'] = 'Import'
         Edit: _typing.ClassVar['UpdateType'] = 'Edit'
         Compose: _typing.ClassVar['UpdateType'] = 'Compose'

      name: str
      annotation: str
      updateType: str
      host: _typing.Optional[pyVmomi.vim.HostSystem] = None
      applyProfile: _typing.Optional[HostApplyProfile] = None
      failures: list[pyVmomi.vim.fault.ProfileUpdateFailed.UpdateFailure] = []
      faults: list[pyVmomi.vmodl.MethodFault] = []

   @property
   def validationState(self) -> _typing.Optional[str]: ...
   @property
   def validationStateUpdateTime(self) -> _typing.Optional[_datetime.datetime]: ...
   @property
   def validationFailureInfo(self) -> _typing.Optional[ValidationFailureInfo]: ...
   @property
   def complianceCheckTime(self) -> _typing.Optional[_datetime.datetime]: ...
   @property
   def referenceHost(self) -> _typing.Optional[pyVmomi.vim.HostSystem]: ...

   def ResetValidationState(self) -> None: ...
   def UpdateReferenceHost(self, host: _typing.Optional[pyVmomi.vim.HostSystem]) -> None: ...
   def Update(self, config: ConfigSpec) -> None: ...
   def Execute(self, host: pyVmomi.vim.HostSystem, deferredParam: list[pyVmomi.vim.profile.DeferredPolicyOptionParameter]) -> ExecuteResult: ...


class HostSpecification(pyVmomi.vmodl.DynamicData):
   createdTime: _datetime.datetime
   lastModified: _typing.Optional[_datetime.datetime] = None
   host: pyVmomi.vim.HostSystem
   subSpecs: list[HostSubSpecification] = []
   changeID: _typing.Optional[str] = None


class HostSpecificationManager(pyVmomi.VmomiSupport.ManagedObject):
   def UpdateHostSpecification(self, host: pyVmomi.vim.HostSystem, hostSpec: HostSpecification) -> None: ...
   def UpdateHostSubSpecification(self, host: pyVmomi.vim.HostSystem, hostSubSpec: HostSubSpecification) -> None: ...
   def RetrieveHostSpecification(self, host: pyVmomi.vim.HostSystem, fromHost: bool) -> HostSpecification: ...
   def DeleteHostSubSpecification(self, host: pyVmomi.vim.HostSystem, subSpecName: str) -> None: ...
   def DeleteHostSpecification(self, host: pyVmomi.vim.HostSystem) -> None: ...
   def GetUpdatedHosts(self, startChangeID: _typing.Optional[str], endChangeID: _typing.Optional[str]) -> list[pyVmomi.vim.HostSystem]: ...


class HostSubSpecification(pyVmomi.vmodl.DynamicData):
   name: str
   createdTime: _datetime.datetime
   data: list[pyVmomi.VmomiSupport.byte] = []
   binaryData: _typing.Optional[pyVmomi.VmomiSupport.binary] = None


class IpAddressProfile(pyVmomi.vim.profile.ApplyProfile):
   pass


class IpRouteProfile(pyVmomi.vim.profile.ApplyProfile):
   staticRoute: list[StaticRouteProfile] = []


class NasStorageProfile(pyVmomi.vim.profile.ApplyProfile):
   key: str


class NetStackInstanceProfile(pyVmomi.vim.profile.ApplyProfile):
   key: str
   dnsConfig: NetworkProfile.DnsConfigProfile
   ipRouteConfig: IpRouteProfile


class NetworkPolicyProfile(pyVmomi.vim.profile.ApplyProfile):
   pass


class NetworkProfile(pyVmomi.vim.profile.ApplyProfile):
   class DnsConfigProfile(pyVmomi.vim.profile.ApplyProfile):
      pass

   vswitch: list[VirtualSwitchProfile] = []
   vmPortGroup: list[VmPortGroupProfile] = []
   hostPortGroup: list[HostPortGroupProfile] = []
   serviceConsolePortGroup: list[ServiceConsolePortGroupProfile] = []
   dnsConfig: _typing.Optional[DnsConfigProfile] = None
   ipRouteConfig: _typing.Optional[IpRouteProfile] = None
   consoleIpRouteConfig: _typing.Optional[IpRouteProfile] = None
   pnic: list[PhysicalNicProfile] = []
   dvswitch: list[DvsProfile] = []
   dvsServiceConsoleNic: list[DvsServiceConsoleVNicProfile] = []
   dvsHostNic: list[DvsHostVNicProfile] = []
   nsxHostNic: list[NsxHostVNicProfile] = []
   netStackInstance: list[NetStackInstanceProfile] = []
   opaqueSwitch: _typing.Optional[OpaqueSwitchProfile] = None


class NsxHostVNicProfile(pyVmomi.vim.profile.ApplyProfile):
   key: str
   ipConfig: IpAddressProfile


class OpaqueSwitchProfile(pyVmomi.vim.profile.ApplyProfile):
   pass


class OptionProfile(pyVmomi.vim.profile.ApplyProfile):
   key: str


class PermissionProfile(pyVmomi.vim.profile.ApplyProfile):
   key: str


class PhysicalNicProfile(pyVmomi.vim.profile.ApplyProfile):
   key: str


class PnicUplinkProfile(pyVmomi.vim.profile.ApplyProfile):
   key: str


class PortGroupProfile(pyVmomi.vim.profile.ApplyProfile):
   class VlanProfile(pyVmomi.vim.profile.ApplyProfile):
      pass

   class VirtualSwitchSelectionProfile(pyVmomi.vim.profile.ApplyProfile):
      pass

   key: str
   name: str
   vlan: VlanProfile
   vswitch: VirtualSwitchSelectionProfile
   networkPolicy: NetworkPolicyProfile


class ProfileManager(pyVmomi.vim.profile.ProfileManager):
   class TaskListRequirement(pyVmomi.VmomiSupport.Enum):
      maintenanceModeRequired: _typing.ClassVar['TaskListRequirement'] = 'maintenanceModeRequired'
      rebootRequired: _typing.ClassVar['TaskListRequirement'] = 'rebootRequired'

   class ConfigTaskList(pyVmomi.vmodl.DynamicData):
      configSpec: _typing.Optional[pyVmomi.vim.host.ConfigSpec] = None
      taskDescription: list[pyVmomi.vmodl.LocalizableMessage] = []
      taskListRequirement: list[str] = []

   class AnswerFileCreateSpec(pyVmomi.vmodl.DynamicData):
      validating: _typing.Optional[bool] = None

   class AnswerFileOptionsCreateSpec(AnswerFileCreateSpec):
      userInput: list[pyVmomi.vim.profile.DeferredPolicyOptionParameter] = []

   class AnswerFileSerializedCreateSpec(AnswerFileCreateSpec):
      answerFileConfigString: str

   class AnswerFileStatus(pyVmomi.VmomiSupport.Enum):
      valid: _typing.ClassVar['AnswerFileStatus'] = 'valid'
      invalid: _typing.ClassVar['AnswerFileStatus'] = 'invalid'
      unknown: _typing.ClassVar['AnswerFileStatus'] = 'unknown'

   class EntityCustomizations(pyVmomi.vmodl.DynamicData):
      pass

   class StructuredCustomizations(EntityCustomizations):
      entity: pyVmomi.vim.ManagedEntity
      customizations: _typing.Optional[AnswerFile] = None

   class HostToConfigSpecMap(pyVmomi.vmodl.DynamicData):
      host: pyVmomi.vim.HostSystem
      configSpec: AnswerFileCreateSpec

   class ApplyHostConfigSpec(ExecuteResult):
      host: pyVmomi.vim.HostSystem
      taskListRequirement: list[str] = []
      taskDescription: list[pyVmomi.vmodl.LocalizableMessage] = []
      rebootStateless: _typing.Optional[bool] = None
      rebootHost: _typing.Optional[bool] = None
      faultData: _typing.Optional[pyVmomi.vmodl.MethodFault] = None

   class ApplyHostConfigResult(pyVmomi.vmodl.DynamicData):
      class Status(pyVmomi.VmomiSupport.Enum):
         success: _typing.ClassVar['Status'] = 'success'
         failed: _typing.ClassVar['Status'] = 'failed'
         reboot_failed: _typing.ClassVar['Status'] = 'reboot_failed'
         stateless_reboot_failed: _typing.ClassVar['Status'] = 'stateless_reboot_failed'
         check_compliance_failed: _typing.ClassVar['Status'] = 'check_compliance_failed'
         state_not_satisfied: _typing.ClassVar['Status'] = 'state_not_satisfied'
         exit_maintenancemode_failed: _typing.ClassVar['Status'] = 'exit_maintenancemode_failed'
         canceled: _typing.ClassVar['Status'] = 'canceled'

      startTime: _datetime.datetime
      completeTime: _datetime.datetime
      host: pyVmomi.vim.HostSystem
      status: str
      errors: list[pyVmomi.vmodl.MethodFault] = []

   class CompositionValidationResult(pyVmomi.vmodl.DynamicData):
      class ResultElement(pyVmomi.vmodl.DynamicData):
         class Status(pyVmomi.VmomiSupport.Enum):
            success: _typing.ClassVar['Status'] = 'success'
            error: _typing.ClassVar['Status'] = 'error'

         target: pyVmomi.vim.profile.Profile
         status: str
         errors: list[pyVmomi.vmodl.LocalizableMessage] = []
         sourceDiffForToBeMerged: _typing.Optional[HostApplyProfile] = None
         targetDiffForToBeMerged: _typing.Optional[HostApplyProfile] = None
         toBeAdded: _typing.Optional[HostApplyProfile] = None
         toBeDeleted: _typing.Optional[HostApplyProfile] = None
         toBeDisabled: _typing.Optional[HostApplyProfile] = None
         toBeEnabled: _typing.Optional[HostApplyProfile] = None
         toBeReenableCC: _typing.Optional[HostApplyProfile] = None

      results: list[ResultElement] = []
      errors: list[pyVmomi.vmodl.LocalizableMessage] = []

   class CompositionResult(pyVmomi.vmodl.DynamicData):
      class ResultElement(pyVmomi.vmodl.DynamicData):
         class Status(pyVmomi.VmomiSupport.Enum):
            success: _typing.ClassVar['Status'] = 'success'
            error: _typing.ClassVar['Status'] = 'error'

         target: pyVmomi.vim.profile.Profile
         status: str
         errors: list[pyVmomi.vmodl.LocalizableMessage] = []

      errors: list[pyVmomi.vmodl.LocalizableMessage] = []
      results: list[ResultElement] = []

   def ApplyHostConfiguration(self, host: pyVmomi.vim.HostSystem, configSpec: pyVmomi.vim.host.ConfigSpec, userInput: list[pyVmomi.vim.profile.DeferredPolicyOptionParameter]) -> pyVmomi.vim.Task: ...
   def GenerateConfigTaskList(self, configSpec: pyVmomi.vim.host.ConfigSpec, host: pyVmomi.vim.HostSystem) -> ConfigTaskList: ...
   def GenerateTaskList(self, configSpec: pyVmomi.vim.host.ConfigSpec, host: pyVmomi.vim.HostSystem) -> pyVmomi.vim.Task: ...
   def QueryProfileMetadata(self, profileName: list[type], profile: _typing.Optional[pyVmomi.vim.profile.Profile]) -> list[pyVmomi.vim.profile.ProfileMetadata]: ...
   def QueryProfileStructure(self, profile: _typing.Optional[pyVmomi.vim.profile.Profile]) -> pyVmomi.vim.profile.ProfileStructure: ...
   def CreateDefaultProfile(self, profileType: type, profileTypeName: _typing.Optional[str], profile: _typing.Optional[pyVmomi.vim.profile.Profile]) -> pyVmomi.vim.profile.ApplyProfile: ...
   def UpdateAnswerFile(self, host: pyVmomi.vim.HostSystem, configSpec: AnswerFileCreateSpec) -> pyVmomi.vim.Task: ...
   def RetrieveAnswerFile(self, host: pyVmomi.vim.HostSystem) -> _typing.Optional[AnswerFile]: ...
   def RetrieveAnswerFileForProfile(self, host: pyVmomi.vim.HostSystem, applyProfile: HostApplyProfile) -> _typing.Optional[AnswerFile]: ...
   def ExportAnswerFile(self, host: pyVmomi.vim.HostSystem) -> pyVmomi.vim.Task: ...
   def CheckAnswerFileStatus(self, host: list[pyVmomi.vim.HostSystem]) -> pyVmomi.vim.Task: ...
   def QueryAnswerFileStatus(self, host: list[pyVmomi.vim.HostSystem]) -> list[AnswerFileStatusResult]: ...
   def RetrieveHostCustomizations(self, hosts: list[pyVmomi.vim.HostSystem]) -> list[StructuredCustomizations]: ...
   def RetrieveHostCustomizationsForProfile(self, hosts: list[pyVmomi.vim.HostSystem], applyProfile: HostApplyProfile) -> list[StructuredCustomizations]: ...
   def GenerateHostConfigTaskSpec(self, hostsInfo: list[StructuredCustomizations]) -> pyVmomi.vim.Task: ...
   def ApplyEntitiesConfiguration(self, applyConfigSpecs: list[ApplyHostConfigSpec]) -> pyVmomi.vim.Task: ...
   def ValidateComposition(self, source: pyVmomi.vim.profile.Profile, targets: list[pyVmomi.vim.profile.Profile], toBeMerged: _typing.Optional[HostApplyProfile], toReplaceWith: _typing.Optional[HostApplyProfile], toBeDeleted: _typing.Optional[HostApplyProfile], enableStatusToBeCopied: _typing.Optional[HostApplyProfile], errorOnly: _typing.Optional[bool]) -> pyVmomi.vim.Task: ...
   def CompositeProfile(self, source: pyVmomi.vim.profile.Profile, targets: list[pyVmomi.vim.profile.Profile], toBeMerged: _typing.Optional[HostApplyProfile], toBeReplacedWith: _typing.Optional[HostApplyProfile], toBeDeleted: _typing.Optional[HostApplyProfile], enableStatusToBeCopied: _typing.Optional[HostApplyProfile]) -> pyVmomi.vim.Task: ...


class SecurityProfile(pyVmomi.vim.profile.ApplyProfile):
   permission: list[PermissionProfile] = []

class ServiceConsolePortGroupProfile(PortGroupProfile):
   ipConfig: IpAddressProfile


class ServiceProfile(pyVmomi.vim.profile.ApplyProfile):
   key: str


class StaticRouteProfile(pyVmomi.vim.profile.ApplyProfile):
   key: _typing.Optional[str] = None


class StorageProfile(pyVmomi.vim.profile.ApplyProfile):
   nasStorage: list[NasStorageProfile] = []


class UserGroupProfile(pyVmomi.vim.profile.ApplyProfile):
   key: str


class UserProfile(pyVmomi.vim.profile.ApplyProfile):
   key: str


class VirtualSwitchProfile(pyVmomi.vim.profile.ApplyProfile):
   class LinkProfile(pyVmomi.vim.profile.ApplyProfile):
      pass

   class NumPortsProfile(pyVmomi.vim.profile.ApplyProfile):
      pass

   key: str
   name: str
   link: LinkProfile
   numPorts: NumPortsProfile
   networkPolicy: NetworkPolicyProfile

class VmPortGroupProfile(PortGroupProfile):
   pass
