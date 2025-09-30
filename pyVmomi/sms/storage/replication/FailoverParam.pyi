# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Datastore import Datastore

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.sms.storage.replication.DeviceId import DeviceId

from pyVmomi.sms.storage.replication.PointInTimeReplicaId import PointInTimeReplicaId

from pyVmomi.vim.vm.replication.ReplicationGroupId import ReplicationGroupId

class FailoverParam(DynamicData):
   class ReplicationGroupData(DynamicData):
      groupId: ReplicationGroupId
      pitId: Optional[PointInTimeReplicaId] = None

   class PolicyAssociation(DynamicData):
      id: DeviceId
      policyId: str
      datastore: Datastore

   isPlanned: bool
   checkOnly: bool
   replicationGroupsToFailover: list[ReplicationGroupData] = []
   policyAssociations: list[PolicyAssociation] = []
