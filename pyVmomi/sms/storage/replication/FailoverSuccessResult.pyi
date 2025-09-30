# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.sms.storage.replication.DeviceId import DeviceId

from pyVmomi.sms.storage.replication.GroupOperationResult import GroupOperationResult

from pyVmomi.sms.storage.replication.PointInTimeReplicaId import PointInTimeReplicaId

from pyVmomi.sms.storage.replication.ReplicaId import ReplicaId

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
