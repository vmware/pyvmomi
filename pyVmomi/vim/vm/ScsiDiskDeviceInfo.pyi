# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.host.ScsiDisk import ScsiDisk

from pyVmomi.vim.vm.DiskDeviceInfo import DiskDeviceInfo

class ScsiDiskDeviceInfo(DiskDeviceInfo):
   disk: Optional[ScsiDisk] = None
   transportHint: Optional[str] = None
   lunNumber: Optional[int] = None
