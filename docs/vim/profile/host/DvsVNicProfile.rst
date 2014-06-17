.. _str: https://docs.python.org/2/library/stdtypes.html

.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _DvsVNicProfile: ../../../vim/profile/host/DvsVNicProfile.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.host.IpAddressProfile: ../../../vim/profile/host/IpAddressProfile.rst


vim.profile.host.DvsVNicProfile
===============================
  The `DvsVNicProfile`_ data object is the base object for host and service console Virtual NIC subprofiles. If a profile plug-in defines additional policies or subprofiles, use the `policy`_ or `property`_ list to access the configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       Linkable identifier.
    ipConfig (`vim.profile.host.IpAddressProfile`_):

       IP address for a distributed virtual switch Virtual NIC.
