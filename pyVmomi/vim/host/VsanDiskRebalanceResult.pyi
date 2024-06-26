# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class VsanDiskRebalanceResult(DynamicData):
   status: str
   bytesMoving: Optional[long] = None
   remainingBytesToMove: Optional[long] = None
   diskUsage: Optional[float] = None
   maxDiskUsage: Optional[float] = None
   minDiskUsage: Optional[float] = None
   avgDiskUsage: Optional[float] = None
   diskCompUsage: Optional[float] = None
   maxDiskCompUsage: Optional[float] = None
   minDiskCompUsage: Optional[float] = None
   avgDiskCompUsage: Optional[float] = None
