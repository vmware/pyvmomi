
vim.dvs.ProductSpec
===================
  This data object type is a subset of `AboutInfo <vim/AboutInfo.rst>`_ . An object of this type can be used to describe the specification for a proxy switch module of a `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Short form of the product name.
    vendor (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Name of the vendor of this product.
    version (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Dot-separated version string. For example, "1.2".
    build (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Build string for the server on which this call is made. For example, x.y.z-num. This string does not apply to the API.
    forwardingClass (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Forwarding class of the distributed virtual switch.
    bundleId (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The ID of the bundle if a host component bundle needs to be installed on the host members to support the functionality of the switch.
    bundleUrl (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The URL of the bundle that VMware Update Manager will use to install the bundle on the host members, if `bundleId <vim/dvs/ProductSpec.rst#bundleId>`_ is set.
