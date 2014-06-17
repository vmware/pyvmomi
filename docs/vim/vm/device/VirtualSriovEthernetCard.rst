.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.5: ../../../vim/version.rst#vimversionversion9

.. _VirtualSriovEthernetCard: ../../../vim/vm/device/VirtualSriovEthernetCard.rst

.. _vim.vm.device.VirtualEthernetCard: ../../../vim/vm/device/VirtualEthernetCard.rst

.. _vim.vm.device.VirtualSriovEthernetCard.SriovBackingInfo: ../../../vim/vm/device/VirtualSriovEthernetCard/SriovBackingInfo.rst


vim.vm.device.VirtualSriovEthernetCard
======================================
  The `VirtualSriovEthernetCard`_ data object defines the properties of a SR-IOV enabled Ethernet card attached to a virtual machine.
:extends: vim.vm.device.VirtualEthernetCard_
:since: `vSphere API 5.5`_

Attributes:
    allowGuestOSMtuChange (`bool`_, optional):

       Indicates whether MTU can be changed from guest OS.
    sriovBacking (`vim.vm.device.VirtualSriovEthernetCard.SriovBackingInfo`_, optional):

       Information about SR-IOV passthrough backing of this VirtualSriovEthernetCard.
