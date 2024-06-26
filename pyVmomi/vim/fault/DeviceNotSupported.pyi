# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.fault import VirtualHardwareCompatibilityIssue

class DeviceNotSupported(VirtualHardwareCompatibilityIssue):
   class Reason(Enum):
      host: ClassVar['Reason'] = 'host'
      guest: ClassVar['Reason'] = 'guest'
      ft: ClassVar['Reason'] = 'ft'

   device: str
   reason: Optional[str] = None
