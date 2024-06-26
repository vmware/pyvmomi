# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.vim import ExtensibleManagedObject
from pyVmomi.vim import TaskInfo

from pyVmomi.vmodl import LocalizableMessage
from pyVmomi.vmodl import MethodFault

class Task(ExtensibleManagedObject):
   @property
   def info(self) -> TaskInfo: ...

   def Cancel(self) -> NoReturn: ...
   def UpdateProgress(self, percentDone: int) -> NoReturn: ...
   def SetState(self, state: TaskInfo.State, result: Optional[object], fault: Optional[MethodFault]) -> NoReturn: ...
   def UpdateDescription(self, description: LocalizableMessage) -> NoReturn: ...
