.. _vmodl.DynamicData: ../vmodl/DynamicData.rst

.. _vim.TypeDescription: ../vim/TypeDescription.rst

.. _TaskInfo State enum: ../vim/TaskInfo/State.rst

.. _vim.ElementDescription: ../vim/ElementDescription.rst


vim.TaskDescription
===================
  Static strings for task objects. These strings are locale-specific.
:extends: vmodl.DynamicData_

Attributes:
    methodInfo ([`vim.ElementDescription`_]):

       Display label and summary for all tasks
    state ([`vim.ElementDescription`_]):

        `TaskInfo State enum`_ 
    reason ([`vim.TypeDescription`_]):

       Kind of entity responsible for creating this task.
