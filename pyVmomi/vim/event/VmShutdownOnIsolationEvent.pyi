# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.event.HostEventArgument import HostEventArgument

from pyVmomi.vim.event.VmPoweredOffEvent import VmPoweredOffEvent

class VmShutdownOnIsolationEvent(VmPoweredOffEvent):
   class Operation(Enum):
      shutdown: ClassVar['Operation'] = 'shutdown'
      poweredOff: ClassVar['Operation'] = 'poweredOff'

   isolatedHost: HostEventArgument
   shutdownResult: Optional[str] = None
