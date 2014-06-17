.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst


vim.net.DnsConfigInfo
=====================
  Domain Name Server (DNS) Configuration Specification - a data object for reporting the configuration of RFC 1034 client side DNS settings.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    dhcp (`bool`_):

       Indicates whether or not dynamic host control protocol (DHCP) is used to configure DNS configuration.
    hostName (`str`_):

       The host name portion of DNS name. For example, "esx01" part of esx01.example.com.
    domainName (`str`_):

       The domain name portion of the DNS name. "example.com" part of esx01.example.com.
    ipAddress (`str`_, optional):

       The IP addresses of the DNS servers in order of use. IPv4 addresses are specified using dotted decimal notation. For example, "192.0.2.1". IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373.
    searchDomain (`str`_, optional):

       The domain in which to search for hosts, placed in order of preference.
