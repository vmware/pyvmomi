# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

class SgxInfo(DynamicData):
   class FlcModes(Enum):
      locked: ClassVar['FlcModes'] = 'locked'
      unlocked: ClassVar['FlcModes'] = 'unlocked'

   epcSize: long
   flcMode: Optional[str] = None
   lePubKeyHash: Optional[str] = None
   requireAttestation: Optional[bool] = None
