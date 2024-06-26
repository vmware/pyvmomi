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

class DiskMappingCreationSpec(DynamicData):
   class DiskMappingCreationType(Enum):
      hybrid: ClassVar['DiskMappingCreationType'] = 'hybrid'
      allFlash: ClassVar['DiskMappingCreationType'] = 'allFlash'
      vsandirect: ClassVar['DiskMappingCreationType'] = 'vsandirect'
      pmem: ClassVar['DiskMappingCreationType'] = 'pmem'
      DiskMappingCreationType_Unknown: ClassVar['DiskMappingCreationType'] = 'DiskMappingCreationType_Unknown'

   host: HostSystem
   cacheDisks: list[ScsiDisk] = []
   capacityDisks: list[ScsiDisk] = []
   creationType: str
