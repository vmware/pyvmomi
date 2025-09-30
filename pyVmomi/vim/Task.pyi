# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.vim.ExtensibleManagedObject import ExtensibleManagedObject

from pyVmomi.vim.TaskInfo import TaskInfo

from pyVmomi.vmodl.LocalizableMessage import LocalizableMessage

from pyVmomi.vmodl.MethodFault import MethodFault

class Task(ExtensibleManagedObject):
   @property
   def info(self) -> TaskInfo: ...

   def Cancel(self) -> None: ...
   def UpdateProgress(self, percentDone: int) -> None: ...
   def SetState(self, state: TaskInfo.State, result: Optional[object], fault: Optional[MethodFault]) -> None: ...
   def UpdateDescription(self, description: LocalizableMessage) -> None: ...
