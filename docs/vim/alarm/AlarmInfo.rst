
vim.alarm.AlarmInfo
===================
  Attributes of an alarm.
:extends: vim.alarm.AlarmSpec_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The unique key.
    alarm (`vim.alarm.Alarm <vim/alarm/Alarm.rst>`_):

       The alarm object.
    entity (`vim.ManagedEntity <vim/ManagedEntity.rst>`_):

       The entity on which the alarm is registered.
    lastModifiedTime (`datetime <https://docs.python.org/2/library/stdtypes.html>`_):

       The time the alarm was created or modified.
    lastModifiedUser (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       User name that modified the alarm most recently.
    creationEventId (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The event ID that records the alarm creation.
