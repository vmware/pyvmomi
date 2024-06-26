# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class SharesInfo(DynamicData):
   class Level(Enum):
      low: ClassVar['Level'] = 'low'
      normal: ClassVar['Level'] = 'normal'
      high: ClassVar['Level'] = 'high'
      custom: ClassVar['Level'] = 'custom'

   shares: int
   level: Level
