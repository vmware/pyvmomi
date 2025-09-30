# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ExtensibleManagedObject import ExtensibleManagedObject

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.IpConfig import IpConfig

from pyVmomi.vim.host.VirtualNic import VirtualNic

class VMotionSystem(ExtensibleManagedObject):
   class NetConfig(DynamicData):
      candidateVnic: list[VirtualNic] = []
      selectedVnic: Optional[VirtualNic] = None

   @property
   def netConfig(self) -> Optional[NetConfig]: ...
   @property
   def ipConfig(self) -> Optional[IpConfig]: ...

   def UpdateIpConfig(self, ipConfig: IpConfig) -> None: ...
   def SelectVnic(self, device: str) -> None: ...
   def DeselectVnic(self) -> None: ...
