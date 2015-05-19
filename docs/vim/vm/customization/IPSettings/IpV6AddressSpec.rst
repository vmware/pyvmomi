.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _vim.vm.customization.IpV6Generator: ../../../../vim/vm/customization/IpV6Generator.rst


vim.vm.customization.IPSettings.IpV6AddressSpec
===============================================
  IPv6 settings
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    ip ([`vim.vm.customization.IpV6Generator`_]):

       ipv6 address generators
    gateway ([`str`_], optional):

       gateways
