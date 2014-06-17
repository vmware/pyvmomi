.. _int: https://docs.python.org/2/library/stdtypes.html

.. _str: https://docs.python.org/2/library/stdtypes.html

.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _device: ../../../vim/vm/VirtualHardware.rst#device

.. _connected: ../../../vim/vm/device/VirtualUSB.rst#connected

.. _deviceName: ../../../vim/vm/device/VirtualDevice/DeviceBackingInfo.rst#deviceName

.. _VirtualUSB: ../../../vim/vm/device/VirtualUSB.rst

.. _hardwareOptions: ../../../vim/vm/ConfigOption.rst#hardwareOptions

.. _VirtualHardware: ../../../vim/vm/VirtualHardware.rst

.. _VirtualUSBOption: ../../../vim/vm/device/VirtualUSBOption.rst

.. _QueryConfigOption: ../../../vim/EnvironmentBrowser.rst#queryConfigOption

.. _virtualDeviceOption: ../../../vim/vm/VirtualHardwareOption.rst#virtualDeviceOption

.. _VirtualUSBController: ../../../vim/vm/device/VirtualUSBController.rst

.. _VirtualDeviceConfigSpec: ../../../vim/vm/device/VirtualDeviceSpec.rst

.. _VirtualUSBUSBBackingInfo: ../../../vim/vm/device/VirtualUSB/USBBackingInfo.rst

.. _VirtualMachineUsbInfoSpeed: ../../../vim/vm/UsbInfo/Speed.rst

.. _VirtualMachineConfigOption: ../../../vim/vm/ConfigOption.rst

.. _VirtualMachineUsbInfoFamily: ../../../vim/vm/UsbInfo/Family.rst

.. _vim.vm.device.VirtualDevice: ../../../vim/vm/device/VirtualDevice.rst

.. _VirtualDeviceDeviceBackingInfo: ../../../vim/vm/device/VirtualDevice/DeviceBackingInfo.rst

.. _VirtualUSBRemoteHostBackingInfo: ../../../vim/vm/device/VirtualUSB/RemoteHostBackingInfo.rst


vim.vm.device.VirtualUSB
========================
  The `VirtualUSB`_ data object describes the USB device configuration for a virtual machine. You can attach a USB device to an ESX host. The device is available to only one virtual machine at a time. When you remove the device from the virtual machine, it becomes available to other virtual machines located on the host. You can add up to 20 USB devices to a virtual machine. Virtual USB support requires virtual machine hardware version 7 or later.The `VirtualUSB`_ object represents either a configuration to be applied to the virtual machine or the current device configuration on the virtual machine.
   * To configure a USB connection for the virtual machine, add a
   * `VirtualUSB`_
   * object to the
   * `VirtualDeviceConfigSpec`_
   * . Use USB backing (
   * `VirtualUSBUSBBackingInfo`_
   * ) to establish a connection with a virtual machine that will remain on the host to which the USB device is attached. The vSphere Server does not support vMotion for standard USB backing. To configure vMotion support for a virtual machine with a USB connection, use remote host backing for the USB connection (
   * `VirtualUSBRemoteHostBackingInfo`_
   * ).
   * To configure a USB device for a virtual machine, the virtual machine must have a USB controller. To add a controller, include a
   * `VirtualUSBController`_
   * object in the virtual device specification for your virtual machine configuration. You can add only one USB controller to a virtual machine.
   * To determine USB device configuration status for the virtual machine, check the virtual hardware device list (
   * `VirtualHardware`_
   * .
   * `device`_
   * ). The presence of the
   * `VirtualUSB`_
   * object in the hardware device list indicates that the virtual machine is configured to use a USB device. The
   * `connected`_
   * property indicates whether the virtual machine is connected to the device.To determine the USB options available on the host, use the `QueryConfigOption`_ method to retrieve the virtual machine configuration. The presence of the `VirtualUSBOption`_ object in the retrieved configuration ( `VirtualMachineConfigOption`_ . `hardwareOptions`_ . `virtualDeviceOption`_ ) indicates that the host supports USB connections.The following operations will disconnect a USB device, losing data if data transfer is in progress over the USB connection.
   * Hot add of memory, CPU, or PCI devices. A hot add operation disconnects only USB devices for virtual machines that use a local connection to the device (
   * `VirtualUSBUSBBackingInfo`_
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
    connected (`bool`_):

       Flag indicating whether the device is currently connected. The virtual machine is not connected to the device if the autoconnect pattern specified in the USB device backing ( `VirtualDeviceDeviceBackingInfo`_ . `deviceName`_ ) can not be satisfied, either because there is no such device, or the matching device is not available. Valid only while the virtual machine is running.
    vendor (`int`_, optional):

       Vendor ID of the USB device.
    product (`int`_, optional):

       Product ID of the USB device.
    family (`str`_, optional):

       Device class families. For possible values see `VirtualMachineUsbInfoFamily`_ .
    speed (`str`_, optional):

       Device speeds detected by server. For possible values see `VirtualMachineUsbInfoSpeed`_ .
