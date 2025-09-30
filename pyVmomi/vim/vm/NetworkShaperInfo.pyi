# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

class NetworkShaperInfo(DynamicData):
   enabled: Optional[bool] = None
   peakBps: Optional[long] = None
   averageBps: Optional[long] = None
   burstSize: Optional[long] = None
