# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class LatencySensitivity(DynamicData):
   class SensitivityLevel(Enum):
      low: ClassVar['SensitivityLevel'] = 'low'
      normal: ClassVar['SensitivityLevel'] = 'normal'
      medium: ClassVar['SensitivityLevel'] = 'medium'
      high: ClassVar['SensitivityLevel'] = 'high'
      custom: ClassVar['SensitivityLevel'] = 'custom'

   level: SensitivityLevel
   sensitivity: Optional[int] = None
