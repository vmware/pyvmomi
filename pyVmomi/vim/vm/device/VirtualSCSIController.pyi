# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.vm.device import VirtualController

class VirtualSCSIController(VirtualController):
   class Sharing(Enum):
      noSharing: ClassVar['Sharing'] = 'noSharing'
      virtualSharing: ClassVar['Sharing'] = 'virtualSharing'
      physicalSharing: ClassVar['Sharing'] = 'physicalSharing'

   hotAddRemove: Optional[bool] = None
   sharedBus: Sharing
   scsiCtlrUnitNumber: Optional[int] = None
