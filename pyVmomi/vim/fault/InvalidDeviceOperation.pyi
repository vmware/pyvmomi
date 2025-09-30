# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.fault.InvalidDeviceSpec import InvalidDeviceSpec

from pyVmomi.vim.vm.device.VirtualDeviceSpec import VirtualDeviceSpec

class InvalidDeviceOperation(InvalidDeviceSpec):
   badOp: Optional[VirtualDeviceSpec.Operation] = None
   badFileOp: Optional[VirtualDeviceSpec.FileOperation] = None
