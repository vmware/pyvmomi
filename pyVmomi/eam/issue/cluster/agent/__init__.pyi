from typing import List
from pyVmomi import eam, vim, vmodl


class AgentIssue(eam.issue.AgencyIssue):
    @property
    def agent(self) -> eam.Agent: ...
    @property
    def cluster(self) -> vim.ComputeResource: ...


class InsufficientClusterResources(VmPoweredOff): ...


class InsufficientClusterSpace(VmNotDeployed): ...


class InvalidConfig(VmIssue):
    @property
    def error(self) -> object: ...


class MissingClusterVmDatastore(VmNotDeployed):
    @property
    def missingDatastores(self) -> List[vim.Datastore]: ...


class MissingClusterVmNetwork(VmNotDeployed):
    @property
    def missingNetworks(self) -> List[vim.Network]: ...
    @property
    def networkNames(self) -> List[str]: ...


class OvfInvalidProperty(AgentIssue):
    @property
    def error(self) -> List[vmodl.MethodFault]: ...


class VmIssue(AgentIssue):
    @property
    def vm(self) -> vim.VirtualMachine: ...


class VmNotDeployed(AgentIssue): ...


class VmNotRemoved(VmIssue): ...


class VmPoweredOff(VmIssue): ...


class VmPoweredOn(VmIssue): ...


class VmSuspended(VmIssue): ...