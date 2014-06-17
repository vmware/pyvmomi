.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostConfigChangeOperation: ../../../vim/host/ConfigChange/Operation.rst

.. _vim.net.IpRouteConfigSpec.GatewaySpec: ../../../vim/net/IpRouteConfigSpec/GatewaySpec.rst


vim.net.IpRouteConfigSpec.IpRouteSpec
=====================================
  Specify an individual host, network or default destination network reachable through a given gateway.
:extends: vmodl.DynamicData_
:since: `vSphere API 4.1`_

Attributes:
    network (`str`_):

       IP Address of the destination IP network. IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373. To Specify a default network use the value: 0 with prefixLenth 0.
    prefixLength (`int`_):

       The prefix length. For IPv4 the value range is 0-31. For IPv6 prefixLength is a decimal value range 0-127. The property represents the number of contiguous, higher-order bits of the address that make up the network portion of the IP address.
    gateway (`vim.net.IpRouteConfigSpec.GatewaySpec`_):

       Where to send the packets for this route.
    operation (`str`_):

       Requires one of the values from `HostConfigChangeOperation`_ .
