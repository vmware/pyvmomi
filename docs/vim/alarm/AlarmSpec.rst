
vim.alarm.AlarmSpec
===================
  Parameters for alarm creation.
:extends: vmodl.DynamicData_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the alarm.
    systemName (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       System name of the alarm.This is set only for predefined Alarms - i.e. Alarms created by the server automatically. Editing or renaming Alarms from the UI does not affect this value, and user-created Alarms do not have a systemName at all.The purpose of this field is to identify system-created Alarms reliably, even if they are edited by users.
    description (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Description of the alarm.
    enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag to indicate whether or not the alarm is enabled or disabled.
    expression (`vim.alarm.AlarmExpression <vim/alarm/AlarmExpression.rst>`_):

       Top-level alarm expression that defines trigger conditions.
    action (`vim.alarm.AlarmAction <vim/alarm/AlarmAction.rst>`_, optional):

       Action to perform when the alarm is triggered.
    actionFrequency (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Frequency in seconds, which specifies how often appropriate actions should repeat when an alarm does not change state.
    setting (`vim.alarm.AlarmSetting <vim/alarm/AlarmSetting.rst>`_, optional):

       Tolerance and maximum frequency settings.
