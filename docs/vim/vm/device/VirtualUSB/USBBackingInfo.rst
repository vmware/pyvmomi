.. _deviceName: ../../../../vim/vm/device/VirtualDevice/DeviceBackingInfo.rst#deviceName

.. _VI API 2.5: ../../../../vim/version.rst#vimversionversion2

.. _VirtualUSBUSBBackingInfo: ../../../../vim/vm/device/VirtualUSB/USBBackingInfo.rst

.. _vim.vm.device.VirtualDevice.DeviceBackingInfo: ../../../../vim/vm/device/VirtualDevice/DeviceBackingInfo.rst


vim.vm.device.VirtualUSB.USBBackingInfo
=======================================
  The `VirtualUSBUSBBackingInfo`_ data object identifies a USB device on the host where the virtual machine is located. This type of backing supports only a local connection where the virtual machine will remain on the host to which the USB device is attached.To identify the USB device, you specify an autoconnect pattern for the `deviceName`_ . The virtual machine can connect to the USB device if the ESX server can find a USB device described by the autoconnect pattern. The autoconnect pattern consists of name:value pairs. You can use any combination of the following fields.
   * path - USB connection path on the host
   * pid - idProduct field in the USB device descriptor
   * vid - idVendor field in the USB device descriptor
   * hostId - unique ID for the host
   * speed - device speed (low, full, or high)For example, the following pattern identifies a USB device:"path:1/3/0 hostId:44\ 45\ 4c\ 43\ 00\ 10\ 54-80\ 35\ ca\ c0\ 4f\ 4d\ 37\ 31"This pattern identifies the USB device connected to port 1/3/0 on the host with the unique id0x44454c4c430010548035cac04f4d3731.Special characters for autoconnect pattern values:
   * The name and value are separated by a colon (:).
   * Name:value pairs are separated by spaces.
   * The escape character is a backslash (\). Use a single backslash to embed a space in a value. Use a double blackslash to embed a single backslash in the value.
:extends: vim.vm.device.VirtualDevice.DeviceBackingInfo_
:since: `VI API 2.5`_

Attributes:
