# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class VirtualDeviceSwap(DynamicData):
   class DeviceSwapStatus(Enum):
      none: ClassVar['DeviceSwapStatus'] = 'none'
      scheduled: ClassVar['DeviceSwapStatus'] = 'scheduled'
      inprogress: ClassVar['DeviceSwapStatus'] = 'inprogress'
      failed: ClassVar['DeviceSwapStatus'] = 'failed'
      completed: ClassVar['DeviceSwapStatus'] = 'completed'

   class DeviceSwapInfo(DynamicData):
      enabled: Optional[bool] = None
      applicable: Optional[bool] = None
      status: Optional[str] = None

   lsiToPvscsi: Optional[DeviceSwapInfo] = None
