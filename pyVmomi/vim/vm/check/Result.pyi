# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.VirtualMachine import VirtualMachine

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vmodl.MethodFault import MethodFault

class Result(DynamicData):
   vm: Optional[VirtualMachine] = None
   host: Optional[HostSystem] = None
   warning: list[MethodFault] = []
   error: list[MethodFault] = []
