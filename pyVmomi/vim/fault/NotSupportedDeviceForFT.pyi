# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import Optional

from pyVmomi.VmomiSupport import Enum

from pyVmomi.vim import HostSystem
from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.fault import VmFaultToleranceIssue

class NotSupportedDeviceForFT(VmFaultToleranceIssue):
   class DeviceType(Enum):
      virtualVmxnet3: ClassVar['DeviceType'] = 'virtualVmxnet3'
      paraVirtualSCSIController: ClassVar['DeviceType'] = 'paraVirtualSCSIController'

   host: HostSystem
   hostName: Optional[str] = None
   vm: VirtualMachine
   vmName: Optional[str] = None
   deviceType: str
   deviceLabel: Optional[str] = None
