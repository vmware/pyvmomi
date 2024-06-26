# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.fault import VimFault

class HostIncompatibleForRecordReplay(VimFault):
   class Reason(Enum):
      product: ClassVar['Reason'] = 'product'
      processor: ClassVar['Reason'] = 'processor'

   hostName: Optional[str] = None
   reason: Optional[str] = None
