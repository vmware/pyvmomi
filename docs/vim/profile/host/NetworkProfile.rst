
vim.profile.host.NetworkProfile
===============================
  The `NetworkProfile <vim/profile/host/NetworkProfile.rst>`_ data object contains a set of subprofiles for network configuration.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    vswitch ([`vim.profile.host.VirtualSwitchProfile <vim/profile/host/VirtualSwitchProfile.rst>`_], optional):

       List of virtual switch subprofiles. Use the `key <vim/profile/host/VirtualSwitchProfile.rst#key>`_ property to access a subprofile in the list.
    vmPortGroup ([`vim.profile.host.VmPortGroupProfile <vim/profile/host/VmPortGroupProfile.rst>`_], optional):

       List of port groups for use by virtual machines. Use the `VmPortGroupProfile <vim/profile/host/VmPortGroupProfile.rst>`_ . `key <vim/profile/host/PortGroupProfile.rst#key>`_ property to access a port group in the list.
    hostPortGroup ([`vim.profile.host.HostPortGroupProfile <vim/profile/host/HostPortGroupProfile.rst>`_], optional):

       List of port groups for use by the host. Use the `HostPortGroupProfile <vim/profile/host/HostPortGroupProfile.rst>`_ . `key <vim/profile/host/PortGroupProfile.rst#key>`_ property to access port groups in the list.
    serviceConsolePortGroup ([`vim.profile.host.ServiceConsolePortGroupProfile <vim/profile/host/ServiceConsolePortGroupProfile.rst>`_], optional):

       List of port groups for use by the service console. The Profile Engine uses this field only when applying a profile to a host that has a service console.
    dnsConfig (`vim.profile.host.NetworkProfile.DnsConfigProfile <vim/profile/host/NetworkProfile/DnsConfigProfile.rst>`_, optional):

       DNS (Domain Name System) configuration subprofile.
    ipRouteConfig (`vim.profile.host.IpRouteProfile <vim/profile/host/IpRouteProfile.rst>`_, optional):

       Subprofile that describes the IP Route configuration for the VMKernel gateway.
    consoleIpRouteConfig (`vim.profile.host.IpRouteProfile <vim/profile/host/IpRouteProfile.rst>`_, optional):

       Subprofile that describes the IP Route configuration for the Service Console gateway.
    pnic ([`vim.profile.host.PhysicalNicProfile <vim/profile/host/PhysicalNicProfile.rst>`_], optional):

       List of subprofiles that represent physical NIC configuration. Use the `key <vim/profile/host/PhysicalNicProfile.rst#key>`_ property to access a subprofile in the list.
    dvswitch ([`vim.profile.host.DvsProfile <vim/profile/host/DvsProfile.rst>`_], optional):

       List of subprofiles for distributed virtual switches to which this host is connected. Use the `key <vim/profile/host/DvsProfile.rst#key>`_ property to access a subprofile in the list.
    dvsServiceConsoleNic ([`vim.profile.host.DvsServiceConsoleVNicProfile <vim/profile/host/DvsServiceConsoleVNicProfile.rst>`_], optional):

       List of subprofiles for service console Virtual NICs connected to a distributed virtual switch. Use the `DvsServiceConsoleVNicProfile <vim/profile/host/DvsServiceConsoleVNicProfile.rst>`_ . `key <vim/profile/host/DvsVNicProfile.rst#key>`_ property to access a subprofile in the list.
    dvsHostNic ([`vim.profile.host.DvsHostVNicProfile <vim/profile/host/DvsHostVNicProfile.rst>`_], optional):

       List of subprofiles for host Virtual NICs connected to a distributed virtual switch. Use the `DvsHostVNicProfile <vim/profile/host/DvsHostVNicProfile.rst>`_ . `key <vim/profile/host/DvsVNicProfile.rst#key>`_ property to access a subprofile in the list.
    netStackInstance ([`vim.profile.host.NetStackInstanceProfile <vim/profile/host/NetStackInstanceProfile.rst>`_], optional):

       List of NetStackInstance subprofiles. Use the `key <vim/profile/host/NetStackInstanceProfile.rst#key>`_ property to access a subprofile in the list.
