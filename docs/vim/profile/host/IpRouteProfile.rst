.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _IpRouteProfile: ../../../vim/profile/host/IpRouteProfile.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.host.StaticRouteProfile: ../../../vim/profile/host/StaticRouteProfile.rst


vim.profile.host.IpRouteProfile
===============================
  The `IpRouteProfile`_ data object represents the host IP route configuration. If a profile plug-in defines policies or subprofiles, use the `policy`_ or `property`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0`_

Attributes:
    staticRoute ([`vim.profile.host.StaticRouteProfile`_], optional):

       List of static routes to be configured.
