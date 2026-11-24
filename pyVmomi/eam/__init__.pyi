# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from . import fault as fault
from . import issue as issue
from . import vib as vib

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.eam.issue
import pyVmomi.eam.vib
import pyVmomi.vim.vApp



class Agency(EamObject):
   class VMResourcePool(pyVmomi.vmodl.DynamicData):
      resourcePoolId: pyVmomi.vim.ResourcePool
      computeResourceId: pyVmomi.vim.ComputeResource

   class VMFolder(pyVmomi.vmodl.DynamicData):
      folderId: pyVmomi.vim.Folder
      datacenterId: pyVmomi.vim.Datacenter

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      agentConfig: list[Agent.ConfigInfo] = []
      scope: _typing.Optional[Scope] = None
      manuallyMarkAgentVmAvailableAfterProvisioning: _typing.Optional[bool] = None
      manuallyMarkAgentVmAvailableAfterPowerOn: _typing.Optional[bool] = None
      optimizedDeploymentEnabled: _typing.Optional[bool] = None
      agentName: _typing.Optional[str] = None
      agencyName: _typing.Optional[str] = None
      useUuidVmName: _typing.Optional[bool] = None
      manuallyProvisioned: _typing.Optional[bool] = None
      manuallyMonitored: _typing.Optional[bool] = None
      bypassVumEnabled: _typing.Optional[bool] = None
      agentVmNetwork: list[pyVmomi.vim.Network] = []
      agentVmDatastore: list[pyVmomi.vim.Datastore] = []
      preferHostConfiguration: _typing.Optional[bool] = None
      ipPool: _typing.Optional[pyVmomi.vim.vApp.IpPool] = None
      resourcePools: list[VMResourcePool] = []
      folders: list[VMFolder] = []

   class Scope(pyVmomi.vmodl.DynamicData):
      pass

   class ComputeResourceScope(Scope):
      computeResource: list[pyVmomi.vim.ComputeResource] = []

   @property
   def solutionId(self) -> str: ...
   @property
   def owner(self) -> _typing.Optional[str]: ...
   @property
   def config(self) -> ConfigInfo: ...
   @property
   def runtime(self) -> EamObject.RuntimeInfo: ...
   @property
   def agent(self) -> list[Agent]: ...

   def QuerySolutionId(self) -> str: ...
   def QueryConfig(self) -> ConfigInfo: ...
   def Update(self, config: ConfigInfo) -> None: ...
   def QueryRuntime(self) -> EamObject.RuntimeInfo: ...
   def QueryAgent(self) -> list[Agent]: ...
   def RegisterAgentVm(self, agentVm: pyVmomi.vim.VirtualMachine) -> Agent: ...
   def UnregisterAgentVm(self, agentVm: pyVmomi.vim.VirtualMachine) -> None: ...
   def Enable(self) -> None: ...
   def Disable(self) -> None: ...
   def Uninstall(self) -> None: ...
   def DestroyAgency(self) -> None: ...
   def AddIssue(self, issue: pyVmomi.eam.issue.Issue) -> pyVmomi.eam.issue.Issue: ...


class Agent(EamObject):
   class RuntimeInfo(EamObject.RuntimeInfo):
      vmPowerState: pyVmomi.vim.VirtualMachine.PowerState
      receivingHeartBeat: bool
      host: _typing.Optional[pyVmomi.vim.HostSystem] = None
      vm: _typing.Optional[pyVmomi.vim.VirtualMachine] = None
      vmIp: _typing.Optional[str] = None
      vmName: str
      esxAgentResourcePool: _typing.Optional[pyVmomi.vim.ResourcePool] = None
      esxAgentFolder: _typing.Optional[pyVmomi.vim.Folder] = None
      installedBulletin: list[str] = []
      installedVibs: list[pyVmomi.eam.vib.VibInfo] = []
      agency: _typing.Optional[Agency] = None
      vmHook: _typing.Optional[VmHook] = None

   class VmHook(pyVmomi.vmodl.DynamicData):
      class VmState(pyVmomi.VmomiSupport.Enum):
         provisioned: _typing.ClassVar['VmState'] = 'provisioned'
         poweredOn: _typing.ClassVar['VmState'] = 'poweredOn'
         prePowerOn: _typing.ClassVar['VmState'] = 'prePowerOn'

      vm: pyVmomi.vim.VirtualMachine
      vmState: str

   class StoragePolicy(pyVmomi.vmodl.DynamicData):
      pass

   class VsanStoragePolicy(StoragePolicy):
      profileId: str

   class SslTrust(pyVmomi.vmodl.DynamicData):
      pass

   class PinnedPemCertificate(SslTrust):
      sslCertificate: str

   class AnyCertificate(SslTrust):
      pass

   class ConfigInfo(pyVmomi.vmodl.DynamicData):
      class OvfDiskProvisioning(pyVmomi.VmomiSupport.Enum):
         none: _typing.ClassVar['OvfDiskProvisioning'] = 'none'
         thin: _typing.ClassVar['OvfDiskProvisioning'] = 'thin'
         thick: _typing.ClassVar['OvfDiskProvisioning'] = 'thick'

      class AuthenticationScheme(pyVmomi.VmomiSupport.Enum):
         NONE: _typing.ClassVar['AuthenticationScheme'] = 'NONE'
         VMWARE_SESSION_ID: _typing.ClassVar['AuthenticationScheme'] = 'VMWARE_SESSION_ID'

      productLineId: _typing.Optional[str] = None
      hostVersion: _typing.Optional[str] = None
      ovfPackageUrl: _typing.Optional[str] = None
      authenticationScheme: _typing.Optional[str] = None
      ovfSslTrust: _typing.Optional[SslTrust] = None
      ovfEnvironment: _typing.Optional[OvfEnvironmentInfo] = None
      vibUrl: _typing.Optional[str] = None
      vibSslTrust: _typing.Optional[SslTrust] = None
      vibMatchingRules: list[VibMatchingRule] = []
      vibName: _typing.Optional[str] = None
      dvFilterEnabled: _typing.Optional[bool] = None
      rebootHostAfterVibUninstall: _typing.Optional[bool] = None
      vmciService: list[str] = []
      ovfDiskProvisioning: _typing.Optional[str] = None
      vmStoragePolicies: list[StoragePolicy] = []
      vmResourceConfiguration: _typing.Optional[str] = None

   class OvfEnvironmentInfo(pyVmomi.vmodl.DynamicData):
      class OvfProperty(pyVmomi.vmodl.DynamicData):
         key: str
         value: str

      ovfProperty: list[OvfProperty] = []

   class VibMatchingRule(pyVmomi.vmodl.DynamicData):
      vibNameRegex: str
      vibVersionRegex: str

   @property
   def runtime(self) -> RuntimeInfo: ...
   @property
   def config(self) -> ConfigInfo: ...

   def QueryRuntime(self) -> RuntimeInfo: ...
   def MarkAsAvailable(self) -> None: ...
   def QueryConfig(self) -> ConfigInfo: ...


class EamObject(pyVmomi.VmomiSupport.ManagedObject):
   class RuntimeInfo(pyVmomi.vmodl.DynamicData):
      class Status(pyVmomi.VmomiSupport.Enum):
         green: _typing.ClassVar['Status'] = 'green'
         yellow: _typing.ClassVar['Status'] = 'yellow'
         red: _typing.ClassVar['Status'] = 'red'

      class GoalState(pyVmomi.VmomiSupport.Enum):
         enabled: _typing.ClassVar['GoalState'] = 'enabled'
         disabled: _typing.ClassVar['GoalState'] = 'disabled'
         uninstalled: _typing.ClassVar['GoalState'] = 'uninstalled'

      status: str
      issue: list[pyVmomi.eam.issue.Issue] = []
      goalState: str
      entity: EamObject

   def Resolve(self, issueKey: list[int]) -> list[int]: ...
   def ResolveAll(self) -> None: ...
   def QueryIssue(self, issueKey: list[int]) -> list[pyVmomi.eam.issue.Issue]: ...


class EsxAgentManager(EamObject):
   class MaintenanceModePolicy(pyVmomi.VmomiSupport.Enum):
      singleHost: _typing.ClassVar['MaintenanceModePolicy'] = 'singleHost'
      multipleHosts: _typing.ClassVar['MaintenanceModePolicy'] = 'multipleHosts'

   @property
   def agency(self) -> list[Agency]: ...
   @property
   def issue(self) -> list[pyVmomi.eam.issue.Issue]: ...

   def QueryAgency(self) -> list[Agency]: ...
   def CreateAgency(self, agencyConfigInfo: Agency.ConfigInfo, initialGoalState: str) -> Agency: ...
   def ScanForUnknownAgentVm(self) -> None: ...
   def SetMaintenanceModePolicy(self, policy: str) -> None: ...
   def GetMaintenanceModePolicy(self) -> str: ...


class Task(pyVmomi.VmomiSupport.ManagedObject):
   pass
