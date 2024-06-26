# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vm.device import VirtualDevice

class VirtualHardware(DynamicData):
   class MotherboardLayout(Enum):
      i440bxHostBridge: ClassVar['MotherboardLayout'] = 'i440bxHostBridge'
      acpiHostBridges: ClassVar['MotherboardLayout'] = 'acpiHostBridges'

   numCPU: int
   numCoresPerSocket: Optional[int] = None
   autoCoresPerSocket: Optional[bool] = None
   memoryMB: int
   virtualICH7MPresent: Optional[bool] = None
   virtualSMCPresent: Optional[bool] = None
   device: list[VirtualDevice] = []
   motherboardLayout: Optional[str] = None
   simultaneousThreads: Optional[int] = None
