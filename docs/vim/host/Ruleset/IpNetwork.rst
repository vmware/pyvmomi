
vim.host.Ruleset.IpNetwork
==========================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    network (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The IPv4 or IPv6 network. All IPv4 subnet addresses are specified as strings using dotted decimal format. For example, "192.0.20.0". IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373.
    prefixLength (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The prefix length for the network. For example the prefix length for a network 10.20.120/22 is 22
