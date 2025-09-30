# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from datetime import datetime

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.Task import Task

from pyVmomi.vim.TaskInfo import TaskInfo

from pyVmomi.vmodl.MethodFault import MethodFault

from pyVmomi.vim.scheduler.ScheduledTask import ScheduledTask

from pyVmomi.vim.scheduler.ScheduledTaskSpec import ScheduledTaskSpec

class ScheduledTaskInfo(ScheduledTaskSpec):
   scheduledTask: ScheduledTask
   entity: ManagedEntity
   lastModifiedTime: datetime
   lastModifiedUser: str
   nextRunTime: Optional[datetime] = None
   prevRunTime: Optional[datetime] = None
   state: TaskInfo.State
   error: Optional[MethodFault] = None
   result: Optional[object] = None
   progress: Optional[int] = None
   activeTask: Optional[Task] = None
   taskObject: ManagedObject
