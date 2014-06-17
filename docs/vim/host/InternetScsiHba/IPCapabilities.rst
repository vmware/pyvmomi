.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.InternetScsiHba.IPCapabilities
=======================================
  The IP Capabilities for the host bus adapter
:extends: vmodl.DynamicData_

Attributes:
    addressSettable (`bool`_):

       True if the host bus adapter supports setting its IP address.
    ipConfigurationMethodSettable (`bool`_):

       True if the host bus adapter supports DHCP.
    subnetMaskSettable (`bool`_):

       True if the host bus adapter supports setting its subnet mask.
    defaultGatewaySettable (`bool`_):

       True if the host bus adapter supports setting its gateway.
    primaryDnsServerAddressSettable (`bool`_):

       True if the host bus adapter supports setting its primary DNS.
    alternateDnsServerAddressSettable (`bool`_):

       True if the host bus adapter supports setting its secondary DNS.
    ipv6Supported (`bool`_, optional):

       True if the host bus adapter supports the use of IPv6 addresses
    arpRedirectSettable (`bool`_, optional):

       True if the host bus adapter supports setting its ARP Redirect value
    mtuSettable (`bool`_, optional):

       True if the host bus adapter supports setting its MTU, (for Jumbo Frames, etc)
    hostNameAsTargetAddress (`bool`_, optional):

       True if the discovery and static targets can be configured with a host name as opposed to an IP address.
    nameAliasSettable (`bool`_, optional):

       True if the host bus adapter supports setting its name and alias
