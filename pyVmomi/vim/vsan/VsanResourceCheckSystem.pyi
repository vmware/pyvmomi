# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import Task

from pyVmomi.vim.vsan import ResourceCheckSpec
from pyVmomi.vim.vsan import ResourceCheckStatus

class VsanResourceCheckSystem(ManagedObject):
   def PerformResourceCheck(self, resourceCheckSpec: ResourceCheckSpec, cluster: Optional[ClusterComputeResource]) -> Task: ...
   def GetResourceCheckStatus(self, resourceCheckSpec: Optional[ResourceCheckSpec], cluster: Optional[ClusterComputeResource]) -> ResourceCheckStatus: ...
   def PerformResourceCheckOnHost(self, resourceCheckSpec: ResourceCheckSpec) -> Task: ...
   def CancelResourceCheckOnHost(self) -> bool: ...
