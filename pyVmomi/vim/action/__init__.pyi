from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from pyVmomi.VmomiSupport import ManagedMethod


class Action(vmodl.DynamicData):


    class ActionParameter(Enum):
        targetName = "targetName"
        alarmName = "alarmName"
        oldStatus = "oldStatus"
        newStatus = "newStatus"
        triggeringSummary = "triggeringSummary"
        declaringSummary = "declaringSummary"
        eventDescription = "eventDescription"
        target = "target"
        alarm = "alarm"


class CreateTaskAction(Action):
    @property
    def taskTypeId(self) -> str: ...
    @taskTypeId.setter
    def taskTypeId(self, value: str):
        self._taskTypeId = value
    @property
    def cancelable(self) -> bool: ...
    @cancelable.setter
    def cancelable(self, value: bool):
        self._cancelable = value


class MethodAction(Action):
    @property
    def name(self) -> ManagedMethod: ...
    @name.setter
    def name(self, value: ManagedMethod):
        self._name = value
    @property
    def argument(self) -> List[MethodActionArgument]: ...
    @argument.setter
    def argument(self, value: List[MethodActionArgument]):
        self._argument = value


class MethodActionArgument(vmodl.DynamicData):
    @property
    def value(self) -> object: ...
    @value.setter
    def value(self, value: object):
        self._value = value


class RunScriptAction(Action):
    @property
    def script(self) -> str: ...
    @script.setter
    def script(self, value: str):
        self._script = value


class SendEmailAction(Action):
    @property
    def toList(self) -> str: ...
    @toList.setter
    def toList(self, value: str):
        self._toList = value
    @property
    def ccList(self) -> str: ...
    @ccList.setter
    def ccList(self, value: str):
        self._ccList = value
    @property
    def subject(self) -> str: ...
    @subject.setter
    def subject(self, value: str):
        self._subject = value
    @property
    def body(self) -> str: ...
    @body.setter
    def body(self, value: str):
        self._body = value


class SendSNMPAction(Action): ...