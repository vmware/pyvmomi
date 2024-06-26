# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ClusterComputeResource
from pyVmomi.vim import Task

from pyVmomi.vim.vsan import VsanCloudHealthStatus

class VsanPhoneHomeSystem(ManagedObject):
   def VsanPerformOnlineHealthCheck(self, cluster: ClusterComputeResource) -> Task: ...
   def QueryVsanCloudHealthStatus(self) -> Optional[VsanCloudHealthStatus]: ...
   def VsanQueryObjectSnapshotsInfo(self, cluster: ClusterComputeResource) -> Optional[str]: ...
   def VsanQueryNvmeCriticalWarningStats(self, cluster: ClusterComputeResource) -> Optional[str]: ...
   def VsanQueryZdomScrubberData(self, cluster: ClusterComputeResource) -> Optional[str]: ...
   def VsanQueryLSOMwbsize(self, cluster: ClusterComputeResource) -> Optional[str]: ...
