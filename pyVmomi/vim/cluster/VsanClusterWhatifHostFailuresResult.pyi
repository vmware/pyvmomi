# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import CapacityReservationInfo
from pyVmomi.vim.vsan import VsanHealthThreshold

class VsanClusterWhatifHostFailuresResult(DynamicData):
   numFailures: long
   totalUsedCapacityB: long
   totalCapacityB: long
   totalRcReservationB: long
   totalRcSizeB: long
   usedComponents: long
   totalComponents: long
   componentLimitHealth: Optional[str] = None
   diskFreeSpaceHealth: Optional[str] = None
   rcFreeReservationHealth: Optional[str] = None
   slackSpaceCapRequired: Optional[long] = None
   diskSpaceThreshold: Optional[VsanHealthThreshold] = None
   capacityReservationInfo: Optional[CapacityReservationInfo] = None
