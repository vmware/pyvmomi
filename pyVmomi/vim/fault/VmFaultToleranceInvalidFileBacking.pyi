# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim.fault import VmFaultToleranceIssue

class VmFaultToleranceInvalidFileBacking(VmFaultToleranceIssue):
   class DeviceType(Enum):
      virtualFloppy: ClassVar['DeviceType'] = 'virtualFloppy'
      virtualCdrom: ClassVar['DeviceType'] = 'virtualCdrom'
      virtualSerialPort: ClassVar['DeviceType'] = 'virtualSerialPort'
      virtualParallelPort: ClassVar['DeviceType'] = 'virtualParallelPort'
      virtualDisk: ClassVar['DeviceType'] = 'virtualDisk'

   backingType: Optional[str] = None
   backingFilename: Optional[str] = None
