# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ComputeResource import ComputeResource

from pyVmomi.vim.Task import Task

from pyVmomi.vim.cluster.ClusterPowerContext import ClusterPowerContext

from pyVmomi.vim.cluster.PerformClusterPowerActionSpec import PerformClusterPowerActionSpec

class VsanClusterPowerSystem(ManagedObject):
   def PerformClusterPowerAction(self, cluster: ComputeResource, spec: PerformClusterPowerActionSpec) -> Task: ...
   def QueryClusterPowerContext(self, cluster: ComputeResource) -> ClusterPowerContext: ...
   def UpdateClusterPowerStatus(self, cluster: ComputeResource, status: str) -> bool: ...
