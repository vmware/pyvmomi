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
        SUCCESS = "success"
        UNKNOWN_ERROR = "unknown_error"
        VM_CONFIG_ERROR = "vm_config_error"


    class HookType(Enum):
        POST_PROVISIONING = "post_provisioning"
        PRE_POWER_ON = "pre_power_on"
        POST_POWER_ON = "post_power_on"


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
        INVALID_OVF_DESCRIPTOR = "invalid_ovf_descriptor"
        INACCESSBLE_VM_SOURCE = "inaccessble_vm_source"
        INVALID_NETWORKS = "invalid_networks"
        INVALID_DATASTORES = "invalid_datastores"
        INVALID_RESOURCE_POOL = "invalid_resource_pool"
        INVALID_FOLDER = "invalid_folder"
        INVALID_PROPERTIES = "invalid_properties"
        INVALID_TRANSITION = "invalid_transition"


    class NonComplianceReason(Enum):
        WORKING = "working"
        ISSUE = "issue"
        IN_HOOK = "in_hook"
        OBSOLETE_SPEC = "obsolete_spec"
        NO_SPEC = "no_spec"


    class VMDeploymentOptimization(Enum):
        ALL_CLONES = "all_clones"
        FULL_CLONES_ONLY = "full_clones_only"
        NO_CLONES = "no_clones"


    class VMDiskProvisioning(Enum):
        THIN = "thin"
        THICK = "thick"