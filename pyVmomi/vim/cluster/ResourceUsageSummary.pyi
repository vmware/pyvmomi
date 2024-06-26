# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class ResourceUsageSummary(DynamicData):
   cpuUsedMHz: int
   cpuCapacityMHz: int
   memUsedMB: int
   memCapacityMB: int
   pMemAvailableMB: Optional[long] = None
   pMemCapacityMB: Optional[long] = None
   storageUsedMB: long
   storageCapacityMB: long
