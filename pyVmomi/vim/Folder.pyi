# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vim.ComputeResource import ComputeResource

from pyVmomi.vim.Datacenter import Datacenter

from pyVmomi.vim.DistributedVirtualSwitch import DistributedVirtualSwitch

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.ResourcePool import ResourcePool

from pyVmomi.vim.StoragePod import StoragePod

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.LocalizableMessage import LocalizableMessage

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.cluster.ConfigSpec import ConfigSpec

from pyVmomi.vim.cluster.ConfigSpecEx import ConfigSpecEx

from pyVmomi.vim.host.ConnectSpec import ConnectSpec

from pyVmomi.vim.vm.ConfigSpec import ConfigSpec

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

   class ExternallyManagedFolderType(Enum):
      PROJECT_ROOT: ClassVar['ExternallyManagedFolderType'] = 'PROJECT_ROOT'
      PROJECT: ClassVar['ExternallyManagedFolderType'] = 'PROJECT'
      VPC_ROOT: ClassVar['ExternallyManagedFolderType'] = 'VPC_ROOT'
      VPC: ClassVar['ExternallyManagedFolderType'] = 'VPC'
      SUBNET: ClassVar['ExternallyManagedFolderType'] = 'SUBNET'
      SEGMENT: ClassVar['ExternallyManagedFolderType'] = 'SEGMENT'
      SUPERVISOR: ClassVar['ExternallyManagedFolderType'] = 'SUPERVISOR'
      VSPHERE_POD: ClassVar['ExternallyManagedFolderType'] = 'VSPHERE_POD'

   class ExternallyManagedFolderInfo(DynamicData):
      id: str
      type: str

   @property
   def childType(self) -> list[type]: ...
   @property
   def childEntity(self) -> list[ManagedEntity]: ...
   @property
   def namespace(self) -> Optional[str]: ...
   @property
   def externallyManagedFolderInfo(self) -> Optional[ExternallyManagedFolderInfo]: ...

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
