.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _NetworkInfo: ../../vim/host/NetworkInfo.rst

.. _HostNetworkInfo: ../../vim/host/NetworkInfo.rst

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.DnsConfig: ../../vim/host/DnsConfig.rst

.. _vim.host.IpRouteConfig: ../../vim/host/IpRouteConfig.rst

.. _vim.host.PortGroup.Config: ../../vim/host/PortGroup/Config.rst

.. _vim.host.NatService.Config: ../../vim/host/NatService/Config.rst

.. _vim.host.VirtualNic.Config: ../../vim/host/VirtualNic/Config.rst

.. _vim.host.PhysicalNic.Config: ../../vim/host/PhysicalNic/Config.rst

.. _vim.host.IpRouteTableConfig: ../../vim/host/IpRouteTableConfig.rst

.. _vim.host.DhcpService.Config: ../../vim/host/DhcpService/Config.rst

.. _vim.host.VirtualSwitch.Config: ../../vim/host/VirtualSwitch/Config.rst

.. _vim.host.HostProxySwitch.Config: ../../vim/host/HostProxySwitch/Config.rst

.. _vim.host.NetworkConfig.NetStackSpec: ../../vim/host/NetworkConfig/NetStackSpec.rst


vim.host.NetworkConfig
======================
  This data object type describes networking host configuration data objects. These objects contain only the configuration information for networking. The runtime information is available from the `NetworkInfo`_ data object type.See `HostNetworkInfo`_ 
:extends: vmodl.DynamicData_

Attributes:
    vswitch (`vim.host.VirtualSwitch.Config`_, optional):

       Virtual switches configured on the host.
    proxySwitch (`vim.host.HostProxySwitch.Config`_, optional):

       Host proxy switches configured on the host.
    portgroup (`vim.host.PortGroup.Config`_, optional):

       Port groups configured on the host.
    pnic (`vim.host.PhysicalNic.Config`_, optional):

       Physical network adapters as seen by the primary operating system.
    vnic (`vim.host.VirtualNic.Config`_, optional):

       Virtual network adapters configured for use by the host operating system network adapter.
    consoleVnic (`vim.host.VirtualNic.Config`_, optional):

       Virtual network adapters configured for use by the Service Console.
    dnsConfig (`vim.host.DnsConfig`_, optional):

       Client-side DNS configuration for the host. The DNS configuration is global to the entire host.
    ipRouteConfig (`vim.host.IpRouteConfig`_, optional):

       IP route configuration of the host.
    consoleIpRouteConfig (`vim.host.IpRouteConfig`_, optional):

       IP route configuration of the service console.
    routeTableConfig (`vim.host.IpRouteTableConfig`_, optional):

       IP routing table configuration of the host.
    dhcp (`vim.host.DhcpService.Config`_, optional):

       Dynamic Host Control Protocol (DHCP) Service instances configured on the host.
    nat (`vim.host.NatService.Config`_, optional):

       Network address translation (NAT) Service instances configured on the host.
    ipV6Enabled (`bool`_, optional):

       Enable or disable IPv6 protocol on this system. This property must be set by itself, no other property can accompany this change. Following the successful change, the system should be rebooted to have the change take effect.
    netStackSpec (`vim.host.NetworkConfig.NetStackSpec`_, optional):

       The list of network stack instance spec
