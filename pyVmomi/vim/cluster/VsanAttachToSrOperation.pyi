# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

class VsanAttachToSrOperation(DynamicData):
   task: Optional[Task] = None
   success: Optional[bool] = None
   timestamp: Optional[datetime] = None
   srNumber: str
