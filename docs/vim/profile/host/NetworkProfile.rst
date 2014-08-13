.. _NetworkProfile: ../../../vim/profile/host/NetworkProfile.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _VmPortGroupProfile: ../../../vim/profile/host/VmPortGroupProfile.rst

.. _DvsHostVNicProfile: ../../../vim/profile/host/DvsHostVNicProfile.rst

.. _HostPortGroupProfile: ../../../vim/profile/host/HostPortGroupProfile.rst

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.host.DvsProfile: ../../../vim/profile/host/DvsProfile.rst

.. _DvsServiceConsoleVNicProfile: ../../../vim/profile/host/DvsServiceConsoleVNicProfile.rst

.. _vim.profile.host.IpRouteProfile: ../../../vim/profile/host/IpRouteProfile.rst

.. _vim.profile.host.PhysicalNicProfile: ../../../vim/profile/host/PhysicalNicProfile.rst

.. _vim.profile.host.DvsHostVNicProfile: ../../../vim/profile/host/DvsHostVNicProfile.rst

.. _vim.profile.host.VmPortGroupProfile: ../../../vim/profile/host/VmPortGroupProfile.rst

.. _vim.profile.host.HostPortGroupProfile: ../../../vim/profile/host/HostPortGroupProfile.rst

.. _vim.profile.host.VirtualSwitchProfile: ../../../vim/profile/host/VirtualSwitchProfile.rst

.. _vim.profile.host.NetStackInstanceProfile: ../../../vim/profile/host/NetStackInstanceProfile.rst

.. _vim.profile.host.DvsServiceConsoleVNicProfile: ../../../vim/profile/host/DvsServiceConsoleVNicProfile.rst

.. _vim.profile.host.ServiceConsolePortGroupProfile: ../../../vim/profile/host/ServiceConsolePortGroupProfile.rst

.. _vim.profile.host.NetworkProfile.DnsConfigProfile: ../../../vim/profile/host/NetworkProfile/DnsConfigProfile.rst


vim.profile.host.NetworkProfile
===============================
  The `NetworkProfile`_ data object contains a set of subprofiles for network configuration.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0`_

Attributes:
    vswitch ([`vim.profile.host.VirtualSwitchProfile`_], optional):

       List of virtual switch subprofiles. Use the `key`_ property to access a subprofile in the list.
    vmPortGroup ([`vim.profile.host.VmPortGroupProfile`_], optional):

       List of port groups for use by virtual machines. Use the `VmPortGroupProfile`_ . `key`_ property to access a port group in the list.
    hostPortGroup ([`vim.profile.host.HostPortGroupProfile`_], optional):

       List of port groups for use by the host. Use the `HostPortGroupProfile`_ . `key`_ property to access port groups in the list.
    serviceConsolePortGroup ([`vim.profile.host.ServiceConsolePortGroupProfile`_], optional):

       List of port groups for use by the service console. The Profile Engine uses this field only when applying a profile to a host that has a service console.
    dnsConfig (`vim.profile.host.NetworkProfile.DnsConfigProfile`_, optional):

       DNS (Domain Name System) configuration subprofile.
    ipRouteConfig (`vim.profile.host.IpRouteProfile`_, optional):

       Subprofile that describes the IP Route configuration for the VMKernel gateway.
    consoleIpRouteConfig (`vim.profile.host.IpRouteProfile`_, optional):

       Subprofile that describes the IP Route configuration for the Service Console gateway.
    pnic ([`vim.profile.host.PhysicalNicProfile`_], optional):

       List of subprofiles that represent physical NIC configuration. Use the `key`_ property to access a subprofile in the list.
    dvswitch ([`vim.profile.host.DvsProfile`_], optional):

       List of subprofiles for distributed virtual switches to which this host is connected. Use the `key`_ property to access a subprofile in the list.
    dvsServiceConsoleNic ([`vim.profile.host.DvsServiceConsoleVNicProfile`_], optional):

       List of subprofiles for service console Virtual NICs connected to a distributed virtual switch. Use the `DvsServiceConsoleVNicProfile`_ . `key`_ property to access a subprofile in the list.
    dvsHostNic ([`vim.profile.host.DvsHostVNicProfile`_], optional):

       List of subprofiles for host Virtual NICs connected to a distributed virtual switch. Use the `DvsHostVNicProfile`_ . `key`_ property to access a subprofile in the list.
    netStackInstance ([`vim.profile.host.NetStackInstanceProfile`_], optional):

       List of NetStackInstance subprofiles. Use the `key`_ property to access a subprofile in the list.
