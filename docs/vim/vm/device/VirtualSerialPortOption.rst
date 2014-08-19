
vim.vm.device.VirtualSerialPortOption
=====================================
  The `VirtualSerialPortOption <vim/vm/device/VirtualSerialPortOption.rst>`_ data object contains the options for configuring the virtual serial port device defined by the `VirtualSerialPort <vim/vm/device/VirtualSerialPort.rst>`_ data object. These options include information about how the device is backed physically on the host: by a network socket, a host file, a host serial port device, or a pipe to another process.
:extends: vim.vm.device.VirtualDeviceOption_

Attributes:
    yieldOnPoll (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Indicates whether the virtual machine supports the CPU yield option during virtual serial port polling. When this feature is supported and enabled, the virtual machine will periodically relinquish the processor if its sole task is polling the virtual serial port.IfyieldOnPoll.supportedisfalse, the virtual machine ignores the virtual serial port object setting for `yieldOnPoll <vim/vm/device/VirtualSerialPort.rst#yieldOnPoll>`_ .
