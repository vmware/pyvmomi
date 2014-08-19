
vim.host.NatService.PortForwardSpecification
============================================
  This data object type describes the Network Address Translation (NAT) port forwarding specification.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    type (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Either "tcp" or "udp".
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The user-defined name to identify the service being forwarded. No white spaces are allowed in the string.
    hostPort (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The port number on the host. Network traffic sent to the host on this TCP/UDP port is forwarded to the guest at the specified IP address and port.
    guestPort (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The port number for the guest. Network traffic from the host is forwarded to this port.
    guestIpAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The IP address for the guest. Network traffic from the host is forwarded to this IP address.
