# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import IpConfig
from pyVmomi.vim.host import VirtualNic

class VMotionSystem(ExtensibleManagedObject):
   class NetConfig(DynamicData):
      candidateVnic: list[VirtualNic] = []
      selectedVnic: Optional[VirtualNic] = None

   @property
   def netConfig(self) -> Optional[NetConfig]: ...
   @property
   def ipConfig(self) -> Optional[IpConfig]: ...

   def UpdateIpConfig(self, ipConfig: IpConfig) -> NoReturn: ...
   def SelectVnic(self, device: str) -> NoReturn: ...
   def DeselectVnic(self) -> NoReturn: ...
