# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

class VsanClusterHealthQuerySpec(DynamicData):
   task: Optional[Task] = None
   diskNames: list[str] = []
   includeHealthRemediation: Optional[bool] = None
