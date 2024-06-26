# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import VsanConfigGeneration

from pyVmomi.vim.vsan import RepairTimerInfo
from pyVmomi.vim.vsan import ResyncIopsInfo

class RuntimeStats(DynamicData):
   resyncIopsInfo: Optional[ResyncIopsInfo] = None
   configGeneration: Optional[VsanConfigGeneration] = None
   supportedClusterSize: Optional[int] = None
   repairTimerInfo: Optional[RepairTimerInfo] = None
   componentLimitPerCluster: Optional[int] = None
   maxWitnessClusters: Optional[int] = None
