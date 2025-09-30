# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

class VsanFileServiceOvfSpec(DynamicData):
   version: Optional[str] = None
   updateTime: Optional[datetime] = None
   task: Optional[Task] = None
