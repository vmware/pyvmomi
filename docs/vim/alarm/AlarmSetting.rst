.. _int: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.alarm.AlarmSetting
======================
  Tolerance and frequency limits of an alarm.
:extends: vmodl.DynamicData_

Attributes:
    toleranceRange (`int`_):

       Tolerance range for the metric triggers, measured in one hundredth percentage.A zero value means that the alarm triggers whenever the metric value is above or below the specified value. A nonzero value means that the alarm triggers only after reaching a certain percentage above or below the nominal trigger value.
    reportingFrequency (`int`_):

       How often the alarm is triggered, measured in seconds.A zero value means that the alarm is allowed to trigger as often as possible. A nonzero value means that any subsequent triggers are suppressed for a period of seconds following a reported trigger.
