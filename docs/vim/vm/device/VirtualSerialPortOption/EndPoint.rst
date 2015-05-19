.. _endpoint: ../../../../vim/vm/device/VirtualSerialPortOption/PipeBackingOption.rst#endpoint

.. _VirtualSerialPortEndPoint: ../../../../vim/vm/device/VirtualSerialPortOption/EndPoint.rst

.. _vim.vm.device.VirtualSerialPortOption: ../../../../vim/vm/device/VirtualSerialPortOption.rst

.. _vim.vm.device.VirtualSerialPortOption.EndPoint: ../../../../vim/vm/device/VirtualSerialPortOption/EndPoint.rst

vim.vm.device.VirtualSerialPortOption.EndPoint
==============================================
  The `VirtualSerialPortEndPoint`_ enum defines endpoint values for virtual serial port pipe backing. When you use serial port pipe backing to connect a virtual machine to another process, you must define the endpoints. See the `endpoint`_ property for the virtual serial port pipe backing information data object.The possible endpoint values are:
   * client
   * server
   * 
   * For the supported choices, see the
   * `endpoint`_
   * property for the virtual serial port pipe backing option data object.
  :contained by: `vim.vm.device.VirtualSerialPortOption`_

  :type: `vim.vm.device.VirtualSerialPortOption.EndPoint`_

  :name: server

values:
--------

client
   client

server
   server
