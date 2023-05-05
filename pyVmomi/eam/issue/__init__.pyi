from typing import List
from pyVmomi import eam, vim, vmodl
from datetime import datetime


class AgencyDisabled(AgencyIssue): ...


class AgencyIssue(Issue):
    @property
    def agency(self) -> eam.Agency: ...
    @property
    def agencyName(self) -> str: ...
    @property
    def solutionId(self) -> str: ...
    @property
    def solutionName(self) -> str: ...


class AgentIssue(AgencyIssue):
    @property
    def agent(self) -> eam.Agent: ...
    @property
    def agentName(self) -> str: ...
    @property
    def host(self) -> vim.HostSystem: ...
    @property
    def hostName(self) -> str: ...


class CannotAccessAgentOVF(VmNotDeployed):
    @property
    def downloadUrl(self) -> str: ...


class CannotAccessAgentVib(VibNotInstalled):
    @property
    def downloadUrl(self) -> str: ...


class ExtensibleIssue(Issue):
    @property
    def typeId(self) -> str: ...
    @property
    def argument(self) -> List[vmodl.KeyAnyValue]: ...
    @property
    def target(self) -> vim.ManagedEntity: ...
    @property
    def agent(self) -> eam.Agent: ...
    @property
    def agency(self) -> eam.Agency: ...


class HostInMaintenanceMode(VmDeployed): ...


class HostInStandbyMode(VmDeployed): ...


class HostIssue(Issue):
    @property
    def host(self) -> vim.HostSystem: ...


class HostNotReachable(AgentIssue): ...


class HostPoweredOff(VmDeployed): ...


class ImmediateHostRebootRequired(VibIssue): ...


class IncompatibleHostVersion(VmNotDeployed): ...


class InsufficientIpAddresses(VmPoweredOff):
    @property
    def network(self) -> vim.Network: ...


class InsufficientResources(VmNotDeployed): ...


class InsufficientSpace(VmNotDeployed): ...


class InvalidConfig(VmIssue):
    @property
    def error(self) -> object: ...


class Issue(vmodl.DynamicData):
    @property
    def key(self) -> int: ...
    @property
    def description(self) -> str: ...
    @property
    def time(self) -> datetime: ...


class MissingAgentIpPool(VmPoweredOff):
    @property
    def network(self) -> vim.Network: ...


class MissingDvFilterSwitch(AgentIssue): ...


class NoAgentVmDatastore(VmNotDeployed): ...


class NoAgentVmNetwork(VmNotDeployed): ...


class NoCustomAgentVmDatastore(NoAgentVmDatastore):
    @property
    def customAgentVmDatastore(self) -> List[vim.Datastore]: ...
    @property
    def customAgentVmDatastoreName(self) -> List[str]: ...


class NoCustomAgentVmNetwork(NoAgentVmNetwork):
    @property
    def customAgentVmNetwork(self) -> List[vim.Network]: ...
    @property
    def customAgentVmNetworkName(self) -> List[str]: ...


class NoDiscoverableAgentVmDatastore(VmNotDeployed): ...


class NoDiscoverableAgentVmNetwork(VmNotDeployed): ...


class OrphanedAgency(AgencyIssue): ...


class OrphanedDvFilterSwitch(HostIssue): ...


class OvfInvalidFormat(VmNotDeployed):
    @property
    def error(self) -> List[vmodl.MethodFault]: ...


class OvfInvalidProperty(AgentIssue):
    @property
    def error(self) -> List[vmodl.MethodFault]: ...


class UnknownAgentVm(HostIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...


class VibCannotPutHostInMaintenanceMode(VibIssue): ...


class VibCannotPutHostOutOfMaintenanceMode(VibIssue): ...


class VibDependenciesNotMetByHost(VibNotInstalled): ...


class VibInvalidFormat(VibNotInstalled): ...


class VibIssue(AgentIssue): ...


class VibNotInstalled(VibIssue): ...


class VibRequirementsNotMetByHost(VibNotInstalled): ...


class VibRequiresHostInMaintenanceMode(VibIssue): ...


class VibRequiresHostReboot(VibIssue): ...


class VibRequiresManualInstallation(VibIssue):
    @property
    def bulletin(self) -> List[str]: ...


class VibRequiresManualUninstallation(VibIssue):
    @property
    def bulletin(self) -> List[str]: ...


class VmCorrupted(VmIssue):
    @property
    def missingFile(self) -> str: ...


class VmDeployed(VmIssue): ...


class VmIssue(AgentIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...


class VmMarkedAsTemplate(VmIssue): ...


class VmNotDeployed(AgentIssue): ...


class VmOrphaned(VmIssue): ...


class VmPoweredOff(VmIssue): ...


class VmPoweredOn(VmIssue): ...


class VmRequiresHostOutOfMaintenanceMode(VmNotDeployed): ...


class VmSuspended(VmIssue): ...


class VmWrongFolder(VmIssue):
    @property
    def currentFolder(self) -> vim.Folder: ...
    @property
    def requiredFolder(self) -> vim.Folder: ...


class VmWrongResourcePool(VmIssue):
    @property
    def currentResourcePool(self) -> vim.ResourcePool: ...
    @property
    def requiredResourcePool(self) -> vim.ResourcePool: ...