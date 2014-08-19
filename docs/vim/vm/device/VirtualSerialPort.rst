
vim.vm.device.VirtualSerialPort
===============================
  The `VirtualSerialPort <vim/vm/device/VirtualSerialPort.rst>`_ data object represents a serial port on a virtual machine. A virtual serial port uses one of the following backing types to specify how the virtual machine performs serial port operations.
   * Network backing (
   * `VirtualSerialPortURIBackingInfo <vim/vm/device/VirtualSerialPort/URIBackingInfo.rst>`_
   * ) supports a connection between the virtual machine and a resource on the network. The virtual machine can initiate a connection with the network resource, or it can listen for connections originating from the network.
   * Pipe backing (
   * `VirtualSerialPortPipeBackingInfo <vim/vm/device/VirtualSerialPort/PipeBackingInfo.rst>`_
   * ) supports I/O through a named pipe. The pipe connects the virtual machine to a host application or a virtual machine on the same host.
   * File backing (
   * `VirtualSerialPortFileBackingInfo <vim/vm/device/VirtualSerialPort/FileBackingInfo.rst>`_
   * ) supports output through the virtual serial port to a file on the same host.
   * Physical serial port backing (
   * `VirtualSerialPortDeviceBackingInfo <vim/vm/device/VirtualSerialPort/DeviceBackingInfo.rst>`_
   * ) supports a connection between the virtual machine and a device that is connected to a physical serial port on the host.
   * ThinPrint backing (
   * `VirtualSerialPortThinPrintBackingInfo <vim/vm/device/VirtualSerialPort/ThinPrintBackingInfo.rst>`_
   * ) provides driver-free printing.
   * 
   * When you use network backing, you can also configure a virtual serial port to use a virtual serial port concentrator. The virtual machine initiates a telnet connection with the concentrator, and the concentrator acts as a proxy between the virtual machine and a system on the network. By using a virtual serial port concentrator, you can maintain the connection between the virtual machine and the network resource when a vMotion event moves the virtual machine from one host to another. Without a virtual serial port concentrator, the connection would be lost. For information about using a serial port concentrator, see
   * Using a Proxy with vSphere Virtual Serial Ports
   * .
   * You can configure a virtual serial port when you create or reconfigure a virtual machine. For example, to create a virtual serial port with network backing, use the following sequence of operations. In this procedure, the virtual serial port uses a proxy and will accept a network connection.
   * 
   * Use the
   * `QueryConfigOption <vim/EnvironmentBrowser.rst#queryConfigOption>`_
   * method to determine the backing options that are available on a host. The method returns a
   * `VirtualMachineConfigOption <vim/vm/ConfigOption.rst>`_
   * data object. The virtual machine configuration data includes a list of backing options (
   * `backingOption <vim/vm/device/VirtualDeviceOption.rst#backingOption>`_
   * ). The following pseudocode shows the path to the backing options.
   * 
   * `VirtualMachineConfigOption <vim/vm/ConfigOption.rst>`_
   * .hardwareOptions.VirtualDeviceOption[].backingOption[]
   * 
   * The array of virtual device options can include a virtual serial port (
   * `VirtualSerialPortOption <vim/vm/device/VirtualSerialPortOption.rst>`_
   * ). The array of serial port backing options can include URI, file, pipe, or device backing options.
   * Use the
   * `CreateVM_Task <vim/Folder.rst#createVm>`_
   * method (or the
   * `CreateChildVM_Task <vim/ResourcePool.rst#createVm>`_
   * method) to create the virtual machine and configure the virtual serial port backing. Create a
   * `VirtualMachineConfigSpec <vim/vm/ConfigSpec.rst>`_
   * data object and nested data objects for the method's
   * config
   * parameter. The following pseudocode shows the resulting path to the backing information.
   * 
   * `VirtualMachineConfigSpec <vim/vm/ConfigSpec.rst>`_
   * .deviceChange[].device.backing
   * 
   * Set the direction property to "server" to direct the virtual machine to accept a connection. Set the serviceURI property to the URI for the host on which the virtual machine runs.
   * If you use physical device backing (
   * `VirtualSerialPortDeviceBackingOption <vim/vm/device/VirtualSerialPortOption/DeviceBackingOption.rst>`_
   * ), you should also use the
   * `QueryConfigTarget <vim/EnvironmentBrowser.rst#queryConfigTarget>`_
   * method to determine if a serial device is available before configuring device backing.
:extends: vim.vm.device.VirtualDevice_

Attributes:
    yieldOnPoll (`bool <https://docs.python.org/2/library/stdtypes.html>`_):

       Enables CPU yield behavior. If you setyieldOnPolltotrue, the virtual machine will periodically relinquish the processor if its sole task is polling the virtual serial port. The amount of time it takes to regain the processor will depend on the degree of other virtual machine activity on the host.To use this property, the CPU yield option must be supported. (See the `yieldOnPoll <vim/vm/device/VirtualSerialPortOption.rst#yieldOnPoll>`_ property for the virtual serial port option object.)
