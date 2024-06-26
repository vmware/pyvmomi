# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.sms.storage.replication import GroupInfo
from pyVmomi.sms.storage.replication import TargetGroupMemberInfo

from pyVmomi.vim.vm.replication import ReplicationGroupId

class TargetGroupInfo(GroupInfo):
   class TargetToSourceInfo(DynamicData):
      sourceGroupId: ReplicationGroupId
      replicationAgreementDescription: Optional[str] = None

   sourceInfo: TargetToSourceInfo
   state: str
   devices: list[TargetGroupMemberInfo] = []
   isPromoteCapable: Optional[bool] = None
   name: Optional[str] = None
