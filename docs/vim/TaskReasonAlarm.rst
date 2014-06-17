.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.TaskReason: ../vim/TaskReason.rst

.. _vim.alarm.Alarm: ../vim/alarm/Alarm.rst

.. _vim.ManagedEntity: ../vim/ManagedEntity.rst


vim.TaskReasonAlarm
===================
  Indicates that the task was queued by an alarm.
:extends: vim.TaskReason_

Attributes:
    alarmName (`str`_):

       The name of the alarm that queued the task, retained in the history collector database.
    alarm (`vim.alarm.Alarm`_):

       The alarm object that queued the task.
    entityName (`str`_):

       The name of the managed entity on which the alarm is triggered, retained in the history collector database.
    entity (`vim.ManagedEntity`_):

       The managed entity object on which the alarm is triggered.
