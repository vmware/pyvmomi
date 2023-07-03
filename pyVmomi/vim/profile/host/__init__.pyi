from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType, PropertyPath, binary, byte
from . import profileEngine as profileEngine


class HostProfile(vim.profile.Profile):
    @property
    def validationState(self) -> str: ...
    @property
    def validationStateUpdateTime(self) -> datetime: ...
    @property
    def validationFailureInfo(self) -> HostProfile.ValidationFailureInfo: ...
    @property
    def complianceCheckTime(self) -> datetime: ...
    @property
    def referenceHost(self) -> vim.HostSystem: ...
    def ResetValidationState(self) -> NoneType: ...
    def UpdateReferenceHost(self, host: vim.HostSystem) -> NoneType: ...
    def Update(self, config: HostProfile.ConfigSpec) -> NoneType: ...
    def Execute(self, host: vim.HostSystem, deferredParam: List[vim.profile.DeferredPolicyOptionParameter]) -> ExecuteResult: ...


    class CompleteConfigSpec(HostProfile.ConfigSpec):
        @property
        def applyProfile(self) -> HostApplyProfile: ...
        @applyProfile.setter
        def applyProfile(self, value: HostApplyProfile):
            self._applyProfile = value
        @property
        def customComplyProfile(self) -> vim.profile.ComplianceProfile: ...
        @customComplyProfile.setter
        def customComplyProfile(self, value: vim.profile.ComplianceProfile):
            self._customComplyProfile = value
        @property
        def disabledExpressionListChanged(self) -> bool: ...
        @disabledExpressionListChanged.setter
        def disabledExpressionListChanged(self, value: bool):
            self._disabledExpressionListChanged = value
        @property
        def disabledExpressionList(self) -> List[str]: ...
        @disabledExpressionList.setter
        def disabledExpressionList(self, value: List[str]):
            self._disabledExpressionList = value
        @property
        def validatorHost(self) -> vim.HostSystem: ...
        @validatorHost.setter
        def validatorHost(self, value: vim.HostSystem):
            self._validatorHost = value
        @property
        def validating(self) -> bool: ...
        @validating.setter
        def validating(self, value: bool):
            self._validating = value
        @property
        def hostConfig(self) -> HostProfile.ConfigInfo: ...
        @hostConfig.setter
        def hostConfig(self, value: HostProfile.ConfigInfo):
            self._hostConfig = value


    class ConfigInfo(vim.profile.Profile.ConfigInfo):
        @property
        def applyProfile(self) -> HostApplyProfile: ...
        @applyProfile.setter
        def applyProfile(self, value: HostApplyProfile):
            self._applyProfile = value
        @property
        def defaultComplyProfile(self) -> vim.profile.ComplianceProfile: ...
        @defaultComplyProfile.setter
        def defaultComplyProfile(self, value: vim.profile.ComplianceProfile):
            self._defaultComplyProfile = value
        @property
        def defaultComplyLocator(self) -> List[vim.profile.ComplianceLocator]: ...
        @defaultComplyLocator.setter
        def defaultComplyLocator(self, value: List[vim.profile.ComplianceLocator]):
            self._defaultComplyLocator = value
        @property
        def customComplyProfile(self) -> vim.profile.ComplianceProfile: ...
        @customComplyProfile.setter
        def customComplyProfile(self, value: vim.profile.ComplianceProfile):
            self._customComplyProfile = value
        @property
        def disabledExpressionList(self) -> List[str]: ...
        @disabledExpressionList.setter
        def disabledExpressionList(self, value: List[str]):
            self._disabledExpressionList = value
        @property
        def description(self) -> vim.profile.Profile.Description: ...
        @description.setter
        def description(self, value: vim.profile.Profile.Description):
            self._description = value


    class ConfigSpec(vim.profile.Profile.CreateSpec): ...


    class HostBasedConfigSpec(HostProfile.ConfigSpec):
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def useHostProfileEngine(self) -> bool: ...
        @useHostProfileEngine.setter
        def useHostProfileEngine(self, value: bool):
            self._useHostProfileEngine = value


    class SerializedHostProfileSpec(vim.profile.Profile.SerializedCreateSpec):
        @property
        def validatorHost(self) -> vim.HostSystem: ...
        @validatorHost.setter
        def validatorHost(self, value: vim.HostSystem):
            self._validatorHost = value
        @property
        def validating(self) -> bool: ...
        @validating.setter
        def validating(self, value: bool):
            self._validating = value


    class ValidationFailureInfo(vmodl.DynamicData):
        @property
        def name(self) -> str: ...
        @name.setter
        def name(self, value: str):
            self._name = value
        @property
        def annotation(self) -> str: ...
        @annotation.setter
        def annotation(self, value: str):
            self._annotation = value
        @property
        def updateType(self) -> str: ...
        @updateType.setter
        def updateType(self, value: str):
            self._updateType = value
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def applyProfile(self) -> HostApplyProfile: ...
        @applyProfile.setter
        def applyProfile(self, value: HostApplyProfile):
            self._applyProfile = value
        @property
        def failures(self) -> List[vim.fault.ProfileUpdateFailed.UpdateFailure]: ...
        @failures.setter
        def failures(self, value: List[vim.fault.ProfileUpdateFailed.UpdateFailure]):
            self._failures = value
        @property
        def faults(self) -> List[vmodl.MethodFault]: ...
        @faults.setter
        def faults(self, value: List[vmodl.MethodFault]):
            self._faults = value


        class UpdateType(Enum):
            HostBased = "HostBased"
            Import = "Import"
            Edit = "Edit"
            Compose = "Compose"


    class ValidationState(Enum):
        Ready = "Ready"
        Running = "Running"
        Failed = "Failed"


class HostSpecificationManager(ManagedObject):
    def UpdateHostSpecification(self, host: vim.HostSystem, hostSpec: HostSpecification) -> NoneType: ...
    def UpdateHostSubSpecification(self, host: vim.HostSystem, hostSubSpec: HostSubSpecification) -> NoneType: ...
    def RetrieveHostSpecification(self, host: vim.HostSystem, fromHost: bool) -> HostSpecification: ...
    def DeleteHostSubSpecification(self, host: vim.HostSystem, subSpecName: str) -> NoneType: ...
    def DeleteHostSpecification(self, host: vim.HostSystem) -> NoneType: ...
    def GetUpdatedHosts(self, startChangeID: str, endChangeID: str) -> List[vim.HostSystem]: ...


class ProfileManager(vim.profile.ProfileManager):
    def ApplyHostConfiguration(self, host: vim.HostSystem, configSpec: vim.host.ConfigSpec, userInput: List[vim.profile.DeferredPolicyOptionParameter]) -> vim.Task: ...
    def GenerateConfigTaskList(self, configSpec: vim.host.ConfigSpec, host: vim.HostSystem) -> ProfileManager.ConfigTaskList: ...
    def GenerateTaskList(self, configSpec: vim.host.ConfigSpec, host: vim.HostSystem) -> vim.Task: ...
    def QueryProfileMetadata(self, profileName: List[type], profile: vim.profile.Profile) -> List[vim.profile.ProfileMetadata]: ...
    def QueryProfileStructure(self, profile: vim.profile.Profile) -> vim.profile.ProfileStructure: ...
    def CreateDefaultProfile(self, profileType: type, profileTypeName: str, profile: vim.profile.Profile) -> vim.profile.ApplyProfile: ...
    def UpdateAnswerFile(self, host: vim.HostSystem, configSpec: ProfileManager.AnswerFileCreateSpec) -> vim.Task: ...
    def RetrieveAnswerFile(self, host: vim.HostSystem) -> AnswerFile: ...
    def RetrieveAnswerFileForProfile(self, host: vim.HostSystem, applyProfile: HostApplyProfile) -> AnswerFile: ...
    def ExportAnswerFile(self, host: vim.HostSystem) -> vim.Task: ...
    def CheckAnswerFileStatus(self, host: List[vim.HostSystem]) -> vim.Task: ...
    def QueryAnswerFileStatus(self, host: List[vim.HostSystem]) -> List[AnswerFileStatusResult]: ...
    def UpdateHostCustomizations(self, hostToConfigSpecMap: List[ProfileManager.HostToConfigSpecMap]) -> vim.Task: ...
    def RetrieveHostCustomizations(self, hosts: List[vim.HostSystem]) -> List[ProfileManager.StructuredCustomizations]: ...
    def RetrieveHostCustomizationsForProfile(self, hosts: List[vim.HostSystem], applyProfile: HostApplyProfile) -> List[ProfileManager.StructuredCustomizations]: ...
    def GenerateHostConfigTaskSpec(self, hostsInfo: List[ProfileManager.StructuredCustomizations]) -> vim.Task: ...
    def ApplyEntitiesConfiguration(self, applyConfigSpecs: List[ProfileManager.ApplyHostConfigSpec]) -> vim.Task: ...
    def ValidateComposition(self, source: vim.profile.Profile, targets: List[vim.profile.Profile], toBeMerged: HostApplyProfile, toReplaceWith: HostApplyProfile, toBeDeleted: HostApplyProfile, enableStatusToBeCopied: HostApplyProfile, errorOnly: bool) -> vim.Task: ...
    def CompositeProfile(self, source: vim.profile.Profile, targets: List[vim.profile.Profile], toBeMerged: HostApplyProfile, toBeReplacedWith: HostApplyProfile, toBeDeleted: HostApplyProfile, enableStatusToBeCopied: HostApplyProfile) -> vim.Task: ...


    class AnswerFileCreateSpec(vmodl.DynamicData):
        @property
        def validating(self) -> bool: ...
        @validating.setter
        def validating(self, value: bool):
            self._validating = value


    class AnswerFileOptionsCreateSpec(ProfileManager.AnswerFileCreateSpec):
        @property
        def userInput(self) -> List[vim.profile.DeferredPolicyOptionParameter]: ...
        @userInput.setter
        def userInput(self, value: List[vim.profile.DeferredPolicyOptionParameter]):
            self._userInput = value


    class AnswerFileSerializedCreateSpec(ProfileManager.AnswerFileCreateSpec):
        @property
        def answerFileConfigString(self) -> str: ...
        @answerFileConfigString.setter
        def answerFileConfigString(self, value: str):
            self._answerFileConfigString = value


    class ApplyHostConfigResult(vmodl.DynamicData):
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
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def status(self) -> str: ...
        @status.setter
        def status(self, value: str):
            self._status = value
        @property
        def errors(self) -> List[vmodl.MethodFault]: ...
        @errors.setter
        def errors(self, value: List[vmodl.MethodFault]):
            self._errors = value


    class ApplyHostConfigSpec(ExecuteResult):
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def taskListRequirement(self) -> List[str]: ...
        @taskListRequirement.setter
        def taskListRequirement(self, value: List[str]):
            self._taskListRequirement = value
        @property
        def taskDescription(self) -> List[vmodl.LocalizableMessage]: ...
        @taskDescription.setter
        def taskDescription(self, value: List[vmodl.LocalizableMessage]):
            self._taskDescription = value
        @property
        def rebootStateless(self) -> bool: ...
        @rebootStateless.setter
        def rebootStateless(self, value: bool):
            self._rebootStateless = value
        @property
        def rebootHost(self) -> bool: ...
        @rebootHost.setter
        def rebootHost(self, value: bool):
            self._rebootHost = value
        @property
        def faultData(self) -> vmodl.MethodFault: ...
        @faultData.setter
        def faultData(self, value: vmodl.MethodFault):
            self._faultData = value


    class CompositionResult(vmodl.DynamicData):
        @property
        def errors(self) -> List[vmodl.LocalizableMessage]: ...
        @errors.setter
        def errors(self, value: List[vmodl.LocalizableMessage]):
            self._errors = value
        @property
        def results(self) -> List[ProfileManager.CompositionResult.ResultElement]: ...
        @results.setter
        def results(self, value: List[ProfileManager.CompositionResult.ResultElement]):
            self._results = value


        class ResultElement(vmodl.DynamicData):
            @property
            def target(self) -> vim.profile.Profile: ...
            @target.setter
            def target(self, value: vim.profile.Profile):
                self._target = value
            @property
            def status(self) -> str: ...
            @status.setter
            def status(self, value: str):
                self._status = value
            @property
            def errors(self) -> List[vmodl.LocalizableMessage]: ...
            @errors.setter
            def errors(self, value: List[vmodl.LocalizableMessage]):
                self._errors = value


    class CompositionValidationResult(vmodl.DynamicData):
        @property
        def results(self) -> List[ProfileManager.CompositionValidationResult.ResultElement]: ...
        @results.setter
        def results(self, value: List[ProfileManager.CompositionValidationResult.ResultElement]):
            self._results = value
        @property
        def errors(self) -> List[vmodl.LocalizableMessage]: ...
        @errors.setter
        def errors(self, value: List[vmodl.LocalizableMessage]):
            self._errors = value


        class ResultElement(vmodl.DynamicData):
            @property
            def target(self) -> vim.profile.Profile: ...
            @target.setter
            def target(self, value: vim.profile.Profile):
                self._target = value
            @property
            def status(self) -> str: ...
            @status.setter
            def status(self, value: str):
                self._status = value
            @property
            def errors(self) -> List[vmodl.LocalizableMessage]: ...
            @errors.setter
            def errors(self, value: List[vmodl.LocalizableMessage]):
                self._errors = value
            @property
            def sourceDiffForToBeMerged(self) -> HostApplyProfile: ...
            @sourceDiffForToBeMerged.setter
            def sourceDiffForToBeMerged(self, value: HostApplyProfile):
                self._sourceDiffForToBeMerged = value
            @property
            def targetDiffForToBeMerged(self) -> HostApplyProfile: ...
            @targetDiffForToBeMerged.setter
            def targetDiffForToBeMerged(self, value: HostApplyProfile):
                self._targetDiffForToBeMerged = value
            @property
            def toBeAdded(self) -> HostApplyProfile: ...
            @toBeAdded.setter
            def toBeAdded(self, value: HostApplyProfile):
                self._toBeAdded = value
            @property
            def toBeDeleted(self) -> HostApplyProfile: ...
            @toBeDeleted.setter
            def toBeDeleted(self, value: HostApplyProfile):
                self._toBeDeleted = value
            @property
            def toBeDisabled(self) -> HostApplyProfile: ...
            @toBeDisabled.setter
            def toBeDisabled(self, value: HostApplyProfile):
                self._toBeDisabled = value
            @property
            def toBeEnabled(self) -> HostApplyProfile: ...
            @toBeEnabled.setter
            def toBeEnabled(self, value: HostApplyProfile):
                self._toBeEnabled = value
            @property
            def toBeReenableCC(self) -> HostApplyProfile: ...
            @toBeReenableCC.setter
            def toBeReenableCC(self, value: HostApplyProfile):
                self._toBeReenableCC = value


    class ConfigTaskList(vmodl.DynamicData):
        @property
        def configSpec(self) -> vim.host.ConfigSpec: ...
        @configSpec.setter
        def configSpec(self, value: vim.host.ConfigSpec):
            self._configSpec = value
        @property
        def taskDescription(self) -> List[vmodl.LocalizableMessage]: ...
        @taskDescription.setter
        def taskDescription(self, value: List[vmodl.LocalizableMessage]):
            self._taskDescription = value
        @property
        def taskListRequirement(self) -> List[str]: ...
        @taskListRequirement.setter
        def taskListRequirement(self, value: List[str]):
            self._taskListRequirement = value


    class EntityCustomizations(vmodl.DynamicData): ...


    class HostToConfigSpecMap(vmodl.DynamicData):
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def configSpec(self) -> ProfileManager.AnswerFileCreateSpec: ...
        @configSpec.setter
        def configSpec(self, value: ProfileManager.AnswerFileCreateSpec):
            self._configSpec = value


    class StructuredCustomizations(ProfileManager.EntityCustomizations):
        @property
        def entity(self) -> vim.ManagedEntity: ...
        @entity.setter
        def entity(self, value: vim.ManagedEntity):
            self._entity = value
        @property
        def customizations(self) -> AnswerFile: ...
        @customizations.setter
        def customizations(self, value: AnswerFile):
            self._customizations = value


    class AnswerFileStatus(Enum):
        valid = "valid"
        invalid = "invalid"
        unknown = "unknown"


    class TaskListRequirement(Enum):
        maintenanceModeRequired = "maintenanceModeRequired"
        rebootRequired = "rebootRequired"


class ActiveDirectoryProfile(vim.profile.ApplyProfile): ...


class AnswerFile(vmodl.DynamicData):
    @property
    def userInput(self) -> List[vim.profile.DeferredPolicyOptionParameter]: ...
    @userInput.setter
    def userInput(self, value: List[vim.profile.DeferredPolicyOptionParameter]):
        self._userInput = value
    @property
    def createdTime(self) -> datetime: ...
    @createdTime.setter
    def createdTime(self, value: datetime):
        self._createdTime = value
    @property
    def modifiedTime(self) -> datetime: ...
    @modifiedTime.setter
    def modifiedTime(self, value: datetime):
        self._modifiedTime = value


class AnswerFileStatusResult(vmodl.DynamicData):
    @property
    def checkedTime(self) -> datetime: ...
    @checkedTime.setter
    def checkedTime(self, value: datetime):
        self._checkedTime = value
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def status(self) -> str: ...
    @status.setter
    def status(self, value: str):
        self._status = value
    @property
    def error(self) -> List[AnswerFileStatusResult.AnswerFileStatusError]: ...
    @error.setter
    def error(self, value: List[AnswerFileStatusResult.AnswerFileStatusError]):
        self._error = value


    class AnswerFileStatusError(vmodl.DynamicData):
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


class AuthenticationProfile(vim.profile.ApplyProfile):
    @property
    def activeDirectory(self) -> ActiveDirectoryProfile: ...
    @activeDirectory.setter
    def activeDirectory(self, value: ActiveDirectoryProfile):
        self._activeDirectory = value


class DateTimeProfile(vim.profile.ApplyProfile): ...


class DvsHostVNicProfile(DvsVNicProfile): ...


class DvsProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def uplink(self) -> List[PnicUplinkProfile]: ...
    @uplink.setter
    def uplink(self, value: List[PnicUplinkProfile]):
        self._uplink = value


class DvsServiceConsoleVNicProfile(DvsVNicProfile): ...


class DvsVNicProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def ipConfig(self) -> IpAddressProfile: ...
    @ipConfig.setter
    def ipConfig(self, value: IpAddressProfile):
        self._ipConfig = value


class ExecuteResult(vmodl.DynamicData):
    @property
    def status(self) -> str: ...
    @status.setter
    def status(self, value: str):
        self._status = value
    @property
    def configSpec(self) -> vim.host.ConfigSpec: ...
    @configSpec.setter
    def configSpec(self, value: vim.host.ConfigSpec):
        self._configSpec = value
    @property
    def inapplicablePath(self) -> List[PropertyPath]: ...
    @inapplicablePath.setter
    def inapplicablePath(self, value: List[PropertyPath]):
        self._inapplicablePath = value
    @property
    def requireInput(self) -> List[vim.profile.DeferredPolicyOptionParameter]: ...
    @requireInput.setter
    def requireInput(self, value: List[vim.profile.DeferredPolicyOptionParameter]):
        self._requireInput = value
    @property
    def error(self) -> List[ExecuteResult.ExecuteError]: ...
    @error.setter
    def error(self, value: List[ExecuteResult.ExecuteError]):
        self._error = value


    class ExecuteError(vmodl.DynamicData):
        @property
        def path(self) -> vim.profile.ProfilePropertyPath: ...
        @path.setter
        def path(self, value: vim.profile.ProfilePropertyPath):
            self._path = value
        @property
        def message(self) -> vmodl.LocalizableMessage: ...
        @message.setter
        def message(self, value: vmodl.LocalizableMessage):
            self._message = value


    class Status(Enum):
        success = "success"
        needInput = "needInput"
        error = "error"


class FirewallProfile(vim.profile.ApplyProfile):
    @property
    def ruleset(self) -> List[FirewallProfile.RulesetProfile]: ...
    @ruleset.setter
    def ruleset(self, value: List[FirewallProfile.RulesetProfile]):
        self._ruleset = value


    class RulesetProfile(vim.profile.ApplyProfile):
        @property
        def key(self) -> str: ...
        @key.setter
        def key(self, value: str):
            self._key = value


class HostApplyProfile(vim.profile.ApplyProfile):
    @property
    def memory(self) -> HostMemoryProfile: ...
    @memory.setter
    def memory(self, value: HostMemoryProfile):
        self._memory = value
    @property
    def storage(self) -> StorageProfile: ...
    @storage.setter
    def storage(self, value: StorageProfile):
        self._storage = value
    @property
    def network(self) -> NetworkProfile: ...
    @network.setter
    def network(self, value: NetworkProfile):
        self._network = value
    @property
    def datetime(self) -> DateTimeProfile: ...
    @datetime.setter
    def datetime(self, value: DateTimeProfile):
        self._datetime = value
    @property
    def firewall(self) -> FirewallProfile: ...
    @firewall.setter
    def firewall(self, value: FirewallProfile):
        self._firewall = value
    @property
    def security(self) -> SecurityProfile: ...
    @security.setter
    def security(self, value: SecurityProfile):
        self._security = value
    @property
    def service(self) -> List[ServiceProfile]: ...
    @service.setter
    def service(self, value: List[ServiceProfile]):
        self._service = value
    @property
    def option(self) -> List[OptionProfile]: ...
    @option.setter
    def option(self, value: List[OptionProfile]):
        self._option = value
    @property
    def userAccount(self) -> List[UserProfile]: ...
    @userAccount.setter
    def userAccount(self, value: List[UserProfile]):
        self._userAccount = value
    @property
    def usergroupAccount(self) -> List[UserGroupProfile]: ...
    @usergroupAccount.setter
    def usergroupAccount(self, value: List[UserGroupProfile]):
        self._usergroupAccount = value
    @property
    def authentication(self) -> AuthenticationProfile: ...
    @authentication.setter
    def authentication(self, value: AuthenticationProfile):
        self._authentication = value


class HostMemoryProfile(vim.profile.ApplyProfile): ...


class HostPortGroupProfile(PortGroupProfile):
    @property
    def ipConfig(self) -> IpAddressProfile: ...
    @ipConfig.setter
    def ipConfig(self, value: IpAddressProfile):
        self._ipConfig = value


class HostSpecification(vmodl.DynamicData):
    @property
    def createdTime(self) -> datetime: ...
    @createdTime.setter
    def createdTime(self, value: datetime):
        self._createdTime = value
    @property
    def lastModified(self) -> datetime: ...
    @lastModified.setter
    def lastModified(self, value: datetime):
        self._lastModified = value
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value
    @property
    def subSpecs(self) -> List[HostSubSpecification]: ...
    @subSpecs.setter
    def subSpecs(self, value: List[HostSubSpecification]):
        self._subSpecs = value
    @property
    def changeID(self) -> str: ...
    @changeID.setter
    def changeID(self, value: str):
        self._changeID = value


class HostSubSpecification(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def createdTime(self) -> datetime: ...
    @createdTime.setter
    def createdTime(self, value: datetime):
        self._createdTime = value
    @property
    def data(self) -> List[byte]: ...
    @data.setter
    def data(self, value: List[byte]):
        self._data = value
    @property
    def binaryData(self) -> binary: ...
    @binaryData.setter
    def binaryData(self, value: binary):
        self._binaryData = value


class IpAddressProfile(vim.profile.ApplyProfile): ...


class IpRouteProfile(vim.profile.ApplyProfile):
    @property
    def staticRoute(self) -> List[StaticRouteProfile]: ...
    @staticRoute.setter
    def staticRoute(self, value: List[StaticRouteProfile]):
        self._staticRoute = value


class NasStorageProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class NetStackInstanceProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def dnsConfig(self) -> NetworkProfile.DnsConfigProfile: ...
    @dnsConfig.setter
    def dnsConfig(self, value: NetworkProfile.DnsConfigProfile):
        self._dnsConfig = value
    @property
    def ipRouteConfig(self) -> IpRouteProfile: ...
    @ipRouteConfig.setter
    def ipRouteConfig(self, value: IpRouteProfile):
        self._ipRouteConfig = value


class NetworkPolicyProfile(vim.profile.ApplyProfile): ...


class NetworkProfile(vim.profile.ApplyProfile):
    @property
    def vswitch(self) -> List[VirtualSwitchProfile]: ...
    @vswitch.setter
    def vswitch(self, value: List[VirtualSwitchProfile]):
        self._vswitch = value
    @property
    def vmPortGroup(self) -> List[VmPortGroupProfile]: ...
    @vmPortGroup.setter
    def vmPortGroup(self, value: List[VmPortGroupProfile]):
        self._vmPortGroup = value
    @property
    def hostPortGroup(self) -> List[HostPortGroupProfile]: ...
    @hostPortGroup.setter
    def hostPortGroup(self, value: List[HostPortGroupProfile]):
        self._hostPortGroup = value
    @property
    def serviceConsolePortGroup(self) -> List[ServiceConsolePortGroupProfile]: ...
    @serviceConsolePortGroup.setter
    def serviceConsolePortGroup(self, value: List[ServiceConsolePortGroupProfile]):
        self._serviceConsolePortGroup = value
    @property
    def dnsConfig(self) -> NetworkProfile.DnsConfigProfile: ...
    @dnsConfig.setter
    def dnsConfig(self, value: NetworkProfile.DnsConfigProfile):
        self._dnsConfig = value
    @property
    def ipRouteConfig(self) -> IpRouteProfile: ...
    @ipRouteConfig.setter
    def ipRouteConfig(self, value: IpRouteProfile):
        self._ipRouteConfig = value
    @property
    def consoleIpRouteConfig(self) -> IpRouteProfile: ...
    @consoleIpRouteConfig.setter
    def consoleIpRouteConfig(self, value: IpRouteProfile):
        self._consoleIpRouteConfig = value
    @property
    def pnic(self) -> List[PhysicalNicProfile]: ...
    @pnic.setter
    def pnic(self, value: List[PhysicalNicProfile]):
        self._pnic = value
    @property
    def dvswitch(self) -> List[DvsProfile]: ...
    @dvswitch.setter
    def dvswitch(self, value: List[DvsProfile]):
        self._dvswitch = value
    @property
    def dvsServiceConsoleNic(self) -> List[DvsServiceConsoleVNicProfile]: ...
    @dvsServiceConsoleNic.setter
    def dvsServiceConsoleNic(self, value: List[DvsServiceConsoleVNicProfile]):
        self._dvsServiceConsoleNic = value
    @property
    def dvsHostNic(self) -> List[DvsHostVNicProfile]: ...
    @dvsHostNic.setter
    def dvsHostNic(self, value: List[DvsHostVNicProfile]):
        self._dvsHostNic = value
    @property
    def nsxHostNic(self) -> List[NsxHostVNicProfile]: ...
    @nsxHostNic.setter
    def nsxHostNic(self, value: List[NsxHostVNicProfile]):
        self._nsxHostNic = value
    @property
    def netStackInstance(self) -> List[NetStackInstanceProfile]: ...
    @netStackInstance.setter
    def netStackInstance(self, value: List[NetStackInstanceProfile]):
        self._netStackInstance = value
    @property
    def opaqueSwitch(self) -> OpaqueSwitchProfile: ...
    @opaqueSwitch.setter
    def opaqueSwitch(self, value: OpaqueSwitchProfile):
        self._opaqueSwitch = value


    class DnsConfigProfile(vim.profile.ApplyProfile): ...


class NsxHostVNicProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def ipConfig(self) -> IpAddressProfile: ...
    @ipConfig.setter
    def ipConfig(self, value: IpAddressProfile):
        self._ipConfig = value


class OpaqueSwitchProfile(vim.profile.ApplyProfile): ...


class OptionProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class PermissionProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class PhysicalNicProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class PnicUplinkProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class PortGroupProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def vlan(self) -> PortGroupProfile.VlanProfile: ...
    @vlan.setter
    def vlan(self, value: PortGroupProfile.VlanProfile):
        self._vlan = value
    @property
    def vswitch(self) -> PortGroupProfile.VirtualSwitchSelectionProfile: ...
    @vswitch.setter
    def vswitch(self, value: PortGroupProfile.VirtualSwitchSelectionProfile):
        self._vswitch = value
    @property
    def networkPolicy(self) -> NetworkPolicyProfile: ...
    @networkPolicy.setter
    def networkPolicy(self, value: NetworkPolicyProfile):
        self._networkPolicy = value


    class VirtualSwitchSelectionProfile(vim.profile.ApplyProfile): ...


    class VlanProfile(vim.profile.ApplyProfile): ...


class SecurityProfile(vim.profile.ApplyProfile):
    @property
    def permission(self) -> List[PermissionProfile]: ...
    @permission.setter
    def permission(self, value: List[PermissionProfile]):
        self._permission = value


class ServiceConsolePortGroupProfile(PortGroupProfile):
    @property
    def ipConfig(self) -> IpAddressProfile: ...
    @ipConfig.setter
    def ipConfig(self, value: IpAddressProfile):
        self._ipConfig = value


class ServiceProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class StaticRouteProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class StorageProfile(vim.profile.ApplyProfile):
    @property
    def nasStorage(self) -> List[NasStorageProfile]: ...
    @nasStorage.setter
    def nasStorage(self, value: List[NasStorageProfile]):
        self._nasStorage = value


class UserGroupProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class UserProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value


class VirtualSwitchProfile(vim.profile.ApplyProfile):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def link(self) -> VirtualSwitchProfile.LinkProfile: ...
    @link.setter
    def link(self, value: VirtualSwitchProfile.LinkProfile):
        self._link = value
    @property
    def numPorts(self) -> VirtualSwitchProfile.NumPortsProfile: ...
    @numPorts.setter
    def numPorts(self, value: VirtualSwitchProfile.NumPortsProfile):
        self._numPorts = value
    @property
    def networkPolicy(self) -> NetworkPolicyProfile: ...
    @networkPolicy.setter
    def networkPolicy(self, value: NetworkPolicyProfile):
        self._networkPolicy = value


    class LinkProfile(vim.profile.ApplyProfile): ...


    class NumPortsProfile(vim.profile.ApplyProfile): ...


class VmPortGroupProfile(PortGroupProfile): ...