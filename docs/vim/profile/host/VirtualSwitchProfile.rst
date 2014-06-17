.. _str: https://docs.python.org/2/library/stdtypes.html

.. _policy: ../../../vim/profile/ApplyProfile.rst#policy

.. _property: ../../../vim/profile/ApplyProfile.rst#property

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _VirtualSwitchProfile: ../../../vim/profile/host/VirtualSwitchProfile.rst

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.host.NetworkPolicyProfile: ../../../vim/profile/host/NetworkPolicyProfile.rst

.. _vim.profile.host.VirtualSwitchProfile.LinkProfile: ../../../vim/profile/host/VirtualSwitchProfile/LinkProfile.rst

.. _vim.profile.host.VirtualSwitchProfile.NumPortsProfile: ../../../vim/profile/host/VirtualSwitchProfile/NumPortsProfile.rst


vim.profile.host.VirtualSwitchProfile
=====================================
  The `VirtualSwitchProfile`_ data object represents a subprofile for a virtual switch. If a profile plug-in defines policies or subprofiles, use the `policy`_ or `property`_ list to access the additional configuration data.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       Linkable identifier.
    name (`str`_):

       Name of the virtual switch.
    link (`vim.profile.host.VirtualSwitchProfile.LinkProfile`_):

       Links that are connected to the virtual switch.
    numPorts (`vim.profile.host.VirtualSwitchProfile.NumPortsProfile`_):

       Number of ports on the virtual switch.
    networkPolicy (`vim.profile.host.NetworkPolicyProfile`_):

       Network policy for the virtual switch.
