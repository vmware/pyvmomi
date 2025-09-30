# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.HostSystem import HostSystem

from pyVmomi.vim.Task import Task

from pyVmomi.vmodl.DynamicData import DynamicData

from pyVmomi.vim.host.MaintenanceSpec import MaintenanceSpec

class ResourceCheckTaskDetails(DynamicData):
   task: Task
   host: Optional[HostSystem] = None
   hostUuid: Optional[str] = None
   maintenanceSpec: Optional[MaintenanceSpec] = None
