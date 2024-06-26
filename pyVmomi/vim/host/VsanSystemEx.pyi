# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Task

from pyVmomi.vim.host import MaintenanceSpec

from pyVmomi.vim.vsan.host import AbortWipeDiskStatus
from pyVmomi.vim.vsan.host import AboutInfoEx
from pyVmomi.vim.vsan.host import ClusterStatus
from pyVmomi.vim.vsan.host import DiskMapping
from pyVmomi.vim.vsan.host import DrsStats
from pyVmomi.vim.vsan.host import RuntimeStats
from pyVmomi.vim.vsan.host import VsanSyncingObjectQueryResult
from pyVmomi.vim.vsan.host import VsanWhatIfEvacResult
from pyVmomi.vim.vsan.host import WipeDiskStatus

class VsanSystemEx(ManagedObject):
   def QueryWhatIfEvacuationResult(self, evacEntityUuid: str) -> VsanWhatIfEvacResult: ...
   def GetRuntimeStats(self, stats: list[str], clusterUuid: Optional[str]) -> RuntimeStats: ...
   def GetAboutInfoEx(self) -> AboutInfoEx: ...
   def QuerySyncingVsanObjects(self, uuids: list[str], start: Optional[int], limit: Optional[int], includeSummary: Optional[bool]) -> VsanSyncingObjectQueryResult: ...
   def QueryHostDrsStats(self, hostUuids: list[str], vms: list[str]) -> DrsStats: ...
   def UnmountDiskMappingEx(self, mappings: list[DiskMapping], maintenanceSpec: Optional[MaintenanceSpec], timeout: Optional[int], evacReason: Optional[str]) -> Task: ...
   def QueryHostStatusEx(self, clusterUuids: list[str]) -> list[ClusterStatus]: ...
   def WipeDisk(self, disks: list[str]) -> Task: ...
   def QueryWipeDiskStatus(self, disks: list[str]) -> list[WipeDiskStatus]: ...
   def AbortWipeDisk(self, disks: list[str]) -> list[AbortWipeDiskStatus]: ...
