
vim.profile.host.AuthenticationProfile
======================================
  The `AuthenticationProfile <vim/profile/host/AuthenticationProfile.rst>`_ data object represents the host configuration for authentication. If a profile plug-in defines policies or subprofiles, use the `policy <vim/profile/ApplyProfile.rst#policy>`_ or `property <vim/profile/ApplyProfile.rst#property>`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    activeDirectory (`vim.profile.host.ActiveDirectoryProfile <vim/profile/host/ActiveDirectoryProfile.rst>`_, optional):

       Subprofile representing the Active Directory configuration.
