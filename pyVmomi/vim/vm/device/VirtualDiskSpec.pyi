# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vm.device import VirtualDeviceSpec

class VirtualDiskSpec(VirtualDeviceSpec):
   diskMoveType: Optional[str] = None
   migrateCache: Optional[bool] = None
