# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vmodl.DynamicData import DynamicData

class Network(ManagedEntity):
   class Summary(DynamicData):
      network: Optional[Network] = None
      name: str
      accessible: bool
      ipPoolName: str
      ipPoolId: Optional[int] = None

   @property
   def summary(self) -> Summary: ...
   @property
   def host(self) -> list[HostSystem]: ...
   @property
   def vm(self) -> list[VirtualMachine]: ...

   def DestroyNetwork(self) -> None: ...
