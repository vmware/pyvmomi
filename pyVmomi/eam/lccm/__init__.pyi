from typing import List
from enum import Enum
from pyVmomi import eam, vim, vmodl
from datetime import datetime


class Hooks():


    class HookInfo(vmodl.DynamicData):
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @property
        def solution(self) -> str: ...
        @property
        def hookType(self) -> str: ...
        @property
        def raisedAt(self) -> datetime: ...


    class HookListSpec(vmodl.DynamicData):
        @property
        def solutions(self) -> List[str]: ...
        @property
        def hosts(self) -> List[vim.HostSystem]: ...


    class HookProcessSpec(vmodl.DynamicData):
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @property
        def hookType(self) -> str: ...
        @property
        def processingResult(self) -> str: ...


    class ExternalProcessingResult(Enum):
        SUCCESS = "SUCCESS"
        UNKNOWN_ERROR = "UNKNOWN_ERROR"
        VM_CONFIG_ERROR = "VM_CONFIG_ERROR"


    class HookType(Enum):
        POST_PROVISIONING = "POST_PROVISIONING"
        PRE_POWER_ON = "PRE_POWER_ON"
        POST_POWER_ON = "POST_POWER_ON"


class Solutions():


    class ApplicationResult(vmodl.DynamicData):
        @property
        def hosts(self) -> List[Solutions.HostApplicationResult]: ...


    class ApplySpec(vmodl.DynamicData):
        @property
        def desiredState(self) -> List[Solutions.SolutionConfig]: ...
        @property
        def transitionMap(self) -> List[Solutions.TransitionInfo]: ...
        @property
        def solutions(self) -> List[str]: ...
        @property
        def hosts(self) -> List[vim.HostSystem]: ...


    class ComplianceResult(vmodl.DynamicData):
        @property
        def compliant(self) -> bool: ...
        @property
        def hosts(self) -> List[Solutions.HostComplianceResult]: ...


    class ComplianceSpec(vmodl.DynamicData):
        @property
        def desiredState(self) -> List[Solutions.SolutionConfig]: ...
        @property
        def solutions(self) -> List[str]: ...
        @property
        def hosts(self) -> List[vim.HostSystem]: ...


    class HookAcknowledgeConfig(vmodl.DynamicData): ...


    class HookConfig(vmodl.DynamicData):
        @property
        def type(self) -> str: ...
        @property
        def acknowledgement(self) -> Solutions.HookAcknowledgeConfig: ...


    class HostApplicationResult(vmodl.DynamicData):
        @property
        def host(self) -> vim.HostSystem: ...
        @property
        def started(self) -> bool: ...
        @property
        def hostOperational(self) -> bool: ...
        @property
        def solutions(self) -> List[Solutions.SolutionApplicationResult]: ...


    class HostBoundSolutionConfig(Solutions.TypeSpecificSolutionConfig):
        @property
        def preferHostConfiguration(self) -> bool: ...
        @property
        def networks(self) -> List[vim.Network]: ...
        @property
        def datastores(self) -> List[vim.Datastore]: ...
        @property
        def vmci(self) -> List[str]: ...


    class HostComplianceResult(vmodl.DynamicData):
        @property
        def host(self) -> vim.HostSystem: ...
        @property
        def compliant(self) -> bool: ...
        @property
        def solutions(self) -> List[Solutions.SolutionComplianceResult]: ...


    class InteractiveHookAcknowledgeConfig(Solutions.HookAcknowledgeConfig): ...


    class OvfProperty(vmodl.DynamicData):
        @property
        def key(self) -> str: ...
        @property
        def value(self) -> str: ...


    class ProfileIdStoragePolicy(Solutions.StoragePolicy):
        @property
        def profileId(self) -> str: ...


    class SolutionApplicationResult(vmodl.DynamicData):
        @property
        def solution(self) -> str: ...
        @property
        def installing(self) -> bool: ...
        @property
        def validation(self) -> Solutions.SolutionValidationResult: ...


    class SolutionComplianceResult(vmodl.DynamicData):
        @property
        def solution(self) -> str: ...
        @property
        def compliant(self) -> bool: ...
        @property
        def installing(self) -> bool: ...
        @property
        def nonComplianceReason(self) -> str: ...
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @property
        def upgradingVm(self) -> vim.VirtualMachine: ...
        @property
        def hook(self) -> Hooks.HookInfo: ...
        @property
        def issues(self) -> List[eam.issue.Issue]: ...
        @property
        def solutionConfig(self) -> Solutions.SolutionConfig: ...


    class SolutionConfig(vmodl.DynamicData):
        @property
        def solution(self) -> str: ...
        @property
        def name(self) -> str: ...
        @property
        def version(self) -> str: ...
        @property
        def vmSource(self) -> Solutions.VMSource: ...
        @property
        def uuidVmName(self) -> bool: ...
        @property
        def resourcePool(self) -> vim.ResourcePool: ...
        @property
        def folder(self) -> vim.Folder: ...
        @property
        def ovfProperties(self) -> List[Solutions.OvfProperty]: ...
        @property
        def storagePolicies(self) -> List[Solutions.StoragePolicy]: ...
        @property
        def vmDiskProvisioning(self) -> str: ...
        @property
        def vmDeploymentOptimization(self) -> str: ...
        @property
        def typeSpecificConfig(self) -> Solutions.TypeSpecificSolutionConfig: ...
        @property
        def hooks(self) -> List[Solutions.HookConfig]: ...


    class SolutionValidationResult(vmodl.DynamicData):
        @property
        def solution(self) -> str: ...
        @property
        def valid(self) -> bool: ...
        @property
        def invalidReason(self) -> str: ...


    class StoragePolicy(vmodl.DynamicData): ...


    class TransitionInfo(vmodl.DynamicData):
        @property
        def solution(self) -> str: ...
        @property
        def agencyId(self) -> str: ...


    class TypeSpecificSolutionConfig(vmodl.DynamicData): ...


    class UrlVMSource(Solutions.VMSource):
        @property
        def ovfUrl(self) -> str: ...
        @property
        def certificatePEM(self) -> str: ...


    class VMSource(vmodl.DynamicData): ...


    class ValidateSpec(vmodl.DynamicData):
        @property
        def desiredState(self) -> List[Solutions.SolutionConfig]: ...
        @property
        def transitionMap(self) -> List[Solutions.TransitionInfo]: ...


    class ValidationResult(vmodl.DynamicData):
        @property
        def valid(self) -> bool: ...
        @property
        def solutionResult(self) -> List[Solutions.SolutionValidationResult]: ...


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