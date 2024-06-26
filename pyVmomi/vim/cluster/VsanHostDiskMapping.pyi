# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import HostSystem

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import ScsiDisk

class VsanHostDiskMapping(DynamicData):
   class VsanDiskGroupCreationType(Enum):
      allflash: ClassVar['VsanDiskGroupCreationType'] = 'allflash'
      hybrid: ClassVar['VsanDiskGroupCreationType'] = 'hybrid'
      vsandirect: ClassVar['VsanDiskGroupCreationType'] = 'vsandirect'
      pmem: ClassVar['VsanDiskGroupCreationType'] = 'pmem'
      VsanDiskGroupCreationType_Unknown: ClassVar['VsanDiskGroupCreationType'] = 'VsanDiskGroupCreationType_Unknown'

   host: HostSystem
   cacheDisks: list[ScsiDisk] = []
   capacityDisks: list[ScsiDisk] = []
   type: str
