
vim.host.NetworkConfig
======================
  This data object type describes networking host configuration data objects. These objects contain only the configuration information for networking. The runtime information is available from the `NetworkInfo <vim/host/NetworkInfo.rst>`_ data object type.See `HostNetworkInfo <vim/host/NetworkInfo.rst>`_ 
:extends: vmodl.DynamicData_

Attributes:
    vswitch ([`vim.host.VirtualSwitch.Config <vim/host/VirtualSwitch/Config.rst>`_], optional):

       Virtual switches configured on the host.
    proxySwitch ([`vim.host.HostProxySwitch.Config <vim/host/HostProxySwitch/Config.rst>`_], optional):

       Host proxy switches configured on the host.
    portgroup ([`vim.host.PortGroup.Config <vim/host/PortGroup/Config.rst>`_], optional):

       Port groups configured on the host.
    pnic ([`vim.host.PhysicalNic.Config <vim/host/PhysicalNic/Config.rst>`_], optional):

       Physical network adapters as seen by the primary operating system.
    vnic ([`vim.host.VirtualNic.Config <vim/host/VirtualNic/Config.rst>`_], optional):

       Virtual network adapters configured for use by the host operating system network adapter.
    consoleVnic ([`vim.host.VirtualNic.Config <vim/host/VirtualNic/Config.rst>`_], optional):

       Virtual network adapters configured for use by the Service Console.
    dnsConfig (`vim.host.DnsConfig <vim/host/DnsConfig.rst>`_, optional):

       Client-side DNS configuration for the host. The DNS configuration is global to the entire host.
    ipRouteConfig (`vim.host.IpRouteConfig <vim/host/IpRouteConfig.rst>`_, optional):

       IP route configuration of the host.
    consoleIpRouteConfig (`vim.host.IpRouteConfig <vim/host/IpRouteConfig.rst>`_, optional):

       IP route configuration of the service console.
    routeTableConfig (`vim.host.IpRouteTableConfig <vim/host/IpRouteTableConfig.rst>`_, optional):

       IP routing table configuration of the host.
    dhcp ([`vim.host.DhcpService.Config <vim/host/DhcpService/Config.rst>`_], optional):

       Dynamic Host Control Protocol (DHCP) Service instances configured on the host.
    nat ([`vim.host.NatService.Config <vim/host/NatService/Config.rst>`_], optional):

       Network address translation (NAT) Service instances configured on the host.
    ipV6Enabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Enable or disable IPv6 protocol on this system. This property must be set by itself, no other property can accompany this change. Following the successful change, the system should be rebooted to have the change take effect.
    netStackSpec ([`vim.host.NetworkConfig.NetStackSpec <vim/host/NetworkConfig/NetStackSpec.rst>`_], optional):

       The list of network stack instance spec
