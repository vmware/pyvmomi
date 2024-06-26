# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vslm import BaseConfigInfo
from pyVmomi.vim.vslm import ID

class VStorageObject(DynamicData):
   class ConsumptionType(Enum):
      disk: ClassVar['ConsumptionType'] = 'disk'

   class ConfigInfo(BaseConfigInfo):
      descriptorVersion: Optional[int] = None
      capacityInMB: long
      consumptionType: list[str] = []
      consumerId: list[ID] = []

   config: ConfigInfo
