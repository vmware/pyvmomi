.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.Extension.FaultTypeInfo
===========================
  This data object type describes fault types defined by the extension.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    faultID (`str`_):

       The ID of the fault type. Should follow java package naming conventions for uniqueness.
