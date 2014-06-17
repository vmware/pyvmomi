.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _NetStackInstanceProfile: ../../../vim/profile/host/NetStackInstanceProfile.rst

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.host.IpRouteProfile: ../../../vim/profile/host/IpRouteProfile.rst

.. _vim.profile.host.NetworkProfile.DnsConfigProfile: ../../../vim/profile/host/NetworkProfile/DnsConfigProfile.rst


vim.profile.host.NetStackInstanceProfile
========================================
  The `NetStackInstanceProfile`_ data object represents a subprofile for a netStackInstance.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 5.5`_

Attributes:
    key (`str`_):

       Linkable identifier.
    dnsConfig (`vim.profile.host.NetworkProfile.DnsConfigProfile`_):

       DnsConfigProfile for this instance of the stack.
    ipRouteConfig (`vim.profile.host.IpRouteProfile`_):

       IpRouteProfile for this instance of the stack.
