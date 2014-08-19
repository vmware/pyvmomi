
vim.host.InternetScsiHba.IPCapabilities
=======================================
  The IP Capabilities for the host bus adapter
:extends: vmodl.DynamicData_

Attributes:
    addressSettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if the host bus adapter supports setting its IP address.
    ipConfigurationMethodSettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if the host bus adapter supports DHCP.
    subnetMaskSettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if the host bus adapter supports setting its subnet mask.
    defaultGatewaySettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if the host bus adapter supports setting its gateway.
    primaryDnsServerAddressSettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if the host bus adapter supports setting its primary DNS.
    alternateDnsServerAddressSettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if the host bus adapter supports setting its secondary DNS.
    ipv6Supported (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if the host bus adapter supports the use of IPv6 addresses
    arpRedirectSettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if the host bus adapter supports setting its ARP Redirect value
    mtuSettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if the host bus adapter supports setting its MTU, (for Jumbo Frames, etc)
    hostNameAsTargetAddress (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if the discovery and static targets can be configured with a host name as opposed to an IP address.
    nameAliasSettable (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if the host bus adapter supports setting its name and alias
