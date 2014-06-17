.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 4.0: ../../../vim/version.rst#vimversionversion5

.. _PortGroupProfile: ../../../vim/profile/host/PortGroupProfile.rst

.. _vim.profile.ApplyProfile: ../../../vim/profile/ApplyProfile.rst

.. _vim.profile.host.NetworkPolicyProfile: ../../../vim/profile/host/NetworkPolicyProfile.rst

.. _vim.profile.host.PortGroupProfile.VlanProfile: ../../../vim/profile/host/PortGroupProfile/VlanProfile.rst

.. _vim.profile.host.PortGroupProfile.VirtualSwitchSelectionProfile: ../../../vim/profile/host/PortGroupProfile/VirtualSwitchSelectionProfile.rst


vim.profile.host.PortGroupProfile
=================================
   `PortGroupProfile`_ is the base class for the different port group subprofile objects.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0`_

Attributes:
    key (`str`_):

       Linkable identifier.
    name (`str`_):

       Name of the portgroup.
    vlan (`vim.profile.host.PortGroupProfile.VlanProfile`_):

       VLAN identifier for the port group.
    vswitch (`vim.profile.host.PortGroupProfile.VirtualSwitchSelectionProfile`_):

       Virtual switch to which the port group is connected.
    networkPolicy (`vim.profile.host.NetworkPolicyProfile`_):

       The network policy applicable on the port group.
