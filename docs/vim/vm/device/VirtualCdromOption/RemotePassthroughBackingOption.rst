.. _vim.option.BoolOption: ../../../../vim/option/BoolOption.rst

.. _vim.vm.device.VirtualDeviceOption.RemoteDeviceBackingOption: ../../../../vim/vm/device/VirtualDeviceOption/RemoteDeviceBackingOption.rst


vim.vm.device.VirtualCdromOption.RemotePassthroughBackingOption
===============================================================
  The VirtualCdromOption.RemotePassthroughBackingOption data object type contains the options for a remote pass-through CD-ROM device backing.Note that the server cannot present a list of valid remote backing devices because it is unable to scan remote hosts.
:extends: vim.vm.device.VirtualDeviceOption.RemoteDeviceBackingOption_

Attributes:
    exclusive (`vim.option.BoolOption`_):

       Flag to indicate whether or not exclusive CD-ROM device access is supported.
