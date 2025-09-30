# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.BootDeviceInfo import BootDeviceInfo

class BootDeviceSystem(ManagedObject):
   class BootDevice(DynamicData):
      key: str
      description: str

   def QueryBootDevices(self) -> Optional[BootDeviceInfo]: ...
   def UpdateBootDevice(self, key: str) -> None: ...
