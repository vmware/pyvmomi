
vim.vm.device.VirtualUSBXHCIControllerOption
============================================
  The VirtualUSBXHCIControllerOption data object type contains the options for a virtual USB Extensible Host Controller Interface (USB 3.0).
:extends: vim.vm.device.VirtualControllerOption_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    autoConnectDevices (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Flag to indicate whether or not the ability to autoconnect devices is enabled for this virtual USB controller.
    supportedSpeeds ([`str <https://docs.python.org/2/library/stdtypes.html>`_]):

       Range of USB device speeds supported by this USB controller type. Acceptable values are specified at `VirtualMachineUsbInfoSpeed <vim/vm/UsbInfo/Speed.rst>`_ .
