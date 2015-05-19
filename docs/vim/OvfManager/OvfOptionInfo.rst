.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.1: ../../vim/version.rst#vimversionversion8

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vmodl.LocalizableMessage: ../../vmodl/LocalizableMessage.rst


vim.OvfManager.OvfOptionInfo
============================
  Represents the OVF options the server support for import and export of OVFs
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1`_

Attributes:
    option (`str`_):

       The name of the OVF option that is supported by the server
    description (`vmodl.LocalizableMessage`_):

       A description of the OVF option
