.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _VirtualUSBController: ../../../vim/vm/device/VirtualUSBController.rst

.. _VirtualUSBXHCIController: ../../../vim/vm/device/VirtualUSBXHCIController.rst

.. _vim.vm.device.VirtualController: ../../../vim/vm/device/VirtualController.rst


vim.vm.device.VirtualUSBXHCIController
======================================
  The `VirtualUSBXHCIController`_ data object describes a virtual USB Extensible Host Controller Interface (USB 3.0). For more informatino see `VirtualUSBController`_ .
:extends: vim.vm.device.VirtualController_
:since: `vSphere API 5.0`_

Attributes:
    autoConnectDevices (`bool`_, optional):

       Flag to indicate whether or not the ability to hot plug devices is enabled on this controller.
