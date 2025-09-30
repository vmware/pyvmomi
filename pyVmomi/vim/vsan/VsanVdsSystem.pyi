# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ComputeResource import ComputeResource

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.Task import Task

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vim.dvs.VmwareDistributedVirtualSwitch import VmwareDistributedVirtualSwitch

from pyVmomi.vim.vsan.VsanVdsMigrationPlan import VsanVdsMigrationPlan

class VsanVdsSystem(ManagedObject):
   def VsanVdsGetMigrationPlan(self, cluster: ComputeResource, vswitchName: Optional[str], vdsName: Optional[str], vmnicDevices: list[str], infraVm: list[VirtualMachine], vds: Optional[VmwareDistributedVirtualSwitch], hosts: list[HostSystem]) -> VsanVdsMigrationPlan: ...
   def VsanVdsMigrateVss(self, cluster: ComputeResource, migrationPlan: Optional[VsanVdsMigrationPlan], vswitchName: Optional[str], vdsName: Optional[str], vmnicDevices: list[str], infraVm: list[VirtualMachine], vds: Optional[VmwareDistributedVirtualSwitch], hosts: list[HostSystem]) -> Task: ...
   def VsanVssMigrateVds(self, cluster: Optional[ComputeResource], hosts: list[HostSystem], vds: VmwareDistributedVirtualSwitch, vswitchName: Optional[str], vmnicDevices: list[str], infraVm: list[VirtualMachine]) -> Task: ...
   def RollbackVdsToVss(self, task: Task) -> bool: ...
