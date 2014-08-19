
vim.profile.host.VirtualSwitchProfile
=====================================
  The `VirtualSwitchProfile <vim/profile/host/VirtualSwitchProfile.rst>`_ data object represents a subprofile for a virtual switch. If a profile plug-in defines policies or subprofiles, use the `policy <vim/profile/ApplyProfile.rst#policy>`_ or `property <vim/profile/ApplyProfile.rst#property>`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Linkable identifier.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the virtual switch.
    link (`vim.profile.host.VirtualSwitchProfile.LinkProfile <vim/profile/host/VirtualSwitchProfile/LinkProfile.rst>`_):

       Links that are connected to the virtual switch.
    numPorts (`vim.profile.host.VirtualSwitchProfile.NumPortsProfile <vim/profile/host/VirtualSwitchProfile/NumPortsProfile.rst>`_):

       Number of ports on the virtual switch.
    networkPolicy (`vim.profile.host.NetworkPolicyProfile <vim/profile/host/NetworkPolicyProfile.rst>`_):

       Network policy for the virtual switch.
