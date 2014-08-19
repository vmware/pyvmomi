
vim.profile.host.IpRouteProfile
===============================
  The `IpRouteProfile <vim/profile/host/IpRouteProfile.rst>`_ data object represents the host IP route configuration. If a profile plug-in defines policies or subprofiles, use the `policy <vim/profile/ApplyProfile.rst#policy>`_ or `property <vim/profile/ApplyProfile.rst#property>`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    staticRoute ([`vim.profile.host.StaticRouteProfile <vim/profile/host/StaticRouteProfile.rst>`_], optional):

       List of static routes to be configured.
