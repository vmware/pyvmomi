# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.vm.device import VirtualDevice

class VirtualVideoCard(VirtualDevice):
   class Use3dRenderer(Enum):
      automatic: ClassVar['Use3dRenderer'] = 'automatic'
      software: ClassVar['Use3dRenderer'] = 'software'
      hardware: ClassVar['Use3dRenderer'] = 'hardware'

   videoRamSizeInKB: Optional[long] = None
   numDisplays: Optional[int] = None
   useAutoDetect: Optional[bool] = None
   enable3DSupport: Optional[bool] = None
   use3dRenderer: Optional[str] = None
   graphicsMemorySizeInKB: Optional[long] = None
