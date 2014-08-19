
vim.DistributedVirtualSwitch.CreateSpec
=======================================
  Specification to create a `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    configSpec (`vim.DistributedVirtualSwitch.ConfigSpec <vim/DistributedVirtualSwitch/ConfigSpec.rst>`_):

       Configuration data.
    productInfo (`vim.dvs.ProductSpec <vim/dvs/ProductSpec.rst>`_, optional):

       Product information for this switch implementation. If you do not specify this property, the Server will use the latest version to create the `DistributedVirtualSwitch <vim/DistributedVirtualSwitch.rst>`_ .
    capability (`vim.DistributedVirtualSwitch.Capability <vim/DistributedVirtualSwitch/Capability.rst>`_, optional):

       Capability of the switch.
