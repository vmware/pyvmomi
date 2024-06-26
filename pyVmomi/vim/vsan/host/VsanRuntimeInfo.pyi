# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan.host import MembershipInfo

class VsanRuntimeInfo(DynamicData):
   class DiskIssueType(Enum):
      nonExist: ClassVar['DiskIssueType'] = 'nonExist'
      stampMismatch: ClassVar['DiskIssueType'] = 'stampMismatch'
      unknown: ClassVar['DiskIssueType'] = 'unknown'

   class DiskIssue(DynamicData):
      diskId: str
      issue: str

   membershipList: list[MembershipInfo] = []
   diskIssues: list[DiskIssue] = []
   accessGenNo: Optional[int] = None
