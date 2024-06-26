# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.eam import Agent
from pyVmomi.eam import EamObject

from pyVmomi.vim import ComputeResource
from pyVmomi.vim import Datacenter
from pyVmomi.vim import Datastore
from pyVmomi.vim import Folder
from pyVmomi.vim import Network
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.eam.issue import Issue

from pyVmomi.vim.vApp import IpPool

class Agency(EamObject):
   class VMResourcePool(DynamicData):
      resourcePoolId: ResourcePool
      computeResourceId: ComputeResource

   class VMFolder(DynamicData):
      folderId: Folder
      datacenterId: Datacenter

   class ConfigInfo(DynamicData):
      agentConfig: list[Agent.ConfigInfo] = []
      scope: Optional[Scope] = None
      manuallyMarkAgentVmAvailableAfterProvisioning: Optional[bool] = None
      manuallyMarkAgentVmAvailableAfterPowerOn: Optional[bool] = None
      optimizedDeploymentEnabled: Optional[bool] = None
      agentName: Optional[str] = None
      agencyName: Optional[str] = None
      useUuidVmName: Optional[bool] = None
      manuallyProvisioned: Optional[bool] = None
      manuallyMonitored: Optional[bool] = None
      bypassVumEnabled: Optional[bool] = None
      agentVmNetwork: list[Network] = []
      agentVmDatastore: list[Datastore] = []
      preferHostConfiguration: Optional[bool] = None
      ipPool: Optional[IpPool] = None
      resourcePools: list[VMResourcePool] = []
      folders: list[VMFolder] = []

   class Scope(DynamicData):
      pass

   class ComputeResourceScope(Scope):
      computeResource: list[ComputeResource] = []

   @property
   def solutionId(self) -> str: ...
   @property
   def owner(self) -> Optional[str]: ...
   @property
   def config(self) -> ConfigInfo: ...
   @property
   def runtime(self) -> EamObject.RuntimeInfo: ...
   @property
   def agent(self) -> list[Agent]: ...

   def QuerySolutionId(self) -> str: ...
   def QueryConfig(self) -> ConfigInfo: ...
   def Update(self, config: ConfigInfo) -> NoReturn: ...
   def QueryRuntime(self) -> EamObject.RuntimeInfo: ...
   def QueryAgent(self) -> list[Agent]: ...
   def RegisterAgentVm(self, agentVm: VirtualMachine) -> Agent: ...
   def UnregisterAgentVm(self, agentVm: VirtualMachine) -> NoReturn: ...
   def Enable(self) -> NoReturn: ...
   def Disable(self) -> NoReturn: ...
   def Uninstall(self) -> NoReturn: ...
   def DestroyAgency(self) -> NoReturn: ...
   def AddIssue(self, issue: Issue) -> Issue: ...
