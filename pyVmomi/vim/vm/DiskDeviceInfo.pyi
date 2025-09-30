# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import long

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vim.vm.TargetInfo import TargetInfo

class DiskDeviceInfo(TargetInfo):
   capacity: Optional[long] = None
   vm: list[VirtualMachine] = []
