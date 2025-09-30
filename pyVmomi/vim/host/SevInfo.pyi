# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl.DynamicData import DynamicData

class SevInfo(DynamicData):
   class SevState(Enum):
      uninitialized: ClassVar['SevState'] = 'uninitialized'
      initialized: ClassVar['SevState'] = 'initialized'
      working: ClassVar['SevState'] = 'working'
      disabledBios: ClassVar['SevState'] = 'disabledBios'

   sevState: str
   maxSevEsGuests: long
   snpState: Optional[str] = None
   snpSupported: Optional[bool] = None
