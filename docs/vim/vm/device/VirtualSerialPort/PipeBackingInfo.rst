
vim.vm.device.VirtualSerialPort.PipeBackingInfo
===============================================
  The `VirtualSerialPortPipeBackingInfo <vim/vm/device/VirtualSerialPort/PipeBackingInfo.rst>`_ data object defines information for backing a `VirtualSerialPort <vim/vm/device/VirtualSerialPort.rst>`_ with a named pipe. You can use a pipe to connect a virtual serial port to a host application or to another virtual machine on the host computer. This is useful for capturing debugging information sent through the virtual serial port.
:extends: vim.vm.device.VirtualDevice.PipeBackingInfo_

Attributes:
    endpoint (`str <https://docs.python.org/2/library/stdtypes.html>`_):

       Indicates the role the virtual machine assumes as an endpoint for the pipe. The valid values are "client" or "server".
    noRxLoss (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Enables optimized data transfer over the pipe. When you use this feature, the ESX server buffers data to prevent data overrun. This allows the virtual machine to read all of the data transferred over the pipe with no data loss. To use optimized data transfer, setnoRxLosstotrue. To disable this feature, set the property tofalse.This property is optional. If this property is not set, the ESX server uses the default value specified in the pipe backing options (noRxLoss.defaultValue - see `noRxLoss <vim/vm/device/VirtualSerialPortOption/PipeBackingOption.rst#noRxLoss>`_ in the pipe backing option object).To use this property, optimized data transfer must be supported on the host. (See `noRxLoss <vim/vm/device/VirtualSerialPortOption/PipeBackingOption.rst#noRxLoss>`_ in the pipe backing option object.) If the ESX server does not support the option, it ignores thenoRxLosssetting in the pipe backing information object.Note: You can use this feature even if the other end of the pipe is not an application, but this is more likely to fail.
