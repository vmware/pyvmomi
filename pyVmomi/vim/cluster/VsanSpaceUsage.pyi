# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanObjectSpaceSummary
from pyVmomi.vim.cluster import VsanSpaceUsageDetailResult
from pyVmomi.vim.cluster import VsanWhatifCapacity

from pyVmomi.vim.vsan import DataEfficiencyCapacityState
from pyVmomi.vim.vsan import VsanHealthThreshold
from pyVmomi.vim.vsan import VsanSpaceEfficiencyRatio

class VsanSpaceUsage(DynamicData):
   totalCapacityB: long
   freeCapacityB: Optional[long] = None
   spaceOverview: Optional[VsanObjectSpaceSummary] = None
   spaceDetail: Optional[VsanSpaceUsageDetailResult] = None
   efficientCapacity: Optional[DataEfficiencyCapacityState] = None
   whatifCapacities: list[VsanWhatifCapacity] = []
   uncommittedB: Optional[long] = None
   capacityHealthThreshold: Optional[VsanHealthThreshold] = None
   spaceEfficiencyRatio: Optional[VsanSpaceEfficiencyRatio] = None
