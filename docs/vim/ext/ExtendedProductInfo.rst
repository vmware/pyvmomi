
vim.ext.ExtendedProductInfo
===========================
  This data object encapsulates extended product information for an extension.
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    companyUrl (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       URL to extension vendor.
    productUrl (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       URL to vendor's description of this extension.
    managementUrl (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       URL to management UI for this extension.
    self (`vim.ManagedEntity <vim/ManagedEntity.rst>`_, optional):

       The VirtualMachine or VirtualApp that is running this extension.
