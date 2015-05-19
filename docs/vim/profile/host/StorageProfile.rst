.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _StorageProfile: ../../../vim/profile/host/StorageProfile.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.host.NasStorageProfile: ../../../vim/profile/host/NasStorageProfile.rst


vim.profile.host.StorageProfile
===============================
  The `StorageProfile`_ data object represents the host storage configuration. If a profile plug-in defines policies or subprofiles, use the `policy`_ or `property`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0`_

Attributes:
    nasStorage ([`vim.profile.host.NasStorageProfile`_], optional):

       List of NAS storage subprofiles. Use the `key`_ property to access a subprofile in the list.
