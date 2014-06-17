.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _other: ../../../vim/host/IpConfig/IpV6AddressConfigType.rst#other

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.IpConfig.IpV6Address: ../../../vim/host/IpConfig/IpV6Address.rst


vim.host.IpConfig.IpV6AddressConfiguration
==========================================
  The ipv6 address configuration
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    ipV6Address (`vim.host.IpConfig.IpV6Address`_, optional):

       Ipv6 adrresses configured on the interface. The global addresses can be configured through DHCP, stateless or manual configuration. Link local addresses can be only configured with the origin set to `other`_ .
    autoConfigurationEnabled (`bool`_, optional):

       Specify if IPv6 address and routing information information be enabled or not as per RFC 2462.
    dhcpV6Enabled (`bool`_, optional):

       The flag to indicate whether or not DHCP (dynamic host control protocol) is enabled to obtain an ipV6 address. If this property is set to true, an ipV6 address is configured through dhcpV6.
