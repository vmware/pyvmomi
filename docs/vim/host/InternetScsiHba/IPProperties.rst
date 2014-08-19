
vim.host.InternetScsiHba.IPProperties
=====================================
  The IP properties for the host bus adapter
:extends: vmodl.DynamicData_

Attributes:
    mac (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The MAC address.
    address (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The current IPv4 address.
    dhcpConfigurationEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       True if the host bus adapter fetches its IP using DHCP.
    subnetMask (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The current IPv4 subnet mask.
    defaultGateway (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The current IPv4 gateway.
    primaryDnsServerAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The current primary DNS address.
    alternateDnsServerAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The current secondary DNS address.
    ipv6Address (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The current IPv6 address.
    ipv6SubnetMask (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The current IPv6 subnet mask.
    ipv6DefaultGateway (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The current IPv6 default gateway.
    arpRedirectEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if ARP Redirect is enabled
    mtu (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       True if the host bus adapter supports setting its MTU, (for Jumbo Frames, etc) Setting enableJumboFrames and not a numeric mtu value implies autoselection of appropriate MTU value for Jumbo Frames.
    jumboFramesEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

