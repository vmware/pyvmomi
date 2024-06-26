# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import ComputeResource
from pyVmomi.vim import Datacenter
from pyVmomi.vim import DistributedVirtualSwitch
from pyVmomi.vim import HostSystem
from pyVmomi.vim import ManagedEntity
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import StoragePod
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import LocalizableMessage
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.cluster import ConfigSpec
from pyVmomi.vim.cluster import ConfigSpecEx

from pyVmomi.vim.host import ConnectSpec

from pyVmomi.vim.vm import ConfigSpec

class Folder(ManagedEntity):
   class DesiredHostState(Enum):
      maintenance: ClassVar['DesiredHostState'] = 'maintenance'
      non_maintenance: ClassVar['DesiredHostState'] = 'non_maintenance'

   class NewHostSpec(DynamicData):
      hostCnxSpec: ConnectSpec
      esxLicense: Optional[str] = None

   class FailedHostResult(DynamicData):
      hostName: Optional[str] = None
      host: Optional[HostSystem] = None
      context: LocalizableMessage
      fault: MethodFault

   class BatchAddStandaloneHostsResult(DynamicData):
      addedHosts: list[HostSystem] = []
      hostsFailedInventoryAdd: list[FailedHostResult] = []

   class BatchAddHostsToClusterResult(DynamicData):
      hostsAddedToCluster: list[HostSystem] = []
      hostsFailedInventoryAdd: list[FailedHostResult] = []
      hostsFailedMoveToCluster: list[FailedHostResult] = []

   @property
   def childType(self) -> list[type]: ...
   @property
   def childEntity(self) -> list[ManagedEntity]: ...
   @property
   def namespace(self) -> Optional[str]: ...

   def CreateFolder(self, name: str) -> Folder: ...
   def MoveInto(self, list: list[ManagedEntity]) -> Task: ...
   def CreateVm(self, config: ConfigSpec, pool: ResourcePool, host: Optional[HostSystem]) -> Task: ...
   def RegisterVm(self, path: str, name: Optional[str], asTemplate: bool, pool: Optional[ResourcePool], host: Optional[HostSystem]) -> Task: ...
   def CreateCluster(self, name: str, spec: ConfigSpec) -> ClusterComputeResource: ...
   def CreateClusterEx(self, name: str, spec: ConfigSpecEx) -> ClusterComputeResource: ...
   def AddStandaloneHost(self, spec: ConnectSpec, compResSpec: Optional[ComputeResource.ConfigSpec], addConnected: bool, license: Optional[str]) -> Task: ...
   def CreateDatacenter(self, name: str) -> Datacenter: ...
   def UnregisterAndDestroy(self) -> Task: ...
   def CreateDistributedVirtualSwitch(self, spec: DistributedVirtualSwitch.CreateSpec) -> Task: ...
   def CreateStoragePod(self, name: str) -> StoragePod: ...
   def BatchAddStandaloneHosts(self, newHosts: list[NewHostSpec], compResSpec: Optional[ComputeResource.ConfigSpec], addConnected: bool) -> Task: ...
   def BatchAddHostsToCluster(self, cluster: ClusterComputeResource, newHosts: list[NewHostSpec], existingHosts: list[HostSystem], compResSpec: Optional[ComputeResource.ConfigSpec], desiredState: Optional[str]) -> Task: ...
