# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class UsageSummary(DynamicData):
   totalCpuCapacityMhz: int
   totalMemCapacityMB: int
   cpuReservationMhz: int
   memReservationMB: int
   poweredOffCpuReservationMhz: Optional[int] = None
   poweredOffMemReservationMB: Optional[int] = None
   cpuDemandMhz: int
   memDemandMB: int
   statsGenNumber: long
   cpuEntitledMhz: int
   memEntitledMB: int
   poweredOffVmCount: int
   totalVmCount: int
