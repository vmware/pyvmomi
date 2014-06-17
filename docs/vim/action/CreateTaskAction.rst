.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.action.Action: ../../vim/action/Action.rst


vim.action.CreateTaskAction
===========================
  This data object type specifies the type of task to be created when this action is triggered.
:extends: vim.action.Action_
:since: `VI API 2.5`_

Attributes:
    taskTypeId (`str`_):

       Extension registered task type identifier for type of task being created.
    cancelable (`bool`_):

       Whether the task should be cancelable.
