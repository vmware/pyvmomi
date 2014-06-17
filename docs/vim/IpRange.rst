.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.IpAddress: ../vim/IpAddress.rst

.. _vSphere API 5.5: ../vim/version.rst#vimversionversion9


vim.IpRange
===========
  This class specifies a range of IP addresses by using prefix. Usage: 128.20.20.10/24. Here 128.20.20.10 is IP address and 24 is prefix length.
:extends: vim.IpAddress_
:since: `vSphere API 5.5`_

Attributes:
    addressPrefix (`str`_):

       IP address prefix.
    prefixLength (`int`_, optional):

       Prefix length with max value of 32 for IPv4 and 128 for IPv6.
