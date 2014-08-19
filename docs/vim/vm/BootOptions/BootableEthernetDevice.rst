
vim.vm.BootOptions.BootableEthernetDevice
=========================================
  Bootable ethernet adapter. PXE boot is attempted from the device.
:extends: vim.vm.BootOptions.BootableDevice_
:since: `vSphere API 5.0 <vim/version.rst#vimversionversion7>`_

Attributes:
    deviceKey (`int <https://docs.python.org/2/library/stdtypes.html>`_):

        `Key <vim/vm/device/VirtualDevice.rst#key>`_ property of the bootable ethernet adapter.
