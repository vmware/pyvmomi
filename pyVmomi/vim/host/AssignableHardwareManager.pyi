# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import binary

from pyVmomi.vim.host import AssignableHardwareBinding
from pyVmomi.vim.host import AssignableHardwareConfig

from pyVmomi.vim.vm import DynamicPassthroughInfo
from pyVmomi.vim.vm import VendorDeviceGroupInfo

class AssignableHardwareManager(ManagedObject):
   @property
   def binding(self) -> list[AssignableHardwareBinding]: ...
   @property
   def config(self) -> AssignableHardwareConfig: ...

   def DownloadDescriptionTree(self) -> binary: ...
   def RetrieveDynamicPassthroughInfo(self) -> list[DynamicPassthroughInfo]: ...
   def RetrieveVendorDeviceGroupInfo(self) -> list[VendorDeviceGroupInfo]: ...
   def UpdateConfig(self, config: AssignableHardwareConfig) -> NoReturn: ...
