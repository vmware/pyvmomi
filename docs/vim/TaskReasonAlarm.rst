
vim.TaskReasonAlarm
===================
  Indicates that the task was queued by an alarm.
:extends: vim.TaskReason_

Attributes:
    alarmName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the alarm that queued the task, retained in the history collector database.
    alarm (`vim.alarm.Alarm <vim/alarm/Alarm.rst>`_):

       The alarm object that queued the task.
    entityName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the managed entity on which the alarm is triggered, retained in the history collector database.
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):

       The managed entity object on which the alarm is triggered.
