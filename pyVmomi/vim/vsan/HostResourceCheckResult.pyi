# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem

from pyVmomi.vim.vsan import DiskGroupResourceCheckResult
from pyVmomi.vim.vsan import EntityResourceCheckDetails
from pyVmomi.vim.vsan import StoragePoolResourceCheckResult

class HostResourceCheckResult(EntityResourceCheckDetails):
   host: Optional[HostSystem] = None
   diskGroups: list[DiskGroupResourceCheckResult] = []
   storagePools: list[StoragePoolResourceCheckResult] = []
