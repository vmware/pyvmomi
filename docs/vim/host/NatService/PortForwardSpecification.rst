.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst


vim.host.NatService.PortForwardSpecification
============================================
  This data object type describes the Network Address Translation (NAT) port forwarding specification.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    type (`str`_):

       Either "tcp" or "udp".
    name (`str`_):

       The user-defined name to identify the service being forwarded. No white spaces are allowed in the string.
    hostPort (`int`_):

       The port number on the host. Network traffic sent to the host on this TCP/UDP port is forwarded to the guest at the specified IP address and port.
    guestPort (`int`_):

       The port number for the guest. Network traffic from the host is forwarded to this port.
    guestIpAddress (`str`_):

       The IP address for the guest. Network traffic from the host is forwarded to this IP address.
