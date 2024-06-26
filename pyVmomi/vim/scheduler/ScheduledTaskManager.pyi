# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ManagedEntity

from pyVmomi.vim.scheduler import ScheduledTask
from pyVmomi.vim.scheduler import ScheduledTaskDescription
from pyVmomi.vim.scheduler import ScheduledTaskSpec

class ScheduledTaskManager(ManagedObject):
   @property
   def scheduledTask(self) -> list[ScheduledTask]: ...
   @property
   def description(self) -> ScheduledTaskDescription: ...

   def Create(self, entity: ManagedEntity, spec: ScheduledTaskSpec) -> ScheduledTask: ...
   def RetrieveEntityScheduledTask(self, entity: Optional[ManagedEntity]) -> list[ScheduledTask]: ...
   def CreateObjectScheduledTask(self, obj: ManagedObject, spec: ScheduledTaskSpec) -> ScheduledTask: ...
   def RetrieveObjectScheduledTask(self, obj: Optional[ManagedObject]) -> list[ScheduledTask]: ...
