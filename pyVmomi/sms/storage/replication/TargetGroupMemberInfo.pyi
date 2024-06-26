# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim import Datastore

from pyVmomi.vmodl import DynamicData

from pyVmomi.sms.storage.replication import DeviceId
from pyVmomi.sms.storage.replication import ReplicaId

class TargetGroupMemberInfo(DynamicData):
   replicaId: ReplicaId
   sourceId: DeviceId
   targetDatastore: Datastore
