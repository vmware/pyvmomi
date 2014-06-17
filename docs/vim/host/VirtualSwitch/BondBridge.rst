.. _str: https://docs.python.org/2/library/stdtypes.html

.. _LinkDiscoveryProtocolConfig: ../../../vim/host/LinkDiscoveryProtocolConfig.rst

.. _vim.host.VirtualSwitch.Bridge: ../../../vim/host/VirtualSwitch/Bridge.rst

.. _vim.host.VirtualSwitch.BeaconConfig: ../../../vim/host/VirtualSwitch/BeaconConfig.rst

.. _vim.host.LinkDiscoveryProtocolConfig: ../../../vim/host/LinkDiscoveryProtocolConfig.rst


vim.host.VirtualSwitch.BondBridge
=================================
  This data object type describes a bridge that provides network adapter teaming capabilities.
:extends: vim.host.VirtualSwitch.Bridge_

Attributes:
    nicDevice (`str`_):

       The list of keys of the physical network adapters to be bridged.
    beacon (`vim.host.VirtualSwitch.BeaconConfig`_, optional):

       The beacon configuration to probe for the validity of a link. If this is set, beacon probing is configured and will be used. If this is not set, beacon probing is disabled.
    linkDiscoveryProtocolConfig (`vim.host.LinkDiscoveryProtocolConfig`_, optional):

       The link discovery protocol configuration for the virtual switch.See `LinkDiscoveryProtocolConfig`_ 
