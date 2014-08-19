
vim.vm.device.VirtualDeviceOption.DeviceBackingOption
=====================================================
  The DeviceBackingOption data class contains device-specific backing options.
:extends: vim.vm.device.VirtualDeviceOption.BackingOption_

Attributes:
    autoDetectAvailable (`vim.option.BoolOption <vim/option/BoolOption.rst>`_):

       Flag to indicate whether the specific instance of this device can be auto-detected on the host instead of having to specify a particular physical device.
