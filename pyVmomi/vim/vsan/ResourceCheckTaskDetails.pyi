# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim import HostSystem
from pyVmomi.vim import Task

from pyVmomi.vmodl import DynamicData

from pyVmomi.vim.host import MaintenanceSpec

class ResourceCheckTaskDetails(DynamicData):
   task: Task
   host: Optional[HostSystem] = None
   hostUuid: Optional[str] = None
   maintenanceSpec: Optional[MaintenanceSpec] = None
