.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.InternetScsiHba.IPProperties
=====================================
  The IP properties for the host bus adapter
:extends: vmodl.DynamicData_

Attributes:
    mac (`str`_, optional):

       The MAC address.
    address (`str`_, optional):

       The current IPv4 address.
    dhcpConfigurationEnabled (`bool`_):

       True if the host bus adapter fetches its IP using DHCP.
    subnetMask (`str`_, optional):

       The current IPv4 subnet mask.
    defaultGateway (`str`_, optional):

       The current IPv4 gateway.
    primaryDnsServerAddress (`str`_, optional):

       The current primary DNS address.
    alternateDnsServerAddress (`str`_, optional):

       The current secondary DNS address.
    ipv6Address (`str`_, optional):

       The current IPv6 address.
    ipv6SubnetMask (`str`_, optional):

       The current IPv6 subnet mask.
    ipv6DefaultGateway (`str`_, optional):

       The current IPv6 default gateway.
    arpRedirectEnabled (`bool`_, optional):

       True if ARP Redirect is enabled
    mtu (`int`_, optional):

       True if the host bus adapter supports setting its MTU, (for Jumbo Frames, etc) Setting enableJumboFrames and not a numeric mtu value implies autoselection of appropriate MTU value for Jumbo Frames.
    jumboFramesEnabled (`bool`_, optional):

