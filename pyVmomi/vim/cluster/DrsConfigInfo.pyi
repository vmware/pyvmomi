# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import OptionValue

class DrsConfigInfo(DynamicData):
   class DrsBehavior(Enum):
      manual: ClassVar['DrsBehavior'] = 'manual'
      partiallyAutomated: ClassVar['DrsBehavior'] = 'partiallyAutomated'
      fullyAutomated: ClassVar['DrsBehavior'] = 'fullyAutomated'

   enabled: Optional[bool] = None
   enableVmBehaviorOverrides: Optional[bool] = None
   defaultVmBehavior: Optional[DrsBehavior] = None
   vmotionRate: Optional[int] = None
   scaleDescendantsShares: Optional[str] = None
   option: list[OptionValue] = []
