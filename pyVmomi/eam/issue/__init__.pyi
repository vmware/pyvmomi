from typing import List
from pyVmomi import eam, vim, vmodl
from datetime import datetime
from . import cluster, integrity, personality


class AgencyDisabled(AgencyIssue): ...


class AgencyIssue(Issue):
    @property
    def agency(self) -> eam.Agency: ...
    @agency.setter
    def agency(self, value: eam.Agency):
        self._agency = value
    @property
    def agencyName(self) -> str: ...
    @agencyName.setter
    def agencyName(self, value: str):
        self._agencyName = value
    @property
    def solutionId(self) -> str: ...
    @solutionId.setter
    def solutionId(self, value: str):
        self._solutionId = value
    @property
    def solutionName(self) -> str: ...
    @solutionName.setter
    def solutionName(self, value: str):
        self._solutionName = value


class AgentIssue(AgencyIssue):
    @property
    def agent(self) -> eam.Agent: ...
    @agent.setter
    def agent(self, value: eam.Agent):
        self._agent = value
    @property
    def agentName(self) -> str: ...
    @agentName.setter
    def agentName(self, value: str):
        self._agentName = value
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


class CannotAccessAgentOVF(VmNotDeployed):
    @property
    def downloadUrl(self) -> str: ...
    @downloadUrl.setter
    def downloadUrl(self, value: str):
        self._downloadUrl = value


class CannotAccessAgentVib(VibNotInstalled):
    @property
    def downloadUrl(self) -> str: ...
    @downloadUrl.setter
    def downloadUrl(self, value: str):
        self._downloadUrl = value


class ExtensibleIssue(Issue):
    @property
    def typeId(self) -> str: ...
    @typeId.setter
    def typeId(self, value: str):
        self._typeId = value
    @property
    def argument(self) -> List[vmodl.KeyAnyValue]: ...
    @argument.setter
    def argument(self, value: List[vmodl.KeyAnyValue]):
        self._argument = value
    @property
    def target(self) -> vim.ManagedEntity: ...
    @target.setter
    def target(self, value: vim.ManagedEntity):
        self._target = value
    @property
    def agent(self) -> eam.Agent: ...
    @agent.setter
    def agent(self, value: eam.Agent):
        self._agent = value
    @property
    def agency(self) -> eam.Agency: ...
    @agency.setter
    def agency(self, value: eam.Agency):
        self._agency = value


class HostInMaintenanceMode(VmDeployed): ...


class HostInStandbyMode(VmDeployed): ...


class HostIssue(Issue):
    @property
    def host(self) -> vim.HostSystem: ...
    @host.setter
    def host(self, value: vim.HostSystem):
        self._host = value


class HostNotReachable(AgentIssue): ...


class HostPoweredOff(VmDeployed): ...


class ImmediateHostRebootRequired(VibIssue): ...


class IncompatibleHostVersion(VmNotDeployed): ...


class InsufficientIpAddresses(VmPoweredOff):
    @property
    def network(self) -> vim.Network: ...
    @network.setter
    def network(self, value: vim.Network):
        self._network = value


class InsufficientResources(VmNotDeployed): ...


class InsufficientSpace(VmNotDeployed): ...


class InvalidConfig(VmIssue):
    @property
    def error(self) -> object: ...
    @error.setter
    def error(self, value: object):
        self._error = value


class Issue(vmodl.DynamicData):
    @property
    def key(self) -> int: ...
    @key.setter
    def key(self, value: int):
        self._key = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def time(self) -> datetime: ...
    @time.setter
    def time(self, value: datetime):
        self._time = value


class MissingAgentIpPool(VmPoweredOff):
    @property
    def network(self) -> vim.Network: ...
    @network.setter
    def network(self, value: vim.Network):
        self._network = value


class MissingDvFilterSwitch(AgentIssue): ...


class NoAgentVmDatastore(VmNotDeployed): ...


class NoAgentVmNetwork(VmNotDeployed): ...


class NoCustomAgentVmDatastore(NoAgentVmDatastore):
    @property
    def customAgentVmDatastore(self) -> List[vim.Datastore]: ...
    @customAgentVmDatastore.setter
    def customAgentVmDatastore(self, value: List[vim.Datastore]):
        self._customAgentVmDatastore = value
    @property
    def customAgentVmDatastoreName(self) -> List[str]: ...
    @customAgentVmDatastoreName.setter
    def customAgentVmDatastoreName(self, value: List[str]):
        self._customAgentVmDatastoreName = value


class NoCustomAgentVmNetwork(NoAgentVmNetwork):
    @property
    def customAgentVmNetwork(self) -> List[vim.Network]: ...
    @customAgentVmNetwork.setter
    def customAgentVmNetwork(self, value: List[vim.Network]):
        self._customAgentVmNetwork = value
    @property
    def customAgentVmNetworkName(self) -> List[str]: ...
    @customAgentVmNetworkName.setter
    def customAgentVmNetworkName(self, value: List[str]):
        self._customAgentVmNetworkName = value


class NoDiscoverableAgentVmDatastore(VmNotDeployed): ...


class NoDiscoverableAgentVmNetwork(VmNotDeployed): ...


class OrphanedAgency(AgencyIssue): ...


class OrphanedDvFilterSwitch(HostIssue): ...


class OvfInvalidFormat(VmNotDeployed):
    @property
    def error(self) -> List[vmodl.MethodFault]: ...
    @error.setter
    def error(self, value: List[vmodl.MethodFault]):
        self._error = value


class OvfInvalidProperty(AgentIssue):
    @property
    def error(self) -> List[vmodl.MethodFault]: ...
    @error.setter
    def error(self, value: List[vmodl.MethodFault]):
        self._error = value


class UnknownAgentVm(HostIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value


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
    @bulletin.setter
    def bulletin(self, value: List[str]):
        self._bulletin = value


class VibRequiresManualUninstallation(VibIssue):
    @property
    def bulletin(self) -> List[str]: ...
    @bulletin.setter
    def bulletin(self, value: List[str]):
        self._bulletin = value


class VmCorrupted(VmIssue):
    @property
    def missingFile(self) -> str: ...
    @missingFile.setter
    def missingFile(self, value: str):
        self._missingFile = value


class VmDeployed(VmIssue): ...


class VmIssue(AgentIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value


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
    @currentFolder.setter
    def currentFolder(self, value: vim.Folder):
        self._currentFolder = value
    @property
    def requiredFolder(self) -> vim.Folder: ...
    @requiredFolder.setter
    def requiredFolder(self, value: vim.Folder):
        self._requiredFolder = value


class VmWrongResourcePool(VmIssue):
    @property
    def currentResourcePool(self) -> vim.ResourcePool: ...
    @currentResourcePool.setter
    def currentResourcePool(self, value: vim.ResourcePool):
        self._currentResourcePool = value
    @property
    def requiredResourcePool(self) -> vim.ResourcePool: ...
    @requiredResourcePool.setter
    def requiredResourcePool(self, value: vim.ResourcePool):
        self._requiredResourcePool = value