# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class VsanNetworkLoadTestResult(DynamicData):
   hostname: str
   status: Optional[str] = None
   client: bool
   bandwidthBps: long
   totalBytes: long
   lostDatagrams: Optional[long] = None
   lossPct: Optional[long] = None
   sentDatagrams: Optional[long] = None
   jitterMs: Optional[float] = None
