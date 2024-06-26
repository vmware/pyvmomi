# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Task
from pyVmomi.vim import VirtualMachine

from pyVmomi.vim.option import OptionValue

from pyVmomi.vim.vm.customization import Specification

from pyVmomi.vim.vm.guest import GuestAuthentication

class GuestCustomizationManager(ManagedObject):
   def Customize(self, vm: VirtualMachine, auth: GuestAuthentication, spec: Specification, configParams: list[OptionValue]) -> Task: ...
   def StartNetwork(self, vm: VirtualMachine, auth: GuestAuthentication) -> Task: ...
   def AbortCustomization(self, vm: VirtualMachine, auth: GuestAuthentication) -> Task: ...
