
vim.vm.device.VirtualUSBXHCIController
======================================
  The `VirtualUSBXHCIController <vim/vm/device/VirtualUSBXHCIController.rst>`_ data object describes a virtual USB Extensible Host Controller Interface (USB 3.0). For more informatino see `VirtualUSBController <vim/vm/device/VirtualUSBController.rst>`_ .
:extends: vim.vm.device.VirtualController_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    autoConnectDevices (`bool <https://docs.python.org/2/library/stdtypes.html>`_, optional):

       Flag to indicate whether or not the ability to hot plug devices is enabled on this controller.
