# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.event import VmEvent

class VmFailedStartingSecondaryEvent(VmEvent):
   class FailureReason(Enum):
      incompatibleHost: ClassVar['FailureReason'] = 'incompatibleHost'
      loginFailed: ClassVar['FailureReason'] = 'loginFailed'
      registerVmFailed: ClassVar['FailureReason'] = 'registerVmFailed'
      migrateFailed: ClassVar['FailureReason'] = 'migrateFailed'

   reason: Optional[str] = None
