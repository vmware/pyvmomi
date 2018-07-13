.. _vim.action.Action: ../../../vim/action/Action.rst

.. _vim.action.Action.ActionParameter: ../../../vim/action/Action/ActionParameter.rst

vim.action.Action.ActionParameter
=================================
  These constant strings can be used as parameters in user-specified email subject and body templates as well as in scripts. The action processor in VirtualCenter substitutes the run-time values for the parameters. For example, an email subject provided by the client could be the string:"Alarm - {alarmName} Description:\n{eventDescription}". Or a script action provided could be:"myScript {alarmName}"
  :contained by: `vim.action.Action`_

  :type: `vim.action.Action.ActionParameter`_

  :name: alarm

values:
--------

target
   The object of the entity where the alarm is associated.

eventDescription
   The event description.

newStatus
   The status after the alarm is triggered.

alarm
   The object of the triggering alarm.

oldStatus
   The status prior to the alarm being triggered.

declaringSummary
   A summary of declarations made during the triggering of the alarm.

alarmName
   The name of the triggering alarm.

targetName
   The name of the entity where the alarm is triggered.

triggeringSummary
   A summary of information involved in triggering the alarm.
