# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class SpaceLoadBalanceConfig(DynamicData):
   class SpaceThresholdMode(Enum):
      utilization: ClassVar['SpaceThresholdMode'] = 'utilization'
      freeSpace: ClassVar['SpaceThresholdMode'] = 'freeSpace'

   spaceThresholdMode: Optional[str] = None
   spaceUtilizationThreshold: Optional[int] = None
   freeSpaceThresholdGB: Optional[int] = None
   minSpaceUtilizationDifference: Optional[int] = None
