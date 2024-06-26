# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class NetworkShaperInfo(DynamicData):
   enabled: Optional[bool] = None
   peakBps: Optional[long] = None
   averageBps: Optional[long] = None
   burstSize: Optional[long] = None
