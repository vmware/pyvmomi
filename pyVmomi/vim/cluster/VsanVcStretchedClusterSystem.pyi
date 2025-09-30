# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.Task import Task

from pyVmomi.vim.cluster.VSANPreferredFaultDomainInfo import VSANPreferredFaultDomainInfo

from pyVmomi.vim.cluster.VSANStretchedClusterCapability import VSANStretchedClusterCapability

from pyVmomi.vim.cluster.VSANStretchedClusterFaultDomainConfig import VSANStretchedClusterFaultDomainConfig

from pyVmomi.vim.cluster.VSANWitnessHostInfo import VSANWitnessHostInfo

from pyVmomi.vim.host.VsanHostVirtualApplianceInfo import VsanHostVirtualApplianceInfo

from pyVmomi.vim.vsan.ClusterRuntimeInfo import ClusterRuntimeInfo

from pyVmomi.vim.vsan.SharedWitnessCompatibilityResult import SharedWitnessCompatibilityResult

from pyVmomi.vim.vsan.VsanVcStretchedClusterConfigSpec import VsanVcStretchedClusterConfigSpec

from pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec import AddStoragePoolDiskSpec

from pyVmomi.vim.vsan.host.DiskMapping import DiskMapping

class VsanVcStretchedClusterSystem(ManagedObject):
   def AddWitnessHost(self, cluster: ClusterComputeResource, witnessHost: HostSystem, preferredFd: str, diskMapping: Optional[DiskMapping], metadataMode: Optional[bool], storagePoolSpec: Optional[AddStoragePoolDiskSpec]) -> Task: ...
   def RemoveWitnessHost(self, cluster: ClusterComputeResource, witnessHost: Optional[HostSystem], witnessAddress: Optional[str]) -> Task: ...
   def ConvertToStretchedCluster(self, cluster: ClusterComputeResource, faultDomainConfig: VSANStretchedClusterFaultDomainConfig, witnessHost: HostSystem, preferredFd: str, diskMapping: Optional[DiskMapping], storagePoolSpec: Optional[AddStoragePoolDiskSpec]) -> Task: ...
   def SetPreferredFaultDomain(self, cluster: ClusterComputeResource, preferredFd: str, witnessHost: Optional[HostSystem]) -> Task: ...
   def GetPreferredFaultDomain(self, cluster: ClusterComputeResource) -> Optional[VSANPreferredFaultDomainInfo]: ...
   def IsWitnessHost(self, host: HostSystem) -> bool: ...
   def GetWitnessHosts(self, cluster: ClusterComputeResource) -> list[VSANWitnessHostInfo]: ...
   def RetrieveStretchedClusterVcCapability(self, cluster: ClusterComputeResource, verifyAllConnected: Optional[bool]) -> list[VSANStretchedClusterCapability]: ...
   def IsWitnessVirtualAppliance(self, hosts: list[HostSystem]) -> list[VsanHostVirtualApplianceInfo]: ...
   def QuerySharedWitnessCompatibility(self, sharedWitnessHost: HostSystem, roboClusters: list[ClusterComputeResource]) -> SharedWitnessCompatibilityResult: ...
   def QueryWitnessHostClusterInfo(self, witnessHost: HostSystem, skipComponentsCount: Optional[bool]) -> list[ClusterRuntimeInfo]: ...
   def ReplaceWitnessHostForClusters(self, configSpec: VsanVcStretchedClusterConfigSpec) -> Task: ...
   def AddWitnessHostForClusters(self, configSpec: VsanVcStretchedClusterConfigSpec) -> Task: ...
