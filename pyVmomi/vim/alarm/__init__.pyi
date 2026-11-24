# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import datetime as _datetime
import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vim
import pyVmomi.vmodl
import pyVmomi.vim.action



class Alarm(pyVmomi.vim.ExtensibleManagedObject):
   @property
   def info(self) -> AlarmInfo: ...

   def Remove(self) -> None: ...
   def Reconfigure(self, spec: AlarmSpec) -> None: ...


class AlarmAction(pyVmomi.vmodl.DynamicData):
   pass


class AlarmDescription(pyVmomi.vmodl.DynamicData):
   expr: list[pyVmomi.vim.TypeDescription] = []
   stateOperator: list[pyVmomi.vim.ElementDescription] = []
   metricOperator: list[pyVmomi.vim.ElementDescription] = []
   hostSystemConnectionState: list[pyVmomi.vim.ElementDescription] = []
   virtualMachinePowerState: list[pyVmomi.vim.ElementDescription] = []
   datastoreConnectionState: list[pyVmomi.vim.ElementDescription] = []
   hostSystemPowerState: list[pyVmomi.vim.ElementDescription] = []
   virtualMachineGuestHeartbeatStatus: list[pyVmomi.vim.ElementDescription] = []
   entityStatus: list[pyVmomi.vim.ElementDescription] = []
   action: list[pyVmomi.vim.TypeDescription] = []


class AlarmExpression(pyVmomi.vmodl.DynamicData):
   pass


class AlarmFilterSpec(pyVmomi.vmodl.DynamicData):
   class AlarmTypeByEntity(pyVmomi.VmomiSupport.Enum):
      entityTypeAll: _typing.ClassVar['AlarmTypeByEntity'] = 'entityTypeAll'
      entityTypeHost: _typing.ClassVar['AlarmTypeByEntity'] = 'entityTypeHost'
      entityTypeVm: _typing.ClassVar['AlarmTypeByEntity'] = 'entityTypeVm'

   class AlarmTypeByTrigger(pyVmomi.VmomiSupport.Enum):
      triggerTypeAll: _typing.ClassVar['AlarmTypeByTrigger'] = 'triggerTypeAll'
      triggerTypeEvent: _typing.ClassVar['AlarmTypeByTrigger'] = 'triggerTypeEvent'
      triggerTypeMetric: _typing.ClassVar['AlarmTypeByTrigger'] = 'triggerTypeMetric'

   status: list[pyVmomi.vim.ManagedEntity.Status] = []
   typeEntity: _typing.Optional[str] = None
   typeTrigger: _typing.Optional[str] = None


class AlarmInfo(AlarmSpec):
   key: str
   alarm: Alarm
   entity: pyVmomi.vim.ManagedEntity
   lastModifiedTime: _datetime.datetime
   lastModifiedUser: str
   creationEventId: int


class AlarmManager(pyVmomi.VmomiSupport.ManagedObject):
   @property
   def defaultExpression(self) -> list[AlarmExpression]: ...
   @property
   def description(self) -> AlarmDescription: ...

   def Create(self, entity: pyVmomi.vim.ManagedEntity, spec: AlarmSpec) -> Alarm: ...
   def GetAlarm(self, entity: _typing.Optional[pyVmomi.vim.ManagedEntity]) -> list[Alarm]: ...
   def GetAlarmActionsEnabled(self, entity: pyVmomi.vim.ManagedEntity) -> bool: ...
   def SetAlarmActionsEnabled(self, entity: pyVmomi.vim.ManagedEntity, enabled: bool) -> None: ...
   def GetAlarmState(self, entity: pyVmomi.vim.ManagedEntity) -> list[AlarmState]: ...
   def AcknowledgeAlarm(self, alarm: Alarm, entity: pyVmomi.vim.ManagedEntity) -> None: ...
   def ClearTriggeredAlarms(self, filter: AlarmFilterSpec) -> None: ...
   def DisableAlarm(self, alarm: Alarm, entity: pyVmomi.vim.ManagedEntity) -> None: ...
   def EnableAlarm(self, alarm: Alarm, entity: pyVmomi.vim.ManagedEntity) -> None: ...


class AlarmSetting(pyVmomi.vmodl.DynamicData):
   toleranceRange: int
   reportingFrequency: int


class AlarmSpec(pyVmomi.vmodl.DynamicData):
   name: str
   systemName: _typing.Optional[str] = None
   description: str
   enabled: bool
   expression: AlarmExpression
   action: _typing.Optional[AlarmAction] = None
   actionFrequency: _typing.Optional[int] = None
   setting: _typing.Optional[AlarmSetting] = None


class AlarmState(pyVmomi.vmodl.DynamicData):
   key: str
   entity: pyVmomi.vim.ManagedEntity
   alarm: Alarm
   overallStatus: pyVmomi.vim.ManagedEntity.Status
   time: _datetime.datetime
   acknowledged: _typing.Optional[bool] = None
   acknowledgedByUser: _typing.Optional[str] = None
   acknowledgedTime: _typing.Optional[_datetime.datetime] = None
   eventKey: _typing.Optional[int] = None
   disabled: _typing.Optional[bool] = None


class AlarmTriggeringAction(AlarmAction):
   class TransitionSpec(pyVmomi.vmodl.DynamicData):
      startState: pyVmomi.vim.ManagedEntity.Status
      finalState: pyVmomi.vim.ManagedEntity.Status
      repeats: bool

   action: pyVmomi.vim.action.Action
   transitionSpecs: list[TransitionSpec] = []
   green2yellow: bool
   yellow2red: bool
   red2yellow: bool
   yellow2green: bool

class AndAlarmExpression(AlarmExpression):
   expression: list[AlarmExpression] = []


class EventAlarmExpression(AlarmExpression):
   class ComparisonOperator(pyVmomi.VmomiSupport.Enum):
      equals: _typing.ClassVar['ComparisonOperator'] = 'equals'
      notEqualTo: _typing.ClassVar['ComparisonOperator'] = 'notEqualTo'
      startsWith: _typing.ClassVar['ComparisonOperator'] = 'startsWith'
      doesNotStartWith: _typing.ClassVar['ComparisonOperator'] = 'doesNotStartWith'
      endsWith: _typing.ClassVar['ComparisonOperator'] = 'endsWith'
      doesNotEndWith: _typing.ClassVar['ComparisonOperator'] = 'doesNotEndWith'

   class Comparison(pyVmomi.vmodl.DynamicData):
      attributeName: str
      operator: str
      value: str

   comparisons: list[Comparison] = []
   eventType: type
   eventTypeId: _typing.Optional[str] = None
   objectType: _typing.Optional[type] = None
   status: _typing.Optional[pyVmomi.vim.ManagedEntity.Status] = None

class GroupAlarmAction(AlarmAction):
   action: list[AlarmAction] = []


class MetricAlarmExpression(AlarmExpression):
   class MetricOperator(pyVmomi.VmomiSupport.Enum):
      isAbove: _typing.ClassVar['MetricOperator'] = 'isAbove'
      isBelow: _typing.ClassVar['MetricOperator'] = 'isBelow'

   operator: MetricOperator
   type: type
   metric: pyVmomi.vim.PerformanceManager.MetricId
   yellow: _typing.Optional[int] = None
   yellowInterval: _typing.Optional[int] = None
   red: _typing.Optional[int] = None
   redInterval: _typing.Optional[int] = None

class OrAlarmExpression(AlarmExpression):
   expression: list[AlarmExpression] = []


class StateAlarmExpression(AlarmExpression):
   class StateOperator(pyVmomi.VmomiSupport.Enum):
      isEqual: _typing.ClassVar['StateOperator'] = 'isEqual'
      isUnequal: _typing.ClassVar['StateOperator'] = 'isUnequal'

   operator: StateOperator
   type: type
   statePath: pyVmomi.VmomiSupport.PropertyPath
   yellow: _typing.Optional[str] = None
   red: _typing.Optional[str] = None
