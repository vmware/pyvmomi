
vim.net.DhcpConfigSpec.DhcpOptionsSpec
======================================
  Provides for configuration of IPv6
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    enable (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Enable or disable dhcp for IPv4.
    config ([`vim.KeyValue <vim/KeyValue.rst>`_]):

       Platform specific settings for DHCP Client. The key part is a unique number, the value part is the platform specific configuration command. See `NetDhcpConfigInfo <vim/net/DhcpConfigInfo.rst>`_ for value formatting.
    operation (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Requires one of the values from `HostConfigChangeOperation <vim/host/ConfigChange/Operation.rst>`_ .
