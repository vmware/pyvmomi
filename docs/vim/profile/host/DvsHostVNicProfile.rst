
vim.profile.host.DvsHostVNicProfile
===================================
  The `DvsHostVNicProfile <vim/profile/host/DvsHostVNicProfile.rst>`_ data object describes the IP configuration for a host Virtual NIC connected to a distributed virtual switch. The `ipConfig <vim/profile/host/DvsVNicProfile.rst#ipConfig>`_ property contains the Virtual NIC IP address. If a profile plug-in defines policies or subprofiles, use the `policy <vim/profile/ApplyProfile.rst#policy>`_ or `property <vim/profile/ApplyProfile.rst#property>`_ list to access the additional configuration data.
:extends: vim.profile.host.DvsVNicProfile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
