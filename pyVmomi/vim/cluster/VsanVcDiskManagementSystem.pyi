# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ClusterComputeResource import ClusterComputeResource

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.Task import Task

from pyVmomi.vim.host.MaintenanceSpec import MaintenanceSpec

from pyVmomi.vim.host.ScsiDisk import ScsiDisk

from pyVmomi.vim.vsan.DataEfficiencyCapacityState import DataEfficiencyCapacityState

from pyVmomi.vim.vsan.host.AddStoragePoolDiskSpec import AddStoragePoolDiskSpec

from pyVmomi.vim.vsan.host.DeleteStoragePoolDiskSpec import DeleteStoragePoolDiskSpec

from pyVmomi.vim.vsan.host.DiskMapInfoEx import DiskMapInfoEx

from pyVmomi.vim.vsan.host.DiskMapping import DiskMapping

from pyVmomi.vim.vsan.host.DiskMappingCreationSpec import DiskMappingCreationSpec

from pyVmomi.vim.vsan.host.QueryVsanDisksSpec import QueryVsanDisksSpec

from pyVmomi.vim.vsan.host.VsanHostCapability import VsanHostCapability

from pyVmomi.vim.vsan.host.VsanManagedDisksInfo import VsanManagedDisksInfo

class VsanVcDiskManagementSystem(ManagedObject):
   def RetrieveAllFlashCapabilities(self, cluster: ClusterComputeResource) -> list[VsanHostCapability]: ...
   def InitializeDiskMappings(self, spec: DiskMappingCreationSpec) -> Task: ...
   def QueryDiskMappings(self, host: HostSystem) -> list[DiskMapInfoEx]: ...
   def QueryVsanManagedDisks(self, host: HostSystem, filterSpec: Optional[QueryVsanDisksSpec]) -> Optional[VsanManagedDisksInfo]: ...
   def QueryClusterDataEfficiencyCapacityState(self, cluster: ClusterComputeResource) -> DataEfficiencyCapacityState: ...
   def RebuildDiskMapping(self, host: HostSystem, mapping: DiskMapping, maintenanceSpec: MaintenanceSpec) -> Task: ...
   def UnmountDiskMappingEx(self, cluster: ClusterComputeResource, mappings: list[DiskMapping], maintenanceSpec: MaintenanceSpec) -> Task: ...
   def RemoveDiskMappingEx(self, cluster: ClusterComputeResource, mappings: list[DiskMapping], maintenanceSpec: MaintenanceSpec) -> Task: ...
   def RemoveDiskEx(self, cluster: ClusterComputeResource, disks: list[ScsiDisk], maintenanceSpec: MaintenanceSpec) -> Task: ...
   def AddStoragePoolDisks(self, specs: list[AddStoragePoolDiskSpec]) -> Task: ...
   def DeleteStoragePoolDisk(self, cluster: ClusterComputeResource, spec: DeleteStoragePoolDiskSpec) -> Task: ...
   def UnmountStoragePoolDisks(self, cluster: ClusterComputeResource, spec: DeleteStoragePoolDiskSpec) -> Task: ...
