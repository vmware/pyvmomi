# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.cluster import Action

class HostPowerAction(Action):
   class OperationType(Enum):
      powerOn: ClassVar['OperationType'] = 'powerOn'
      powerOff: ClassVar['OperationType'] = 'powerOff'

   operationType: OperationType
   powerConsumptionWatt: Optional[int] = None
   cpuCapacityMHz: Optional[int] = None
   memCapacityMB: Optional[int] = None
