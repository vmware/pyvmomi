
vim.profile.host.NetStackInstanceProfile
========================================
  The `NetStackInstanceProfile <vim/profile/host/NetStackInstanceProfile.rst>`_ data object represents a subprofile for a netStackInstance.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Linkable identifier.
    dnsConfig (`vim.profile.host.NetworkProfile.DnsConfigProfile <vim/profile/host/NetworkProfile/DnsConfigProfile.rst>`_):

       DnsConfigProfile for this instance of the stack.
    ipRouteConfig (`vim.profile.host.IpRouteProfile <vim/profile/host/IpRouteProfile.rst>`_):

       IpRouteProfile for this instance of the stack.
