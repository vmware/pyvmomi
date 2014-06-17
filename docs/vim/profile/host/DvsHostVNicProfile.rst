.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _ipConfig: ../../../vim/profile/host/DvsVNicProfile.rst#ipConfig

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _DvsHostVNicProfile: ../../../vim/profile/host/DvsHostVNicProfile.rst

.. _vim.profile.host.DvsVNicProfile: ../../../vim/profile/host/DvsVNicProfile.rst


vim.profile.host.DvsHostVNicProfile
===================================
  The `DvsHostVNicProfile`_ data object describes the IP configuration for a host Virtual NIC connected to a distributed virtual switch. The `ipConfig`_ property contains the Virtual NIC IP address. If a profile plug-in defines policies or subprofiles, use the `policy`_ or `property`_ list to access the additional configuration data.
:extends: vim.profile.host.DvsVNicProfile_
:since: `vSphere API 4.0`_

Attributes:
