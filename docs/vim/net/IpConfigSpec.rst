.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.net.DhcpConfigSpec: ../../vim/net/DhcpConfigSpec.rst

.. _vim.net.IpConfigSpec.IpAddressSpec: ../../vim/net/IpConfigSpec/IpAddressSpec.rst


vim.net.IpConfigSpec
====================
  Internet Protocol Address Configuration for version 4 and version 6.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    ipAddress (`vim.net.IpConfigSpec.IpAddressSpec`_, optional):

       A set of manual (static) IP addresses to be configured on a given interface.
    dhcp (`vim.net.DhcpConfigSpec`_, optional):

       Configure client side DHCP for a given interface.
    autoConfigurationEnabled (`bool`_, optional):

       Enable or disable ICMPv6 router solictitation requests from a given interface to acquire an IPv6 address and default gateway route from zero, one or more routers on the connected network.
