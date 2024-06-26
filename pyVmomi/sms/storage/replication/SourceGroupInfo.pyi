# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.sms.storage.replication import GroupInfo
from pyVmomi.sms.storage.replication import SourceGroupMemberInfo

from pyVmomi.vim.vm.replication import ReplicationGroupId

class SourceGroupInfo(GroupInfo):
   class ReplicationTargetInfo(DynamicData):
      targetGroupId: ReplicationGroupId
      replicationAgreementDescription: Optional[str] = None

   name: Optional[str] = None
   description: Optional[str] = None
   state: str
   replica: list[ReplicationTargetInfo] = []
   memberInfo: list[SourceGroupMemberInfo] = []
