.. _str: https://docs.python.org/2/library/stdtypes.html

.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _ServiceProfile: ../../../vim/profile/host/ServiceProfile.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst


vim.profile.host.ServiceProfile
===============================
  The `ServiceProfile`_ data object controls the configuration of a service. Use the `policy`_ list for access to configuration data for the service profile. Use the `property`_ list for access to subprofiles, if any.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       Linkable identifier.
