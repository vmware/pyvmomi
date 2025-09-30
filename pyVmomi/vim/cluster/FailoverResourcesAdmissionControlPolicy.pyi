# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.cluster.DasAdmissionControlPolicy import DasAdmissionControlPolicy

class FailoverResourcesAdmissionControlPolicy(DasAdmissionControlPolicy):
   cpuFailoverResourcesPercent: int
   memoryFailoverResourcesPercent: int
   failoverLevel: Optional[int] = None
   autoComputePercentages: Optional[bool] = None
   pMemFailoverResourcesPercent: Optional[int] = None
   autoComputePMemFailoverResourcesPercent: Optional[bool] = None
