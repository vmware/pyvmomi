.. _vim.option.ChoiceOption: ../../../../vim/option/ChoiceOption.rst

.. _vim.vm.device.VirtualDeviceOption.BackingOption: ../../../../vim/vm/device/VirtualDeviceOption/BackingOption.rst


vim.vm.device.VirtualDeviceOption.FileBackingOption
===================================================
  The FileBackingOption data class contains file-specific backing options.
:extends: vim.vm.device.VirtualDeviceOption.BackingOption_

Attributes:
    fileNameExtensions (`vim.option.ChoiceOption`_, optional):

       Valid filename extension for the filename. If no extensions are present, any file extension is acceptable.
