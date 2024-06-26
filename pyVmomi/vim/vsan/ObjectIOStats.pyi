# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import IODiagnosticsObjectLayout
from pyVmomi.vim.vsan import IOLatency

class ObjectIOStats(DynamicData):
   backingObjectId: str
   ioLatencyStats: list[IOLatency] = []
   objectLayout: IODiagnosticsObjectLayout
