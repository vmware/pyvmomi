
vim.vm.device.VirtualSerialPortOption.PipeBackingOption
=======================================================
  The `VirtualSerialPortPipeBackingOption <vim/vm/device/VirtualSerialPortOption/PipeBackingOption.rst>`_ data object contains the options for backing a serial port device with a pipe to another process.
:extends: vim.vm.device.VirtualDeviceOption.PipeBackingOption_

Attributes:
    endpoint (`vim.option.ChoiceOption <vim/option/ChoiceOption.rst>`_):

       Indicates the choices available and the default setting for the pipe endpoint. As an endpoint, the virtual machine can act as a client or a server.
    noRxLoss (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Indicates whether the server supports optimized data transfer over the pipe and also specifies default behavior.When this feature is supported and enabled, the server buffers data to prevent data overrun. This allows the virtual machine to read all of the data transferred over the pipe with no data loss.If optimized data transfer is supported (noRxLoss.supportedistrue):
        * You can enable (or disable) the feature explicitly by setting the
        * `noRxLoss <vim/vm/device/VirtualSerialPort/PipeBackingInfo.rst#noRxLoss>`_
        * property on the pipe backing information object.
        * If you do not set the
        * `noRxLoss <vim/vm/device/VirtualSerialPort/PipeBackingInfo.rst#noRxLoss>`_
        * property on the the pipe backing information object, the server enables optimized data transfer if the
        * noRxLoss.defaultValue
        * property on the pipe backing options object is
        * true
        * .
        * 
        * If
        * noRxLoss.supported
        * is
        * false
        * , the server ignores the optimization settings.
        * 
        * Note
        * : You can use this feature even if the other end of the pipe is not an application, but it is more likely to fail.
