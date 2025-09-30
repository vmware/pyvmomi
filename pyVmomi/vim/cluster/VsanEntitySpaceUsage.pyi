# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanObjectSpaceSummary import VsanObjectSpaceSummary

from pyVmomi.vim.vsan.DataEfficiencyCapacityState import DataEfficiencyCapacityState

class VsanEntitySpaceUsage(DynamicData):
   entityId: Optional[str] = None
   spaceUsageByObjectType: list[VsanObjectSpaceSummary] = []
   totalCapacityB: Optional[long] = None
   freeCapacityB: Optional[long] = None
   efficientCapacity: Optional[DataEfficiencyCapacityState] = None
