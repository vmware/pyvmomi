# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import HostSystem

from pyVmomi.vim.fault import VimFault

class CannotEnableVmcpForCluster(VimFault):
   class Reason(Enum):
      APDTimeoutDisabled: ClassVar['Reason'] = 'APDTimeoutDisabled'

   host: Optional[HostSystem] = None
   hostName: Optional[str] = None
   reason: Optional[str] = None
