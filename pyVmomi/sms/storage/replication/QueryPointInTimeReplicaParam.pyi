# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

class QueryPointInTimeReplicaParam(DynamicData):
   class ReplicaQueryIntervalParam(DynamicData):
      fromDate: Optional[datetime] = None
      toDate: Optional[datetime] = None
      number: Optional[int] = None

   replicaTimeQueryParam: Optional[ReplicaQueryIntervalParam] = None
   pitName: Optional[str] = None
   tags: list[str] = []
   preferDetails: Optional[bool] = None
