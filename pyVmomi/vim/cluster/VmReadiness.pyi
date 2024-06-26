# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class VmReadiness(DynamicData):
   class ReadyCondition(Enum):
      none: ClassVar['ReadyCondition'] = 'none'
      poweredOn: ClassVar['ReadyCondition'] = 'poweredOn'
      guestHbStatusGreen: ClassVar['ReadyCondition'] = 'guestHbStatusGreen'
      appHbStatusGreen: ClassVar['ReadyCondition'] = 'appHbStatusGreen'
      useClusterDefault: ClassVar['ReadyCondition'] = 'useClusterDefault'

   readyCondition: Optional[str] = None
   postReadyDelay: Optional[int] = None
