# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import CapacityReservationInfo
from pyVmomi.vim.vsan import ProactiveRebalanceInfo

class VsanExtendedConfig(DynamicData):
   objectRepairTimer: Optional[long] = None
   disableSiteReadLocality: Optional[bool] = None
   enableCustomizedSwapObject: Optional[bool] = None
   largeScaleClusterSupport: Optional[bool] = None
   proactiveRebalanceInfo: Optional[ProactiveRebalanceInfo] = None
   capacityReservationInfo: Optional[CapacityReservationInfo] = None
