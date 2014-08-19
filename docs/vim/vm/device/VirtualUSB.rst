
vim.vm.device.VirtualUSB
========================
  The `VirtualUSB <vim/vm/device/VirtualUSB.rst>`_ data object describes the USB device configuration for a virtual machine. You can attach a USB device to an ESX host. The device is available to only one virtual machine at a time. When you remove the device from the virtual machine, it becomes available to other virtual machines located on the host. You can add up to 20 USB devices to a virtual machine. Virtual USB support requires virtual machine hardware version 7 or later.The `VirtualUSB <vim/vm/device/VirtualUSB.rst>`_ object represents either a configuration to be applied to the virtual machine or the current device configuration on the virtual machine.
   * To configure a USB connection for the virtual machine, add a
   * `VirtualUSB <vim/vm/device/VirtualUSB.rst>`_
   * object to the
   * `VirtualDeviceConfigSpec <vim/vm/device/VirtualDeviceSpec.rst>`_
   * . Use USB backing (
   * `VirtualUSBUSBBackingInfo <vim/vm/device/VirtualUSB/USBBackingInfo.rst>`_
   * ) to establish a connection with a virtual machine that will remain on the host to which the USB device is attached. The vSphere Server does not support vMotion for standard USB backing. To configure vMotion support for a virtual machine with a USB connection, use remote host backing for the USB connection (
   * `VirtualUSBRemoteHostBackingInfo <vim/vm/device/VirtualUSB/RemoteHostBackingInfo.rst>`_
   * ).
   * To configure a USB device for a virtual machine, the virtual machine must have a USB controller. To add a controller, include a
   * `VirtualUSBController <vim/vm/device/VirtualUSBController.rst>`_
   * object in the virtual device specification for your virtual machine configuration. You can add only one USB controller to a virtual machine.
   * To determine USB device configuration status for the virtual machine, check the virtual hardware device list (
   * `VirtualHardware <vim/vm/VirtualHardware.rst>`_
   * .
   * `device <vim/vm/VirtualHardware.rst#device>`_
   * ). The presence of the
   * `VirtualUSB <vim/vm/device/VirtualUSB.rst>`_
   * object in the hardware device list indicates that the virtual machine is configured to use a USB device. The
   * `connected <vim/vm/device/VirtualUSB.rst#connected>`_
   * property indicates whether the virtual machine is connected to the device.To determine the USB options available on the host, use the `QueryConfigOption <vim/EnvironmentBrowser.rst#queryConfigOption>`_ method to retrieve the virtual machine configuration. The presence of the `VirtualUSBOption <vim/vm/device/VirtualUSBOption.rst>`_ object in the retrieved configuration ( `VirtualMachineConfigOption <vim/vm/ConfigOption.rst>`_ . `hardwareOptions <vim/vm/ConfigOption.rst#hardwareOptions>`_ . `virtualDeviceOption <vim/vm/VirtualHardwareOption.rst#virtualDeviceOption>`_ ) indicates that the host supports USB connections.The following operations will disconnect a USB device, losing data if data transfer is in progress over the USB connection.
   * Hot add of memory, CPU, or PCI devices. A hot add operation disconnects only USB devices for virtual machines that use a local connection to the device (
   * `VirtualUSBUSBBackingInfo <vim/vm/device/VirtualUSB/USBBackingInfo.rst>`_
   * ).
   * Suspend and resume on a virtual machine.
   * vMotion of a virtual machine with a USB connection, if you are not using remote host USB backing.
   * 
   * The following services do not support USB connections.
   * 
   * Fault Tolerance virtual machines cannot use USB devices.
   * DPM (Distributed Power Management) will put a host into standby, regardless of any connections to USB devices on the host.
   * DRS (Distributed Resource Scheduling) may power-off hosts that have USB connections to virtual machines.
:extends: vim.vm.device.VirtualDevice_

Attributes:
    connected (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Flag indicating whether the device is currently connected. The virtual machine is not connected to the device if the autoconnect pattern specified in the USB device backing ( `VirtualDeviceDeviceBackingInfo <vim/vm/device/VirtualDevice/DeviceBackingInfo.rst>`_ . `deviceName <vim/vm/device/VirtualDevice/DeviceBackingInfo.rst#deviceName>`_ ) can not be satisfied, either because there is no such device, or the matching device is not available. Valid only while the virtual machine is running.
    vendor (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Vendor ID of the USB device.
    product (`int <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Product ID of the USB device.
    family ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Device class families. For possible values see `VirtualMachineUsbInfoFamily <vim/vm/UsbInfo/Family.rst>`_ .
    speed ([`str <https://docs.python.org/2/library/stdtypes.html>`_], optional):

       Device speeds detected by server. For possible values see `VirtualMachineUsbInfoSpeed <vim/vm/UsbInfo/Speed.rst>`_ .
