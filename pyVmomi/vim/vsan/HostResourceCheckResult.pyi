# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.vsan.DiskGroupResourceCheckResult import DiskGroupResourceCheckResult

from pyVmomi.vim.vsan.EntityResourceCheckDetails import EntityResourceCheckDetails

from pyVmomi.vim.vsan.StoragePoolResourceCheckResult import StoragePoolResourceCheckResult

class HostResourceCheckResult(EntityResourceCheckDetails):
   host: Optional[HostSystem] = None
   diskGroups: list[DiskGroupResourceCheckResult] = []
   storagePools: list[StoragePoolResourceCheckResult] = []
