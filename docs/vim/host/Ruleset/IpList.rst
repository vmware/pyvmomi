.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.Ruleset.IpNetwork: ../../../vim/host/Ruleset/IpNetwork.rst


vim.host.Ruleset.IpList
=======================
  
:extends: vmodl.DynamicData_
:since: `vSphere API 5.0`_

Attributes:
    ipAddress ([`str`_], optional):

       The list of ipAddresses. All IPv4 addresses are specified as strings using dotted decimal format. For example, "192.0.20.10". IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373.
    ipNetwork ([`vim.host.Ruleset.IpNetwork`_], optional):

       The list of networks
    allIp (`bool`_):

       Flag indicating whether the ruleset works for all ip addresses.
