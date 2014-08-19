
vim.vm.device.VirtualSriovEthernetCard
======================================
  The `VirtualSriovEthernetCard <vim/vm/device/VirtualSriovEthernetCard.rst>`_ data object defines the properties of a SR-IOV enabled Ethernet card attached to a virtual machine.
:extends: vim.vm.device.VirtualEthernetCard_
:since: `vSphere API 5.5 <vim/version.rst#vimversionversion9>`_

Attributes:
    allowGuestOSMtuChange (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether MTU can be changed from guest OS.
    sriovBacking (`vim.vm.device.VirtualSriovEthernetCard.SriovBackingInfo <vim/vm/device/VirtualSriovEthernetCard/SriovBackingInfo.rst>`_, optional):

       Information about SR-IOV passthrough backing of this VirtualSriovEthernetCard.
