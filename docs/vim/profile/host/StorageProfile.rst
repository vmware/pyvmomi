
vim.profile.host.StorageProfile
===============================
  The `StorageProfile <vim/profile/host/StorageProfile.rst>`_ data object represents the host storage configuration. If a profile plug-in defines policies or subprofiles, use the `policy <vim/profile/ApplyProfile.rst#policy>`_ or `property <vim/profile/ApplyProfile.rst#property>`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    nasStorage ([`vim.profile.host.NasStorageProfile <vim/profile/host/NasStorageProfile.rst>`_], optional):

       List of NAS storage subprofiles. Use the `key <vim/profile/host/NasStorageProfile.rst#key>`_ property to access a subprofile in the list.
