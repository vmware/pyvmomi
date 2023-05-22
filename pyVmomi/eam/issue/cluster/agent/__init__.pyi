from typing import List
from pyVmomi import eam, vim, vmodl


class AgentIssue(eam.issue.AgencyIssue):
    @property
    def agent(self) -> eam.Agent: ...
    @agent.setter
    def agent(self, value: eam.Agent):
        self._agent = value
    @property
    def cluster(self) -> vim.ComputeResource: ...
    @cluster.setter
    def cluster(self, value: vim.ComputeResource):
        self._cluster = value


class InsufficientClusterResources(VmPoweredOff): ...


class InsufficientClusterSpace(VmNotDeployed): ...


class InvalidConfig(VmIssue):
    @property
    def error(self) -> object: ...
    @error.setter
    def error(self, value: object):
        self._error = value


class MissingClusterVmDatastore(VmNotDeployed):
    @property
    def missingDatastores(self) -> List[vim.Datastore]: ...
    @missingDatastores.setter
    def missingDatastores(self, value: List[vim.Datastore]):
        self._missingDatastores = value


class MissingClusterVmNetwork(VmNotDeployed):
    @property
    def missingNetworks(self) -> List[vim.Network]: ...
    @missingNetworks.setter
    def missingNetworks(self, value: List[vim.Network]):
        self._missingNetworks = value
    @property
    def networkNames(self) -> List[str]: ...
    @networkNames.setter
    def networkNames(self, value: List[str]):
        self._networkNames = value


class OvfInvalidProperty(AgentIssue):
    @property
    def error(self) -> List[vmodl.MethodFault]: ...
    @error.setter
    def error(self, value: List[vmodl.MethodFault]):
        self._error = value


class VmIssue(AgentIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...
    @vm.setter
    def vm(self, value: vim.VirtualMachine):
        self._vm = value


class VmNotDeployed(AgentIssue): ...


class VmNotRemoved(VmIssue): ...


class VmPoweredOff(VmIssue): ...


class VmPoweredOn(VmIssue): ...


class VmSuspended(VmIssue): ...