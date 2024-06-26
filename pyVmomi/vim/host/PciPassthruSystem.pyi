# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vim.host import PciPassthruConfig
from pyVmomi.vim.host import PciPassthruInfo
from pyVmomi.vim.host import SriovDevicePoolInfo

class PciPassthruSystem(ExtensibleManagedObject):
   @property
   def pciPassthruInfo(self) -> list[PciPassthruInfo]: ...
   @property
   def sriovDevicePoolInfo(self) -> list[SriovDevicePoolInfo]: ...

   def Refresh(self) -> NoReturn: ...
   def UpdatePassthruConfig(self, config: list[PciPassthruConfig]) -> NoReturn: ...
