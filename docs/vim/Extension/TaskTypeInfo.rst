.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.Extension.TaskTypeInfo
==========================
  This data object type describes task types defined by the extension.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    taskID (`str`_):

       The ID of the task type. Should follow java package naming conventions for uniqueness.
