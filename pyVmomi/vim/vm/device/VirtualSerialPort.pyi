# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vm.device import VirtualDevice

class VirtualSerialPort(VirtualDevice):
   class FileBackingInfo(VirtualDevice.FileBackingInfo):
      pass

   class DeviceBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class PipeBackingInfo(VirtualDevice.PipeBackingInfo):
      endpoint: str
      noRxLoss: Optional[bool] = None

   class URIBackingInfo(VirtualDevice.URIBackingInfo):
      pass

   class ThinPrintBackingInfo(VirtualDevice.BackingInfo):
      pass

   yieldOnPoll: bool
