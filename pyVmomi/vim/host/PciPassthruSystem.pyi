# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ExtensibleManagedObject import ExtensibleManagedObject

from pyVmomi.vim.host.PciPassthruConfig import PciPassthruConfig

from pyVmomi.vim.host.PciPassthruInfo import PciPassthruInfo

from pyVmomi.vim.host.SriovDevicePoolInfo import SriovDevicePoolInfo

class PciPassthruSystem(ExtensibleManagedObject):
   @property
   def pciPassthruInfo(self) -> list[PciPassthruInfo]: ...
   @property
   def sriovDevicePoolInfo(self) -> list[SriovDevicePoolInfo]: ...

   def Refresh(self) -> None: ...
   def UpdatePassthruConfig(self, config: list[PciPassthruConfig]) -> None: ...
