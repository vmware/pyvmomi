.. _str: https://docs.python.org/2/library/stdtypes.html

.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _DvsProfile: ../../../vim/profile/host/DvsProfile.rst

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.host.PnicUplinkProfile: ../../../vim/profile/host/PnicUplinkProfile.rst


vim.profile.host.DvsProfile
===========================
  The `DvsProfile`_ data object represents the distributed virtual switch to which this host is connected. If a profile plug-in defines policies or subprofiles, use the `policy`_ or `property`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       Linkable identifier.
    name (`str`_):

       Unique identifier for the distributed virtual switch.
    uplink ([`vim.profile.host.PnicUplinkProfile`_], optional):

       List of subprofiles that map physical NICs to uplink ports. Use the `key`_ property to access subprofiles in the list.
