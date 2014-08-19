
vim.vApp.IpPool.IpPoolConfigInfo
================================
  Specifications of either IPv4 or IPv6 configuration to be used on this network. This is a part of network configuration.IPv4 addresses are in dot-decimal notation, e.g.: 192.0.2.235IPv6 addresses are in colon-hexadecimal notation, e.g.: 2001:0db8:85a3::0370:7334
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    subnetAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Address of the subnet.For example:
        * IPv4: 192.168.5.0
        * IPv6: 2001:0db8:85a3::
    netmask (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       NetmaskFor example:
        * IPv4: 255.255.255.0
        * IPv6: ffff:ffff:ffff::
    gateway (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Gateway. This can be an empty string - if no gateway is configured.Examples:
        * IPv4: 192.168.5.1
        * IPv6: 2001:0db8:85a3::1
    range (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       IP range. This is specified as a set of ranges separated with commas. One range is given by a start address, a hash (#), and the length of the range.For example:
        * 192.0.2.235 # 20 is the IPv4 range from 192.0.2.235 to 192.0.2.254
        * 2001::7334 # 20 is the IPv6 range from 2001::7334 to 2001::7347
    dns ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       DNS serversFor example:
        * IPv4: ["10.20.0.1", "10.20.0.2"]
        * IPv6: ["2001:0db8:85a3::0370:7334", "2001:0db8:85a3::0370:7335"]If an empty list is passed, the existing value remains unchanged. To clear this list, pass an array containing the empty string as it's only element.
    dhcpServerAvailable (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Whether a DHCP server is available on this network.
    ipPoolEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       IP addresses can only be allocated from the range if the IP pool is enabled.
