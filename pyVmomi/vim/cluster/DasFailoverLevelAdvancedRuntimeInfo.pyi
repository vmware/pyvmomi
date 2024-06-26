# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem
from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import DasAdvancedRuntimeInfo

class DasFailoverLevelAdvancedRuntimeInfo(DasAdvancedRuntimeInfo):
   class SlotInfo(DynamicData):
      numVcpus: int
      cpuMHz: int
      memoryMB: int

   class HostSlots(DynamicData):
      host: HostSystem
      slots: int

   class VmSlots(DynamicData):
      vm: VirtualMachine
      slots: int

   slotInfo: SlotInfo
   totalSlots: int
   usedSlots: int
   unreservedSlots: int
   totalVms: int
   totalHosts: int
   totalGoodHosts: int
   hostSlots: list[HostSlots] = []
   vmsRequiringMultipleSlots: list[VmSlots] = []
