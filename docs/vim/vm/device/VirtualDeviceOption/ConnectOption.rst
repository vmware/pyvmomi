.. _vmodl.DynamicData: ../../../../vmodl/DynamicData.rst

.. _vim.option.BoolOption: ../../../../vim/option/BoolOption.rst


vim.vm.device.VirtualDeviceOption.ConnectOption
===============================================
  The ConnectOption data object type contains information about options for connectable virtual devices.
:extends: vmodl.DynamicData_

Attributes:
    startConnected (`vim.option.BoolOption`_):

       Flag to indicate whether or not the device supports the startConnected feature.
    allowGuestControl (`vim.option.BoolOption`_):

       Flag to indicate whether or not the device can be connected and disconnected from within the guest operating system.
