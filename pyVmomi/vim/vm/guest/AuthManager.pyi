# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject
from pyVmomi.VmomiSupport import long

from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.vm.guest import GuestAuthentication

class AuthManager(ManagedObject):
   def ValidateCredentials(self, vm: VirtualMachine, auth: GuestAuthentication) -> NoReturn: ...
   def AcquireCredentials(self, vm: VirtualMachine, requestedAuth: GuestAuthentication, sessionID: Optional[long]) -> GuestAuthentication: ...
   def ReleaseCredentials(self, vm: VirtualMachine, auth: GuestAuthentication) -> NoReturn: ...
