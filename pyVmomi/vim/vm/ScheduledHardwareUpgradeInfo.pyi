# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

class ScheduledHardwareUpgradeInfo(DynamicData):
   class HardwareUpgradePolicy(Enum):
      never: ClassVar['HardwareUpgradePolicy'] = 'never'
      onSoftPowerOff: ClassVar['HardwareUpgradePolicy'] = 'onSoftPowerOff'
      always: ClassVar['HardwareUpgradePolicy'] = 'always'

   class HardwareUpgradeStatus(Enum):
      none: ClassVar['HardwareUpgradeStatus'] = 'none'
      pending: ClassVar['HardwareUpgradeStatus'] = 'pending'
      success: ClassVar['HardwareUpgradeStatus'] = 'success'
      failed: ClassVar['HardwareUpgradeStatus'] = 'failed'

   upgradePolicy: Optional[str] = None
   versionKey: Optional[str] = None
   scheduledHardwareUpgradeStatus: Optional[str] = None
   fault: Optional[MethodFault] = None
