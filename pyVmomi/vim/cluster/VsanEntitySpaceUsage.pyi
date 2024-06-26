# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanObjectSpaceSummary

from pyVmomi.vim.vsan import DataEfficiencyCapacityState

class VsanEntitySpaceUsage(DynamicData):
   entityId: Optional[str] = None
   spaceUsageByObjectType: list[VsanObjectSpaceSummary] = []
   totalCapacityB: Optional[long] = None
   freeCapacityB: Optional[long] = None
   efficientCapacity: Optional[DataEfficiencyCapacityState] = None
