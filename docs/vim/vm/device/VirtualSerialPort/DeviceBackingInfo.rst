.. _status: ../../../../vim/vm/device/VirtualDevice/ConnectInfo.rst#status

.. _VirtualSerialPort: ../../../../vim/vm/device/VirtualSerialPort.rst

.. _VirtualSerialPortDeviceBackingInfo: ../../../../vim/vm/device/VirtualSerialPort/DeviceBackingInfo.rst

.. _vim.vm.device.VirtualDevice.DeviceBackingInfo: ../../../../vim/vm/device/VirtualDevice/DeviceBackingInfo.rst


vim.vm.device.VirtualSerialPort.DeviceBackingInfo
=================================================
  The `VirtualSerialPortDeviceBackingInfo`_ data object defines information for using a host serial port device as backing for a `VirtualSerialPort`_ . On a host, the first virtual machine to configure physical device backing for a virtual serial port will obtain the mapping. As long as that machine maintains the backing, any additional attempts to configure backing using that device will fail (a recoverable error, see the connection info `status`_ ).
:extends: vim.vm.device.VirtualDevice.DeviceBackingInfo_

Attributes:
