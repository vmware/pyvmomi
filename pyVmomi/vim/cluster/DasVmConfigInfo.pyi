# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import DasVmSettings

class DasVmConfigInfo(DynamicData):
   class Priority(Enum):
      disabled: ClassVar['Priority'] = 'disabled'
      low: ClassVar['Priority'] = 'low'
      medium: ClassVar['Priority'] = 'medium'
      high: ClassVar['Priority'] = 'high'

   key: VirtualMachine
   restartPriority: Optional[Priority] = None
   powerOffOnIsolation: Optional[bool] = None
   dasSettings: Optional[DasVmSettings] = None
