# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.vm.guest.AliasManager import AliasManager

from pyVmomi.vim.vm.guest.AuthManager import AuthManager

from pyVmomi.vim.vm.guest.FileManager import FileManager

from pyVmomi.vim.vm.guest.ProcessManager import ProcessManager

from pyVmomi.vim.vm.guest.WindowsRegistryManager import WindowsRegistryManager

class GuestOperationsManager(ManagedObject):
   @property
   def authManager(self) -> Optional[AuthManager]: ...
   @property
   def fileManager(self) -> Optional[FileManager]: ...
   @property
   def processManager(self) -> Optional[ProcessManager]: ...
   @property
   def guestWindowsRegistryManager(self) -> Optional[WindowsRegistryManager]: ...
   @property
   def aliasManager(self) -> Optional[AliasManager]: ...
