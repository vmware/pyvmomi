# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.Task import Task

from pyVmomi.vim.host.MaintenanceSpec import MaintenanceSpec

from pyVmomi.vim.vsan.host.AbortWipeDiskStatus import AbortWipeDiskStatus

from pyVmomi.vim.vsan.host.AboutInfoEx import AboutInfoEx

from pyVmomi.vim.vsan.host.ClusterStatus import ClusterStatus

from pyVmomi.vim.vsan.host.DiskMapping import DiskMapping

from pyVmomi.vim.vsan.host.DrsStats import DrsStats

from pyVmomi.vim.vsan.host.RuntimeStats import RuntimeStats

from pyVmomi.vim.vsan.host.VsanSyncingObjectQueryResult import VsanSyncingObjectQueryResult

from pyVmomi.vim.vsan.host.VsanWhatIfEvacResult import VsanWhatIfEvacResult

from pyVmomi.vim.vsan.host.WipeDiskStatus import WipeDiskStatus

class VsanSystemEx(ManagedObject):
   def QueryWhatIfEvacuationResult(self, evacEntityUuid: str) -> VsanWhatIfEvacResult: ...
   def GetRuntimeStats(self, stats: list[str], clusterUuid: Optional[str]) -> RuntimeStats: ...
   def GetAboutInfoEx(self) -> AboutInfoEx: ...
   def QuerySyncingVsanObjects(self, uuids: list[str], start: Optional[int], limit: Optional[int], includeSummary: Optional[bool]) -> VsanSyncingObjectQueryResult: ...
   def QueryHostDrsStats(self, hostUuids: list[str], vms: list[str], hostIndex: Optional[int]) -> DrsStats: ...
   def UnmountDiskMappingEx(self, mappings: list[DiskMapping], maintenanceSpec: Optional[MaintenanceSpec], timeout: Optional[int], evacReason: Optional[str]) -> Task: ...
   def QueryHostStatusEx(self, clusterUuids: list[str]) -> list[ClusterStatus]: ...
   def WipeDisk(self, disks: list[str]) -> Task: ...
   def QueryWipeDiskStatus(self, disks: list[str]) -> list[WipeDiskStatus]: ...
   def AbortWipeDisk(self, disks: list[str]) -> list[AbortWipeDiskStatus]: ...
