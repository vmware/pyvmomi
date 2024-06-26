# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.vm.device import VirtualDiskId

class DrsFaults(DynamicData):
   class FaultsByVm(DynamicData):
      vm: Optional[VirtualMachine] = None
      fault: list[MethodFault] = []

   class FaultsByVirtualDisk(FaultsByVm):
      disk: Optional[VirtualDiskId] = None

   reason: str
   faultsByVm: list[FaultsByVm] = []
