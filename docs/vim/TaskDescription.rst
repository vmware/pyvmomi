
vim.TaskDescription
===================
  Static strings for task objects. These strings are locale-specific.
:extends: vmodl.DynamicData_

Attributes:
    methodInfo ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

       Display label and summary for all tasks
    state ([`vim.ElementDescription <vim/ElementDescription.rst>`_]):

        `TaskInfo State enum <vim/TaskInfo/State.rst>`_ 
    reason ([`vim.TypeDescription <vim/TypeDescription.rst>`_]):

       Kind of entity responsible for creating this task.
