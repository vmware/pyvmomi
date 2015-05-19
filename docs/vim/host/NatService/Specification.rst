.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _VI API 2.5: ../../../vim/version.rst#vimversionversion2

.. _vmodl.DynamicData: ../../../vmodl/DynamicData.rst

.. _vim.host.NatService.NameServiceSpec: ../../../vim/host/NatService/NameServiceSpec.rst

.. _vim.host.NatService.PortForwardSpecification: ../../../vim/host/NatService/PortForwardSpecification.rst


vim.host.NatService.Specification
=================================
  This data object type provides the details about the Network Address Translation (NAT) service.
:extends: vmodl.DynamicData_
:since: `VI API 2.5`_

Attributes:
    virtualSwitch (`str`_):

       The name of the virtual switch to which nat service is connected.
    activeFtp (`bool`_):

       The flag to indicate whether or not non-passive mode FTP connections should be allowed.
    allowAnyOui (`bool`_):

       The flag to indicate whether or not the NAT Service allows media access control traffic from any Organizational Unique Identifier (OUI)? By default, it does not allow traffic that originated from the host to avoid packet loops.
    configPort (`bool`_):

       The flag to indicate whether or not the NAT Service should open a configuration port.
    ipGatewayAddress (`str`_):

       The IP address that the NAT Service should use on the virtual network.
    udpTimeout (`int`_):

       The time allotted for UDP packets.
    portForward ([`vim.host.NatService.PortForwardSpecification`_], optional):

       The port forwarding specifications to allow network connections to be initiated from outside the firewall.
    nameService (`vim.host.NatService.NameServiceSpec`_, optional):

       The configuration of naming services. These parameters are specific to Windows.
