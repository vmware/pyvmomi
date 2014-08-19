
vim.alarm.EventAlarmExpression.Comparison
=========================================
  Encapsulates Comparison of an event's attribute to a value.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    attributeName (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The attribute of the event to compare
    operator (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       An operator from the list above
    value (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The value to compare against
