
vim.profile.host.SecurityProfile
================================
  The `SecurityProfile <vim/profile/host/SecurityProfile.rst>`_ data object represents host security configuration. If a profile plug-in defines policies or subprofiles, use the `policy <vim/profile/ApplyProfile.rst#policy>`_ or `property <vim/profile/ApplyProfile.rst#property>`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    permission ([`vim.profile.host.PermissionProfile <vim/profile/host/PermissionProfile.rst>`_], optional):

       Permission configuration.
