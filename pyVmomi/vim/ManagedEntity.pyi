# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import ClassVar
from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import Enum
from pyVmomi.VmomiSupport import ManagedMethod

from pyVmomi.vim import AuthorizationManager
from pyVmomi.vim import CustomFieldsManager
from pyVmomi.vim import ExtensibleManagedObject
from pyVmomi.vim import Tag
from pyVmomi.vim import Task

from pyVmomi.vim.alarm import AlarmState

from pyVmomi.vim.event import Event

class ManagedEntity(ExtensibleManagedObject):
   class Status(Enum):
      gray: ClassVar['Status'] = 'gray'
      green: ClassVar['Status'] = 'green'
      yellow: ClassVar['Status'] = 'yellow'
      red: ClassVar['Status'] = 'red'

   @property
   def parent(self) -> Optional[ManagedEntity]: ...
   @property
   def customValue(self) -> list[CustomFieldsManager.Value]: ...
   @property
   def overallStatus(self) -> Status: ...
   @property
   def configStatus(self) -> Status: ...
   @property
   def configIssue(self) -> list[Event]: ...
   @property
   def effectiveRole(self) -> list[int]: ...
   @property
   def permission(self) -> list[AuthorizationManager.Permission]: ...
   @property
   def name(self) -> str: ...
   @property
   def disabledMethod(self) -> list[ManagedMethod]: ...
   @property
   def recentTask(self) -> list[Task]: ...
   @property
   def declaredAlarmState(self) -> list[AlarmState]: ...
   @property
   def triggeredAlarmState(self) -> list[AlarmState]: ...
   @property
   def alarmActionsEnabled(self) -> Optional[bool]: ...
   @property
   def tag(self) -> list[Tag]: ...

   def Reload(self) -> NoReturn: ...
   def Rename(self, newName: str) -> Task: ...
   def Destroy(self) -> Task: ...
