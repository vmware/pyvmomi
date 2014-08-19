
vim.action.CreateTaskAction
===========================
  This data object type specifies the type of task to be created when this action is triggered.
:extends: vim.action.Action_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    taskTypeId (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Extension registered task type identifier for type of task being created.
    cancelable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Whether the task should be cancelable.
