# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.vsan import ResourceCheckComponentResult
from pyVmomi.vim.vsan import ResourceCheckResult
from pyVmomi.vim.vsan import ResourceCheckTaskDetails

class ResourceCheckStatus(DynamicData):
   status: str
   result: Optional[ResourceCheckResult] = None
   task: Optional[ResourceCheckTaskDetails] = None
   parentTask: Optional[ResourceCheckTaskDetails] = None
   componentResults: list[ResourceCheckComponentResult] = []
