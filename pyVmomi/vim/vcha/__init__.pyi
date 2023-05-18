from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from pyVmomi.VmomiSupport import ManagedMethod, ManagedObject


class FailoverClusterConfigurator(ManagedObject):
    @property
    def disabledConfigureMethod(self) -> List[ManagedMethod]: ...
    def Prepare(self, networkSpec: FailoverClusterConfigurator.VchaClusterNetworkSpec) -> vim.Task: ...
    def Deploy(self, deploymentSpec: FailoverClusterConfigurator.VchaClusterDeploymentSpec) -> vim.Task: ...
    def Configure(self, configSpec: FailoverClusterConfigurator.VchaClusterConfigSpec) -> vim.Task: ...
    def CreatePassiveNode(self, passiveDeploymentSpec: FailoverClusterConfigurator.PassiveNodeDeploymentSpec, sourceVcSpec: FailoverClusterConfigurator.SourceNodeSpec) -> vim.Task: ...
    def CreateWitnessNode(self, witnessDeploymentSpec: FailoverClusterConfigurator.NodeDeploymentSpec, sourceVcSpec: FailoverClusterConfigurator.SourceNodeSpec) -> vim.Task: ...
    def GetConfig(self) -> FailoverClusterConfigurator.VchaClusterConfigInfo: ...
    def Destroy(self) -> vim.Task: ...


    class ClusterNetworkConfigSpec(vmodl.DynamicData):
        @property
        def networkPortGroup(self) -> vim.Network: ...
        @property
        def ipSettings(self) -> vim.vm.customization.IPSettings: ...


    class FailoverNodeInfo(vmodl.DynamicData):
        @property
        def clusterIpSettings(self) -> vim.vm.customization.IPSettings: ...
        @property
        def failoverIp(self) -> vim.vm.customization.IPSettings: ...
        @property
        def biosUuid(self) -> str: ...


    class NodeDeploymentSpec(vmodl.DynamicData):
        @property
        def esxHost(self) -> vim.HostSystem: ...
        @property
        def datastore(self) -> vim.Datastore: ...
        @property
        def publicNetworkPortGroup(self) -> vim.Network: ...
        @property
        def clusterNetworkPortGroup(self) -> vim.Network: ...
        @property
        def folder(self) -> vim.Folder: ...
        @property
        def resourcePool(self) -> vim.ResourcePool: ...
        @property
        def managementVc(self) -> vim.ServiceLocator: ...
        @property
        def nodeName(self) -> str: ...
        @property
        def ipSettings(self) -> vim.vm.customization.IPSettings: ...


    class NodeNetworkSpec(vmodl.DynamicData):
        @property
        def ipSettings(self) -> vim.vm.customization.IPSettings: ...


    class PassiveNodeDeploymentSpec(FailoverClusterConfigurator.NodeDeploymentSpec):
        @property
        def failoverIpSettings(self) -> vim.vm.customization.IPSettings: ...


    class PassiveNodeNetworkSpec(FailoverClusterConfigurator.NodeNetworkSpec):
        @property
        def failoverIpSettings(self) -> vim.vm.customization.IPSettings: ...


    class SourceNodeSpec(vmodl.DynamicData):
        @property
        def managementVc(self) -> vim.ServiceLocator: ...
        @property
        def activeVc(self) -> vim.VirtualMachine: ...


    class VchaClusterConfigInfo(vmodl.DynamicData):
        @property
        def failoverNodeInfo1(self) -> FailoverClusterConfigurator.FailoverNodeInfo: ...
        @property
        def failoverNodeInfo2(self) -> FailoverClusterConfigurator.FailoverNodeInfo: ...
        @property
        def witnessNodeInfo(self) -> FailoverClusterConfigurator.WitnessNodeInfo: ...
        @property
        def state(self) -> str: ...


    class VchaClusterConfigSpec(vmodl.DynamicData):
        @property
        def passiveIp(self) -> str: ...
        @property
        def witnessIp(self) -> str: ...


    class VchaClusterDeploymentSpec(vmodl.DynamicData):
        @property
        def passiveDeploymentSpec(self) -> FailoverClusterConfigurator.PassiveNodeDeploymentSpec: ...
        @property
        def witnessDeploymentSpec(self) -> FailoverClusterConfigurator.NodeDeploymentSpec: ...
        @property
        def activeVcSpec(self) -> FailoverClusterConfigurator.SourceNodeSpec: ...
        @property
        def activeVcNetworkConfig(self) -> FailoverClusterConfigurator.ClusterNetworkConfigSpec: ...


    class VchaClusterNetworkSpec(vmodl.DynamicData):
        @property
        def witnessNetworkSpec(self) -> FailoverClusterConfigurator.NodeNetworkSpec: ...
        @property
        def passiveNetworkSpec(self) -> FailoverClusterConfigurator.PassiveNodeNetworkSpec: ...


    class WitnessNodeInfo(vmodl.DynamicData):
        @property
        def ipSettings(self) -> vim.vm.customization.IPSettings: ...
        @property
        def biosUuid(self) -> str: ...


    class VchaState(Enum):
        configured = "configured"
        notConfigured = "notConfigured"
        invalid = "invalid"
        prepared = "prepared"


class FailoverClusterManager(ManagedObject):
    @property
    def disabledClusterMethod(self) -> List[ManagedMethod]: ...
    def SetClusterMode(self, mode: str) -> vim.Task: ...
    def GetClusterMode(self) -> str: ...
    def GetClusterHealth(self) -> FailoverClusterManager.VchaClusterHealth: ...
    def InitiateFailover(self, planned: bool) -> vim.Task: ...


    class VchaClusterHealth(vmodl.DynamicData):
        @property
        def runtimeInfo(self) -> FailoverClusterManager.VchaClusterRuntimeInfo: ...
        @property
        def healthMessages(self) -> List[vmodl.LocalizableMessage]: ...
        @property
        def additionalInformation(self) -> List[vmodl.LocalizableMessage]: ...


    class VchaClusterRuntimeInfo(vmodl.DynamicData):
        @property
        def clusterState(self) -> str: ...
        @property
        def nodeInfo(self) -> List[FailoverClusterManager.VchaNodeRuntimeInfo]: ...
        @property
        def clusterMode(self) -> str: ...


    class VchaNodeRuntimeInfo(vmodl.DynamicData):
        @property
        def nodeState(self) -> str: ...
        @property
        def nodeRole(self) -> str: ...
        @property
        def nodeIp(self) -> str: ...


    class VchaClusterMode(Enum):
        enabled = "enabled"
        disabled = "disabled"
        maintenance = "maintenance"


    class VchaClusterState(Enum):
        healthy = "healthy"
        degraded = "degraded"
        isolated = "isolated"


    class VchaNodeRole(Enum):
        active = "active"
        passive = "passive"
        witness = "witness"


    class VchaNodeState(Enum):
        up = "up"
        down = "down"