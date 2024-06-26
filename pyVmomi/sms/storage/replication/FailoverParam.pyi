# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Datastore

from pyVmomi.vmodl import DynamicData

from pyVmomi.sms.storage.replication import DeviceId
from pyVmomi.sms.storage.replication import PointInTimeReplicaId

from pyVmomi.vim.vm.replication import ReplicationGroupId

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
