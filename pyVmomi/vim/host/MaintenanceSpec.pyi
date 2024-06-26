# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan.host import DecommissionMode

class MaintenanceSpec(DynamicData):
   class Purpose(Enum):
      hostUpgrade: ClassVar['Purpose'] = 'hostUpgrade'

   vsanMode: Optional[DecommissionMode] = None
   purpose: Optional[str] = None
