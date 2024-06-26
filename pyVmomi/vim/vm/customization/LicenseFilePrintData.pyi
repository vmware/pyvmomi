# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

class LicenseFilePrintData(DynamicData):
   class AutoMode(Enum):
      perServer: ClassVar['AutoMode'] = 'perServer'
      perSeat: ClassVar['AutoMode'] = 'perSeat'

   autoMode: AutoMode
   autoUsers: Optional[int] = None
