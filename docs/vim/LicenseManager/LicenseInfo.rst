.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.KeyValue: ../../vim/KeyValue.rst

.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.KeyAnyValue: ../../vmodl/KeyAnyValue.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.LicenseManager.LicenseInfo
==============================
  Encapsulates information about a license
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    licenseKey (`str`_):

       Key for the license. E.g. serial number.
    editionKey (`str`_):

       Edition key.
    name (`str`_):

       Display name for the license
    total (`int`_):

       Total number of units contain in the license
    used (`int`_, optional):

       Number of units used from this license
    costUnit (`str`_):

       The cost unit for this license
    properties ([`vmodl.KeyAnyValue`_], optional):

       Additional properties associated with this license
    labels ([`vim.KeyValue`_], optional):

       Key-value lables for this license
