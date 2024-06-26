# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import VirtualMachine

from pyVmomi.vmodl import DynamicData

class GraphicsInfo(DynamicData):
   class GraphicsType(Enum):
      basic: ClassVar['GraphicsType'] = 'basic'
      shared: ClassVar['GraphicsType'] = 'shared'
      direct: ClassVar['GraphicsType'] = 'direct'
      sharedDirect: ClassVar['GraphicsType'] = 'sharedDirect'

   class VgpuMode(Enum):
      none: ClassVar['VgpuMode'] = 'none'
      sameSize: ClassVar['VgpuMode'] = 'sameSize'
      mixedSize: ClassVar['VgpuMode'] = 'mixedSize'
      multiInstanceGpu: ClassVar['VgpuMode'] = 'multiInstanceGpu'

   deviceName: str
   vendorName: str
   pciId: str
   graphicsType: str
   vgpuMode: Optional[str] = None
   memorySizeInKB: long
   vm: list[VirtualMachine] = []
