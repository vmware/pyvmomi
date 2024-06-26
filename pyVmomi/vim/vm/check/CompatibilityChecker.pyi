# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import HostSystem
from pyVmomi.vim import ResourcePool
from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.vm import ConfigSpec

class CompatibilityChecker(ManagedObject):
   def CheckCompatibility(self, vm: VirtualMachine, host: Optional[HostSystem], pool: Optional[ResourcePool], testType: list[str]) -> Task: ...
   def CheckVmConfig(self, spec: ConfigSpec, vm: Optional[VirtualMachine], host: Optional[HostSystem], pool: Optional[ResourcePool], testType: list[str]) -> Task: ...
   def CheckPowerOn(self, vm: VirtualMachine, host: Optional[HostSystem], pool: Optional[ResourcePool], testType: list[str]) -> Task: ...
