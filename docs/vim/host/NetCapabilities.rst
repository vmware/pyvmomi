
vim.host.NetCapabilities
========================
  Capability vector indicating the available product features.
:extends: vmodl.DynamicData_

Attributes:
    canSetPhysicalNicLinkSpeed (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not a physical network adapter's link speed and duplex settings can be changed through this API. For a hosted product, the host uses its physical network adapters for network connectivity. Configuration of link speed is done through regular host operations. In ESX Server, the configuration can be changed through this API.
    supportsNicTeaming (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not network adapter teaming is available. Multiple network adapters can be bridged to a virtual switch through a BondBridge. Also, network adapter teaming policies such as failover order and detection are enabled.
    nicTeamingPolicy ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       The available teaming policies if the platform supports network adapter teaming.
    supportsVlan (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not VLANs can be configured on PortGroups attached to VirtualSwitch objects. This allows VLANs for virtual machines without requiring special VLAN capable hardware switches.
    usesServiceConsoleNic (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not a service console network adapter is used or required. This means that the system software has two TCP/IP stacks. As a result, at least two types of VirtualNics may be created -- the normal VirtualNic and the service console VirtualNic. If this is not set, then only the VirtualNic type is supported.
    supportsNetworkHints (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether or not the host is able to support the querying of network hints.
    maxPortGroupsPerVswitch (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       The maximum number of port groups supported per virtual switch. This property will not be set if this value is unlimited.
    vswitchConfigSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether virtual switch configuration is supported. This means that operations to add, remove, update virtual switches are supported.
    vnicConfigSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether Virtual NIC configuration is supported. This means that operations to add, remove, update virtualNic are supported.
    ipRouteConfigSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether ip route configuration for the host is supported.
    dnsConfigSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether DNS configuration for the host is supported.
    dhcpOnVnicSupported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       This flag indicates whether or not the host is able to support dhcp configuration for vnics.
    ipV6Supported (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       The flag to indicate whether the host is capable of communicating using ipv6 protocol
