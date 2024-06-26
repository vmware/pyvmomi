# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vm import TargetInfo

class DynamicPassthroughInfo(TargetInfo):
   vendorName: str
   deviceName: str
   customLabel: Optional[str] = None
   vendorId: int
   deviceId: int
