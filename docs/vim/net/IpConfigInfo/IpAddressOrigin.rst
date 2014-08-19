vim.net.IpConfigInfo.IpAddressOrigin
====================================
  This specifies how an IP address was obtained for a given interface. See RFC 4293 IpAddressOriginTC.
  :contained by: `vim.net.IpConfigInfo <vim/net/IpConfigInfo.rst>`_

  :type: `vim.net.IpConfigInfo.IpAddressOrigin <vim/net/IpConfigInfo/IpAddressOrigin.rst>`_

  :name: random

values:
--------

random
   The address is chosen by the system at random e.g., an IPv4 address within 169.254/16, or an RFC 3041 privacy address.

dhcp
   The address is configured through dhcp.

other
   Any other type of address configuration other than the below mentioned ones will fall under this category. For e.g., automatic address configuration for the link local address falls under this type.

manual
   The address is configured manually. The term 'static' is a synonym.

linklayer
   The address is obtained through stateless autoconfiguration (autoconf). See RFC 4862, IPv6 Stateless Address Autoconfiguration.
