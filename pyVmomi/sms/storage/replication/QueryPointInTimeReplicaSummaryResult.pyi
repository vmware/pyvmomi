# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.sms.storage.replication.GroupOperationResult import GroupOperationResult

class QueryPointInTimeReplicaSummaryResult(GroupOperationResult):
   class ReplicaIntervalQueryResult(DynamicData):
      fromDate: datetime
      toDate: datetime
      number: int

   intervalResults: list[ReplicaIntervalQueryResult] = []
