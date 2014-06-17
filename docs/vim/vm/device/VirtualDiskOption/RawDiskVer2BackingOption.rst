.. _bool: https://docs.python.org/2/library/stdtypes.html

.. _vim.option.ChoiceOption: ../../../../vim/option/ChoiceOption.rst

.. _vim.vm.device.VirtualDeviceOption.DeviceBackingOption: ../../../../vim/vm/device/VirtualDeviceOption/DeviceBackingOption.rst


vim.vm.device.VirtualDiskOption.RawDiskVer2BackingOption
========================================================
  The VirtualDiskOption.RawDiskVer2BackingOption object type contains the available options when backing a virtual disk using a host device on VMware Server.
:extends: vim.vm.device.VirtualDeviceOption.DeviceBackingOption_

Attributes:
    descriptorFileNameExtensions (`vim.option.ChoiceOption`_):

       Valid extensions for the filename of the raw disk descriptor file.
    uuid (`bool`_):

       Flag to indicate whether this backing supports disk UUID property.
