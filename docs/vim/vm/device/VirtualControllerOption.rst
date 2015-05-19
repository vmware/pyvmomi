.. _str: https://docs.python.org/2/library/stdtypes.html

.. _vim.option.IntOption: ../../../vim/option/IntOption.rst

.. _vim.vm.device.VirtualDeviceOption: ../../../vim/vm/device/VirtualDeviceOption.rst


vim.vm.device.VirtualControllerOption
=====================================
  The VirtualControllerOption data object type contains information about a virtual controller type.
:extends: vim.vm.device.VirtualDeviceOption_

Attributes:
    devices (`vim.option.IntOption`_):

       The minimum and maximum number of devices this controller can control at run time.
    supportedDevice ([`str`_], optional):

       Array of supported device options for this controller.
