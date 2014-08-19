
vim.alarm.GroupAlarmAction
==========================
  This data object type describes a group of actions that occur when the alarm is triggered. These actions are not necessarily executed in order.
:extends: vim.alarm.AlarmAction_

Attributes:
    action ([`vim.alarm.AlarmAction <vim/alarm/AlarmAction.rst>`_]):

       The list of alarm actions that occur when the alarm is triggered.
