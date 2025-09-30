# Copyright (c) 2006-2025 Broadcom. All Rights Reserved.
# Broadcom Confidential. The term "Broadcom" refers to Broadcom Inc.
# and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

from typing import Optional

from pyVmomi.VmomiSupport import ManagedObject

from pyVmomi.vim.ManagedEntity import ManagedEntity

from pyVmomi.vim.alarm.Alarm import Alarm

from pyVmomi.vim.alarm.AlarmDescription import AlarmDescription

from pyVmomi.vim.alarm.AlarmExpression import AlarmExpression

from pyVmomi.vim.alarm.AlarmFilterSpec import AlarmFilterSpec

from pyVmomi.vim.alarm.AlarmSpec import AlarmSpec

from pyVmomi.vim.alarm.AlarmState import AlarmState

class AlarmManager(ManagedObject):
   @property
   def defaultExpression(self) -> list[AlarmExpression]: ...
   @property
   def description(self) -> AlarmDescription: ...

   def Create(self, entity: ManagedEntity, spec: AlarmSpec) -> Alarm: ...
   def GetAlarm(self, entity: Optional[ManagedEntity]) -> list[Alarm]: ...
   def GetAlarmActionsEnabled(self, entity: ManagedEntity) -> bool: ...
   def SetAlarmActionsEnabled(self, entity: ManagedEntity, enabled: bool) -> None: ...
   def GetAlarmState(self, entity: ManagedEntity) -> list[AlarmState]: ...
   def AcknowledgeAlarm(self, alarm: Alarm, entity: ManagedEntity) -> None: ...
   def ClearTriggeredAlarms(self, filter: AlarmFilterSpec) -> None: ...
   def DisableAlarm(self, alarm: Alarm, entity: ManagedEntity) -> None: ...
   def EnableAlarm(self, alarm: Alarm, entity: ManagedEntity) -> None: ...
