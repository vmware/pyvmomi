.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vSphere API 5.0: ../../../vim/version.rst#vimversionversion7

.. _vim.option.BoolOption: ../../../vim/option/BoolOption.rst

.. _VirtualMachineUsbInfoSpeed: ../../../vim/vm/UsbInfo/Speed.rst

.. _vim.vm.device.VirtualControllerOption: ../../../vim/vm/device/VirtualControllerOption.rst


vim.vm.device.VirtualUSBXHCIControllerOption
============================================
  The VirtualUSBXHCIControllerOption data object type contains the options for a virtual USB Extensible Host Controller Interface (USB 3.0).
:extends: vim.vm.device.VirtualControllerOption_
:since: `vSphere API 5.0`_

Attributes:
    autoConnectDevices (`vim.option.BoolOption`_):

       Flag to indicate whether or not the ability to autoconnect devices is enabled for this virtual USB controller.
    supportedSpeeds (`str`_):

       Range of USB device speeds supported by this USB controller type. Acceptable values are specified at `VirtualMachineUsbInfoSpeed`_ .
