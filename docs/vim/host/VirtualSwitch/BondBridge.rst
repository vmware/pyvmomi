
vim.host.VirtualSwitch.BondBridge
=================================
  This data object type describes a bridge that provides network adapter teaming capabilities.
:extends: vim.host.VirtualSwitch.Bridge_

Attributes:
    nicDevice ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       The list of keys of the physical network adapters to be bridged.
    beacon (`vim.host.VirtualSwitch.BeaconConfig <vim/host/VirtualSwitch/BeaconConfig.rst>`_, optional):

       The beacon configuration to probe for the validity of a link. If this is set, beacon probing is configured and will be used. If this is not set, beacon probing is disabled.
    linkDiscoveryProtocolConfig (`vim.host.LinkDiscoveryProtocolConfig <vim/host/LinkDiscoveryProtocolConfig.rst>`_, optional):

       The link discovery protocol configuration for the virtual switch.See `LinkDiscoveryProtocolConfig <vim/host/LinkDiscoveryProtocolConfig.rst>`_ 
