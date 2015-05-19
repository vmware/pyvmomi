.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.alarm.AlarmAction: ../../vim/alarm/AlarmAction.rst

.. _vim.alarm.AlarmSetting: ../../vim/alarm/AlarmSetting.rst

.. _vim.alarm.AlarmExpression: ../../vim/alarm/AlarmExpression.rst


vim.alarm.AlarmSpec
===================
  Parameters for alarm creation.
:extends: vmodl.DynamicData_

Attributes:
    name (`str`_):

       Name of the alarm.
    systemName (`str`_, optional):

       System name of the alarm.This is set only for predefined Alarms - i.e. Alarms created by the server automatically. Editing or renaming Alarms from the UI does not affect this value, and user-created Alarms do not have a systemName at all.The purpose of this field is to identify system-created Alarms reliably, even if they are edited by users.
    description (`str`_):

       Description of the alarm.
    enabled (`bool`_):

       Flag to indicate whether or not the alarm is enabled or disabled.
    expression (`vim.alarm.AlarmExpression`_):

       Top-level alarm expression that defines trigger conditions.
    action (`vim.alarm.AlarmAction`_, optional):

       Action to perform when the alarm is triggered.
    actionFrequency (`int`_, optional):

       Frequency in seconds, which specifies how often appropriate actions should repeat when an alarm does not change state.
    setting (`vim.alarm.AlarmSetting`_, optional):

       Tolerance and maximum frequency settings.
