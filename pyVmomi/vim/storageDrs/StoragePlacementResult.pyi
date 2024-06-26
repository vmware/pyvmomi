# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.cluster import DrsFaults
from pyVmomi.vim.cluster import Recommendation

class StoragePlacementResult(DynamicData):
   recommendations: list[Recommendation] = []
   drsFault: Optional[DrsFaults] = None
   task: Optional[Task] = None
