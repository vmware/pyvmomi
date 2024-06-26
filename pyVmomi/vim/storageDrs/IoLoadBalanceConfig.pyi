# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

class IoLoadBalanceConfig(DynamicData):
   reservablePercentThreshold: Optional[int] = None
   reservableIopsThreshold: Optional[int] = None
   reservableThresholdMode: Optional[str] = None
   ioLatencyThreshold: Optional[int] = None
   ioLoadImbalanceThreshold: Optional[int] = None
