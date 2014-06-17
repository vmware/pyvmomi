.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../vim/version.rst#vimversionversion2

.. _vim.Description: ../../vim/Description.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.Extension.ClientInfo
========================
  This data object type describes a client of the extension.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    version (`str`_):

       Client version number as a dot-separated string. For example, "1.0.0"
    description (`vim.Description`_):

       Description of client.
    company (`str`_):

       Company information.
    type (`str`_):

       Type of client (examples may include win32, .net, linux, etc.).
    url (`str`_):

       Plugin url.
