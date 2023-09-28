from typing import List
from enum import Enum
from pyVmomi import eam, vim, vmodl
from datetime import datetime


class Hooks():


    class HookInfo(vmodl.DynamicData):
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @vm.setter
        def vm(self, value: vim.VirtualMachine):
            self._vm = value
        @property
        def solution(self) -> str: ...
        @solution.setter
        def solution(self, value: str):
            self._solution = value
        @property
        def hookType(self) -> str: ...
        @hookType.setter
        def hookType(self, value: str):
            self._hookType = value
        @property
        def raisedAt(self) -> datetime: ...
        @raisedAt.setter
        def raisedAt(self, value: datetime):
            self._raisedAt = value


    class HookListSpec(vmodl.DynamicData):
        @property
        def solutions(self) -> List[str]: ...
        @solutions.setter
        def solutions(self, value: List[str]):
            self._solutions = value
        @property
        def hosts(self) -> List[vim.HostSystem]: ...
        @hosts.setter
        def hosts(self, value: List[vim.HostSystem]):
            self._hosts = value


    class MarkAsProcessedSpec(vmodl.DynamicData):
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @vm.setter
        def vm(self, value: vim.VirtualMachine):
            self._vm = value
        @property
        def hookType(self) -> str: ...
        @hookType.setter
        def hookType(self, value: str):
            self._hookType = value
        @property
        def success(self) -> bool: ...
        @success.setter
        def success(self, value: bool):
            self._success = value


    class HookType(Enum):
        POST_PROVISIONING = "POST_PROVISIONING"
        POST_POWER_ON = "POST_POWER_ON"


class Solutions():


    class ApplySpec(vmodl.DynamicData):
        @property
        def desiredState(self) -> List[Solutions.SolutionConfig]: ...
        @desiredState.setter
        def desiredState(self, value: List[Solutions.SolutionConfig]):
            self._desiredState = value
        @property
        def solutions(self) -> List[str]: ...
        @solutions.setter
        def solutions(self, value: List[str]):
            self._solutions = value
        @property
        def hosts(self) -> List[vim.HostSystem]: ...
        @hosts.setter
        def hosts(self, value: List[vim.HostSystem]):
            self._hosts = value


    class ComplianceResult(vmodl.DynamicData):
        @property
        def compliant(self) -> bool: ...
        @compliant.setter
        def compliant(self, value: bool):
            self._compliant = value
        @property
        def hosts(self) -> List[Solutions.HostComplianceResult]: ...
        @hosts.setter
        def hosts(self, value: List[Solutions.HostComplianceResult]):
            self._hosts = value


    class ComplianceSpec(vmodl.DynamicData):
        @property
        def desiredState(self) -> List[Solutions.SolutionConfig]: ...
        @desiredState.setter
        def desiredState(self, value: List[Solutions.SolutionConfig]):
            self._desiredState = value
        @property
        def solutions(self) -> List[str]: ...
        @solutions.setter
        def solutions(self, value: List[str]):
            self._solutions = value
        @property
        def hosts(self) -> List[vim.HostSystem]: ...
        @hosts.setter
        def hosts(self, value: List[vim.HostSystem]):
            self._hosts = value


    class HookAcknowledgeConfig(vmodl.DynamicData): ...


    class HookConfig(vmodl.DynamicData):
        @property
        def type(self) -> str: ...
        @type.setter
        def type(self, value: str):
            self._type = value
        @property
        def acknowledgement(self) -> Solutions.HookAcknowledgeConfig: ...
        @acknowledgement.setter
        def acknowledgement(self, value: Solutions.HookAcknowledgeConfig):
            self._acknowledgement = value


    class HostBoundSolutionConfig(Solutions.TypeSpecificSolutionConfig):
        @property
        def preferHostConfiguration(self) -> bool: ...
        @preferHostConfiguration.setter
        def preferHostConfiguration(self, value: bool):
            self._preferHostConfiguration = value
        @property
        def networks(self) -> List[vim.Network]: ...
        @networks.setter
        def networks(self, value: List[vim.Network]):
            self._networks = value
        @property
        def datastores(self) -> List[vim.Datastore]: ...
        @datastores.setter
        def datastores(self, value: List[vim.Datastore]):
            self._datastores = value
        @property
        def vmci(self) -> List[str]: ...
        @vmci.setter
        def vmci(self, value: List[str]):
            self._vmci = value


    class HostComplianceResult(vmodl.DynamicData):
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def compliant(self) -> bool: ...
        @compliant.setter
        def compliant(self, value: bool):
            self._compliant = value
        @property
        def solutions(self) -> List[Solutions.SolutionComplianceResult]: ...
        @solutions.setter
        def solutions(self, value: List[Solutions.SolutionComplianceResult]):
            self._solutions = value


    class InteractiveHookAcknowledgeConfig(Solutions.HookAcknowledgeConfig): ...


    class OvfProperty(vmodl.DynamicData):
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


    class ProfileIdStoragePolicy(Solutions.StoragePolicy):
        @property
        def profileId(self) -> str: ...
        @profileId.setter
        def profileId(self, value: str):
            self._profileId = value


    class SolutionComplianceResult(vmodl.DynamicData):
        @property
        def solution(self) -> str: ...
        @solution.setter
        def solution(self, value: str):
            self._solution = value
        @property
        def compliant(self) -> bool: ...
        @compliant.setter
        def compliant(self, value: bool):
            self._compliant = value
        @property
        def nonComplianceReason(self) -> str: ...
        @nonComplianceReason.setter
        def nonComplianceReason(self, value: str):
            self._nonComplianceReason = value
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @vm.setter
        def vm(self, value: vim.VirtualMachine):
            self._vm = value
        @property
        def upgradingVm(self) -> vim.VirtualMachine: ...
        @upgradingVm.setter
        def upgradingVm(self, value: vim.VirtualMachine):
            self._upgradingVm = value
        @property
        def hook(self) -> Hooks.HookInfo: ...
        @hook.setter
        def hook(self, value: Hooks.HookInfo):
            self._hook = value
        @property
        def issues(self) -> List[eam.issue.Issue]: ...
        @issues.setter
        def issues(self, value: List[eam.issue.Issue]):
            self._issues = value
        @property
        def solutionConfig(self) -> Solutions.SolutionConfig: ...
        @solutionConfig.setter
        def solutionConfig(self, value: Solutions.SolutionConfig):
            self._solutionConfig = value


    class SolutionConfig(vmodl.DynamicData):
        @property
        def solution(self) -> str: ...
        @solution.setter
        def solution(self, value: str):
            self._solution = value
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
        def vmSource(self) -> Solutions.VMSource: ...
        @vmSource.setter
        def vmSource(self, value: Solutions.VMSource):
            self._vmSource = value
        @property
        def uuidVmName(self) -> bool: ...
        @uuidVmName.setter
        def uuidVmName(self, value: bool):
            self._uuidVmName = value
        @property
        def resourcePool(self) -> vim.ResourcePool: ...
        @resourcePool.setter
        def resourcePool(self, value: vim.ResourcePool):
            self._resourcePool = value
        @property
        def folder(self) -> vim.Folder: ...
        @folder.setter
        def folder(self, value: vim.Folder):
            self._folder = value
        @property
        def ovfProperties(self) -> List[Solutions.OvfProperty]: ...
        @ovfProperties.setter
        def ovfProperties(self, value: List[Solutions.OvfProperty]):
            self._ovfProperties = value
        @property
        def storagePolicies(self) -> List[Solutions.StoragePolicy]: ...
        @storagePolicies.setter
        def storagePolicies(self, value: List[Solutions.StoragePolicy]):
            self._storagePolicies = value
        @property
        def vmDiskProvisioning(self) -> str: ...
        @vmDiskProvisioning.setter
        def vmDiskProvisioning(self, value: str):
            self._vmDiskProvisioning = value
        @property
        def vmDeploymentOptimization(self) -> str: ...
        @vmDeploymentOptimization.setter
        def vmDeploymentOptimization(self, value: str):
            self._vmDeploymentOptimization = value
        @property
        def typeSpecificConfig(self) -> Solutions.TypeSpecificSolutionConfig: ...
        @typeSpecificConfig.setter
        def typeSpecificConfig(self, value: Solutions.TypeSpecificSolutionConfig):
            self._typeSpecificConfig = value
        @property
        def hooks(self) -> List[Solutions.HookConfig]: ...
        @hooks.setter
        def hooks(self, value: List[Solutions.HookConfig]):
            self._hooks = value


    class SolutionValidationResult(vmodl.DynamicData):
        @property
        def solution(self) -> str: ...
        @solution.setter
        def solution(self, value: str):
            self._solution = value
        @property
        def valid(self) -> bool: ...
        @valid.setter
        def valid(self, value: bool):
            self._valid = value
        @property
        def invalidReason(self) -> str: ...
        @invalidReason.setter
        def invalidReason(self, value: str):
            self._invalidReason = value


    class StoragePolicy(vmodl.DynamicData): ...


    class TransitionSpec(vmodl.DynamicData):
        @property
        def solution(self) -> str: ...
        @solution.setter
        def solution(self, value: str):
            self._solution = value
        @property
        def agencyId(self) -> str: ...
        @agencyId.setter
        def agencyId(self, value: str):
            self._agencyId = value


    class TypeSpecificSolutionConfig(vmodl.DynamicData): ...


    class UrlVMSource(Solutions.VMSource):
        @property
        def ovfUrl(self) -> str: ...
        @ovfUrl.setter
        def ovfUrl(self, value: str):
            self._ovfUrl = value
        @property
        def certificatePEM(self) -> str: ...
        @certificatePEM.setter
        def certificatePEM(self, value: str):
            self._certificatePEM = value


    class VMSource(vmodl.DynamicData): ...


    class ValidateSpec(vmodl.DynamicData):
        @property
        def desiredState(self) -> List[Solutions.SolutionConfig]: ...
        @desiredState.setter
        def desiredState(self, value: List[Solutions.SolutionConfig]):
            self._desiredState = value


    class ValidationResult(vmodl.DynamicData):
        @property
        def valid(self) -> bool: ...
        @valid.setter
        def valid(self, value: bool):
            self._valid = value
        @property
        def solutionResult(self) -> List[Solutions.SolutionValidationResult]: ...
        @solutionResult.setter
        def solutionResult(self, value: List[Solutions.SolutionValidationResult]):
            self._solutionResult = value


    class InvalidReason(Enum):
        INVALID_OVF_DESCRIPTOR = "INVALID_OVF_DESCRIPTOR"
        INACCESSBLE_VM_SOURCE = "INACCESSBLE_VM_SOURCE"
        INVALID_NETWORKS = "INVALID_NETWORKS"
        INVALID_DATASTORES = "INVALID_DATASTORES"
        INVALID_RESOURCE_POOL = "INVALID_RESOURCE_POOL"
        INVALID_FOLDER = "INVALID_FOLDER"
        INVALID_PROPERTIES = "INVALID_PROPERTIES"
        INVALID_TRANSITION = "INVALID_TRANSITION"


    class NonComplianceReason(Enum):
        WORKING = "WORKING"
        ISSUE = "ISSUE"
        IN_HOOK = "IN_HOOK"
        OBSOLETE_SPEC = "OBSOLETE_SPEC"
        NO_SPEC = "NO_SPEC"


    class VMDeploymentOptimization(Enum):
        ALL_CLONES = "ALL_CLONES"
        FULL_CLONES_ONLY = "FULL_CLONES_ONLY"
        NO_CLONES = "NO_CLONES"


    class VMDiskProvisioning(Enum):
        THIN = "THIN"
        THICK = "THICK"