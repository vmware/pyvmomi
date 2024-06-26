# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedMethod
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Datastore
from pyVmomi.vim import Folder
from pyVmomi.vim import HostSystem
from pyVmomi.vim import Network
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import ServiceLocator
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm.customization import IPSettings

class FailoverClusterConfigurator(ManagedObject):
   class ClusterNetworkConfigSpec(DynamicData):
      networkPortGroup: Network
      ipSettings: IPSettings

   class SourceNodeSpec(DynamicData):
      managementVc: ServiceLocator
      activeVc: VirtualMachine

   class NodeNetworkSpec(DynamicData):
      ipSettings: IPSettings

   class PassiveNodeNetworkSpec(NodeNetworkSpec):
      failoverIpSettings: Optional[IPSettings] = None

   class VchaClusterNetworkSpec(DynamicData):
      witnessNetworkSpec: NodeNetworkSpec
      passiveNetworkSpec: PassiveNodeNetworkSpec

   class NodeDeploymentSpec(DynamicData):
      esxHost: Optional[HostSystem] = None
      datastore: Optional[Datastore] = None
      publicNetworkPortGroup: Optional[Network] = None
      clusterNetworkPortGroup: Optional[Network] = None
      folder: Folder
      resourcePool: Optional[ResourcePool] = None
      managementVc: Optional[ServiceLocator] = None
      nodeName: str
      ipSettings: IPSettings

   class PassiveNodeDeploymentSpec(NodeDeploymentSpec):
      failoverIpSettings: Optional[IPSettings] = None

   class VchaClusterConfigSpec(DynamicData):
      passiveIp: str
      witnessIp: str

   class VchaClusterDeploymentSpec(DynamicData):
      passiveDeploymentSpec: PassiveNodeDeploymentSpec
      witnessDeploymentSpec: NodeDeploymentSpec
      activeVcSpec: SourceNodeSpec
      activeVcNetworkConfig: Optional[ClusterNetworkConfigSpec] = None

   class FailoverNodeInfo(DynamicData):
      clusterIpSettings: IPSettings
      failoverIp: Optional[IPSettings] = None
      biosUuid: Optional[str] = None

   class WitnessNodeInfo(DynamicData):
      ipSettings: IPSettings
      biosUuid: Optional[str] = None

   class VchaState(Enum):
      configured: ClassVar['VchaState'] = 'configured'
      notConfigured: ClassVar['VchaState'] = 'notConfigured'
      invalid: ClassVar['VchaState'] = 'invalid'
      prepared: ClassVar['VchaState'] = 'prepared'

   class VchaClusterConfigInfo(DynamicData):
      failoverNodeInfo1: Optional[FailoverNodeInfo] = None
      failoverNodeInfo2: Optional[FailoverNodeInfo] = None
      witnessNodeInfo: Optional[WitnessNodeInfo] = None
      state: str

   @property
   def disabledConfigureMethod(self) -> list[ManagedMethod]: ...

   def Prepare(self, networkSpec: VchaClusterNetworkSpec) -> Task: ...
   def Deploy(self, deploymentSpec: VchaClusterDeploymentSpec) -> Task: ...
   def Configure(self, configSpec: VchaClusterConfigSpec) -> Task: ...
   def CreatePassiveNode(self, passiveDeploymentSpec: PassiveNodeDeploymentSpec, sourceVcSpec: SourceNodeSpec) -> Task: ...
   def CreateWitnessNode(self, witnessDeploymentSpec: NodeDeploymentSpec, sourceVcSpec: SourceNodeSpec) -> Task: ...
   def GetConfig(self) -> VchaClusterConfigInfo: ...
   def Destroy(self) -> Task: ...
