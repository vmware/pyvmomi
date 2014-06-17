.. _vSphere API 4.0: ../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.dvs.ProductSpec: ../../vim/dvs/ProductSpec.rst

.. _DistributedVirtualSwitch: ../../vim/DistributedVirtualSwitch.rst

.. _vim.DistributedVirtualSwitch.Capability: ../../vim/DistributedVirtualSwitch/Capability.rst

.. _vim.DistributedVirtualSwitch.ConfigSpec: ../../vim/DistributedVirtualSwitch/ConfigSpec.rst


vim.DistributedVirtualSwitch.CreateSpec
=======================================
  Specification to create a `DistributedVirtualSwitch`_ .
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    configSpec (`vim.DistributedVirtualSwitch.ConfigSpec`_):

       Configuration data.
    productInfo (`vim.dvs.ProductSpec`_, optional):

       Product information for this switch implementation. If you do not specify this property, the Server will use the latest version to create the `DistributedVirtualSwitch`_ .
    capability (`vim.DistributedVirtualSwitch.Capability`_, optional):

       Capability of the switch.
