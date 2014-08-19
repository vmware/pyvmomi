vim.host.IpConfig.IpV6AddressConfigType
=======================================
  This specifies how the ipv6 address is configured for the interface. We follow rfc4293 in defining the values for the configType.
  :contained by: `vim.host.IpConfig <vim/host/IpConfig.rst>`_

  :type: `vim.host.IpConfig.IpV6AddressConfigType <vim/host/IpConfig/IpV6AddressConfigType.rst>`_

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
   The address is configured manually.

linklayer
   The address is obtained through stateless autoconfiguration.
