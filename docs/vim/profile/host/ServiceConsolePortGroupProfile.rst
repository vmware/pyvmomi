
vim.profile.host.ServiceConsolePortGroupProfile
===============================================
  The `ServiceConsolePortGroupProfile <vim/profile/host/ServiceConsolePortGroupProfile.rst>`_ data object represents the profile for a port group that will be used by the service console. If a profile plug-in defines policies or subprofiles, use the `policy <vim/profile/ApplyProfile.rst#policy>`_ or `property <vim/profile/ApplyProfile.rst#property>`_ list to access the additional configuration data.
:extends: vim.profile.host.PortGroupProfile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    ipConfig (`vim.profile.host.IpAddressProfile <vim/profile/host/IpAddressProfile.rst>`_):

       IP address configuration for the service console network.
