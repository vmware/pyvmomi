.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _datetime: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _HostConfigChangeOperation: ../../../vim/host/ConfigChange/Operation.rst

.. _HostIpConfigIpV6AddressStatus: ../../../vim/host/IpConfig/IpV6AddressStatus.rst

.. _HostIpConfigIpV6AddressConfigType: ../../../vim/host/IpConfig/IpV6AddressConfigType.rst


vim.host.IpConfig.IpV6Address
=============================
  The ipv6 address specification
:extends: vmodl.DynamicData_
:since: `vSphere API 4.0`_

Attributes:
    ipAddress (`str`_):

       The ipv6 address. When DHCP is enabled, this property reflects the current IP configuration and cannot be set.
    prefixLength (`int`_):

       The prefix length. An ipv6 prefixLength is a decimal value that indicates the number of contiguous, higher-order bits of the address that make up the network portion of the address. For example, 10FA:6604:8136:6502::/64 is a possible IPv6 prefix. The prefix length in this case is 64.
    origin (`str`_, optional):

       The type of the ipv6 address configuration on the interface. This can be one of the types defined my the enum `HostIpConfigIpV6AddressConfigType`_ .
    dadState (`str`_, optional):

       The state of this ipAddress. Can be one of `HostIpConfigIpV6AddressStatus`_ 
    lifetime (`datetime`_, optional):

       The time when will this address expire. If not set the address lifetime is unlimited.
    operation (`str`_, optional):

       Valid values are "add" and "remove". See `HostConfigChangeOperation`_ .
