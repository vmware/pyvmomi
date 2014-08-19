
vim.profile.host.DvsProfile
===========================
  The `DvsProfile <vim/profile/host/DvsProfile.rst>`_ data object represents the distributed virtual switch to which this host is connected. If a profile plug-in defines policies or subprofiles, use the `policy <vim/profile/ApplyProfile.rst#policy>`_ or `property <vim/profile/ApplyProfile.rst#property>`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Linkable identifier.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Unique identifier for the distributed virtual switch.
    uplink ([`vim.profile.host.PnicUplinkProfile <vim/profile/host/PnicUplinkProfile.rst>`_], optional):

       List of subprofiles that map physical NICs to uplink ports. Use the `key <vim/profile/host/PnicUplinkProfile.rst#key>`_ property to access subprofiles in the list.
