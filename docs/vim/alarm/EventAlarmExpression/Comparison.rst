.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.alarm.EventAlarmExpression.Comparison
=========================================
  Encapsulates Comparison of an event's attribute to a value.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    attributeName (`str`_):

       The attribute of the event to compare
    operator (`str`_):

       An operator from the list above
    value (`str`_):

       The value to compare against
