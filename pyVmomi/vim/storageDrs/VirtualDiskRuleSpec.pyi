# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.cluster import RuleInfo

class VirtualDiskRuleSpec(RuleInfo):
   class RuleType(Enum):
      affinity: ClassVar['RuleType'] = 'affinity'
      antiAffinity: ClassVar['RuleType'] = 'antiAffinity'
      disabled: ClassVar['RuleType'] = 'disabled'

   diskRuleType: str
   diskId: list[int] = []
