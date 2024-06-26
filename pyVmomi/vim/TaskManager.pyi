# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import Task
from pyVmomi.vim import TaskDescription
from pyVmomi.vim import TaskFilterSpec
from pyVmomi.vim import TaskHistoryCollector
from pyVmomi.vim import TaskInfo
from pyVmomi.vim import TaskInfoFilterSpec

class TaskManager(ManagedObject):
   @property
   def recentTask(self) -> list[Task]: ...
   @property
   def description(self) -> TaskDescription: ...
   @property
   def maxCollector(self) -> int: ...

   def CreateCollector(self, filter: TaskFilterSpec) -> TaskHistoryCollector: ...
   def CreateCollectorWithInfoFilter(self, filter: TaskFilterSpec, infoFilter: Optional[TaskInfoFilterSpec]) -> TaskHistoryCollector: ...
   def CreateTask(self, obj: ManagedObject, taskTypeId: str, initiatedBy: Optional[str], cancelable: bool, parentTaskKey: Optional[str], activationId: Optional[str]) -> TaskInfo: ...
