# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vsan.DiskResourceCheckResult import DiskResourceCheckResult

from pyVmomi.vim.vsan.EntityResourceCheckDetails import EntityResourceCheckDetails

class DiskGroupResourceCheckResult(EntityResourceCheckDetails):
   cacheTierDisk: Optional[DiskResourceCheckResult] = None
   capacityTierDisks: list[DiskResourceCheckResult] = []
