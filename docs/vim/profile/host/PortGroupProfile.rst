
vim.profile.host.PortGroupProfile
=================================
   `PortGroupProfile <vim/profile/host/PortGroupProfile.rst>`_ is the base class for the different port group subprofile objects.
:extends: vim.profile.ApplyProfile_
:since: `vSphere API 4.0 <vim/version.rst#vimversionversion5>`_

Attributes:
    key (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Linkable identifier.
    name (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the portgroup.
    vlan (`vim.profile.host.PortGroupProfile.VlanProfile <vim/profile/host/PortGroupProfile/VlanProfile.rst>`_):

       VLAN identifier for the port group.
    vswitch (`vim.profile.host.PortGroupProfile.VirtualSwitchSelectionProfile <vim/profile/host/PortGroupProfile/VirtualSwitchSelectionProfile.rst>`_):

       Virtual switch to which the port group is connected.
    networkPolicy (`vim.profile.host.NetworkPolicyProfile <vim/profile/host/NetworkPolicyProfile.rst>`_):

       The network policy applicable on the port group.
