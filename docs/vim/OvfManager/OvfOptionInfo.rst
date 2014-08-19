
vim.OvfManager.OvfOptionInfo
============================
  Represents the OVF options the server support for import and export of OVFs
:extends: vmodl.DynamicData_
:since: `vSphere API 5.1 <vim/version.rst#vimversionversion8>`_

Attributes:
    option (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the OVF option that is supported by the server
    description (`vmodl.LocalizableMessage <vmodl/LocalizableMessage.rst>`_):

       A description of the OVF option
