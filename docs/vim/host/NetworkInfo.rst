.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vmodl.DynamicData: ../../vmodl/DynamicData.rst

.. _vim.host.PortGroup: ../../vim/host/PortGroup.rst

.. _vim.host.DnsConfig: ../../vim/host/DnsConfig.rst

.. _vim.host.VirtualNic: ../../vim/host/VirtualNic.rst

.. _vim.host.NatService: ../../vim/host/NatService.rst

.. _vim.host.PhysicalNic: ../../vim/host/PhysicalNic.rst

.. _vim.host.DhcpService: ../../vim/host/DhcpService.rst

.. _vim.host.OpaqueSwitch: ../../vim/host/OpaqueSwitch.rst

.. _vim.host.VirtualSwitch: ../../vim/host/VirtualSwitch.rst

.. _vim.host.IpRouteConfig: ../../vim/host/IpRouteConfig.rst

.. _vim.host.HostProxySwitch: ../../vim/host/HostProxySwitch.rst

.. _vim.host.IpRouteTableInfo: ../../vim/host/IpRouteTableInfo.rst

.. _vim.host.NetStackInstance: ../../vim/host/NetStackInstance.rst

.. _vim.host.OpaqueNetworkInfo: ../../vim/host/OpaqueNetworkInfo.rst


vim.host.NetworkInfo
====================
  This data object type describes networking host configuration data objects.
:extends: vmodl.DynamicData_

Attributes:
    vswitch (`vim.host.VirtualSwitch`_, optional):

       Virtual switches configured on the host.
    proxySwitch (`vim.host.HostProxySwitch`_, optional):

       Proxy switches configured on the host.
    portgroup (`vim.host.PortGroup`_, optional):

       Port groups configured on the host.
    pnic (`vim.host.PhysicalNic`_, optional):

       Physical network adapters as seen by the primary operating system.
    vnic (`vim.host.VirtualNic`_, optional):

       Virtual network adapters configured on the host (hosted products) or the vmkernel. In the hosted architecture, these network adapters are used by the host to communicate with the virtual machines running on that host. In the VMkernel architecture, these virtual network adapters provide the ESX Server with external network access through a virtual switch that is bridged to a physical network adapter. The VMkernel uses these network adapters for features such as VMotion, NAS, iSCSI, and remote MKS connections.
    consoleVnic (`vim.host.VirtualNic`_, optional):

       Virtual network adapters configured for use by the service console. The service console uses this network access for system management and bootstrapping services like network boot. The two sets of virtual network adapters are mutually exclusive. A virtual network adapter in this list cannot be used for things like VMotion. Likewise, a virtual network adapter in the other list cannot be used by the service console.
    dnsConfig (`vim.host.DnsConfig`_, optional):

       Client-side DNS configuration.
    ipRouteConfig (`vim.host.IpRouteConfig`_, optional):

       IP route configuration.
    consoleIpRouteConfig (`vim.host.IpRouteConfig`_, optional):

       IP route configuration of the service console.
    routeTableInfo (`vim.host.IpRouteTableInfo`_, optional):

       IP routing table
    dhcp (`vim.host.DhcpService`_, optional):

       DHCP Service instances configured on the host.
    nat (`vim.host.NatService`_, optional):

       NAT service instances configured on the host.
    ipV6Enabled (`bool`_, optional):

       Enable or disable IPv6 protocol on this system.
    atBootIpV6Enabled (`bool`_, optional):

       If true then dual IPv4/IPv6 stack enabled else IPv4 only.
    netStackInstance (`vim.host.NetStackInstance`_, optional):

       List of NetStackInstances
    opaqueSwitch (`vim.host.OpaqueSwitch`_, optional):

       List of opaque switches configured on the host.
    opaqueNetwork (`vim.host.OpaqueNetworkInfo`_, optional):

       List of opaque networks
