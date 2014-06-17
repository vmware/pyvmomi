.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.net.IpConfigInfo.IpAddress
==============================
  Information about a specific IP Address.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    ipAddress (`str`_):

       IPv4 address is specified using dotted decimal notation. For example, "192.0.2.1". IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373.
    prefixLength (`int`_):

       Denotes the length of a generic Internet network address prefix. The prefix length for IPv4 the value range is 0-32. For IPv6 prefixLength is a decimal value range 0-128. A value of n corresponds to an IP address mask that has n contiguous 1-bits from the most significant bit (MSB), with all other bits set to 0. A value of zero is valid only if the calling context defines it.
    origin (`str`_, optional):

       How this address was configured. This can be one of the values from the enum IpAddressOrigin See IpAddressOrigin for values.
    state (`str`_, optional):

       The state of this ipAddress. Can be one of IpAddressStatus.
    lifetime (`datetime`_, optional):

       The time when will this address expire. Durning this time state may change states but is still visible from the network.
