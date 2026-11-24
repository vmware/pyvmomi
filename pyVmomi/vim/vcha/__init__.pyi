# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.vm.customization



class FailoverClusterConfigurator(pyVmomi.VmomiSupport.ManagedObject):
   class ClusterNetworkConfigSpec(pyVmomi.vmodl.DynamicData):
      networkPortGroup: pyVmomi.vim.Network
      ipSettings: pyVmomi.vim.vm.customization.IPSettings

   class SourceNodeSpec(pyVmomi.vmodl.DynamicData):
      managementVc: pyVmomi.vim.ServiceLocator
      activeVc: pyVmomi.vim.VirtualMachine

   class NodeNetworkSpec(pyVmomi.vmodl.DynamicData):
      ipSettings: pyVmomi.vim.vm.customization.IPSettings

   class PassiveNodeNetworkSpec(NodeNetworkSpec):
      failoverIpSettings: _typing.Optional[pyVmomi.vim.vm.customization.IPSettings] = None

   class VchaClusterNetworkSpec(pyVmomi.vmodl.DynamicData):
      witnessNetworkSpec: NodeNetworkSpec
      passiveNetworkSpec: PassiveNodeNetworkSpec

   class NodeDeploymentSpec(pyVmomi.vmodl.DynamicData):
      esxHost: _typing.Optional[pyVmomi.vim.HostSystem] = None
      datastore: _typing.Optional[pyVmomi.vim.Datastore] = None
      publicNetworkPortGroup: _typing.Optional[pyVmomi.vim.Network] = None
      clusterNetworkPortGroup: _typing.Optional[pyVmomi.vim.Network] = None
      folder: pyVmomi.vim.Folder
      resourcePool: _typing.Optional[pyVmomi.vim.ResourcePool] = None
      managementVc: _typing.Optional[pyVmomi.vim.ServiceLocator] = None
      nodeName: str
      ipSettings: pyVmomi.vim.vm.customization.IPSettings

   class PassiveNodeDeploymentSpec(NodeDeploymentSpec):
      failoverIpSettings: _typing.Optional[pyVmomi.vim.vm.customization.IPSettings] = None

   class VchaClusterConfigSpec(pyVmomi.vmodl.DynamicData):
      passiveIp: str
      witnessIp: str

   class VchaClusterDeploymentSpec(pyVmomi.vmodl.DynamicData):
      passiveDeploymentSpec: PassiveNodeDeploymentSpec
      witnessDeploymentSpec: NodeDeploymentSpec
      activeVcSpec: SourceNodeSpec
      activeVcNetworkConfig: _typing.Optional[ClusterNetworkConfigSpec] = None

   class FailoverNodeInfo(pyVmomi.vmodl.DynamicData):
      clusterIpSettings: pyVmomi.vim.vm.customization.IPSettings
      failoverIp: _typing.Optional[pyVmomi.vim.vm.customization.IPSettings] = None
      biosUuid: _typing.Optional[str] = None

   class WitnessNodeInfo(pyVmomi.vmodl.DynamicData):
      ipSettings: pyVmomi.vim.vm.customization.IPSettings
      biosUuid: _typing.Optional[str] = None

   class VchaState(pyVmomi.VmomiSupport.Enum):
      configured: _typing.ClassVar['VchaState'] = 'configured'
      notConfigured: _typing.ClassVar['VchaState'] = 'notConfigured'
      invalid: _typing.ClassVar['VchaState'] = 'invalid'
      prepared: _typing.ClassVar['VchaState'] = 'prepared'

   class VchaClusterConfigInfo(pyVmomi.vmodl.DynamicData):
      failoverNodeInfo1: _typing.Optional[FailoverNodeInfo] = None
      failoverNodeInfo2: _typing.Optional[FailoverNodeInfo] = None
      witnessNodeInfo: _typing.Optional[WitnessNodeInfo] = None
      state: str

   @property
   def disabledConfigureMethod(self) -> list[pyVmomi.VmomiSupport.ManagedMethod]: ...

   def Prepare(self, networkSpec: VchaClusterNetworkSpec) -> pyVmomi.vim.Task: ...
   def Deploy(self, deploymentSpec: VchaClusterDeploymentSpec) -> pyVmomi.vim.Task: ...
   def Configure(self, configSpec: VchaClusterConfigSpec) -> pyVmomi.vim.Task: ...
   def CreatePassiveNode(self, passiveDeploymentSpec: PassiveNodeDeploymentSpec, sourceVcSpec: SourceNodeSpec) -> pyVmomi.vim.Task: ...
   def CreateWitnessNode(self, witnessDeploymentSpec: NodeDeploymentSpec, sourceVcSpec: SourceNodeSpec) -> pyVmomi.vim.Task: ...
   def GetConfig(self) -> VchaClusterConfigInfo: ...
   def Destroy(self) -> pyVmomi.vim.Task: ...


class FailoverClusterManager(pyVmomi.VmomiSupport.ManagedObject):
   class VchaNodeRole(pyVmomi.VmomiSupport.Enum):
      active: _typing.ClassVar['VchaNodeRole'] = 'active'
      passive: _typing.ClassVar['VchaNodeRole'] = 'passive'
      witness: _typing.ClassVar['VchaNodeRole'] = 'witness'

   class VchaClusterMode(pyVmomi.VmomiSupport.Enum):
      enabled: _typing.ClassVar['VchaClusterMode'] = 'enabled'
      disabled: _typing.ClassVar['VchaClusterMode'] = 'disabled'
      maintenance: _typing.ClassVar['VchaClusterMode'] = 'maintenance'

   class VchaClusterState(pyVmomi.VmomiSupport.Enum):
      healthy: _typing.ClassVar['VchaClusterState'] = 'healthy'
      degraded: _typing.ClassVar['VchaClusterState'] = 'degraded'
      isolated: _typing.ClassVar['VchaClusterState'] = 'isolated'

   class VchaNodeState(pyVmomi.VmomiSupport.Enum):
      up: _typing.ClassVar['VchaNodeState'] = 'up'
      down: _typing.ClassVar['VchaNodeState'] = 'down'

   class VchaNodeRuntimeInfo(pyVmomi.vmodl.DynamicData):
      nodeState: str
      nodeRole: str
      nodeIp: str

   class VchaClusterRuntimeInfo(pyVmomi.vmodl.DynamicData):
      clusterState: str
      nodeInfo: list[VchaNodeRuntimeInfo] = []
      clusterMode: str

   class VchaClusterHealth(pyVmomi.vmodl.DynamicData):
      runtimeInfo: VchaClusterRuntimeInfo
      healthMessages: list[pyVmomi.vmodl.LocalizableMessage] = []
      additionalInformation: list[pyVmomi.vmodl.LocalizableMessage] = []

   @property
   def disabledClusterMethod(self) -> list[pyVmomi.VmomiSupport.ManagedMethod]: ...

   def SetClusterMode(self, mode: str) -> pyVmomi.vim.Task: ...
   def GetClusterMode(self) -> str: ...
   def GetClusterHealth(self) -> VchaClusterHealth: ...
   def InitiateFailover(self, planned: bool) -> pyVmomi.vim.Task: ...
