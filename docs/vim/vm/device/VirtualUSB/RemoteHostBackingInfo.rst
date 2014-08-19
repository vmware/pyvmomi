
vim.vm.device.VirtualUSB.RemoteHostBackingInfo
==============================================
  The `VirtualUSBRemoteHostBackingInfo <vim/vm/device/VirtualUSB/RemoteHostBackingInfo.rst>`_ data object identifies a host and a USB device that is attached to the host. Use this object to configure support for persistent access to the USB device when vMotion operations migrate a virtual machine to a different host. The vCenter Server will not migrate the virtual machine to a host that does not support the USB remote host backing capability.Specify remote host backing as part of the USB device configuration when you create or reconfigure a virtual machine ( `VirtualMachineConfigSpec <vim/vm/ConfigSpec.rst>`_ . `deviceChange <vim/vm/ConfigSpec.rst#deviceChange>`_ . `device <vim/vm/device/VirtualDeviceSpec.rst#device>`_ . `backing <vim/vm/device/VirtualDevice.rst#backing>`_ ).To identify the USB device, you specify an autoconnect pattern for the `deviceName <vim/vm/device/VirtualDevice/DeviceBackingInfo.rst#deviceName>`_ . The virtual machine can connect to the USB device if the ESX server can find a USB device described by the autoconnect pattern. The autoconnect pattern consists of name:value pairs. You can use any combination of the following fields.
   * path - USB connection path on the host
   * pid - idProduct field in the USB device descriptor
   * vid - idVendor field in the USB device descriptor
   * hostId - unique ID for the host
   * speed - device speed (low, full, or high)For example, the following pattern identifies a USB device:"path:1/3/0 hostId:44\ 45\ 4c\ 43\ 00\ 10\ 54-80\ 35\ ca\ c0\ 4f\ 4d\ 37\ 31"This pattern identifies the USB device connected to port 1/3/0 on the host with the unique id0x44454c4c430010548035cac04f4d3731.Special characters for autoconnect pattern values:
   * The name and value are separated by a colon (:).
   * Name:value pairs are separated by spaces.
   * The escape character is a backslash (\). Use a single backslash to embed a space in a value. Use a double blackslash to embed a single backslash in the value.
:extends: vim.vm.device.VirtualDevice.DeviceBackingInfo_
:since: `vSphere API 4.1 <vim/version.rst#vimversionversion6>`_

Attributes:
    hostname (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Name of the ESX host to which the physical USB device is attached ( `HostSystem <vim/HostSystem.rst>`_ . `name <vim/ManagedEntity.rst#name>`_ ). When you configure remote host backing, hostname must identify the local host on which the virtual machine is running.
