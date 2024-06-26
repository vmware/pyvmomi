# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.sms.storage.replication import GroupOperationResult
from pyVmomi.sms.storage.replication import PointInTimeReplicaId

class QueryPointInTimeReplicaSuccessResult(GroupOperationResult):
   class PointInTimeReplicaInfo(DynamicData):
      id: PointInTimeReplicaId
      pitName: str
      timeStamp: datetime
      tags: list[str] = []

   replicaInfo: list[PointInTimeReplicaInfo] = []
