# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vmodl import DynamicData
from pyVmomi.vmodl import MethodFault

from pyVmomi.vim.host import ScsiDisk

class DiskResult(DynamicData):
   class State(Enum):
      inUse: ClassVar['State'] = 'inUse'
      eligible: ClassVar['State'] = 'eligible'
      ineligible: ClassVar['State'] = 'ineligible'

   disk: ScsiDisk
   state: str
   vsanUuid: Optional[str] = None
   error: Optional[MethodFault] = None
   degraded: Optional[bool] = None
