# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ExtensibleManagedObject import ExtensibleManagedObject

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.HttpNfcLease import HttpNfcLease

from pyVmomi.vim.Task import Task

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vim.vm.ConfigInfo import ConfigInfo

class Snapshot(ExtensibleManagedObject):
   @property
   def config(self) -> ConfigInfo: ...
   @property
   def childSnapshot(self) -> list[Snapshot]: ...
   @property
   def vm(self) -> VirtualMachine: ...

   def Revert(self, host: Optional[HostSystem], suppressPowerOn: Optional[bool]) -> Task: ...
   def Remove(self, removeChildren: bool, consolidate: Optional[bool]) -> Task: ...
   def Rename(self, name: Optional[str], description: Optional[str]) -> None: ...
   def ExportSnapshot(self) -> HttpNfcLease: ...
