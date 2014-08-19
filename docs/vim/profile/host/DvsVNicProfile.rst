
vim.profile.host.DvsVNicProfile
===============================
  The `DvsVNicProfile <vim/profile/host/DvsVNicProfile.rst>`_ data object is the base object for host and service console Virtual NIC subprofiles. If a profile plug-in defines additional policies or subprofiles, use the `policy <vim/profile/ApplyProfile.rst#policy>`_ or `property <vim/profile/ApplyProfile.rst#property>`_ list to access the configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Linkable identifier.
    ipConfig (`vim.profile.host.IpAddressProfile <vim/profile/host/IpAddressProfile.rst>`_):

       IP address for a distributed virtual switch Virtual NIC.
