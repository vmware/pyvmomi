# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vim import Datastore

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.sms.storage.replication import DeviceId
from pyVmomi.sms.storage.replication import GroupOperationResult
from pyVmomi.sms.storage.replication import PointInTimeReplicaId
from pyVmomi.sms.storage.replication import ReplicaId

class FailoverSuccessResult(GroupOperationResult):
   class RecoveredDiskInfo(DynamicData):
      deviceKey: int
      dsUrl: str
      diskPath: str

   class RecoveredDevice(DynamicData):
      targetDeviceId: Optional[ReplicaId] = None
      recoveredDeviceId: Optional[DeviceId] = None
      sourceDeviceId: DeviceId
      info: list[str] = []
      datastore: Datastore
      recoveredDiskInfo: list[RecoveredDiskInfo] = []
      error: Optional[MethodFault] = None
      warnings: list[MethodFault] = []

   newState: str
   pitId: Optional[PointInTimeReplicaId] = None
   pitIdBeforeFailover: Optional[PointInTimeReplicaId] = None
   recoveredDeviceInfo: list[RecoveredDevice] = []
   timeStamp: Optional[datetime] = None
