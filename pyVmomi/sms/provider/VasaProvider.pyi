# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.sms import Task

from pyVmomi.sms.provider import AlarmFilter
from pyVmomi.sms.provider import AlarmResult
from pyVmomi.sms.provider import Provider

from pyVmomi.sms.storage.replication import FailoverParam
from pyVmomi.sms.storage.replication import GroupOperationResult
from pyVmomi.sms.storage.replication import PromoteParam
from pyVmomi.sms.storage.replication import QueryPointInTimeReplicaParam
from pyVmomi.sms.storage.replication import QueryReplicationPeerResult
from pyVmomi.sms.storage.replication import TestFailoverParam

from pyVmomi.vim.vm.replication import FaultDomainId
from pyVmomi.vim.vm.replication import ReplicationGroupId

class VasaProvider(Provider):
   def Sync(self, arrayId: Optional[str]) -> Task: ...
   def RefreshCertificate(self) -> Task: ...
   def RevokeCertificate(self) -> Task: ...
   def Reconnect(self) -> Task: ...
   def QueryReplicationPeer(self, faultDomainId: list[FaultDomainId]) -> list[QueryReplicationPeerResult]: ...
   def QueryReplicationGroup(self, groupId: list[ReplicationGroupId]) -> list[GroupOperationResult]: ...
   def QueryPointInTimeReplica(self, groupId: list[ReplicationGroupId], queryParam: Optional[QueryPointInTimeReplicaParam]) -> list[GroupOperationResult]: ...
   def TestFailoverReplicationGroupStart(self, testFailoverParam: TestFailoverParam) -> Task: ...
   def TestFailoverReplicationGroupStop(self, groupId: list[ReplicationGroupId], force: bool) -> Task: ...
   def PromoteReplicationGroup(self, promoteParam: PromoteParam) -> Task: ...
   def SyncReplicationGroup(self, groupId: list[ReplicationGroupId], pitName: str) -> Task: ...
   def PrepareFailoverReplicationGroup(self, groupId: list[ReplicationGroupId]) -> Task: ...
   def FailoverReplicationGroup(self, failoverParam: FailoverParam) -> Task: ...
   def ReverseReplicateGroup(self, groupId: list[ReplicationGroupId]) -> Task: ...
   def QueryActiveAlarm(self, alarmFilter: Optional[AlarmFilter]) -> Optional[AlarmResult]: ...