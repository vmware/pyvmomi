# Copyright (c) 2006-2026 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******

import typing as _typing
import pyVmomi.VmomiSupport
import pyVmomi.vmodl



class Action(pyVmomi.vmodl.DynamicData):
   """
   This data object type defines the action initiated by a scheduled task or alarm.
   
   This is an abstract type.
   A client creates a scheduled task or an alarm each of which triggers
   an action, defined by a subclass of this type.
   """
   class ActionParameter(pyVmomi.VmomiSupport.Enum):
      """
      These constant strings can be used as parameters in user-specified
      email subject and body templates as well as in scripts.
      
      The action processor
      in VirtualCenter substitutes the run-time values for the parameters.
      For example, an email subject provided by the client could be the string:
      `Alarm - {alarmName} Description:\\n{eventDescription}`.
      Or a script action provided could be: `myScript {alarmName}`.
      
      Attributes:
          targetName: The name of the entity where the alarm is triggered.
          alarmName: The name of the triggering alarm.
          oldStatus: The status prior to the alarm being triggered.
          newStatus: The status after the alarm is triggered.
          triggeringSummary: A summary of information involved in triggering the alarm.
          declaringSummary: A summary of declarations made during the triggering of the alarm.
          eventDescription: The event description.
          target: The object of the entity where the alarm is associated.
          alarm: The object of the triggering alarm.
      """
      targetName: _typing.ClassVar['Action.ActionParameter'] = 'targetName'
      alarmName: _typing.ClassVar['Action.ActionParameter'] = 'alarmName'
      oldStatus: _typing.ClassVar['Action.ActionParameter'] = 'oldStatus'
      newStatus: _typing.ClassVar['Action.ActionParameter'] = 'newStatus'
      triggeringSummary: _typing.ClassVar['Action.ActionParameter'] = 'triggeringSummary'
      declaringSummary: _typing.ClassVar['Action.ActionParameter'] = 'declaringSummary'
      eventDescription: _typing.ClassVar['Action.ActionParameter'] = 'eventDescription'
      target: _typing.ClassVar['Action.ActionParameter'] = 'target'
      alarm: _typing.ClassVar['Action.ActionParameter'] = 'alarm'

class CreateTaskAction(Action):
   """
   This data object type specifies the type of task to be created
   when this action is triggered.
   
   Attributes:
       taskTypeId: Extension registered task type identifier
           for type of task being created.
       cancelable: Whether the task should be cancelable.
   """
   taskTypeId: str
   cancelable: bool


class MethodAction(Action):
   """
   This data object type defines an operation and its arguments, invoked
   on a particular entity.
   
   Attributes:
       name: Name of the operation.
       argument: An array consisting of the arguments for the operation.
   """
   name: pyVmomi.VmomiSupport.ManagedMethod
   argument: list[MethodActionArgument] = []


class MethodActionArgument(pyVmomi.vmodl.DynamicData):
   """
   This data object type defines a named argument for an operation.
   
   Attributes:
       value: The value of the argument.
   """
   value: _typing.Optional[object] = None

class RunScriptAction(Action):
   """
   This data object type specifies a script that is triggered by an alarm.
   
   You can use any elements of the
   `pyVmomi.vim.action.Action.ActionParameter` enumerated list
   as part of your script to provide information available at runtime.
   
   Attributes:
       script: The fully-qualified path to a shell script that runs on the
           VirtualCenter server as a result of an alarm.
   """
   script: str

class SendEmailAction(Action):
   """
   This data object type defines an email that is triggered by an
   alarm.
   
   You can use any
   elements of the `pyVmomi.vim.action.Action.ActionParameter`
   enumerated list as part of your strings to provide information available
   at runtime.
   
   Attributes:
       toList: A comma-separated list of addresses to which the email notification is sent.
       ccList: A comma-separated list of addresses that are cc'ed on the email notification.
       subject: Subject of the email notification.
       body: Content of the email notification.
   """
   toList: str
   ccList: str
   subject: str
   body: str

class SendSNMPAction(Action):
   """This data object type specifies an SNMP trap that is triggered by an alarm."""
   pass
