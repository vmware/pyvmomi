# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.host.PhysicalNic import PhysicalNic

from pyVmomi.vim.host.SriovDevicePoolInfo import SriovDevicePoolInfo

class SriovNetworkDevicePoolInfo(SriovDevicePoolInfo):
   switchKey: Optional[str] = None
   switchUuid: Optional[str] = None
   pnic: list[PhysicalNic] = []
