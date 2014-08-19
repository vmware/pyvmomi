
vim.host.NatService.Specification
=================================
  This data object type provides the details about the Network Address Translation (NAT) service.
:extends: vmodl.DynamicData_
:since: `VI API 2.5 <vim/version.rst#vimversionversion2>`_

Attributes:
    virtualSwitch (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The name of the virtual switch to which nat service is connected.
    activeFtp (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not non-passive mode FTP connections should be allowed.
    allowAnyOui (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not the NAT Service allows media access control traffic from any Organizational Unique Identifier (OUI)? By default, it does not allow traffic that originated from the host to avoid packet loops.
    configPort (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not the NAT Service should open a configuration port.
    ipGatewayAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       The IP address that the NAT Service should use on the virtual network.
    udpTimeout (`int <https://docs.python.org/2/library/stdtypes.html>`_):

       The time allotted for UDP packets.
    portForward ([`vim.host.NatService.PortForwardSpecification <vim/host/NatService/PortForwardSpecification.rst>`_], optional):

       The port forwarding specifications to allow network connections to be initiated from outside the firewall.
    nameService (`vim.host.NatService.NameServiceSpec <vim/host/NatService/NameServiceSpec.rst>`_, optional):

       The configuration of naming services. These parameters are specific to Windows.
