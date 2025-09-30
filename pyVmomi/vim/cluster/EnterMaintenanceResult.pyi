# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.cluster.DrsFaults import DrsFaults

from pyVmomi.vim.cluster.Recommendation import Recommendation

class EnterMaintenanceResult(DynamicData):
   recommendations: list[Recommendation] = []
   fault: Optional[DrsFaults] = None
