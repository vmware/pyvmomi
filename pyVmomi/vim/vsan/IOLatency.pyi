# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import KeyAnyValue

from pyVmomi.vim.vsan import IOLatencyMetrics

class IOLatency(DynamicData):
   latencyType: str
   sourceEntityUuid: str
   destEntityUuid: str
   readLatencyStats: IOLatencyMetrics
   writeLatencyStats: IOLatencyMetrics
   detailedInfo: list[KeyAnyValue] = []
