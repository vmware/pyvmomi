# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.option import OptionValue

class DpmConfigInfo(DynamicData):
   class DpmBehavior(Enum):
      manual: ClassVar['DpmBehavior'] = 'manual'
      automated: ClassVar['DpmBehavior'] = 'automated'

   enabled: Optional[bool] = None
   defaultDpmBehavior: Optional[DpmBehavior] = None
   hostPowerActionRate: Optional[int] = None
   option: list[OptionValue] = []
