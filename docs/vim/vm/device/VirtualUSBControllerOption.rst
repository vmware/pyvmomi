
vim.vm.device.VirtualUSBControllerOption
========================================
  The VirtualUSBControllerOption data object type contains the options for a virtual USB Host Controller Interface.
:extends: vim.vm.device.VirtualControllerOption_

Attributes:
    autoConnectDevices (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Flag to indicate whether or not the ability to autoconnect devices is enabled for this virtual USB controller.
    ehciSupported (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Flag to indicate whether or not enhanced host controller interface (USB 2.0) is available on this virtual USB controller.
    supportedSpeeds ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       Range of USB device speeds supported by this USB controller type. Acceptable values are specified at `VirtualMachineUsbInfoSpeed <vim/vm/UsbInfo/Speed.rst>`_ .
