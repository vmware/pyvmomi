# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.scheduler.ScheduledTask import ScheduledTask

from pyVmomi.vim.scheduler.ScheduledTaskDescription import ScheduledTaskDescription

from pyVmomi.vim.scheduler.ScheduledTaskSpec import ScheduledTaskSpec

class ScheduledTaskManager(ManagedObject):
   @property
   def scheduledTask(self) -> list[ScheduledTask]: ...
   @property
   def description(self) -> ScheduledTaskDescription: ...

   def Create(self, entity: ManagedEntity, spec: ScheduledTaskSpec) -> ScheduledTask: ...
   def RetrieveEntityScheduledTask(self, entity: Optional[ManagedEntity]) -> list[ScheduledTask]: ...
   def CreateObjectScheduledTask(self, obj: ManagedObject, spec: ScheduledTaskSpec) -> ScheduledTask: ...
   def RetrieveObjectScheduledTask(self, obj: Optional[ManagedObject]) -> list[ScheduledTask]: ...
