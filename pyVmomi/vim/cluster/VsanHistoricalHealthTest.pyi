# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.VsanClusterHealthResultBase import VsanClusterHealthResultBase

from pyVmomi.vim.cluster.VsanHealthCorrelation import VsanHealthCorrelation

class VsanHistoricalHealthTest(DynamicData):
   timestamp: datetime
   health: str
   testDetails: list[VsanClusterHealthResultBase] = []
   testCorrelation: Optional[VsanHealthCorrelation] = None
