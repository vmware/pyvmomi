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
        @networkPortGroup.setter
        def networkPortGroup(self, value: vim.Network):
            self._networkPortGroup = value
        @property
        def ipSettings(self) -> vim.vm.customization.IPSettings: ...
        @ipSettings.setter
        def ipSettings(self, value: vim.vm.customization.IPSettings):
            self._ipSettings = value


    class FailoverNodeInfo(vmodl.DynamicData):
        @property
        def clusterIpSettings(self) -> vim.vm.customization.IPSettings: ...
        @clusterIpSettings.setter
        def clusterIpSettings(self, value: vim.vm.customization.IPSettings):
            self._clusterIpSettings = value
        @property
        def failoverIp(self) -> vim.vm.customization.IPSettings: ...
        @failoverIp.setter
        def failoverIp(self, value: vim.vm.customization.IPSettings):
            self._failoverIp = value
        @property
        def biosUuid(self) -> str: ...
        @biosUuid.setter
        def biosUuid(self, value: str):
            self._biosUuid = value


    class NodeDeploymentSpec(vmodl.DynamicData):
        @property
        def esxHost(self) -> vim.HostSystem: ...
        @esxHost.setter
        def esxHost(self, value: vim.HostSystem):
            self._esxHost = value
        @property
        def datastore(self) -> vim.Datastore: ...
        @datastore.setter
        def datastore(self, value: vim.Datastore):
            self._datastore = value
        @property
        def publicNetworkPortGroup(self) -> vim.Network: ...
        @publicNetworkPortGroup.setter
        def publicNetworkPortGroup(self, value: vim.Network):
            self._publicNetworkPortGroup = value
        @property
        def clusterNetworkPortGroup(self) -> vim.Network: ...
        @clusterNetworkPortGroup.setter
        def clusterNetworkPortGroup(self, value: vim.Network):
            self._clusterNetworkPortGroup = value
        @property
        def folder(self) -> vim.Folder: ...
        @folder.setter
        def folder(self, value: vim.Folder):
            self._folder = value
        @property
        def resourcePool(self) -> vim.ResourcePool: ...
        @resourcePool.setter
        def resourcePool(self, value: vim.ResourcePool):
            self._resourcePool = value
        @property
        def managementVc(self) -> vim.ServiceLocator: ...
        @managementVc.setter
        def managementVc(self, value: vim.ServiceLocator):
            self._managementVc = value
        @property
        def nodeName(self) -> str: ...
        @nodeName.setter
        def nodeName(self, value: str):
            self._nodeName = value
        @property
        def ipSettings(self) -> vim.vm.customization.IPSettings: ...
        @ipSettings.setter
        def ipSettings(self, value: vim.vm.customization.IPSettings):
            self._ipSettings = value


    class NodeNetworkSpec(vmodl.DynamicData):
        @property
        def ipSettings(self) -> vim.vm.customization.IPSettings: ...
        @ipSettings.setter
        def ipSettings(self, value: vim.vm.customization.IPSettings):
            self._ipSettings = value


    class PassiveNodeDeploymentSpec(FailoverClusterConfigurator.NodeDeploymentSpec):
        @property
        def failoverIpSettings(self) -> vim.vm.customization.IPSettings: ...
        @failoverIpSettings.setter
        def failoverIpSettings(self, value: vim.vm.customization.IPSettings):
            self._failoverIpSettings = value


    class PassiveNodeNetworkSpec(FailoverClusterConfigurator.NodeNetworkSpec):
        @property
        def failoverIpSettings(self) -> vim.vm.customization.IPSettings: ...
        @failoverIpSettings.setter
        def failoverIpSettings(self, value: vim.vm.customization.IPSettings):
            self._failoverIpSettings = value


    class SourceNodeSpec(vmodl.DynamicData):
        @property
        def managementVc(self) -> vim.ServiceLocator: ...
        @managementVc.setter
        def managementVc(self, value: vim.ServiceLocator):
            self._managementVc = value
        @property
        def activeVc(self) -> vim.VirtualMachine: ...
        @activeVc.setter
        def activeVc(self, value: vim.VirtualMachine):
            self._activeVc = value


    class VchaClusterConfigInfo(vmodl.DynamicData):
        @property
        def failoverNodeInfo1(self) -> FailoverClusterConfigurator.FailoverNodeInfo: ...
        @failoverNodeInfo1.setter
        def failoverNodeInfo1(self, value: FailoverClusterConfigurator.FailoverNodeInfo):
            self._failoverNodeInfo1 = value
        @property
        def failoverNodeInfo2(self) -> FailoverClusterConfigurator.FailoverNodeInfo: ...
        @failoverNodeInfo2.setter
        def failoverNodeInfo2(self, value: FailoverClusterConfigurator.FailoverNodeInfo):
            self._failoverNodeInfo2 = value
        @property
        def witnessNodeInfo(self) -> FailoverClusterConfigurator.WitnessNodeInfo: ...
        @witnessNodeInfo.setter
        def witnessNodeInfo(self, value: FailoverClusterConfigurator.WitnessNodeInfo):
            self._witnessNodeInfo = value
        @property
        def state(self) -> str: ...
        @state.setter
        def state(self, value: str):
            self._state = value


    class VchaClusterConfigSpec(vmodl.DynamicData):
        @property
        def passiveIp(self) -> str: ...
        @passiveIp.setter
        def passiveIp(self, value: str):
            self._passiveIp = value
        @property
        def witnessIp(self) -> str: ...
        @witnessIp.setter
        def witnessIp(self, value: str):
            self._witnessIp = value


    class VchaClusterDeploymentSpec(vmodl.DynamicData):
        @property
        def passiveDeploymentSpec(self) -> FailoverClusterConfigurator.PassiveNodeDeploymentSpec: ...
        @passiveDeploymentSpec.setter
        def passiveDeploymentSpec(self, value: FailoverClusterConfigurator.PassiveNodeDeploymentSpec):
            self._passiveDeploymentSpec = value
        @property
        def witnessDeploymentSpec(self) -> FailoverClusterConfigurator.NodeDeploymentSpec: ...
        @witnessDeploymentSpec.setter
        def witnessDeploymentSpec(self, value: FailoverClusterConfigurator.NodeDeploymentSpec):
            self._witnessDeploymentSpec = value
        @property
        def activeVcSpec(self) -> FailoverClusterConfigurator.SourceNodeSpec: ...
        @activeVcSpec.setter
        def activeVcSpec(self, value: FailoverClusterConfigurator.SourceNodeSpec):
            self._activeVcSpec = value
        @property
        def activeVcNetworkConfig(self) -> FailoverClusterConfigurator.ClusterNetworkConfigSpec: ...
        @activeVcNetworkConfig.setter
        def activeVcNetworkConfig(self, value: FailoverClusterConfigurator.ClusterNetworkConfigSpec):
            self._activeVcNetworkConfig = value


    class VchaClusterNetworkSpec(vmodl.DynamicData):
        @property
        def witnessNetworkSpec(self) -> FailoverClusterConfigurator.NodeNetworkSpec: ...
        @witnessNetworkSpec.setter
        def witnessNetworkSpec(self, value: FailoverClusterConfigurator.NodeNetworkSpec):
            self._witnessNetworkSpec = value
        @property
        def passiveNetworkSpec(self) -> FailoverClusterConfigurator.PassiveNodeNetworkSpec: ...
        @passiveNetworkSpec.setter
        def passiveNetworkSpec(self, value: FailoverClusterConfigurator.PassiveNodeNetworkSpec):
            self._passiveNetworkSpec = value


    class WitnessNodeInfo(vmodl.DynamicData):
        @property
        def ipSettings(self) -> vim.vm.customization.IPSettings: ...
        @ipSettings.setter
        def ipSettings(self, value: vim.vm.customization.IPSettings):
            self._ipSettings = value
        @property
        def biosUuid(self) -> str: ...
        @biosUuid.setter
        def biosUuid(self, value: str):
            self._biosUuid = value


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
        @runtimeInfo.setter
        def runtimeInfo(self, value: FailoverClusterManager.VchaClusterRuntimeInfo):
            self._runtimeInfo = value
        @property
        def healthMessages(self) -> List[vmodl.LocalizableMessage]: ...
        @healthMessages.setter
        def healthMessages(self, value: List[vmodl.LocalizableMessage]):
            self._healthMessages = value
        @property
        def additionalInformation(self) -> List[vmodl.LocalizableMessage]: ...
        @additionalInformation.setter
        def additionalInformation(self, value: List[vmodl.LocalizableMessage]):
            self._additionalInformation = value


    class VchaClusterRuntimeInfo(vmodl.DynamicData):
        @property
        def clusterState(self) -> str: ...
        @clusterState.setter
        def clusterState(self, value: str):
            self._clusterState = value
        @property
        def nodeInfo(self) -> List[FailoverClusterManager.VchaNodeRuntimeInfo]: ...
        @nodeInfo.setter
        def nodeInfo(self, value: List[FailoverClusterManager.VchaNodeRuntimeInfo]):
            self._nodeInfo = value
        @property
        def clusterMode(self) -> str: ...
        @clusterMode.setter
        def clusterMode(self, value: str):
            self._clusterMode = value


    class VchaNodeRuntimeInfo(vmodl.DynamicData):
        @property
        def nodeState(self) -> str: ...
        @nodeState.setter
        def nodeState(self, value: str):
            self._nodeState = value
        @property
        def nodeRole(self) -> str: ...
        @nodeRole.setter
        def nodeRole(self, value: str):
            self._nodeRole = value
        @property
        def nodeIp(self) -> str: ...
        @nodeIp.setter
        def nodeIp(self, value: str):
            self._nodeIp = value


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