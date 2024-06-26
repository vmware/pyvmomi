# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class Fru(DynamicData):
   class FruType(Enum):
      undefined: ClassVar['FruType'] = 'undefined'
      board: ClassVar['FruType'] = 'board'
      product: ClassVar['FruType'] = 'product'

   type: str
   partName: str
   partNumber: str
   manufacturer: str
   serialNumber: Optional[str] = None
   mfgTimeStamp: Optional[datetime] = None
