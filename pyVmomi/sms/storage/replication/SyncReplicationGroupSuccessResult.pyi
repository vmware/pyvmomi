# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.sms.storage.replication import GroupOperationResult
from pyVmomi.sms.storage.replication import PointInTimeReplicaId

class SyncReplicationGroupSuccessResult(GroupOperationResult):
   timeStamp: datetime
   pitId: Optional[PointInTimeReplicaId] = None
   pitName: Optional[str] = None
