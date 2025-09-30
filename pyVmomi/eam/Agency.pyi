# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.eam.Agent import Agent

from pyVmomi.eam.EamObject import EamObject

from pyVmomi.vim.ComputeResource import ComputeResource

from pyVmomi.vim.Datacenter import Datacenter

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vim.Folder import Folder

from pyVmomi.vim.Network import Network

from pyVmomi.vim.ResourcePool import ResourcePool

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.eam.issue.Issue import Issue

from pyVmomi.vim.vApp.IpPool import IpPool

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
   def Update(self, config: ConfigInfo) -> None: ...
   def QueryRuntime(self) -> EamObject.RuntimeInfo: ...
   def QueryAgent(self) -> list[Agent]: ...
   def RegisterAgentVm(self, agentVm: VirtualMachine) -> Agent: ...
   def UnregisterAgentVm(self, agentVm: VirtualMachine) -> None: ...
   def Enable(self) -> None: ...
   def Disable(self) -> None: ...
   def Uninstall(self) -> None: ...
   def DestroyAgency(self) -> None: ...
   def AddIssue(self, issue: Issue) -> Issue: ...
