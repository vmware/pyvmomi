# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.sms.storage.replication.GroupInfo import GroupInfo

from pyVmomi.sms.storage.replication.SourceGroupMemberInfo import SourceGroupMemberInfo

from pyVmomi.vim.vm.replication.ReplicationGroupId import ReplicationGroupId

class SourceGroupInfo(GroupInfo):
   class ReplicationTargetInfo(DynamicData):
      targetGroupId: ReplicationGroupId
      replicationAgreementDescription: Optional[str] = None

   name: Optional[str] = None
   description: Optional[str] = None
   state: str
   replica: list[ReplicationTargetInfo] = []
   memberInfo: list[SourceGroupMemberInfo] = []
