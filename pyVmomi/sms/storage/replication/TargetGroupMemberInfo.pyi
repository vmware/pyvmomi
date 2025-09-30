# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.sms.storage.replication.DeviceId import DeviceId

from pyVmomi.sms.storage.replication.ReplicaId import ReplicaId

class TargetGroupMemberInfo(DynamicData):
   replicaId: ReplicaId
   sourceId: DeviceId
   targetDatastore: Datastore
