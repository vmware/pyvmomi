# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vmodl



class Action(pyVmomi.vmodl.DynamicData):
   class ActionParameter(pyVmomi.VmomiSupport.Enum):
      targetName: _typing.ClassVar['ActionParameter'] = 'targetName'
      alarmName: _typing.ClassVar['ActionParameter'] = 'alarmName'
      oldStatus: _typing.ClassVar['ActionParameter'] = 'oldStatus'
      newStatus: _typing.ClassVar['ActionParameter'] = 'newStatus'
      triggeringSummary: _typing.ClassVar['ActionParameter'] = 'triggeringSummary'
      declaringSummary: _typing.ClassVar['ActionParameter'] = 'declaringSummary'
      eventDescription: _typing.ClassVar['ActionParameter'] = 'eventDescription'
      target: _typing.ClassVar['ActionParameter'] = 'target'
      alarm: _typing.ClassVar['ActionParameter'] = 'alarm'

class CreateTaskAction(Action):
   taskTypeId: str
   cancelable: bool


class MethodAction(Action):
   name: pyVmomi.VmomiSupport.ManagedMethod
   argument: list[MethodActionArgument] = []


class MethodActionArgument(pyVmomi.vmodl.DynamicData):
   value: _typing.Optional[object] = None

class RunScriptAction(Action):
   script: str

class SendEmailAction(Action):
   toList: str
   ccList: str
   subject: str
   body: str

class SendSNMPAction(Action):
   pass
