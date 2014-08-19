vim.vm.UsbInfo.Family
=====================
  Device class family.
  :contained by: `vim.vm.UsbInfo <vim/vm/UsbInfo.rst>`_

  :type: `vim.vm.UsbInfo.Family <vim/vm/UsbInfo/Family.rst>`_

  :name: unknownFamily

values:
--------

printer
   Printer device.

hub
   USB hubs.

communication
   Communication device.

storage
   Mass storage device.

wusb
   Wireless device related to the Wireless USB standard, this is a subset of wireless controllers,

vendor_specific
   Device that has an interface using a vendor-specific protocol.

bluetooth
   Standard bluetooth adapter that uses HCI protocol, this is a subset of wireless controllers.

wireless
   Wireless controller.

other
   Other miscellaneous device.

hid
   Human interface device.

imaging
   Still imaging device.

hid_bootable
   Bootable human interface device, this is a subset of HID devices.

unknownFamily
   There was an error in determining this device's classes accurately.

video
   Video device.

smart_card
   Smart card device.

audio
   Audio capable device.

security
   Content security device.

pda
   Palm PDA, and Micorsoft ActiveSync PDA.

physical
   Physical interface device.
