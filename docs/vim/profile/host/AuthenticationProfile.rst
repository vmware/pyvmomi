.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _vSphere API 4.1: ../../../vim/version.rst#vimversionversion6

.. _AuthenticationProfile: ../../../vim/profile/host/AuthenticationProfile.rst

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.host.ActiveDirectoryProfile: ../../../vim/profile/host/ActiveDirectoryProfile.rst


vim.profile.host.AuthenticationProfile
======================================
  The `AuthenticationProfile`_ data object represents the host configuration for authentication. If a profile plug-in defines policies or subprofiles, use the `policy`_ or `property`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.1`_

Attributes:
    activeDirectory (`vim.profile.host.ActiveDirectoryProfile`_, optional):

       Subprofile representing the Active Directory configuration.
