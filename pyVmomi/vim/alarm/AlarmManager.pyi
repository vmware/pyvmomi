# Copyright (c) 2006-2024 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import NoReturn
from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim import ManagedEntity

from pyVmomi.vim.alarm import Alarm
from pyVmomi.vim.alarm import AlarmDescription
from pyVmomi.vim.alarm import AlarmExpression
from pyVmomi.vim.alarm import AlarmFilterSpec
from pyVmomi.vim.alarm import AlarmSpec
from pyVmomi.vim.alarm import AlarmState

class AlarmManager(ManagedObject):
   @property
   def defaultExpression(self) -> list[AlarmExpression]: ...
   @property
   def description(self) -> AlarmDescription: ...

   def Create(self, entity: ManagedEntity, spec: AlarmSpec) -> Alarm: ...
   def GetAlarm(self, entity: Optional[ManagedEntity]) -> list[Alarm]: ...
   def GetAlarmActionsEnabled(self, entity: ManagedEntity) -> bool: ...
   def SetAlarmActionsEnabled(self, entity: ManagedEntity, enabled: bool) -> NoReturn: ...
   def GetAlarmState(self, entity: ManagedEntity) -> list[AlarmState]: ...
   def AcknowledgeAlarm(self, alarm: Alarm, entity: ManagedEntity) -> NoReturn: ...
   def ClearTriggeredAlarms(self, filter: AlarmFilterSpec) -> NoReturn: ...
   def DisableAlarm(self, alarm: Alarm, entity: ManagedEntity) -> NoReturn: ...
   def EnableAlarm(self, alarm: Alarm, entity: ManagedEntity) -> NoReturn: ...