# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class SevInfo(DynamicData):
   class SevState(Enum):
      uninitialized: ClassVar['SevState'] = 'uninitialized'
      initialized: ClassVar['SevState'] = 'initialized'
      working: ClassVar['SevState'] = 'working'

   sevState: str
   maxSevEsGuests: long
