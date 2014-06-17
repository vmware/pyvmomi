.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.Network: ../../../../vim/Network.rst

.. _VirtualEthernetCardNetworkBackingInfo: ../../../../vim/vm/device/VirtualEthernetCard/NetworkBackingInfo.rst

.. _vim.vm.device.VirtualDevice.DeviceBackingInfo: ../../../../vim/vm/device/VirtualDevice/DeviceBackingInfo.rst


vim.vm.device.VirtualEthernetCard.NetworkBackingInfo
====================================================
  The `VirtualEthernetCardNetworkBackingInfo`_ data object defines network backing for a virtual Ethernet card.
:extends: vim.vm.device.VirtualDevice.DeviceBackingInfo_

Attributes:
    network (`vim.Network`_, optional):

       Reference to the network managed object to which this backing applies. This is not used during configuration.
    inPassthroughMode (`bool`_, optional):

       
