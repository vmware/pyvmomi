# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vm.device import VirtualDevice

class VirtualUSB(VirtualDevice):
   class USBBackingInfo(VirtualDevice.DeviceBackingInfo):
      pass

   class RemoteHostBackingInfo(VirtualDevice.DeviceBackingInfo):
      hostname: str

   class RemoteClientBackingInfo(VirtualDevice.RemoteDeviceBackingInfo):
      hostname: str

   connected: bool
   vendor: Optional[int] = None
   product: Optional[int] = None
   family: list[str] = []
   speed: list[str] = []
