# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vm.device.VirtualController import VirtualController

from pyVmomi.vim.vm.device.VirtualDevice import VirtualDevice

class VirtualUSBController(VirtualController):
   class PciBusSlotInfo(VirtualDevice.PciBusSlotInfo):
      ehciPciSlotNumber: Optional[int] = None

   autoConnectDevices: Optional[bool] = None
   ehciEnabled: Optional[bool] = None
