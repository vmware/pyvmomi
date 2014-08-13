.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _SecurityProfile: ../../../vim/profile/host/SecurityProfile.rst

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.host.PermissionProfile: ../../../vim/profile/host/PermissionProfile.rst


vim.profile.host.SecurityProfile
================================
  The `SecurityProfile`_ data object represents host security configuration. If a profile plug-in defines policies or subprofiles, use the `policy`_ or `property`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0`_

Attributes:
    permission ([`vim.profile.host.PermissionProfile`_], optional):

       Permission configuration.
