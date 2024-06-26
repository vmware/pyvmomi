# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn

from pyVmomi.vim import ExtensibleManagedObject

from pyVmomi.vim.scheduler import ScheduledTaskInfo
from pyVmomi.vim.scheduler import ScheduledTaskSpec

class ScheduledTask(ExtensibleManagedObject):
   @property
   def info(self) -> ScheduledTaskInfo: ...

   def Remove(self) -> NoReturn: ...
   def Reconfigure(self, spec: ScheduledTaskSpec) -> NoReturn: ...
   def Run(self) -> NoReturn: ...
