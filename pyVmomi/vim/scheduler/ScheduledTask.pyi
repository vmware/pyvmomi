# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from pyVmomi.vim.ExtensibleManagedObject import ExtensibleManagedObject

from pyVmomi.vim.scheduler.ScheduledTaskInfo import ScheduledTaskInfo

from pyVmomi.vim.scheduler.ScheduledTaskSpec import ScheduledTaskSpec

class ScheduledTask(ExtensibleManagedObject):
   @property
   def info(self) -> ScheduledTaskInfo: ...

   def Remove(self) -> None: ...
   def Reconfigure(self, spec: ScheduledTaskSpec) -> None: ...
   def Run(self) -> None: ...
