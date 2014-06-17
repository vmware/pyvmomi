.. _str: https://docs.python.org/2/library/stdtypes.html

.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _NasStorageProfile: ../../../vim/profile/host/NasStorageProfile.rst

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst


vim.profile.host.NasStorageProfile
==================================
  The `NasStorageProfile`_ data object represents one NAS datastore configuration. Use the `policy`_ list for access to configuration data for the NAS storage profile. Use the `property`_ list for access to subprofile configuration data, if any.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       Linkable identifier.
