# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.KeyAnyValue import KeyAnyValue

from pyVmomi.vim.vsan.IOLatencyMetrics import IOLatencyMetrics

class IOLatency(DynamicData):
   latencyType: str
   sourceEntityUuid: str
   destEntityUuid: str
   readLatencyStats: IOLatencyMetrics
   writeLatencyStats: IOLatencyMetrics
   detailedInfo: list[KeyAnyValue] = []
