# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vm.PciPassthroughInfo import PciPassthroughInfo

from pyVmomi.vim.vm.SriovDevicePoolInfo import SriovDevicePoolInfo

class SriovInfo(PciPassthroughInfo):
   virtualFunction: bool
   pnic: Optional[str] = None
   devicePool: Optional[SriovDevicePoolInfo] = None
