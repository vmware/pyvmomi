.. _vim.option.BoolOption: ../../../../vim/option/BoolOption.rst

.. _vim.vm.device.VirtualDeviceOption.BackingOption: ../../../../vim/vm/device/VirtualDeviceOption/BackingOption.rst


vim.vm.device.VirtualDeviceOption.RemoteDeviceBackingOption
===========================================================
  VirtualDeviceOption.RemoteDeviceBackingOption describes the options for a remote device backing. The primary difference between a remote device backing and a local device backing is that the VirtualCenter server cannot provide a list of remote host devices available for this virtual device backing.
:extends: vim.vm.device.VirtualDeviceOption.BackingOption_

Attributes:
    autoDetectAvailable (`vim.option.BoolOption`_):

       Flag to indicate whether the specific instance of this device can be auto-detected on the host instead of having to specify a particular physical device.
