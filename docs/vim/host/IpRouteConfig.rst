
vim.host.IpRouteConfig
======================
  IP Route Configuration. All IPv4 addresses, subnet addresses, and netmasks are specified as strings using dotted decimal notation. For example, "192.0.2.1". IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373.
:extends: vmodl.DynamicData_

Attributes:
    defaultGateway (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The default gateway address.
    gatewayDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The gateway device. This applies to service console gateway only, it is ignored otherwise.
    ipV6DefaultGateway (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The default ipv6 gateway address
    ipV6GatewayDevice (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The ipv6 gateway device. This applies to service console gateway only, it
