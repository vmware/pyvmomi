.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.ManagedEntity: ../../vim/ManagedEntity.rst


vim.ext.ExtendedProductInfo
===========================
  This data object encapsulates extended product information for an extension.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    companyUrl (`str`_, optional):

       URL to extension vendor.
    productUrl (`str`_, optional):

       URL to vendor's description of this extension.
    managementUrl (`str`_, optional):

       URL to management UI for this extension.
    self (`vim.ManagedEntity`_, optional):

       The VirtualMachine or VirtualApp that is running this extension.
