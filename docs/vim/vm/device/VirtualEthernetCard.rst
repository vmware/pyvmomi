
vim.vm.device.VirtualEthernetCard
=================================
  The `VirtualEthernetCard <vim/vm/device/VirtualEthernetCard.rst>`_ data object contains the properties of an Ethernet adapter attached to a virtual machine.
:extends: vim.vm.device.VirtualDevice_

Attributes:
    addressType (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       MAC address type.Valid values for address type are:ManualStatically assigned MAC address.GeneratedAutomatically generated MAC address.AssignedMAC address assigned by VirtualCenter.
    macAddress (`str <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       MAC address assigned to the virtual network adapter. Clients can set this property to any of the allowed address types. The server might override the specified value for "Generated" or "Assigned" if it does not fall in the right ranges or is determined to be a duplicate.
    wakeOnLanEnabled (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Indicates whether wake-on-LAN is enabled on this virtual network adapter. Clients can set this property to selectively enable or disable wake-on-LAN.
