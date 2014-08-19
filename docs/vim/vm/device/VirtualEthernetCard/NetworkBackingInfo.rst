
vim.vm.device.VirtualEthernetCard.NetworkBackingInfo
====================================================
  The `VirtualEthernetCardNetworkBackingInfo <vim/vm/device/VirtualEthernetCard/NetworkBackingInfo.rst>`_ data object defines network backing for a virtual Ethernet card.
:extends: vim.vm.device.VirtualDevice.DeviceBackingInfo_

Attributes:
    network (`vim.Network <vim/Network.rst>`_, optional):

       Reference to the network managed object to which this backing applies. This is not used during configuration.
    inPassthroughMode (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       
