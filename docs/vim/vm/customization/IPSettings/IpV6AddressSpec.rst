
vim.vm.customization.IPSettings.IpV6AddressSpec
===============================================
  IPv6 settings
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    ip ([`vim.vm.customization.IpV6Generator <vim/vm/customization/IpV6Generator.rst>`_]):

       ipv6 address generators
    gateway ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       gateways
