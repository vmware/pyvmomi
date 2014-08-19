
vim.LicenseManager.LicenseInfo
==============================
  Encapsulates information about a license
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    licenseKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Key for the license. E.g. serial number.
    editionKey (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Edition key.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Display name for the license
    total (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       Total number of units contain in the license
    used (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Number of units used from this license
    costUnit (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The cost unit for this license
    properties ([`vmodl.KeyAnyValue <vmodl/KeyAnyValue.rst>`_], optional):

       Additional properties associated with this license
    labels ([`vim.KeyValue <vim/KeyValue.rst>`_], optional):

       Key-value lables for this license
