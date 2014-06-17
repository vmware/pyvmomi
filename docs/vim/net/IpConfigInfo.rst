.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.net.DhcpConfigInfo: ../../vim/net/DhcpConfigInfo.rst

.. _vim.net.IpConfigInfo.IpAddress: ../../vim/net/IpConfigInfo/IpAddress.rst


vim.net.IpConfigInfo
====================
  Protocol version independent address reporting data object for network interfaces.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    ipAddress (`vim.net.IpConfigInfo.IpAddress`_, optional):

       Zero, one or more manual (static) assigned IP addresses to be configured on a given interface.
    dhcp (`vim.net.DhcpConfigInfo`_, optional):

       Client side DHCP for a given interface.
    autoConfigurationEnabled (`bool`_, optional):

       Enable or disable ICMPv6 router solictitation requests from a given interface to acquire an IPv6 address and default gateway route from zero, one or more routers on the connected network. If not set then ICMPv6 is not available on this system, See vim.host.Network.Capabilities
