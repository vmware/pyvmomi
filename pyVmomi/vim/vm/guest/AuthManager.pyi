# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vim.vm.guest.GuestAuthentication import GuestAuthentication

class AuthManager(ManagedObject):
   def ValidateCredentials(self, vm: VirtualMachine, auth: GuestAuthentication) -> None: ...
   def AcquireCredentials(self, vm: VirtualMachine, requestedAuth: GuestAuthentication, sessionID: Optional[long]) -> GuestAuthentication: ...
   def ReleaseCredentials(self, vm: VirtualMachine, auth: GuestAuthentication) -> None: ...
