# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.cluster import VsanVcLifecycleCheckResult
from pyVmomi.vim.cluster import VsanVcLifecycleCheckSpec

from pyVmomi.vim.vsan import ConfigInfoEx
from pyVmomi.vim.vsan import ReconfigSpec
from pyVmomi.vim.vsan import RuntimeStatsHostMap

from pyVmomi.vim.vsan.host import DrsStats

class VsanVcClusterConfigSystem(ManagedObject):
   def ReconfigureEx(self, cluster: ClusterComputeResource, vsanReconfigSpec: ReconfigSpec) -> Task: ...
   def GetConfigInfoEx(self, cluster: ClusterComputeResource) -> ConfigInfoEx: ...
   def RekeyEncryptedCluster(self, encryptedCluster: ClusterComputeResource, deepRekey: Optional[bool], allowReducedRedundancy: Optional[bool]) -> Task: ...
   def GetRuntimeStats(self, cluster: ClusterComputeResource, stats: list[str]) -> list[RuntimeStatsHostMap]: ...
   def QueryClusterDrsStats(self, cluster: ClusterComputeResource, vms: list[VirtualMachine]) -> list[DrsStats]: ...
   def ValidateConfigSpec(self, cluster: ClusterComputeResource, vsanReconfigSpec: ReconfigSpec) -> list[ClusterComputeResource.ValidationResultBase]: ...
   def RunLifecycleCheck(self, cluster: ClusterComputeResource, vsanLifecycleCheckSpec: VsanVcLifecycleCheckSpec) -> VsanVcLifecycleCheckResult: ...
   def GetClaimedCapacity(self, cluster: ClusterComputeResource) -> long: ...
