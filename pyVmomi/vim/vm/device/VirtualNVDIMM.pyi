# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.vm.device import VirtualDevice

class VirtualNVDIMM(VirtualDevice):
   class BackingInfo(VirtualDevice.FileBackingInfo):
      parent: Optional[BackingInfo] = None
      changeId: Optional[str] = None

   capacityInMB: long
   configuredCapacityInMB: Optional[long] = None
