# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vim import ClusterComputeResource

from pyVmomi.vmodl import DynamicData

class VsanHistoricalHealthQuerySpec(DynamicData):
   clusters: list[ClusterComputeResource] = []
   start: datetime
   end: Optional[datetime] = None
   testId: Optional[str] = None
   groupId: Optional[str] = None
   includeHealthRemediation: Optional[bool] = None
