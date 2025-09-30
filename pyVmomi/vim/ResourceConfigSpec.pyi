# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.ResourceAllocationInfo import ResourceAllocationInfo

from pyVmomi.vmodl.DynamicData import DynamicData

class ResourceConfigSpec(DynamicData):
   class ScaleSharesBehavior(Enum):
      disabled: ClassVar['ScaleSharesBehavior'] = 'disabled'
      scaleCpuAndMemoryShares: ClassVar['ScaleSharesBehavior'] = 'scaleCpuAndMemoryShares'

   entity: Optional[ManagedEntity] = None
   changeVersion: Optional[str] = None
   lastModified: Optional[datetime] = None
   cpuAllocation: ResourceAllocationInfo
   memoryAllocation: ResourceAllocationInfo
   scaleDescendantsShares: Optional[str] = None
