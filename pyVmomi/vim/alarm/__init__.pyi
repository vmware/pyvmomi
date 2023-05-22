from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType, PropertyPath


class Alarm(vim.ExtensibleManagedObject):
    @property
    def info(self) -> AlarmInfo: ...
    def Remove(self) -> NoneType: ...
    def Reconfigure(self, spec: AlarmSpec) -> NoneType: ...


class AlarmManager(ManagedObject):
    @property
    def defaultExpression(self) -> List[AlarmExpression]: ...
    @property
    def description(self) -> AlarmDescription: ...
    def Create(self, entity: vim.ManagedEntity, spec: AlarmSpec) -> Alarm: ...
    def GetAlarm(self, entity: vim.ManagedEntity) -> List[Alarm]: ...
    def GetAlarmActionsEnabled(self, entity: vim.ManagedEntity) -> bool: ...
    def SetAlarmActionsEnabled(self, entity: vim.ManagedEntity, enabled: bool) -> NoneType: ...
    def GetAlarmState(self, entity: vim.ManagedEntity) -> List[AlarmState]: ...
    def AcknowledgeAlarm(self, alarm: Alarm, entity: vim.ManagedEntity) -> NoneType: ...
    def ClearTriggeredAlarms(self, filter: AlarmFilterSpec) -> NoneType: ...
    def DisableAlarm(self, alarm: Alarm, entity: vim.ManagedEntity) -> NoneType: ...
    def EnableAlarm(self, alarm: Alarm, entity: vim.ManagedEntity) -> NoneType: ...


class AlarmAction(vmodl.DynamicData): ...


class AlarmDescription(vmodl.DynamicData):
    @property
    def expr(self) -> List[vim.TypeDescription]: ...
    @expr.setter
    def expr(self, value: List[vim.TypeDescription]):
        self._expr = value
    @property
    def stateOperator(self) -> List[vim.ElementDescription]: ...
    @stateOperator.setter
    def stateOperator(self, value: List[vim.ElementDescription]):
        self._stateOperator = value
    @property
    def metricOperator(self) -> List[vim.ElementDescription]: ...
    @metricOperator.setter
    def metricOperator(self, value: List[vim.ElementDescription]):
        self._metricOperator = value
    @property
    def hostSystemConnectionState(self) -> List[vim.ElementDescription]: ...
    @hostSystemConnectionState.setter
    def hostSystemConnectionState(self, value: List[vim.ElementDescription]):
        self._hostSystemConnectionState = value
    @property
    def virtualMachinePowerState(self) -> List[vim.ElementDescription]: ...
    @virtualMachinePowerState.setter
    def virtualMachinePowerState(self, value: List[vim.ElementDescription]):
        self._virtualMachinePowerState = value
    @property
    def datastoreConnectionState(self) -> List[vim.ElementDescription]: ...
    @datastoreConnectionState.setter
    def datastoreConnectionState(self, value: List[vim.ElementDescription]):
        self._datastoreConnectionState = value
    @property
    def hostSystemPowerState(self) -> List[vim.ElementDescription]: ...
    @hostSystemPowerState.setter
    def hostSystemPowerState(self, value: List[vim.ElementDescription]):
        self._hostSystemPowerState = value
    @property
    def virtualMachineGuestHeartbeatStatus(self) -> List[vim.ElementDescription]: ...
    @virtualMachineGuestHeartbeatStatus.setter
    def virtualMachineGuestHeartbeatStatus(self, value: List[vim.ElementDescription]):
        self._virtualMachineGuestHeartbeatStatus = value
    @property
    def entityStatus(self) -> List[vim.ElementDescription]: ...
    @entityStatus.setter
    def entityStatus(self, value: List[vim.ElementDescription]):
        self._entityStatus = value
    @property
    def action(self) -> List[vim.TypeDescription]: ...
    @action.setter
    def action(self, value: List[vim.TypeDescription]):
        self._action = value


class AlarmExpression(vmodl.DynamicData): ...


class AlarmFilterSpec(vmodl.DynamicData):
    @property
    def status(self) -> List[vim.ManagedEntity.Status]: ...
    @status.setter
    def status(self, value: List[vim.ManagedEntity.Status]):
        self._status = value
    @property
    def typeEntity(self) -> str: ...
    @typeEntity.setter
    def typeEntity(self, value: str):
        self._typeEntity = value
    @property
    def typeTrigger(self) -> str: ...
    @typeTrigger.setter
    def typeTrigger(self, value: str):
        self._typeTrigger = value


    class AlarmTypeByEntity(Enum):
        entityTypeAll = "entityTypeAll"
        entityTypeHost = "entityTypeHost"
        entityTypeVm = "entityTypeVm"


    class AlarmTypeByTrigger(Enum):
        triggerTypeAll = "triggerTypeAll"
        triggerTypeEvent = "triggerTypeEvent"
        triggerTypeMetric = "triggerTypeMetric"


class AlarmInfo(AlarmSpec):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def alarm(self) -> Alarm: ...
    @alarm.setter
    def alarm(self, value: Alarm):
        self._alarm = value
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @entity.setter
    def entity(self, value: vim.ManagedEntity):
        self._entity = value
    @property
    def lastModifiedTime(self) -> datetime: ...
    @lastModifiedTime.setter
    def lastModifiedTime(self, value: datetime):
        self._lastModifiedTime = value
    @property
    def lastModifiedUser(self) -> str: ...
    @lastModifiedUser.setter
    def lastModifiedUser(self, value: str):
        self._lastModifiedUser = value
    @property
    def creationEventId(self) -> int: ...
    @creationEventId.setter
    def creationEventId(self, value: int):
        self._creationEventId = value


class AlarmSetting(vmodl.DynamicData):
    @property
    def toleranceRange(self) -> int: ...
    @toleranceRange.setter
    def toleranceRange(self, value: int):
        self._toleranceRange = value
    @property
    def reportingFrequency(self) -> int: ...
    @reportingFrequency.setter
    def reportingFrequency(self, value: int):
        self._reportingFrequency = value


class AlarmSpec(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, value: str):
        self._name = value
    @property
    def systemName(self) -> str: ...
    @systemName.setter
    def systemName(self, value: str):
        self._systemName = value
    @property
    def description(self) -> str: ...
    @description.setter
    def description(self, value: str):
        self._description = value
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value
    @property
    def expression(self) -> AlarmExpression: ...
    @expression.setter
    def expression(self, value: AlarmExpression):
        self._expression = value
    @property
    def action(self) -> AlarmAction: ...
    @action.setter
    def action(self, value: AlarmAction):
        self._action = value
    @property
    def actionFrequency(self) -> int: ...
    @actionFrequency.setter
    def actionFrequency(self, value: int):
        self._actionFrequency = value
    @property
    def setting(self) -> AlarmSetting: ...
    @setting.setter
    def setting(self, value: AlarmSetting):
        self._setting = value


class AlarmState(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @key.setter
    def key(self, value: str):
        self._key = value
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @entity.setter
    def entity(self, value: vim.ManagedEntity):
        self._entity = value
    @property
    def alarm(self) -> Alarm: ...
    @alarm.setter
    def alarm(self, value: Alarm):
        self._alarm = value
    @property
    def overallStatus(self) -> vim.ManagedEntity.Status: ...
    @overallStatus.setter
    def overallStatus(self, value: vim.ManagedEntity.Status):
        self._overallStatus = value
    @property
    def time(self) -> datetime: ...
    @time.setter
    def time(self, value: datetime):
        self._time = value
    @property
    def acknowledged(self) -> bool: ...
    @acknowledged.setter
    def acknowledged(self, value: bool):
        self._acknowledged = value
    @property
    def acknowledgedByUser(self) -> str: ...
    @acknowledgedByUser.setter
    def acknowledgedByUser(self, value: str):
        self._acknowledgedByUser = value
    @property
    def acknowledgedTime(self) -> datetime: ...
    @acknowledgedTime.setter
    def acknowledgedTime(self, value: datetime):
        self._acknowledgedTime = value
    @property
    def eventKey(self) -> int: ...
    @eventKey.setter
    def eventKey(self, value: int):
        self._eventKey = value
    @property
    def disabled(self) -> bool: ...
    @disabled.setter
    def disabled(self, value: bool):
        self._disabled = value


class AlarmTriggeringAction(AlarmAction):
    @property
    def action(self) -> vim.action.Action: ...
    @action.setter
    def action(self, value: vim.action.Action):
        self._action = value
    @property
    def transitionSpecs(self) -> List[AlarmTriggeringAction.TransitionSpec]: ...
    @transitionSpecs.setter
    def transitionSpecs(self, value: List[AlarmTriggeringAction.TransitionSpec]):
        self._transitionSpecs = value
    @property
    def green2yellow(self) -> bool: ...
    @green2yellow.setter
    def green2yellow(self, value: bool):
        self._green2yellow = value
    @property
    def yellow2red(self) -> bool: ...
    @yellow2red.setter
    def yellow2red(self, value: bool):
        self._yellow2red = value
    @property
    def red2yellow(self) -> bool: ...
    @red2yellow.setter
    def red2yellow(self, value: bool):
        self._red2yellow = value
    @property
    def yellow2green(self) -> bool: ...
    @yellow2green.setter
    def yellow2green(self, value: bool):
        self._yellow2green = value


    class TransitionSpec(vmodl.DynamicData):
        @property
        def startState(self) -> vim.ManagedEntity.Status: ...
        @startState.setter
        def startState(self, value: vim.ManagedEntity.Status):
            self._startState = value
        @property
        def finalState(self) -> vim.ManagedEntity.Status: ...
        @finalState.setter
        def finalState(self, value: vim.ManagedEntity.Status):
            self._finalState = value
        @property
        def repeats(self) -> bool: ...
        @repeats.setter
        def repeats(self, value: bool):
            self._repeats = value


class AndAlarmExpression(AlarmExpression):
    @property
    def expression(self) -> List[AlarmExpression]: ...
    @expression.setter
    def expression(self, value: List[AlarmExpression]):
        self._expression = value


class EventAlarmExpression(AlarmExpression):
    @property
    def comparisons(self) -> List[EventAlarmExpression.Comparison]: ...
    @comparisons.setter
    def comparisons(self, value: List[EventAlarmExpression.Comparison]):
        self._comparisons = value
    @property
    def eventType(self) -> type: ...
    @eventType.setter
    def eventType(self, value: type):
        self._eventType = value
    @property
    def eventTypeId(self) -> str: ...
    @eventTypeId.setter
    def eventTypeId(self, value: str):
        self._eventTypeId = value
    @property
    def objectType(self) -> type: ...
    @objectType.setter
    def objectType(self, value: type):
        self._objectType = value
    @property
    def status(self) -> vim.ManagedEntity.Status: ...
    @status.setter
    def status(self, value: vim.ManagedEntity.Status):
        self._status = value


    class Comparison(vmodl.DynamicData):
        @property
        def attributeName(self) -> str: ...
        @attributeName.setter
        def attributeName(self, value: str):
            self._attributeName = value
        @property
        def operator(self) -> str: ...
        @operator.setter
        def operator(self, value: str):
            self._operator = value
        @property
        def value(self) -> str: ...
        @value.setter
        def value(self, value: str):
            self._value = value


    class ComparisonOperator(Enum):
        equals = "equals"
        notEqualTo = "notEqualTo"
        startsWith = "startsWith"
        doesNotStartWith = "doesNotStartWith"
        endsWith = "endsWith"
        doesNotEndWith = "doesNotEndWith"


class GroupAlarmAction(AlarmAction):
    @property
    def action(self) -> List[AlarmAction]: ...
    @action.setter
    def action(self, value: List[AlarmAction]):
        self._action = value


class MetricAlarmExpression(AlarmExpression):
    @property
    def operator(self) -> MetricAlarmExpression.MetricOperator: ...
    @operator.setter
    def operator(self, value: MetricAlarmExpression.MetricOperator):
        self._operator = value
    @property
    def type(self) -> type: ...
    @type.setter
    def type(self, value: type):
        self._type = value
    @property
    def metric(self) -> vim.PerformanceManager.MetricId: ...
    @metric.setter
    def metric(self, value: vim.PerformanceManager.MetricId):
        self._metric = value
    @property
    def yellow(self) -> int: ...
    @yellow.setter
    def yellow(self, value: int):
        self._yellow = value
    @property
    def yellowInterval(self) -> int: ...
    @yellowInterval.setter
    def yellowInterval(self, value: int):
        self._yellowInterval = value
    @property
    def red(self) -> int: ...
    @red.setter
    def red(self, value: int):
        self._red = value
    @property
    def redInterval(self) -> int: ...
    @redInterval.setter
    def redInterval(self, value: int):
        self._redInterval = value


    class MetricOperator(Enum):
        isAbove = "isAbove"
        isBelow = "isBelow"


class OrAlarmExpression(AlarmExpression):
    @property
    def expression(self) -> List[AlarmExpression]: ...
    @expression.setter
    def expression(self, value: List[AlarmExpression]):
        self._expression = value


class StateAlarmExpression(AlarmExpression):
    @property
    def operator(self) -> StateAlarmExpression.StateOperator: ...
    @operator.setter
    def operator(self, value: StateAlarmExpression.StateOperator):
        self._operator = value
    @property
    def type(self) -> type: ...
    @type.setter
    def type(self, value: type):
        self._type = value
    @property
    def statePath(self) -> PropertyPath: ...
    @statePath.setter
    def statePath(self, value: PropertyPath):
        self._statePath = value
    @property
    def yellow(self) -> str: ...
    @yellow.setter
    def yellow(self, value: str):
        self._yellow = value
    @property
    def red(self) -> str: ...
    @red.setter
    def red(self, value: str):
        self._red = value


    class StateOperator(Enum):
        isEqual = "isEqual"
        isUnequal = "isUnequal"