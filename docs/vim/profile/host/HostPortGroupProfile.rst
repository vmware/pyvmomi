.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _HostPortGroupProfile: ../../../vim/profile/host/HostPortGroupProfile.rst

.. _vim.profile.host.PortGroupProfile: ../../../vim/profile/host/PortGroupProfile.rst

.. _vim.profile.host.IpAddressProfile: ../../../vim/profile/host/IpAddressProfile.rst


vim.profile.host.HostPortGroupProfile
=====================================
  The `HostPortGroupProfile`_ data object represents the subprofile for a port group that will be used by the ESX host. If a profile plug-in defines policies or subprofiles, use the `policy`_ or `property`_ list to access the additional configuration data.
:extends: vim.profile.host.PortGroupProfile_
:since: `vSphere API 4.0`_

Attributes:
    ipConfig (`vim.profile.host.IpAddressProfile`_):

       IP address configuration for the Host network.
