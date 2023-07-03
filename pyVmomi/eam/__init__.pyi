from typing import List, Literal
from enum import Enum
from pyVmomi import eam, vim, vmodl
from pyVmomi.VmomiSupport import ManagedObject, NoneType
from . import fault as fault
from . import issue as issue
from . import lccm as lccm
from . import vib as vib


class Agency(EamObject):
    @property
    def solutionId(self) -> str: ...
    @property
    def owner(self) -> str: ...
    @property
    def config(self) -> Agency.ConfigInfo: ...
    @property
    def runtime(self) -> EamObject.RuntimeInfo: ...
    @property
    def agent(self) -> List[Agent]: ...
    def QuerySolutionId(self) -> str: ...
    def QueryConfig(self) -> Agency.ConfigInfo: ...
    def Update(self, config: Agency.ConfigInfo) -> NoneType: ...
    def QueryRuntime(self) -> EamObject.RuntimeInfo: ...
    def QueryAgent(self) -> List[Agent]: ...
    def RegisterAgentVm(self, agentVm: vim.VirtualMachine) -> Agent: ...
    def UnregisterAgentVm(self, agentVm: vim.VirtualMachine) -> NoneType: ...
    def Enable(self) -> NoneType: ...
    def Disable(self) -> NoneType: ...
    def Uninstall(self) -> NoneType: ...
    def DestroyAgency(self) -> NoneType: ...
    def AddIssue(self, issue: eam.issue.Issue) -> eam.issue.Issue: ...


    class ComputeResourceScope(Agency.Scope):
        @property
        def computeResource(self) -> List[vim.ComputeResource]: ...
        @computeResource.setter
        def computeResource(self, value: List[vim.ComputeResource]):
            self._computeResource = value


    class ConfigInfo(vmodl.DynamicData):
        @property
        def agentConfig(self) -> List[Agent.ConfigInfo]: ...
        @agentConfig.setter
        def agentConfig(self, value: List[Agent.ConfigInfo]):
            self._agentConfig = value
        @property
        def scope(self) -> Agency.Scope: ...
        @scope.setter
        def scope(self, value: Agency.Scope):
            self._scope = value
        @property
        def manuallyMarkAgentVmAvailableAfterProvisioning(self) -> bool: ...
        @manuallyMarkAgentVmAvailableAfterProvisioning.setter
        def manuallyMarkAgentVmAvailableAfterProvisioning(self, value: bool):
            self._manuallyMarkAgentVmAvailableAfterProvisioning = value
        @property
        def manuallyMarkAgentVmAvailableAfterPowerOn(self) -> bool: ...
        @manuallyMarkAgentVmAvailableAfterPowerOn.setter
        def manuallyMarkAgentVmAvailableAfterPowerOn(self, value: bool):
            self._manuallyMarkAgentVmAvailableAfterPowerOn = value
        @property
        def optimizedDeploymentEnabled(self) -> bool: ...
        @optimizedDeploymentEnabled.setter
        def optimizedDeploymentEnabled(self, value: bool):
            self._optimizedDeploymentEnabled = value
        @property
        def agentName(self) -> str: ...
        @agentName.setter
        def agentName(self, value: str):
            self._agentName = value
        @property
        def agencyName(self) -> str: ...
        @agencyName.setter
        def agencyName(self, value: str):
            self._agencyName = value
        @property
        def useUuidVmName(self) -> bool: ...
        @useUuidVmName.setter
        def useUuidVmName(self, value: bool):
            self._useUuidVmName = value
        @property
        def manuallyProvisioned(self) -> bool: ...
        @manuallyProvisioned.setter
        def manuallyProvisioned(self, value: bool):
            self._manuallyProvisioned = value
        @property
        def manuallyMonitored(self) -> bool: ...
        @manuallyMonitored.setter
        def manuallyMonitored(self, value: bool):
            self._manuallyMonitored = value
        @property
        def bypassVumEnabled(self) -> bool: ...
        @bypassVumEnabled.setter
        def bypassVumEnabled(self, value: bool):
            self._bypassVumEnabled = value
        @property
        def agentVmNetwork(self) -> List[vim.Network]: ...
        @agentVmNetwork.setter
        def agentVmNetwork(self, value: List[vim.Network]):
            self._agentVmNetwork = value
        @property
        def agentVmDatastore(self) -> List[vim.Datastore]: ...
        @agentVmDatastore.setter
        def agentVmDatastore(self, value: List[vim.Datastore]):
            self._agentVmDatastore = value
        @property
        def preferHostConfiguration(self) -> bool: ...
        @preferHostConfiguration.setter
        def preferHostConfiguration(self, value: bool):
            self._preferHostConfiguration = value
        @property
        def ipPool(self) -> vim.vApp.IpPool: ...
        @ipPool.setter
        def ipPool(self, value: vim.vApp.IpPool):
            self._ipPool = value
        @property
        def resourcePools(self) -> List[Agency.VMResourcePool]: ...
        @resourcePools.setter
        def resourcePools(self, value: List[Agency.VMResourcePool]):
            self._resourcePools = value
        @property
        def folders(self) -> List[Agency.VMFolder]: ...
        @folders.setter
        def folders(self, value: List[Agency.VMFolder]):
            self._folders = value


    class Scope(vmodl.DynamicData): ...


    class VMFolder(vmodl.DynamicData):
        @property
        def folderId(self) -> vim.Folder: ...
        @folderId.setter
        def folderId(self, value: vim.Folder):
            self._folderId = value
        @property
        def datacenterId(self) -> vim.Datacenter: ...
        @datacenterId.setter
        def datacenterId(self, value: vim.Datacenter):
            self._datacenterId = value


    class VMResourcePool(vmodl.DynamicData):
        @property
        def resourcePoolId(self) -> vim.ResourcePool: ...
        @resourcePoolId.setter
        def resourcePoolId(self, value: vim.ResourcePool):
            self._resourcePoolId = value
        @property
        def computeResourceId(self) -> vim.ComputeResource: ...
        @computeResourceId.setter
        def computeResourceId(self, value: vim.ComputeResource):
            self._computeResourceId = value


class Agent(EamObject):
    @property
    def runtime(self) -> Agent.RuntimeInfo: ...
    @property
    def config(self) -> Agent.ConfigInfo: ...
    def QueryRuntime(self) -> Agent.RuntimeInfo: ...
    def MarkAsAvailable(self) -> NoneType: ...
    def QueryConfig(self) -> Agent.ConfigInfo: ...


    class ConfigInfo(vmodl.DynamicData):
        @property
        def productLineId(self) -> str: ...
        @productLineId.setter
        def productLineId(self, value: str):
            self._productLineId = value
        @property
        def hostVersion(self) -> str: ...
        @hostVersion.setter
        def hostVersion(self, value: str):
            self._hostVersion = value
        @property
        def ovfPackageUrl(self) -> str: ...
        @ovfPackageUrl.setter
        def ovfPackageUrl(self, value: str):
            self._ovfPackageUrl = value
        @property
        def ovfEnvironment(self) -> Agent.OvfEnvironmentInfo: ...
        @ovfEnvironment.setter
        def ovfEnvironment(self, value: Agent.OvfEnvironmentInfo):
            self._ovfEnvironment = value
        @property
        def vibUrl(self) -> str: ...
        @vibUrl.setter
        def vibUrl(self, value: str):
            self._vibUrl = value
        @property
        def vibMatchingRules(self) -> List[Agent.VibMatchingRule]: ...
        @vibMatchingRules.setter
        def vibMatchingRules(self, value: List[Agent.VibMatchingRule]):
            self._vibMatchingRules = value
        @property
        def vibName(self) -> str: ...
        @vibName.setter
        def vibName(self, value: str):
            self._vibName = value
        @property
        def dvFilterEnabled(self) -> bool: ...
        @dvFilterEnabled.setter
        def dvFilterEnabled(self, value: bool):
            self._dvFilterEnabled = value
        @property
        def rebootHostAfterVibUninstall(self) -> bool: ...
        @rebootHostAfterVibUninstall.setter
        def rebootHostAfterVibUninstall(self, value: bool):
            self._rebootHostAfterVibUninstall = value
        @property
        def vmciService(self) -> List[str]: ...
        @vmciService.setter
        def vmciService(self, value: List[str]):
            self._vmciService = value
        @property
        def ovfDiskProvisioning(self) -> str: ...
        @ovfDiskProvisioning.setter
        def ovfDiskProvisioning(self, value: str):
            self._ovfDiskProvisioning = value
        @property
        def vmStoragePolicies(self) -> List[Agent.StoragePolicy]: ...
        @vmStoragePolicies.setter
        def vmStoragePolicies(self, value: List[Agent.StoragePolicy]):
            self._vmStoragePolicies = value


        class OvfDiskProvisioning(Enum):
            none = "none"
            thin = "thin"
            thick = "thick"


    class OvfEnvironmentInfo(vmodl.DynamicData):
        @property
        def ovfProperty(self) -> List[Agent.OvfEnvironmentInfo.OvfProperty]: ...
        @ovfProperty.setter
        def ovfProperty(self, value: List[Agent.OvfEnvironmentInfo.OvfProperty]):
            self._ovfProperty = value


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


    class RuntimeInfo(EamObject.RuntimeInfo):
        @property
        def vmPowerState(self) -> vim.VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended']: ...
        @vmPowerState.setter
        def vmPowerState(self, value: vim.VirtualMachine.PowerState | Literal['poweredOff', 'poweredOn', 'suspended']):
            self._vmPowerState = value
        @property
        def receivingHeartBeat(self) -> bool: ...
        @receivingHeartBeat.setter
        def receivingHeartBeat(self, value: bool):
            self._receivingHeartBeat = value
        @property
        def host(self) -> vim.HostSystem: ...
        @host.setter
        def host(self, value: vim.HostSystem):
            self._host = value
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @vm.setter
        def vm(self, value: vim.VirtualMachine):
            self._vm = value
        @property
        def vmIp(self) -> str: ...
        @vmIp.setter
        def vmIp(self, value: str):
            self._vmIp = value
        @property
        def vmName(self) -> str: ...
        @vmName.setter
        def vmName(self, value: str):
            self._vmName = value
        @property
        def esxAgentResourcePool(self) -> vim.ResourcePool: ...
        @esxAgentResourcePool.setter
        def esxAgentResourcePool(self, value: vim.ResourcePool):
            self._esxAgentResourcePool = value
        @property
        def esxAgentFolder(self) -> vim.Folder: ...
        @esxAgentFolder.setter
        def esxAgentFolder(self, value: vim.Folder):
            self._esxAgentFolder = value
        @property
        def installedBulletin(self) -> List[str]: ...
        @installedBulletin.setter
        def installedBulletin(self, value: List[str]):
            self._installedBulletin = value
        @property
        def installedVibs(self) -> List[eam.vib.VibInfo]: ...
        @installedVibs.setter
        def installedVibs(self, value: List[eam.vib.VibInfo]):
            self._installedVibs = value
        @property
        def agency(self) -> Agency: ...
        @agency.setter
        def agency(self, value: Agency):
            self._agency = value
        @property
        def vmHook(self) -> Agent.VmHook: ...
        @vmHook.setter
        def vmHook(self, value: Agent.VmHook):
            self._vmHook = value


    class StoragePolicy(vmodl.DynamicData): ...


    class VibMatchingRule(vmodl.DynamicData):
        @property
        def vibNameRegex(self) -> str: ...
        @vibNameRegex.setter
        def vibNameRegex(self, value: str):
            self._vibNameRegex = value
        @property
        def vibVersionRegex(self) -> str: ...
        @vibVersionRegex.setter
        def vibVersionRegex(self, value: str):
            self._vibVersionRegex = value


    class VmHook(vmodl.DynamicData):
        @property
        def vm(self) -> vim.VirtualMachine: ...
        @vm.setter
        def vm(self, value: vim.VirtualMachine):
            self._vm = value
        @property
        def vmState(self) -> str: ...
        @vmState.setter
        def vmState(self, value: str):
            self._vmState = value


        class VmState(Enum):
            provisioned = "provisioned"
            poweredOn = "poweredOn"
            prePowerOn = "prePowerOn"


    class VsanStoragePolicy(Agent.StoragePolicy):
        @property
        def profileId(self) -> str: ...
        @profileId.setter
        def profileId(self, value: str):
            self._profileId = value


class EamObject(ManagedObject):
    def Resolve(self, issueKey: List[int]) -> List[int]: ...
    def ResolveAll(self) -> NoneType: ...
    def QueryIssue(self, issueKey: List[int]) -> List[eam.issue.Issue]: ...


    class RuntimeInfo(vmodl.DynamicData):
        @property
        def status(self) -> str: ...
        @status.setter
        def status(self, value: str):
            self._status = value
        @property
        def issue(self) -> List[eam.issue.Issue]: ...
        @issue.setter
        def issue(self, value: List[eam.issue.Issue]):
            self._issue = value
        @property
        def goalState(self) -> str: ...
        @goalState.setter
        def goalState(self, value: str):
            self._goalState = value
        @property
        def entity(self) -> EamObject: ...
        @entity.setter
        def entity(self, value: EamObject):
            self._entity = value


        class GoalState(Enum):
            enabled = "enabled"
            disabled = "disabled"
            uninstalled = "uninstalled"


        class Status(Enum):
            green = "green"
            yellow = "yellow"
            red = "red"


class EsxAgentManager(EamObject):
    @property
    def agency(self) -> List[Agency]: ...
    @property
    def issue(self) -> List[eam.issue.Issue]: ...
    def QueryAgency(self) -> List[Agency]: ...
    def CreateAgency(self, agencyConfigInfo: Agency.ConfigInfo, initialGoalState: str) -> Agency: ...
    def ScanForUnknownAgentVm(self) -> NoneType: ...
    def SetMaintenanceModePolicy(self, policy: str) -> NoneType: ...
    def GetMaintenanceModePolicy(self) -> str: ...


    class MaintenanceModePolicy(Enum):
        singleHost = "singleHost"
        multipleHosts = "multipleHosts"


class Task(ManagedObject): ...