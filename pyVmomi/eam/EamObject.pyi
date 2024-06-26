# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vmodl import DynamicData

from pyVmomi.eam.issue import Issue

class EamObject(ManagedObject):
   class RuntimeInfo(DynamicData):
      class Status(Enum):
         green: ClassVar['Status'] = 'green'
         yellow: ClassVar['Status'] = 'yellow'
         red: ClassVar['Status'] = 'red'

      class GoalState(Enum):
         enabled: ClassVar['GoalState'] = 'enabled'
         disabled: ClassVar['GoalState'] = 'disabled'
         uninstalled: ClassVar['GoalState'] = 'uninstalled'

      status: str
      issue: list[Issue] = []
      goalState: str
      entity: EamObject

   def Resolve(self, issueKey: list[int]) -> list[int]: ...
   def ResolveAll(self) -> NoReturn: ...
   def QueryIssue(self, issueKey: list[int]) -> list[Issue]: ...
