
vim.vApp.ProductInfo
====================
  Information that describes what product a vApp contains, for example, the software that is installed in the contained virtual machines.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       A unique key for the product section
    classId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Class name for this attribute.Valid values for classId: Any string except any white-space characters.
    instanceId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Class name for this attribute.Valid values for instanceId: Any string except any white-space characters.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the product.
    vendor (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Vendor of the product.
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Short version of the product, for example, 1.0.
    fullVersion (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Full-version of the product, for example, 1.0-build 12323.
    vendorUrl (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       URL to vendor homepage.
    productUrl (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       URL to product homepage.
    appUrl (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       URL to entry-point for application. This is often specified using a macro, for example, http://${app.ip}/, where app.ip is a defined property on the virtual machine or vApp container.
