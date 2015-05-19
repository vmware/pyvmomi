.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.action.Action: ../../vim/action/Action.rst

.. _vim.scheduler.TaskScheduler: ../../vim/scheduler/TaskScheduler.rst


vim.scheduler.ScheduledTaskSpec
===============================
  Parameters for scheduled task creation.
:extends: vmodl.DynamicData_

Attributes:
    name (`str`_):

       Name of the scheduled task.
    description (`str`_):

       Description of the scheduled task.
    enabled (`bool`_):

       Flag to indicate whether the scheduled task is enabled or disabled.
    scheduler (`vim.scheduler.TaskScheduler`_):

       The time scheduler that determines when the scheduled task runs.
    action (`vim.action.Action`_):

       The action of the scheduled task, to be done when the scheduled task runs.
    notification (`str`_, optional):

       The email notification. If not set, this property is set to empty string, indicating no notification.
