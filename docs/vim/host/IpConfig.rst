
vim.host.IpConfig
=================
  The IP configuration.
:extends: vmodl.DynamicData_

Attributes:
    dhcp (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not DHCP (dynamic host control protocol) is enabled. If this property is set to true, the ipAddress and the subnetMask strings cannot be set explicitly.
    ipAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The IP address currently used by the network adapter. All IP addresses are specified using IPv4 dot notation. For example, "192.168.0.1". Subnet addresses and netmasks are specified using the same notation.Note: When DHCP is enabled, this property reflects the current IP configuration and cannot be set. When DHCP is not enabled, this property can be set explicitly.
    subnetMask (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The subnet mask.Note: When DHCP is not enabled, this property can be set explicitly. When DHCP is enabled, this property reflects the current IP configuration and cannot be set.
    ipV6Config (`vim.host.IpConfig.IpV6AddressConfiguration <vim/host/IpConfig/IpV6AddressConfiguration.rst>`_, optional):

       The ipv6 configuration
