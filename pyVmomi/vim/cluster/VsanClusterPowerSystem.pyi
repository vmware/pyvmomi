# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ComputeResource
from pyVmomi.vim import Task

from pyVmomi.vim.cluster import ClusterPowerContext
from pyVmomi.vim.cluster import PerformClusterPowerActionSpec

class VsanClusterPowerSystem(ManagedObject):
   def PerformClusterPowerAction(self, cluster: ComputeResource, spec: PerformClusterPowerActionSpec) -> Task: ...
   def QueryClusterPowerContext(self, cluster: ComputeResource) -> ClusterPowerContext: ...
   def UpdateClusterPowerStatus(self, cluster: ComputeResource, status: str) -> bool: ...
