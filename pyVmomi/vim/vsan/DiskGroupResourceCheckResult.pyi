# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.vsan import DiskResourceCheckResult
from pyVmomi.vim.vsan import EntityResourceCheckDetails

class DiskGroupResourceCheckResult(EntityResourceCheckDetails):
   cacheTierDisk: Optional[DiskResourceCheckResult] = None
   capacityTierDisks: list[DiskResourceCheckResult] = []
