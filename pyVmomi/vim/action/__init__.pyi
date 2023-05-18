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
    @property
    def cancelable(self) -> bool: ...


class MethodAction(Action):
    @property
    def name(self) -> ManagedMethod: ...
    @property
    def argument(self) -> List[MethodActionArgument]: ...


class MethodActionArgument(vmodl.DynamicData):
    @property
    def value(self) -> object: ...


class RunScriptAction(Action):
    @property
    def script(self) -> str: ...


class SendEmailAction(Action):
    @property
    def toList(self) -> str: ...
    @property
    def ccList(self) -> str: ...
    @property
    def subject(self) -> str: ...
    @property
    def body(self) -> str: ...


class SendSNMPAction(Action): ...