# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanObjectSpaceSummary import VsanObjectSpaceSummary

from pyVmomi.vim.cluster.VsanSpaceUsageDetailResult import VsanSpaceUsageDetailResult

from pyVmomi.vim.cluster.VsanWhatifCapacity import VsanWhatifCapacity

from pyVmomi.vim.vsan.DataEfficiencyCapacityState import DataEfficiencyCapacityState

from pyVmomi.vim.vsan.VsanHealthThreshold import VsanHealthThreshold

from pyVmomi.vim.vsan.VsanSpaceEfficiencyRatio import VsanSpaceEfficiencyRatio

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
