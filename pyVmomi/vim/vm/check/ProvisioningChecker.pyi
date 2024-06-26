# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Folder
from pyVmomi.vim import HostSystem
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.vm import CloneSpec
from pyVmomi.vim.vm import InstantCloneSpec
from pyVmomi.vim.vm import RelocateSpec

class ProvisioningChecker(ManagedObject):
   def QueryVMotionCompatibilityEx(self, vm: list[VirtualMachine], host: list[HostSystem]) -> Task: ...
   def CheckMigrate(self, vm: VirtualMachine, host: Optional[HostSystem], pool: Optional[ResourcePool], state: Optional[VirtualMachine.PowerState], testType: list[str]) -> Task: ...
   def CheckRelocate(self, vm: VirtualMachine, spec: RelocateSpec, testType: list[str]) -> Task: ...
   def CheckClone(self, vm: VirtualMachine, folder: Folder, name: str, spec: CloneSpec, testType: list[str]) -> Task: ...
   def CheckInstantClone(self, vm: VirtualMachine, spec: InstantCloneSpec, testType: list[str]) -> Task: ...
