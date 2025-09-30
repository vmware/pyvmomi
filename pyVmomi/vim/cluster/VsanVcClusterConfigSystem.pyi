# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vim.Task import Task

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vim.cluster.VsanVcLifecycleCheckResult import VsanVcLifecycleCheckResult

from pyVmomi.vim.cluster.VsanVcLifecycleCheckSpec import VsanVcLifecycleCheckSpec

from pyVmomi.vim.vsan.ConfigInfoEx import ConfigInfoEx

from pyVmomi.vim.vsan.ReconfigSpec import ReconfigSpec

from pyVmomi.vim.vsan.RuntimeStatsHostMap import RuntimeStatsHostMap

from pyVmomi.vim.vsan.host.DrsStats import DrsStats

class VsanVcClusterConfigSystem(ManagedObject):
   def ReconfigureEx(self, cluster: ClusterComputeResource, vsanReconfigSpec: ReconfigSpec) -> Task: ...
   def GetConfigInfoEx(self, cluster: ClusterComputeResource) -> ConfigInfoEx: ...
   def RekeyEncryptedCluster(self, encryptedCluster: ClusterComputeResource, deepRekey: Optional[bool], allowReducedRedundancy: Optional[bool]) -> Task: ...
   def GetRuntimeStats(self, cluster: ClusterComputeResource, stats: list[str]) -> list[RuntimeStatsHostMap]: ...
   def QueryClusterDrsStats(self, cluster: ClusterComputeResource, vms: list[VirtualMachine]) -> list[DrsStats]: ...
   def ValidateConfigSpec(self, cluster: ClusterComputeResource, vsanReconfigSpec: ReconfigSpec) -> list[ClusterComputeResource.ValidationResultBase]: ...
   def RunLifecycleCheck(self, cluster: ClusterComputeResource, vsanLifecycleCheckSpec: VsanVcLifecycleCheckSpec) -> VsanVcLifecycleCheckResult: ...
   def GetClaimedCapacity(self, cluster: ClusterComputeResource) -> long: ...
