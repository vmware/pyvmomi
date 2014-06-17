.. _str: https://docs.python.org/2/library/stdtypes.html

.. _int: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vim.alarm.Alarm: ../../vim/alarm/Alarm.rst

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst

.. _vim.alarm.AlarmSpec: ../../vim/alarm/AlarmSpec.rst


vim.alarm.AlarmInfo
===================
  Attributes of an alarm.
:extends: vim.alarm.AlarmSpec_

Attributes:
    key (`str`_):

       The unique key.
    alarm (`vim.alarm.Alarm`_):

       The alarm object.
    entity (`vim.ManagedEntity`_):

       The entity on which the alarm is registered.
    lastModifiedTime (`datetime`_):

       The time the alarm was created or modified.
    lastModifiedUser (`str`_):

       User name that modified the alarm most recently.
    creationEventId (`int`_):

       The event ID that records the alarm creation.
